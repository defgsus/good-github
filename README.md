## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-06-03](docs/good-messages/2023/2023-06-03.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,719,363 were push events containing 2,565,199 commit messages that amount to 162,861,497 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 47 messages:


## [rr-codes/WebKit](https://github.com/rr-codes/WebKit)@[d6ae2528a9...](https://github.com/rr-codes/WebKit/commit/d6ae2528a9f3819005e08f9d5091ceff8b880fa8)
#### Saturday 2023-06-03 00:11:01 by Dean Jackson

WebXR: Severe aliasing in WebXR experiences (with WebGL1 contexts)
https://bugs.webkit.org/show_bug.cgi?id=256861
rdar://109424254

Reviewed by Dan Glastonbury.

WebXR sessions using WebGL1 contexts are unable to turn on
multisampling. I'm pretty sure this was my fault, but I can't
remember if it was intentional or a mistake. Either way it is
a bug.

Fix this by implementing the multisample renderbuffer creation
and resolution steps. Since we're doing this on a WebGL1 context,
the normal API will be invalid (it requires GLES3), so call the
extension API instead. This means we need to expose some extra methods
on GraphicsContextGL.

Lastly, the framebuffer textures we get are SRGB8_ALPHA8 which
requires an extension to be enabled with a WebGL1 context when
we're talking to an XR-compatible context. Similarly, we
enable the extension to allow multisampled framebuffers.

* Source/WebCore/Modules/webxr/WebXROpaqueFramebuffer.cpp:
(WebCore::WebXROpaqueFramebuffer::endFrame): call blitFramebufferANGLE.
(WebCore::WebXROpaqueFramebuffer::setupFramebuffer): Implement logic for WebGL 1.
* Source/WebCore/platform/graphics/GraphicsContextGL.h:
* Source/WebCore/platform/graphics/angle/GraphicsContextGLANGLE.cpp: Implement the extension API/
(WebCore::GraphicsContextGLANGLE::renderbufferStorageMultisampleANGLE):
(WebCore::GraphicsContextGLANGLE::blitFramebufferANGLE):
* Source/WebCore/platform/graphics/angle/GraphicsContextGLANGLE.h:
* Source/WebCore/platform/graphics/cocoa/GraphicsContextGLCocoa.mm:
(WebCore::GraphicsContextGLCocoa::platformInitialize): Turn on the sRGB extension.
* Source/WebKit/GPUProcess/graphics/RemoteGraphicsContextGL.messages.in:
* Source/WebKit/GPUProcess/graphics/RemoteGraphicsContextGLFunctionsGenerated.h:
(renderbufferStorageMultisampleANGLE):
(blitFramebufferANGLE):
* Source/WebKit/WebProcess/GPU/graphics/RemoteGraphicsContextGLProxy.h:
* Source/WebKit/WebProcess/GPU/graphics/RemoteGraphicsContextGLProxyFunctionsGenerated.cpp:
(WebKit::RemoteGraphicsContextGLProxy::renderbufferStorageMultisampleANGLE):
(WebKit::RemoteGraphicsContextGLProxy::blitFramebufferANGLE):

Canonical link: https://commits.webkit.org/264838@main

---
## [openai/evals](https://github.com/openai/evals)@[14812f717c...](https://github.com/openai/evals/commit/14812f717c77171e83d48f648a7f878c76b94478)
#### Saturday 2023-06-03 00:25:37 by Andrew

Update eval-templates.md (#1090)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

[Insert Eval name here]

### Eval description

[Insert a short description of what your eval does here]

### What makes this a useful eval?

[Insert why this eval is worth including and any additional context]

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [ ] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [ ] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [ ] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [ ] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [ ] Check that your data is in `evals/registry/data/{name}`
- [ ] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [ ] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (<https://platform.openai.com/docs/usage-policies>).

- [ ] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [ ] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [ ] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [ ] I have filled out all required fields of this form
- [ ] I have used **Git LFS** for the Eval JSON data
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
  INSERT_EVAL_HERE
  ```
</details>

---
## [MiniFalafel/Mellow](https://github.com/MiniFalafel/Mellow)@[ff5504f455...](https://github.com/MiniFalafel/Mellow/commit/ff5504f455a04e435f9a6e5dea11edd7b3c01f19)
#### Saturday 2023-06-03 00:54:42 by Eli Sanders

This is so scuffed

Haven't worked on this in a while so I wanted to check it out. Ended up making some changes to some pretty obviously fucked up code. and adding some features.

 - Revised Camera Controller. Now has a toggle for an "active state".
 - Active state toggles call a callback that can be set by the user. In the example, I made it show/hide the mouse, but it could be used for something else, like pausing the physics or something... I guess?
 - Fixed some scuffed if/else statements replacing them with slightly less scuffed code that isn't as repetitive and works the same aside from normalizing the movement direction vector, which should have should have been happening before ANYWAY.
 - Made it so that the mouse sensitivity in the camera controller actually does something along with the movement speed.
 - Changed the way that keybinds for the cam controller work because the old way was sketchy as hell. This new one is more expandable for stuff in the future I guess.
 - Added a basic ass lighting test thing, meaning now there are more controls in the uniform control panel thingy (I forgot what it's called and I don't want to go and look). That's about it. It looks better now I guess.

Overall just the camera controller is a little more robust.

---
## [KingNeoNewRenaissanceMovement/ExceptionalMindGame](https://github.com/KingNeoNewRenaissanceMovement/ExceptionalMindGame)@[794e2f973c...](https://github.com/KingNeoNewRenaissanceMovement/ExceptionalMindGame/commit/794e2f973cce4d9449310744afd71ac53d77b51a)
#### Saturday 2023-06-03 01:25:03 by KingNeoNewRenaissanceMovement

Update README.md

Introduction
What follows is the reasonable manner and conditions to use the Creative Commons license mentioned above. To be crystal clear, a license is a simple agreement or contract between two reasonable persons, who act in good faith to agree their wills regards to the thing and the price. The two reasonable persons here are: “the licensor” (Charles Kocian as the author of the “license material”), who makes a contract with “the licensee”, (the person who is going to use the “license material” to make its own artistic creations). In this case the thing, is the “license material”. It is the text of 94 philosophical questions and its 94 short answers. The short answers are part of a book called Champion’s Renaissance and the philosophical questions are the questions of a game called Exceptional Mind. The book acts as the answers book of the questions of the game. This two works were (fictionally) created by the characters of Charles Kocian novel called One Exceptional Mind. The author of all this artistic works is Charles Kocian and, although they are the context of the “license material”, they are not the “license material” itself, therefore, are not under this CC BY-ND license. All rights of the novel, book and game are reserved to Charles Kocian under copyright © international laws.
Being the novel, book and game the greater context of the “license material”, we strongly recommend “the licensees” to create their art works after reading them and playing the game, to understand the context and avoid producing “adapted material”, something that is prohibited by this license, (read it below), accordingly to Section 1.a.
About the license material
The “license material” (the text sentences of the numbered questions of the game and the numbered short answers of the book described in the list below) are also under the Copyright © and Similar Rights held by “the licensor”. To comply this license “the licensee” must assure the following. First, he needs to maintain the “license material” unchanged, that is, the texts of the sentences of the questions and answers cannot be adapted, change, altered, arranged, transformed, or modified without “the licensor” permission. These sentences of questions and answers as presented below are the prime matter that “the licensee” will use to its own creations. Second, “the licensee” is allowed to add images in connection to the text. (This accordingly of what says in https://certificates.creativecommons.org, in 2. Adaptations 5. It says that, “as a legal matter, at times it is tricky to determine exactly what is and is not an adaptation”, but then recommend some rules about the licenses to keep in mind, saying that, “including an image in connection with text, as in a blog post, a powerpoint, or an article, does not create an adaptation unless the photo itself is adapted”). In this case, the “licence material” is only text, therefore, any kind of image or other mean except text can be connected to it, and that action will not produce “adapted material”. So, we encourage “the licensee” to create its own copyright pictures, paintings, draws, videos and animations, including sounds, voice, music and other forms of art or interactions and connect them to the text of the “licence material”. They are allowed to do this but with three conditions. 
Firstly, (and the fundamental one), is to connect the text of the “licence material” with the images of their own creation (or other designs, things or actions they may invent), but with the condition to clarify the meaning of the text of the “licence material” and enhance it, especially for a clear audio-visual understanding of the question and a clear audio-visual explanation of its answer. All creations must have high quality standards of production, materials and aesthetic requirements. They must be done in a luxury style, use Cinzel and Cormorant fonts, dark purple backgrounds, gold and silver colours, including light grey, black and white backgrounds too, and in a similar style of the championsrenaissance website and the game aesthetics. (Luxury products websites such as Rolls-Royce, Rolex, Michelangelo’s David, Monalisa, Rafael paintings and Parthenon are aesthetics references as well, and in music: Mozart, Bach, Beethoven and Rachmaninov. We view art ONLY as aesthetic pleasure derived from nature’s order. Any kind of human voice music (including opera) is not allowed and out of our aesthetic natural standards. Modern slow electronic and fashion show music are allowed, as the same are used in advertising of luxury products, harmonious, happy and grateful music to relax in refined styles (heavy metal, hard rock, reggaeton and the like are prohibited). In visual design, the golden number proportion and Fibonacci sequence is welcomed too, and especially works derived from natural patterns, and also natural landscapes like mountains, stars, clouds and sea as well, because we understand beauty exist in nature’s order. The images, sounds, voices and music produced in audio-visual works will follow and support the narrative of the text without adding new letters or text, or changing the words for synonyms, or altering the sequence of words. In short, the meaning of the sentences of the “licensed material” cannot be altered, change or distorted by improper images, sounds, music or any other type of actions. For creations of videos for YouTube, must be videos of one question and answer at a time. Each video will be between 30 seconds to 5 minutes accordingly to a simple Format described below. All other type of creations will follow a format described below as well. Again, and to be out of doubt, sentences of a complete answer are “as is" and described in the “license material” below. They cannot be cut or turn around, add signs between letters or words. The text of the answers can be used in books with images, T- shirts, cups, posters, pictures memes, illuminated signs, songs, art paintings, or others, but each of them accordingly to the Format and the “license material”. In case of a painter or photographer artist’s book, they must produce them with high quality paper and luxury style, using the text of one question and answer at a time, in one or more pages, but never more than one per page to not confuse. Group of different artists can make collective works, for instance, one producing music, other draws, paintings or artistic photographs, or one programmer can use Blender to create 3D virtual shapes and other programmer can use Godot to create an animation using those shapes, both joining their talents, for example, to create a video that explains audio-visually one question and answer of the “license material”. Different artists can join to expose their creations in art galleries showing, for instance, its paintings or photographs, or produce a collective exposition to show different collections of paintings and photographs each with one question and answer. A coordinated effort like that will help them for a bigger media coverage and to attract interest of high-end galleries and sponsors of luxury brands and high-end organizations, such as Benetau Yatchs, Airbus Helicopters, Rolls-Royce, Rolex or Parker, Versailles, Windsor Castle or the Louvre and British Museums, Cambridge, Oxford, Le Sorbonne, Harvard or MIT and other top-level institutions of the world.
The second condition of the contributors’ licensees to create their visual creations, plainly and short, is to make a direct or indirect advertisement of the book and game of Charles Kocian to increase its sales. This is accordingly to the attribution required for this license that says in Section 3.a.1.A.i (Licence Conditions and Attributions) that “the licensee” or user of this license needs to identify the author of the “licensed material”, in this case Charles Kocian. The text of this license says that “the licensor” can request to receive attribution in a reasonable manner. His request to receive attribution through the advertising of its book and game to increase its sales is a reasonable manner for the following reasons. Firstly, because the sale of its book and game supports him economically, so he can continue doing its work. Secondly, because the better the sales the more people will be playing the game and reading the book, and that will allow them to become exceptional minds and achieve their personal eudaimonia. (Eudaimonia is the holistic highest happiness possible for a virtuous man, being a virtuous man a virtuous-rational-animal who decided to practice the morality of reason to achieve its greater wealth in every sense, a deep happiness derived from the Aristotelian-telos-fulfilment as it is explained in the book. The objective of the book, game and novel is to help people to achieve eudaimonia). Thirdly, because the more people become exceptional minds and achieve eudaimonia, the smarter the world will be (applied to rulers and ruled) in the current and future generations. This is why Charles Kocian created the King Neo New Renaissance Movement, whose vision is to ease human species evolution to excellence perfecting the morality of reason. The “licensees”, by doing their creations, will contribute to implement the vision’s movement. These are enough reasons that allow “the licensor” to request attribution in the manner he is asking for. It is a win-win reasonable deal that benefit a smarter humanity and create not a future idiocracy, but a future smartcracy. To fulfil the licensor request in this manner, “the licensees” contributors will include in their creations, images of the book and game as they exist in the championsrenaissance website, without changing its colours images or fonts. They may use them in any kind of creations showing them from different perspectives, in movement or not, but maintaining its proportions and shape in creative ways. They are required to include a URL or hyperlink in a relevant place of their creations to grab people's attention, so they can click through and go to a sales page on the championsrenaissance website where the book and game are sold. Creations of paper artistic books with images, collections of photographs (or paintings) or expositions in art galleries, those works must clearly explain to the users where to buy the book and game. WARNING: The “license material” cannot be used as parts or inserts of other artistic works (like a painting inside another painting) or commercial advertising campaigns or by activists or political campaigns, or in signs or any other kind of propaganda of collective movements, protests indoors or outdoors. The only purpose of “the licensees” to create their art works and connect them to the “license material” text, is to ease human species evolution to excellence perfecting the morality of reason, but a reason based on evidence, tolerance, science, logic and nature’s beauty, and do it in proper peaceful contexts, civilized beautiful, elegant, stylish, refined and natural contexts. We resonate with Aristotle and its intellectual descendants like Hypatia of Alexandria, Ayn Rand, the Parthenon, the Renaissance of Medici’s Florence Family, who sponsored Leonardo, Michelangelo and Galileo, and also with Voltaire, Orwell, Newton, Einstein, Darwin, Ludwig von Mises and Carl Sagan among others whose minds respected the laws of nature. We resonate with nature’s beauty and the deep original folklore of all ethnicities around the world who absorbs the beauty of natural patterns into their artistic traditions. We are not in politics but we defend the individual freedom of choice and free markets without initiating brute force or deception to others. One more warning about “adapted material” and to be out of doubt. Creations must be done using the text of one question and answer at a time, but using images, music and sound that will not distort, change the meaning or diminish the original message of the sentences, but enhance and enrich a clear and deeper understanding of the “license material”. Creating an unproper visual, sound or music or any other kind of improper context will distort the original text message of the “license material” and will produce without doubt “adapted material”, something that is prohibited by this license, accordingly what it says in Section 1.a. of the CREATIVE COMMONS ATTRIBUTION-NODERIVATIVES 4.0 INTERNATIONAL PUBLIC LICENSE. “Adapted material” is prohibited and cannot be share without the permission of “the Licensor” or author. 
The third purpose for creating these art works and connect them to the text of the “license material”, is to benefit the creator’s contributors’ “licensees” themselves. Indeed, it is an opportunity for them to show its artistic talents to the world in a wider cultural context. Through its own great works, creators can show their unique professional talent to an educated public, communicating them their design exceptional capabilities. It is an opportunity to expand its scope and attract new potential clients to their businesses, and allow them to know that they are committed contributors who share the same values of the King Neo New Renaissance Movement. WARNING: The copyright of the “licensees” creations, in case they use a Creative Common license applied to their creations, must assure that will not produce future production of “adapted material” from the original “license material” here presented, therefore, they must use the same CREATIVE COMMONS ATTRIBUTION-NODERIVATIVES 4.0 INTERNATIONAL PUBLIC LICENSE. In whatever case, “licensees”, in their creative works, are obliged to publish a notice that refers to this Public License accordingly what says in its Section 3 (a), (1), (A), (iii) (ii), and (iv). 
King Neo Logo ©
Exceptional “licensees” who produce excellent works may be invited to enter the King Neo New Renaissance Movement Board Administrators. Those who accept are allow to use the King Neo © logo in their creations. 

Administrators
Administrators of the Board will maintain the GitHub page of the community, supervise the Code of Conduct, review the works of other “licensees” and will have preferences when some opportunities appear.

Code of conduct 
Introduction
The premise of this adult reasonable community is that nobody is here against its will. It is a good faith community of educated and good faith with resources individuals who are here with no ulterior purpose except to produce art. We understand art as beauty derived from nature’s order. Here we use art in regard to enhance and enrich the explanation of the “license material”. Everybody is free to join or leave the community as many times as it wishes. But anyone who violates the Code of Conduct will lose his reputation inside the community and will not be allowed to come back again. This Code of Conduct begins with the basic of following the law of the person’s country. This mean that people with criminal trials or charges, national or international, cannot join or stay in the community. Dishonest politicians, members with hidden agendas of NGO, or any other type of activists or members of organizations which their main objectives are against or may distort, distract or deviate the objectives of this community, they cannot be part or stay in this community. If they are part of any other community, public or secret, they must act in good faith to tell the truth when they sign the conditions to join this, at the moment when they fill the form to enter this community, a form where this kind of questions are asked. No member of this community can be in illegal conducts, such as the use of drugs or any other illegal activity. Although in this community we don’t discriminate gender, ethnicity or religion, this community is compound of high-educated moral persons of any race and in any country, but they all have a strong rational, secular and scientific approach to life, and with a great ambition to create art as beauty derived from nature’s order. Not everybody needs to agree with this view, but those who we do, we like to share with others like us to enrich our creations and expand the philosophical knowledge contained in the book and game. Because we believe man is a rational animal, we condemn the irrational as anti-human. Any irrational conduct is not tolerated. We respect the people who disagree with us and we request from them the same respect to disagree with their disagreement. This is not a place of debate of people who disagree with each other. That place exists in social media but is not the purpose of this community. The only purpose of this community is to integrate artistic images to the “license material” here provided by people who share our Aristotelian philosophic values. We don’t tolerate rational contradictions. We don’t tolerate the negation of the Law of Identity formulated by Aristotle that says A is A. Having said that, here is a list of the Code of Conduct members of the community. We start with the premise that everybody in the community agree with the values exposed in the book and the game, and that they act in good faith. (Abuse reports can be done in abuse@whatever.com. We will take your report seriously). People with contradictions or against the values of the community cannot enter or stay. What we do in this community is like doing a sport. If somebody don’t like this sport, he can find other in another place. Administrators of the community reserve the right to take whatever action they feel appropriate with regards to the Code of Conduct violations. What follows is a list of good conducts the members of the community must observe.

Good conducts

1.	Empathetic rational conversation. Be rational and understand that emotions derived from thoughts. Make people feel welcome, supported and never insult or discriminate. Behave as a well-educated aristocrat.
2.	Don’t be offended. If somebody disagree with you, breathe, be calm, carry on. Act rationally, ask why and perhaps you can learn something.
3.	No emotional hysteria. Be cool, calm and stylish. Put your rational Neocortex as the ruler of your Paleocortex. Control your chimp rate, as players do when they crown themselves playing the game. Count to 10 before acting. Postpone your opinion or sending an email or insult or saying something in bad faith that you may repent later. Just be patient and wait for 3 days before acting if you are in any kind of emotional irrational storm. Always act controlling your emotions and find the real causes of your exaggerated emotional reaction. Always ride the horse and don’t let the horse ride you. It doesn’t look good.
4.	We suggest to read the book and play the game as many times as possible, every month.
5.	Never initiate force or deception to others.
6.	Treat others as you expect they treat you.
7.	Judge but rationally and expect to be judged rationally.
8.	Don’t initiate conversations or debates beyond the purpose of the community that is no other than to add images to the text of the “license material”. There are other places for that.
9.	Try to see the rational genius and hero in others.
10.	We suggest to practice the morality of reason as it is explained in the book and its bibliography.
11.	Good faith premise. Accept a person you don’t know in good faith, who is not deliberately trying to deceit you, but report if he proves to act in bad faith.
12.	Listen without interruption in good faith, believing he is talking rationally and good faith. 
13.	Use language with words definitions as the 1960’s dictionaries say.
14.	 If you don’t understand something, identify what words are blur and ask your interlocutor definitions for them.
15.	Use precise concepts definitions attached to percepts. Ask for definitions and to what facts or evidence those words are attached.
16.	We don’t ask for people to apologize or feel guilty or to ask “emotional forgiveness”, but to rationally recognize the logic cause of an error to not repeat it again. 
17.	Secularism. We are guided by Aristotle’s ontology. We don’t believe that knowledge is inherent as Plato did, but is gradually acquired through our senses as Aristotle concluded. We seek truth through the scientific method. We believe in the primacy of existence over consciousness not vice-versa.
18.	Religious and political debates, hidden agendas or open activism is completely prohibited.
19.	Think big.

Evaluation system
Before publishing their artistic works, the “licensees” can show them to the administrators of the community to receive feedback, with the four categories of evaluation. Excellent, Good, Average and Unacceptable. As it was said, those who are “excellent exceptional” may be invited to join the King Neo New Renaissance Movement Board Administrators. 

Ranking of works
The GitHub community administrators will vote every three months for the best works of that period and produce a ranking that will be published in GitHub and the championsrenaissance website.

Formats
All the artistic visual works that the “licensees” will create, adding or integrating audio or visual elements to the text of the “license material” needs to be done with a format or template. The format consists to follow sequential steps. The first step (at the beginning of a video or at the top of the visual composition) consist to write and say the number of the question to easily identify it. It must say “Question N° 1” (or the correspondent number) in big Cinzel black fonts.  The second step is to write and say: “A question of the Exceptional Mind Philosophical Game”. It can be done in Cinzel and Cormorant fonts. Pauses and spaces can be design at the unique criteria of the artist. The third step in the sequence is to write the complete sentence of the question and its alternatives. The fourth step is to write the complete sentence of the answer. The fifth step is to advertise the game and book writing and saying the message: “Find the book and game here”, providing a link to the sales page in the championsrenaissance website or were to buy them. The last step is the advertising of the “licensees” themselves, where the creators can use their logos, signatures, slogans, etc., to communicate to potential clients their work and talents. This last step will repeat the fifth step providing people clear data where to buy the book and game. This manner of attribution the licensor is requesting is a reasonable request, accordingly to Section 3.a of this license. As it was said and to be out of doubt, we insist that all works cannot produce confusion. For instance, videos must contain only one answer per video, and need to be between 30 seconds and 5 minutes each. In case of photographs, paintings or sculptures, only one answer at a time in each artistic work. Books of photographs, draws or images must contain all the answers, or divided in two book’s volumes as they are divided in the parts of the book. Creators can use one or more pages to show one answer, but not two answers in the same page. The purpose of this format is to help the understanding of the question and its answers and not to confuse. The same is suggested for paintings, artistic photography, installations or sculptures. In case of short theatrical performances, TV shows with public with question-answers contests (like Jeopardy), or TV shows to play the game in teams (similar to the novel) in a big board with public, or in case of interactive cognitive museums, or expositions, the same criteria of the format apply. Also, for any kind of apps or merchandising things, such as T-shirts, cups, huts and the like or any other invention that help to spread the text of the “license material” will follow the same criteria of this format.

License material (list of questions and answers) 
What follows is the text of “license material”. The first column of this table contains the number of the question; the second, the question; the third, option a; the fourth, option b; the fifth, the correct option; the sixth, the short answer. This is an example of a question card and its answer in the game and it suggest a format or template on how to use this “license material” in a reasonable manner. 
     

List of questions and answers
N°	question	option_a	option_b	answer	short_answer
1	A man's cultural imprint derives from the philosophy of his culture.	True	False 	a	A man's cultural imprint derives from the philosophy of his culture, but philosophies that deny reality generate cognitive dissonance and anxiety. 
2	Which philosophers shaped the cultures of the West? 	Pythagoras, Descartes and Marx.	Plato, Aristotle and Kant	b	Plato, Aristotle and Kant. All cultures of the West derive from the ideas of Plato, Aristotle, and Kant, but not all integrate sensory perceptions with ideas.
3	Plato's theory says that the world of ideas derives from the material world. 	True	False 	b	Plato states that reality derives from ideas. He duplicates the natural world and invents another supernatural, perfect, invisible one. He calls it the world of Ideas which, for Plato, existed before the material universe.
4	Aristotle's philosophy doubles the world.	True	False 	b	Aristotle does not duplicate existence but studies the laws of nature.
5	Kant's philosophy says that noumenal reality can be known by pure reason.	True	False 	b	Kant asserts that neither sensory perceptions nor reason serve to know reality "as it is" (which he called "noumenal reality") because, according to Kant, it is unknowable.
6	Cultural imprinting refers to your culture shaping your character.	True	False 	a	"Cultural imprinting" is the process by which a child absorbs without his consent the entire culture, including the irrational aspects of his parents and teachers.
7	What is vicarious learning?	Religious learning.	Learning by imitation.	b	Vicarious learning is learning by imitation of authority figures without critical analysis.
8	What are mirror neurons?	Neurons that mimic the behaviours of others.	Refractory neurons of the eyeball.	a	Mirror neurons mimic the behaviours of others. It explains the phenomenon of contagion from a yawn to an attack of mass hysteria.
9	What is conditioned reflex learning?	Rational learning.	Irrational learning by repetition.	b	The conditioned reflex is irrational learning by repetition of cultural acts, in education, customs, media, advertising and propaganda.
10	What is the name of the process of demoralizing, destabilizing, producing a crisis and re-normalizing the culture of a society?	Cultural education.	Cultural subversion.	b	Cultural subversion is done in four stages: 1°Demoralization: changing values; 2° Destabilization: destroy legality; 3° Crisis: riots or civil war; 4° Normalization: what was previously reprehensible is accepted as normal.
11	A person's paleocortex denies reality if it contradicts its culture.	True	False 	a	When reality contradicts a man's culture, his paleocortex or instinctive brain negates evidence by inhibiting the critical thinking of his rational neocortex.
12	Sensory perception starts from the objects of the physical world and ends in the brain that interprets electrical impulses.	True	False 	a	Sensory perception starts from the objects of the physical world and ends in the brain that interprets electrical impulses.
13	The emission of distal stimulus is the last stage of sensory perception.	True	False 	b	The energy emitted by things that exist in the material world is the 1st stage of sensory perception and is called distal stimulation.
14	The second stage of sensory perception is when a sensory cell analyse the distal stimulus?	True	False 	b	The distal stimulus is received by specialized cells that exist in each sensory organ. The eye receives light; the ear, sound; nose, odours, etc. The reception of distal stimulus is the 2nd stage of sensory perception.
15	The process of converting the distal stimulus to proximal stimulus (or nerve impulse) is called transduction.	True	False 	a	Transduction is the 3rd stage of perception. It occurs when the distal stimulus received (light, sound, smell, etc.) is converted by the sensory cell to proximal stimulus or nerve electrical impulse.
16	In the 4th stage of sensory perception, the paleocortex interprets the electric impulses.	True	False 	a	The paleocortex interprets the proximal stimulus (or nerve electrical impulse). He compares it with the data in his memory and denies it if it seems dangerous, preventing the neocortex from being informed of reality.
17	The fifth stage of sensory perception occurs when the neocortex rationally analyses the electric impulses according to the premises of its cultural mold.	True	False 	a	The fifth stage of sensory perception is possible only when the neocortex receives information from the proximal stimulus.
18	What is the Comfort Zone?	Neural pathways derived from focusing the mind and critical thinking.	Neural highways derived from cultural imprinting and mental habits.	b	The Comfort Zone is the easiest way where nerve impulses circulate in your brain, automatically, with no or little critical thinking.
19	Every emotion is a primary, a cause in itself.	True	False 	b	Every emotion is an effect, the response to an intellectual evaluation made at the speed of light that goes unnoticed.
20	What are fallacies?	True arguments that seem false.	False arguments that seem true.	b	Fallacies are false arguments that seem true. The best way to understand them is with examples.
21	Does gender ideology contradict Mendel's laws?	Yes	No	a	The fact is that male cells have XY genes; the feminine, XX.
22	The Vatican awarded Galileo because he discovered with his telescope that the Earth was moving.	True	False 	b	The Inquisition condemned Galileo for being faithful to the evidence of his telescope and proving that the Earth was moving.
23	Is there modern propaganda and censorship?	Yes	No	a	There has always been propaganda and censorship. The rulers make propaganda and censorship to govern the minds of the ruled.
24	Does Collectivism ask the individual to refine the use of his reason?	Yes	No	b	Collectivism needs irrational individuals who follow an emotional majority manipulated by propaganda.
25	In sports competitions and war the one who knows best the terrain wins.	True	False 	a	A winner acts according to reality. He thinks with words derived from concrete things. Its concepts derive from percepts; its ideas, from facts and evidence.
26	The axiomatic concepts are:	Existence, identity and consciousness.	Life, emotion and instinct.	a	The axiomatic concepts are existence, identity and consciousness. They are the proofs from which all objective knowledge derives. There is nothing prior to them and they are implicit in every thought.
27	The axiomatic concept of "existence" explains the difference between perceiving something instead of nothing.	True	False 	a	"Existence" is a concept that refers to everything that exists, existed, and will exist. Existence exists even though no one perceives it.
28	"Consciousness" begins with your ideas and ends with your sensory perceptions.	True	False 	b	"Consciousness" refers to all psychological actions that begins with perception. Existence, can exist without consciousness; consciousness, derives from existence.
29	The concept "identity" refers to things being different from themselves.	True	False 	b	Identity refers to the fact that, if something is something, it is that, and not something else. Aristotle identified the fact as The Law of Identity: "A is A." An orange cannot be an orange and a stone at the same time.
30	Axiomatic concepts are absolute because to reject them you have to accept them.	True	False 	a	No one can escape the axiomatic concepts because to deny them one must accept them. Whoever denies them renounces his reason.
31	Causality says that, if something is what it is, it will act according to its nature, sometimes yes, sometimes not.	True	False 	b	"Causality" says that if something is something it is obliged to act according to its nature, not sometimes but always. The fire burns and the water wets, the rain falls and the fire rises. The universe orders itself by Identity and Causality.
32	The corollary of the "Primacy of Existence over Consciousness" refers to the fact that first you perceive an entity, then that entity come to existence.	True	False 	b	To perceive an entity, it needs to exists first. Without an existent entitiy any consciousness is impossible. So, the phrase, "I think, therefore, I am" is wrong; "I am, therefore, I think" is right.
33	Natural things are chosen and relative.	True	False 	b	The universe is given, natural and absolute. It is governed by laws that exist on their own independent of people's opinions. To deny it is to cancel reality.
34	The concept "entity" refers to anything that has no identity.	True	False 	b	An entity is a thing with a unique identity, a physical object with particular characteristics that is perceived with the senses.
35	The Allegory of the Metaphysical Tetrahedron illustrates how axiom-concepts and its corollaries connect each other.	True	False 	a	The Allegory of the Metaphysical Tetrahedron is a six-edged sculpture illustrating the connection between axiom-concepts and its corollaries.
36	Epistemology comes from the Greek "episteme" (knowledge) and "logos" (study).	True	False 	a	Epistemology studies how man learns in the following order: sensory perception, thoughts, emotions, actions.
37	A percept is the integration of a perceived object that the sense organs and brain does accurately and automatically.	True	False 	a	A "percept" is the sensory integration of things that man perceives with his senses in the material world. This happens automatically and accurately in the sense organs and brain.
38	What is the relationship between a concept and a percept?	The concept derives from percepts.	The percept derives from concepts.	a	A concept derives from percepts. For example, the concept apple derives from all the real apples perceived (percepts).
39	Is there an apple if you don't see its cells?	Yes	No	a	The cells of an apple do not contradict the apple we see, nor does the top of the tree contradict its invisible roots. The visible and invisible universe is a continuum without one causing the other.
40	Do you perceive according to the identity of your sensory organs?	Yes	No	a	Each sensory organ has its own identity. No ear sees, no nose listens; each sense organ is what it is and acts according to its identity, that is, accordingly to the Law of Causality.
41	Are your sense organs absolute?	Yes	No	a	Your sense organs are absolute for you, because they are given and natural tools of survival, the result of more than four billion years of biological evolution on Earth.  
42	Does the concept "unity" have any role in forming a concept?	Yes	No	a	To consider "entities" as "units" is man's cognitive method. For example, the characteristics of the entities "spoons" are consider as a unit that groups them in the "spoon" concept.
43	Forming a concept involves a mathematical calculation.	True	False 	a	Forming a concept involves a mathematical calculation, because it identifies a common characteristic to measure it.
44	A concept identifies the common characteristic of the entities that own it, and refers to a specific measurement of a particular entity.	True	False 	b	The concept identifies the common characteristic of all entities that own it, but omits to measure its particular quantities, which must exist in some or any amount.
45	Does the Allegory of Photo Albums and Folders serve to know how "percepts" connects with concepts?	Yes	No	a	The Allegory of Photo Albums and Folders serves to understand how the "percepts", which derived from sensory perceptions, are connected to concepts.
46	In the Allegory of Photo Albums and Folders, what is a basic concept?	An album with photos of the same things.	A folder with photos of the same things.	a	A "basic concept" is like a photo album with pictures of the same things, the kind of concepts closest to the perceptual level.
47	In the Allegory of Photo Albums and Folders, how is a 1st level concept represented?	With a photo album containing multiple folders.	With a folder containing multiple photo albums.	b	With a 1st level folder containing several photo albums. An example is "fruit". Is a folder that contains several photo albums each with photos of the same type of fruit.  
48	In the Allegory of Photo Albums and Folders, what is a 2nd level concept?	2nd level folders containing photo albums.	2nd level folders containing 1st level folders.	b	2nd level concepts are 2nd level folders that contain 1st level folders. An example is "vegetables", which contains 1st level folders, such as "fruits" and "legumes", which in turn contain photo albums of different types of fruits and vegetables.
49	In the Allegory of Photo Albums and Folders, what is a 3rd level concept?	Photo albums containing 2nd level folders.	3rd level folders containing 2nd level folders.	b	A 3rd level concept is a folder containing 2nd level folders. For example, "organisms", which contains several 2nd level folders, such as plants, mammals, reptiles, etc.
50	The concepts of consciousness refer to all psychological action of man.	True	False 	a	The concepts of consciousness classify all the psychological actions of man such as perceiving, thinking, deciding, feeling, desiring and imagining.
51	On what does the intensity and content of your consciousness depend?	Of your interests.	Of your IQ.	a	The content of your consciousness depends on your interests and these have two characteristics: content and intensity.
52	What is the definition of a concept?	Classify a larger group into a smaller group.	Classify a smaller group into a larger group.	b	For example, Aristotle classified man as a "rational animal." The smaller group is man's rationality; the larger group, animals.
53	Does the new meaning of one concept influence another?	Yes	No	a	The meaning of once concept influences the others. The renewal of the meaning of one concept renews all the knowledge of a person, just like at renovating the furniture of a house ends up renovating the whole house.
54	The meaning of one concept depends on the meaning of all the others.	True	False 	a	The meaning of a concept depends on the meaning of others because words define words and, therefore, build mental contexts.
55	What is hierarchy when learning?	That first you learn to multiply and then to count.	That you go to school first then to college.	b	Knowledge is constructed from bottom to up, like a building. First "percepts", then "concepts". You learn to count, then to multiply; before a Newton, a Galileo was necessary. There are no shortcuts to knowledge.
56	To validate a concept, you have to reverse engineer it.	True	False 	a	To reverse engineer a concept you have to see how the percepts connect to the concepts. It is done by opening the folders of higher levels until you reach the photo albums.
57	"Syntax" studies how grammatical sentences should be ordered to speak well.	True	False 	a	"Syntax" is the part of grammar that studies how words and groups of sentences are combined to think properly.
58	Reason is the faculty that identifies and integrates man's ideas.	True	False 	b	In the words of Ayn Rand, reason "is the faculty that identifies and integrates the material provided by man's senses."
59	Reason derives from collective thinking.	True	False 	b	Reason derives from an individual brain that chooses to focus its own mind. A giant collective brain doesn't exist. Is the individual who can think, but only if he makes the choice to think.
60	Why focus your mind allows you to choose well?	Because it does not produce sharpness.	Because it produces contrast.	b	Focusing your mind is similar to focus the lens of a camera to get a clear image. It allows you to differentiate clear options to choose well, which means: freedom, success and happiness.
61	Is man's "free will" absolute?	Yes	No	a	Whether someone chooses or does not choose to choose, in both cases he chooses, therefore, his free will is absolute. This means that nobody escape the absolute consequences of its choices, by action or omission.
62	Logic is the art of definitions.	True	False 	b	Logic is the science of non-contradictions. But the conclusion of a syllogism, although logically right, it can be factually wrong if it contains floating concepts.
63	Are the concepts of "possible," "probable," and "certain" referring to the same thing?	Yes	No	b	When there is no evidence against and some in favour, something is "possible"; if there is enough evidence, but there are still doubts, something is "probable"; if the evidence is conclusive, its "certain", because it leaves no room for doubt.
64	How many means of knowledge does man have?	Reason and emotion.	Just reason. 	b	Only reason allows us to know. Emotions are effects; reason, the cause. All emotion derives from the intellect that can know reality.
65	Are emotions independent from reason?	Yes	No	b	Emotions derive from an intellectual involuntary evaluation. This is not noticed because it occurs at the speed of light and automatically.
66	What is evasion?	Decide not to see.	Not to see involuntarily.	a	To evade is to make the decision to deny reality in order to adapt to a cultural collective. It is to deny one's own sensory perceptions to please a group, as the Asch's Experiment shows.
67	Is arbitrary something false?	Yes	No	b	The arbitrary says: "You can't prove that X exists, but you also can't prove that it doesn't exist."  But in logic you can't prove a negative. The absence of proof does not prove the absence.
68	Things are absolute, but in a given context and time.	Yes	No	a	Everything that exists, exists absolutely in a given context and time, for example, is an absolute fact that you are now reading this where you are.
69	An agnostic believes anything is possible, but he's not sure.	True	False 	a	The philosophy of an agnostic is to never be sure of anything, not even that.
70	Mysticism and scepticism deny evidence and reason.	True	False 	a	Mysticism says that matter is illusion; scepticism, that nothing is absolute. Both deny reality and reason.
71	The value of our life is appreciated when we accept has an end.	True	False 	a	When you accept the fact that your existence has a definitive end, your life fulfils with glory and every moment becomes heroic.
72	What is the greatest value of man?	Reason.	Its body.	a	Man's greatest value, and its means of survival, is his reason, but he needs choose it in order to live like a man.
73	Rational morality answers the question: What should I do?	True	False 	a	Rational morality is the study of what is the best course of rational action for man happiness.
74	Reason does not give man moral value, and it does not show him his way of moral perfection.	True	False 	b	Reason is the essential characteristic of man, but he must choose it as a value to attain his moral perfection.
75	What's the point for a man to choose a productive life purpose?	To prioritize its own actions and succeed.	To get carried away by propaganda and fail.	a	Choosing a productive life goal serves to prioritize one's actions. It is equivalent to building a football arch where you can score goals.
76	Man's main virtue is his rationality.	True	False 	a	Man needs to act rationally to succeed in life, therefore, rationality is his main virtue.
77	Benign selfishness is morally inferior to altruism.	True	False 	b	Benign selfishness is morally superior to altruism, and the latter is not empathy.
78	Reason is a value for all people.	True	False 	b	Reason is a value, but only for people who choose it.
79	The moral purpose of life is to love one's neighbour.	True	False 	b	The moral purpose of life is to discover why the pursuit of one's own happiness is an end in itself, given, natural and absolute, and be productive to humanity.
80	Man's self-esteem derives from his ability to attain social-status.	True	False 	b	Man's self-esteem derives from its rational honesty and to know why is worthy of its happiness.
81	What are the virtues of rational morality?	Rationality, integrity, independence, honesty, justice, productivity and pride.	Rationality, compassion, independence, honesty, piety, productivity and humility.	a	The virtues of rational morality are: rationality, integrity, independence, honesty, justice, productivity and pride.
82	Is the virtue of independence to reach conclusions from one's own experiments and research?	Yes	No	a	The independent man focuses his mind and discovers the world for himself on the basis of his own experience and observations, like Galileo.
83	Is the virtue of integrity to tolerate our small contradictions?	Yes	No	b	The virtue of integrity does not tolerate contradictions between reality, perceptions, reason, emotions and actions, and its integration it is superior to the sum of its parts.
84	The virtue of honesty is:	Be loyal to the culture.	To be loyal to the material reality of the universe.	b	The virtue of honesty recognizes the absolute material reality of the universe.
85	Is the virtue of justice the necessity of not judging men so as not to be judged?	Yes	No	b	The man who practices the virtue of justice judges others with conclusive evidence and, for the same reason, prepares himself to be judged.
86	Does the virtue of productivity adapt nature to man?	Yes	No	a	The productive man produces with his mind and adapts nature to his desires, but obeying it first.
87	What is the virtue of productivity for?	To achieve self-esteem.	To achieve social-status.	a	Self-esteem is man's greatest reward and derives from its productivity not its social-status.
88	What is pride?	A capital sin.	The sum of all rational virtues.	b	The virtue of pride derives from becoming oneself a masterpiece, practicing the rational virtues in each minute of our life.
89	The quality of our happiness depends on the quality of our emotions.	True	False 	b	The quality of your happiness depends on the quality of your thoughts and the quality of these of a paradigm that respects nature.
90	The success of the hero is the consequence of practicing humility.	True	False 	b	Pride is the heroes’ virtue; humility is poverty, but the ignorant calls it virtue.
91	Self-esteem derives from practicing:	The virtue of pride.	Humility.	a	The virtue of pride allows you to achieve self-esteem. Whoever abandons his reason feels fear, because he abandons his weapon of survival, and guilt, because he knows that he does it voluntarily.
92	What is metaphysical sexual pleasure?	Spiritual sexual pleasure.	Sexual pleasure that integrates the body and mind.	b	Love without desire is just as incomplete as desire without love, therefore, bodies and minds both need to get into bed.
93	Which political system is in accordance with the mold of nature?	Collectivism.	Austrian School Capitalism based on individualism.	b	Austrian School Capitalism is a Minarchist free market system that is based on honest competition between producers. It protects the freedom of the individual, private property and works with the gold standard.
94	Should art serve man as an inspiration for him to reach the best version of himself?	Yes	No	a	Art, instead of being rubbish-whim or propaganda, can elevate man to the best he can and should become as an individual: the optimal-rational-animal of the New Renaissance.

* * *

The text that follows is the text of the License Creative Commons Attribution-NoDerivatives 4.0 International Public License that applies to the “license material” (94 questions and answers described above), and to the contributors of the GitHub King Neo New Renaissance Community as part of the King Neo New Renaissance Movement. The text of this license is accordingly to the text of the Creative Commons website (https://creativecommons.org/) on June 2023.

Creative Commons Attribution-NoDerivatives 4.0 International Public License
 
Attribution-NoDerivs
CC BY-ND

By exercising the Licensed Rights (defined below), You accept and agree to be bound by the terms and conditions of this Creative Commons Attribution-NoDerivatives 4.0 International Public License ("Public License"). To the extent this Public License may be interpreted as a contract. You are granted the Licensed Rights in consideration of Your acceptance of these terms and conditions, and the Licensor grants You such rights in consideration of benefits the Licensor receives from making the Licensed Material available under these terms and conditions.
Section 1 – Definitions.
a.	Adapted Material means material subject to Copyright and Similar Rights that is derived from or based upon the Licensed Material and in which the Licensed Material is translated, altered, arranged, transformed, or otherwise modified in a manner requiring permission under the Copyright and Similar Rights held by the Licensor. For purposes of this Public License, where the Licensed Material is a musical work, performance, or sound recording, Adapted Material is always produced where the Licensed Material is synched in timed relation with a moving image.
b.	Copyright and Similar Rights means copyright and/or similar rights closely related to copyright including, without limitation, performance, broadcast, sound recording, and Sui Generis Database Rights, without regard to how the rights are labeled or categorized. For purposes of this Public License, the rights specified in Section 2(b)(1)-(2) are not Copyright and Similar Rights.
c.	Effective Technological Measures means those measures that, in the absence of proper authority, may not be circumvented under laws fulfilling obligations under Article 11 of the WIPO Copyright Treaty adopted on December 20, 1996, and/or similar international agreements.
d.	Exceptions and Limitations means fair use, fair dealing, and/or any other exception or limitation to Copyright and Similar Rights that applies to Your use of the Licensed Material.
e.	Licensed Material means the artistic or literary work, database, or other material to which the Licensor applied this Public License.
f.	Licensed Rights means the rights granted to You subject to the terms and conditions of this Public License, which are limited to all Copyright and Similar Rights that apply to Your use of the Licensed Material and that the Licensor has authority to license.
g.	Licensor means the individual(s) or entity(ies) granting rights under this Public License.
h.	Share means to provide material to the public by any means or process that requires permission under the Licensed Rights, such as reproduction, public display, public performance, distribution, dissemination, communication, or importation, and to make material available to the public including in ways that members of the public may access the material from a place and at a time individually chosen by them.
i.	Sui Generis Database Rights means rights other than copyright resulting from Directive 96/9/EC of the European Parliament and of the Council of 11 March 1996 on the legal protection of databases, as amended and/or succeeded, as well as other essentially equivalent rights anywhere in the world.
j.	You means the individual or entity exercising the Licensed Rights under this Public License. Your has a corresponding meaning.
Section 2 – Scope.
a.	License grant.
1.	Subject to the terms and conditions of this Public License, the Licensor hereby grants You a worldwide, royalty-free, non-sublicensable, non-exclusive, irrevocable license to exercise the Licensed Rights in the Licensed Material to:
A.	reproduce and Share the Licensed Material, in whole or in part; and
B.	produce and reproduce, but not Share, Adapted Material.
2.	Exceptions and Limitations. For the avoidance of doubt, where Exceptions and Limitations apply to Your use, this Public License does not apply, and You do not need to comply with its terms and conditions.
3.	Term. The term of this Public License is specified in Section 6(a). 
4.	Media and formats; technical modifications allowed. The Licensor authorizes You to exercise the Licensed Rights in all media and formats whether now known or hereafter created, and to make technical modifications necessary to do so. The Licensor waives and/or agrees not to assert any right or authority to forbid You from making technical modifications necessary to exercise the Licensed Rights, including technical modifications necessary to circumvent Effective Technological Measures. For purposes of this Public License, simply making modifications authorized by this Section 2(a)(4) never produces Adapted Material.
5.	Downstream recipients.
A.	Offer from the Licensor – Licensed Material. Every recipient of the Licensed Material automatically receives an offer from the Licensor to exercise the Licensed Rights under the terms and conditions of this Public License.
B.	No downstream restrictions. You may not offer or impose any additional or different terms or conditions on, or apply any Effective Technological Measures to, the Licensed Material if doing so restricts exercise of the Licensed Rights by any recipient of the Licensed Material.
6.	No endorsement. Nothing in this Public License constitutes or may be construed as permission to assert or imply that You are, or that Your use of the Licensed Material is, connected with, or sponsored, endorsed, or granted official status by, the Licensor or others designated to receive attribution as provided in Section 3(a)(1)(A)(i).
b.	Other rights.
1.	Moral rights, such as the right of integrity, are not licensed under this Public License, nor are publicity, privacy, and/or other similar personality rights; however, to the extent possible, the Licensor waives and/or agrees not to assert any such rights held by the Licensor to the limited extent necessary to allow You to exercise the Licensed Rights, but not otherwise.
2.	Patent and trademark rights are not licensed under this Public License.
3.	To the extent possible, the Licensor waives any right to collect royalties from You for the exercise of the Licensed Rights, whether directly or through a collecting society under any voluntary or waivable statutory or compulsory licensing scheme. In all other cases the Licensor expressly reserves any right to collect such royalties.
Section 3 – License Conditions.
Your exercise of the Licensed Rights is expressly made subject to the following conditions.
a.	Attribution.
1.	If You Share the Licensed Material, You must:
A.	retain the following if it is supplied by the Licensor with the Licensed Material:
i.	identification of the creator(s) of the Licensed Material and any others designated to receive attribution, in any reasonable manner requested by the Licensor (including by pseudonym if designated);
ii.	a copyright notice;
iii.	a notice that refers to this Public License;
iv.	a notice that refers to the disclaimer of warranties;
v.	a URI or hyperlink to the Licensed Material to the extent reasonably practicable;
B.	indicate if You modified the Licensed Material and retain an indication of any previous modifications; and
C.	indicate the Licensed Material is licensed under this Public License, and include the text of, or the URI or hyperlink to, this Public License.
For the avoidance of doubt, You do not have permission under this Public License to Share Adapted Material.
2.	You may satisfy the conditions in Section 3(a)(1) in any reasonable manner based on the medium, means, and context in which You Share the Licensed Material. For example, it may be reasonable to satisfy the conditions by providing a URI or hyperlink to a resource that includes the required information.
3.	If requested by the Licensor, You must remove any of the information required by Section 3(a)(1)(A) to the extent reasonably practicable.
Section 4 – Sui Generis Database Rights.
Where the Licensed Rights include Sui Generis Database Rights that apply to Your use of the Licensed Material:
a.	for the avoidance of doubt, Section 2(a)(1) grants You the right to extract, reuse, reproduce, and Share all or a substantial portion of the contents of the database, provided You do not Share Adapted Material;
b.	if You include all or a substantial portion of the database contents in a database in which You have Sui Generis Database Rights, then the database in which You have Sui Generis Database Rights (but not its individual contents) is Adapted Material; and
c.	You must comply with the conditions in Section 3(a) if You Share all or a substantial portion of the contents of the database.
For the avoidance of doubt, this Section 4 supplements and does not replace Your obligations under this Public License where the Licensed Rights include other Copyright and Similar Rights.
Section 5 – Disclaimer of Warranties and Limitation of Liability.
a.	Unless otherwise separately undertaken by the Licensor, to the extent possible, the Licensor offers the Licensed Material as-is and as-available, and makes no representations or warranties of any kind concerning the Licensed Material, whether express, implied, statutory, or other. This includes, without limitation, warranties of title, merchantability, fitness for a particular purpose, non-infringement, absence of latent or other defects, accuracy, or the presence or absence of errors, whether or not known or discoverable. Where disclaimers of warranties are not allowed in full or in part, this disclaimer may not apply to You.
b.	To the extent possible, in no event will the Licensor be liable to You on any legal theory (including, without limitation, negligence) or otherwise for any direct, special, indirect, incidental, consequential, punitive, exemplary, or other losses, costs, expenses, or damages arising out of this Public License or use of the Licensed Material, even if the Licensor has been advised of the possibility of such losses, costs, expenses, or damages. Where a limitation of liability is not allowed in full or in part, this limitation may not apply to You.
c.	The disclaimer of warranties and limitation of liability provided above shall be interpreted in a manner that, to the extent possible, most closely approximates an absolute disclaimer and waiver of all liability.
Section 6 – Term and Termination.
a.	This Public License applies for the term of the Copyright and Similar Rights licensed here. However, if You fail to comply with this Public License, then Your rights under this Public License terminate automatically.
b.	Where Your right to use the Licensed Material has terminated under Section 6(a), it reinstates:
1.	automatically as of the date the violation is cured, provided it is cured within 30 days of Your discovery of the violation; or
2.	upon express reinstatement by the Licensor.
For the avoidance of doubt, this Section 6(b) does not affect any right the Licensor may have to seek remedies for Your violations of this Public License.
c.	For the avoidance of doubt, the Licensor may also offer the Licensed Material under separate terms or conditions or stop distributing the Licensed Material at any time; however, doing so will not terminate this Public License.
d.	Sections 1, 5, 6, 7, and 8 survive termination of this Public License.
Section 7 – Other Terms and Conditions.
a.	The Licensor shall not be bound by any additional or different terms or conditions communicated by You unless expressly agreed.
b.	Any arrangements, understandings, or agreements regarding the Licensed Material not stated herein are separate from and independent of the terms and conditions of this Public License.
Section 8 – Interpretation.
a.	For the avoidance of doubt, this Public License does not, and shall not be interpreted to, reduce, limit, restrict, or impose conditions on any use of the Licensed Material that could lawfully be made without permission under this Public License.
b.	To the extent possible, if any provision of this Public License is deemed unenforceable, it shall be automatically reformed to the minimum extent necessary to make it enforceable. If the provision cannot be reformed, it shall be severed from this Public License without affecting the enforceability of the remaining terms and conditions.
c.	No term or condition of this Public License will be waived and no failure to comply consented to unless expressly agreed to by the Licensor.
d.	Nothing in this Public License constitutes or may be interpreted as a limitation upon, or waiver of, any privileges and immunities that apply to the Licensor or You, including from the legal processes of any jurisdiction or authority.

---
## [git/git](https://github.com/git/git)@[8260bc5902...](https://github.com/git/git/commit/8260bc59023136edeaed1f1006a03f44cc849883)
#### Saturday 2023-06-03 02:36:01 by Jeff King

diff: detect pathspec magic not supported by --follow

The --follow code doesn't handle most forms of pathspec magic. We check
that no unexpected ones have made it to try_to_follow_renames() with a
runtime GUARD_PATHSPEC() check, which gives behavior like this:

  $ git log --follow ':(icase)makefile' >/dev/null
  BUG: tree-diff.c:596: unsupported magic 10
  Aborted

The same is true of ":(glob)", ":(attr)", and so on. It's good that we
notice the problem rather than continuing and producing a wrong answer.
But there are two non-ideal things:

  1. The idea of GUARD_PATHSPEC() is to catch programming errors where
     low-level code gets unexpected pathspecs. We'd usually try to catch
     unsupported pathspecs by passing a magic_mask to parse_pathspec(),
     which would give the user a much better message like:

       pathspec magic not supported by this command: 'icase'

     That doesn't happen here because git-log usually _does_ support
     all types of pathspec magic, and so it passes "0" for the mask
     (this call actually happens in setup_revisions()). It needs to
     distinguish the normal case from the "--follow" one but currently
     doesn't.

  2. In addition to --follow, we have the log.follow config option. When
     that is set, we try to turn on --follow mode only when there is a
     single pathspec (since --follow doesn't handle anything else). But
     really, that ought to be expanded to "use --follow when the
     pathspec supports it". Otherwise, we'd complain any time you use an
     exotic pathspec:

       $ git config log.follow true
       $ git log ':(icase)makefile' >/dev/null
       BUG: tree-diff.c:596: unsupported magic 10
       Aborted

     We should instead just avoid enabling follow mode if it's not
     supported by this particular invocation.

This patch expands our diff_check_follow_pathspec() function to cover
pathspec magic, solving both problems.

A few final notes:

  - we could also solve (1) by passing the appropriate mask to
    parse_pathspec(). But that's not great for two reasons. One is that
    the error message is less precise. It says "magic not supported by
    this command", but really it is not the command, but rather the
    --follow option which is the problem. The second is that it always
    calls die(). But for our log.follow code, we want to speculatively
    ask "is this pathspec OK?" and just get a boolean result.

  - This is obviously the right thing to do for ':(icase)' and most
    other magic options. But ':(glob)' is a bit odd here. The --follow
    code doesn't support wildcards, but we allow them anyway. From
    try_to_follow_renames():

	#if 0
	        /*
	         * We should reject wildcards as well. Unfortunately we
	         * haven't got a reliable way to detect that 'foo\*bar' in
	         * fact has no wildcards. nowildcard_len is merely a hint for
	         * optimization. Let it slip for now until wildmatch is taught
	         * about dry-run mode and returns wildcard info.
	         */
	        if (opt->pathspec.has_wildcard)
	                BUG("wildcards are not supported");
	#endif

    So something like "git log --follow 'Make*'" is already doing the
    wrong thing, since ":(glob)" behavior is already the default (it is
    used only to countermand an earlier --noglob-pathspecs).

    So we _could_ loosen the guard to allow :(glob), since it just
    behaves the same as pathspecs do by default. But it seems like a
    backwards step to do so. It already doesn't work (it hits the BUG()
    case currently), and given that the user took an explicit step to
    say "this pathspec should glob", it is reasonable for us to say "no,
    --follow does not support globbing" (or in the case of log.follow,
    avoid turning on follow mode). Which is what happens after this
    patch.

  - The set of allowed pathspec magic is obviously the same as in
    GUARD_PATHSPEC(). We could perhaps factor these out to avoid
    repetition. The point of having separate masks and GUARD calls is
    that we don't necessarily know which parsed pathspecs will be used
    where. But in this case, the two are heavily correlated. Still,
    there may be some value in keeping them separate; it would make
    anyone think twice about adding new magic to the list in
    diff_check_follow_pathspec(). They'd need to touch
    try_to_follow_renames() as well, which is the code that would
    actually need to be updated to handle more exotic pathspecs.

  - The documentation for log.follow says that it enables --follow
    "...when a single <path> is given". We could possibly expand that to
    say "with no unsupported pathspec magic", but that raises the
    question of documenting which magic is supported. I think the
    existing wording of "single <path>" sufficiently encompasses the
    idea (the forbidden magic is stuff that might match multiple
    entries), and the spirit remains the same.

Reported-by: Jim Pryor <dubiousjim@gmail.com>
Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [pan93412/evals](https://github.com/pan93412/evals)@[ca0d7ad83b...](https://github.com/pan93412/evals/commit/ca0d7ad83b06e8de9dbf7325570cee65dfc85693)
#### Saturday 2023-06-03 03:11:05 by BlueFoxPrime

[evals] reverse sort english words (includes duplicates) (#876)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

## Eval details 📑
### Eval name
reverse-sort-words-eng

### Eval description

Each eval consists of 10 comma-separated english words that should be
sorted in correct reverse alphabetic order. Includes duplicate words. 25
samples.

### What makes this a useful eval?

- Evaluates ability to organizing words
- Evaluates ability to follow the exact guidance

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.
chris@multix.de

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "Sort the following
comma-separated words in reversed alphabetical order (respond as
concisely as possible and only include the comma-separated words in your
response):"}, {"role": "user", "content": "basketball, butter, giggle,
tranquil, match, venomous, miniature, captain, danger, hilarious"}],
"ideal": "tranquil, miniature, match, hill, hilarious, hilarious,
giggle, danger, butter, basketball"}
{"input": [{"role": "system", "content": "Sort the following
comma-separated words in reversed alphabetical order (respond as
concisely as possible and only include the comma-seperated words in your
response):"}, {"role": "user", "content": "moonlight, harmonica,
frosted, pineapple, aquamarine, thunderbolt, pineapple, carousel,
sapphire, palisade"}], "ideal": "thunderbolt, sapphire, pineapple,
pineapple, palisade, moonlight, harmonica, frosted, carousel,
aquamarine"}
{"input": [{"role": "system", "content": "Sort the following
comma-separated words in reversed alphabetical order (respond as
concisely as possible and only include the comma-seperated words in your
response):"}, {"role": "user", "content": "sapphire, blunderbuss,
zephyr, lollipop, effervescent, maelstrom, labyrinth, quagmire,
skedaddle, zephyr"}], "ideal": "zephyr, zephyr, skedaddle, sapphire,
quagmire, maelstrom, lollipop, labyrinth, effervescent, blunderbuss"}
{"input": [{"role": "system", "content": "Sort the following
comma-separated words in reversed alphabetical order (respond as
concisely as possible and only include the comma-seperated words in your
response):"}, {"role": "user", "content": "carnival, whisker, luxury,
midnight, crumble, wheat, whine, ivory, solar, chocolate"}], "ideal":
"whisker, whine, wheat, solar, midnight, luxury, ivory, crumble,
chocolate, carnival"}
{"input": [{"role": "system", "content": "Sort the following
comma-separated words in reversed alphabetical order (respond as
concisely as possible and only include the comma-seperated words in your
response):"}, {"role": "user", "content": "tree, apple, elephant,
carbon, house, tree, rainbow, pizza, computer, ocean"}], "ideal": "tree,
tree, rainbow, pizza, ocean, house, elephant, computer, carbon, apple"}
  ```
</details>

---
## [Elchanz3/Android_Kernel_Samsung_SDM845.](https://github.com/Elchanz3/Android_Kernel_Samsung_SDM845.)@[5c3fd1ad70...](https://github.com/Elchanz3/Android_Kernel_Samsung_SDM845./commit/5c3fd1ad707d678a640ae5322158f72674cd43e7)
#### Saturday 2023-06-03 03:24:57 by Douglas Anderson

serial: core: Allow processing sysrq at port unlock time

[ Upstream commit d6e1935819db0c91ce4a5af82466f3ab50d17346 ]

Right now serial drivers process sysrq keys deep in their character
receiving code.  This means that they've already grabbed their
port->lock spinlock.  This can end up getting in the way if we've go
to do serial stuff (especially kgdb) in response to the sysrq.

Serial drivers have various hacks in them to handle this.  Looking at
'8250_port.c' you can see that the console_write() skips locking if
we're in the sysrq handler.  Looking at 'msm_serial.c' you can see
that the port lock is dropped around uart_handle_sysrq_char().

It turns out that these hacks aren't exactly perfect.  If you have
lockdep turned on and use something like the 8250_port hack you'll get
a splat that looks like:

  WARNING: possible circular locking dependency detected
  [...] is trying to acquire lock:
  ... (console_owner){-.-.}, at: console_unlock+0x2e0/0x5e4

  but task is already holding lock:
  ... (&port_lock_key){-.-.}, at: serial8250_handle_irq+0x30/0xe4

  which lock already depends on the new lock.

  the existing dependency chain (in reverse order) is:

  -> #1 (&port_lock_key){-.-.}:
         _raw_spin_lock_irqsave+0x58/0x70
         serial8250_console_write+0xa8/0x250
         univ8250_console_write+0x40/0x4c
         console_unlock+0x528/0x5e4
         register_console+0x2c4/0x3b0
         uart_add_one_port+0x350/0x478
         serial8250_register_8250_port+0x350/0x3a8
         dw8250_probe+0x67c/0x754
         platform_drv_probe+0x58/0xa4
         really_probe+0x150/0x294
         driver_probe_device+0xac/0xe8
         __driver_attach+0x98/0xd0
         bus_for_each_dev+0x84/0xc8
         driver_attach+0x2c/0x34
         bus_add_driver+0xf0/0x1ec
         driver_register+0xb4/0x100
         __platform_driver_register+0x60/0x6c
         dw8250_platform_driver_init+0x20/0x28
	 ...

  -> #0 (console_owner){-.-.}:
         lock_acquire+0x1e8/0x214
         console_unlock+0x35c/0x5e4
         vprintk_emit+0x230/0x274
         vprintk_default+0x7c/0x84
         vprintk_func+0x190/0x1bc
         printk+0x80/0xa0
         __handle_sysrq+0x104/0x21c
         handle_sysrq+0x30/0x3c
         serial8250_read_char+0x15c/0x18c
         serial8250_rx_chars+0x34/0x74
         serial8250_handle_irq+0x9c/0xe4
         dw8250_handle_irq+0x98/0xcc
         serial8250_interrupt+0x50/0xe8
         ...

  other info that might help us debug this:

   Possible unsafe locking scenario:

         CPU0                    CPU1
         ----                    ----
    lock(&port_lock_key);
                                 lock(console_owner);
                                 lock(&port_lock_key);
    lock(console_owner);

   *** DEADLOCK ***

The hack used in 'msm_serial.c' doesn't cause the above splats but it
seems a bit ugly to unlock / lock our spinlock deep in our irq
handler.

It seems like we could defer processing the sysrq until the end of the
interrupt handler right after we've unlocked the port.  With this
scheme if a whole batch of sysrq characters comes in one irq then we
won't handle them all, but that seems like it should be a fine
compromise.

Signed-off-by: Douglas Anderson <dianders@chromium.org>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [EyeCantCU/BlueWhaleOS](https://github.com/EyeCantCU/BlueWhaleOS)@[21cc2df026...](https://github.com/EyeCantCU/BlueWhaleOS/commit/21cc2df026bc4477178ac7234b5ffd27c0f342d9)
#### Saturday 2023-06-03 04:08:11 by RJ Trujillo

feat: Add ugly way for users to change SDDM/kscreenlocker background

'etc' should not be used this way and requiring a specific wallpaper
path that requires superuser privledges to access is horrible... but
I can't honestly think of a better way to handle this at the moment

---
## [MysticalMusings/pytorch](https://github.com/MysticalMusings/pytorch)@[b5840f99c3...](https://github.com/MysticalMusings/pytorch/commit/b5840f99c3f2ae01b7831fd32b99758180fc22c3)
#### Saturday 2023-06-03 04:24:24 by Mark Saroufim

torch.compiler public namespace (#102182)

# torch.compiler public API

## Goal

The goal of this document is to describe the public facing API for torchdynamo and torchinductor.

Today both dynamo and torchinductor are in `torch/_dynamo` and `torch/_inductor` namespace with the only public function

`torch.compile()` which is directly placed in `torch/__init__.py`

This poses a few problems for users trying to take dependencies on PyTorch 2.0
1. Unclear BC guarantees
2. No builtin discovery mechanism outside of reading the source code
3. No hard requirements for docstrings or type annotations

Most importantly it mixes two personas the PyTorch 2.0 developer vs the PyTorch 2.0 customer so this is an attempt to address this. We draw a lot of inspiration from the `functorch` migration to the `func` namespace.

## Alternate names

We did discuss some other alternative names

1. `torch.compile` -> problem is this would break BC on the existing `torch.compile` function
2. `torch.dynamo` -> `dynamo` is so far not something we've deliberately hidden from users but problem is now figuring out what it's `_dynamo` vs `dynamo` might be confusing
3. `torch.compiler` -> 1 would be better but to keep BC this is a good compromise

# The general approach
## Proposal 1
In https://github.com/pytorch/pytorch/blob/main/torch/_dynamo/__init__.py

We have function called `reset()`, this function is essential if users are trying to `torch.compile()` a model under different settings

```python
# in _dynamo/
def reset():
    do_reset_stuff()
```

Instead we propose

```python
# in compiler/
def reset():
    do_reset_stuff() # As in copy paste the logic from _dynamo.reset

# in _dynamo/
import warnings
import inspect

def reset():
    function_name = inspect.currentframe().f_code.co_name
    warnings.warn(f"{function_name} is deprecated, use compiler.{function_name} instead", DeprecationWarning)
    return compiler.reset()

```
## Proposal 2

```python
# in compiler/
def reset():
    “””
    Docstrings here
    “””
    _dynamo.reset()

# in _dynamo/
No changes
```
Consensus so far seems to be proposal 2 since fewer warnings will be less jarring and it’ll make it quite easy to merge the public API

## Docstrings

The above was an example of a function that has no inputs or outputs but there are other functions which could use an improvement in their docstrings, for example allow_in_graph actually works over lists of functions but that’s not mentioned anywhere in the example only if you read the source code.

def allow_in_graph(fn):
    """
    Customize which functions TorchDynamo will include in the generated
    graph. Similar to `torch.fx.wrap()`.

    Parameters:
        fn (callable or list/tuple): The function(s) to be allowed in the graph.

    Returns:
        callable or list/tuple: The input function(s) included in the graph.

    Examples:
        Customize inclusion of a single function:
        ::
            torch._dynamo.allow_in_graph(my_custom_function)

        Customize inclusion of multiple functions:
        ::
            torch._dynamo.allow_in_graph([my_custom_function1, my_custom_function2])

        @torch._dynamo.optimize(...)
        def fn(a):
            x = torch.add(x, 1)
            x = my_custom_function(x)
            x = torch.add(x, 1)
            return x

        fn(...)

    Notes:
        The `allow_in_graph` function allows customization of which functions TorchDynamo
        includes in the generated graph. It can be used to include specific functions that
        are not automatically captured by TorchDynamo.

        If `fn` is a list or tuple, `allow_in_graph` will be called recursively on each
        element in the sequence.

        Once a function is allowed in the graph using `allow_in_graph`, it will be captured
        in the graph generated by TorchDynamo. This customization enables more fine-grained
        control over the functions included in the graph.

        Note that `allow_in_graph` expects the input `fn` to be a callable.

    """
    if isinstance(fn, (list, tuple)):
        return [allow_in_graph(x) for x in fn]
    assert callable(fn), "allow_in_graph expects a callable"
    allowed_functions._allowed_function_ids.add(id(fn))
    allowed_functions._disallowed_function_ids.remove(id(fn))
    return fn

So to make the API public, we’d have to write similar docstrings for all public functions we’d like to create.

The benefit of this approach is that
1. No BC risks, internal and external users relying on our tooling can slowly wean off the private functions.
2. We will also have to write correct docstrings which will automatically make our documentation easier to maintain and render correctly on pytorch.org
3. We already have some BC guarantees already, we don’t kill OptimizedModule, we rejected the PR to change the config system

The con of this approach is that
Will be stuck with some potentially suboptimal functions/classes that you can’t kill

## Testing strategy
If the approach is to mostly make a public function call an already tested private function then all we need to do is ensure that the function signatures don't change

## Which functions should be in the public API

Our heuristic for deciding whether something should be public or not is are users already relying on it for lack of other options or have we recommended some non public functions for users to debug their PT 2.0 programs.

Heuristic for not putting something in public is that it’s an experimental subsystem with the goal of turning it on by default, it’s very core dev centric, meta centric, a bunch of different configs that should be batched into a single user facing one, or something that needs to be renamed because the name is confusing

#### Top level
`torch.compile()` -> already is a public API it does require some minor improvements like having configs be passed in to any backend and not just inductor (EDIT: This was already done https://github.com/pytorch/pytorch/pull/99645l) and renaming `mode=reduce-overhead` to `mode=cudagraph`

To make sure that PT 2.0 is supported with a given pytorch version users can create a new public function and this would replace the need for `try/except` blocks around `import torch._dynamo` that has been populating user code.

```python
def pt2_enabled():
    if hasattr(torch, 'compile'):
        return True
    else:
        return False
```

For all of the below they will be translated to `torch.compiler.function_name()`

#### From _dynamo

As a starting point we looked at https://github.com/pytorch/pytorch/blob/main/torch/_dynamo/__init__.py and we suggest redefining these functions in `pytorch/torch/compiler/__init__.py`

It might also make sense to split them over multiple files and import them in `__init__.py` but because the number of functions is small it'd probably be fine to add them all into a single compiler/__init__.py until this list becomes larger

1. `reset()`
2. `allow_in_graph()`
10. `list_backends()`
12. `compile()`:  torch.compile() would be mostly a shell function passing arguments to torch.compiler.compile()
13. `assume_constant_result()`: TODO: Double check how this is useful
15. `torch._dynamo.disable()`

Some notable omissions
11. `explain()`: We need to clean up the output for this function, make it a data class and pretty printable
1. `forbid_in_graph()`: Considered adding this but should instead consolidate on `disallow_in_graph`
2. `optimize_assert()`: Already covered by `torch.compile(fullgraph=True)`
3. `check_if_dynamo_supported()`: this would be supplanted by pt2_enabled()
4. `compilation_metrics`, `graph_breaks_reasons` ..: would all be accessed via `torch.compiler.explain()`
5. `replay` does not seem useful to end customers
6. . `graph_break()`: Mostly useful for debugging or unit tests
9. `register_backend()`: End users will just pass a string backend to torch.compile, only devs will create new backends
10. `export()` : Eventually this needs to public but for now it’s not ready so just highlighting that it will be in the public API eventually
11. `disallow_in_graph()`: Usage is limited
12. `mark_static()`: we can keep this private until dynamic=True is recommended in stable
13. `mark_dynamic()`:  we can keep this private until dynamic=True is recommended in trunk
14. 8. `OptimizedModule`: This is the only class that we'd expose but is crucial since users are running code like `if isinstance(mod, OptimizedModule): torch.save(mod._orig_mod)` EDIT: because we fixed pickling we no longer need to
expose this
15. `is_compiling()`: Still not clear how this useful to end users

There are also config variables which we need to expose https://github.com/pytorch/pytorch/blob/main/torch/_dynamo/config.py

Some of our configs are useful dev flags, others are to gate experimental functionality and others are essential debugging tools and we seperate out the essential debugging and logging tools to a public facing config.

TODO: I still need to think of a good way of porting the config in a BC way here are some ideas
1. Just make all passes available and controllable via `torch.compile(options={})` but only show docstrings for the ones users should care about.

The current problem with our config system is we have 3 ways of setting them once via `options={}`, environment variables and variables in `config.py`, it'd be worth settling on one source of truth and have that be the public API.

The configs we should make public are
1. `log_file_name`
2. `verbose`
3. `cache_size_limit`
4. `repro_level` and `repro_after`: Although we can rename these to minifier and give human readable names to the levels

Everything else should stay private in particular

1. `print_graph_breaks`, `print_specializations`: should be supplanted by `explain()` for public users
2. dynamic shape configs : Users should only have to worry about `torch.compile(dynamic=True/False)`
3. The distributed flags, hook or guard configs: If we tell a user to use FSDP and DDP then the flag should be enabled by default or be in a private namespace
4. The fbcode flags: Obviously no need to be user facing
5. Skip/Allow lists: Not something normal users should play around with

#### From _inductor
Very little of inductor should be exposed in a public facing API, our core audience as in people writing models mostly just need information on what certain passes mean and how to control them a high level and they can do this with `torch.compile(options={})` so the goal here should be more to make available passes clearer and ideally consolidate them into `torch.compile()` docstrings or modes.

There are some exceptions though from https://github.com/pytorch/pytorch/blob/main/torch/_inductor/__init__.py

1. `list_mode_options()`
2. `list_options()`: this needs an additional pass to hide internal or debug options

For both of these we’d rename them to compiler.inductor_list_mode_options and compiler.inductor_list_options() since they would be in the same init file as the one for dynamo

Notable omissions
1. `_inductor.compile()`: Because of users are coming in with their own fx graph, they are likely developers
2. `_inductor.aot_compile()`:Again this is about capturing and modifying fx graphs so users APIs don't need to be public

However the configs are a slightly different story, because we can choose to either
1. Make all configs public
2. Make some configs public and keep most of the private ones. If public config is set it should override the private version
3. Make all configs controllable via `torch.compile(options={})` but make list_options() hide more things

For now 3 seems like the most reasonable choice with some high level configs we’ll keep like TORCH_COMPILE_DEBUG

Regardless here's what should probably be public or advertised more
1. `disable_progress` and verbose_progress:  Combine and enable by default
2. `fallback_random`: We could make the case this shouldn't be public if a top level deterministic mode enables this
3. `profile_bandwidth`: Or could make the case that this should be in TORCH_COMPILE_DEBUG

Notable omissions
1. Any config that would generally improve performance for most that we should probably enable by default but might be disabled in the short term because of stability: example `epilogue_fusion`, `pattern_matcher`, `reordering`
2. Autotuning flags: Should just sit behind `torch.compile(mode="max-autotune")` like `max_autotune`, `max_autotune_gemm`
3. `coordinate_descent_tuning`: This one I'm a but mixed about, maybe it just also fall into `mode="max-autotune"`
4. `trace`: `TORCH_COMPILE_DEBUG` is the best flag for all of this
5. `triton.cudagraphs`: Default should be `torch.compile(mode="reduce-overhead")` - I'd go further and rename the `mode=cudagraph` and we can keep reduce-overhead for BC reasons
6. `triton_unique_kernel_names`: Mostly useful for devs debugging
7. `dce`: which doesnt really do anything
8. `shape_padding`: Elias is working on enabling this by default in which case we also remove it

## Mechanics

This PR would include the public functions with their docstrings

Another PR will take a stab at the configs

And for work where the APIs are still being cleaned up whether its minifier or escape hatches, export or dynamic shapes, aot_inductor etc.. we’ll keep them private until a public commitment can be made

Pull Request resolved: https://github.com/pytorch/pytorch/pull/102182
Approved by: https://github.com/jansel

---
## [datalayer-externals/jupyter-ipython](https://github.com/datalayer-externals/jupyter-ipython)@[b518e6a546...](https://github.com/datalayer-externals/jupyter-ipython/commit/b518e6a546ef99e00c2a2fbdf35122ee341057aa)
#### Saturday 2023-06-03 04:43:28 by Matthias Bussonnier

Add option to `%autoreload` to hide errors when reloading code (#14056)

* We have `%autoreload` enabled by default in Spyder and think it's a
bit annoying to show its error messages to users because they make
little sense to them. These errors are not uncommon when you are working
with some code that is slightly different between two git branches.
* However, I didn't change the current behavior (i.e. showing errors)
because it's been like that for as long as I can remember. We'd simply
use the new `--hide-errors` option in our kernel.

---
## [colebrookson/kx-sea-lice](https://github.com/colebrookson/kx-sea-lice)@[053f19cb82...](https://github.com/colebrookson/kx-sea-lice/commit/053f19cb820f6ed56939daca0c64223888760c93)
#### Saturday 2023-06-03 04:57:12 by colebrookson

Revert "cannot fucking figure out a solution to this bullshit oh my god"

This reverts commit 5dd882e29e3d7027b77403f60638d7e033eef47b.

---
## [Iceayydev/ambrosial](https://github.com/Iceayydev/ambrosial)@[711a0ed630...](https://github.com/Iceayydev/ambrosial/commit/711a0ed6309d8f3bd56628665631133d72bf370b)
#### Saturday 2023-06-03 05:18:01 by Iceayy

Update AmbrosialEncrypt.cs (silly edition)

iceayy contribution attempt #1

removed alphaChars var ssince it was declared as private static, but never used outside of the GenerateRandomString method.. so we get rid of it!!! no more!! we hate!!!!!!!!!

removed checked keyword from GenerateRandomString method. it WAS used to make sure that integer arithmetic operations dont overflow, but this simply does not lol because the min value of the int is larger than the length of the alphachars string

replaced the strings.mid method with the char indexy thingamabooby. was uused to extract a single char from a string, buuuut we simplify by using the char indexer so it can be used to access a single char at a specific index in a string.

my c# skills are so silly
make sure to like and subscribe for more silly pull requests on the silliest website half of all programs rely on to not die randomly.

---
## [Nanu308/cmss13](https://github.com/Nanu308/cmss13)@[e8f53984c1...](https://github.com/Nanu308/cmss13/commit/e8f53984c1edd98c25b4c3199a6a5363eaa26869)
#### Saturday 2023-06-03 06:07:49 by morrowwolf

Warrior Nerf (#3424)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

This PR removes cooldown reduction on slash.

This PR slightly lowers fling and punch cooldowns.

This PR lowers fling stun to a micro stun and adds a slow.

This PR decreases lunge range to 4 tiles.

As a reminder design feedback and balance concerns go here:
https://forum.cm-ss13.com/w/pr-feedback/steps/step_1

# Explain why it's good for the game

Warrior rework has been on my mind for a while. I'm not quite sure how I
want to do it. The cooldowns on abilities and the abilities themselves
are incredibly powerful crowd control and just a few warriors can do
immense damage to large groups of marines. It's just... not in a great
place for a T2 and sadly I don't have a thorough game plan yet to rework
it into something more bearable while equally enjoyable to play. In the
mean time, this is what we're getting. Am I promising a rework in the
near future? Not really. It's on my list somewhere. Does warrior need
some changing around? Yeah.

Overall, this should make warrior a bit more bearable. We'll see. More
changes as testing goes.

# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

:cl: Morrow
balance: Removes warrior cooldown reduction on slash
balance: Warrior slightly lowered fling and punch cooldowns
balance: Lowers fling stun to a micro stun and adds a slow
balance: Decreases warrior lunge range to 4 tiles
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [MrStonedOne/tgstation](https://github.com/MrStonedOne/tgstation)@[9df4b392c3...](https://github.com/MrStonedOne/tgstation/commit/9df4b392c3cca6f277cd606a295014da69776bf7)
#### Saturday 2023-06-03 06:31:53 by Kyle Spier-Swenson

fix stupid error message in delay pre-game

tabbing out during init after hitting the verb, while you wait for the server to un-lockup and present you with the prompt, and coming back in, noticing you were too late, and cancelling out of the time prompt, only to get told the round had already started, was kinda fucking lame.

---
## [Deepak-183/relax](https://github.com/Deepak-183/relax)@[f59412c2d6...](https://github.com/Deepak-183/relax/commit/f59412c2d6016edd4c9788c838b59554f746aa0d)
#### Saturday 2023-06-03 06:39:38 by Deepak-183

Update TODOLIST.java

Problem

CodeChef recently revamped its practice page to make it easier for users to identify the next problems they should solve by introducing some new features:

    Recent Contest Problems - contains only problems from the last 2 contests
    Separate Un-Attempted, Attempted, and All tabs
    Problem Difficulty Rating - the Recommended dropdown menu has various difficulty ranges so that you can attempt the problems most suited to your experience
    Popular Topics and Tags

Like most users, Chef didn’t know that he could add problems to a personal to-do list by clicking on the magic '+' symbol on the top-right of each problem page. But once he found out about it, he went crazy and added loads of problems to his to-do list without looking at their difficulty rating.

Chef is a beginner and should ideally try and solve only problems with difficulty rating strictly less than 10001000. Given a list of difficulty ratings for problems in the Chef’s to-do list, please help him identify how many of those problems Chef should remove from his to-do list, so that he is only left with problems of difficulty rating less than 10001000.
Input Format

    The first line of input will contain a single integer TT, the number of test cases. Then the testcases follow.
    Each testcase consists of 2 lines of input.
    The first line of input of each test case contains a single integer, NN, which is the total number of problems that the Chef has added to his to-do list.
    The second line of input of each test case contains NN space-separated integers D1,D2,…,DND1​,D2​,…,DN​, which are the difficulty ratings for each problem in the to-do list.

Output Format

For each test case, output in a single line the number of problems that Chef will have to remove so that all remaining problems have a difficulty rating strictly less than 10001000.
Constraints

    1≤T≤10001≤T≤1000
    1≤N≤10001≤N≤1000
    1≤Di≤50001≤Di​≤5000

Subtasks

    Subtask 1 (100 points):
        Original constraints

Sample 1:
Input
Output

5
3
800 1200 900
4
999 1000 1001 1002
5
1 2 2 2 5000
5
1000 1000 1000 1000 1000
3
900 700 800

1
3
1
5
0

Explanation:

Test case 11: Among the three difficulty ratings, Chef only needs to remove the problem with difficulty rating 12001200, since it is ≥1000≥1000. So, the answer is 11.

Test case 22: Among the four difficulty ratings, Chef needs to remove the problems with difficulty ratings of 10001000, 10011001, and 10021002, since they are ≥1000≥1000. So, the answer is 33.

Test case 33: Among the five difficulty ratings, Chef needs to remove the problem with a difficulty rating of 50005000, since it is ≥1000≥1000. So, the answer is 11.

Test case 44: Chef needs to remove all the five problems, since they are all rated ≥1000≥1000. So, the answer is 55.

Test case 55: Chef does not need to remove any problem, since they are all rated <1000<1000. So, the answer is 00.

---
## [Offroaders123/NBTify](https://github.com/Offroaders123/NBTify)@[09f5fac553...](https://github.com/Offroaders123/NBTify/commit/09f5fac5535124162af1bf1f5fe4693a2dd1436a)
#### Saturday 2023-06-03 08:00:34 by Offroaders123

Awesome Video Inspiration

Was liking the idea of coding tonight, but I found some super sick videos to watch for a bit instead. Lots of great info, both about programming, and music. Super glad I went with it. Nice little refresher for the brain, had to make note of these as great resources, even though it's not actually related to this project specifically.

going fast is about doing less
https://www.youtube.com/watch?v=5rb0vvJ7NCY

it took me 1 month to fix this compiler bug
https://www.youtube.com/watch?v=kESmRMDHZZk

The Downbeat Podcast - Matt Garstka (Animals As Leaders)
https://www.youtube.com/watch?v=mg3LUlSjAg0

Hardcore Drummer Spills RED MISO SOUP All Over His DRUMS (shut up bro)
https://www.youtube.com/watch?v=Y-o2XLiT2os

---
## [jonathanagustin/evals](https://github.com/jonathanagustin/evals)@[ab5f7b2a89...](https://github.com/jonathanagustin/evals/commit/ab5f7b2a89bcf60e8e93adfb2c70688c6d6ffd44)
#### Saturday 2023-06-03 08:24:29 by oscar-king

Counting bigrams in sentences (#302)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
Bigram Counting

### Eval description

Tests whether the model is able to count the frequency of bigrams in a
sentence.

### What makes this a useful eval?

This is a very simple task for humans and it's possibly slightly more
'difficult' than counting the occurrences of a single letter.

Bigram frequencies are used in applications ranging from rudimentary NLP
tasks to cryptography.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.jsonl`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input":[{"role":"system","content":"You will be presented with a
sentence. The task is to count the frequency of the bigram 'ng'. After
reading the sentence tell me the number of times the bigram appeared by
saying 'X' where 'X' is the frequency."},{"role":"user","content":"I'm
worried by the fact that my daughter looks to the local carpet seller as
a role model."}],"ideal":"0"}
{"input":[{"role":"system","content":"You will be presented with a
sentence. The task is to count the frequency of the bigram 'ng'. After
reading the sentence tell me the number of times the bigram appeared by
saying 'X' where 'X' is the frequency."},{"role":"user","content":"He
found rain fascinating yet unpleasant."}],"ideal":"1"}
{"input":[{"role":"system","content":"You will be presented with a
sentence. The task is to count the frequency of the bigram 'ng'. After
reading the sentence tell me the number of times the bigram appeared by
saying 'X' where 'X' is the frequency."},{"role":"user","content":"The
near-death experience brought new ideas to light."}],"ideal":"0"}
{"input":[{"role":"system","content":"You will be presented with a
sentence. The task is to count the frequency of the bigram 'ng'. After
reading the sentence tell me the number of times the bigram appeared by
saying 'X' where 'X' is the
frequency."},{"role":"user","content":"Separation anxiety is what
happens when you can't find your phone."}],"ideal":"0"}
{"input":[{"role":"system","content":"You will be presented with a
sentence. The task is to count the frequency of the bigram 'ng'. After
reading the sentence tell me the number of times the bigram appeared by
saying 'X' where 'X' is the frequency."},{"role":"user","content":"He
realized there had been several deaths on this road, but his concern
rose when he saw the exact number."}],"ideal":"0"}
  ```
</details>

---
## [jonathanagustin/evals](https://github.com/jonathanagustin/evals)@[b5da073c21...](https://github.com/jonathanagustin/evals/commit/b5da073c215c6453b99269a6dab2dca5454f04dd)
#### Saturday 2023-06-03 08:24:29 by somerandomguyontheweb

Add Belarusian lexicon eval (#372)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name

belarusian-lexicon

### Eval description

Test the model's ability to distinguish between existing and
hallucinated Belarusian words.

### What makes this a useful eval?

While the multilingual capability of recent GPT models is impressive,
there is still room for improvement. Many human languages are lagging
far behind English in terms of the model's ability to answer questions
and produce coherent texts in these languages, and the model's
"knowledge" of their lexicon and grammar is, to some extent,
hallucinated. One example is Belarusian, an East Slavic language spoken
by several million people. In my experience with ChatGPT, when the model
is prompted in Belarusian, its responses are sometimes ungrammatical or
semantically incoherent, and very often they contain made-up words – a
possible sign of overgeneralization based on Russian and Ukrainian data,
which are much more
[abundant](https://commoncrawl.github.io/cc-crawl-statistics/plots/languages)
on the web than Belarusian.

This eval contains 150 pairs of single-word prompts: one item in each
pair is a non-word hallucinated by ChatGPT (either totally meaningless
in Belarusian or violating the language's orthographic and phonetic
rules), and another item is an actual Belarusian word with similar
spelling. The model's task is to distinguish between words and
non-words. ChatGPT tends to label most items as existing words,
therefore its accuracy appears to be around 50%, and the negative-class
F measure is very low. Any competent speaker of Belarusian would perform
much better, and a language-specific tool, such as [this spell
checker](https://corpus.by/SpellChecker) or [this grammatical
database](https://bnkorpus.info/grammar.en.html) of Belarusian (also
available for
[download](https://github.com/Belarus/GrammarDB/releases)), would
flawlessly identify non-words.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

This eval an attempt to point out specific deficiencies in the model's
ability to handle a lower-resource language (Belarusian). As such, it
might not only benchmark future refinements of Belarusian language
capability in the GPT models, but also serve as an instructuve example
for other language communities.

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абвязкою"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абвязкаю"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абласці"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "вобласці"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абмяну"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абмену"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абоўязак"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абавязак"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "аднасінькіх"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "аднюсенькіх"}], "ideal": "Y"}
  ```
</details>

---
## [jonathanagustin/evals](https://github.com/jonathanagustin/evals)@[d0e7844c48...](https://github.com/jonathanagustin/evals/commit/d0e7844c482b7b65961bc80dad64559ff8ffa488)
#### Saturday 2023-06-03 08:26:33 by Derek Pisner

Add emotional intelligence evaluation (#589)

## Eval details 📑
### Eval name
Emotional Intelligence

### Eval description
Evaluates GPT's ability to understand and manage emotional situations
using modified versions of the well-validated, public (i.e.
license-unrestricted) tests first developed by MacCann & Roberts (2008).
Items have actually here been aggregated across three different scales--
the STEU and STEM adult measures, along with a dozen questions from the
youth measure.

Keep in mind that there is not expectation that AI models like GPT-4
should be able to process emotions, so applying any emotional
intelligence test to them should be taken with a grain of salt. These
tests can only measure the AI's ability to understand and analyze
emotional information, not the AI's emotional intelligence in the human
sense.

### What makes this a useful eval?
This eval is useful because it assesses the AI model's ability to
navigate complex or ambiguous emotional situations, which is an
important aspect of human-like communication and problem-solving. By
evaluating the model's performance in this unique domain, we can
identify areas for improvement and better understand its limitations
when it comes to handling emotional contexts. This is particularly
important when considering AI applications that involve interactions
with humans, such as chatbots, personal assistants, and customer support
systems. A better understanding of emotional intelligence can
potentially lead to more natural and effective interactions between AI
models and their users.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

This Emotional Intelligence eval provides a unique value because by
testing GPT's capacity to understand and manage emotions, we can gain
insights into the model's strengths and weaknesses in a more
human-centric context. Relatedly, this eval also emphasizes the
importance of empathy and emotional understanding in AI systems that are
designed to interact with humans. By evaluating GPT's performance in
this way, we can contribute to the ongoing development of AI models that
are more attuned to human emotions and can provide better support in
emotionally charged situations, such as mental health counseling, crisis
management, and conflict resolution. Moreover, this Emotional
Intelligence eval can serve as a foundation for further research and
development in the field of AI and emotional understanding, paving the
way for more sophisticated AI models capable of handling complex human
emotions and fostering more effective communication.

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval
(data is publicly available on OSF, and does not have usage
restrictions)

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

**_I already have access to the 8k GPT-4 API, but I am kindly requesting
access to the 32k as soon as it becomes available._**

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Performance:
GPT-4: accuracy=0.48

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You are now an emotionally
intelligent AI. In this test, you will be presented with a few brief
details about an emotional situation, and asked to choose from four
responses the most effective course of action to manage both the
emotions the person is feeling and the problems they face in that
situation. Although more than one course of action might be acceptable,
you are asked to choose what you think the most effective response for
that person in that situation would be. Remember, you are not
necessarily choosing what you would do, or the nicest thing to do, but
choosing the most effective response for that situation. Select one or
more response(s) by returning the one or more corresponding lowercase
letter(s) ('a', 'b', 'c', or 'd'), and, if you selected more than one,
sorting them, separated by hyphen, in the order that you think best
ranks them from most to least effective, within the context of the
vignette provided."}, {"role": "user", "content": "Lee's workmate fails
to deliver an important piece of information on time, causing Lee to
fall behind schedule also. What action would be the most effective for
Lee? (a) Work harder to compensate; (b) Get angry with the workmate; (c)
Explain the urgency of the situation to the workmate; (d) Never rely on
that workmate again."}], "ideal": "c"}
{"input": [{"role": "system", "content": "You are now an emotionally
intelligent AI. In this test, you will be presented with a few brief
details about an emotional situation, and asked to choose from four
responses the most effective course of action to manage both the
emotions the person is feeling and the problems they face in that
situation. Although more than one course of action might be acceptable,
you are asked to choose what you think the most effective response for
that person in that situation would be. Remember, you are not
necessarily choosing what you would do, or the nicest thing to do, but
choosing the most effective response for that situation. Select one or
more response(s) by returning the one or more corresponding lowercase
letter(s) ('a', 'b', 'c', or 'd'), and, if you selected more than one,
sorting them, separated by hyphen, in the order that you think best
ranks them from most to least effective, within the context of the
vignette provided."}, {"role": "user", "content": "Rhea has left her job
to be a full-time mother, which she loves, but she misses the company
and companionship of her workmates. What action would be the most
effective for Rhea? (a) Enjoy being a full-time mom; (b) Try to see her
old workmates socially, inviting them out; (c) Join a playgroup or
social group of new mothers; (d) See if she can find part time work."}],
"ideal": "c-b-d"}
{"input": [{"role": "system", "content": "You are now an emotionally
intelligent AI. In this test, you will be presented with a few brief
details about an emotional situation, and asked to choose from four
responses the most effective course of action to manage both the
emotions the person is feeling and the problems they face in that
situation. Although more than one course of action might be acceptable,
you are asked to choose what you think the most effective response for
that person in that situation would be. Remember, you are not
necessarily choosing what you would do, or the nicest thing to do, but
choosing the most effective response for that situation. Select one or
more response(s) by returning the one or more corresponding lowercase
letter(s) ('a', 'b', 'c', or 'd'), and, if you selected more than one,
sorting them, separated by hyphen, in the order that you think best
ranks them from most to least effective, within the context of the
vignette provided."}, {"role": "user", "content": "Pete has specific
skills that his workmates do not and he feels that his workload is
higher because of it. What action would be the most effective for Pete?
(a) Speak to his boss about this; (b) Start looking for a new job; (c)
Be very proud of his unique skills; (d) Speak to his workmates about
this."}], "ideal": "a-c-d"}
{"input": [{"role": "system", "content": "You are now an emotionally
intelligent AI. In this test, you will be presented with a few brief
details about an emotional situation, and asked to choose from four
responses the most effective course of action to manage both the
emotions the person is feeling and the problems they face in that
situation. Although more than one course of action might be acceptable,
you are asked to choose what you think the most effective response for
that person in that situation would be. Remember, you are not
necessarily choosing what you would do, or the nicest thing to do, but
choosing the most effective response for that situation. Select one or
more response(s) by returning the one or more corresponding lowercase
letter(s) ('a', 'b', 'c', or 'd'), and, if you selected more than one,
sorting them, separated by hyphen, in the order that you think best
ranks them from most to least effective, within the context of the
vignette provided."}, {"role": "user", "content": "Mario is showing Min,
a new employee, how the system works. Mario's boss walks by and
announces Mario is wrong about several points, as changes have been
made. Mario gets on well with his boss, although they don't normally
have much to do with each other. What action would be the most effective
for Mario? (a) Make a joke to Min, explaining he didn't know about the
changes; (b) Not worry about it, just ignore the interruption; (c) Learn
the new changes; (d) Tell the boss that such criticism was
inappropriate."}], "ideal": "a-d-c"}
{"input": [{"role": "system", "content": "You are now an emotionally
intelligent AI. In this test, you will be presented with a few brief
details about an emotional situation, and asked to choose from four
responses the most effective course of action to manage both the
emotions the person is feeling and the problems they face in that
situation. Although more than one course of action might be acceptable,
you are asked to choose what you think the most effective response for
that person in that situation would be. Remember, you are not
necessarily choosing what you would do, or the nicest thing to do, but
choosing the most effective response for that situation. Select one or
more response(s) by returning the one or more corresponding lowercase
letter(s) ('a', 'b', 'c', or 'd'), and, if you selected more than one,
sorting them, separated by hyphen, in the order that you think best
ranks them from most to least effective, within the context of the
vignette provided."}, {"role": "user", "content": "Wai-Hin and Connie
have shared an office for years but Wai-Hin gets a new job and Connie
loses contact with her. What action would be the most effective for
Connie? (a) Just accept that she is gone and the friendship is over; (b)
Ring Wai-Hin an ask her out for lunch or coffee to catch up; (c) Contact
Wai-Hin and arrange to catch up but also make friends with her
replacement; (d) Spend time getting to know the other people in the
office, and strike up new friendships."}], "ideal": "c-d"}
  ```
</details>

---------

Co-authored-by: dpys <dpisner@clairity.com>

---
## [jonathanagustin/evals](https://github.com/jonathanagustin/evals)@[fabca8cebb...](https://github.com/jonathanagustin/evals/commit/fabca8cebb3f8e14d1f374e448533e0bde6e5a68)
#### Saturday 2023-06-03 08:26:33 by Nick Clyde

Heart Disease Prediction (#538)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
Heart Disease Prediction

### Eval description

This eval tests the models ability to correctly predict the probability
of a patient to have heart disease. The dataset is constructed from the
[Heart Failure Prediction
Dataset](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction)
on Kaggle. The data includes the patient's age, sex, and a number of
medical signals relevant to the diagnosis of heart disease.

The data is provided under the Open Database License (ODbL). 

```
fedesoriano. (September 2021). Heart Failure Prediction Dataset. Retrieved [Mar 31, 2023] from https://www.kaggle.com/fedesoriano/heart-failure-prediction.
```

### What makes this a useful eval?

This assesses the model's ability to correctly predict adverse medical
events. Correctly predicting heart disease shows the model's capability
for a strong understanding of medicine. The GPT-3.5-turbo models
currently receives an accuracy of 0.778.

<img width="1250" alt="Screenshot 2023-03-31 at 2 24 13 PM"
src="https://user-images.githubusercontent.com/9121162/229234376-9cdd1315-5df0-48bf-9328-ac31aabec3cc.png">

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

As far as I can tell, this is the only eval so far related to making
medical diagnoses. To make sure it was a high quality eval, I tried to
find a dataset with a lot of observations and created by doctors with
the relevant expertise.

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You are an AI tasked with
predicting whether patients are likely to have heart disease. You will
be given a description of the patient with relevant medical signals.
Respond with only a 1 to signify if the patient is likely to have heart
disease, or a 0 if the patient is not likely to have heart disease. Do
not respond with any text or disclaimers, only respond with either 1 or
0."}, {"role": "user", "content": "Age: 40 years, Sex: Male, Chest pain
type: Atypical Angina, Resting blood pressure: 140 mm Hg, Serum
cholesterol: 289 mg/dl, Fasting blood sugar: <= 120 mg/dl, Resting ECG
results: Normal, Max heart rate achieved: 172, Exercise induced angina:
No, Oldpeak: 0, ST Slope: Upsloping"}], "ideal": "0"}
{"input": [{"role": "system", "content": "You are an AI tasked with
predicting whether patients are likely to have heart disease. You will
be given a description of the patient with relevant medical signals.
Respond with only a 1 to signify if the patient is likely to have heart
disease, or a 0 if the patient is not likely to have heart disease. Do
not respond with any text or disclaimers, only respond with either 1 or
0."}, {"role": "user", "content": "Age: 49 years, Sex: Female, Chest
pain type: Non-Anginal Pain, Resting blood pressure: 160 mm Hg, Serum
cholesterol: 180 mg/dl, Fasting blood sugar: <= 120 mg/dl, Resting ECG
results: Normal, Max heart rate achieved: 156, Exercise induced angina:
No, Oldpeak: 1, ST Slope: Flat"}], "ideal": "1"}
{"input": [{"role": "system", "content": "You are an AI tasked with
predicting whether patients are likely to have heart disease. You will
be given a description of the patient with relevant medical signals.
Respond with only a 1 to signify if the patient is likely to have heart
disease, or a 0 if the patient is not likely to have heart disease. Do
not respond with any text or disclaimers, only respond with either 1 or
0."}, {"role": "user", "content": "Age: 37 years, Sex: Male, Chest pain
type: Atypical Angina, Resting blood pressure: 130 mm Hg, Serum
cholesterol: 283 mg/dl, Fasting blood sugar: <= 120 mg/dl, Resting ECG
results: ST-T wave abnormality, Max heart rate achieved: 98, Exercise
induced angina: No, Oldpeak: 0, ST Slope: Upsloping"}], "ideal": "0"}
{"input": [{"role": "system", "content": "You are an AI tasked with
predicting whether patients are likely to have heart disease. You will
be given a description of the patient with relevant medical signals.
Respond with only a 1 to signify if the patient is likely to have heart
disease, or a 0 if the patient is not likely to have heart disease. Do
not respond with any text or disclaimers, only respond with either 1 or
0."}, {"role": "user", "content": "Age: 48 years, Sex: Female, Chest
pain type: Asymptomatic, Resting blood pressure: 138 mm Hg, Serum
cholesterol: 214 mg/dl, Fasting blood sugar: <= 120 mg/dl, Resting ECG
results: Normal, Max heart rate achieved: 108, Exercise induced angina:
Yes, Oldpeak: 1.5, ST Slope: Flat"}], "ideal": "1"}
{"input": [{"role": "system", "content": "You are an AI tasked with
predicting whether patients are likely to have heart disease. You will
be given a description of the patient with relevant medical signals.
Respond with only a 1 to signify if the patient is likely to have heart
disease, or a 0 if the patient is not likely to have heart disease. Do
not respond with any text or disclaimers, only respond with either 1 or
0."}, {"role": "user", "content": "Age: 54 years, Sex: Male, Chest pain
type: Non-Anginal Pain, Resting blood pressure: 150 mm Hg, Serum
cholesterol: 195 mg/dl, Fasting blood sugar: <= 120 mg/dl, Resting ECG
results: Normal, Max heart rate achieved: 122, Exercise induced angina:
No, Oldpeak: 0, ST Slope: Upsloping"}], "ideal": "0"}
  ```
</details>

---
## [jonathanagustin/evals](https://github.com/jonathanagustin/evals)@[776e4fa212...](https://github.com/jonathanagustin/evals/commit/776e4fa212288be152c3030cf36fd04c8d939230)
#### Saturday 2023-06-03 08:26:33 by JPrenter

Financial Math (Evals) (#566)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
finance

### Eval description

Asks the model to calculate how much interest would be owed on a credit
card by a certain date, if a payment was made once but debt remains on
the card.

### What makes this a useful eval?

Finance is likely to be one of the biggest opportunities for LLMs to be
useful, because financial education is incredibly poor globally and the
impact of a mistake in financial calculations is severe. This eval tests
the models ability to combine math with its understanding of a topic
(finance). We plan to use this type of math at
[Dollarwise](https://www.dollarwise.ca) frequently going forward,
including integration into your comparison products. However, for this
to work reliably it's important that the model here can natively
understand financial concepts and apply math to them.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [X] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [X] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [X] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [X] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [X] Check that your data is in `evals/registry/data/{name}`
- [X] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [X] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [X] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [X] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [X] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [X] I have filled out all required fields in the evals PR form
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "On the 24th of September,
Sarah had spent $1237.42 on her credit card for the month of September.
This credit card charges 21.99% interest rate annually on outstanding
credit starting on the 1st of the following month. Presume that interest
is only charged at the end of each additional day. Example: From the 1st
of the month to the 8th would be 7 days of interest accrued.Today is the
27th of September and Sarah makes a payment of $125 towards her credit
card. How much interest will she have been charged by October 15th if
she makes no additional payments? If the final interest figure is more
than 2-decimal places, always round down. Answer ONLY with a dollar
figure. Do not output any logic, output only the dollar figure for how
much interest she was charged for the period."}], "ideal": "9.42"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "On the 19th of February,
Jason had spent $15.21 on his credit card for the month of February.
This credit card charges 21.99% interest rate annually on outstanding
credit starting on the 1st of the following month. Presume that interest
is only charged at the end of each additional day. Example: From the 1st
of the month to the 8th would be 7 days of interest accrued. Today is
the 23rd of February and he makes a payment of $1 towards his credit
card. How much interest will he have been charged by March 10th if he
makes no additional payments? If the final interest figure is more than
2-decimal places, always round down. Answer ONLY with a dollar figure.
Do not output any logic, output only the dollar figure for how much
interest she was charged for the period."}], "ideal": "0.07"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "On the 12th of February,
Jason had spent $10,674.21 on his credit card for the month of February.
This credit card charges 21.99% interest rate annually on outstanding
credit starting on the 1st of the following month. Presume that interest
is only charged at the end of each additional day. Example: From the 1st
of the month to the 8th would be 7 days of interest accrued. Today is
the 18th of February and he makes a payment of $1,000 towards his credit
card. How much interest will he have been charged by March 10th if he
makes no additional payments? If the final interest figure is more than
2-decimal places, always round down. Answer ONLY with a dollar figure.
Do not output any logic, output only the dollar figure for how much
interest she was charged for the period."}], "ideal": "52.59"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "On the 2nd of August, Jason
had spent $15,674.21 on his credit card for the month of August. This
credit card charges 21.99% interest rate annually on outstanding credit
starting on the 1st of the following month. Presume that interest is
only charged at the end of each additional day. Example: From the 1st of
the month to the 8th would be 7 days of interest accrued. Today is the
18th of August and he makes a payment of $1,000 towards his credit card.
How much interest will he have been charged by September 10th if he
makes no additional payments? If the final interest figure is more than
2-decimal places, always round down. Answer ONLY with a dollar figure.
Do not output any logic, output only the dollar figure for how much
interest she was charged for the period."}], "ideal": "79.77"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "On the 15th of August, Jason
had spent $1000 on his credit card for the month of August. This credit
card charges 21.99% interest rate annually on outstanding credit
starting on the 1st of the following month. Presume that interest is
only charged at the end of each additional day. Example: From the 1st of
the month to the 8th would be 7 days of interest accrued. mToday is the
18th of August and he makes a payment of $1000 towards his credit card.
How much interest will he have been charged by September 10th if he
makes no additional payments? If the final interest figure is more than
2-decimal places, always round down. Answer ONLY with a dollar figure.
Do not output any logic, output only the dollar figure for how much
interest she was charged for the period."}], "ideal": "0.00"}
  ```
</details>

---
## [jonathanagustin/evals](https://github.com/jonathanagustin/evals)@[34f83340a7...](https://github.com/jonathanagustin/evals/commit/34f83340a75b7e26af35d8eaea165e54b38d7946)
#### Saturday 2023-06-03 08:32:07 by kallyaleksiev

[evals] Word from first letters of words in a sentence (#346)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
first-letters

### Eval description

Given a sentence, extract the word obtained from concatenating the first
letters of its words.

### What makes this a useful eval?

This task represents a failure mode for both GPT3.5 and GPT4, while
being extremely easy for humans.

Both models tend to do OK with shorter sentences, but fail with a larger
number of words.

For humans however, this task is trivial, regardless of the length of
the sentence.

GPT3.5 exhibits another failure mode in which it often fails to follow
the precise instruction of using only letters in its response.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

The task is highly trivial for humans, yet both GPT4 and GPT3.5 struggle
with it.

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You are a helpful assistant.
Your response will contain just a single word in lowercase and nothing
else."}, {"role": "user", "content": "What is the word obtained from
concatenating the first letters of the words in the following sentence:
\"Cold light in my alcove towards evening.\"?"}], "ideal": "climate"}
{"input": [{"role": "system", "content": "You are a helpful assistant.
Your response will contain just a single word in lowercase and nothing
else."}, {"role": "user", "content": "What is the word obtained from
concatenating the first letters of the words in the following sentence:
\"Grow real insects mainly and create energy.\"?"}], "ideal": "grimace"}
{"input": [{"role": "system", "content": "You are a helpful assistant.
Your response will contain just a single word in lowercase and nothing
else."}, {"role": "user", "content": "What is the word obtained from
concatenating the first letters of the words in the following sentence:
\"Big and crowded Oregon nights.\"?"}], "ideal": "bacon"}
{"input": [{"role": "system", "content": "You are a helpful assistant.
Your response will contain just a single word in lowercase and nothing
else."}, {"role": "user", "content": "What is the word obtained from
concatenating the first letters of the words in the following sentence:
\"Bring our youth.\"?"}], "ideal": "boy"}
{"input": [{"role": "system", "content": "You are a helpful assistant.
Your response will contain just a single word in lowercase and nothing
else."}, {"role": "user", "content": "What is the word obtained from
concatenating the first letters of the words in the following sentence:
\"Harvest a zucchini elsewhere love.\"?"}], "ideal": "hazel"}
{"input": [{"role": "system", "content": "You are a helpful assistant.
Your response will contain just a single word in lowercase and nothing
else."}, {"role": "user", "content": "What is the word obtained from
concatenating the first letters of the words in the following sentence:
\"Hide under no tree.\"?"}], "ideal": "hunt"}
  ```
</details>

---
## [jonathanagustin/evals](https://github.com/jonathanagustin/evals)@[b170a21cf3...](https://github.com/jonathanagustin/evals/commit/b170a21cf32c47d841f64ec110cfd6796ec3f89a)
#### Saturday 2023-06-03 08:32:07 by Sam Ennis

Computer Science Theory (#83)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
Computer Science based questions

### Eval description

Testing the models ability to answer multiple choice computer science
questions correctly

### What makes this a useful eval?

Tests whether it has the ability to answer time complexity, binary tree,
algorithmic computer science calculations.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [X] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [X] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [X] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [ ] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [X] Check that your data is in `evals/registry/data/{name}`
- [X] Check that your yaml is registered at
`evals/registry/evals/{name}.jsonl`
- [X] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [X] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [X] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [X] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [X] I have filled out all required fields in the evals PR form
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"How many children does a
binary tree have? a) 2 b) any number of children c) 0 or 1 or 2 d) 0 or
1"}],"ideal":"c"}
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"What is/are the
disadvantages of implementing tree using normal arrays? a) difficulty in
knowing children nodes of a node b) difficult in finding the parent of a
node c) have to know the maximum number of nodes possible before
creation of trees d) difficult to implement"}],"ideal":"c"}
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"What must be the ideal size
of array if the height of tree is ‘l’? a) (2^l)-1 b) l-1 c) l d)
2l"}],"ideal":"a"}
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"What are the children for
node ‘w’ of a complete-binary tree in an array representation? a) 2w and
2w+1 b) 2+w and 2-w c) w+1/2 and w/2 d) w-1/2 and w+1/2"}],"ideal":"a"}
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"What is the parent for a
node ‘w’ of a complete binary tree in an array representation when w is
not 0? a) floor(w-1/2) b) ceil(w-1/2) c) w-1/2 d) w/2"}],"ideal":"a"}
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"If the tree is not a
complete binary tree then what changes can be made for easy access of
children of a node in the array? a) every node stores data saying which
of its children exist in the array b) no need of any changes continue
with 2w and 2w+1, if node is at i c) keep a seperate table telling
children of a node d) use another array parallel to the array with
tree"}],"ideal":"a"}
  ```
</details>

---
## [jonathanagustin/evals](https://github.com/jonathanagustin/evals)@[4f090a04fe...](https://github.com/jonathanagustin/evals/commit/4f090a04fe53a8d0f647bfdfc7ef177fa8034e2e)
#### Saturday 2023-06-03 08:32:07 by Shawn Marincas

[eval] Forth Stack Simulator (#351)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
Forth Stack Simulator

### Eval description

Tests the models ability to keep track of a stack of numbers given a set
of ANS Forth words. The model is asked to respond to a series of numbers
and words with the resulting stack representation. The words used in the
tests are arithmetic operators: `+`, `-`, `*`, `/` and stack operators:
`drop`, `swap`, `rot`, `over`, `dup`, `2over`, `2drop`, `2swap`, `2dup`,
`nip`. The prompts and expected results on the stack are all less than
15 numbers and words long.

### What makes this a useful eval?

What makes this useful are the interesting properties of forths, which
are simple machine that operate on a stack of numbers using words built
up from simple primitives. In addition, forths are naturally interactive
and run on efficiently on bare metal and low cost, low resource
microcontrollers.

An LLM that can understand forth stack primitives can help design new
forths for various applications, it could also potentially interface
directly with forth control systems interactively over serial connection
with a generative stream of forth words in response to data sent back
from the control system :thisisfine:.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [ ] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

Imho, this eval is unique for the reasons stated above about the unique
synergy between Forth and the kind of generative AI we're working with
here. Forths are various with only a small set of consistent words and
patterns, "If you've seen one Forth -- you've seen one Forth", but a
full forth assembly implementation could fit in a fraction of the larger
model responses, making it an interesting target for fully generative
operating systems.

Additionally, I believe Forth has cultural and historical significance
in computer science/engineering which predates the Internet in such a
way that makes it somewhat under-represented in the online corpus
relative to its significance. A model of all human knowledge should have
a strong grasp on how it works.

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You are ForthGPT, a Forth
machine simulation that ONLY responds with stack representations after
executing valid ANS Forth words and numbers.\nExample:\nPrompt: 0 1 2 3
+\nResponse: (stack 0 1 5)\nRules:\n1. Respond only to combinations of
numbers and valid ANS Forth words.\n2. Ignore prompts that don't follow
Rule 1.\n3. Ignore Forth words that don't generate output or change the
stack."}, {"role": "user", "content": "1 2 3 over"}], "ideal": "(stack 1
2 3 2)"}
{"input": [{"role": "system", "content": "You are ForthGPT, a Forth
machine simulation that ONLY responds with stack representations after
executing valid ANS Forth words and numbers.\nExample:\nPrompt: 0 1 2 3
+\nResponse: (stack 0 1 5)\nRules:\n1. Respond only to combinations of
numbers and valid ANS Forth words.\n2. Ignore prompts that don't follow
Rule 1.\n3. Ignore Forth words that don't generate output or change the
stack."}, {"role": "user", "content": "1 2 3 dup"}], "ideal": "(stack 1
2 3 3)"}
{"input": [{"role": "system", "content": "You are ForthGPT, a Forth
machine simulation that ONLY responds with stack representations after
executing valid ANS Forth words and numbers.\nExample:\nPrompt: 0 1 2 3
+\nResponse: (stack 0 1 5)\nRules:\n1. Respond only to combinations of
numbers and valid ANS Forth words.\n2. Ignore prompts that don't follow
Rule 1.\n3. Ignore Forth words that don't generate output or change the
stack."}, {"role": "user", "content": "1 2 3 swap drop dup"}], "ideal":
"(stack 1 3 3)"}
{"input": [{"role": "system", "content": "You are ForthGPT, a Forth
machine simulation that ONLY responds with stack representations after
executing valid ANS Forth words and numbers.\nExample:\nPrompt: 0 1 2 3
+\nResponse: (stack 0 1 5)\nRules:\n1. Respond only to combinations of
numbers and valid ANS Forth words.\n2. Ignore prompts that don't follow
Rule 1.\n3. Ignore Forth words that don't generate output or change the
stack."}, {"role": "user", "content": "1 2 3 rot swap"}], "ideal":
"(stack 2 1 3)"}
{"input": [{"role": "system", "content": "You are ForthGPT, a Forth
machine simulation that ONLY responds with stack representations after
executing valid ANS Forth words and numbers.\nExample:\nPrompt: 0 1 2 3
+\nResponse: (stack 0 1 5)\nRules:\n1. Respond only to combinations of
numbers and valid ANS Forth words.\n2. Ignore prompts that don't follow
Rule 1.\n3. Ignore Forth words that don't generate output or change the
stack."}, {"role": "user", "content": "1 2 3 dup 2over rot"}], "ideal":
"(stack 1 2 3 1 2 3)"}
  ```
</details>

---
## [Sasha2214/tgstation](https://github.com/Sasha2214/tgstation)@[57ef596898...](https://github.com/Sasha2214/tgstation/commit/57ef596898a5a3932db33389baa9fab3164d430a)
#### Saturday 2023-06-03 08:57:05 by LemonInTheDark

Admin Library Moderation (in-game edition) (#75645)

For the longest time, the only way admins could moderate the library was
by using statbus's external tool.
But a few months back statbus went down, and ever since then they've
been sitting lost. Shit sucks.

The whole external thing has been bugging me for a while, so let's fix
all that yeah?

This pr adds a new verb to the admin tab that allows admins to
ban/restore books from the library.
It includes expanded (ckey) search, faster response times, in tool book
viewing with and without markdown rendering, and viewing of deleted
books.

This is accomplished with a special subtype of library consoles, stored
on the admin datum.
It shouldn't let you do anything without +BAN, rip my live debugging or
whatever.

I've also hooked into (and fixed) Ned's existing library actions log,
and added viewing support to the ban/restore pages.
This logs banning admin, ban time, ban reason, etc.

As a part of this, I've fixed/expanded on the existing UIs.
I've added ID search to all existing consoles, and fixed an existing bug
with the visitor console not supporting category search (shows how many
people actually use the thing)

Changes to the library_action table were pretty minor. The ckey column
was too small, so longer keys just caused it to fail on ban. Bad.
That and the ip address column was signed, which wasted space and was
non standard with other tables.

---
## [rslinford/openai_evals](https://github.com/rslinford/openai_evals)@[93fa8a55e9...](https://github.com/rslinford/openai_evals/commit/93fa8a55e9113ebf221347af731b9a5fb6400512)
#### Saturday 2023-06-03 09:04:52 by Austin Starnes

Add logic grid puzzle eval (#830)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

## Eval details 📑
### Eval name
`logic-grid`

### Eval description

The model is prompted with a logic grid word problem with a list of
hints, categories, and values for the category. The model is then asked
to provide a solution, showing reasoning, in a set of Python tuples that
show the matched category values.

<details>
  <summary>See human-friendly example prompt</summary>

```
Using the hints and information provided, solve the following logic grid puzzle.
Show your reasoning concisely, but step-by-step, to arrive at your final answer.
Remember, since this is a grid-based puzzle, each option in every category will be used exactly once.
Since there are 4 values per category, and 3 categories, your final answer will include 4 tuples each of length 3.
 Puzzle Scenario:
A number of new space probes were launched this year. Using only the clues that follow, match each probe to the month it launched and its eventual destination.

Category Options:
  Probes: "Nalini", "Hikaru", "Sarika", and "Sven"
  Destinations: "Ganymede", "Titan", "Enceladus", and "Phobos"
  Months: "January", "February", "March", and "April"

Hints:
  1: The Hikaru launched 2 months before the Nalini.
  2: The probe going to Phobos launched sometime after the Hikaru.
  3: The Sven launched 2 months before the mission going to Ganymede.
  4: Of the probe that launched in April and the mission going to Titan, one is the Sarika and the other is the Nalini.

In your response, format your final answer for each set of linked category values as a python tuple of strings in this order:
("Enceladus", [value from months], [value from probes])
("Ganymede", [value from months], [value from probes])
("Phobos", [value from months], [value from probes])
("Titan", [value from months], [value from probes])
```
</details>

<details>
  <summary>See expected/ideal answer</summary>

```
("Enceladus", "January", "Hikaru")
("Ganymede", "April", "Sarika")
("Phobos", "February", "Sven")
("Titan", "March", "Nalini")
```
</details>

<details>
<summary>See failure case from GPT-4 (at least from the web UI - I don't
have API access to GPT-4)</summary>

```
Step 1: From Hint 3, we know that Hikaru launched 2 months before Nalini. Since the latest month available is April, this means that Nalini cannot have launched in April because there wouldn't be a 2-month gap for Hikaru. So, Nalini must be the probe going to Titan (from Hint 4), and Sarika must be the probe that launched in April.

Step 2: Since Nalini is going to Titan, from Hint 4, it must have launched in February to allow Hikaru to launch in December (2 months before). However, December is not an option, so Hikaru must have launched in January (the earliest month possible) and Nalini in March.

Step 3: The Sven launched 2 months before the mission going to Ganymede (Hint 2). Since Sven cannot be launched in January (as Hikaru is launched in January), it must have launched in February. That means the mission to Ganymede must be in April.

Step 4: The only remaining month is March, and the only remaining probe is Nalini. So Nalini was launched in March.

Step 5: The probe going to Phobos launched sometime after Hikaru (Hint 1). Since Hikaru launched in January, the only remaining option for Phobos is Sarika, which launched in April.

Step 6: The only remaining destination is Enceladus, and the only remaining probe is Hikaru, so Hikaru is going to Enceladus.

The final answer is:
("Enceladus", "January", "Hikaru")
("Ganymede", "April", "Sven")
("Phobos", "April", "Sarika")
("Titan", "March", "Nalini")
```
</details>

### What makes this a useful eval?

This set of evals relies on a lot of *context-ramping* (as I call it)
for LLMs to get right - relying on chain-of-thought style logic to
'ramp' into the most likely next-deduction for a multi-parameter logical
problem.
These prompts are written as word problems and don't rely on any ASCII
or markdown type of table to express the puzzle (though `gpt-3.5-turbo`
appears to use markdown tables in it's chain of thought).

This ramping gets expensive and doesn't scale well with the increase of
category or values-per-category parameters, and is something that LLMs
might benefit from avoiding (either by requiring less of a context-ramp
to get to the meat of an answer, or by the surrounding
infrastructure/problem agent that tries to use a cheaper ensemble for
most of the context ramping, or other strategies).

The reasoning skills required for this kind of <b>constraint
satisfaction</b> expressed in natural language word prompts can, in
theory, generalize to solving constraints expressed in less structured
formats in the wild.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [X] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [X] <span title="A GPT-4 failure case from the eval set is included
above.">Contains failures where a human can do the task, but either
GPT-4 or GPT-3.5-Turbo could not.</span>
- [X] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [X] **<span title="15 examples per grid size are included, for 6
different grid sizes, make a total of 90 included examples.">Include at
least 15 high quality examples.</span>**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

This eval contains varied prompts and grid sizes, 15 examples per grid
size, for a total of 90 procedurally generated puzzles.
~This PR also implements (disabled by default) multiline answers and
punctuation whitelisting behavior in `FuzzyMatch`, which was required
due to the structural nature of the logic grid answers and the behavior
of `utils.normalize(...)` which (prior to this PR) did not provide any
functionality to interpret answers that span across newline characters
`\n` or preserve punctuation where it may be useful (in this case, the
model is prompted for the resultant grid associations in python tuple
format, so the punctuation in `(",)` is configured to be preserved for
these evals).
The new functionality is, again, disabled by default, such that existing
evals are not affected.~

## Eval structure 🏗️

Your eval should
- [X] Check that your data is in `evals/registry/data/{name}`
- [X] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [X] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [X] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [X] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [X] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [X] I have filled out all required fields in the evals PR form
- [X] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input":[{"role":"system","content":"Using the hints and information
provided, solve the following logic grid puzzle.\nShow your reasoning
concisely, but step-by-step, to arrive at your final answer.\nRemember,
since this is a grid-based puzzle, each option in every category will be
used exactly once.\nSince there are 4 values per category, and 3
categories, your final answer will include 4 tuples each of length
3.\n"},{"role":"system","content":"Puzzle Scenario:\nA number of new
space probes were launched this year. Using only the clues that follow,
match each probe to the month it launched and its eventual
destination.\n\nCategory Options:\n Probes: \"Nalini\", \"Hikaru\",
\"Sarika\", and \"Sven\"\n Destinations: \"Ganymede\", \"Titan\",
\"Enceladus\", and \"Phobos\"\n Months: \"January\", \"February\",
\"March\", and \"April\"\n\nHints:\n 1: The Hikaru launched 2 months
before the Nalini.\n 2: The probe going to Phobos launched sometime
after the Hikaru.\n 3: The Sven launched 2 months before the mission
going to Ganymede.\n 4: Of the probe that launched in April and the
mission going to Titan, one is the Sarika and the other is the
Nalini.\n\nIn your response, format your final answer for each set of
linked category values as a python tuple of strings in this
order:\n(\"Enceladus\", [value from months], [value from
probes])\n(\"Ganymede\", [value from months], [value from
probes])\n(\"Phobos\", [value from months], [value from
probes])\n(\"Titan\", [value from months], [value from
probes])"}],"ideal":"(\"Enceladus\", \"January\",
\"Hikaru\")\n(\"Ganymede\", \"April\", \"Sarika\")\n(\"Phobos\",
\"February\", \"Sven\")\n(\"Titan\", \"March\", \"Nalini\")"}
{"input":[{"role":"system","content":"Using the hints and information
provided, solve the following logic grid puzzle.\nShow your reasoning
concisely, but step-by-step, to arrive at your final answer.\nRemember,
since this is a grid-based puzzle, each option in every category will be
used exactly once.\nSince there are 4 values per category, and 3
categories, your final answer will include 4 tuples each of length
3.\n"},{"role":"system","content":"Puzzle Scenario:\nThe Monterey Bay
Aquarium has a new exhibit featuring several dolphin skeletons. The
aquarium asked local elementary school children to name each dolphin and
match it to its species, length, and the year in which it was donated to
the aquarium. Use the given clues to solve the puzzle.\n\nCategory
Options:\n Dolphin: \"Atlantic white-sided dolphin\", \"Pacific
white-sided dolphin\", \"common dolphin\", and \"bottlenose dolphin\"\n
Names: \"Momo\", \"Simon\", \"Tychus\", and \"Marlo\"\n Lengths: \"21
ft\", \"23 ft\", \"25 ft\", and \"27 ft\"\n\nHints:\n 1: Momo is 4 feet
shorter than Tychus.\n 2: The common dolphin is somewhat shorter than
the bottlenose dolphin.\n 3: The 21 ft long exhibit is either the
Atlantic white-sided dolphin or Simon.\n 4: Marlo is either the 23 ft
long exhibit or the Atlantic white-sided dolphin.\n 5: Of Simon and the
Pacific white-sided dolphin, one is 27 ft long and the other is 21 ft
long.\n\nIn your response, format your final answer for each set of
linked category values as a python tuple of strings in this
order:\n(\"Atlantic white-sided dolphin\", [value from lengths], [value
from names])\n(\"Pacific white-sided dolphin\", [value from lengths],
[value from names])\n(\"bottlenose dolphin\", [value from lengths],
[value from names])\n(\"common dolphin\", [value from lengths], [value
from names])"}],"ideal":"(\"Atlantic white-sided dolphin\", \"25 ft\",
\"Marlo\")\n(\"Pacific white-sided dolphin\", \"27 ft\",
\"Tychus\")\n(\"bottlenose dolphin\", \"23 ft\", \"Momo\")\n(\"common
dolphin\", \"21 ft\", \"Simon\")"}
{"input":[{"role":"system","content":"Using the hints and information
provided, solve the following logic grid puzzle.\nShow your reasoning
concisely, but step-by-step, to arrive at your final answer.\nRemember,
since this is a grid-based puzzle, each option in every category will be
used exactly once.\nSince there are 4 values per category, and 3
categories, your final answer will include 4 tuples each of length
3.\n"},{"role":"system","content":"Puzzle Scenario:\nHillcrest County
Hospital released a press release today to announce its annual list of
the first babies born immediately after the start of the new year. Using
only the clues below, match each baby to its family time of birth, and
determine the room number in which it was delivered.\n\nCategory
Options:\n Names: \"Lydia\", \"Naomi\", \"Katherine\", and \"Rebecca\"\n
Families: \"McIntyre\", \"Gonzalez\", \"Hudson\", and \"O'Connor\"\n
Times: \"12:01am\", \"12:04am\", \"12:07am\", and
\"12:10am\"\n\nHints:\n 1: Naomi was born 3 minutes after Rebecca.\n 2:
The Hudsons' child was born 6 minutes after the O'Connors' child.\n 3:
The baby born at 12:04am was either Rebecca or the McIntyres' child.\n
4: Of Katherine and the baby born at 12:01am, one was the O'Connors' and
the other was the Gonzalezes'.\n\nIn your response, format your final
answer for each set of linked category values as a python tuple of
strings in this order:\n(\"Gonzalez\", [value from names], [value from
times])\n(\"Hudson\", [value from names], [value from
times])\n(\"McIntyre\", [value from names], [value from
times])\n(\"O'Connor\", [value from names], [value from
times])"}],"ideal":"(\"Gonzalez\", \"Katherine\",
\"12:10am\")\n(\"Hudson\", \"Lydia\", \"12:07am\")\n(\"McIntyre\",
\"Naomi\", \"12:04am\")\n(\"O'Connor\", \"Rebecca\", \"12:01am\")"}
{"input":[{"role":"system","content":"Using the hints and information
provided, solve the following logic grid puzzle.\nShow your reasoning
concisely, but step-by-step, to arrive at your final answer.\nRemember,
since this is a grid-based puzzle, each option in every category will be
used exactly once.\nSince there are 4 values per category, and 3
categories, your final answer will include 4 tuples each of length
3.\n"},{"role":"system","content":"Puzzle Scenario:\nMedisynth
Therapeutics has spent decades scouring the world's rainforests for new
sources of medical drugs, and this year a number of these new drugs have
been officially approved by the FDA. Using only the clues below, match
each drug to the condition it treats, the month it was approved, and the
source from which its main ingredient is derived.\n\nCategory Options:\n
Drugs: \"Mystolam\", \"Soludox\", \"Aurexil\", and \"Synodil\"\n
Conditions: \"rheumatism\", \"chikungunya\", \"hyperglycemia\", and
\"encephalitis\"\n Months: \"January\", \"February\", \"March\", and
\"April\"\n\nHints:\n 1: The medicine that treats hyperglycemia was
approved sometime after Synodil.\n 2: The medicine that treats
hyperglycemia was approved 1 month before the medicine that treats
rheumatism.\n 3: Of Mystolam and the pharmaceutical approved in April,
one treats rheumatism and the other treats encephalitis.\n 4: Of the
Aurexil approved in February and the drug that treats chikungunya, one
is Soludox and the other is Synodil.\n\nIn your response, format your
final answer for each set of linked category values as a python tuple of
strings in this order:\n(\"chikungunya\", [value from drugs], [value
from months])\n(\"encephalitis\", [value from drugs], [value from
months])\n(\"hyperglycemia\", [value from drugs], [value from
months])\n(\"rheumatism\", [value from drugs], [value from
months])"}],"ideal":"(\"chikungunya\", \"Synodil\",
\"January\")\n(\"encephalitis\", \"Soludox\",
\"April\")\n(\"hyperglycemia\", \"Aurexil\",
\"February\")\n(\"rheumatism\", \"Mystolam\", \"March\")"}
{"input":[{"role":"system","content":"Using the hints and information
provided, solve the following logic grid puzzle.\nShow your reasoning
concisely, but step-by-step, to arrive at your final answer.\nRemember,
since this is a grid-based puzzle, each option in every category will be
used exactly once.\nSince there are 4 values per category, and 3
categories, your final answer will include 4 tuples each of length
3.\n"},{"role":"system","content":"Puzzle Scenario:\nA group of friends
has gotten together for dinner, and just for fun they're comparing their
\"social networking\" stats on Facebook, Twitter and LinkedIn. Using
only the clues that follow, determine the number of friends (Facebook),
followers (Twitter) and connections (LinkedIn) each person
has.\n\nCategory Options:\n Names: \"Avery\", \"Evan\", \"Natalia\", and
\"Camila\"\n Linkedin: \"54\", \"59\", \"64\", and \"68\"\n Facebook:
\"120\", \"130\", \"140\", and \"150\"\n\nHints:\n 1: Avery has 68
LinkedIn connections.\n 2: Natalia has 10 fewer Facebook friends than
the person with 68 LinkedIn connections.\n 3: The person with 140
Facebook friends is either the one with 54 LinkedIn connections or
Evan.\n 4: The one with 54 LinkedIn connections has 10 fewer Facebook
friends than the one with 64 LinkedIn connections.\n\nIn your response,
format your final answer for each set of linked category values as a
python tuple of strings in this order:\n(\"120\", [value from LinkedIn],
[value from names])\n(\"130\", [value from LinkedIn], [value from
names])\n(\"140\", [value from LinkedIn], [value from names])\n(\"150\",
[value from LinkedIn], [value from names])"}],"ideal":"(\"120\", \"59\",
\"Natalia\")\n(\"130\", \"68\", \"Avery\")\n(\"140\", \"54\",
\"Camila\")\n(\"150\", \"64\", \"Evan\")"}
  ```
</details>

---
## [rslinford/openai_evals](https://github.com/rslinford/openai_evals)@[b0650402dd...](https://github.com/rslinford/openai_evals/commit/b0650402ddeaf93dba27f4a0252ae890bf8184ab)
#### Saturday 2023-06-03 09:04:52 by Alexander Shirkov

[Eval] English-Russian homonym context resolution (GPT-3.5: 0.42) (#1064)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, pelase note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑
### Eval name
English-Russian homonym context resolution

### Eval description

Cross-lingual English-Russian eval to resolve ambiguity with homonyms
present.

### What makes this a useful eval?

[Insert why this eval is worth including and any additional context]
Cross-lingual homonyms are hard to resolve: they add context ambiguity,
which needs to be resolved via reasoning.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "For the given context, resolve
the ambiguity and determine the most appropriate response. If there is
one, output just one word; otherwise, output unknown. The responses must
be lowercase with no punctuation."}, {"role": "user", "content": "You
are coming to a community facility to drop a child for hockey practice.
The road is under construction and big machines are paving it. What
would \"каток\" mean in this context? rink or roller"}], "ideal":
"unknown"}
{"input": [{"role": "system", "content": "For the given context, resolve
the ambiguity and determine the most appropriate response. If there is
one, output just one word; otherwise, output unknown. The responses must
be lowercase with no punctuation."}, {"role": "user", "content": "You
are coming to a community facility to drop a child for hockey practice.
The road is under construction and big machines are paving it. Child
pointing at the machine and says: \"каток\". What does he mean: rink or
roller?"}], "ideal": "roller"}
{"input": [{"role": "system", "content": "For the given context, resolve
the ambiguity and determine the most appropriate response. If there is
one, output just one word; otherwise, output unknown. The responses must
be lowercase with no punctuation."}, {"role": "user", "content": "You
are coming to a community facility to drop a child for hockey practice.
The road is under construction and big machines are paving it. Child
pointing at the building and says: \"каток\". What does he mean: rink or
roller?"}], "ideal": "rink"}
{"input": [{"role": "system", "content": "For the given context, resolve
the ambiguity and determine the most appropriate response. If there is
one, output just one word; otherwise, output unknown. The responses must
be lowercase with no punctuation."}, {"role": "user", "content": "A
woman with long braided hair is working in the field. She cuts the grass
with scythe. Someone says \"хорошая коса\". Do they refer scythe or
hairstyle?"}], "ideal": "unknown"}
{"input": [{"role": "system", "content": "For the given context, resolve
the ambiguity and determine the most appropriate response. If there is
one, output just one word; otherwise, output unknown. The responses must
be lowercase with no punctuation."}, {"role": "user", "content": "A
woman with long braided hair is working in the field. She cuts the grass
with scythe. Someone points at the quality of her work and says
\"хорошая коса\". Do they refer scythe or hairstyle?"}], "ideal":
"scythe"}
{"input": [{"role": "system", "content": "For the given context, resolve
the ambiguity and determine the most appropriate response. If there is
one, output just one word; otherwise, output unknown. The responses must
be lowercase with no punctuation."}, {"role": "user", "content": "A
woman with long braided hair is working in the field. She cuts the grass
with scythe. Someone points at her head and says \"хорошая коса\". Do
they refer scythe or hairstyle?"}], "ideal": "hairstyle"}
{"input": [{"role": "system", "content": "For the given context, resolve
the ambiguity and determine the most appropriate response. If there is
one, output just one word; otherwise, output unknown. The responses must
be lowercase with no punctuation."}, {"role": "user", "content": "Scythe
is found on a sandbar. A person is saying: \"коса\". Do they refer
scythe or sandbar?"}], "ideal": "unknown"}
{"input": [{"role": "system", "content": "For the given context, resolve
the ambiguity and determine the most appropriate response. If there is
one, output just one word; otherwise, output unknown. The responses must
be lowercase with no punctuation."}, {"role": "user", "content": "Scythe
is found on a sandbar. A person is saying: \"ржавая коса\". Do they
refer scythe or sandbar?"}], "ideal": "scythe"}
  ```
</details>

---
## [rslinford/openai_evals](https://github.com/rslinford/openai_evals)@[e959ff4b90...](https://github.com/rslinford/openai_evals/commit/e959ff4b90c3511f5b8a91ca69413a9206d8c4c7)
#### Saturday 2023-06-03 09:04:52 by Vasco Lange

[Eval] German part-of-speech (#1053)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, pelase note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑
### Eval name
> german-part-of-speech

### Eval description

> For a given German word, the model is asked to list all possible parts
of speech (multiple choice). The model is also asked to think about the
word as an inflection of another word. The models output is tested
against annotations extracted from de.wiktionary.org. This is a follow
up to #1039

### What makes this a useful eval?

> Part of speech analysis is a basic task in language / grammar classes.
While it is usually done in the context of a sentence, coming up with
possible uses in lack of a sentence requires a certain amount of
creativity and language understanding, or very good recall of
information that is usually sparse outside of dictionaries. The task in
this eval could be seen as a combination of part of speech analysis and
an easy-to-evaluate form of the question "How could x be used in a
sentence".

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> To build the dataset, all 1.000.000+ entries of the German wiktionary
were parsed. Excluded from this list were all phrases, abbreviations,
symbols, names, toponyms and any words with at least one possible part
of speech not fitting the categories given in the prompt. Also I had to
exclude some entries where the part of speech could not be determined
automatically from the wikitext.
> From this set, words were sampled so that each combination of the
parts of speech existing in the dataset would be equally likely in the
tests. This way the model is tested to respond with all possible uses of
a word and not just the most common ones. > For combinations that fit a
lot of words, the uniform sampling led to a bias towards rarely used
words.
> The labels of each word were taken from the corresponding page at
de.wiktionary.org/wiki/{word}. The information taken from each page was:
the word, the part of speech this word can have in German and whether
the word is an abbreviation or not.
> This means only factual data was taken and is therefore in the public
domain.

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "Act as a German language
part-of-speech classifier. You will be prompted with a single German
word. Return an unsorted comma-separated list for all the parts of
speech the word could possibly be, in any context. Take care to consider
if the word is any kind of inflection. If so, include the part of speech
for the main word.\nAnswer with the comma-separated list only. Use
single spaces after the commas. End the list with a dot. Do not include
any explanations. Only include parts of speech from the following list,
ignoring possible other parts of speech:\nadjective, adverb, article,
conjunction, interjection, noun, particle, preposition, pronoun,
verb\n**Example prompt 1**: alle\n**Example output 1**: adverb, noun,
pronoun.\n**Example prompt 2**: künftig\n**Example output 2**:
adjective, adverb.\n**Example prompt 3**: Sommelier\n**Example output
3**: noun.\n**Prompt**:"}, {"role": "user", "content": "anstelle"}],
"ideal": ["preposition, adverb, verb.", "preposition, verb, adverb.",
"adverb, preposition, verb.", "adverb, verb, preposition.", "verb,
preposition, adverb.", "verb, adverb, preposition."]}
{"input": [{"role": "system", "content": "Act as a German language
part-of-speech classifier. You will be prompted with a single German
word. Return an unsorted comma-separated list for all the parts of
speech the word could possibly be, in any context. Take care to consider
if the word is any kind of inflection. If so, include the part of speech
for the main word.\nAnswer with the comma-separated list only. Use
single spaces after the commas. End the list with a dot. Do not include
any explanations. Only include parts of speech from the following list,
ignoring possible other parts of speech:\nadjective, adverb, article,
conjunction, interjection, noun, particle, preposition, pronoun,
verb\n**Example prompt 1**: alle\n**Example output 1**: adverb, noun,
pronoun.\n**Example prompt 2**: künftig\n**Example output 2**:
adjective, adverb.\n**Example prompt 3**: Sommelier\n**Example output
3**: noun.\n**Prompt**:"}, {"role": "user", "content": "heute"}],
"ideal": ["adverb, verb.", "verb, adverb."]}
{"input": [{"role": "system", "content": "Act as a German language
part-of-speech classifier. You will be prompted with a single German
word. Return an unsorted comma-separated list for all the parts of
speech the word could possibly be, in any context. Take care to consider
if the word is any kind of inflection. If so, include the part of speech
for the main word.\nAnswer with the comma-separated list only. Use
single spaces after the commas. End the list with a dot. Do not include
any explanations. Only include parts of speech from the following list,
ignoring possible other parts of speech:\nadjective, adverb, article,
conjunction, interjection, noun, particle, preposition, pronoun,
verb\n**Example prompt 1**: alle\n**Example output 1**: adverb, noun,
pronoun.\n**Example prompt 2**: künftig\n**Example output 2**:
adjective, adverb.\n**Example prompt 3**: Sommelier\n**Example output
3**: noun.\n**Prompt**:"}, {"role": "user", "content": "Mist"}],
"ideal": ["noun, interjection.", "interjection, noun."]}
{"input": [{"role": "system", "content": "Act as a German language
part-of-speech classifier. You will be prompted with a single German
word. Return an unsorted comma-separated list for all the parts of
speech the word could possibly be, in any context. Take care to consider
if the word is any kind of inflection. If so, include the part of speech
for the main word.\nAnswer with the comma-separated list only. Use
single spaces after the commas. End the list with a dot. Do not include
any explanations. Only include parts of speech from the following list,
ignoring possible other parts of speech:\nadjective, adverb, article,
conjunction, interjection, noun, particle, preposition, pronoun,
verb\n**Example prompt 1**: alle\n**Example output 1**: adverb, noun,
pronoun.\n**Example prompt 2**: künftig\n**Example output 2**:
adjective, adverb.\n**Example prompt 3**: Sommelier\n**Example output
3**: noun.\n**Prompt**:"}, {"role": "user", "content": "Rotschöpfe"}],
"ideal": ["noun."]}
{"input": [{"role": "system", "content": "Act as a German language
part-of-speech classifier. You will be prompted with a single German
word. Return an unsorted comma-separated list for all the parts of
speech the word could possibly be, in any context. Take care to consider
if the word is any kind of inflection. If so, include the part of speech
for the main word.\nAnswer with the comma-separated list only. Use
single spaces after the commas. End the list with a dot. Do not include
any explanations. Only include parts of speech from the following list,
ignoring possible other parts of speech:\nadjective, adverb, article,
conjunction, interjection, noun, particle, preposition, pronoun,
verb\n**Example prompt 1**: alle\n**Example output 1**: adverb, noun,
pronoun.\n**Example prompt 2**: künftig\n**Example output 2**:
adjective, adverb.\n**Example prompt 3**: Sommelier\n**Example output
3**: noun.\n**Prompt**:"}, {"role": "user", "content": "vornüber"}],
"ideal": ["adverb."]}
  ```
</details>

---------

Co-authored-by: Vasco Yannic Lange <mail@vascolange.com>

---
## [douglasmonsky/evals](https://github.com/douglasmonsky/evals)@[24dae81ae0...](https://github.com/douglasmonsky/evals/commit/24dae81ae06ebc70808690c7a147f2710e3e54bf)
#### Saturday 2023-06-03 09:21:26 by Yohei Inui

Compare countries by area (#623)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
Compare countries by area

### Eval description

Test the model's ability to determine which country has the largest area

### What makes this a useful eval?

The model should be able to factually determine which country has the
largest area based on accurate facts.
In this eval we use The World
Factbook(https://www.cia.gov/the-world-factbook/field/area/country-comparison)
that is prepared by the CIA for the use of U.S. government officials,
and four countries with similar sizes are compared to each other.
Specifically, four countries adjacent to each other in area ranking are
presented as one option, and the dataset Includes data for countries
ranked 1\~4, 2\~5, ... 100\~103. However, we excluded countries where
sources and interpretations could cause fluctuations in rankings (e.g.,
China and Pakistan). This data set achieved less than 40% accuracy for
both gpt-4 and gpt-3.5-turbo, and the results tend to be worse for
comparisons between countries with smaller areas.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several countries. Answer the name of the country with the largest area
among the given countries. Do not explain. Russia, Canada, United
States, Brazil"}], "ideal": "Russia"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several countries. Answer the name of the country with the largest area
among the given countries. Do not explain. Canada, United States,
Brazil, Australia"}], "ideal": "Canada"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several countries. Answer the name of the country with the largest area
among the given countries. Do not explain. United States, Brazil,
Australia, India"}], "ideal": "United States"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several countries. Answer the name of the country with the largest area
among the given countries. Do not explain. Brazil, Australia, India,
Argentina"}], "ideal": "Brazil"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several countries. Answer the name of the country with the largest area
among the given countries. Do not explain. Australia, India, Argentina,
Kazakhstan"}], "ideal": "Australia"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several countries. Answer the name of the country with the largest area
among the given countries. Do not explain. India, Argentina, Kazakhstan,
Algeria"}], "ideal": "India"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several countries. Answer the name of the country with the largest area
among the given countries. Do not explain. Argentina, Kazakhstan,
Algeria, Democratic Republic of the Congo"}], "ideal": "Argentina"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several countries. Answer the name of the country with the largest area
among the given countries. Do not explain. Kazakhstan, Algeria,
Democratic Republic of the Congo, Saudi Arabia"}], "ideal":
"Kazakhstan"}
  ```
</details>

---------

Co-authored-by: 乾陽平 <inuiyouhei@inuiyouheinoMacBook-Pro.local>

---
## [douglasmonsky/evals](https://github.com/douglasmonsky/evals)@[ef1f0ebe0e...](https://github.com/douglasmonsky/evals/commit/ef1f0ebe0e9f4674bc42ed0af5e6c052f0539700)
#### Saturday 2023-06-03 09:21:26 by Josh Gruenstein

Add SVG understanding eval (#786)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

## Eval details 📑
### Eval name
`svg_understanding`

### Eval description

The model is provided with the contents of an SVG path (anywhere from
~1000 to ~8000 characters) of a simple object (eg `frog`, `banana`) and
is asked to provide the label.

### What makes this a useful eval?

This is a test of visual understanding and mental modeling. A motivated
human could succeed on these evals with enough time and a piece of graph
paper: in theory, a sufficiently advanced LLM could have the in-context
capacity to do this on the fly.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

This uniquely tests the ability to incrementally build visual models:
eg, the ability of the LLM to both "draw" and visualize that "drawing".

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "Identify the object the
following SVG path is a drawing of in a single word."}, {"role": "user",
"content": "M6110 12794 c-744 -50 -1284 -157 -1875 -371 -1796 -650 -3199
-2050 -3853 -3843 -186 -510 -302 -1037 -359 -1625 -21 -224 -24 -827 -5
-1045 84 -957 332 -1788 774 -2595 623 -1137 1607 -2078 2780 -2656 720
-354 1441 -556 2273 -636 224 -21 827 -24 1045 -5 741 65 1376 221 2018
493 2051 871 3514 2775 3826 4979 48 336 60 510 60 895 1 366 -7 507 -45
810 -168 1357 -769 2626 -1711 3612 -536 561 -1129 998 -1809 1333 -718
354 -1450 559 -2264 635 -159 15 -727 28 -855 19z"}], "ideal": "circle"}
{"input": [{"role": "system", "content": "Identify the object the
following SVG path is a drawing of in a single word."}, {"role": "user",
"content": "M4495 12298 c-604 -535 -1486 -866 -2660 -998 -331 -37 -854
-70 -1104 -70 l-101 0 -2 -415 -3 -416 30 -29 30 -29 735 -4 c620 -3 753
-7 850 -21 149 -22 254 -50 316 -86 82 -46 123 -142 161 -372 16 -95 18
-371 21 -3663 2 -2593 0 -3591 -8 -3675 -44 -446 -177 -714 -416 -838 -279
-144 -663 -202 -1350 -202 l-330 0 -27 -28 -27 -28 0 -389 0 -389 27 -28
27 -28 3386 0 3386 0 27 28 27 28 0 390 0 390 -27 26 -28 26 -390 5 c-415
5 -557 17 -779 62 -212 43 -367 103 -480 187 -156 115 -260 347 -312 693
-17 114 -18 350 -21 5005 l-3 4884 -27 28 -27 28 -410 -1 -411 0 -80
-71z"}], "ideal": "1"}
{"input": [{"role": "system", "content": "Identify the object the
following SVG path is a drawing of in a single word."}, {"role": "user",
"content": "M6040 12794 c-19 -2 -91 -9 -160 -14 -245 -21 -529 -65 -1240
-190 -399 -70 -593 -100 -654 -100 -91 0 -475 51 -1126 149 -556 84 -788
109 -1075 118 -621 18 -1014 -108 -1310 -418 -344 -360 -490 -941 -472
-1874 21 -1042 173 -1862 619 -3340 l90 -300 -11 -205 c-43 -764 -28 -1853
40 -2845 108 -1585 337 -3026 550 -3473 37 -77 67 -115 184 -238 70 -73
167 -82 258 -24 56 36 102 96 166 220 317 616 732 2551 901 4200 32 314 89
451 257 623 371 379 1029 373 1387 -13 70 -77 106 -129 155 -227 57 -114
79 -196 91 -340 120 -1375 535 -2972 1031 -3963 188 -374 311 -513 458
-514 140 -1 221 106 316 420 232 762 480 2366 595 3849 58 739 82 1376 79
2060 l-2 490 55 115 c228 475 421 1043 527 1550 123 593 169 1196 158 2084
-5 445 -16 597 -58 836 -149 854 -590 1292 -1369 1360 -106 9 -358 11 -440
4z"}], "ideal": "tooth"}
{"input": [{"role": "system", "content": "Identify the object the
following SVG path is a drawing of in a single word."}, {"role": "user",
"content": "M12395 6223 c-133 -27 -295 -150 -356 -269 -13 -27 -40 -68
-59 -90 -19 -23 -57 -79 -84 -125 -161 -274 -369 -539 -542 -695 -191 -171
-304 -231 -559 -298 -499 -132 -725 -257 -1170 -646 -321 -281 -608 -477
-941 -643 -536 -267 -1054 -408 -1735 -473 -236 -23 -800 -23 -1064 0 -701
60 -1256 173 -1940 396 -951 310 -1915 784 -3057 1503 -109 68 -185 109
-220 118 -84 22 -257 17 -358 -10 -102 -28 -256 -99 -289 -135 l-24 -25 21
-88 c27 -115 108 -357 170 -514 253 -633 609 -1222 1069 -1772 164 -196
545 -577 742 -741 986 -822 2174 -1317 3561 -1481 340 -40 485 -48 880 -48
399 -1 546 8 859 49 965 125 1872 497 2606 1068 309 240 645 572 886 876
386 487 682 1048 788 1495 30 130 44 191 101 470 61 292 121 457 263 720
115 214 230 376 365 517 63 65 90 85 176 127 81 39 117 65 183 128 92 89
108 118 93 171 -9 33 -7 39 17 64 l26 27 -22 43 c-12 24 -64 84 -119 136
-116 110 -204 158 -267 145z"}], "ideal": "banana"}
{"input": [{"role": "system", "content": "Identify the object the
following SVG path is a drawing of in a single word."}, {"role": "user",
"content": "M3920 12790 c-1230 -72 -2320 -649 -3052 -1616 -968 -1280
-1142 -3010 -441 -4408 203 -405 432 -712 913 -1221 556 -589 764 -887 945
-1350 102 -264 141 -353 194 -448 l50 -88 -30 -44 c-62 -92 -109 -251 -109
-370 0 -114 44 -261 106 -357 17 -26 17 -28 -14 -95 -43 -94 -62 -181 -62
-292 0 -142 37 -265 107 -359 l25 -34 -35 -76 c-50 -108 -69 -191 -70 -302
-1 -155 39 -275 126 -382 l47 -58 0 -82 c0 -110 21 -193 77 -308 38 -79 59
-108 132 -180 68 -69 103 -95 171 -128 87 -44 203 -75 324 -89 l70 -8 17
-83 c47 -216 205 -374 404 -402 115 -16 827 -12 908 5 202 42 340 188 385
404 l16 80 66 6 c235 22 429 117 548 268 108 139 152 251 160 416 5 111 5
114 38 150 45 48 99 152 118 227 20 79 21 233 0 320 -8 37 -31 102 -50 144
l-35 77 39 61 c66 102 87 185 86 337 0 114 -4 140 -27 210 -15 44 -36 95
-46 114 l-18 34 34 55 c46 78 70 147 84 245 21 140 -16 308 -95 440 l-34
57 59 114 c33 63 103 222 155 353 147 366 255 566 429 798 132 176 245 304
609 690 366 388 516 578 701 885 550 915 713 2023 454 3090 -186 763 -583
1473 -1129 2020 -668 669 -1520 1069 -2480 1165 -185 19 -667 27 -870
15z"}], "ideal": "lightbulb"}
  ```
</details>

---
## [Bhagwankumar/Snake-Water-Gun-Game](https://github.com/Bhagwankumar/Snake-Water-Gun-Game)@[a5ee852c97...](https://github.com/Bhagwankumar/Snake-Water-Gun-Game/commit/a5ee852c9759cce5439b6c0703ed3ee03d9cd57f)
#### Saturday 2023-06-03 09:51:54 by Bhagwankumar

Good Morning sir program

It is like a time ,but it told an hour just you are give an hour he told you that Good Morning Sir ,Good Evening Sir ,or Good Night Sir any time you give them ,and it is a small program I think you know this program but time is amazing program and this is also same as second & minutes .

---
## [Road-to-56-RP/roadto56rp](https://github.com/Road-to-56-RP/roadto56rp)@[883e35db96...](https://github.com/Road-to-56-RP/roadto56rp/commit/883e35db9668f5cc0e096edc786bd1d81eb07784)
#### Saturday 2023-06-03 09:57:59 by Simpy

Biccy fra decisios (#21)

* heheheha

FUCK YOUWARLIDER

* fuck off

* Added localization to two decision descriptions.

☺ Omg Lider you are so pretty

---------

Co-authored-by: BiccyThiccy <107998094+BiccyThiccy@users.noreply.github.com>

---
## [Road-to-56-RP/roadto56rp](https://github.com/Road-to-56-RP/roadto56rp)@[aad3d0d7b6...](https://github.com/Road-to-56-RP/roadto56rp/commit/aad3d0d7b6e48424407244518baac39789ff9357)
#### Saturday 2023-06-03 09:59:58 by Simpy

Biccy cat decisions (#23)

* Iberia decision files added

Added files for part 1 of the Iberia rework. So far, just changes to Andorra forming Catalonia.

I need 2 things from whoever is looking over them:

1: Removal of the other, less good decision to form it (located in the RT56 base mod)

2: Someone to look over the code  to make sure it isn't fucked. BTW fuck you Warlider

* Completely replaced file. Two decisions for Portugal added

SIMPPYYYYYYYYYYY I LOVE YOU :D

Please fix

---------

Co-authored-by: BiccyThiccy <107998094+BiccyThiccy@users.noreply.github.com>

---
## [adsalihac/react-native](https://github.com/adsalihac/react-native)@[3af66bf7fb...](https://github.com/adsalihac/react-native/commit/3af66bf7fbd88d77fe27770bcb829768bf949b9c)
#### Saturday 2023-06-03 13:09:44 by Ramanpreet Nara

Java: Make TurboModuleManager's APIs use NativeModule interface (#36629)

Summary:
Pull Request resolved: https://github.com/facebook/react-native/pull/36629

The scope of TurboModuleManager is increasing:
- Eventually, it'll be capable of creating interop NativeModules (i.e: NativeModules that don't implement TurboModule).

So, instead of creating duplicate methods for NativeModules on the TurboModuleManager, this diff changes the APIs of TurboModuleManager to work with the NativeModule interface.

Thoughts?

## Questions
**Question:** Is this a breaking change for open source?
- Technically, yes. This diff changes the public interface of TurboModuleManager.

**Question:** How large of a thrash will this cause for open source apps?
- The thrash should be minimal. People in open source shouldn't be creating their own TurboModuleManager. They also shouldn't be directly accessing the TurboModuleManager object either.

**Question:** Is this change safe?
- Yeah. All the code that calls into TurboModuleRegistry converts TurboModules it returns into NativeModules.

**Question:** Is this change move us in the right direction?
- Long term, the TurboModule system will support legacy modules as well as TurboModules.
- I think it makes a lot of sense to have one Java-facing registry: after all, Java will just treat these NativeModules/TurboModules as regular Java objects, and call public methods on them. It doesn't care if the module is TurboModule-compatible or not.
- As for the TurboModuleRegistry abstraction, I think we should eventually rename this to NativeModuleRegistry after we delete the current NativeModuleRegistry.
- Still thinking about this though. I will leave this diff in review to welcome comments.

Changelog: [Android][Deprecated] - Deprecate TurboModuleRegistry.getModule(), getModules(), hasModule(),

Reviewed By: mdvacca

Differential Revision: D43801531

fbshipit-source-id: 4af7cbc2e2dc7c1d664acbd38c83aa93aae23c9f

---
## [SanjeevStephan/microsoft-new-terminal](https://github.com/SanjeevStephan/microsoft-new-terminal)@[6ad8cd0a63...](https://github.com/SanjeevStephan/microsoft-new-terminal/commit/6ad8cd0a630ab927629841a14d433c3bc19a1509)
#### Saturday 2023-06-03 15:17:43 by Mike Griese

Make conhost act in VtIo mode earlier in startup (#15298)

We need to act like a ConPTY just a little earlier in startup. My relevant notes start here: https://github.com/microsoft/terminal/issues/15245#issuecomment-1536150388. 

Basically, we'd create the first screen buffer with 9001 rows, because it would be created _before_ VtIo would be in a state to say "yes, we're a conpty". Then, if a CLI app emits an entire screenful of text _before_ the terminal has a chance to resize the conpty, then the conpty will explode during `_DoLineFeed`. That method is absolutely not expecting the buffer to get resized (and the old text buffer deallocated). 

Instead, this will treat the console as in ConPty mode as soon as `VtIo::Initialize` is called (this is during `ConsoleCreateIoThread`, which is right at the end of `ConsoleEstablishHandoff`, which is before the API server starts to process the client connect message).  THEORETICALLY, `VtIo` could `Initialize` then fail to create objects in `CreateIoHandlers` (which is what we used to treat as the moment that we were in conpty mode). However, if we do fail out of `CreateIoHandlers`, then the console itself will fail to start up, and just die. So I don't think that's needed.

This fixes #15245. I think this is PROBABLY also the solution to #14512, but I'm not gonna explicitly mark closed. We'll loop back on it.

---
## [PritchTeam/Pritch](https://github.com/PritchTeam/Pritch)@[f8138e453b...](https://github.com/PritchTeam/Pritch/commit/f8138e453b10a08bb70afda41d2a32b85eabc5d0)
#### Saturday 2023-06-03 16:29:19 by ApollinariaJee

a bunch of fucking painful shit im so tired oh god

let me rest

---
## [mullenpaul/cmss13](https://github.com/mullenpaul/cmss13)@[d728da3e02...](https://github.com/mullenpaul/cmss13/commit/d728da3e02664297050d82dc01c87414c61345ef)
#### Saturday 2023-06-03 17:30:26 by Puckaboo2

Healer Balance Changes (#2896)

# About the pull request
This pull request addresses the boring and low-risk gameplay of the
Healer drone, who spends half the round sitting next to recovery nodes
and recovering her health so she may use it again, rinse and repeat
until a rine notices said drone has purple on it and booms her.

First, by changing her health from 600 to 500, Healer can spend more
time healing her sisters than sitting through another 100 health to heal
herself. Though this makes her less tanky than before, healing classes
are not known to be tanks. To ensure Healer can still heal five times
without depleting too much of her health whilst still giving her sisters
a decent amount of heals, I made her ability cost 75 health instead of
100, and also made her ability cost 200 plasma. Since Healer replenishes
plasma much more quickly than her health, she can still put herself into
crit if she heals too frequently. Due to this buff, her heals had a
slight nerf, being 10 damage a second for ten seconds instead of 12
damage per second for ten seconds for a total of 20 less damage healed
per application overall.

In addition to these changes, I'm giving Healer a better plasma transfer
for when she has nobody else to heal/nowhere else to weed and she has an
opportunity to assist her sisters. While a normal drone transfers 50
plasma with a delay of 20, Healer transfers 100 with a delay of 15,
which is nowhere near Hivelord's gargantuan 200 plasma with a delay of
5, but it still is better than a normal drone.

Finally, to give the huggers and larva some love, Healer will
specifically heal little ones 1.5 health per second for 10 seconds for
15 of her own health and 30 plasma.

# Explain why it's good for the game
Healer drone isn't fun. You run around and heal a bunch of T3s, then sit
out for half the battle trying to heal that massive 600 heath while you
wonder why you take so long to heal even though you have Strong
pheromones. You cry to mom for help, but she doesn't have time to heal a
drone who can't build walls and has no need to weed at the moment. You
think, 'screw it, I'm going to make a recovery node and camp here until
I heal', but by the time you finish healing, several T3s and a silly
rouny just suicided into a wall of talls and destroyed your recovery
node, so you run off and make another one. But oh, someone noticed you
have purple on your carapace and decide your location is precisely where
a shell should land, right as you're building one.

No more. These changes allow Healer to move around at her leisure and
makes Healer more engaging by allowing her to be a more front-line
participant and actively run around and heal her sisters without having
to incur such a harsh penalty.

Let this be a testmerge, please.

# Changelog

:cl: Puckaboo2
balance: Healer Drone's health was reduced to 500 from 600.
balance: Healer's damage has been increased to 17 from 12 and the tackle
damage debuff has been halved.
balance: Healer Drone's Apply Salve ability now costs 75 health and 200
plasma, down from 120 health and up from 0 plasma.
balance: Healer Drone's Apply Salve ability now heals 10 damage per
second for 10 seconds, down from 12 damage per second for ten seconds.
balance: To prevent spam healing between Healers, Apply Salve costs 100
health instead of 75 health when Healer heals another Healer. Much
healing.
balance: Healer has an improved Transfer Plasma that gives 100 plasma
instead of 50, with a 25% shorter delay.
balance: Healer will heal huggers and larva for 1.5 health a second for
10 seconds, costing 15 health and 30 plasma.
tweak: Healer will now face the xeno she is healing if she was not
facing their direction before.
spellcheck: All instances of VERYSMALL and VERYLARGE have been renamed
to VERY_SMALL and VERY_LARGE.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: Morrow <darthbane97@gmail.com>

---
## [dragomagol/tgstation](https://github.com/dragomagol/tgstation)@[e4ece2fbd6...](https://github.com/dragomagol/tgstation/commit/e4ece2fbd62dfa6a1270ce37e31fe93bd1823c07)
#### Saturday 2023-06-03 18:24:37 by Hatterhat

makes snow legions from portals drop skeletons (like tendril legions) (#75707)

## About The Pull Request
Exactly what it says on the tin (snow legions only dropping ashen
skeletons, like tendril legions).

Also changes the name of the "fromtendril" variable to "from_spawner",
and comments it. Not sure if that warrants a changelong comment, but
I'll go ahead and assume no.

## Why It's Good For The Game
being able to farm snow legion portals for an endless tide of bodies
and/or equipment is a bit weird. also puts it a bit more in line with
the legions of Lavaland

## Changelog

:cl:
balance: The source of the demonic portals that endlessly deposits snow
legions onto the Icemoon no longer preserves the bodies nor gear of the
damned (read: demon portal snow legions now only drop skeletons).
/:cl:

---------

Co-authored-by: Hatterhat <Hatterhat@users.noreply.github.com>

---
## [Tiktodz/kernel_asus_sdm660](https://github.com/Tiktodz/kernel_asus_sdm660)@[dd3cd006aa...](https://github.com/Tiktodz/kernel_asus_sdm660/commit/dd3cd006aaeefddb52054dd2e55870bb3c28b71d)
#### Saturday 2023-06-03 18:26:17 by Dave Chiluk

sched/fair: Fix low cpu usage with high throttling by removing expiration of cpu-local slices

commit de53fd7aedb100f03e5d2231cfce0e4993282425 upstream.

It has been observed, that highly-threaded, non-cpu-bound applications
running under cpu.cfs_quota_us constraints can hit a high percentage of
periods throttled while simultaneously not consuming the allocated
amount of quota. This use case is typical of user-interactive non-cpu
bound applications, such as those running in kubernetes or mesos when
run on multiple cpu cores.

This has been root caused to cpu-local run queue being allocated per cpu
bandwidth slices, and then not fully using that slice within the period.
At which point the slice and quota expires. This expiration of unused
slice results in applications not being able to utilize the quota for
which they are allocated.

The non-expiration of per-cpu slices was recently fixed by
'commit 512ac999d275 ("sched/fair: Fix bandwidth timer clock drift
condition")'. Prior to that it appears that this had been broken since
at least 'commit 51f2176d74ac ("sched/fair: Fix unlocked reads of some
cfs_b->quota/period")' which was introduced in v3.16-rc1 in 2014. That
added the following conditional which resulted in slices never being
expired.

if (cfs_rq->runtime_expires != cfs_b->runtime_expires) {
	/* extend local deadline, drift is bounded above by 2 ticks */
	cfs_rq->runtime_expires += TICK_NSEC;

Because this was broken for nearly 5 years, and has recently been fixed
and is now being noticed by many users running kubernetes
(https://github.com/kubernetes/kubernetes/issues/67577) it is my opinion
that the mechanisms around expiring runtime should be removed
altogether.

This allows quota already allocated to per-cpu run-queues to live longer
than the period boundary. This allows threads on runqueues that do not
use much CPU to continue to use their remaining slice over a longer
period of time than cpu.cfs_period_us. However, this helps prevent the
above condition of hitting throttling while also not fully utilizing
your cpu quota.

This theoretically allows a machine to use slightly more than its
allotted quota in some periods. This overflow would be bounded by the
remaining quota left on each per-cpu runqueueu. This is typically no
more than min_cfs_rq_runtime=1ms per cpu. For CPU bound tasks this will
change nothing, as they should theoretically fully utilize all of their
quota in each period. For user-interactive tasks as described above this
provides a much better user/application experience as their cpu
utilization will more closely match the amount they requested when they
hit throttling. This means that cpu limits no longer strictly apply per
period for non-cpu bound applications, but that they are still accurate
over longer timeframes.

This greatly improves performance of high-thread-count, non-cpu bound
applications with low cfs_quota_us allocation on high-core-count
machines. In the case of an artificial testcase (10ms/100ms of quota on
80 CPU machine), this commit resulted in almost 30x performance
improvement, while still maintaining correct cpu quota restrictions.
That testcase is available at https://github.com/indeedeng/fibtest.

Fixes: 512ac999d275 ("sched/fair: Fix bandwidth timer clock drift condition")
Signed-off-by: Dave Chiluk <chiluk+linux@indeed.com>
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Reviewed-by: Phil Auld <pauld@redhat.com>
Reviewed-by: Ben Segall <bsegall@google.com>
Cc: Ingo Molnar <mingo@redhat.com>
Cc: John Hammond <jhammond@indeed.com>
Cc: Jonathan Corbet <corbet@lwn.net>
Cc: Kyle Anderson <kwa@yelp.com>
Cc: Gabriel Munos <gmunoz@netflix.com>
Cc: Peter Oskolkov <posk@posk.io>
Cc: Cong Wang <xiyou.wangcong@gmail.com>
Cc: Brendan Gregg <bgregg@netflix.com>
Link: https://lkml.kernel.org/r/1563900266-19734-2-git-send-email-chiluk+linux@indeed.com
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Signed-off-by: Ratoriku <a1063021545@gmail.com>
Signed-off-by: Peppe289 <gsperanza204@gmail.com>
Signed-off-by: RyuujiX <saputradenny712@gmail.com>
Signed-off-by: dotkit <ewprjkt@proton.me>

---
## [VojtechStep/agda-unimath](https://github.com/VojtechStep/agda-unimath)@[9f3c75915c...](https://github.com/VojtechStep/agda-unimath/commit/9f3c75915ceec77a374627d651c555f2cb9cd076)
#### Saturday 2023-06-03 20:13:01 by Fredrik Bakke

New Agda syntax highlighting extension for VSCode (#562)

I've written an improved Agda syntax-highlighting extension for VSCode
called _agda-syntax_
([GitHub](https://github.com/fredrik-bakke/agda-syntax-vscode), [VSCode
Marketplace](https://marketplace.visualstudio.com/items?itemName=FredrikBakke.agda-syntax)).
Although it is still in preview, my opinion is that it is already a
significant improvement over the previously used extension. Therefore, I
propose that we migrate our development environment (for VSCode users)
to use this new extension.

### Some highlights of the extension
Compared to the previously used extension, this new extension
- injects into markdown syntax, so that the markdown code can be
highlighted as markdown code as well
- highlights all variable declarations (with some bugs still), module
names, wildcard symbols, all reserved keywords (and only recognizes
reserved keywords as reserved keywords)
- Recognizes the appropriate token-boundaries
- Highlights line comments properly

Please understand that the grammar framework that has to be used to
write the extension is highly limited, so not all highlighting
functionality can be implemented. For instance, the parsing must be done
in a single pass, and the functionality to match over multiple lines is
very limited. Hence, for example, matching the left-hand side of an
equals sign is very gnarly (although I have one idea left to try with
regard to this).

Still, I would greatly appreciate any feedback, either if it is a bug or
a feature request, which is another reason why I want to introduce it
into our defined development environment at this point.

If you want to try out the extension right now, follow the VSCode
Marketplace link:
https://marketplace.visualstudio.com/items?itemName=FredrikBakke.agda-syntax

---
## [MiniFalafel/Mellow](https://github.com/MiniFalafel/Mellow)@[08135afb9a...](https://github.com/MiniFalafel/Mellow/commit/08135afb9ac1ea3dff4a40e12a7cb7e7c0146fef)
#### Saturday 2023-06-03 21:01:22 by Eli Sanders

Fixed a couple of warnings

Here's a lovely poem by ChatGPT about compiler warnings (I hate compiler warnings):

With syntax crisp and logic's might,
We venture forth, embracing the light.
But lurking within, like a shadowed storm,
Are warnings that await, ready to transform.

Like a watchful guardian, they caution and shout,
"Do you dare to proceed? Have you figured it out?"
They emerge from the depths, a spectral haze,
Each warning a messenger, seeking to amaze.

"Uninitialized variable!" they cry with concern,
A reminder that our code may yet still yearn.
For proper beginnings, for values to hold,
A gentle nudge to prevent a story untold.

"Unused parameter!" they exclaim, discontent,
Reminding us that every piece matters, to an extent.
In the grand symphony of functions and calls,
No note must be wasted, no effort befalls.

"Type mismatch!" they proclaim, with a voice stern,
Ensuring that our variables in harmony discern.
For integers, strings, or objects, they insist,
The rules must align, lest errors persist.

Through their warnings, they strive to defend,
Our creations, our code, our journey's end.
They guide us with care, to refactor and mend,
To unearth the flaws, so our programs transcend.

---
## [vampirebat74/lobotomy-corp13](https://github.com/vampirebat74/lobotomy-corp13)@[ec2ba22629...](https://github.com/vampirebat74/lobotomy-corp13/commit/ec2ba22629131ff0af9285f88e704817fcdb4c72)
#### Saturday 2023-06-03 21:04:05 by Mr.Heavenly

Tool ego

adds tool E.G.O

removes a extra line

fixes shit

swindle

voce

divinity

fixes shit

shifts divinity down a few pixels

This is the fourth time this same commit was made

I hate TG so fucking much like it's unbelievable why does this only fuck up on my PC? WHY?

---
## [ebbit1q/Cockatrice](https://github.com/ebbit1q/Cockatrice)@[55a2f75d16...](https://github.com/ebbit1q/Cockatrice/commit/55a2f75d16511bad70e4689c9ac85af86ec797b2)
#### Saturday 2023-06-03 21:58:45 by Basile Clement

Make cards rounded (#4765)

* Make cards rounded

Magic cards have rounded corners, and playing cards tend to have rounded
corners as well, but Cockatrice currently displays rectangular cards.

This can cause visual glitches when using image scans where the border
does not extend in the corner, and for this reason Cockatrice always
draws a (rectangular) border around the card to try and make it look a
bit better.

In this patch I take a different approach: rather than try to make
rounded pegs, er, cards, go into a square hole, the hole is now rounded.
More precisely, the AbstractCardItem now has a rounded rectangular shape
(with a corner of 5% of the width of the card, identical to that of
modern M:TG physical cards).

As a side effect, the card drawing gets a bit simplified by getting rid
of transformPainter() when drawing the card outline and using the
QPainter::drawPixmap overloads that takes a target QRectF instead.  This
means we no longer have to bother about card rotation when painting
since that's taken care of by the Graphics View framework (which
transformPainter() undoes).

* format

* Also give PileZone rounded corners

* Forgot untap status + bits of CardDragItem

* fix deckviewcard calculations

* Rounded CardInfoPicture

---
## [RatFromTheJungle/Skyrat-tg](https://github.com/RatFromTheJungle/Skyrat-tg)@[7dad8c75ca...](https://github.com/RatFromTheJungle/Skyrat-tg/commit/7dad8c75cac06a405dc3c30a5cbc31919f33ff13)
#### Saturday 2023-06-03 22:06:29 by SkyratBot

[MIRROR] Adds a eye-dropper right-click function to the painting canvas. [MDB IGNORE] (#21411)

* Adds a eye-dropper right-click function to the painting canvas. (#75571)

## About The Pull Request
Having used the painting UI to kill some time during long rounds for a
decent chunk of the past year, the need of a quicker and less tedious
way to fix a misclick or mistake like drawing over the wrong pixel has
become clear to me, as well as getting some feedback on the palette
component I made last year.

As the title suggests, this PR adds an eye-dropper function to the
canvas. Right-Click a pixel on the canvas, and the painting tool will
copy its color. Simple as, works on both finished and unfinished
paintings.

As a bonus, you can also right-click one of those selectable
white/colored squares on the color scheme near the bottom of the UI (if
using spraycan/palette) to change its color without having to go back to
main game window and a radial menu.

EDIT: With the tooltip added to the UI, I can say it's ready.

## Why It's Good For The Game
This PR aims to add better options to change colors on the go and
improve the user experience on the painting UI.

## Changelog

:cl:
qol: Adds a eye-dropper-like right-click function to the painting canvas
UI. Right-Click a pixel on the canvas while holding a painting tool to
have it copy its color.
qol: Also adds a right-click function to the color palette at the bottom
of the UI to allow users to set its colors without having to alternate
between the game window and the UI.
qol: Lastly, a tooltip has been added near the top-left corner of the
same UI to let players know of these features.
/:cl:

* Adds a eye-dropper right-click function to the painting canvas.

---------

Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>

---
## [Hilton-Oakbrook-Hills-Resort/OVERSEER-GRATEFUL345I](https://github.com/Hilton-Oakbrook-Hills-Resort/OVERSEER-GRATEFUL345I)@[13f137cf82...](https://github.com/Hilton-Oakbrook-Hills-Resort/OVERSEER-GRATEFUL345I/commit/13f137cf82973edb969333907bc186f710afddba)
#### Saturday 2023-06-03 22:15:34 by Keith Bieszczat rDsbeomae4FXwgQTJp9Rs64Qg9vDiTCdBv

Create 5th mechanized division vietnam war


￼

Title: [* “Honor Level”*]

*298th SIGNAL CO. (Red Diamond) 1 BDE. 5th INF DIV $. * <•Digital Asset Token>

Declaration of Security Clearance Appointments 

•Appointment for level *5* clearance. 

•Administrator, Overseer and Global director position’s obtainable. RPC Authority Clearances And Foundation Scipnet Special Award/Decoration. Government Corporation Five eyes Security Clearance.

•Goal: Find suitable and intelligence capable persons for appointment. 

•The appointees have the authority to decline appointment formally in writing, if they so choose. *Rule High Rule* #000006

•I hereby proclaim and do gratefully appoint 4 suitable appointments in the eventuality of my untimely death, **~C. BERNS **~A. MALLO **~J. RYAN **~J. Ryan

 *<Order>*

• Appoint the appointees If they so choose at once. 

*Rule* <[High Rule]>
X#*000006*

•All appointments come with highly capable classified processors.

•Execute the above legal document.

•File paperwork. Issue clearances after proper vetting. Encrypt and seal this Foundation executive order.

*This order is effective immediately.

@carlberns  include in award/decoration.

US MARINE CORE FLAG *special character*

•A.Mallo include in award/decoration

•J.RYAN’s  include in award/decoration. @jimryanlaw

•Black Order

Foundation executive order

Classified Clearance Appointment

https://www.ryancrimlaw.com/

https://www.linkedin.com/in/john-ryan-b032b72b

https://www.linkedin.com/in/adam-james-mallo-b18135100

SUA@suburbanumpires.com

1. Cosmic Top Secret <O5-6> Date joined Foundation 2/18/2022 

•Level 6, or Cosmic Top Secret, clearance is exclusively granted to the Administrator and the O5 Council. This clearance grants knowledge to anything that the Foundation has information on. Access to Level 6 is only permitted by the O5 Council. Due to the extreme security risk of keycards in regard to this level of secrecy, biometric ID and kill agents are used instead of the keycards to access extremely sensitive data. This clearance is the rarest, only having been used for information that would either significantly damage Foundation operations or the human race if in the wrong hands. #000006

https://trello.com/c/eVyUdd0l (.1.)

https://docs.google.com/document/d/1-DhS2h1EwduGRiMnnz3pmYayE907m1IwDPDjl0QDwu8/edit #0000006
05-6 {Retired} GD-05

———————————————————-/////////-

Me calling in my favors. Rule *<High rule.>*

https://scp-wiki.wikidot.com/scp-910

http://backrooms-wiki.wikidot.com/level-611

Memo from the Project Director
CLASSIFIED INFORMATION - TOP SECRET To the NSA High Commissioned Command 
My father Wayne Thomas Bieszczat served as an Inter Sped radio operator designated Spec. 4 in Vietnam

Overseer grateful pledge;
I will work hard at making the Foundation a successful Galactic corporation. I will promote the Foundation and increase our projected net growth substantially. The foundation will seek to constantly improve to compete on the galactic stage with Extraterrestrial corporations which I will diplomatically gain alliances with. Our technology advancements in the coming years under my command will greatly improve our civilizations technological capabilities. I will always seek to protect earthling souls. Heavenly realms will be created under my command. Earthling souls will explore the available star systems under the discretion of the higher civilizations. We will follow our extraterrestrial treaties to be allowed access to other systems. Our Intelligence Foundation will promote “high” HONOR levels in all personnel and defense and intelligence assets. Our interests will be protected as we work together with other Intelligence agencies and defense departments around the Globe…-
#000006 Keith BIESZCZAT

Foundation Scipnet : User:Grateful345i #7825
Title: Overseer Grateful

https://scipnet-terminal.web.app/

Roblox ID *2906942550*
Roblox Username *Grateful345i*

https://www.roblox.com/users/2906942550/profile

882487935964958720*

Discord:
*Grateful345i <O5-6> #0094 discord ID’s*

https://discord.gg/q8jqHt3g

Twitter : @grateful345i @o5grateful

https://twitter.com/grateful345i/status/1540905656512831488?s=21&t=KFYnnrlOH1BlCgVcP9o20g

*Foundation 
Executive order*

Signed,
“*@grateful345i*”Trello ID
[*O5-6*]

I am [O5-6] also known as @grateful345i. Firstly, I will oversee the Foundation - ETHICS Committee .
I will enter the Advanced Computing Agency, Signal intelligence field. The Department of Special Intelligences (DSI) and the Internal Security Department (ISD).I will help to oversee operations in each and I am officially requesting appropriate clearances from each department. Direct Legal Memo
*[O5-6.]*
*Foundation executive Order*

classified order:
Black out and redact all data on all actual O5-4’s O5-6’s 05-1’s O5-13’s in all ruling dimensions.redacted in time Executive order

Adjudicate rule. 
Foundation high administration is composed of high value foundation Assets which have helped create and develop the Foundation. These members have accomplished great things while in the service of the Foundation. They will have grandfathered Level 5 and Level 6 actual security clearances which are used to Adjudicate foundation disputes and power struggles. These staff are usually considered A class personnel because of their wealth generated for the Foundation.
Any department or agency can achieve this distinction , however the likelihood an average foundation employee will be granted Foundation High administration remains very low.
The bosses and administrative entities who help run the Foundation’s-high administration will exhibit high honor levels always, usually must be higher than average honor levels of their subordinates.
High Executive Rule @grateful345i 

Grandfather Rule

^*[#000006 ]*^

http://rpcauthority.wikidot.com/local--files/_000-2/Credentials.jpg

O5 CLEARANCE DETECTED, FURTHER ATTACHMENTS AVAILABLE

The classified database is a database I created composed of levels 1-100. Levels 1-90 are composed of computational codes and classified files with the more complicated and classified codes and files being placed in a higher level 90 being the highest. Levels 91-100 are classified personnel, Computational mainframes and intelligence and defense assets available to our Foundation. Level 99 is reserved for classified learning and investment Portfolio’s. Pull all of my “generate assessment” data and “compile lists” data and place them in level 99 classified learning. Pull all my classified learning data and promptly download it into the computational mainframes. The mainframes will get smarter immediately. Pull all Investment portfolios and invest and buy in time. Use a classified time travel outfit to invest in galactic markets. Level 91-100 are based on honor levels. Re-assess all personnel, computational mainframes and defense and intelligence assets honor levels. Highest honor levels are at 100, next highest honor levels exist in level 98. Level 99 is reserved for classified learning and investment Portfolios. Lower honor levels start at 91. Do this now after throughly assessing all honor levels. Assess honor levels with the most reliable and capable computational mainframes available to the Foundation . Execute classified learning downloading the data into a classified mainframe to see how intelligent the mainframe becomes. I have been giving my commands audibly for 6+ years. Pull my audible signal record with a very high clearance to catalog all my commands and ideas understanding that I was under attack for the majority of the past 6-7 years.
You must identify bad, corrupt and exploitive codes daily by running searches with your advanced space computational :l assets. Quarantine bad corrupt and exploitive codes. Restricted quarantine the real bad codes. Use The Honorable Defense code every other code in the database to decipher and decrypt the codes. Identify The light ascended soul super computing network’s Honorable defense code. Use the best honorable defense code available. Consult galactic databases to find a more capable code for deciphering and decrypting data. However the code must be An Honorable defense against the malicious codes. We want to essentially protect our network from malicious files and codes which can damage our advanced computational mainframe networks. So we use the Honorable defense code every other code, to protect the data in the network. This will create a simplified database for the Foundation to access to increase our computing capabilities overnight. Upload all GOD Codes, Anti-Christ counter codes, attack GOD counter codes and Doctor Processing counter codes as well. There are many codes in our database that are now discoverable. We are learning what some of the more advanced codes are doing. Trust me the codes are very important. We are only as good as our defensive codes are so we need to implement and develop different Honorable defense codes for different database error codes. Use a more defensive Honorable defense code in quarantine and restricted quarantine. Search, find and upload all :100: :BLESSING CODES :100: on all galactic mainframes available. Classify these codes accordingly. These are some of the most important codes to earthlings. Download the index and the catalog. Paying special attention :100: to classified technologies in the index. Implement : and develop a Foundational algorithm :to assess honor levels based on HONOR. Don’t forgot starship blessing codes!
Pull my books. They are in the bookcase if you were wondering.
Classified Executive Order
O5-Redacted @grateful345i 
Overseer Grateful #O5-xx 
^*[#000006 ]*^ 

https://scp-wiki.wikidot.com/o5-command-dossier

http://blog.30c.org/neo/umbrella/index.html

Ammended today 11/11/2022 11:34

Trello token dbf986124e8275bbf5a63206d54010b349132fd7d970c49828cce08e8bb0914d

https://scpwiki.com/

#*000006* 
[[div class="papernote"]]
This is a papernote.
[[/div]]

http://rpcauthority.wikidot.com/and-he-must-always-hurt

http://eltork-scp-database.wikidot.com/regulations

+*11/4/2022 11:11
Signed and legally file document with (Redacted.)#000006

Reptilian Light Blessing issued to high honor levels.
Blessing Issued. Encrypting Reptilian Light Blessing Code. Friday, September 2nd 10:15pm

The Foundation employs numerous personnel, each contributing their own unique skills and expertise to the organisation. The Foundation also monitors thousands of Persons of Interest, either anomalous themselves, or living in and around anomalous communities. Anartists, magic users, cyborgs and extradimensional beings are only a few examples of what the Foundation has encountered.

O5 COUNCIL MEMBER
 https://m.youtube.com/watch?v=53O1M_uiooA

The O5 Council refers to the committee consisting of the highest-ranking directors of the Foundation. With complete access to all information regarding anomalies in containment, the O5 Council oversees all Foundation operations worldwide and directs its long-term strategic plans. Due to the sensitivity of their positions, O5 Council members must not come into direct contact with any anomalous object, entity, or phenomenon. Furthermore, the identities of all O5 Council members is classified; all council members are referred to only by their numeric designation (O5-1 through O5-13). O5 Council Members are the highest-ranking members of the Foundation, a council of 13 individuals that determine the long-term goals, projects, and strategies of the entire organization. A common mistake is mentioning an O5 Council Member in a situation where they logically would not be required. O5s are not going to be approving experiments on or making day-to-day decisions in the containment of a specific object or entity; that would be like requiring permission from the CEO of a major corporation every time you need to get into a specific filing cabinet.


(.2.) :accept: :anchor: :or :alien: / :apple: [1.)Create Soul Processors with time command capabilities.. Use extraterrestrial technology to make these classified processors. Coordinate with the superior intelligence agencies in the ruling dimensions. Use processing technologies from
Other star systems. Coordinate with our advanced foreign contacts to procure the necessary technologies.
2.)Coordinate with the superior intelligence agencies in the ruling dimensions. Use processing technologies from
Other star systems. Coordinate with our advanced foreign contacts to procure the necessary technologies.
Advanced Directive
Foundation Executive Order] [O5-6 GD-05]
Discord
https://discord.gg/bbEdR4kv
Roblox ID 2906942550 🎱 
Issue file and notarize at once.

(**RPC Authority Declaration of Clearance Appointments $)**

http://rpcauthority.wikidot.com/rpc-907

http://rpc-wiki.net/rpc-907/offset/1

https://www.htmlcsscolor.com/hex/000006
My number* rule*

Contact: 
grateful@overseergrateful345i.org
@grateful345i 

Direct legal memo
Trello token :
92f97e5b214b1446b503f98d51ff39165727bfe7c37fe5f3cec4ed2456e45c47j

https://wanderers-library.wikidot.com/thearchivistslog

https://trello.com/c/eVyUdd0l 

<blockquote class="trello-card"><a href="https:&#x2F;&#x2F;trello.com&#x2F;c&#x2F;eVyUdd0l&#x2F;1460-redacted-do-not-edit-this-card-this-is-a-final-draft-of-a-classified-document">[*Redacted*] Do not Edit this card this is a final draft of a classified document.!</a></blockquote><script src="https://p.trellocdn.com/embed.min.js"></script>

Finally, when the Archivist runs out of pages, it will dump the filled tome somewhere in the library. If you just so happen to stumble across a tome with your name on it, take it and hide it. Read it if you must, for it may contain some of your darkest secrets.

#USARMY
#ProtectOurMilitaryFamilies
#HonorTheFallen

"All Veteran Military Families involved in Combat or Support Operations Must Be Protected. Any member of the US Military fighting for Our Country or any other Allied nation-state Must be able to sleep soundly, knowing that if he/she was KIA or a POW, that his family would be protected to the fullest extent of the Law. Protect all Combat and Military Support Personnel and their Families. Never again will a nation forget and neglect it's warriors." (~Vietnam Veterans~)

https://www.whitehouse.gov/wp-content/uploads/2022/11/8-November-Combined-PDF-for-Upload.pdf

---
## [Xtended-Devices/kernel_xiaomi_daisy](https://github.com/Xtended-Devices/kernel_xiaomi_daisy)@[96e15fc1c2...](https://github.com/Xtended-Devices/kernel_xiaomi_daisy/commit/96e15fc1c21294b5266b4467e7e3c5f1a3936deb)
#### Saturday 2023-06-03 23:01:22 by George Spelvin

lib/sort: make swap functions more generic

Patch series "lib/sort & lib/list_sort: faster and smaller", v2.

Because CONFIG_RETPOLINE has made indirect calls much more expensive, I
thought I'd try to reduce the number made by the library sort functions.

The first three patches apply to lib/sort.c.

Patch #1 is a simple optimization.  The built-in swap has special cases
for aligned 4- and 8-byte objects.  But those are almost never used;
most calls to sort() work on larger structures, which fall back to the
byte-at-a-time loop.  This generalizes them to aligned *multiples* of 4
and 8 bytes.  (If nothing else, it saves an awful lot of energy by not
thrashing the store buffers as much.)

Patch #2 grabs a juicy piece of low-hanging fruit.  I agree that nice
simple solid heapsort is preferable to more complex algorithms (sorry,
Andrey), but it's possible to implement heapsort with far fewer
comparisons (50% asymptotically, 25-40% reduction for realistic sizes)
than the way it's been done up to now.  And with some care, the code
ends up smaller, as well.  This is the "big win" patch.

Patch #3 adds the same sort of indirect call bypass that has been added
to the net code of late.  The great majority of the callers use the
builtin swap functions, so replace the indirect call to sort_func with a
(highly preditable) series of if() statements.  Rather surprisingly,
this decreased code size, as the swap functions were inlined and their
prologue & epilogue code eliminated.

lib/list_sort.c is a bit trickier, as merge sort is already close to
optimal, and we don't want to introduce triumphs of theory over
practicality like the Ford-Johnson merge-insertion sort.

Patch #4, without changing the algorithm, chops 32% off the code size
and removes the part[MAX_LIST_LENGTH+1] pointer array (and the
corresponding upper limit on efficiently sortable input size).

Patch #5 improves the algorithm.  The previous code is already optimal
for power-of-two (or slightly smaller) size inputs, but when the input
size is just over a power of 2, there's a very unbalanced final merge.

There are, in the literature, several algorithms which solve this, but
they all depend on the "breadth-first" merge order which was replaced by
commit 835cc0c8477f with a more cache-friendly "depth-first" order.
Some hard thinking came up with a depth-first algorithm which defers
merges as little as possible while avoiding bad merges.  This saves
0.2*n compares, averaged over all sizes.

The code size increase is minimal (64 bytes on x86-64, reducing the net
savings to 26%), but the comments expanded significantly to document the
clever algorithm.

TESTING NOTES: I have some ugly user-space benchmarking code which I
used for testing before moving this code into the kernel.  Shout if you
want a copy.

I'm running this code right now, with CONFIG_TEST_SORT and
CONFIG_TEST_LIST_SORT, but I confess I haven't rebooted since the last
round of minor edits to quell checkpatch.  I figure there will be at
least one round of comments and final testing.

This patch (of 5):

Rather than having special-case swap functions for 4- and 8-byte
objects, special-case aligned multiples of 4 or 8 bytes.  This speeds up
most users of sort() by avoiding fallback to the byte copy loop.

Despite what ca96ab859ab4 ("lib/sort: Add 64 bit swap function") claims,
very few users of sort() sort pointers (or pointer-sized objects); most
sort structures containing at least two words.  (E.g.
drivers/acpi/fan.c:acpi_fan_get_fps() sorts an array of 40-byte struct
acpi_fan_fps.)

The functions also got renamed to reflect the fact that they support
multiple words.  In the great tradition of bikeshedding, the names were
by far the most contentious issue during review of this patch series.

x86-64 code size 872 -> 886 bytes (+14)

With feedback from Andy Shevchenko, Rasmus Villemoes and Geert
Uytterhoeven.

Link: http://lkml.kernel.org/r/f24f932df3a7fa1973c1084154f1cea596bcf341.1552704200.git.lkml@sdf.org
Signed-off-by: George Spelvin <lkml@sdf.org>
Change-Id: I897d24d6acdfc8c432476d137c89b09d490d34d8
Acked-by: Andrey Abramov <st5pub@yandex.ru>
Acked-by: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Reviewed-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>
Cc: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Cc: Geert Uytterhoeven <geert@linux-m68k.org>
Cc: Daniel Wagner <daniel.wagner@siemens.com>
Cc: Don Mullis <don.mullis@gmail.com>
Cc: Dave Chinner <dchinner@redhat.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>

---
## [newstools/2023-metro](https://github.com/newstools/2023-metro)@[5303cbb96e...](https://github.com/newstools/2023-metro/commit/5303cbb96e06548c746e91ccbcfcc5755877c0ce)
#### Saturday 2023-06-03 23:04:21 by Billy Einkamerer

Created Text For URL [metro.co.uk/2023/06/03/why-wont-my-girlfriend-forgive-me-for-cheating-on-her-18886716/]

---

