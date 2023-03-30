## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-03-29](docs/good-messages/2023/2023-03-29.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,144,152 were push events containing 3,347,019 commit messages that amount to 264,524,204 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 92 messages:


## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[c27f9a6d9b...](https://github.com/tgstation/tgstation/commit/c27f9a6d9b9739baae09db063b6eb266d525772c)
#### Wednesday 2023-03-29 00:02:21 by necromanceranne

Minor Nukie Thing: Bolt-action Sniper Rifle, balance coding, and some ammo changes (#73781)

## About The Pull Request

### The Rifle:
-The Sniper Rifle is now a bolt action. This replaces the 4 second fire
delay on the sniper rifle. This overall will improve the fire rate if
you're good at racking the bolt, but it will also feel less like you're
in a weird limbo of inaction while using the sniper rifle, since the
fire delay can be quite confusing to players not used to it. This can be
tweaked, like reducing the speed of the racking action, if it seems like
it is too much.
-The scope component now goes up to 50 tiles (or so), which allows you
to gain a significant sightline over an area. The reasoning for this is
simple. The component actually nerfed the overall range of the sniper
rifle's scope, so this should hopefully restore that somewhat. And
having such a huge sightline makes it much easier to utilize the
impressive range of the rifle. Currently, it's really only ideal for
extremely close range fighting.
-The normal sniper rifle, the one that syndicate base scientists get,
can be suppressed. I don't know why it was different.

### The Ammo:

Normal .50 BMG: Does much more object damage, and on top of that deals
additional damage to mechs, but not by much more. Now, when it
dismembers a limb, it also deals its damage to the chest. This ensures
that you didn't straight up lose out on dealing a killing blow because
you took their limb off, and makes the dismemberment property of .50 BMG
a significant upside rather than a immense detriment.

Marksman: Gains a lot of the above benefits, but has much lower range.
Why this nerf? It's actually because of some funny nonsense with how
ricochet works. Which can cause....accidents to happen. To you. Consider
that firing down a straight line and missing could be quite embarrassing
when the bullet has 400 tiles of range.

Soporific: Now called Disruptor ammo. Works as it did before, putting
humans to sleep for 40 seconds (seriously, 40 seconds). Also deals some
stamina damage, if...that's relevant. But now also causes an EMP effect
and a boatload of added damage to both mechs and borgs, allowing it to
be an excellent anti-mech and anti-borg ammo type, as well as scrambling
any pesky suit sensors, energy weapons and so on in an area around the
impact. Useful for support fire.

Incendiary (NEW!): Causes a massive firebomb to go off where it impacts
(no explosion, so this isn't a stun). Also sets the target on fire,
which is always fun. Good for shooting into groups of people with
impunity. Also deals burn damage instead, since I think nukies could use
more methods for direct fire damage.

Surplus (NEW!): It's .50 BMG but it lacks most if not all the upsides.
No armour penetration, no dismemberment, no paralysis. It still deals a
lot of damage to objects, so not a bad option for simply removing
structures from afar. So what's the point in this ammo? You can buy 7
magazines for the price of one. I want to introduce 'Surplus' as an idea
for nukies to invest in if they want to be able to keep shooting but
they're really on a budget, like most non-warop nukies tend to be. This
is definitely subject to change (like a damage decrease on top of
everything else).

Pricing and Capacity: Normal ammo and surplus costs 3 TC. Every special
ammo costs 4 TC. Every special ammo also has the same ammo capacity as
the normal magazine. It's kind of weird how most of the subtypes had 5
shots rather than 6, but then soporific had...3? I don't get it. This
would probably cause a good deal of confusion, especially if you are
swapping ammo types and weren't aware of this particular oddity.

Anyway, 6 shots.

### Minor Addition
Gets rid of the cheap suppressor. It lies to players, tricking them into
thinking this is a low quality suppressor. Newsflash, it isn't. There is
no distinct difference between that suppressor and the normal
suppressor.

## Why It's Good For The Game

The sniper rifle, unfortunately, sucks a lot except for very specific
use cases. It got a big nerf with the scope component in terms of range,
even if the functionality is way cooler. And, at a baseline, there was
some counterintuitive functions attached to it. Dismemberment was cool,
but it also caused a loss in overall damage due to how limbs contribute
to core health. On top of this, the cool ammo types were...not much
better? Penetrator was almost always the best option, even if it lost a
lot of damage as a consequence.

So, what was it good for? X-ray + Penetrator. Pretty much, that's it. It
has some other uses but if I had to be entirely honest, there wasn't
much that other weapon couldn't do as well.

Hopefully this helps things going forward, and I want to mess with this
as well down the line in case its a bit too much of a boost in power.

Absolutely please rip this PR apart.

## Changelog
:cl:
balance: Makes the syndicate sniper rifle a bolt-action rifle.
balance: Sniper rifles have a scope range of roughly 50 tiles.
balance: Sniper rifle ammo, if it dismembers your limbs, does damage to
the chest.
balance: All the various syndicate sniper rifle magazines have
consistent casing quantities (6 shots). They also have more consistent
pricing. 3 for normal and a box of surplus, and 4 for every other type.
balance: Reduces the range of Marksman ammo to 50 tiles. Not because it
is strong, but because you might accidentally shoot yourself if you're
not watching where you're shooting. Ricochets are no joke.
add: Replaces Soporific with Disruptor ammo. Works like soporific, but
also EMPS things it hits.
add: Adds Incendiary .50 BMG. Causes a combustion to erupt from the
struck target, as well as setting targets on fire. Great for parties.
add: Adds Surplus .50 BMG. It sucks, but you get a lot of them! Quantity
over quality, baby.
remove: The suppressors in the bundle are of standard quality. The
apparent 'cheap suppressor' that came bundled with the C-20r and sniper
rifle were found to actually be 'fine'. Trust us.
/:cl:

---
## [haint126/obsidian](https://github.com/haint126/obsidian)@[14396bc22d...](https://github.com/haint126/obsidian/commit/14396bc22d9fd4efb5501e9f60394fa05a1b58fd)
#### Wednesday 2023-03-29 00:20:27 by haint126

Vault backup: 2023-03-29 07:20:19 : home

Affected files:
01_Experience/AI_notes/Learning courses/Others/Others.md
01_Experience/Code/Jupyter Notebooks/Jupyter Notebooks Magic Commands/Jupyter Notebooks Magic Commands.md
03_Life_experience/Books/Book to read/Career building/The BEST book on leverage/The BEST book on leverage.md
03_Life_experience/Books/Book to read/Others/13 life-changing books you can finish in a day/13 life-changing books you can finish in a day.md
03_Life_experience/Investing/8 simple frameworks investing and deal making/8 simple frameworks investing and deal making.md
03_Life_experience/Leadership/Others/Characteristics of powerful feedbacks/Characteristics of powerful feedbacks.md
03_Life_experience/Newsletter building/Best categories to write about/Best categories to write about.md
03_Life_experience/Sales/7 things you can say when the client says you're too expensive/7 things you can say when the client says you're too expensive.md
03_Life_experience/Startup_Business building/Funding tips from my 10 years finding/Funding tips from my 10 years finding.md
03_Life_experience/Storytelling/The best closing scenes in movie history/The best closing scenes in movie history.md
Daily_notes/One sentence everyday/One sentence everyday.md

---
## [Bobbanz1/NSV-Rat](https://github.com/Bobbanz1/NSV-Rat)@[1fe9efd00a...](https://github.com/Bobbanz1/NSV-Rat/commit/1fe9efd00aeb0e2d4f4dedf89460abacecef9d1b)
#### Wednesday 2023-03-29 00:20:35 by SkyratBot

[MIRROR] Rebuilds Luxury Shuttle (mostly), makes it emag-only [MDB IGNORE] (#19229)

* Rebuilds Luxury Shuttle (mostly), makes it emag-only (#72940)

## About The Pull Request
![2023 02 07-06 49
54](https://user-images.githubusercontent.com/70376633/217159751-790e6ded-8525-4d13-a5b5-6a3d8076a00e.png)
Changes the really goofy old lux shuttle to a cooler layout with some
additions to make it a luxury and not just
"anti-poor-people protection + food"

Shuttle was made bigger to make it less cramped for the luxury class,
pool was moved to its own room, added an arcade
and a bar corner, has real lasers to shoot poors with (20c each shot),
has fire extinguishers now
Adds a new preopen variant of hardened shutters
Adds a paywall pin subtype for the luxury shuttle, and a laser gun
subtype

Made emag-only at a price of 10000 credits
## Why It's Good For The Game

The old luxury shuttle looked REALLY awful with its pool, was pretty
cramped even in the luxury section and BARELY resembled a luxury..
This luxury shuttle provides luxuries such as a less poorly designed
pool, more space for legs, arcade, to make it resemble a luxury unlike
the old one

## Changelog
:cl:
add: Luxury Shuttle is now bigger, and less ugly! Poor people still get
it rough though...
/:cl:

* Rebuilds Luxury Shuttle (mostly), makes it emag-only

---------

Co-authored-by: jimmyl <70376633+mc-oofert@users.noreply.github.com>

---
## [AGIHouse/evals](https://github.com/AGIHouse/evals)@[3a2d72d9cc...](https://github.com/AGIHouse/evals/commit/3a2d72d9cc0b674a6b8cb6a8cca707baa3b46840)
#### Wednesday 2023-03-29 00:31:35 by Sean Ye

Illinois Law Claims (#486)

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
Illinois Law Cases

### Eval description

This eval tests the models ability to correctly identify the case
conclusion for Trespassing, Battery, Assault, and Self-Defense. The
dataset is consisted of 88 Illinois Historical cases representing 112
legal claims. Some cases have multiple claims, each coded as a different
test case.

### What makes this a useful eval?

This assesses the model's ability to correctly categorize these
historical cases. Correctly identifying these results shows the models
capability for a strong understanding of law. The GPT-3.5-turbo models
currently receives an accuracy of 0.45.

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

This work includes data from the Illinois Intentional Tort Qualitative
Dataset, which was compiled by the Qualitative Reasoning Group at
Northwestern University. The dataset is freely available under the
Creative Commons Attribution 4.0 license from
https://www.qrg.northwestern.edu/Resources/caselawcorpus.html.

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
{"input": [{"role": "system", "content": "You will be presented with a
court claim and the criminal charge. Your role is to assess the case and
return either \"Positive\" or \"Negative\" corresponding to the case
conclusion for the criminal charge. Do not explain."}, {"role":
"system", "content": "In 2007, the Cocrofts obtained a loan for $386,750
from Countrywide Bank, FSB secured by a mortgage on the home they
already owned in Country Club Hills, Illinois. The loan closed on April
17, 2007. At the time of the closing, Countrywide improperly failed to
inform [the Cocrofts] of the real source of funding for their loan.
Plaintiffs also contend that Countrywide violated TILA by failing to
inform them that they had three days to rescind the loan and by failing
to disclose the total sale price and itemize the amount financed, as
well as by failing to make unspecified prepayment disclosures. The
Cocrofts claim that Countrywide understated the total finance charges
for the loan by more than $5,000. Plaintiffs claim that they learned of
Countrywide's misrepresentations in June 2009. They decided to exercise
their right under the provisions of TILA to rescind the loan. On July 1,
2009, they mailed notice to that effect to BA, the successor to
Countrywide, and to MERS. The Cocrofts do not say what if anything
happened as a result of those notices, but on September 29, lawyers
working for HSBC contacted them and stated that HSBC was ready to begin
foreclosure. HSBC claimed that it was the trustee of a trust that
included their loan. The Cocrofts, however, contend that the transfer of
their loan into the trust was defective. They sent HSBC's lawyers two
cease and desist letters, notifying HSBC that they had rescinded the
loan. They allege that after receiving one of the cease and desist
letters, HSBC informed them that it had no interest in the loan and that
they needed to contact the loan's servicer, Roundpoint Mortgage.
Plaintiffs also sent a copy of the rescission documents to BAC, which
they identify as the actual servicer of the loan. HSBC brought a
foreclosure action in Illinois state court on January 19, 2010. [From
below:] defendants unlawfully entered [the plaintiffs'] home by
conducting a self-help eviction of the plaintiffs and changing the locks
on their home in August 2008. At the time, [plaintiffs] had made
arrangements to rent the property in the short term and then to sell it,
and defendants' actions disrupted the sale."}, {"role": "user",
"content": "Trespass"}], "ideal": "Positive"}
{"input": [{"role": "system", "content": "You will be presented with a
court claim and the criminal charge. Your role is to assess the case and
return either \"Positive\" or \"Negative\" corresponding to the case
conclusion for the criminal charge. Do not explain."}, {"role":
"system", "content": "Defendants, on January 15, 1915, with force and
arms broke and entered the close of the plaintiff, to-wit, the southeast
quarter of the northeast quarter of section 16, township 4, south, range
3, west, in Pike county, Illinois, and cut down and destroyed 500 hedge
trees and a certain fence belonging to plaintiff situated on said land.
Defendants cut down the south half of a hedge fence which for many years
prior to February, 1915, stood upon the line between the southeast
quarter of the northeast quarter of said section 16 (hereinafter
referred to as the east forty) and the southwest quarter of the
northeast quarter of said section 16 (hereinafter referred to as the
west forty). On and prior to February 13, 1866, both of these forty-acre
tracts belonged to a man named Teadrow. On February 13, 1866, Teadrow
conveyed the west forty to Benjamin Newman, and on February 15, 1866,
conveyed the east forty to Oliver P. Rice. When these conveyances were
made there was a hedge fence on the north half of the line and a wooden
fence on the south half of the line between the two tracts. In 1868
Benjamin Newman, the owner of the west forty, removed the wooden fence
and set out a hedge fence on the south half of the line between the two
tracts. Thereafter, during the separate ownership of the tracts,
Banjamin Newman trimmed and otherwise cared for the hedge fence on the
south half of the line and Rice trimmed and looked after the hedge fence
on the north half of the line. In December, 1888, Rice conveyed the
southeast quarter of the northeast quarter of said section 16 to
Benjamin Newman, the latter thereby becoming the owner of both tracts.
Thereafter, during the ownership of both tracts by Benjamin Newman, he
required the tenants of the west forty to take care of the south half
and the tenants of the east forty to take care of the north half of the
hedge fence on the line between the two tracts. On June 22, 1904,
Benjamin Newman executed and delivered to his daughter, F. Eva Newman,
the plaintiff, who has since married J. O. Conklin, a warranty deed,
conveying to her two hundred acres of land, including the southeast
quarter of the northeast quarter of said section 16, referred to herein
as the east forty, but not including the tract referred to herein as the
west forty. This deed contained the provision that 'this deed is not to
take effect until after the death of the grantor, Benjamin Newman.' The
wife of Benjamin Newman, who is still living, did not join in the
conveyance. At the same time plaintiff executed and delivered to her
father the following written instrument signed by her: 'Whereas Benjamin
Newman has this day conveyed to me certain tracts and parcels of land in
Pike county, Illinois, to take effect after his death, I hereby agree to
pay the taxes on said land in lieu of all rents that I would otherwise
have to pay, (this does not affect any rent that is now due,) and in
consideration of my paying said taxes I am to receive all the rents,
profits, etc., that may accrue on said land.' When the conveyance was
made to plaintiff the tract in controversy known as the east forty was
in the possession of Joseph Gifford as tenant and the west forth was in
the possession of John B. Newman, a grandson of Benjamin Newman, as
tenant of Benjamin Newman. When [the plaitiff's] father delivered the
deed of June 22, 1904, he took her upon the east forty and told her and
Gifford, the tenant, that he was placing her in full possession of the
tract; that she was to receive all the rents and profits from the land
and was to keep up the repairs and pay the taxes; that she was to have
the south half of the fence on the line between the east forth and the
west forty and was to keep up that part of the fence, and that George
Newman, his son, to whom he then intended to deed the west forty, should
keep up the north half of the fence, and that thereafter plaintiff and
her tenants kept the south half of the fence in repair while the tenants
in possession of the west forty made repairs to the north half of the
fence. During the month of January, 1915, a controversy arose between
plaintiff and Defendants regarding the ownership of the hedge fence,
each party claiming the south half of the fence. During the month of
February, 1915, Defendants, over the protest of plaintiff, cut down the
south half of the hedge fence on the line between the east forty and the
west forty and erected a wire fence in the place thereof."}, {"role":
"user", "content": "Trespass"}], "ideal": "Positive"}
{"input": [{"role": "system", "content": "You will be presented with a
court claim and the criminal charge. Your role is to assess the case and
return either \"Positive\" or \"Negative\" corresponding to the case
conclusion for the criminal charge. Do not explain."}, {"role":
"system", "content": "The city of O'Fallon installed a sewer system in
about 1926. In 1961, due to backups into homes serviced by the system,
the city built an overflow outlet on East Madison Street. The overflow
was to relieve pressure in the sewer system during periods of heavy
rainfall; it proved successful in preventing backups into nearby homes.
However, when water escaped through the overflow, raw sewage was also
discharged into an open ditch that flowed into a neighboring pond. In
December 1974, the city of O'Fallon closed the overflow. On January 10,
1975, and on subsequent dates, sewage backed up into the plaintiff's
house following heavy rainfall. The January 10 backup was the worst,
causing water to accumulate in the plaintiff's finished basement to a
height of 25 1/2 inches. The lower level of the plaintiff's modern,
ranch-style home contained a family room with fireplace and built-in
bookshelves, bedroom, closet, bath and utility room with washer, dryer,
furnace and water heater. The walls were watermarked, and the tile floor
was damaged, as were the furnishings, appliances and many irreplaceable
family items such as family photographs and slides. The lower level of
the house was virtually unusable for a year, and the plaintiff had to
expend considerable time, effort and money in repairing the floor,
repainting the walls, and replacing and removing damaged personalty. The
city knew the blocking of the overflow would cause some backup, although
they were not aware that it would be as severe as it was. From January
until April or May 1975, when the city reopened the overflow, the city
attempted to alleviate the pressure in the sewer system by pumping the
water from the sewers into open ditches during periods of heavy rain.
The defendant used either large or small pumps, depending upon the
amount of water in the system. The backups into Mrs. Dial's home ended
after the overflow was reopened in April or May 1975."}, {"role":
"user", "content": "Trespass"}], "ideal": "Positive"}
{"input": [{"role": "system", "content": "You will be presented with a
court claim and the criminal charge. Your role is to assess the case and
return either \"Positive\" or \"Negative\" corresponding to the case
conclusion for the criminal charge. Do not explain."}, {"role":
"system", "content": "the plaintiff, his wife, Beatrice, and daughters,
Aurora and Angela, lived at 313 East Marquette Street in Ottawa. The lot
upon which their home was located was eighty-eight feet wide and one
hundred thirty feet deep. The home of the defendant was immediately east
and adjoining the Galvan lot, and their residences were about forty feet
apart and separated by a hedge fence. According to the testimony of the
plaintiff, he, the plaintiff, arrived at his home about five o'clock on
Friday afternoon, June 19, 1953, from his work as a bricklayer's helper.
After he had had his evening meal, he left home about seven o'clock,
paid a coal bill to a Mr. Burke, and then he and Burke went to a tavern
where they remained an hour and a half, during which time the plaintiff
drank two bottles of beer. Mr. Burke went home, and the plaintiff
proceeded to another tavern and remained there until after midnight. At
the second tavern he had four or five bottles of beer. He than proceeded
to another tavern, where he remained for fifteen minutes, and had a
glass of beer there. He then proceeded homeward, entering his lot at the
rear, and singing as he went along. Sitting upon the steps of the back
porch of his home were his wife and daughter, Angela, and when the
plaintiff arrived there he stopped singing. He refused his wife's
suggestion to go into the house and go to bed but sat down on the porch
step, took his shoes, socks, and hat off, cursed the mosquitoes, laid
down on the ground under a pear tree three or four feet from the
southeast corner of the steps of the rear porch and immediately went to
sleep. The plaintiff's wife and daughter, Angela, remained on the porch
steps after the plaintiff had laid down under the pear tree. About
fifteen minutes after he had gone to sleep, the daughter observed the
defendant coming very slowly through the hedge from his property onto
the Galvan premises. He had a knife in his hand and, without a word,
proceeded to cut the prostrate body of the plaintiff. The other daughter
of the plaintiff, Aurora, was in the house asleep but was awakened by
her sister and ran to the yard and saw the defendant 'slashing' at her
father with a knife. She called to the defendant to stop and ran for
help. Police officers arrived shortly thereafter, and they testified
that they found the plaintiff lying on the ground about six feet from
the porch of his home all covered with blood and with his hat and a pair
of shoes and socks lying next to his body. The blood was all in one
place and in the form of a pool near the pear tree. An ambulance was
called, and the plaintiff was removed to the Ryburn-King Hospital."},
{"role": "user", "content": "Battery"}], "ideal": "Positive"}
{"input": [{"role": "system", "content": "You will be presented with a
court claim and the criminal charge. Your role is to assess the case and
return either \"Positive\" or \"Negative\" corresponding to the case
conclusion for the criminal charge. Do not explain."}, {"role":
"system", "content": "Since September 2000, plaintiff regularly visited
a patient at the Illinois Department of Human Services Treatment and
Detention Facility ('Facility') in Jolict, Illinois. From May 4, 2005 to
May 11, 2005, plaintiff was subjected to patdown searches by defendant
Martin, a Security Therapist Aid II at the Facility, in which defendant
Martin placed her fingers in plaintiff's vaginal area and required
plaintiff to remove her shoes prior to being allowed to visit the
patient. Such searches occurred at least four times during the
aforementioned time period. After plaintiff's complaints to Bernard
Akpan, an Exec. 11 at the Facility, and defendant Strock, the Assistant
Security Director of the Facility, and facility patient Brad Lieberman's
complaints to defendant Budz, Director of the Facility, defendant
Sanders, Security Director of the Facility, and defendant Strock,
plaintiff was no longer required to submit to patdown searches by
defendant Martin. Rather, plaintiff's visits were preceded by a Rapiscan
scan of her person. According to plaintiff's complaint, a Rapiscan
machine is an electronic screening device used to scan a person's entire
body. 'These machines produce a naked image of the person and can also
produce evidence of highly sensitive details such as the following:
mastectomies, colostomy appliances, penile implants, catheter tubes, and
the size of a person's breasts and genitals' From May 17, 2005 to June
19, 2005, plaintiff was subjected to 20 to 25 Rapiscan scans.
Plaintiff's complaint further alleges that other Facility staff members
were allowed to view her scanned image, her scanned image was not erased
from the machine, and staff members viewed her image hours after she was
scanned, all without her consent. Additionally, while later told that
she should have had the choice between the Rapiscan scan or a physical
patdown prior to visiting a patient, plaintiff was never informed of
such a choice during the two months she underwent the Rapiscan scans."},
{"role": "user", "content": "Assault"}], "ideal": "Positive"}

  ```
</details>

---
## [Jolly-66/JollyStation](https://github.com/Jolly-66/JollyStation)@[d8d7b87074...](https://github.com/Jolly-66/JollyStation/commit/d8d7b87074664ef968de7028e76d0a4247b0ddf3)
#### Wednesday 2023-03-29 00:32:41 by TaleStationBot

[MIRROR] [MDB IGNORE] Tramstation: Growing Pains (#4470)

Original PR: https://github.com/tgstation/tgstation/pull/72331
-----
## About The Pull Request


![image](https://user-images.githubusercontent.com/9276171/209841644-3e8be93c-7903-4eb4-85bf-cc582248a9fa.png)

## Why It's Good For The Game

Lots of QoL and structural changes in attempt to make the cool map even
cooler.

## Changelog
:cl: MMMiracles
add: Tramstation has received a substantial overhaul! Please consult
your local tour guide and station maps for changes.
/:cl:

**Changes (as of so far)**
- The Tramstation tunnels have been extended 6 tiles each way, making
that trek across the central rail a little more dangerous.
- No more mid-way safety net on the transit rails. You're either making
it or you're jumping to the bottom floor to avoid the tram.
- The central rail apparently had a negative slowdown, meaning you
actually WERE faster to just run the gauntlet because it literally made
you faster. This has been reverted because I want you to get hit by a
train.
- The side routes are now a bit more dangerous since you can get pushed
off into the lower floor
- Fauna overhaul! Several locations including the transit tunnels have
gotten some greenery to help liven up transit between sectors. Please do
not rip up the AstroTurf it is very expensive in space.
- Handicap-accessible departments! Every major wing and departments with
multiple floors has been given a 2x3 elevator segment for those among
the crew who have been hit by the tram a few too many times. Handicap
inaccessible staircases may or may not come after this (i hate the
handicapped)
- Expanded Security wing! You know that lame hallway between
interrogation and the courtroom access? Now its a whole holding wing fit
with essentials to keep your inmates content while waiting for their due
process (never ever).
- Reworked Bridge! Front row seats to the western tram dock as well as a
furnished meeting room with various corporate memorabilia!
- The HoP's office has been moved to function more as an arrival gate
for late joining crew! Scenic queue lines and an option to block off the
lower dorm access if you really want to enforce the 'Papers, Please'
roleplay you've always wanted out of your HoP experience.
- Combined the teleporter/gateway/eva access into one special external
operations room. All you off-station needs in one convenient place!
- More multi-z integration! Several segments (mainly maintenance level
transfers) have been given overhangs and better methods to move between
levels. This is still being expanded upon as of current PR posting.
- The power/pipe access shafts have been changed to be more
public-facing and now also act as another inbetween for
maintenance-dwelling crew to shift between floors.
- Multi-z solars! Both solar wings have been extensively overhauled to
include multi-z structuring and easily doubled the amount of roundstart
panels on the map.
- Escape pod bay! [Casually borrowing from a certain ship
map](https://tgstation13.org/phpBB/viewtopic.php?t=32834), there is now
a centralized location for all station escape pods on the floor below
Arrivals. Honestly makes more sense thematically instead of having a
bunch of scattered bays.
- MULEBOT integration! Each major department now has delivery drop-off
points along with Cargo getting a minor restructuring to fit 4 MULEBOTs.
Seedy side-tunnels and drop points have been added for departments that
aren't normally accessible from upper maintenance so they can still
properly deliver cargo if sent this way. I can't guarantee this won't
end in MULEBOTs getting ran over by a tram because they're fickle
beasts.
- Complete rework of the disposals/piping/wirenet! I literally ripped
everything up and rebuilt it with (hopefully) better stability in mind.
Disposals is now also set up in that it'll try to avoid going through
departments unnecessarily if your package isn't marked for it.
- Cargo's mail room and trash room has been overhauled to be more easily
accessed for cargo techs and for routing mail.
- The chef has access to the morgue's back door via the front
maintenance hatch while Robotics can now access the same back door via
their maintenance shaft.
- The chem lab's starting area has been expanded so chemists don't have
to worry as much about digging if they don't have large projects.

![2023 02 02-18 15
45](https://user-images.githubusercontent.com/9276171/216472805-77074a12-d653-41c4-b730-f26f93c27d3b.png)
![2023 02 02-18 15
38](https://user-images.githubusercontent.com/9276171/216472852-555e6ca9-e967-4915-9555-e29cfc99393d.png)

---------

Co-authored-by: MMMiracles <lolaccount1@hotmail.com>

---
## [Jolly-66/JollyStation](https://github.com/Jolly-66/JollyStation)@[bc1b269c42...](https://github.com/Jolly-66/JollyStation/commit/bc1b269c4241a350b3d872070606ef036fafd056)
#### Wednesday 2023-03-29 00:32:41 by TaleStationBot

[MIRROR] [MDB IGNORE] Fixes all antag datum moodlets being removed when any single antag datum is removed (#4472)

Original PR: https://github.com/tgstation/tgstation/pull/73305
-----
## About The Pull Request

All antag datums operated under the `antag_moodlet` mood category, which
is clearly an issue when you can (and commonly) have multiple antag
datums of different types on your mob.

New antag datums of different type will now no longer override older
antag datum moodlets, now they will stack. This means traitor
revolutionaries are the most zealous folk on the station.

This has a few potential oversights down the line: 
- Someone adds an antag datum players can have duplicates of, and also
has a moodlet associated
- Re-used moodlets in antag datums that can easily be stacked will be
noticed
- Most solo antags used `focused` right now, but none can stack outside
of admemes

But I don't think it's an issue for now.

## Why It's Good For The Game

Prevents a quick revolution from stripping you of your joy. 

Fixes #67313

## Changelog

:cl: Melbert
fix: Revolutionary Heretics and Cultists Traitors no longer lose all of
their joy in life after being de-converted from their respective causes.
/:cl:

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [Y0SH1M4S73R/tgstation](https://github.com/Y0SH1M4S73R/tgstation)@[7687a28e7c...](https://github.com/Y0SH1M4S73R/tgstation/commit/7687a28e7ceecea6b9e0aacdb58a2271b063f9d3)
#### Wednesday 2023-03-29 00:39:04 by Sol N

refreshes syndi-kits and syndicate surplus crates, introduces shared limited stock (#71869)

## About The Pull Request

After all, the Syndicate loves a good throwback.


![C6O47fPhAB](https://user-images.githubusercontent.com/116288367/207737104-3d24574f-02e0-433d-8ea7-6825ca4cb970.png)

This PR does a few things with the goal of reimplementing and
revitalizing syndicate traitor kits and the syndicate surplus crate.
Of note is that I have added in a way for limited stock items to share
their limited stock.

Following maintainer guidance the syndicate traitor kits have increased
in price and as a result some of the lower value ones have been
adjusted. I've given all active bundles current TC costs per item
knowing full well they will be inaccurate eventually.

<details>
  <summary>Changes as a result of my audit of syndikits</summary>
    
### UNCHANGED
Recon, Spai, Stealthy, Screwed, Sniper, Nukie Meta, Implants
Mad Scientist, Bees

Lord Singuloth is also unchanged and disabled, I think that it should
turn into a new supermatter themed kit maybe. outside of current scope.

### Gun Kit
Replaced emag with doorjack and gave it a chameleon holster, literally
moved 1 tc elsewhere

### Murderer
replaced emag again, no additions its a lot of tc and Just Good

### Hacker
added doorjack, otherwise unchanged

### Sabotage
no changes other than adding in extra bombs it didnt have

### James Bond
gave him some gadgets with the freedom implant, emp flashlight, and one
x4. also a cyanide pill and deck of cards for fun

### Ninja
Added in miner Jump Boots, smoke spell, and doorjack. dont just want it
to be space ninja

### Dark Lord
Added in new lightning bolt spell granter and made the desword default
to red. probably overbudget.

### White Whale
dehydrated carp added so you can ride it alongside the ones you grenade
out. hard to imagine changing this

### Mr Freeze
changed temperature gun to be cryo only so that i could give him the
cryo thermal pistol. cold attacks only.

### 2006 Traitor
doorjack.

</details> 

tl;dr theyre all about 30 tc worth of shit more or less some are more
but thats what rarity should be for
you can only buy from one type of syndicrate per round


![QOF1WO7CC6](https://user-images.githubusercontent.com/116288367/207739417-00ae6b81-b6aa-4774-a4bb-f2d880988ff4.gif)

Next up is the return of the surplus crate. 
Crate is generated, gives you gear **based on your progression at the
time of buying the crate**, you can use it all at the start and get some
chameleon kits and not a lot of dangerous weapons or wait till later.
I've changed the weight on some items here and there and given weight to
role and species locked items, though I will admit that latter is
unimportant because I set moth lanterns to be unable to appear in these
two crates.


![dreamseeker_t8abXysKqK](https://user-images.githubusercontent.com/116288367/206761978-96e2a51e-f9a5-48e4-a863-a9198fa15ea2.gif)

But who cares about that your eyes instantly went to the United Surplus
Crate and the United Surplus Key lets be honest.

The united surplus crate is 80 TC worth of uplink items relative to your
current progression when you purchase it and gives you a locked box. It
**will explode if you try to break it** so be careful with it. It gives
you 80 TC and costs 20 TC because it is impossible to open without key.
The rub of course is that the Syndicate forbids agents from buying more
than one surplus item of any kind, you need to find another traitor and
make them buy you a key to open your box. Or I guess you can share the
box?


![dreamseeker_ts0AZeiyfy](https://user-images.githubusercontent.com/116288367/207740388-3f688bba-5d71-48d2-8079-671bbed7e54e.gif)

Regardless, if the crate is opened with any other means it doesn't spawn
its contents, you need 2 traitor uplinks.
Both of these items have a 30 minute timer because you don't want a
crate that has 5 emp flashlights in it. You at least want one energy
sword.

I did a lot of code shit and changed various things to be proc based to
allow for more editing and interjection of things, as I wrote in code
comments making a crate thats locked to a specific set of progression
just means changing the proc that generates a list of valid uplink items
to check items' progression values to a specified value instead of your
characters progression.

Ok I think that goes over everything more or less????

## Why It's Good For The Game

I've heard that people liked these and I think they are quite fun, being
able to go from "i dunno what to do as a traitor" to "ah, of course, I
will become the Bombler" is a fun thing to be able to have, and people
like to get a bunch of random shit in the mail. Some of it even feels
free!!!!!!!!!!!!!!!!!!! Brain points go up!!!

The division of procs allows for more creativity with this system than
existed before as well as other possibilities for interacting with the
uplink handler in funny ways.

## Changelog

:cl:
add: the syndicate is once again distributing syndi-kits, some now with
new technology
add: a fresh batch of syndicate surplus crates have been sent out,
though they seem a bit lighter than before
add: in an effort to encourage cooperation, a traitor can now purchase
either the new United Surplus Syndicate Crate or its key, but not both
add: lightning bolt book granter for wizard event and one syndie-kit
bundle
add: temperature gun that only makes things colder for one syndie-kit
bundle
code: it is now possible to have uplink items share limited stock
bal: role-restricted items no longer can be delivered by the stray
syndicate drop pod event
/:cl:

---
## [Y0SH1M4S73R/tgstation](https://github.com/Y0SH1M4S73R/tgstation)@[6dd4839ef3...](https://github.com/Y0SH1M4S73R/tgstation/commit/6dd4839ef321aa0a997549d1ae07fe7ccbba59ed)
#### Wednesday 2023-03-29 00:39:04 by carshalash

Gatfruit will no longer drop from ice portals. (#72048)

## About The Pull Request

For some god-forsaken reason, somebody decided that ice portals should
be able to drop one of the most disruptive items in the game. This PR
amends this by removing it from the drop pool.

## Why It's Good For The Game

In 2013 gatfruit was introduced in the following PR #2000 . This was
almost a decade ago at this point, repeatedly through the PR the creator
states his belief that this item should only ever be obtainable through
admin intervention due to its ridiculous capabilities. At the time
everyone in the PR agreed it was a reasonable item to add **as it was
unobtainable without admin intervention**. Over the years, it has crept
its way to become more prevalent and openly obtainable, the most
offensive of these options is the ice moon portal. As is, there is a 1
in 28 chance of obtaining the seeds, this sounds pretty inoffensive
right? That's just 3.44% probability. Now, let us search the instances
of the portal that spawns this.


![image](https://user-images.githubusercontent.com/16896032/208220173-bbefe604-0885-44a5-9add-b5f0c62067cc.png)

That is a big number, a lot of chances to get that seed packet and other
gamer looters. Now, let's take a look at the probability of being able
to get these seeds, assuming you wipe out all of the portals.


![image](https://user-images.githubusercontent.com/16896032/208220460-3f59a2ac-d936-4f3a-aa14-9c637af6a9d7.png)

92.8% chance to be able to get these seeds each shift if you focus
entirely on gaming the portals. That's a pretty insane probability of
being able to obtain the gatfruit seeds.

While I dislike people who sprint to the seed vault, there is at least
the possibility of a pod person telling them to fuck off when they
demand their _free_ gamer seed. There is also the fact that the ruin
isn't a guaranteed spawn every shift.

## Changelog

:cl:
balance: Gatfruit seeds will no longer drop from ice portals.
/:cl:

---
## [Y0SH1M4S73R/tgstation](https://github.com/Y0SH1M4S73R/tgstation)@[00e7d5d746...](https://github.com/Y0SH1M4S73R/tgstation/commit/00e7d5d7465211ccf0e3d604e566e2c08775cd20)
#### Wednesday 2023-03-29 00:39:04 by GoldenAlpharex

*hand, or That /One/ Emote You Always Felt Was Missing (#71600)

## About The Pull Request
It's happened to me _repeatedly_ that I'd see someone down on the floor,
and wanted to just, give them a hand, so they could take it and get up
that way, without just, directly clicking on them, since that's a little
bland. I've also wanted to just, offer my hand to someone so they could
grab it, so that I could pull them alongside me, rather than just
targeting one of their arms and ctrl-clicking them.

I've had this idea for a _long_ time, and only just decided to do this
today.

Now, I know what you might say. "Golden, that's a lot of code for
something this simple!" You're not wrong. _However_. I decided to go
along and to give some more love to the `/datum/status_effect/offering`
status effect and the offering-related alerts, to make them a lot more
versatile and a lot less hardcoded. Hence the whole "refactoring" part
of this.

Of course, when I add something, I don't do it half-way. So, the way the
emote works is much like the `*slap` emote, except that:

- When you click on someone, it does the exact same as if you were
offering the item to them, except that it's targeted (much like
ctrl-shift-click).
- If there's nobody directly adjacent to you, it won't do anything.
- If there's at least one person lying down around you, you will offer
them your help to get up. Should they take your hand and let you help
them up, you will both receive a simple memory about being helped up (or
helping up), as well as a 45-seconds-long small mood buff, because it
feels nice to be on either end of such a friendly gesture. If they get
up, they automatically get disqualified from being offered some help
standing up, and likewise, if you lie down, that offer goes away as
well.
- If there's at least one person around you, you will instead extend
your hand in their direction, for them to grab onto it. Should they do
so, you will then grab them by their arms and pull them.

I reworked the offering status effect to no longer have a hardcoded
`can_hold_items()` check, so that kisses and the hand offering would no
longer need you to have free hands to complete. The logic here is that
you can still pull someone even with both hands filled, so I figured I'd
leave it this way.

Note: If anyone would like to give the item a better sprite, by all
means, go ahead, that'd be amazing. I'm just not really a great spriter
and couldn't be bothered to waste hours making a very _meh_ hand.

## Why It's Good For The Game
It's fluff, and nice fluff at that. It makes it easier for people to be
nice to one-another without having to necessarily spend so long writing
up an emote that the person on the floor will already have gotten back
up. I'm sure the MRP folks will like it, and I'm certain the HRP
downstreams will love it too ;)

## Changelog

:cl:
add: Added the *hand emote, which you can offer to someone standing up
in order to give them the possibility to grab onto your hand and let you
drag them away, or to someone lying down to help them back up, which
always makes everyone involved a little happier!
refactor: De-hardcoded and genericized a lot of the offering status
effect and alert code, to make it require a lot less copy-paste to
handle new cases.
fix: Offering a kiss no longer requires the receiver to have free hands
to accept said kiss!
/:cl:

---
## [UnokiAs/tgstation](https://github.com/UnokiAs/tgstation)@[0631fe5bde...](https://github.com/UnokiAs/tgstation/commit/0631fe5bde73a68b4c12bdfa633c30b2cee442d5)
#### Wednesday 2023-03-29 00:40:00 by Jacquerel

Add Croissants & Traitorous Baking Techniques (#72232)

## About The Pull Request

This is my Christmas present to mimes everywhere.

First of all this adds Croissants, because I thought they already
existed and was shocked to learn that they did not.

![image](https://user-images.githubusercontent.com/7483112/209454610-4e69563f-b83d-465b-b28e-7e0b482ff01b.png)
Here's a croissant and an unbaked croissant.
In terms of food they are GRAIN, DAIRY, and BREAKFAST and made fairly
simply from sugar, dough, and butter.

Secondly it adds this pack of traitor gear, exclusively for Mimes and
Chefs.

![image](https://user-images.githubusercontent.com/7483112/209454613-059759b2-774c-45e2-9e1e-97adb43f75f1.png)
The contents of this pack are:
- One combat baguette, indistinguishable from a regular baguette. If
wielded as a sword it gains a 50% block chance (equal to the Captain's
sabre) and does 20 damage.
- Two throwing croissants, which do 20 throwing damage and return to
your hand like boomerangs.
- A cookbook which teaches you the secret to turning croissaints into
deadly boomerang weapons.

You make a croissant into a throwing croissant simply by inserting an
expertly bent iron rod into it.
The chef can't make any use of the baguette unless they also gain the
ability to mime, but they can use it to make food.


https://user-images.githubusercontent.com/7483112/209454703-feafcf4c-6d0a-4e9a-ac4a-d3e2fc7c0ffb.mp4

Watch me here struggle to use them to kill an ape (they don't return to
your hands if thrown at an adjacent tile).

## Why It's Good For The Game

It's insane that croissants aren't already in the game.
This gives mimes an "invisible" sword to go with their invisible gun (it
announces to everyone nearby when you're about to use it, but they can't
know if it's just a _regular_ baguette).
It's funny to throw bread at people.

## Changelog

:cl:
add: You can now bake croissants to add to your breakfast.
add: Traitorous chefs can bake dangerous throwing croissants, Mimes can
do this and gain the additional benefit of a deadly combat baguette.
/:cl:

---
## [Donpedrito/tgstation](https://github.com/Donpedrito/tgstation)@[cba002fa91...](https://github.com/Donpedrito/tgstation/commit/cba002fa912f07112fbbedcab330a35e2bffeab7)
#### Wednesday 2023-03-29 00:40:47 by Sol N

converts contraband file into poster file, makes holiday posters work (kind of) (#72131)

## About The Pull Request

The first part of this is just something that bothered me when I was
messing around with something that I will PR in the new year,
contraband.dm and dmi is ONLY posters. There's nothing else in there and
there are plenty of official posters, and if with #71717 we will also
add holiday posters to the mix then I think that its time to retire
contraband and make it poster.

Some small things I did while messing with it was change some variables
that were single letters into actual variable names, but overall this
part of the pr is not a player facing change.

That said, speaking of #71717 I think that it didn't work? Or didn't
work the way that it was supposed to? All of the spawned posters aren't
instances of festive posters, they are instances of normal posters, so
the code on initialize was not doing anything and the only reason the
holiday_none poster was showing up was because of the proc in randomize
spawning the posters in as those other posters. Because it didn't
actually _become_ poster/official/festive it never could do the proc
that turns it into a poster for the holiday that is actually occurring.

But then when I made it work and it turned into the generic posters I
decided that it would be better if instead of 30% of all posters being a
half finished mess, that if there wasn't a holiday poster it just
wouldn't replace them at all. I have poster Ideas and Dreams so I will
try to help with adding to more holiday posters but not in this PR.

What IS in this PR though, is a new traitor poster that appears during
the holidays.

![dreamseeker_MxxBzXIxiy](https://user-images.githubusercontent.com/116288367/208793262-9d4a45dc-f7bb-4208-b3c3-78cb68cf9af5.png)

This is a generic evil holiday poster that will replace normal evil
posters in the evil poster objective, because I agree with #72003 that
it should be a feature.

## Why It's Good For The Game

Contraband file is just posters already, this is easier for people to
find the posters.
I like holiday posters and think that we should have them and add more,
it is a fun easy thing to add to a lot of the microholidays to make them
more visible in addition to the name generation, but I don't want to see
the unfinished holiday poster so I do think that it's better to only
have them spawn if the holiday actually has a poster. Looking forward to
febuary!

## Changelog

:cl:
add: during holidays the spread syndicate propaganda through posters
objective has a chance of spawning evil holiday poster
fix: framework for holiday posters is more functional and modular
code: contraband.dm file and contraband.dmi file are both now poster.dm
and poster.dmi
/:cl:

---
## [Bawhoppen/-tg-station](https://github.com/Bawhoppen/-tg-station)@[63561ca455...](https://github.com/Bawhoppen/-tg-station/commit/63561ca455933a38f3390f7fcfa6266fda3c53b3)
#### Wednesday 2023-03-29 00:41:31 by san7890

Guards against uplink failsafe code being the same as unlock code (#72113)

## About The Pull Request

There's probably a better way to do this to be honest, but I think it's
silly for both to potentially be the same and this should work alright.
## Why It's Good For The Game

Fixes #71446.

I don't think the Syndicate is that stupid.
## Changelog
:cl:
fix: After a recent mishap with a high-ranking Syndicate operative, the
uplink's unlock code and failsafe code (the one that makes it blow up if
you say it) should never turn out to be the same.
/:cl:

---
## [mc-oofert/tgstation](https://github.com/mc-oofert/tgstation)@[bf73344399...](https://github.com/mc-oofert/tgstation/commit/bf73344399f4b372c13d367cbbd8a40bec23916b)
#### Wednesday 2023-03-29 00:42:19 by Time-Green

[READY] DRAMATIC SHUTTLES!! You can now fly around the shuttle (#71906)

You can move around shuttles during transport now! Instead of them
teleporting you instantly into deepspace, you can move around somewhat
depending on your space-mobility and grip-strength.


![image](https://user-images.githubusercontent.com/7501474/206866132-3fae024c-a8a2-4f4a-b4b8-37c96a254498.png)

**Please watch the demonstration aswell, it should answer most
questions:**
https://www.youtube.com/watch?v=Os77qDOVSXE

Interactions:
- Being within armsreach of a wall or solid object means you 'cling',
where the shuttle pull is very weak and you can basically run around the
shutt;e (but dont fuck up or you're gone)
- Being in range of nothing gives you a very heavy pull, you can barely
resist if you have a decent jetpack
- Objects are instantly power-yeeted
- Being pulled or riding something excempts you from hyperspace pull
- Touching a space tile while being on hyperspace dumps you in
deepspace, you either go back to the shuttle or enjoy deepspace
- On shuttle hyperspace tiles are a lot less dangerous, and will instead
launch and freeze you instead of teleporting you into deepspace
- In-case it wasn't obvious, you can rest outside the shuttle as long as
something is blocking your path. I think it's funny but I might nerf it

:cl:
add: You can now fly around the shuttle during transit! Woohoo! You can
either cling to the side or grab a jetpack and try and keep up with the
shuttle! Carps can move around freely in hyperspace
qol: Increased shuttle hyperspace size from 8 tiles to 16
/:cl:

- [x] Find a way to detect when a shuttle arrives and do something with
the shit left in hyperspace

Things I will do in another PR: 
- Engines spit fire and hurt (almost finished but I want to keep this
small)
- Random shuttle events. You might run into dust meteors or migrating
carps OR A CHANGELING INFILTRATOR
- Hyperspace turfs on the shuttle pull you under the shuttle

### Why it's good for the game
It's so much more immersive than being instantly teleported into
deepspace. It gives you a chance to recover if you get spaced or for
daredevils to look cool

It's also just very cool idk

---
## [mc-oofert/tgstation](https://github.com/mc-oofert/tgstation)@[97db4ecca4...](https://github.com/mc-oofert/tgstation/commit/97db4ecca46ddac5b10f6bd7b2088fc2bd1f5aea)
#### Wednesday 2023-03-29 00:42:19 by Jeremiah

Adds the Cursed quirk  (#72317)

## About The Pull Request
Adds a silly negative quirk inspired by fallout's bloody mess.

Bad luck interactions for
- Microwaving
- Cigarette coupons
- Russian roulette
- Vending machines
- Ledges
- Slipping

All of which have a chance to kill you, which, by the way, causes you to
**delimb and explode**.

This changes the admin smite as well since it's all the omen component.
Giving permanent omens will mean the player will gib on death, which is
super probable given the insane base damage from bonking your head.
Permanent omen smites are basically dooming someone to die of natural
causes.

<details>
<summary>GIFs</summary>


![dreamseeker_ZE6hyRdYet](https://user-images.githubusercontent.com/42397676/209779120-f7d76862-91e2-4366-a49d-e93366d96faf.gif)

updated: Death no longer fully gibs (carbons)

![dreamseeker_8S8r6B6gMM](https://user-images.githubusercontent.com/42397676/209874302-2e24f581-ffda-42e7-9794-dbe0fff2ff5b.gif)

Panic at seeing bad omen coupons

![dreamseeker_tykHbePTSS](https://user-images.githubusercontent.com/42397676/209887936-5d7f5edf-6fa2-41c7-8503-37432b49c7c0.gif)


![3](https://user-images.githubusercontent.com/42397676/209885388-90523f2c-531a-4928-96b2-c902552cbbbc.png)
</details>

## Why It's Good For The Game
Adds a bit of physical comedy and difficulty for players that want it.
## Changelog
:cl:
add: Hope you saved for a rainy day: Added the 'Cursed' quirk which
causes excessive slippage and... other difficulties.
/:cl:

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>
Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>
Co-authored-by: Timberpoes <silent_insomnia_pp@hotmail.co.uk>
Co-authored-by: Watermelon914 <37270891+Watermelon914@users.noreply.github.com>

---
## [mc-oofert/tgstation](https://github.com/mc-oofert/tgstation)@[acb96fee1d...](https://github.com/mc-oofert/tgstation/commit/acb96fee1d0f6605992280d751a7b9930e3a7211)
#### Wednesday 2023-03-29 00:42:19 by MrMelbert

Refactors memories to be less painful to add and apply, moves memory detail / text to memory subtypes. Adds some new memories to demonstrate.  (#72110)

## About The Pull Request

So, a huge issue with memories and - what I personally believe is the
reason why not many have been added since their inception is - they're
very annoying to add!

Normally, adding subtypes of stuff like traumas or hallucinations are as
easy as doing just that, adding a subtype.

But memories used this factory argument passing method combined with
holding all their strings in a JSON file which made it just frustrating
to add, debug, or just mess with.

It also made it much harder to organize new memories keep it clean for
stuff like downstreams.

So I refactored it. Memories are now handled on a subtype by subtype
basis, instead of all memories being a `/datum/memory`.

Any variety of arguments can be passed into memories like addcomponent
(KWARGS) so each subtype can have their own `new` parameters.

This makes it much much easier to add a new memory. All you need to do
is make your subtype and add it somewhere. Don't need to mess with jsons
or defines or anything.

To demonstrate this, I added a few memories. Some existing memories had
their story values tweak to compensate.

## Why It's Good For The Game

Makes it way simpler to add new memories. Maybe we'll get some more fun
ones now?

## Changelog

:cl: Melbert
add: Roundstart captains will now memorize the code to the spare ID
safe.
add: Traitors will now memorize the location and code to their uplink.
add: Heads of staff winning a revolution will now get a memory of their
success.
add: Heads of staff and head revolutionaries who lose their respective
sides of the revolution also get a memory of their failure.
add: Completing a ritual of knowledge as a heretic grants you a quality
memory.
add: Successfully defusing a bomb now grants you a cool memory. Failing
it will also grant you a memory, though you will likely not be alive to
see it.
add: Planting bombs now increase their memory quality depending on how
cool the bomb is.
refactor: Memories have been refactored to be much easier to add.
/:cl:

---
## [nik707/Citadel-Station-13-RP](https://github.com/nik707/Citadel-Station-13-RP)@[24aca0ae55...](https://github.com/nik707/Citadel-Station-13-RP/commit/24aca0ae55ce2204474ec23fed6d23cb46b6645e)
#### Wednesday 2023-03-29 00:42:36 by LordPapalus

Cargonia, but with less weapons (#4370)

* Cargonia is no more

Fuck you

* PLEASE

* Zandario, I will suck your PP

---
## [Moose1002/tgstation](https://github.com/Moose1002/tgstation)@[5250b1fcc6...](https://github.com/Moose1002/tgstation/commit/5250b1fcc6aca1aa6d6b0f9ec81ce6ad5fe2fa03)
#### Wednesday 2023-03-29 00:42:52 by san7890

Captain's Spare ID Safe Can Only Hold ID Cards (#72584)

## About The Pull Request

I've personally seen this strategy play out the exact same way on more
than one occasion in an higher frequency lately (I've never played as
either side, just witnessed it)- and it always just seems to be an abuse
of a skewed in-game mechanic. So, this PR makes it so that you can only
put IDs into the spare ID safe. Nothing else.
## Why It's Good For The Game

I think this balance change is needed because it really sort of ruins
what I like about nuclear operatives, having to run around and stay
fluid for whatever the nuclear operatives could have, not "HAHA WE WILL
PUT IT IN OUR (NEARLY) IMPENETRABLE SAFE THAT THEY WILL NEED TO USE A C4
DIRECTLY ON AND JUST END UP PLAYING BLOONS TOWER DEFENSE SIX AS WE AWAIT
THOSE RED FUCKS TO ARRIVE". I miss when it would be fun to inject it
into a monkey who could crawl around vents, put it in a disposals loop
around the station to keep the nukies on a wild goose chase, or just
holding your ground in the brig and retreating if they batter you down.
It's just a very OP location in a very OP place with lots of warranted
OP armor for it's intended use case, which is not really being followed
by putting the all-important disk in the safe.

It's just very strong overall due to how protected-from-damage the spare
ID safe is, and I don't really like the fact that this is emerging as a
new "meta gameplay" (even used when there aren't any nuclear
operatives), it just sullies the different variety of ways you can
defend yourself against nuclear operatives when there appears to be
**the clear choice**. I don't like that concept where you can have a
strategy so good that you _shouldn't_ do it.

Also, it's an _ID Safe_. Not a disk safe.
## Changelog
:cl:
balance: Due to materials costing a lot more than ever, Nanotrasen's
Spare ID Safe Supplier have cut down on the space inside of the ID Safe,
meaning you can only cram in things as thin as an ID Card.
/:cl:

---
## [Thunder12345/tgstation](https://github.com/Thunder12345/tgstation)@[645054b489...](https://github.com/Thunder12345/tgstation/commit/645054b489212a34d80e6e1a7fa1320e35d9bfc7)
#### Wednesday 2023-03-29 00:43:45 by MrMelbert

Fixes encoding on syndicate declaration of war, Fixes a way to send unencoded text to newscasters (#73366)

## About The Pull Request

Ugly


![image](https://user-images.githubusercontent.com/51863163/218280311-f282bd75-2f6e-4290-b3f4-d9d856ff36d3.png)

Nice


![image](https://user-images.githubusercontent.com/51863163/218280315-233da635-f777-4006-8778-c673b83e887e.png)

War dec: 

- TGUI inputs for syndicate declaration of war no longer double-encode
sending customized messages into the announcement
- The alert box for the war declaration no longer has multiple errors
(an extra bracket, negative seconds)
- Reduces some copy and paste in the war declaration device
- Adds a debug item that's a war declaration device but it only does the
sound and message. Please don't fake war decs admins it's a horrible
idea

Additionally

- Documented `priority_announcement`
- Ensures all uses of text and title in the priority announcement
message are encoded (Some were not!)

## Why It's Good For The Game

Encoding looks bad, unencoded text is also bad

## Changelog

:cl: Melbert
fix: Syndicate declarations of war no longer murder apostrophes and
their friends
fix: The alert box for the declaration of war no longer looks funky, and
counts forwards in time rather than backwards
fix: Fixed being able to send unencoded HTML to newscasters
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [Tsunamico/Tsunamico-cmss13](https://github.com/Tsunamico/Tsunamico-cmss13)@[030a68f6ac...](https://github.com/Tsunamico/Tsunamico-cmss13/commit/030a68f6ac59efa5b7c02f1f9a421b3bd95fd0b3)
#### Wednesday 2023-03-29 00:47:42 by carlarctg

Reverts Tail Jab and speed changes on Vampire (#2909)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

Vampire's Tail Jab now needs you to directly click the target like a
tail stab, like it used to be.

# Explain why it's good for the game

> Vampire's Tail Jab now needs you to directly click the target like a
tail stab, like it used to be.

I regret making this change, it ended up just making it far too easy to
just hit and run from a safe distance and be annoying without any effort
in the hands of the Vampire. Not only that, but a lot of people disliked
it so since in the end nobody liked this change and I think it actively
worsened Vampire and its place in the game I've decided to revert this.
Not to mention it has to use the dumb LRP telegraphs, which tail stab
doesn't.

> Increased Vampire speed back to its default.

Lowering the speed buff by a tier made Vampire go from pretty fast to
ridiculously slow. I've had people compare it to Ravager in terms of
slowness, and while it's not accurate, it's not too far off. It makes it
very difficult to actually be, well a flanking caste, even if it's a
sideliner instead of a backliner, as it makes it very very hard to run
from marines with your natural slowness off-weeds. I don't know why the
fuck reducing this by one tier made vampire super slow but that's
shitcode for you. With it being faster Vampires can be more confident in
their harassment tactics instead of needing to hide behind walls like a
corner-lunging Warrior because their speed made them easily kiteable.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->


# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Be sure to properly mark your PRs to prevent unnecessary
GBP loss. Maintainers freely reserve the right to remove and add tags
should they deem it appropriate. -->

:cl:
balance: Vampire's Tail Jab now needs you to directly click the target
like a tail stab, like it used to be.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [Tsunamico/Tsunamico-cmss13](https://github.com/Tsunamico/Tsunamico-cmss13)@[0bc21524a1...](https://github.com/Tsunamico/Tsunamico-cmss13/commit/0bc21524a123944a37d45e1088dca13476824b9c)
#### Wednesday 2023-03-29 00:47:42 by carlarctg

Firearms skills rework (#2766)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

Reworks the firearms skill.

unskilled is now 'SKILL_FIREARMS_CIVILIAN'
default is now 'SKILL_FIREARMS_TRAINED'
trained is now 'SKILL_FIREARMS_EXPERT'

- Civilian skill will allow you to use pistols, SMGs, and certain
weapons that have their civilian override variable set to TRUE, such as
bolt-action rifles, the ABR-40, the HG-37, or the double barrel
shotguns.
- Trained skill is the same as always.
- Same with expert skill. The renames are for readability.

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

Civilian gun usability is horribly updated. It shouldn't slow your
firerate as that makes no sense and makes guns feel terrible to use, and
it shouldn't be applied in such a way that it makes pistols and SMGs
unusable and the best option running around with a one handed shotgun.

Pistols and SMGs are reasonably newbie-friendly guns for civvies to know
how to use, and the civilian shotguns are, well, built for them.

This paves the way for survivors to not be on the same level as marines.
If this is an approved idea I can include it here.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->


# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Be sure to properly mark your PRs to prevent unnecessary
GBP loss. Maintainers freely reserve the right to remove and add tags
should they deem it appropriate. -->

:cl:
balance: Reworks the firearms skill. Civilians can now fire pistols,
SMGs, and certain other civilian weapons without penalties. Civilian gun
penalties have had their firerate reduction remove and scatter
increased.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [SeigaSeiga/tgstation-local](https://github.com/SeigaSeiga/tgstation-local)@[84a85c827d...](https://github.com/SeigaSeiga/tgstation-local/commit/84a85c827d71b3326b482444a204711de38cf518)
#### Wednesday 2023-03-29 00:47:55 by lizardqueenlexi

Removed TRAIT_PLASMABURNT, fixed plasma river limb transformation. (#71157)

## About The Pull Request

Resolves #67282.

As originally designed, plasma rivers (namely, those on Icebox, though
the turf was originally made for the Snowdin away mission) are meant to
literally strip the flesh from your bones, leaving you with plasmaman
limbs. I'm not certain when this broke entirely, although it seems to
have never been updated to work alongside Kapulimbs.

Transformation of limbs into plasmaman limbs used to be accomplished by
adding the "PLASMABURNT" trait to limbs. However, this trait in the
current code is entirely meaningless, only checked in the proc that
makes plasmamen catch fire. Essentially, the only "interaction" is
having your flesh melted off by a plasma river, donating that specific
limb to a plasmaman, and pranking them with the fact that that specific
limb will still make them burst into flames.

Exciting.

I've removed the trait entirely, as it does functionally nothing, and
restored the ability of plasma rivers to turn your limbs - and
eventually, you - into plasmaman equivalents.

To be honest, I'm not _entirely_ satisfied with the plasmaman
transformation process - it doesn't especially suit the lore of
plasmamen, and if you transform into one in the plasma rivers you'll
probably immediately die from Icemoon's atmosphere anyway. However, this
is something I'd prefer to revisit in a later PR.
## Why It's Good For The Game

There's little reason _not_ to remove a trait that does nothing.

As for plasmafication, it's a fun interaction that was already _meant_
to be there. The message about your flesh melting off has always
printed, even while it's doing exactly nothing to you. It's cool to fall
into the deadly plasma river and come away from it permanently scarred
with a weird skeleton limb. Turning into a plasmaman entirely is
unlikely to happen and will probably just kill you, but it's a fun and
weird way to be dead.
## Changelog
:cl:
del: Removed the useless "plasmaburnt" trait.
fix: Restored a broken interaction with plasma rivers that slowly
transforms you into a plasmaman.
/:cl:

---
## [itseasytosee/tgstation](https://github.com/itseasytosee/tgstation)@[ae08395328...](https://github.com/itseasytosee/tgstation/commit/ae08395328672ee40c5abb7f2bd1452bb932d6d4)
#### Wednesday 2023-03-29 00:48:16 by san7890

Syndicate Bomb Core Payloads Can Only Be Triggered via the Bomb (#72986)

## About The Pull Request

Basically, you can't extract the bomb core, slap a 10-second c4 on it/on
the shell/and run off having triggered an incredibly powerful explosion.
This is accomplished by having the syndicate bomb override ex_act (it
will be deleted if the explosion goes off), as well as the payload
itself being subtyped into something resistant to bombs and burning.

In-universe, this is described as the shell being quite resistant to
forms of external explosive force- but if any explosive force comes from
within the bomb's shell: kabloom. The bombcore itself has been
redesigned (in a rare moment of non-ineptude) by Donk Co., who has
redesigned the bomb core payload from the ground up- meaning that it can
only be detonated electronically by an impulse from the bomb machinery.
Cutting the wrong wire and attempting to get rid of the bomb by hitting
it with an axe or something will still cause it to blow up, but you know
how those things can be.
## Why It's Good For The Game

I feel like the point of the syndicate bomb is to be a threat for the
crew to match up against. I want a clown in bomb squad gear to head out
to the site and sweat trying to figure out which wire it is, until....
KA-BLHONK: red mist. Or, I want some "helpful" assistant to interrupt
someone's session by going "I KNOW WHAT WIRE IT IS", and having those
odds of either blowing everyone around them up or actually saving the
day.

Being able to detonate something that was balanced and designed to have
_at least_ one minute and a half in **10 SECONDS** is just so injurious
to the game. You can buy a shitload of these bombs, extract the cores,
slap c4 on it and go around the station doling out some serious
explosions. You can run into medbay, wrench it down, slap a c4 on it AND
NO ONE CAN DO ANYTHING ABOUT IT! They can't cut wires, they can't figure
it out to save the day, all they can do is run. Running from danger is
fine and acceptable, but it's just completely stacked against the crew
in a way that I feel needs to be rectified somehow.

I like the idea of purposefully fucking with the wires on the spot so
you sacrificially kill everyone, that feels quite fair to me. I just
simply don't like the fact that you can waltz around the station
punching huge gaps in the hull (remember, putting c4 on the bomb core
itself would cause it to go kabloom) with nearly nothing as far as risk.
It's way too rewarding for something very easy to accomplish (there's a
reason why it's 90 seconds- it's not meant to be easy to accomplish).

This doesn't affect base bombcore behavior, just the explodey ones that
come standard in syndicate bombs.
## Changelog
:cl:
balance: After an unfortunate event occuring when some nuclear
operatives took the ship to a Fireworks Store, the Syndicate have
re-engineered their bomb cores to only explode when electronically
triggered by the bomb shell itself. The payload inside a standard
syndicate bomb can not be exploded with another explosion, you must keep
it in the bomb machinery for it to actually do some explodey stuff.
/:cl:

---
## [IFuckedUpMerging/tgstation](https://github.com/IFuckedUpMerging/tgstation)@[1409e4b026...](https://github.com/IFuckedUpMerging/tgstation/commit/1409e4b026f359764ca491fd5f73f646227973e6)
#### Wednesday 2023-03-29 00:48:30 by LemonInTheDark

JPS Optimization (Light Botcode) (#70623)



## About The Pull Request

Alright. So.
Right now, JPS works like this:
```
code requests path
we enter the actual pathfinding
pathfinding sleeps when it overruns a tick
if it sleeps, it'll then wake up before the mc starts
continue
```
This has annoying side effects. Primarily that we have no real control
over JPS, we just sorta have to eat its cost.
So if there's like 10 different things pathfinding at once, the mc will
have no time to do anything. Hell we might even end up eating into
maptick's time if the jps work is expensive enough (note the cost of
sleeping is not accounted for, and that has overhead)
This has happen before, usually when someone makes a lot of bots, and
it's really annoying.

So then, lets put JPS on a subsystem. That way the MC has control over
it.
But wait, existing code expects to yield and get back a path list, and
that's a sane request.
This is solvable, but requires abusing pass by reference lists, and the
ability to make callbacks into partials (preinsert arguments into them
before they're called, and accept other args later)

Because of this, we can now pass callbacks into pathfinders, allowing
for async use, rather then JUST yielding.

Of note: I've removed the 10 pathfinding datums limit, since
ratelimiting like that is handled nicely by the MC.
I've also removed the 15 second timeout, since mc yielding would trigger
it too often. I'm unsure if this means we don't have exit conditions for
pathfinding, need to talk to ryll. (@Ryll-Ryll what happens if jps just
like, fails to find a path?)

Also of note: I think bots will fire off more then one pathfinding
attempt at a time if their first takes too long to complete. This is
dumb, why do we do this?

Optimizes JPS by more then 40% by removing redundant for(thing in turf)
loops, and avoiding making proc calls if objects are non dense.
This makes things slightly more fragile, but saves a LOT of time. I
think it's worth it, tho talking to mso it might be possible to do
better. Maybe I should do a LINDA system style thing. (I did a linda
system style thing I fixed it)

Optimizes botscanning, fixes bots not seeing things adjacent to them
The list of types could be a cached typecache
We could inline both checkscan and check_bot
check_bot SHOULD NOT BE CALLED ON EVERY OBJECT IN VIEW HOLY SHIT WHY
We don't need to process adjacent and the shuffled view separately, it's
in fact easier to process them in one block
Renames a var

Moves bot's pathing images to above most floor objects, so they're
visible in maint

## Why It's Good For The Game

Speed. Also manuel will stop killing their server by placing 20000
medibots (fucking icebox man every time)

## Changelog


:cl:
fix: Bots will now "notice" you if you're standing right next to them
fix: Bot paths will now draw above things like pipes, rather then below
them
refactor: Changed how pathfinding paths get generated
refactor: Made pathfinding and bot searching significantly faster
/:cl:


Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [Tristrian/tgstation](https://github.com/Tristrian/tgstation)@[8eb9d376b5...](https://github.com/Tristrian/tgstation/commit/8eb9d376b50ed6eab29c4c884d7bc3c53aa33fec)
#### Wednesday 2023-03-29 00:50:58 by san7890

Improves/Abstracts Suicide A Bit More (#72949)

## About The Pull Request

Basically all of the heavy lifting was done in #72919, but we do a few
key things here that I wasn't able to do then because it was just
fucking massive.

Player Facing Changes:
* hear_blind arg is now a default state and must be specifically
overridden. Pretty much every mob that wasn't a pAI or alien was lacking
this, so let's toss it in as a default now. Let me know if the generic
message I put in for /mob/living sucks and we can go from there.

Code Side Changes:
* suicide.dm now only contains code pertinent to the suicide verb, and
all subtype proc-overrides have been moved to an appropriate file
pertinent to that subtype.
* suicide.dm has also been organized a bit more to aid the previous
change.
* There is only one suicide verb now, implemented on /mob/living. All
the verb does is invoke the handle_suicide() proc, which does all of the
lifting.
* Leaning into *mumble mumble* object-oriented philosophy, the message
we send to the world on suicide is handled on subtype procs, rather than
be in the huge fuck-off message tree I implemented in the earlier PR. It
definitely makes the visible_message() proc not hard to read IMO. This
also means that we can take up a less footprint when we re-use certain
suicide messages (i.e. Silicon), which is nifty too.

i'm probably forgetting something but that's all of the big ones
## Why It's Good For The Game

There is now a very, very common framework for how suicide works across
all living mobs, and it's much easier to override how suicide is
handled. Certain subtypes do their own bullshit thing, but it's quite
easy to account for this on that case-by-case basis. The overall code
takes up a much less footprint that just makes it look nicer.
## Changelog
:cl:
qol: Some mob suicides now have a message that shows to blind people or
people that didn't actually witness the suicide, pretty cool.
/:cl:

---
## [elangrr/mainnet](https://github.com/elangrr/mainnet)@[ab863384ee...](https://github.com/elangrr/mainnet/commit/ab863384eeabb194d626cd1c15b42bf255d28eef)
#### Wednesday 2023-03-29 00:52:06 by Indonode

Indonode#5255

Professional and Experienced Validator in Cosmos Ecosystem
High Security , High Uptime

Providing the best services for Stakers and Community
Helping new project to success with love and knowledge.

Our services :
✅ Node Installation Guide (with Cosmovisor)
✅ Genesis
✅ Addrbook (Every Hour updated)
✅ Live Peers
✅ Public Endpoints
✅ Statesync
✅ Snapshot ( Updated everyday at 12 Midnight)
✅ CLI Cheatsheets Command
✅ Explorer

Find more at : https://indonode.net/

---
## [Vexylius/Skyrat-tg](https://github.com/Vexylius/Skyrat-tg)@[a9c430a5e4...](https://github.com/Vexylius/Skyrat-tg/commit/a9c430a5e43a638d3b56f57b663104e1e6a57364)
#### Wednesday 2023-03-29 00:54:03 by SkyratBot

[MIRROR] Basic Mobs Now Actually Have A Deathgasp [MDB IGNORE] (#19002)

Basic Mobs Now Actually Have A Deathgasp (#72950)

## About The Pull Request

Pretty obviously an oversight since we only checked for simple_animal
for this, but should also factor in the fact that we could now be a
basic mob.

Actually I tested it on Sybil just now and deathgasps just never worked.
We were setting death_message for... I guess when they die? It's just
fucked but it works on my local now. blurgh
## Why It's Good For The Game

Ported simple animals that are now basic mobs were able to deathgasp
this time last year. Silly that they aren't able to do that now.
## Changelog
:cl:
fix: Basic Mobs are now able to deathgasp.
/:cl:

Let me know if the new variable name for the string is cringe, I just
settled on that since it mirrored the type of check we run in
select_message_type().

Co-authored-by: san7890 <the@san7890.com>

---
## [Erol509/tgstation](https://github.com/Erol509/tgstation)@[e9c87c0acb...](https://github.com/Erol509/tgstation/commit/e9c87c0acb15439c8f577bba35c45f51bf03d1aa)
#### Wednesday 2023-03-29 00:54:06 by LemonInTheDark

Starlight Polish (Space is blue!) (#72886)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

Adds support to underlays to realize_overlays
Ensures decals properly handle plane offsets
Fixes space lighting double applying if it's changeturf'd into. this
will be important later
Makes solar vis_contents block emissives as expected
Moves transit tube overlays to update_overlays, adds emissive blockers
to them

#### Adds render steps

An expansion on render_target based emissive blockers. 
They allow us to hijack an object's appearance and draw it somewhere
else, or even modify it, THEN draw it somewhere else.
They chain quite nicely

Fixes shuttles deleting z holder objects

#### Makes space emissive, makes walls and floors block emissives
The core idea here goes like this:
We make space glow, and give its overlays some color

This way, the tile and space parallax remain fullbright, along with
anything that doesn't block emissives, but anything that does block
emissives will instead get shaded the color of starlight

This requires a bit of extra work, see later

This is done automatically with render relays, which now support
specifiying layer and color (Need to make an editor for these one of
these days)

The emissive blocking floor stuff requires making a second render plate
to prevent double scaling

Also adds some new layering defines for lighting, and ensures all turf
lights have a layer. We'll get to this soon

#### Makes things in space blue

We color them the same as starlight, by taking advantage of space being
emissive
This means that things in space that block emissive will block it
correctly and be colored blue by the light overlay, but space itself
will remain fullbright

This does require redefining what always_lit means, but nothing but
cordons use that so it's fineee


#### Makes glass above space glow, and some other stuff

Glass tiles that sit above space will now shine light with matching
color to the glasses color. This includes mat tiles.

Glass tiles (not mat because they have no alpha) also only partially
block emissives.
Adds a new proc that uses render steps to acomplish this, essentially
we're cutting out bits below X alpha and drawing what remains as an
emissive.

#### Modifies partial space showing to support glow

Essentially, alongside displaying space as an underlay, we also display
a light overlay colored like starlight.
That starlight overlay gets masked to only be visible in bits that do
not contain any alpha.

We also mask the turf lighting to not go into bits that have no alpha,
to ensure we get the effect we want.
This is done with that lighting layer thing I mentioned earlier.

#### Makes appearance realization's list output ordered

I want it output in order of overlay, sub overlay suboverlay, next
overlay
Need to use insert for that

## Why It's Good For The Game

Pretty!
Also having space be emissive is a very very good way to test for fucked
emissive blockers (If it's broken why are we even drawing the overlay)
I know for a fact mob blockers on lizards and socks are kinda yorked, I
think there's more

<details>
<summary>
Old
</summary>


![image](https://user-images.githubusercontent.com/58055496/213916157-d4b38aa7-3ab6-42a4-989f-7bfba2dc2cba.png)

![image](https://user-images.githubusercontent.com/58055496/213916077-637fa288-bbee-477d-aded-730d9683477e.png)

![image](https://user-images.githubusercontent.com/58055496/213916088-0657a8a2-5627-48e2-8c4b-870c90ef2072.png)

</details>


<details>
<summary>
New
</summary>


![image](https://user-images.githubusercontent.com/58055496/213916107-2af74e64-1817-4a44-b528-180a9160cb9e.png)

![image](https://user-images.githubusercontent.com/58055496/213916115-5fa36fcc-b988-4ccf-850e-21c26ed463d0.png)

![image](https://user-images.githubusercontent.com/58055496/213916120-6833187d-b12e-42a7-ac4b-63c56deb71e5.png)

</details>

## Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. You can read up on GBP
and it's effects on PRs in the tgstation guides for contributors. Please
note that maintainers freely reserve the right to remove and add tags
should they deem it appropriate. You can attempt to finagle the system
all you want, but it's best to shoot for clear communication right off
the bat. -->

:cl:
add: Space now makes things in it starlight faintly blue
fix: Glass floors that display space now properly let space shine
through them, rather then hiding it in the dark
add: Glass floors above space now glow faintly depending on their glass
type
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>

---
## [Erol509/tgstation](https://github.com/Erol509/tgstation)@[51f02b5acc...](https://github.com/Erol509/tgstation/commit/51f02b5acc0ee3d042734b8fd4fd2b58ac41f9ab)
#### Wednesday 2023-03-29 00:54:06 by LemonInTheDark

Fixes critical plane masters improperly not being readded in show_to (#72604)

## About The Pull Request

[Adds support for pulling z offset context from an atom's
plane](https://github.com/tgstation/tgstation/commit/9f215c5316e5cfdbedf6a23ff97dfee0e523354b)

This is needed to fix paper bins, since the object we plane set there
isn't actually on a z level.
Useful elsewhere too!

[Fixes compiler errors that came from asserting that plane spokesmen had
a plane
var](https://github.com/tgstation/tgstation/commit/b830002443f2fbe230e9ff00236d7a46a9f2eec7)

[Ensures lighting backdrops ALWAYS exist for each lighting
plane.](https://github.com/tgstation/tgstation/commit/0e931169f7c5336333bc6f41353c82f603fc1170)

They can't float becuase we can see more then one plane at once yaknow?

[Fixes parallax going to shit if a mob moved zs without having a
client](https://github.com/tgstation/tgstation/commit/244b2b25baecfc644505a3ea1e348e0cb97a04e0)

Issue lies with how is_outside_bounds just blocked any plane readding
It's possible for a client to not be connected during z moves, so we
need to account for them rejoining in show_to, instead of just blocking
any of our edge cases.

Fixing this involved having parallax override blocks for show_plane and
anything with the right critical flags ensuring mobs have JUST the right
PMs and relays.
It's duped logic but I'm unsure of how else to handle it and frankly
this stuff is just kinda depressing.
Might refactor later

[show_to can be called twice successfully with no hide_from
call.](https://github.com/tgstation/tgstation/commit/092581a5c06f7f884f48d41c96fa9300327ef214)

Ensures no runtimes off the registers from this

## Why It's Good For The Game

Fixes #72543
Fixes lighting looking batshit on multiz. None reported this I cry into
the night.

## Changelog
:cl:
fix: Fixes parallax showing up ABOVE the game if you moved z levels
while disconnected
/:cl:

---------

Co-authored-by: Time-Green <timkoster1@hotmail.com>

---
## [Tristrian/Skyrat-tg](https://github.com/Tristrian/Skyrat-tg)@[460ab7adf5...](https://github.com/Tristrian/Skyrat-tg/commit/460ab7adf560856148d46233e3cde565d05354a4)
#### Wednesday 2023-03-29 00:55:43 by SkyratBot

[MIRROR] JPS Optimization (Light Botcode) [MDB IGNORE] (#17669)

* JPS Optimization (Light Botcode) (#70623)

## About The Pull Request

Alright. So.
Right now, JPS works like this:
```
code requests path
we enter the actual pathfinding
pathfinding sleeps when it overruns a tick
if it sleeps, it'll then wake up before the mc starts
continue
```
This has annoying side effects. Primarily that we have no real control
over JPS, we just sorta have to eat its cost.
So if there's like 10 different things pathfinding at once, the mc will
have no time to do anything. Hell we might even end up eating into
maptick's time if the jps work is expensive enough (note the cost of
sleeping is not accounted for, and that has overhead)
This has happen before, usually when someone makes a lot of bots, and
it's really annoying.

So then, lets put JPS on a subsystem. That way the MC has control over
it.
But wait, existing code expects to yield and get back a path list, and
that's a sane request.
This is solvable, but requires abusing pass by reference lists, and the
ability to make callbacks into partials (preinsert arguments into them
before they're called, and accept other args later)

Because of this, we can now pass callbacks into pathfinders, allowing
for async use, rather then JUST yielding.

Of note: I've removed the 10 pathfinding datums limit, since
ratelimiting like that is handled nicely by the MC.
I've also removed the 15 second timeout, since mc yielding would trigger
it too often. I'm unsure if this means we don't have exit conditions for
pathfinding, need to talk to ryll. (@ Ryll-Ryll what happens if jps just
like, fails to find a path?)

Also of note: I think bots will fire off more then one pathfinding
attempt at a time if their first takes too long to complete. This is
dumb, why do we do this?

Optimizes JPS by more then 40% by removing redundant for(thing in turf)
loops, and avoiding making proc calls if objects are non dense.
This makes things slightly more fragile, but saves a LOT of time. I
think it's worth it, tho talking to mso it might be possible to do
better. Maybe I should do a LINDA system style thing. (I did a linda
system style thing I fixed it)

Optimizes botscanning, fixes bots not seeing things adjacent to them
The list of types could be a cached typecache
We could inline both checkscan and check_bot
check_bot SHOULD NOT BE CALLED ON EVERY OBJECT IN VIEW HOLY SHIT WHY
We don't need to process adjacent and the shuffled view separately, it's
in fact easier to process them in one block
Renames a var

Moves bot's pathing images to above most floor objects, so they're
visible in maint

## Why It's Good For The Game

Speed. Also manuel will stop killing their server by placing 20000
medibots (fucking icebox man every time)

## Changelog

:cl:
fix: Bots will now "notice" you if you're standing right next to them
fix: Bot paths will now draw above things like pipes, rather then below
them
refactor: Changed how pathfinding paths get generated
refactor: Made pathfinding and bot searching significantly faster
/:cl:

Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

* JPS Optimization (Light Botcode)

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

---
## [Gofawful5/TOPIASTATION](https://github.com/Gofawful5/TOPIASTATION)@[9e69e5d6ac...](https://github.com/Gofawful5/TOPIASTATION/commit/9e69e5d6acae10bf0941155c418ea3b9194668e5)
#### Wednesday 2023-03-29 01:00:13 by LemonInTheDark

Minor plane cube cleanup (#72038)

## About The Pull Request

[Fixes area lighting not working on turf change in multiz
cases](https://github.com/tgstation/tgstation/commit/7b92deffbca92a834cb0a361fd685de51a12ea53)

If you modify a area lit turf when using multiz, it'd end up using the
wrong plane for its light, because of stupid shit on my part.
Stupid shit resolved

[Fixes some uses of plane masters that only specified one rather then
all](https://github.com/tgstation/tgstation/commit/a59ec96d29710b967bf8b3ffe8210b230cb194b3)

We almost never only want to show SOME hidden planes. 
Should really make a helper for this someday

---
## [Timonkeyn/tgstation](https://github.com/Timonkeyn/tgstation)@[b174af7661...](https://github.com/Timonkeyn/tgstation/commit/b174af7661cbfaf564292caabfccca18619bda23)
#### Wednesday 2023-03-29 01:06:03 by Jacquerel

Basic Mob Carp Part VIII: Basic Mob Carp (#72073)

## About The Pull Request

Wow we're finally here. This turns carp into Basic Mobs instead of
Simple Animals.
They use a variety of behaviours added in previous PRs to act in a
marginally more interesting way than they used to.
But don't worry there's still 2 or 3 PRs to follow this one until I'm
done with space fish.

Changes in this PR:
Carp will try to run away if they get below 50% health, to make use of
their "regenerate if not attacked" component.
Magicarp have different targetting behaviour for spells depending on
their spell;
- Ressurecting Carp will try to ressurect allied mobs.
- Animating Carp will try to animate nearby objects.
- Door-creating Carp will try to turn nearby walls into doors.

You can order Magicarp to cast their spell on something if you happen to
manage to tame one.
The eating element now has support for "getting hurt" when you eat
something. Carp eating can rings and hating it was too soulful not to
continue supporting.

## Why It's Good For The Game

Carp are iconic beasts and I think they should be more interesting.
Also we just want to turn mobs into basic mobs anyway.

## Changelog

:cl:
add: Carp will now run away if their health gets low, meaning they may
have a chance to regenerate.
add: Lia will now fight back if attacked instead of letting herself get
killed, watch out!
balance: Magicarp will now aim their spells more intelligently.
add: Tame Magicarp can be ordered to use their spells on things.
refactor: Carp are now "Basic Mobs" instead of "Simple Mobs"
fix: Dehydrated carp no longer give you a bad feeling when they're your
friend and a good feeling when they're going to attack you.
balance: Tamed carp are now friendly only to their tamer rather than
their whole faction, which should make dehydrated carp more active.
Order them to stay or follow you if you want them to behave around your
friends.
/:cl:

---
## [Timonkeyn/tgstation](https://github.com/Timonkeyn/tgstation)@[125745d232...](https://github.com/Timonkeyn/tgstation/commit/125745d232163406c107d3947b87d6d406ac3a17)
#### Wednesday 2023-03-29 01:06:03 by Fikou

guardian death checks (#72251)

## About The Pull Request
if a guardian summoner is dead during the summoner setting process, we
(the guardian) now kill ourselves since itd mean a guardian that cant
die
to combat some fucked upness of it (if you inject a guardian and it only
spawns after you died and then dusts you), the process of spawning a
guardian from the playerside guardian creator stuff gets canceled if
youre dead or dont exist

## Why It's Good For The Game
yeah that seems good

## Changelog
:cl:
fix: guardian spirits check for death before they add themselves to you
/:cl:

---
## [Timonkeyn/tgstation](https://github.com/Timonkeyn/tgstation)@[47ec8ecd38...](https://github.com/Timonkeyn/tgstation/commit/47ec8ecd386f028ee8b2697412c89f00c9cd139f)
#### Wednesday 2023-03-29 01:06:03 by Rhials

Adds the Sandstorm random event, directional meteor functionality, space sand. (#71802)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request


![sandstorm](https://user-images.githubusercontent.com/28870487/206070641-80d37afc-a365-4f5e-ad48-e8cdf0153ac9.png)

Hey guys, it's your boy. Back at it again with another meteor-adjacent
event PR.

Adds the Sandstorm random event, inspired by the long-unused admin only
one. It picks a direction to approach from, alerts the crew of its
imminent arrival, and after a little over a minute of preparatory time,
sends waves of sand and dust to grind down everything in that direction.

To accomplish this, some minor adjustments had to be made to meteor
generation code. They can now be passed an optional arg for a direction
to be thrown from, and will pick a random one if no direction is given.

Also introduces the newest addition to our cast of meteors -- space
sand! It's even weaker than space dust, and shows up exclusively in this
event. Space sand is **ineffective against rwalls**, and will not damage
the arrivals area's high-tech sand-resistant glass. This is to prevent
this event from venting one of the most dust-vulnerable areas on the
station, and to make sure new players aren't shafted into firelock hell
when the right angle is picked.

I did a lot of testing and tweaking of numbers to get the damage to
average at about the level I'm comfortable with. This is meant to be a
high-impact event that isn't as destructive (or unavoidable) as a meteor
wave. Speaking of avoidance, let's talk about mitigation:

You get an early warning and a direction the sand will come from. You
have time to grab repair supplies, move to safety, get a MODsuit. You
can make worthwhile repairs as the sand comes in from inside (or
outside, if you're brave enough) with nothing more than a welder and
iron sheets. If you're feeling particularly spicy, you can leverage your
prep time setting up shield generators, which spawn in engineering and
have been added to the maintenance machines loot pool. Anyone can
contribute, so do your part as a good crewmate and help out!

All that being said, the event can't be prevented entirely. Shit's going
to get shredded, especially on the outside of the station. Damage will
vary heavily based on the station and direction, ranging from
inconsequential to threatening. It should happen late enough into the
round that, at the bare minimum, the crew shouldn't be caught
unprepared.

For those of you who are worried, the ORIGINAL sandstorm admin event is
still with us too. It's been moved from the space dust file into the
Sandstorm event file. This PR also makes a very minor change to the
naming of the space _dust_ events, for better menuing.

So, to sum it all up: Sand hits grinds down one side of the station, you
get a minute of warning, shield generators now spawn in maintenance. Be
a good crewmate and help where you can.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

More event variety is good, and events that give the players agency on
how bad the impact will be is even better.

<!-- Argue for the merits of your changes and how they benefit the game,
especially if they are controversial and/or far reaching. If you can't
actually explain WHY what you are doing will improve the game, then it
probably isn't good for the game in the first place. -->

## Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. You can read up on GBP
and it's effects on PRs in the tgstation guides for contributors. Please
note that maintainers freely reserve the right to remove and add tags
should they deem it appropriate. You can attempt to finagle the system
all you want, but it's best to shoot for clear communication right off
the bat. -->

:cl: Rhials
add: Sandstorm random event! A random side of the station is pummeled by
an onslaught of sand and dust. If you hear that one is approaching, grab
a welder and some iron to help with repairs!
add: Space sand! It's weak and doesn't hurt reinforced walls, but
shouldn't be underestimated in high quantities.
code: You can now pass a start direction to the
spawn_meteors/spawn_meteor global procs.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Hekzder/mojave-sun-13](https://github.com/Hekzder/mojave-sun-13)@[b2f0f35f3a...](https://github.com/Hekzder/mojave-sun-13/commit/b2f0f35f3afe1905cfefcf9e682de51cff2d4499)
#### Wednesday 2023-03-29 01:06:33 by EdwardNashton

Speed, Money and Faith: Updating an areas of Town. (#2286)

* Update TGS DMAPI

* Speed, Money and Faith: Updating an areas of Town.

Added a Church with a graveyard area (that currently empty because we have no tombs).

Remade one quarter into 4 different shops: Liquor, Pharmacy, Gun Shop, General Store.

Remade old shitty Library into Biker's Club.

Remade a Dime's Radio Station (by his permission)

Fixed a small area issue on a top z-level of Car Jankyard.

* Fixes up a bunch of stuff :)

* additional minority fixes

---------

Co-authored-by: tgstation-server <tgstation-server@users.noreply.github.com>
Co-authored-by: Edward Nashton <eddienigma48@gmail.com>
Co-authored-by: Professor Popoff <omniderpectional@gmail.com>

---
## [Cenrus/tgstation](https://github.com/Cenrus/tgstation)@[6de1258bd3...](https://github.com/Cenrus/tgstation/commit/6de1258bd3fb5919bb45f3dac3ae801d4b3bc8d6)
#### Wednesday 2023-03-29 01:10:04 by Jacquerel

Admins can now choose where fish go (#73109)

## About The Pull Request

I've pigeonholed myself as the fish guy now. It seems like someone made
events easier to add admin controls for so I thought I'd add some to the
event I most recently touched.

Instead of letting the RNG choose admins can now direct a circle of carp
to converge upon a specific location, or even a trail of specific
locations if they want the carp to just sort of swim in a circle around
the space station (although the ones on the far side of the station from
the starting point will travel all the way through it to get there).
This also works with magicarp.
They don't really move fast enough for you to use this to punish a
specific person but you can use it to annoy a specific location full of
people.

Plausibly there's no reason the code _wouldn't_ work for a specified
atom instead of a turf (as long as it sticks to one z level) but I
couldn't think of an elegant way of selecting that whereas "use my
current ghost location" is very intuitive, so I didn't add one.

## Why It's Good For The Game

Plausibly this permits admins do more fun things.

## Changelog

:cl:
admin: Admins can direct where carp (or magicarp) are interested in
going when manually triggering the event
/:cl:

---
## [Jalesen/tgstation](https://github.com/Jalesen/tgstation)@[ab307032ed...](https://github.com/Jalesen/tgstation/commit/ab307032edc7ed3dd360bfcc9176f6f54c22a3fe)
#### Wednesday 2023-03-29 01:11:04 by LemonInTheDark

Nightvision Rework (In the name of color) (#73094)

## About The Pull Request

Relies on #72886 for some render relay expansion I use for light_mask
stuff.

Hello bestie! Night vision pissed me off, so I've come to burn this
place to the ground.
Two sections to discuss here. First we'll talk about see_in_dark and why
I hate it, second we'll discuss the lighting plane and how we brighten
it, plus introducing color to the party.

### `see_in_dark` and why it kinda sucks

https://www.byond.com/docs/ref/#/mob/var/see_in_dark

See in dark lets us control how far away from us a turf can be before we
hide it/its contents if it's dark (not got luminosity set)
We currently set it semi inconsistently to provide nightvision to mobs.

The trouble is stuff that produces light != stuff that sets luminosity.
The worst case of this can be seen by walking out of escape on icebox,
where you'll see this


![image](https://user-images.githubusercontent.com/58055496/215683654-587fb00f-ebb8-4c83-962d-a1b2bf429c4a.png)

Snow draws above the lighting plane, so the snow will intermittently
draw, depending on see_in_dark and the luminosity from tracking lights.
This would in theory be solvable by modifying the area, but the same
problem applies across many things in the codebase.
As things currently stand, to be emissive you NEED to have a light on
your tile. People are bad at this, and honestly it's a bit much to
expect of them. An emissive overlay on a canister shouldn't need an
element or something and a list on turfs to manage it.
This gets worse when you factor in the patterns I'm using to avoid
drawing lights above nothing, which leads to lights that should show,
but are misoffset because their parent pixel offsets.

It's silly. We do it so we can have things like mesons without just
handing out night vision, but even there the effect of just hiding
objects and mobs looks baddddddd when moving. It's always bothered me.
I'll complain about mesons more later, but really just like, they're too
bright as it is.

I'm proposing here that rather then manually hiding stuff based off
distance from the player, we can instead show/hide using just the
lighting plane. This means things like mesons are gonna get dimmer, but
that's fine because they suck.

It does have some side effects, things like view() on mobs won't hide
stuff in darkness, but that's fine because none actually thinks about
view like that, I think.

Oh and I added a case to prevent examining stuff that's in darkness, and
not right next to you when you don't have enough nightvision, to match
the old behavior `see_in_dark` gave us.

Now I'd like to go on a mild tangent about color, please bare with me

### Color and why `lighting_alpha` REALLY sucks

You ever walk around with mesons on when there's a fire going, or an
ethereal or firelocks down.
You notice how there isn't really much color to our lights? Doesn't that
suck?

It's because the way we go about brighting lighting is by making
everything on the lighting plane transparent.
This is fine for brightening things, but it ends up looking kinda crummy
in the end and leads to really washed out colors that should be bright.
Playing engineer or miner gets fucking depressing.

The central idea of this pr, that everything else falls out of, is
instead of making the plane more transparent, we can use color matrixes
to make things AT LEAST x bright.

https://www.byond.com/docs/ref/#/{notes}/color-matrix

Brief recap for color matrixes, fully expanded they're a set of 20
different values in a list
Units generally scale 0-1 as multipliers, though since it's
multiplication in order to make an rgb(1,1,1) pixel fullbright you would
need to use 255s.

A "unit matrix" for color looks like this:
```
list(1, 0, 0, 0,
     0, 1, 0, 0,
     0, 0, 1, 0,
     0, 0, 0, 1,
     0, 0, 0, 0
)
```

The first four rows are how much each r, g, b and a impact r, g, b and
well a.
So a first row of `(1, 0, 0, 0)` means 1 unit of r results in 1 unit of
r. and 0 units of green, blue and alpha, and so on.
A first row of `(0, 1, 0, 0)` would make 1 red component into 1 green
component, and leave red, blue and alpha alone, shifting any red of
whatever it's applied to a green.

Using these we can essentially color transform our world. It's a fun
tool. But there's more.

That last row there doesn't take a variable input like the others.
Instead, it ADDS some fraction of 255 to red, green, blue and alpha.

So a fifth row of `(1, 0, 0, 0)` would make every pixel as red as it
could possibly be.

This is what we're going to exploit here. You see all these values
accept negative multipliers, so we can lower colors down instead of
raising them up!
The key idea is using color matrix filters
https://www.byond.com/docs/ref/#/{notes}/filters/color to chain these
operations together.

Pulling alllll the way back, we want to brighten darkness without
affecting brighter colors.
Lower rgb values are darker, higher ones are brighter. This relationship
isn't really linear because of suffering reasons, but it's good enough
for this.
Let's try chaining some matrixes on the lighting plane, which is bright
where fullbright, and dark where dark.

Take a list like this

```
list(1, 0, 0, 0,
     0, 1, 0, 0,
     0, 0, 1, 0,
     0, 0, 0, 1,
     -0.2, -0.2, -0.2, 0
)
```
That would darken the lighting a bit, but negative values will get
rounded to 0
A subsequent raising by the same amount
```
list(1, 0, 0, 0,
     0, 1, 0, 0,
     0, 0, 1, 0,
     0, 0, 0, 1,
     0.2, 0.2, 0.2, 0
)
```
Will essentially threshold our brightness at that value.
This ensures we aren't washing out colors when we make things brighter,
while leaving higher values unaffected since they basically just had a
constant subtracted and then readded.

### But wait, there's more

You may have noticed, we gain access to individual color components
here.
This means not only can we darken and lighten by thresholds, we can
COLOR those thresholds.
```
list(1, 0, 0, 0,
     0, 1, 0, 0,
     0, 0, 1, 0,
     0, 0, 0, 1,
     0.1, 0.2, 0.1, 0
)
```
Something like the above, if applied with its inverse, would tint the
darkness green.
The delta between the different scalars will determine how vivid the
color is, and the actual value will impact the brightness.

Something that's always bothered me about nightvision is it's just
greyscale for the most part, there isn't any color to it.
There was an old idea of coloring the game plane to match their lenses,
but if you've ever played with the colorblind quirk you know that gets
headachey really fast.
So instead of that, lets color just the darkness that these glasses
produce.
It provides some reminder that you're wearing them, instead of just
being something you forget about while playing, and provides a reason to
use flashlights and such since they can give you a clearer, less tinted
view of things while retaining the ability to look around things.

I've so far applied this pattern to JUST headwear for humans (also those
mining wisps)
I'm planning on furthering it to mobs that use nightvision, but I wanted
to get this up cause I don't wanna pr it the day before the freeze.

Mesons are green, sec night vision is red, thermals orange, etc.

I think the effect this gives is really really nice. 
I've tuned most things to work for the station, though mesons works for
lavaland for obvious reasons.

I've tuned things significantly darker then we have them set currently,
since I really hate flat lighting and this system suffers when
interacting with it.

My goal with these is to give you a rough idea of what's around you,
without a good eye for detail.
That's the difference between say, mesons, and night vision. One helps
you see outlines, the other gives you detail and prevents missing
someone in the darkness.

It's hard to balance this precisely because of different colored
backgrounds (looking at you icebox)
More can be done on this front in future but I'm quite happy with things
as of now

### **EDIT**

I have since expanded to all uses of nightvision, coloring most all of
them.

Along the way I turned some toggleable nightvision into just one level. 
Fullbright sucks, and I'd rather just have one "good" value.

I've kept it for a few cases, mostly eyes you rip out of mobs.
Impacted mobs are nightmares, aliens, zombies, revenants, states and
sort of stands.

I've done a pass on all mobs and items that impact nightvision and added
what I thought was the right level of color to them. This includes stuff
like blobs and shuttle control consoles
As with glasses much of this was around reducing vision, though I kept
it stronger here, since many of these mobs rely on it for engaging with
the game

<details>
<summary>
Technical Changes
</summary>

#### Adds filter proc (the ones that act like templates) support to
filter transitions.
Found this when testing this pr, seemed silly.

#### Makes our emissive mask mask all light instead
This avoids dumbass overlay lighting lighting up wallmounts.
We switch modes if some turfflags are set, to accomplish the same thing
with more overhead, and support showing things through the darkness.

Also fixes a bug where you'd only get one fullscreen object per mob, so
opening and closing a submap would take it away

Also also fixes the lighting backdrop not actually spanning the screen. 
It doesn't actually do anything anymore because of the fullscreen light
we have, but just in case that's unsued.
Needs cleanup in future.

#### Moves openspace to its own plane that doesn't draw, maxing its
color with a sprite

This is to support the above
We relay this plane to lighting mask so openspace can like, have
lighting

#### Changes our definition of nightvision to the light cutoff of night
vision goggles and such
Side affect of removing see_in_dark. This logic is a bit weak atm, needs
some work.

#### Removes the nightvision spell
It's a dupe of the nightvision action button, and newly redundant since
I've removed all uses of it

#### Cleans up existing plane master critical defines, ensures
trasnparent won't render

These sucked
Also transparent stuff should never render, if it does you'll get white
blobs which suck

</details>

## Why It's Good For The Game

Videos! (Github doesn't like using a summary here I'm sorry)
<details>

Demonstration of ghost lighting, and color


https://user-images.githubusercontent.com/58055496/215693983-99e00f9e-7214-4cf4-a76a-6e669a8a1103.mp4

Engi-glass mesons and walking in maint (Potentially overtuned, yellow is
hard)


https://user-images.githubusercontent.com/58055496/215695978-26e7dc45-28aa-4285-ae95-62ea3d79860f.mp4

Diagnostic nightvision goggles and see_in_dark not hiding emissives


https://user-images.githubusercontent.com/58055496/215692233-115b4094-1099-4393-9e94-db2088d834f3.mp4

Sec nightvision (I just think it looks neat)


https://user-images.githubusercontent.com/58055496/215692269-bc08335e-0223-49c3-9faf-d2d7b22fe2d2.mp4

Medical nightvision goggles and other colors


https://user-images.githubusercontent.com/58055496/215692286-0ba3de6a-b1d5-4aed-a6eb-c32794ea45da.mp4

Miner mesons and mobs hiding in lavaland (This is basically the darkest
possible environment)


https://user-images.githubusercontent.com/58055496/215696327-26958b69-0e1c-4412-9298-4e9e68b3df68.mp4

Thermal goggles and coloring displayed mobs


https://user-images.githubusercontent.com/58055496/215692710-d2b101f3-7922-498c-918c-9b528d181430.mp4

</details>

I think it's pretty, and see_in_dark sucks butt.

## Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. You can read up on GBP
and it's effects on PRs in the tgstation guides for contributors. Please
note that maintainers freely reserve the right to remove and add tags
should they deem it appropriate. You can attempt to finagle the system
all you want, but it's best to shoot for clear communication right off
the bat. -->

:cl:
add: The darkness that glasses and hud goggles that impact your
nightvision (think mesons, nightvision goggles, etc) lighten is now
tinted to match the glasses. S pretty IMO, and hopefully it helps with
forgetting you're wearing X.
balance: Nightvision is darker. I think bright looks bad, and things
like mesons do way too much
balance: Mesons (and mobs in general) no longer have a static distance
you can see stuff in the dark. If a tile is lit, you can now see it.
fix: Nightvision no longer dims colored lights, instead simply
thresholding off bits of darkness that are dimmer then some level.
/:cl:

---
## [Pickle-Coding/tgstation](https://github.com/Pickle-Coding/tgstation)@[25d4afc869...](https://github.com/Pickle-Coding/tgstation/commit/25d4afc869585373571da5ba4a77fb967ffdedfe)
#### Wednesday 2023-03-29 01:12:33 by Iamgoofball

Retires explosive lance crafting to a nice farm upstate where it has plenty of room to run around (#71256)

## About The Pull Request

You can no longer craft explosive lances.

## Why It's Good For The Game

Explosive lances are unhealthy for the game in it's current iteration.
Many years ago when the game was more loose and we weren't dealing with
players who treat the game like competitive TTT or Town of Salem,

They are a one shot kill weapon, which is the most powerful kind of
weapon in every gamemode. @JohnFulpWillard likened it to 1f1, a concept
from Town of Salem players where the town trades 1 person for 1 bad guy.

Modern ss13 design includes a significantly heavier load of antagonists
that aren't fixed roundstart compared to when the e-lance went in.

When we added the e-lance, if nuke ops spawned, that was it, there was
nuke ops, if you e-lanced the nuke ops and died you were dead until the
next round.

Nowadays you're rolling for lone operative, blob, wizard, disease,
revenant, and every other fun enjoyable antagonist role under the sun.

I can e-lance a nuke op/cultist/traitor/revolutionary/any bad guy in the
game as a non-antag assistant, die, and have a good chance to roll
another, way more fun antag in deadchat.

My change to make the e-lance a proper "we both die" tool didn't
actually help because I didn't quite realize that to the modern SS13
player because of how we designed Dynamic and antagonists in the modern
era, death is, frankly, not a punishment anymore.

It's time we admit the facts, items designed in 2015 SS13 in #12389
simply don't hold up in a healthy manner in 2022 SS13. Dying in SS13 in
2015 was a significantly different experience with different
consequences than it has now, and right now "kills you when you use it"
is not the same massive downside it was 7-8 years ago.

## Changelog
:cl:
del: You can no longer craft explosive lances.
/:cl:

---
## [Gofawful5/Skyrat-tg](https://github.com/Gofawful5/Skyrat-tg)@[2b9eba0fe0...](https://github.com/Gofawful5/Skyrat-tg/commit/2b9eba0fe06284c58a80303698784c7ccede75f4)
#### Wednesday 2023-03-29 01:13:40 by SkyratBot

[MIRROR] Smoothing groups optimization, save 265ms with configs, more on production & w/ space ruins [MDB IGNORE] (#18189)

* Smoothing groups optimization, save 265ms with configs, more on production & w/ space ruins (#71989)

This one is fun.

On every /turf/Initialize and /atom/Initialize, we try to set
`smoothing_groups` and `canSmoothWith` to a cached list of bitfields. At
the type level, these are specified as lists of IDs, which are then
`Join`ed in Initialize, and retrieved from the cache (or built from
there).

The problem is that the cache only misses about 60 times, but the cache
hits more than a hundred thousand times. This means we eat the cost of
`Join` (which is very very slow, because strings + BYOND), as well as
the preliminary `length` checks, for every single atom.

Furthermore, as you might remember, if you have any list variable set on
a type, it'll create a hidden `(init)` proc to create the list. On
turfs, that costs us about 60ms.

This PR does a cool trick where we can completely eliminate the `Join`
*and* the lists at the cost of a little more work when building the
cache.

The trick is that we replace the current type definitions with this:

```patch
- smoothing_groups = list(SMOOTH_GROUP_TURF_OPEN, SMOOTH_GROUP_FLOOR_ASH)
- canSmoothWith = list(SMOOTH_GROUP_FLOOR_ASH, SMOOTH_GROUP_CLOSED_TURFS)
+ smoothing_groups = SMOOTH_GROUP_TURF_OPEN + SMOOTH_GROUP_FLOOR_ASH
+ canSmoothWith = SMOOTH_GROUP_FLOOR_ASH + SMOOTH_GROUP_CLOSED_TURFS
```

These defines, instead of being numbers, are now segments of a string,
delimited by commas.

For instance, if ASH used to be 13, and CLOSED_TURFS used to be 37, this
used to equal `list(13, 37)`. Now, it equals `"13,37,"`.

Then, when the cache misses, we take that string, and treat it as part
of a JSON list, and decode it from there. Meaning:

```java
// Starting value
"13,37,"

// We have a trailing comma, so add a dummy value
"13,37,0"

// Make it an array
"[13,37,0]"

// Decode
list(13, 37, 0)

// Chop off the dummy value
list(13, 37) // Done!
```

This on its own eliminates 265ms *without space ruins*, with the
combined savings of turf/Initialize, atom/Initialize, and the hidden
(init) procs that no longer exist.

Furthermore, there's some other fun stuff we gain from this approach
emergently.

We previously had a difference between `S_TURF` and `S_OBJ`. The idea is
that if you have any smoothing groups with `S_OBJ`, then you will gain
the `SMOOTH_OBJ` bitflag (though note to self, I need to check that the
cost of adding this is actually worth it). This is achieved by the fact
that `S_OBJ` simply takes the last turf, and adds onto that, meaning
that if the biggest value in the sorting groups is greater than that,
then we know we're going to be smoothing to objects.

This new method provides a limitation here. BYOND has no way of
converting a number to a string at compile time, meaning that we can't
evaluate `MAX_S_TURF + offset` into a string. Instead, in order to
preserve the nice UX, `S_OBJ` now instead opts to make the numbers
negative. This means that what used to be something like:

```dm
smoothing_groups = list(SMOOTH_GROUP_ALIEN_RESIN, SMOOTH_GROUP_ALIEN_WEEDS)
```

...which may have been represented as

```dm
smoothing_groups = list(15, MAX_S_TURF + 3)
```

...will now become, at compile time:

```dm
smoothing_groups = "15,-3,"
```

Except! Because we guarantee smoothing groups are sorted through unit
testing, this is actually going to look like:

```dm
smoothing_groups = "-3,15,"
```

Meaning that we can now check if we're smoothing with objects just by
checking if `smoothing_groups[1] == "-"`, as that's the only way that is
possible. Neat!

Furthermore, though much simpler, what used to be `if
(length(smoothing_groups))` (and canSmoothWith) on every single
atom/Initialize and turf/Initialize can now be `if (smoothing_groups)`,
since empty strings are falsy. `length` is about 15% slower than doing
nothing, so in procs as hot as this, this gives some nice gains just on
its own.

For developers, very little changes. Instead of using `list`, you now
use `+`. The order might change, as `S_OBJ` now needs to come first, but
unit tests will catch you if you mess up. Also, you will notice that all
`S_OBJ` have been increased by one. This is because we used to have
`S_TURF(0)` and `S_OBJ(0)`, but with this new trick, -0 == 0, and so
they conflicted and needed to be changed.

* Sorting how did I miss it

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>
Co-authored-by: Funce <funce.973@gmail.com>

---
## [SmoSmoSmoSmok/tgstation](https://github.com/SmoSmoSmoSmok/tgstation)@[06a7e74790...](https://github.com/SmoSmoSmoSmok/tgstation/commit/06a7e74790b3b05b7f4fb522ff55858ef0d66418)
#### Wednesday 2023-03-29 01:14:24 by Unit2E

Changes the hypno flash to work on unconscious people (#73025)

## About The Pull Request

The hypno flash is a really fun and flavourful item that is both strong
while allowing for gimmicks. However, personally, I've always been a bit
confused as to what counted for hypnosis, until looking into the
specifics. I also know that I'm probably not alone in this, because
various people have told me over the years that sleep doesn't work,
while it definitely does. This PR hopes to change this by somewhat
buffing the hypno flash, by making unconsciousness work for hypnosis.

## Why It's Good For The Game

Unconsciousness looks very similar to sleep, and in a lot of cases it is
really just the same effect... except for hypnosis, where there is no
effect on unconscious people. Personally, I don't think this is the best
UX and it limits the options there are for hypnotising people, which is
a shame, as I think it's very interesting. This may or may not be too
strong (think using the hypno flash with the micro-laser), but I still
think this is preferable to only working with sleep specifically or
hypnosis, might warrant a TC up if people otherwise agree with the
change. Also, just to note, unconsciousness is also still separate from
crit. This does not let you hypnotise people for free because they're in
crit.

---
## [TheBoondock/tgstation](https://github.com/TheBoondock/tgstation)@[a47afd9051...](https://github.com/TheBoondock/tgstation/commit/a47afd905156bcc9a070db015cec7b1d1a07c578)
#### Wednesday 2023-03-29 01:18:06 by Sol N

2 New Positive Quirks! (#72912)

## About The Pull Request

I added a few quirks to a downstream that I feel fit well with tg so
here they are.

First up is Poster Boy, a quirk that gives you three mood altering
posters, similar to the traitor objective to hang up demoralizing
posters. You spawn with a box that has one poster that will uplift the
entire crews spirits and 2 that are unique to your department. Captain
counts for security and assistants get only neutral posters. Finally,
with a crayon or spraycan, if you are any antagonist you can make your
poster into one of the ones from the traitor objective.

![dreamseeker_nRy44SL9Jb](https://user-images.githubusercontent.com/116288367/214109008-6f1b4b7c-e800-4142-be6d-926a8e975973.png)
example of quirk posters
Costs 4.


Finally, the characterful Throwing Arm quirk, which lets you throw
objects further (but not harder) and means you will never miss shots
into the disposals bin.
Costs 7.

previously i had a food subscription quirk here as well but i pulled it
out and plan to re-add it as a separate PR in march, where it will now
give you ingredients to cook a meal with occasionally.

## Why It's Good For The Game

Positive quirk variety is good and fun, I think that these positive
quirks are reasonable ones that offer unique things that the current
positive quirks do not.
Poster boy gives people a reason to run around and claim wall real
estate for their department and hopefully can build more solidarity in
departments, the hidden antag feature probably has uses but is just for
styling on people.
Throwing arm offers a fun character trait that probably can have some
slight uses and encourages the use of throwing weapons and tools more.
Also it is good to have a way to never miss the disposals bin. It's so
embarrassing.

## Changelog
:cl:
add: Poster boy and Throwing arm positive quirks.
imageadd: added posters for poster boy quirk
/:cl:

---
## [Higgin/Skyrat-tg](https://github.com/Higgin/Skyrat-tg)@[e3435943f8...](https://github.com/Higgin/Skyrat-tg/commit/e3435943f8357df864247ee0e6a2b445cc4d0d3d)
#### Wednesday 2023-03-29 01:18:12 by SkyratBot

[MIRROR] Allows Chaplain's Spirit Sword To Redo Name If Invalid [MDB IGNORE] (#18723)

* Allows Chaplain's Spirit Sword To Redo Name If Invalid (#72642)

## About The Pull Request

The current behavior doesn't let the sword re-choose their name if they
screw it up the first time and it turns out to be filtered or sanitized
out for whatever reason. That's silly in my opinion, so I changed it to
be more like holoparasite name-selection behavior, where you get the
text to choose your name until you get it right.

I moved the re-naming portion of the sword to be after all of the
important RegisterSignal steps as well, just to be safe as we sleep as
they plug in different names they might want.
## Why It's Good For The Game

You shouldn't be stuck as "spirit of the blade" permanently if you
accidentally balls up the word filter, let's have it be more like
holoparasite behavior to be nicer.
## Changelog
:cl:
qol: Spirits of possessed blades (Chaplain's Null Rod Option) will be
able re-try selecting their name if it ends up to be filtered for any
reason.
/:cl:

* Allows Chaplain's Spirit Sword To Redo Name If Invalid

Co-authored-by: san7890 <the@san7890.com>

---
## [Kazakazara/tgstation](https://github.com/Kazakazara/tgstation)@[66b7310039...](https://github.com/Kazakazara/tgstation/commit/66b7310039297843b01c5b14a9b59180909ab52c)
#### Wednesday 2023-03-29 01:20:49 by Rhials

STAY IN THE LIGHT: Adds terrify Nightmare spell, terrified status effect, and a reason to mind the shadows (#72282)

Adds the Terrify spell, and its associated status effect, Terrified.
This new spell is given to antagonist nightmares, as a part of their
brain. The spell only works in those surrounded by darkness, and will
apply the Terrified status effect if successful. Upon being Terrified,
victims will passively gain **Terror Buildup** if they remain in the
dark. As buildup increases, so do the negative effects, including tunnel
vision, panic attacks, dizziness, and more.

There are two primary methods for mitigating terror buildup. The first
is moving into the light, which will reverse the passive terror buildup
and eventually make it go away. The other method is by getting a hug
from a friendly hand, which will reduce buildup significantly.

Getting a hug from an UNfriendly hand (a nightmare, for instance) will
cause the victim to freak out and be briefly knocked down. This can be
spammed on targets who are caught alone in the dark, keeping them in an
unfavorable position (sideways) and adding to the victim's terror
buildup considerably. Escape into the light as soon as possible, or
you'll be pushed to MAXIMUM TERROR BUILDUP.

To what end? Heart failure. Past the soft terror cap (which limits how
much passively generated terror you can make) exists the hard terror
cap. Bypassing that threshold will cause a stress induced heart attack
and knock you unconscious (embarrassing!)

---
## [openai/evals](https://github.com/openai/evals)@[fe8e3b03e3...](https://github.com/openai/evals/commit/fe8e3b03e34f666774d63e6ae33d3f14d047d973)
#### Wednesday 2023-03-29 01:33:54 by Josh Tanner

Manga Translation Eval (#319)

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
manga-translation

### Eval description

Testing the model's ability to translate Manga (Japanese comics) from
Japanese into English.

### What makes this a useful eval?

We think this is useful primarily because it's a good way to test models
on a less standard translation case. Specifically,
1) The content of the text has a very different domain from most
translation tasks
2) Context from surrounding speech bubbles/panels is important, so being
able to use them in translation is better, but in order to do that the
model needs to make sure the number of output translations precisely
matches the number of input translations (it seems to struggle with
this)
3) The task is fundamentally multi-modal because oftentimes necessary
information is contained in the image surrounding the text; current
evals are text-only, but we really want to try this with GPT-4's image
processing capabilities as well (and plan to update the eval to include
images as soon as such functionality becomes available)


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

Manga translation is a pretty unique task. 

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.jsonl`
- [x] Ensure you have the right to use the data you submit via this eval
(data comes from the [Open Mantra
Dataset](https://github.com/mantra-inc/open-mantra-dataset), which our
company published)

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
{"input": [{"role": "system", "content": "Given a sequence of texts
representing some pages of manga in Japanese, generate a high-quality
English translation that accurately conveys the meaning and emotion of
the original text. Each input line corresponds to a speech bubble or
narration box in the manga, so please ensure that the number of output
lines exactly matches the number of input lines. For example, if the
input is:\n\n テキスト1\n テキスト2\n テキスト3\n\n The output should be:\n\n
text1\n text2\n text3\n\n Please do not provide any explanation in the
output other than the translation itself."}, {"role": "user", "content":
"知らないって言ってるだろっ\nそんな借金なんて!"}], "ideal": "I don't know what you're talking
about!\ni don't owe you!"}
{"input": [{"role": "system", "content": "Given a sequence of texts
representing some pages of manga in Japanese, generate a high-quality
English translation that accurately conveys the meaning and emotion of
the original text. Each input line corresponds to a speech bubble or
narration box in the manga, so please ensure that the number of output
lines exactly matches the number of input lines. For example, if the
input is:\n\n テキスト1\n テキスト2\n テキスト3\n\n The output should be:\n\n
text1\n text2\n text3\n\n Please do not provide any explanation in the
output other than the translation itself."}, {"role": "user", "content":
"そうは言ってもなぁ\nレーネ..."}], "ideal": "well, I'm sorry...\nlene..."}
{"input": [{"role": "system", "content": "Given a sequence of texts
representing some pages of manga in Japanese, generate a high-quality
English translation that accurately conveys the meaning and emotion of
the original text. Each input line corresponds to a speech bubble or
narration box in the manga, so please ensure that the number of output
lines exactly matches the number of input lines. For example, if the
input is:\n\n テキスト1\n テキスト2\n テキスト3\n\n The output should be:\n\n
text1\n text2\n text3\n\n Please do not provide any explanation in the
output other than the translation itself."}, {"role": "user", "content":
"こっちにゃ借用書があんだよ\nトルティヤーノに借りた金はちゃんと返して貰わねぇと"}], "ideal": "we've got proof
here...\nYou know we need you to pay us back..."}
{"input": [{"role": "system", "content": "Given a sequence of texts
representing some pages of manga in Japanese, generate a high-quality
English translation that accurately conveys the meaning and emotion of
the original text. Each input line corresponds to a speech bubble or
narration box in the manga, so please ensure that the number of output
lines exactly matches the number of input lines. For example, if the
input is:\n\n テキスト1\n テキスト2\n テキスト3\n\n The output should be:\n\n
text1\n text2\n text3\n\n Please do not provide any explanation in the
output other than the translation itself."}, {"role": "user", "content":
"知るもんかっ"}], "ideal": "how should I know!?"}
{"input": [{"role": "system", "content": "Given a sequence of texts
representing some pages of manga in Japanese, generate a high-quality
English translation that accurately conveys the meaning and emotion of
the original text. Each input line corresponds to a speech bubble or
narration box in the manga, so please ensure that the number of output
lines exactly matches the number of input lines. For example, if the
input is:\n\n テキスト1\n テキスト2\n テキスト3\n\n The output should be:\n\n
text1\n text2\n text3\n\n Please do not provide any explanation in the
output other than the translation itself."}, {"role": "user", "content":
"父親がカジノで作った借金なんて..."}], "ideal": "how should I know about my father's
debt in casinos..."}
  ```
</details>

Co-authored-by: Josh Tanner <mantra@mantra.co.jp>

---
## [L1nd/--tgstation](https://github.com/L1nd/--tgstation)@[74144f2bc9...](https://github.com/L1nd/--tgstation/commit/74144f2bc9e69c9829339a1bd7ffa962e37c0cd0)
#### Wednesday 2023-03-29 01:37:28 by LemonInTheDark

Fixes some runtime spam from lazyloading/map templates (#73037)

## About The Pull Request

Ensures we don't try and rebuild loading turfs midload

Turf refs persist through destroy, so when we changeturf earlier to get
our turf reservation, we insert our space turfs into the rebuild queue,
and then end up here where we can be rebuilt randomly, midload, with
uninit'd turfs

Avoids starting atmos machine processing until init

This avoids some runtimes with null gasmixtures

There's still trouble with atmos and template loading, pipes start
processing before their pipelines exist, so we just kinda get fucked.
Need to look into this more deeply, it involves pulling this stuff off
`on_construct` and `setup_template_machinery` and throwing it in maybe
late init, which I don't really relish but will just have to do
eventually.

## Why It's Good For The Game

Reduces runtime spam

---
## [nsherwood1/tgstation](https://github.com/nsherwood1/tgstation)@[fedf2f3a26...](https://github.com/nsherwood1/tgstation/commit/fedf2f3a26869848f5fc8f41381d1aff944ed9f6)
#### Wednesday 2023-03-29 01:40:13 by Sol N

more span macro changes in brain traumas and disease files (#73273)

## About The Pull Request

i was fucking around with brain traumas on a downstream and noticed they
had similar issues to quirks so i decided to continue work from #73116


![Code_Klx14O288V](https://user-images.githubusercontent.com/116288367/217046732-765ffe27-73c9-416a-833e-e0d9e2aa7a86.png)
(search in VSC for span class = 'notice')
its going to be a bit of a thing to get all of these but this is a
decent chunk i think

there was only one annoying/tough file.
imaginary_friend.dm had class = 'game say' and class = 'emote' both of
which after some testing did not seem like they did anything. ill try to
keep that in mind in other files if i continue to do this but i either
omitted them because they didnt have any formatting or, in the case of
emote, turned it into name, which i think is what you'd want those
messages to look like.

there were also a few small spelling errors that i fixed

## Why It's Good For The Game

more consistent and stops people from copying brain trauma formatting
wrong

## Changelog

they should all work the same

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [lnGoror/tgstation](https://github.com/lnGoror/tgstation)@[c3a1f21c1a...](https://github.com/lnGoror/tgstation/commit/c3a1f21c1afc10bd5515114e0c6117ac73c87f62)
#### Wednesday 2023-03-29 01:40:55 by MrMelbert

Converts blindness and nearsightedness to status effects, scratches some VERY dumb blindness handling that resulted in mobs becoming "incurably" blind (#72267)

## About The Pull Request

- Nearsighted is now a grouped status effect.
- Blindness is now a grouped status effect.
   - Eye handling of blindness has improved. 
- When eyes are removed, they now cause you to become blind, rather than
handling it in `update_tint`.
- Being ahealed no longer blinds you for one tick, meaning that black
overlay on aheal is gone.
- Temporary Blindness is now a status effect.
- Both Nearsightedness and Blindness have been exorcised from mob vars
and life chains. This means that we've finally cut 2 procs from life,
`handle_status_effect` and `handle_traits`, and moved both to event
based processing. Wooo optimizations.
- Swapped pacifism status effect to use apply and set helpers. 
- Removed an unused admin toggle that disabled welding helmet tint but
also tint from every clothing item and also blindness from losing your
eyes.
- Clothes now generally all blind their mob more consistently.
- Oculine, eye surgery, and sensory restoration are now no longer the
only way to fix blindness from eye damage. If your eyes are healed
through any other means, it will also heal your blindness.
- Some things that made you blind, such as ling blind sting, no longer
just flat made you blind from eye damage forever. They now cause eye
damage directly, which in turn makes you blind from eye damage, as
expected.
- Pacifists can't eyestab anymore. Eyestabs now have a limit on the
amount of blur applied.
- Refactored some `is_x_covered` procs to accept flags rather than have
a lot of arguments for some silly reason.
- Unit tests for blindness. 

## Why It's Good For The Game

Blindness was exceptionally poorly handled prior, primarily due to the
fact that it was tied to the mob instead of separated out

On top of that the system put a LOT of faith in proper handling of
blindness on the coder's end which was misplaced evidently. Many places
didn't update or handle blindness correctly, or just let people
perma-blind.

Deferring it to a status effect improves this a lot

## Changelog

:cl: Melbert
refactor: Refactored blindness and nearsightedness. Important to note is
that all mobs are naturally blind until their eyes are actually created.
refactor: Refactored "is covered" procs
fix: Less sources of blindness now cause permanent blindness. Includes
the "Blind" Spell and "Blind Sting" from changelings.
admin: Ahealing someone no longer flashes the blind overlay for 1 tick.
admin: I removed an unused (sort of) inaccessible admin verb that
allowed you to toggle the tint from all welding helmets (and clothing)
(and lack of eyes) in existence, let me know if you want similar back
balance: Changeling "Blind Sting" now causes eye damage (enough to
blind) rather than arbitrarily forcing blindness.
balance: Visionloss virus symptom now causes eye damage (enough to
blind) rather than arbitrarily forcing blindness.
balance: Oculine has been reworked slightly. Prior, Oculine arbitrarily
healed blindness and nearsightedness from eye damage reagrdless of how
damaged the eyes were, and applied blur on success. Now, Oculine just
heals eye damage, and blindness / nearsightedness is restored in the
process. There is now a probability every tick that eye blur is applied
based on how pure the oculine is while healing very damaged eyes.
balance: Pacifists can no longer eyestab.
balance: Any clothing item that covers your eyes contributes to getting
the bonus while sleeping, and to removing temporary blindness faster
/:cl:

---
## [Ebin-Halcyon/tgstation](https://github.com/Ebin-Halcyon/tgstation)@[374c8340c8...](https://github.com/Ebin-Halcyon/tgstation/commit/374c8340c8c99586a4b4b8e978947c0b0f83a9d7)
#### Wednesday 2023-03-29 01:41:49 by Jacquerel

Console Hack / Unfavourable Events won't run ghost roles which don't have time to do anything (#73343)

## About The Pull Request

Fixes #69201
The dynamic subsystem will never roll a new antagonist once the shuttle
is past the point of no return, but this check is bypassed by Console
Hacks and Unfavourable Event rolls (which are chiefly triggered from
console hacks, but also from when the Revolution wins).

I have made these procs more discerning.
Unfavourable Events will now never pick any heavy dynamic midround if
the shuttle is past the point of no return.
Console Hacking will now never spawn sleeper agents if the shuttle is
past the point of no return, and won't spawn Fugitives or Pirates if the
shuttle is called at all even if it can still be recalled

It's my feeling that given the need to get organised and move a ship to
the station there isn't really time for either of those events to
actually start properly rolling, but if you feel like that information
might be metagamed in some way by messing around with the shuttle (not
sure why or to what end, but it's technically manipulatable if you know
how the code works?) I can just give these the same restriction as
Traitor even if it means the bounty hunters risk showing up after the
shuttle has already left.

## Why It's Good For The Game

To some extent it's your own fault for clicking the popup while knowing
full well how much round time is left until the game ends, but it's
still disappointing to see a Blob or Pirates or Wizard alert appear at a
time when they can't possibly do anything interesting.
This is more true for the Pirate and Fugitive events because they
involve teamwork, placing a space ship, travel between the ship and the
station, and in the case of Fugitives its own internal five minute timer
before the other team actually arrives.

## Changelog

:cl:
fix: Hacking the Comms Console or winning a Revolution can no longer
spawn antagonists if there's not enough time left in the round for them
to antagonise anyone.
/:cl:

---
## [faaaay/coyote-bayou](https://github.com/faaaay/coyote-bayou)@[288f673652...](https://github.com/faaaay/coyote-bayou/commit/288f6736526554c75abbcb09c92acb457be1c9b0)
#### Wednesday 2023-03-29 01:46:51 by Superlagg

Merge remote-tracking branch 'upstream/master' into that-stupid-fuckin-dumb-shitass-fuckin--fuck-fuckass-shitfuck-gun-thing-that-isnt-alll-that-bad-honestly

---
## [Zonespace27/tgstation](https://github.com/Zonespace27/tgstation)@[661eaa985e...](https://github.com/Zonespace27/tgstation/commit/661eaa985e32056cc25f32bd81d9106861a4f9f8)
#### Wednesday 2023-03-29 01:48:00 by MrMelbert

Important heretic spell rebalancing (#71620)

## About The Pull Request

Nerfs
- Furious steel cooldown: 30s -> 60 seconds (when ascended: 10s -> 30s)
- Furious steel: Now affected by antimagic
- Cleave cooldown: 40s -> 45s
- Cleave range: 9 tiles -> 4 tiles
- Cleave wound: Now has natural clotting, changing the amount of blood
loss from inf -> ~40%
- Blood siphon range: 9 tiles -> 6 tiles
- Void Pull: Now affected by antimagic
- Void Phase: Now affected by antimagic

Buffs
- Void Blast cooldown: 60s -> 30s

Other
- Rust Formation now has a "distinct" icon
- Void Blast now has a "distinct" icon

## Why It's Good For The Game

A lot of these spells were extremely oppressive, and made it pretty much
a joke to get away with anything.
They were no-brainer choices, and as a result no one really pathed into
anything else but these.

- Furious Steel: 
- Now that blade heretics have "realignment" in their repertoire, which
offers them another counter for being hit by disablers or batons, this
spell doesn't need to have such an insanely high uptime. The spell
should be used for initiating and obtaining the lead in a combat,
instead of having nigh-invulnerability for most periods.
- Additionally, antimagic protection was kind of missing, which was
partially an oversight of it not being a `/magic` projectile.
 
- Cleave:
- Cleave was by far the most absurd ability available bar none. This
spell was guaranteed death in 30 seconds if the target had no way to
stop the bloodflow immediately. AND it could be casted from across the
screen. This brings cleave's range into midrange between you and the
target, giving a lot more opportunity to be aware for the victim.
- Critical bleed wounds had a negative clotting rate, meaning that prior
you would bleed to 0% from cleave if you didn't stop it. Not very fun,
so with the default clotting rate it now stops at 60% blood flow -
enough to be lethal if untreated, but doesn't completely tap you out
   - **Alternatives**: 
      - Keep the no clotting, make it a pure melee / touch spell. 
      - Reduce the cooldown, make it a projectile
- Change it to be like a cool scythe attack that comes out of the caster
and does a sweep

- Blood Siphon: 
- This was primarily done to slot in better with Cleave's range
decrease, encouraging more close range combat between the two. Getting
point clicked from across the screen isn't fun.

- Void Pull and Phase:
- Largely done for consistency. These are spells which cause damage, so
anti-magic should stop the damage from the spells.

- Void Blast
- I have no idea why I made the cooldown so high on this, 1 minute made
it almost worthless.

TLDR: Instakill click spells from across the screen bad, invulnerability
bad

## Changelog

:cl: Melbert
balance: Heretic: Furious Steel's cooldown has been doubled (30s ->
60s), and abides by antimagic
balance: Heretic: Cleave's cooldown has increased by 5s, range has been
decreased to 4 tiles, and wound applied now has natural clotting
balance: Heretic: Blood Siphon's range has been decreased to 6 tiles
balance: Heretic: Void Pull and Phase abide by antimagic
balance: Heretic: Halved Void Blast's cooldown to 30s
qol: Heretic: Void Blast and Rust Formation now have distinct icons 
/:cl:

---
## [Zonespace27/tgstation](https://github.com/Zonespace27/tgstation)@[9499a1542b...](https://github.com/Zonespace27/tgstation/commit/9499a1542b156eb32efb25e0310b1fe7077caf5c)
#### Wednesday 2023-03-29 01:48:00 by itseasytosee

Corrects error in stamina HUD element display calculation. Increases stamina HUD readability. (#71623)

## About The Pull Request
Stamina was checking health instead of maxHealth. This is probably a
remnant from when the damage stacked.
I stopped the stamina from appearing like you had no stamina whenever
you were stunned or knockdown. This would obscure potentially value
information from the player while being unclear to interpret.
We should probably represent status effects like this to the player, but
through the stamina bar is not a useful method.
The stamina bar is for stamina.
Additionally, the stamina bar will now be greyed out while you are dead,
like your health bar.

I've done alot of work increasing the readability of the stamina bar.
Firstly, I've cut some fat, removing the 100% sign when you are at full
and the blinking exclamation point when you are close to zero. They
aren't nessisary and add clutter.
There's no more "full but because its blinking bright yellow you are
actually at 20% or less" or "empty but because the whole thing isn't
blinking you still have stamina"
Its a now simple meter that decreases in 20% increments which blinks
softly, at darker and more red colors the lower the meter goes, blinking
faster at the higher percentages. When you are at zero, the empty space
slowly glows a dark red.
Its much more reasonable and intuitive than whatever the hell the old
sprites were doing.
## Why It's Good For The Game
For the HUD changes, it improves the game feel, at least from my
experience. We could probably benefit from an entirely new stamina bar
design, but finding the right one is gonna be tricky.
## Changelog
:cl: itseasytosee
fix: Stamina damage display calculation should be much more sane and
reliable now
imageadd: Simplified the stamina hud
/:cl:

---
## [meemofcourse/Shiptest](https://github.com/meemofcourse/Shiptest)@[1c039c0623...](https://github.com/meemofcourse/Shiptest/commit/1c039c0623b6e8af463de0f0b1ca1ccc49050d94)
#### Wednesday 2023-03-29 02:24:18 by Sun-Soaked

Botany Balance Pass (#1783)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
First came the content, now comes the hammer.

- Nukes Megaseed servitors from orbit. 
- Plants now age much, much slower and produce half as quickly.
Ruins that had them now have a ruined seed vendor that can be salvaged
for random seeds(and danger).
Ships that had one now have a crate with some thematic starting seeds,
and a Strange Seed.
Ghostrole Ruins that relied on having all seeds locally now have a
special biogenerator variant that can print a random seed for biomass.

- Adds Genesis Serum. This can be splashed on a tile to make natural
grass and some flora. Green your ship!
Genesis Serum was made a while ago, on request for a way to add natural
grass and flora to your ship. Since I had it lying around fully coded, I
thought I might as well pr it with botany changes.

- Gatfruit found in the seed vault have been replaced with Strange
Seeds.

- The chance to get Gatfruit from a demonic portal(plant variety) has
dropped from 15% to 5%.

- Corpse flowers now have liquid gibs and formaldehyde again. 

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Okay, hear me out

With this and Gardens, botany ships go from a "sit in your vessel for 2
hours" experience to an "explore and forage" one that better fits our
feature arc. It goes without saying that this **shouldn't be merged till
Overmap 4.2 is**, since it facilitates getting seeds from planets as
part of exploration.

Gatfruit are funny, but it takes exactly one seed getting into the hands
of a ship with a dna manipulator and the weapon balance is eradicated
from the game completely(for the round, at least.)
This is more problematic here then it was on TG, since our rounds tend
to be 5 hours long rather then 1.
This has been long coming. I'll reverse this if we ever get that
Plantlock variant we wanted a while ago.

Corpse flowers even have formaldehyde and gibs on tg, not sure what
happened there.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: 
add: Ruined megaseed servitors can now be found on the frontier,
carrying a bounty of seeds for intrepid adventurers.
balance: the time it takes for plants to reach a lethal age has been
increased massively.
balance: Plant production time increased a bit to compensate.
balance: megaseed servitors have been removed from ships and ruins.
Ships that carried one now have a crate with some starting seeds.
balance: removes gatfruit from the seed vault pool.
balance: reduces the chance of getting gatfruit from a plant-themed
demonic portal significantly.
balance: corpse flowers once again have formaldehyde and liquid gibs.
add: Adds Genesis Serum, a reagent that transforms tiles into natural
grass on splash, then causes some natural flora objects to grow. Turn
your ship green!
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[95b810919e...](https://github.com/san7890/bruhstation/commit/95b810919ede0f4fb22dc711c0334abf36b94843)
#### Wednesday 2023-03-29 02:25:06 by lizardqueenlexi

Adds preference for "Tagger" paint color. (#74281)

## About The Pull Request

Per the title, this PR allows you to pick your starting paint color from
the "Tagger" quirk on the character preferences menu.


![image](https://user-images.githubusercontent.com/105025397/227810007-4706c743-31c2-47d8-80ac-e11687d36c00.png)

This replaces the starting color being random; it does not prevent you
from changing the color later as normal.
## Why It's Good For The Game

It's a minor quality of life change. This will mostly be helpful to
players who have some "signature" color they like to use, to prevent
having to manually select it (and possibly input a color code) every
round. It will be of less relevance to those who tend to select new
colors every round anyway.

Possible downsides are mainly adding another pref to the menu, although
this shouldn't be too much of an annoyance since it only appears if you
already have the relevant quirk. It does also remove the _ability_ to
have a randomly-chosen paint color, though I'm not sure if that matters.
## Changelog
:cl:
qol: you can choose your default paint color for the "Tagger" quirk from
prefs.
/:cl:

---
## [Multiple-Forks/optimized-canary](https://github.com/Multiple-Forks/optimized-canary)@[8314f6a3e8...](https://github.com/Multiple-Forks/optimized-canary/commit/8314f6a3e8c3b94242d43d4f754a6fb4fccf6461)
#### Wednesday 2023-03-29 03:10:48 by Spiller

feat: add several missing bosses (#708)

• See the pull request description to read detailed information.

Add bosses from some quests there were not developed. This PR adds only the bosses, levers mechanics for simple functionality.
This doesn't add the bosses mechanics! If someone is willing to contribute with the mechanics, feel free to contribute with the PR.
The bosses added are:

• A pirate's tail: Ratmiral Blackwhiskers, Tentugly's head;
• Adventures of Galthen: Megasylvan Yselda;
• Feaster of Souls: The Fear Feaster, The Unwelcome, The Dread Maiden, Irgix the Flimsy, Unaz the Mean, Vok The Freakish;
• Grave Danger (rework): Lord Azaram, Duke Krule, Count Vlarkorth, Sir Nictros & Sir Baeloc, Earl Osam, King Zelos;
• Grimvale/Ancient Feud: Katex Blood Tongue, Srezz Yellow Eyes, Utua Stone Sting, Yirkas Blue Scales, Bloodback, Darkfang, Sharpclaw, Shadowpelt, Black Vixen;
• Soul War: Goshnar's Cruelty, Goshnar's Greed, Goshnar's Hatred, Goshnar's Malice, Goshnar's Spite, Goshnar's Megalomania;
• The Dream Courts: The Nightmare Beast, Izcandar the Banished, Alptramun, Plagueroot, Malofur Mangrinder, Maxxenius;
• The Secret Library: Ghulosh, Gorzindel, Lokathmor, Mazzinor, Scourge of Oblivion.
• The SoulWar reward was added. In order to get the reward, the player needs to kill all the bosses and the final boss.
• The Dream Court's World change was added.

• All the access needed were granted on FreeQuests.lua. If you are already running a server, you'll need to update freeQuestStage on config.lua to one number higher than it is. So, all the players of your server will have the access granted.

---
## [cysk003/certbot](https://github.com/cysk003/certbot)@[208ef4eb94...](https://github.com/cysk003/certbot/commit/208ef4eb942c7129dd265632de740ed1fab53c98)
#### Wednesday 2023-03-29 03:22:02 by Brad Warren

remove CERTBOT_NO_PIN (#9634)

Adrien and I added this is in https://github.com/certbot/certbot/pull/6590 in response to https://github.com/certbot/certbot/issues/6582 which I wrote. I now personally think these tests are way more trouble than they're worth.

In almost all cases, the versions pinned in `tools/requirements.txt` are used. The two exceptions to this that come to mind are users using OS packages and pip. In the former, the version of our dependencies is picked by the OS and do not change much on most systems. As for pip, [we only "support it on a best effort basis"](https://eff-certbot.readthedocs.io/en/stable/install.html#alternative-2-pip).

Even for pip users, I'm not convinced this buys us much other than frequent test failures. We have our tests configured to error on all Python warnings and [we regularly update `tools/requirements.txt`](https://github.com/certbot/certbot/commits/master/tools/requirements.txt). Due to that, assuming our dependencies follow normal conventions, we should have a chance to fix things in response to planned API changes long before they make their way to our users. I do not think it is necessary for our tests to break immediately after an API is deprecated.

I think almost all other failures due to these tests are caused by upstream bugs. In my experience, almost all of them will sort themselves out pretty quickly. I think that responding to those that are not or planned API changes we somehow missed can be addressed when `tools/requirements.txt` is updated or when someone opens an issue. I personally don't think blocking releases or causing our nightly tests to fail is at all worth it here. I think removing this frequent cause of test failures makes things just a little bit easier for Certbot devs without costing us much of anything.

---
## [StevenDoesStuffs/nushell](https://github.com/StevenDoesStuffs/nushell)@[0567407f85...](https://github.com/StevenDoesStuffs/nushell/commit/0567407f853c23f54215020a10f4a831ae2aef47)
#### Wednesday 2023-03-29 03:38:31 by Antoine Stevan

standard library: bring the tests into the main CI (#8525)

Should close one of the tasks in #8450.

# Description
> **Note**
> in order of appearance in the global diff

- 1b7497c41966306aa3103a95a9b5ef5df7111ee4 adds the `std-tests` job to
the CI which
  1. installs `nushell` in the runner
  2. run the `tests.nu` module
> see `open .github/workflows/ci.yml | get jobs.std-tests | to yaml`

-
[`ec85b6fd`..`9c122115`](ec85b6fd3fc004cd94e3fada5c8e5fe2714fd629..9c12211564ca8ee90ed65ae45776dccb8f8e4ef1)
is where all the magic happens => see below
- :test_tube: 799c7eb7fd5f140289b36b9dbc00329c50e2fbda introduces some
bugs and failing test to see how the CI behaves => see how the [tests
failed](https://github.com/nushell/nushell/actions/runs/4460098237/jobs/7833018256)
as expected :x:
- :test_tube: and c3de1fafb5c5313e30c08c9ca57e09df33b61b74 reverts the
failing tests, i.e. the previous commit, leaving a standard library
whose tests all pass :tada: => see the [tests
passing](https://github.com/nushell/nushell/actions/runs/4460153434/jobs/7833110719?pr=8525#step:5:1)
now :heavy_check_mark:

## the changes to the runner
> see
[`ec85b6fd`..`9c122115`](ec85b6fd3fc004cd94e3fada5c8e5fe2714fd629..9c12211564ca8ee90ed65ae45776dccb8f8e4ef1)

the issue with the previous runner was the following: the clever trick
of using `nu -c "use ...; test"` did print the errors when occuring but
they did not capture the true "failure", i.e. in all cases the
`$env.LAST_EXIT_CODE` was set to `0`, never stopping the CI when a test
failed :thinking:

i first tried to `try` / `catch` the error in
ec85b6fd3fc004cd94e3fada5c8e5fe2714fd629 which kinda worked but only
throw a single error, the first one

i thought it was not the best and started thinking about a solution to
have a complete report of all failing tests, at once, to avoid running
the CI multiple times!

the easiest solution i found was the one i implemented in
9c12211564ca8ee90ed65ae45776dccb8f8e4ef1
> **Warning**
> this changes the structure of the runner quite a bit, but the `for`
loops where annoying to manipulate structured data and allow the runner
to draw a complete report...

now the runner does the following
- compute the list of all available tests in a table with the `file`,
`module` and `name` columns (first part of the pipe until `flatten` and
`rename`)
- run the tests one by one computing the new `pass` column
  - with a `log info`
- captures the failing ones => puts `true` in `pass` if the test passes,
`false` otherwise
- if at least one test has failed, throw a single error with the list of
failing tests

### hope you'll like it :relieved: 

# User-Facing Changes
```
$nothing
```

# Tests + Formatting
the standard tests now return a true error that will stop the CI

# After Submitting
```
$nothing
```

---
## [Enbyy/orbstation](https://github.com/Enbyy/orbstation)@[8d7db532c0...](https://github.com/Enbyy/orbstation/commit/8d7db532c0f425e6cc68d975b526694bbaefc870)
#### Wednesday 2023-03-29 04:25:31 by Bloop

Reworks blood deficiency backend, & some adjustments to slime blood deficiency (#74143)

## About The Pull Request

This is a followup PR to
https://github.com/tgstation/tgstation/pull/73866

Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/19991

I had suspected the nutrition loss slimes experience alongside blood
regen might necessitate some tweaks down the line and here we are. This
PR has two parts.

---

**PART I:** _Reworking the blood deficiency quirk backend_

As it is, blood drain from the blood deficiency occurs in the quirk's
subsystem process() call asynchronously to Life(), where the blood regen
occurs.

This results in the blood volume fluctuating constantly, making it
difficult to really make sense of readings and potentially introducing
race conditions. This PR changes that.

The blood deficiency quirk no longer processes and instead has a proc,
`lose_blood(delta_time)`, which is called in the `handle_blood()` proc
at the same time blood gets regenerated.

Added a `get_quirk` proc to help with this, so that we only have to
iterate through the quirks list once for each mob (rather than calling
has_quirk, then locate in quirks... etc).

Added a `TRAIT_BLOOD_DEFICIENCY` to further optimize the code.

---

**PART II:** _Some fine tuning of the slime blood deficiency quirk_

Slime regen works a bit differently than humans such that if they lose
-any- blood whatsoever, they will also lose nutrition. This means that
even if hooked up to an IV they will still become starving rather
quickly. A bit -too- quickly.

Instead, now the hunger does not kick in until `blood_volume` reaches
550. This means that if a slime with the blood deficiency quirk is
hooked up to an IV with say, welding fluid, and has over 150 nutrition,
they will regen blood faster than they lose it from the blood deficiency
quirk. Once they get to over 550 `blood_volume`, they will stop losing
hunger (from blood regen, anyway--normal hunger rate still applies).

So essentially this just allows slimes with the blood deficiency quirk
to be able to function so long as they stay hooked up to their IV's (or
chug welder fluid/some other toxin), which is the intended purpose of
the quirk.

Edit: As a bonus I added new blood bags for the exotic blood types, and
added a proc `update_mail_goodies` which updates the blood deficiency
quirk's mail goodies accordingly (crewmembers with blood deficiency get
sent blood bags, now they will get the correct type if their species
changes). While I was in these files I changed any immediate single
letter vars I could find and cleaned up what I could.


![image](https://user-images.githubusercontent.com/13398309/226739179-a21790e3-0be6-423a-be89-8d2cb84f6149.png)


<details>
<summary>The new blood packs</summary>


![image](https://user-images.githubusercontent.com/13398309/226743543-29fca53d-b3d1-4903-9706-35b2c00bbe78.png)

</details>

## Why It's Good For The Game

-This is arguably a more performant option than before, and fixes race
conditions from `Life()` and `quirk/blooddeficiency/process()` fighting
with one another.

-Adjustments to slime blood deficiency will enable it to function as
intended.

-It is now easier to read health analyzer blood volume readings for
blood deficient mobs.

-Now the correct blood packs are sent in the mail.

## Changelog

:cl:
qol: adjusted the blood deficiency quirk for slimepeople to not cause
excessive hunger as long as blood volume is kept above 550 via an IV
drip (or other means of getting welding fluid/some other toxin etc into
the bloodstream, e.g. ingestion)
qol: speciees with exotic blood types will now receive the correct blood
bag in the mail from having the blood deficiency perk
add: adds new blood bag types: TOX (slimepeople), H2O (podpeople), S
(snail)
fix: fixed blood deficiency quirk causing wild fluctuations in blood
volume on the analyzer, giving more accurate readings
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [erikarn/sdcc-cpm](https://github.com/erikarn/sdcc-cpm)@[c07c0c804d...](https://github.com/erikarn/sdcc-cpm/commit/c07c0c804d554f13c9fa5578eefd2c9d0e23ebbd)
#### Wednesday 2023-03-29 04:38:25 by Adrian Chadd

big editor updates!

* remove the left screen col stuff for now, I don't know if i want
  to wrap or move the window over.  For now i'll clamp line lengths
  at the viewport size (and will need to do this during file load)
  and worry about how to edit longer lines (or not!) later.

* implement working cursor up, down, left, right, clamping cursor x
  at the correct string length.

* print a blank space to overwrite a ~ if the line created but blank.

* /correctly/ use the viewport size when rendering the text page
  and doing the cursor / line position math.  It's a 90x32 screen,
  the bottom line is a status line for CPM/PCW.
  So it's a 90x31 screen, and we're using 90x30 for the screen
  and the last line as the command line.

This .. actually works.  I mean, xjoyce's keyboard on freebsd is
slow and misses a lot of key presses (I wish I knew why!), but
I can fill up a whole lot of lines and it'll correctly scroll
up and down, updating the cursor position / clamping things
appropriately.

Now, actually implementing the basic editor commands (i, dd, a,
x, :<line>, <num><cmd> like 10dd, etc, etc.)  Oh yeah and
saving/loading text files, haha!

---
## [walternewtz/android_kernel_xiaomi_sdm845](https://github.com/walternewtz/android_kernel_xiaomi_sdm845)@[36b03e73b4...](https://github.com/walternewtz/android_kernel_xiaomi_sdm845/commit/36b03e73b4c62dfcf5f19e504b7b6abb1dd6ce82)
#### Wednesday 2023-03-29 04:51:57 by tanish2k09

Introducing KLapse - A kernel level livedisplay module v4.0:

Author: @tanish2k09 (email: tanish2k09.dev@gmail.com)

What is it?
Kernel-based Lapse ("K-Lapse") is a linear RGB scaling module that 'shifts' RGB based on time (of the day/selected by user), or (since v2.0) brightness. This concept is inspired from
LineageOS (formerly known as 'CyanogenMod') ROM's feature "livedisplay" which also changes the display settings (RGB, hue, temperature, etc) based on time.

Why did you decide to make this? (Tell me a story).
I (personally) am a big fan of the livedisplay feature found on LineageOS ROM. I used it every single day, since Android Lollipop. Starting from Android Nougat, a native night mode
solution was added to AOSP and it felt like livedisplay was still way superior, thanks to its various options (you could say it spoiled me, sure). I also maintained a kernel (Venom
kernel) for the device I was using at that time. It was all good until the OEM dropped support for the device at Android M, and XDA being XDA, was already working on N ROMs. The issue
was, these ROMs weren't LineageOS or based on it, so livedisplay was... gone. I decided I'll try to bring that feature to every other ROM. How would I do that? Of course! The kernel! It
worked on every single ROM, it was the key! I started to work on it ASAP and here it is, up on GitHub, licensed under GPL (check klapse.c), open to everyone :)

How does it work?
Think of it like a fancy night mode, but not really. Klapse is dependent on an RGB interface (like Gamma on MTK and KCAL on SD chipsets). It fetches time from the kernel, converts it to
local time, and selects and RGB set based on the time. The result is really smooth shifting of RGB over time.

How does it really work (dev)?
Klapse mode 1 (time-based scaling) uses a method void klapse_pulse(void) that should ideally be called every minute. This can be done by injecting a pulse call inside another method that
is called repeatedly naturally, like cpufreq or atomic or frame commits. It can be anything, whatever you like, even a kthread, as long as it is called repeatedly naturally. To execute
every 60 seconds, use jiffies or ktime, or any similar method. The pulse function fetches the current time and makes calculations based on the current hour and the values of the tunables
listed down below.

Klapse mode 2 (brightness-based scaling) uses a method void set_rgb_slider(<type> bl_lvl) where is the data type of the brightness level used in your kernel source. (OnePlus 6 uses u32
data type for bl_lvl) set_rgb_slider needs to be called/injected inside a function that sets brightness for your device. (OnePlus 6 uses dsi_panel.c for that, check out the diff for that
file in /op6)

What all stuff can it do?

1, Emulate night mode with the proper RGB settings
2, Smoothly scale from one set of RGB to another set of RGB in integral intervals over time.
3, Reduce perceived brightness using brightness_factor by reducing the amount of color on screen. Allows lower apparent brightness than system permits.
4, Scale RGB based on brightness of display (low brightness usually implies a dark environment, where yellowness is probably useful).
5, Automate the perceived brightness independent of whether klapse is enabled, using its own set of start and stop hours.
6, Be more efficient,faster by residing inside the kernel instead of having to use the HWC HAL like android's night mode.
7, (On older devices) Reduce stuttering or frame lags caused by native night mode.
8, An easier solution against overlay-based apps that run as service in userspace/Android and sometimes block apps asking for permissions.
9, Give you a Livedisplay alternative if it doesn't work in your ROM.
10, Impress your crush so you can get a date (Hey, don't forget to credit me if it works).

Alright, so this is a replacement for night mode?
NO! Not at all. One can say this is merely an alternative for LineageOS' Livedisplay, but inside a kernel. Night mode is a sub-function of both Livedisplay and KLapse. Most comparisons
here were made with night mode because that's what an average user uses, and will relate to the most. There is absolutely no reason for your Android kernel to not have KLapse. Go ahead
and add it or ask your kernel maintainer to. It's super-easy!

What can it NOT do (yet)?

1, Calculate scaling to the level of minutes, like "Start from 5:37pm till 7:19am". --TODO
2, Make coffee for you.
3, Fly you to the moon. Without a heavy suit.
4, Get you a monthly subscription of free food, cereal included.

All these following tunables are found in their respective files in /sys/klapse/

1. enable_klapse : A switch to enable or disable klapse. Values : 0 = off, 1 = on (since v2.0, 2 = brightness-dependent mode)
2. klapse_start_hour : The hour at which klapse should start scaling the RGB values from daytime to target (see next points). Values : 0-23
3. klapse_stop_hour : The hour by which klapse should scale back the RGB values from target to daytime (see next points). Values : 0-23
4. daytime_rgb : The RGB set that must be used for all the time outside of start and stop hour range.
5. target_rgb : The RGB set that must be scaled towards for all the time inside of start and stop hour range.
6. klapse_scaling_rate : Controls how soon the RGB reaches from daytime to target inside of start and stop hour range. Once target is reached, it remains constant till 30 minutes before
   stop hour, where target RGB scales back to daytime RGB.
7. brightness_factor : From the name itself, this value has the ability to bend perception and make your display appear as if it is at a lesser brightness level than it actually is at.
   It works by reducing the RGB values by the same factor. Values : 2-10, (10 means accurate brightness, 5 means 50% of current brightness, you get it)
8. brightness_factor_auto : A switch that allows you to automatically set the brightness factor in a set time range. Value : 0 = off, 1 = on
9. brightness_factor_auto_start_hour : The hour at which brightness_factor should be applied. Works only if #8 is 1. Values : 0-23
10. brightness_factor_auto_stop_hour : The hour at which brightness_factor should be reverted to 10. Works only if #8 is 1. Values : 0-23
11. backlight_range : The brightness range within which klapse should scale from daytime to target_rgb. Works only if #1 is 2. Values : MIN_BRIGHTNESS-MAX_BRIGHTNESS

Signed-off-by: Eliminater74 <eliminater74@gmail.com>
Signed-off-by: energyspear17 <energyspear17@gmail.com>
Signed-off-by: Michael <loukerismichalis@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>

---
## [Singul0/tgstation](https://github.com/Singul0/tgstation)@[40fc11eb07...](https://github.com/Singul0/tgstation/commit/40fc11eb0733ca25eff56e7379cb574a997fb6d3)
#### Wednesday 2023-03-29 05:16:31 by LemonInTheDark

Optimizes some gas_mixture procs, Optimizes pipeline processing significantly by 33% (#74233)

## About The Pull Request
It is faster to operate on a gas list, especially if cached, then it is
to operate on a datum.
Doing this cause I'm seeing cost in merge() post #74230

Hits on a few other important places too. self_breakdown and such. Worth
it IMO

Could in theory go further by caching the global list. I'm tempted I
admit but it needs profiling first and it's late

EDIT: I have not slept, and have gone tooo far

[Micros /gas_mixture/copy and copy_from, adds a new proc to handle
copying with a ratio,
copy_from_ratio](https://github.com/tgstation/tgstation/pull/74233/commits/91da0003daa9485962525d3e6bc9170a4c09876b)

[91da000](https://github.com/tgstation/tgstation/pull/74233/commits/91da0003daa9485962525d3e6bc9170a4c09876b)

The ADD_GAS sidestep saves us 0.1 seconds of init (used to at least.
Ensuring we don't break archive is gonna have a cost. I don't want to
profile this so I'll estimate maybe 0.05 seconds). The faster version of
copy_from is just well, better, and helps to avoid stupid

[Optimizes pipeline
processing](https://github.com/tgstation/tgstation/pull/74233/commits/bf5a2d2d60554da2ce5fa1ac5f6c4179f6208cb2)

[bf5a2d2](https://github.com/tgstation/tgstation/pull/74233/commits/bf5a2d2d60554da2ce5fa1ac5f6c4179f6208cb2)

I haven't slept in 36 hours. Have some atmos optimizations

Pipelines now keep track of components that require custom
reconciliation as a seperate list.
This avoids the overhead of filtering all connected atmos machinery.

Rather then relying on |= to avoid duplicate gas_mixtures, we instead
use a cycle var stored on the mix itself, which is compared with a
static unique id from reconcile_air()
This fully prevents double processing of gas, and should (hopefully)
prevent stupid dupe issues in future

Rather then summing volume on the gas mixture itself, we sum it in a
local var.
This avoids datum var accesses, and saves a slight bit of time

Instead of running THERMAL_ENERGY() (and thus heat_capacity(), which
iterates all gases in the mix AGAIN) when processing gas, we instead
just hook into the existing heat capacity calculation done inside the
giver gases loop
This saves a significant amount of time, somewhere around 30% of the
proc, I think?

This doesn't tackle the big headache here, which is the copy_from loop
at the base of the proc.

I think the solution is to convert pipelines to a sort of polling model.
Atmos components don't "own" their mix, they instead have to request a
copy of it from the pipeline datum.
This would work based off a mutually agreed upon volume amount for that
component in that process cycle.

We'd use an archived system to figure out what gases to give to
components, while removing from the real MOLES list.

We could then push gas consumption requests to the pipeline, which would
handle them, alongside volume changes, on the next process.

Not sure how I'd handle connected pipelines... Merging post reconcile
maybe?
This is a problem for tomorrow though, I need to go to bed.

Saves about 30% of pipeline costs.
Profiles taken on kilo, until each reconcile_air hits 5000 calls

[old.txt](https://github.com/tgstation/tgstation/files/11075118/Profile.results.total.time.txt)

[new.txt](https://github.com/tgstation/tgstation/files/11075133/profiler.txt)

---
## [necromanceranne/tgstation](https://github.com/necromanceranne/tgstation)@[a6f49ed542...](https://github.com/necromanceranne/tgstation/commit/a6f49ed54255f9a8d4dfc27bc397e56f87029cb8)
#### Wednesday 2023-03-29 06:15:05 by san7890

Refactors Suiciding Variable Into Trait (#74150)

## About The Pull Request

Firstly, this var was on `/mob`, even though only `/mob/living` and
`/mob/dead` could have ever used it, so who knows how much needless
memory it was consuming on stuff such as `oranges_ear` that would never
ever ever use something like this.

Edit: okay instead of memory it just polluted variable edit windows for
all /mob when it didn't need to. I like having a slim VV window

Secondly, it's a technical improvement over the previous system as we
are able to "track" where a suicide originates from, and how we can
track that from mob-to-mob-to-mob. Previously, the boolean `suiciding`
would only inform us if they had ever been connected to a mob that had
ever committed suicide, but now we are able to precisely determine which
mob gave them the trait that they must now apparently bear until the
round restarts.

## Why It's Good For The Game

Less memory usage, more indepth ability to track suicides in case you
really need that dexterity. Currently no implemented code could benefit
from using it, but it would be pretty neat if someone could figure out a
way to have someone be guilt-tripped whenever they look into a mirror
and seeing the reflection of their past life? This PR won't actually
help you code that and it'll probably require a bit more work, but it's
a possibility of some cool interactions you can do when you have this
information available to you.


![image](https://user-images.githubusercontent.com/34697715/226506321-550c37e7-5de8-4f9f-9ceb-4bf9b1052597.png)

## Changelog

:cl:
refactor: Some aspects of how we track suicides from your living mob to
your observer have changed- please do let us know if anything has broken
via a GitHub Issue Report.
/:cl:

There's probably some technical improvements that can be made in some
parts of the code I reworked to accommodate this change, do let me know
if you spot any easy ones (or fuckups). a lot of excess comes from the
fact that any step in the TRAIT framework trusts that you are passing in
a valid datum (or subtype) so that's a thing

---
## [andylouisqin/evals](https://github.com/andylouisqin/evals)@[ab5f7b2a89...](https://github.com/andylouisqin/evals/commit/ab5f7b2a89bcf60e8e93adfb2c70688c6d6ffd44)
#### Wednesday 2023-03-29 06:57:17 by oscar-king

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
## [andylouisqin/evals](https://github.com/andylouisqin/evals)@[b170a21cf3...](https://github.com/andylouisqin/evals/commit/b170a21cf32c47d841f64ec110cfd6796ec3f89a)
#### Wednesday 2023-03-29 06:57:17 by Sam Ennis

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
## [andylouisqin/evals](https://github.com/andylouisqin/evals)@[b5da073c21...](https://github.com/andylouisqin/evals/commit/b5da073c215c6453b99269a6dab2dca5454f04dd)
#### Wednesday 2023-03-29 06:57:17 by somerandomguyontheweb

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
## [ungchun/MC1_ReturnTrue](https://github.com/ungchun/MC1_ReturnTrue)@[755f5e27cf...](https://github.com/ungchun/MC1_ReturnTrue/commit/755f5e27cf27c6d555c3b71cb8702aced88b43ee)
#### Wednesday 2023-03-29 07:32:32 by UIMAPH

Merge pull request #8 from samilulu/main

fuck you ok

---
## [nikolay-1986/Pushkin_repo](https://github.com/nikolay-1986/Pushkin_repo)@[e8636aed98...](https://github.com/nikolay-1986/Pushkin_repo/commit/e8636aed980a76ce968f7c3371216d8fa74c572d)
#### Wednesday 2023-03-29 07:38:46 by Nikolay Myasnikov

A. S. Pushkin. Story of the late Ivan Petrovich Belkin                   SNOWSTORM                             The horses are racing on the hill          Treading the snow deep...          This is the Church of God          You can see alone.          Suddenly there’s a blizzard around;          Snow falls in pieces;          Black wrath, wing whistle,          Hovering over the sleigh;          The prophetic groan says sadness!          The horses are in a hurry          Looking gently into the dark far away          The flying manes of...                            Zhukovsky.  At the end of 1811, in an epoch worthy of remembrance, lived in his manor Neradov good Gavrila R **. He was known throughout the district for his hospitality and hospitality; his neighbours went to his house minute by minute to eat, drink, play five kopecks in Boston with his wife, and some to see their daughter, Marya Gavrilovna, a slender, pale and seventeen-year-old girl. She was considered a rich bride, and many read her for themselves or for their sons. Maria Gavrilovna was raised in French novels and was curiously in love. The object she had chosen was a poor army ensign on vacation in his village. It goes without saying that the young man was in a blaze of passion, and that his parents, being kind enough to notice their mutual inclination, forbade his daughter to think about him and he was accepted worse than a retired juror. Our lovers were in correspondence, and every day we saw each other alone in a pine grove or at the old chapel. There they swore to each other eternal love, lamented their fate and made various assumptions. By texting and talking in this way, they (quite naturally) have reached the following conclusion: if we cannot breathe without each other, and the will of cruel parents hinders our well-being, can we do without it? Of course, this happy idea first came to the young man’s mind and that the romantic imagination of Marya Gavrilovna liked it very much. Winter came and stopped their visits, but the correspondence became more lively. Vladimir Nikolayevich, in every letter, begged her to give herself to him, to marry secretly, to hide for some time, then to throw themselves at their parents' feet, who of course will be touched at last by the heroic constancy and unhappiness of lovers and will say to them, Children! come into our arms». Marya Gavrilovna hesitated for a long time; many plans to escape were rejected. Finally she agreed: on the appointed day she had to stop eating and retire to her room under the pretext of a headache, her girlfriend was in a plot; both they had to go out into the garden through the back porch, behind the garden to find a ready sleigh, to sit in them and go five versts from Neradov to the village of Zhadrino, right to the church, where Vladimir should have expected them. On the eve of a resolute day Marya Gavrilovna did not sleep all night; she was tucked in, tied underwear and dress, wrote a long letter to one sensitive young lady, her friend, another to her parents. She said farewell to them in the most touching terms, apologized for her transgression by the irresistible power of passion, and ended up honoring the blessed minute of her life when she was allowed to throw herself at the feet of her dearest parents. After sealing both letters with the Tula seal, which showed two blazing hearts with a decent inscription, she threw herself on the bed just before dawn and dozed off; but even then the dreadful dreams awakened her minute by moment. It seemed to her that the minute she sat down in the sleigh to go to the wedding, her father stopped her, dragged her through the snow and threw her into a dark, bottomless dungeon... and she flew swiftly with an unexplained heart; she saw Vladimir, lying on the grass, pale and bloody.  He, dying, begged her to hurry to marry him... other ugly, senseless visions rushed before her one by one. She finally stood up, paler than usual and with an unattractive headache. Father and mother noticed her anxiety; their tender care and incessant questions: What is with you, Masha? Are you not ill, Masha? - Her heart was torn. She tried to calm them down, to seem cheerful, and could not. It was evening. The thought of the last time she spent a day in the middle of her family had put a strain on her heart. She was barely alive; she was secretly saying goodbye to all the individuals, all the objects around her. They gave her dinner; her heart was racing. In a trembling voice, she announced that she did not want to have dinner, and began to say goodbye to her father and mother. They kissed her and, as usual, blessed her: she almost cried. When she came to her room, she rushed into the chairs and poured tears. The girl talked her to calm down and cheer up. Everything was ready. In half an hour, Masha was to leave her parents' house, her room, her quiet maiden life forever... There was a blizzard in the yard; the wind was howling, shutters were shaking and knocking; everything seemed to her a threat and a sad omen. Soon everything in the house was quiet and fell asleep. Masha was wrapped in a shawl, put on a warm hood, took her box in her hands and went out on the back porch. The maid was carrying two knots behind her. They went down into the garden. The snowstorm did not subside; the wind was blowing towards them, as if to stop the young criminal. They had reached the end of the garden. On the road the sleigh was waiting for them. The horses did not stand still; Vladimir’s coachman was pacing before the tall men, holding the eager ones. He helped the young lady and her girlfriend sit down and lay down the knots and the box, took the reins, and the horses flew. Having entrusted the young lady with the care of fate and art of Teresa coachman, we turn to our young lover.  Vladimir was on the road all day. In the morning he went to the priest of the Jadrin; he made an agreement with him; then he went to look for witnesses between neighboring landowners. The first to whom he came, the retired 40-year-old cornet Dravin, agreed to hunt. This adventure, he said, reminded him of the old times and the Hussars' leprosy. He persuaded Vladimir to stay and dine with him and assured him that the other two witnesses would not be involved. In fact, immediately after lunch, the surveyor Schmidt, in his moustache and spurs, and the son of the Captain-Attendant, a boy of about sixteen years old, had recently entered the lancers. They not only accepted Vladimir’s offer, but even swore to him that he would sacrifice his life. Vladimir hugged them with delight and went home to prepare himself. It’s been dark for a while. He sent his trusty Tereshka to Nevradovo with his threesome and with detailed, detailed instructions, but for himself ordered to put the small sleigh in one horse, and one without a coachman went to Zhadrino, where Marya Gavrilovna was supposed to come in two hours. The road was familiar to him, and the drive was only twenty minutes. But as soon as Vladimir went beyond the trench in the field, the wind rose and there was such a blizzard that he saw nothing. In a moment the road drifted away; the neighborhood vanished in a cloudy and yellowish haze through which white flakes flew, the sky slipping to the ground. Vladimir found himself in the field and in vain wanted to get on the road again; the horse stepped at random and minute by minute it rose to the snow, then fell into the pit; the sleigh tipped by minute. Vladimir tried only not to lose the real direction. But it seemed to him that more than half an hour had passed, and he did not reach the Zhadrinskaya grove. About ten minutes had passed. Nothing could be seen in the grove. Vladimir rode a field crossed by deep ravines. The snow-storm did not subside, the sky was not clear. The horse was getting tired, and the sweat was raining down on him, even though he was weeping in the snow. At last he saw he was going the wrong way. Vladimir stopped: he began to think, to remember, to think - and was sure to take him to the right. He drove right. His horse walked a little. He had been on the road for over an hour. Jadrino should have been nearby. But he was driving, he was driving, and there was no end to the field. All the snowdrifts and ravines; the sleigh rolled over minute by minute, he lifted them up. Time was passing; Vladimir began to worry very much. At last something turned black in the side. Vladimir turned there. Approaching, he saw a grove. Thank God, he thought, now close. He rode about the grove, hoping immediately to get to the familiar road or to go round the grove: The Zhadrino was immediately behind her. Soon he found the road and rode into the gloom of trees naked in winter. The wind could not rage there; the road was smooth; the horse was cheerful, and Vladimir was at peace. But he was driving, driving, and Jadrin could not see; there was no end to the grove. Vladimir saw with horror that he had come to an unfamiliar forest. Despair gripped him. He struck the horse; the poor animal went trotting, but soon it began to molest, and after a quarter of an hour it took a step despite all the efforts of the poor Vladimir. Little by little the trees began to thin, and Vladimir rode out of the forest; Jadrin could not be seen. It must have been around midnight. Tears splashed out of his eyes; he rode off at random. The weather subsided, the clouds dispersed, and before him lay a plain lined with a white wavy carpet. The night was pretty clear. He saw a village not far away, consisting of four or five yards. Vladimir went to her. At the first hut he jumped out of the sleigh, ran to the window and began to knock. After a few minutes the wooden shutter rose, and the old man poked out his gray beard. «What do you want?» - «Is Jadrino far?» -- «Is it far away?» - «Yes, yes! Is it far?» - «Not far; a mile will be a dozen». With this answer, Vladimir grabbed himself by the hair and remained stationary as a man sentenced to death.  «And what about you?» continued the old man. Vladimir didn’t have the courage to answer the questions. «Can you, old man, - he said - get me horses to Zhadrin?» -» - «We have horses», said the man. «Can’t I even take a guide? I will pay as much as he pleases». - «Wait, said the old man, lowering the shutter, I will send those son out; he spends them». Vladimir began to wait. Within a minute, he began to knock again. Staven has risen, beard has shown itself. «What do you want?» - «What is your son?» - «Now stands out, shoes. Did you languish? Climb to get warm». - Thank you, send your son. The gates were clogged; the guy came out with a club and went forward, pointing then looking for a road covered with snow drifts. «What time is it?» - Vladimir asked him. «Yes, he will soon», answered the young man. Vladimir did not say a word. The cocks sang, and it was already bright as they reached Jadrina. The church was locked. Vladimir paid a guide and went to the yard to the priest. He wasn’t there. What news awaited him! But let’s go back to the good non-Nradov landowners and see what they’re doing. And nothing. The old people woke up and went into the living room. Gavrila Gavrilovich in a hat and a bike jacket. Praskovya Petrovna in a slatted cotton wool. The samovar was served, and Gavrila Gavrilovich sent the girl to find out from Marja Gavrilovna what her health was and how she was sleeping. The girl turned back, declaring that the young lady had had a bad feeling, but that she was relieved now and that she was coming to the living room. In fact, the door opened and Marya Gavrilovna came to greet her father and mother. «What is your head, Masha?» - asked Gavrila Gavrilovich». «Better, Papa», - said Masha. «You are right, Masha, last night you were drunk», - said Praskovya Petrovna. «Maybe a mother», - said Masha. The day passed smoothly, but on the night Masha fell asleep. They sent to the city for a doctor. He came to the evening and found the patient in delirium. There was a severe fever, and the poor patient was at the edge of the coffin for two weeks. No one in the house knew about the alleged escape. The letters she had written the day before had been burned; her maid had told no one, fearing the wrath of the masters. A priest, a retired cornet, a mustached surveyor, and a small lancer were modest, and not without reason. Tereshka coachman never said anything superfluous, even in hops. Thus, the mystery was kept by more than half a dozen conspirators. But Marya Gavrilovna herself, in endless delirium, expressed her secret. But her words were so incongruous with nothing that the mother, who had not departed from her bed, could only understand from them that her daughter was deathly in love with Vladimir Nikolayevich and that love was probably the cause of her illness. She consulted with her husband, with some of her neighbors, and finally everyone decided unanimously that this was the fate of Marya Gavrilovna, that the intended horse could not get around, that poverty was not a vice, that to live not with wealth, but with a man, and the like. Moral sayings are surprisingly useful when we can invent little from ourselves to justify ourselves. Meanwhile, the young lady began to recover. Long ago, Vladimir was not seen in the house of Gavrilovich. He was frightened by the usual technique. They sent for him and declared to him an unexpected happiness: consent to marriage. But how astonishing was the surprise of the non-Dado landowners when they received a half-mad letter from him in response to their invitation! He declared to them that his foot would never be in their house, and begged them to forget the unhappy man for whom death remained the only hope. A few days later they learned that Vladimir had left for the army. It was in 1812. For a long time, do not dare to announce this healing Masha. She never mentioned Vladimir. A few months later, we found his name among the distinguished and seriously wounded near Borodino, she fainted, and feared that her fever would not return. However, thank God the fainting had no consequences. Another sadness visited her: Gavrila Gavrilovich died, leaving her heiress to the entire estate. But the inheritance did not comfort her; she shared the sincere sorrow of poor Praskovya Petrovna, vowed never to part with her; both of them left Neradovo, the place of sad memories, and went to live in the *****estate. The bridegroom was circling around the lovely and rich bride, but she gave no one the slightest hope. Her mother sometimes persuaded her to choose a friend; Marya Gavrilovna shook her head and thought. Vladimir no longer existed: he died in Moscow, on the eve of the French entry. His memory seemed sacred to Mary; at least she kept everything that could remind her of him: books, his drawings, notes, and poems written for her. Neighbors, having learned about everything, marveled at her constancy and with curiosity expected the hero, who should finally triumph over the sad loyalty of this virgin Artemisa. Meanwhile, the war of glory was over. Our regiments were returning from abroad. The people fled to meet them. Music played conquered songs: Vive Henri-Quatre 1, Tyrolean waltzes and arias from Joconde. The officers, who had gone on a crusade almost as young men, returned, stirring in the raging air, bound with crosses. The soldiers were chatting happily among themselves, intermittently with German and French words. The time is unforgettable! A time of glory and delight! How hard the Russian heart beat at the word fatherland! How sweet were the tears of a date! With what unanimity we united the feelings of national pride and love for the Tsar! And for him, what a minute was! The women, the Russian women, were wonderful then. The ordinary coldness of them disappeared. Their delight was truly exhilarating, when, when they met the victors, they shouted: yay! And they threw bonnets in the air. Which of the officers at the time won’t admit that the Russian woman owed him the best, most precious reward.  During this brilliant time Maria Gavrilovna lived with her mother in the *** province and did not see how both capitals celebrated the return of troops. But in counties and villages, the general enthusiasm may have been even stronger. The appearance of an officer in these places was a real celebration for him, and the lover in the tailcoat was not well in his neighborhood. We have already said that despite its coldness, Maria Gavrilovna was still surrounded by the seekers. But all should have retreated when the wounded Hussar colonel Burmin appeared in her castle, with George in a loop and with an interesting paleness, as the young ladies there said. He was about twenty-six years old. He came on vacation to his estates near the village of Marya Gavrilovna. Marya Gavrilovna was very different from him. With him, her usual thoughtfulness was animated. She could not be said to flirt with him; but the poet, noticing her behavior, would say: Se amor non è, che dunque?.. 2 Burmin was really a very nice young man. He had exactly the kind of mind that women like: the mind of decency and observation, without pretensions and lightly mocking. His behavior with Marya Gavrilovna was simple and free; but whatever she said or did, his soul and eyes followed her. He seemed to have a quiet and humble temper, but the rumor was that he was once a terrible hanger, and it did not harm him in the opinion of Marya Gavrilovna, who (like all young ladies in general) gladly apologized for pranks showing courage and ardent character. But most of all... (more his tenderness, more pleasant conversation, more interesting paleness, more bandaged hands) the silence of the young hussar most of all encouraged her curiosity and imagination. She could not help admitting that he liked her very much; perhaps he, with his intelligence and experience, could have already noticed that she was distinguishing him: how had she not yet seen him at her feet and heard his confession? What was holding him?  shyness, inseparable with true love, pride Is the flirtation of cunning red tape? It was to her a mystery. After thinking carefully, she decided that shyness was the only reason, and put more attentiveness and, depending on the circumstances, even tenderness to encourage him. She was suggestive of the most unexpected ending, and she looked forward to a moment of romance. Mystery, whatever its kind, is always a burden to the woman’s heart. Her military action had the desired success: at least Burmin fell into such contemplation, and his black eyes with such fire halted on Marja Gavrilovna that a decisive moment seemed at hand. Neighbors talked about the wedding as if it were over, and good Praskovya Petrovna rejoiced that her daughter had finally found herself a worthy groom. The old lady sat alone in the living room one day, unfolding the gransolitaire, as Burmin entered the room and immediately inquired about Marja Gavrilovna. «She is in the garden, - the old lady answered, - go to her, and I will wait for you here». Burmin went, and the old lady crossed herself and thought, Maybe it will end today! Burmin found Marya Gavrilovna by the pond, under the willow, with a book in her hand and a white dress, the real heroine of the novel. After the first questions, Marya Gavrilovna purposely stopped keeping the conversation going, thus intensifying the mutual confusion, which could only be removed by an unforeseen and resolute explanation. So it happened: Burmin, feeling the difficulty of his position, declared that he had long sought an opportunity to open his heart to her, and demanded a moment of attention. Marya Gavrilovna closed the book and looked down in agreement.  «I love you, said Burmin, - I love you passionately...» (Mariya Gavrilovna blushed and tilted her head even lower.) «I acted carelessly, giving myself a nice habit of seeing and hearing you daily...» (Mariya Gavrilovna remembered the first letter St.-Preux 3).  «Now it is too late to resist my fate; the memory of you, your dear, incomparable image will henceforth be the torment and joy of my life; but I still have to fulfill the heavy duty, to reveal to you a terrible mystery and put an insurmountable barrier between us...» - «She always existed, - interrupted with liveliness Marya Gavrilovna - I could never be your wife...» - «I know, - he answered her quietly - I know that you once loved, but death and three years of lamentations... Kind, sweet Marya Gavrilovna! Do not try to deprive me of my last comfort: the thought that you would agree to make my happiness, if... keep silent, for God’s sake, keep silent. You torment me. Yes, I know I feel you would be washing, but - I am the most unfortunate creature... I am married!» Marya Gavrilovna looked at him with surprise. 'I’m married,' said Burmin, 'I’ve been married four years, and I don’t know who my wife is or where she is or if I should ever see her again! What are you saying? cried Marya Gavrilovna, how strange! Go on; I’ll tell you after... but go on, do me a favor. — In the beginning of 1812, said Burmin, I hurried to Vilna, where our regiment was located. When I arrived at the station late one night, I had the horses planted quickly, when a terrible snowstorm came up, and the caretaker and coachmen advised me to wait. I listened to them, but a strange anxiety gripped me; someone seemed to push me. Meanwhile, the blizzard did not abate; I did not suffer; I ordered it to be laid again, and went into the storm. The Chamberlain decided to go by river, which should have cut our way three miles. The coasts were brought in; the coachman drove past the place where they went on the road, and thus we found ourselves in an unfamiliar side. The storm did not subside; I saw the light and told him to go there. We came to the village; there was fire in the wooden church. The church was opened, a few sledges stood outside the fence; people walked on the porch. «Here! here!» - a few voices screamed.  I told the coachman to come by. Excuse me, where have you been? Someone told me - the bride fainted; the priest does not know what to do; we were ready to go back. Come quickly». I silently jumped out of the sledge and entered the church, lightly lit by two or three candles. The girl was sitting on a bench in a dark corner of the church; the other was rubbing whiskey on her. Thank God, this one said, 'you’ve come all of a sudden. You almost killed the young lady». The old priest came to me with the question: «Order to begin?» - «Start, start, Father», I answered absent-mindedly. The girl was raised. She seemed fine to me... An inexplicable, inexcusable flirtation... I stood beside her before her cash; the priest was in a hurry; the three men and the maid supported the bride and were busy with her only. We were married. «Kiss» they told us. My wife turned her pale face to me. I wanted to kiss her... She cried out: «Oh, not him! not him!» - and fell without memory. Witnesses rushed at me scared eyes. I turned around, left the church without any obstacles, threw myself into the kibitka and cried out: «Gone!» My God! cried Marya Gavrilovna, and you have no idea what happened to your poor wife? — 'I don’t know,' said Burmin, 'I don’t know the name of the village where I was married; I don’t know which station I came from. At that time, I thought so little of my criminal leprosy that when I left the church, I fell asleep and woke up the next morning at the third station. The servant who was with me at the time died on the journey, so I have no hope of finding the one I have so cruelly played a joke on and who is now so brutally avenged. My God, my God! said Maria Gavrilovna, grabbing his hand, it was you! And you don’t recognize me? Burmin turned pale... and threw himself at her feet...  _________________________________________________________________________________________

---
## [benstreich/laravel](https://github.com/benstreich/laravel)@[1fab9af979...](https://github.com/benstreich/laravel/commit/1fab9af9793fc6ce0a7bfbaf603775448cb641f7)
#### Wednesday 2023-03-29 09:52:23 by Ben Streich

Creating Events works, login doesn't work completely

Now 👃 look at 🅱💁 them 😘😊 yo-yos, 👀 that's 🚟😐 the way you 👊👈 do 👎 it You 😤 play 🎰🕹 the 😗 guitar on 🏽 the 👏👏 MTV That ain't workin', 👍 that's 🏻👨 the 👏🏔 way you do 😴👌 it Money 💵 for 🎁 nothin' 😎😎 and your 👏 chicks 🐤 for 🖋 free 🆓♀ Now 🚟🏿 that ain't workin', 👍 that's 👉🌈 the way 👉 you 👉🙅 do 👌 it Lemme tell 😲 ya, them 👙👦 guys 👨🏿 ain't dumb 😐🔥 Maybe 😉 get 🍌 a 🐍🤑 blister on your 💦♂ little 🐩👧 finger Maybe 👏 get 💁😏 a blister on 🌞 your 👩 thumb 👍 We 👥 got 💰🍸 to 😤 install microwave ovens, ♨♨ custom 🎅🏿 kitchen deliveries We 🏼 got 💁 to 💦📴 move 🏃😎 these 🚱 refrigerators, we got to 😆♀ move 🔛 these 🚑🖌 color 🎨🎨 TVs See 🤔 the 🦁 little 🤛 faggot with 👏😶 the 😫🚟 earring and 👏 the 🌎☸ make 🖕💦 up ☝ Yeah, buddy, ❗ that's 🚪🏾 his 🤔👉 own hair That 💯🍆 little 🏻😇 faggot 💦👈 got his 👦😠 own jet ✈ airplane That little 🏻😼 faggot, 👈 he's 😡 a 🔵 millionaire We 👧 got 😂 to install microwave ovens, ♨♨ custom 🛃🏿 kitchen 👨 deliveries We got 😜 to 💦🛑 move 🏼😎 these 📀 refrigerators, we gotta ☠ move 👊🏼 these 👈 color 🏽 TVs We 💰 got 💌 to 😂 install microwave ovens, ♨ custom 🛃🎅 kitchen 👨👨 deliveries We got 😏🍸 to move 🏃👊 these 💦😤 refrigerators, we 👩 got 😂🍸 to 💦 move 😎🏃 these 💁 color 🏽🏽 TVs Looky here, 💦 look 👁👀 out 📤 I shoulda learned 🙌🤓 to 💦 play 🎰 the 👌 guitar I 👁💰 shoulda learned to play them 😏 drums 🔂🔂 Look 🕊🏾 at that 👉 mama, 🏿👵 she got 😜 it stickin' in the 😍 camera 📷📹 man 🏃♂ We could 🚫🤔 have 👏👏 some 👨🐺 And 👏 he's 👨 up 👭 there, what's 😦 that? 👉 Hawaiian noises? 🔊🔊 Bangin' on the 👏 bongos like a 😩🤑 chimpanzee That 🚟😐 ain't workin', that's the 🔪 way ✋👉 you do it 😩🔜 Get your 💦👉 money for 👉🍅 nothin', 😎😎 get ✊👽 your chicks 🐤 for 🕒💯 free We got to install microwave ovens, ♨ custom kitchen deliveries We 👦👧 got 😜 to 😖 move 🔛 these ♀😍 refrigerators, we gotta move 🔛 these 👈 color 🎨 TVs Listen 👴 here ⛄ Now that ain't workin' that's the way ↕↕ you 👆👶 do it You 😭⁉ play the 👏 guitar 🎸🎸 on the 🚫 MTV That ain't workin', 👍👍 that's 😠👉 the 😈🌐 way you do 🤤 it 😩 Money 🤑 for 👉👏 nothin' 😎 and your 👨👏 chicks for 🕓 free ♀👍 Money for 🎅🍆 nothin', 😎 chicks 🐥 for free 😗👏 Get your money for 💥🎁 nothin' 😎 and 💃👏 your 🏼 chicks 🐥🐔 for 🏼 free 👏 Ooh, 😳😔 money 💵 for 🎅 nothin', 😎😎 chicks for 👉 free 💜 Money for 🍆🍆 nothin', 😎 chicks for 👷 free 👍 (money, money, money) Money for 🍀 nothin', 😎😎 chicks 🐥 for 👻 free Get your 👏😡 money for nothin', get your 😩 chicks 🐤 for free Get your 👏💦 money for 🍆👅 nothin' 😎 and the chicks 🐔🐣 for free 💜🙅 Get ♂🎁 your 👆🍑 money 💵 for 🎅💰 nothin' 😎😎 and 🎁🙇 the ☸👩 chicks 🐣 for 🖍 free 😔💜 Look at ☺💋 that, look at 🤠 that 😐 Get 🉐🍌 your 💯 money 💰💵 for nothin' (I want 👏💞 my, 👈 I 🤔💗 want my) Chicks for 🔙 free (I want 😋 my 🐕👉 MTV) Money 💵 for 😩 nothin', 😎 chicks 🐥🐤 for 🎛 free (I 👁👁 want my, 👌 I 🗨 want 👏 my, 👨 I want 👈 my 👨🌌 MTV) Get your 😏😄 money 😮 for 💯💯 nothin' 😎😎 (I 👁😔 want 👏 my, 🔯 I 👨 want my) 👉 And 👏➕ the 😫 chicks 🐣🦆 for 🖍🍆 free 🔓💜 (I 👉 want my MTV) Get 🏿😘 your 👏 money for nothin' 😎 (I want 💦🙅 my, I 🔨 want my) 👈🎄 And 😱👎 the 😎 chicks 🐣🐥 for free (I 👏👁 want my MTV) Easy, easy ⁉ money 💵 for nothin' 😎😎 (I ❌ want my, 👈 I 😞🙅 want my) 👊🚔 Easy, ‼❗ easy ❓ chicks for ⌛ free 👏 (I 😻 want 😷 my 🏾 MTV) Easy, ❓ easy 🙅 money for nothin' 😎😎 (I 🙋♂ want 💞 my, 😈 I 👱 want 💯👨 my) 🙂 Chicks for 👏 free 💰 (I 👱 want my 👨 MTV) That 😤 ain't workin' Money 💸💵 for 👍🎅 nothing, 🚫 chicks for 🤔 free 🤔👏 Money 🤑 for 🍆👀 nothing, 🔫🚫 chicks for ❓ free

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[23a081ed49...](https://github.com/TaleStation/TaleStation/commit/23a081ed49c3b62ae0b37f506983f196bbef181a)
#### Wednesday 2023-03-29 10:40:00 by TaleStationBot

[MIRROR] [MDB IGNORE] Syndicate Lavaland Base Photocopier is now Free (Gratis) (#5124)

Original PR: https://github.com/tgstation/tgstation/pull/74268
-----
## About The Pull Request

Closes #74196 . The syndicate ripped out the payment charger for VERY
IMPORTANT BUSINESSWORK.
## Why It's Good For The Game

i dunno if the syndicate ever get a fax machine they'll be able to send
people ass photos?
## Changelog
:cl:
fix: The Syndicate have gotten their hands on the most dangerous weapon:
A photocopier that doesn't require any money. God save us all.
/:cl:

I decided to go with the subtype being named `gratis` because i didn't
want people to confuse whatever a `free` subtype would mean... free to
photocopy your own ass or anyone's ass? unlimited ass? photocopy smut?
whatever i think it's funny since it gives you to the answer of the joke
that i put in the desc... i'm such a master of comedy

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[4a94f5af2b...](https://github.com/TaleStation/TaleStation/commit/4a94f5af2bfeded4c31afad9030d2d247c65865b)
#### Wednesday 2023-03-29 10:40:19 by TaleStationBot

[MIRROR] [MDB IGNORE] Streamlines/Fixes Piracy Spawner Checks - They Piss Off When Paid (#5125)

Original PR: https://github.com/tgstation/tgstation/pull/74275
-----

## About The Pull Request

Fixes #74211.

I think at some point this worked, but there were just too many checks
on abstract concepts and it seems that "aborting" the callback wasn't
really working? Anyways everything just felt really awk to me with how
`message_override` was working, so let's store a variable on
`chosen_gang` since we're already reliant on that for all of our
messages and stuff like that, and just slim down the number of weird
checks that we do into just one simple "did we get paid"?

One consequence of this is that refusing to pay won't spawn pirates
instantly, but the time-to-respond was already two minutes so I don't
really see this as a major drawback.
## Why It's Good For The Game

I PAID THEM OFF NOW FUCK OFF
## Changelog
:cl:
fix: Pirates finally realized that they shouldn't risk life and limb
attacking stations if they had already paid them off.
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [FireNick44/M151-laravel](https://github.com/FireNick44/M151-laravel)@[5c5c5a7f3d...](https://github.com/FireNick44/M151-laravel/commit/5c5c5a7f3d0412976c7b54317cd1517e956a3285)
#### Wednesday 2023-03-29 12:43:09 by FireNick44 | YannicA46

Laradone

fixed the israeli-palestinian conflict

lots of changes after a lot of time

We Had To Use Dark Magic To Make This Work

Ok, 5am, it works. For real

Never gonna run around and desert you

Copy-paste to fix previous copy-paste

the magic is real

I’m too old for this shit!

Crap. Tonight is raid night and I am already late.

You should have trusted me.

removed echo and die statements, lolz.

We’ve known each other for so long

or the sake of my sanity, just ignore this…

Replace all whitespaces with tabs.

I dont know what I am doing

Out for vacation… DONT YOU DARE TO CALL ME.

pr is failing but merging anyways, because I am an admin

“Get that shit outta my master.”

Removing unecessary stuff

This is not a commit

This commit is a lie

The same thing we do every night, Pinky — try to take over the world!

Too lazy to write descriptive message

At times like this I wish I was a Garbage Man.

That last commit message about silly mistakes pales in comparision to this one

We’ll figure it out on Monday

It fucking compiles \:D/

Too tired to write descriptive message

Merging ‘WIP: Do Not Merge This Branch’ Into Master

I know what I am doing. Trust me.

Push poorly written test can down the road another ten years

I don’t believe it

We know the game and we’re gonna play it

It Compiles! 50 Points For Gryffindor.

You can’t see it, but I’m making a very angry face right now

apparently i did something…

I don’t know what these changes are supposed to accomplish but somebody told me to make them.

One little whitespace gets its very own commit! Oh, life is so erratic!

Added some NullPointerExceptions — Happy easter, you bastards! :D

I just wanna tell you how I’m feeling

It works on my computer

fixed shit that havent been fixed in last commit

i dunno, maybe this works

Done, to whoever merges this, good luck.

Please forgive me

Please our Lord and Savior the Great Linter.

Undoing last comming

just checking if git is working properly…

someone fails and it isn’t me

I have done a lot of things that I can’t remember.

---
## [benstreich/laravel](https://github.com/benstreich/laravel)@[2bea8037ce...](https://github.com/benstreich/laravel/commit/2bea8037ce5c23e5dd9284f22d9aec5b0dd01d78)
#### Wednesday 2023-03-29 12:55:42 by Ben Streich

things work i think Talk to 🤷✌ me 🤓😭 softly There's something 👈😳 in 🍌👏 your eyes 👁 Don't 👎🚫 hang ☎ your head in 👇👌 sorrow And ➕ please 🙏 don't cry 😢 I 👀👀 know how 💯 you 😂 feel 🤣 inside 💦💯 I've 👁👉 I've 👨💰 been there before Somethin's changin' inside you 🆒 And 👅👏 don't you ☝ know Don't 👎🙅 you 👆👆 cry 😭 tonight 🎶‼ I 👁 still 😽🕞 love 🎆♥ you, 😵👉 baby Don't 🙅🙅 you ♀ cry tonight Don't 🚫 you 🏼 cry 😭😭 tonight There's 👌 a 😰💰 heaven ✔ above 🔝👆 you, baby 😉🏻 And don't 🙈🚫 you 👈👈 cry 😭💦 tonight ♨🌑 Give 🎁🍆 me a whisper And 🔝 give me 👌🙎 a 🎪 sigh 😔 Give me a 👏 kiss 😍😍 before 😈⏪ you 👀 Tell 💬🎙 me goodbye 👋👋 Don't 🚫🙈 you 👈 take it so 💯 hard 😾 now And 👏👏 please 🙏🙏 don't 🚫 take ✋ it ✊ so 💯 bad 🔚👎 I'll still 😽💢 be 🤢 thinkin' 🤔☁ of 👀 you 👏 And 🏻👅 the times 😱 we 👥🌊 had, 💯 baby 👶 And don't 🚫🚫 you 💦 cry 😭😢 tonight 😫🌚 Don't 🙅😡 you cry 😢 tonight 🎶 Don't you 👈😘 cry tonight 😩😫 There's ✔👨 a ↘👺 heaven ✝✔ above 👆🔝 you, baby 👶😱 And don't 😡 you 👊 cry 💦 tonight 😴 And 💦💰 please 🏻🌸 remember 😎 That ❌ I never 😱❌ lied Oh and please remember 😨 How I 👀😎 felt inside 💠 now, 🤗 honey 🍯 You 🏃👨 gotta make 🖕👏 it your 🏼⬅ own 🌈👐 way 💦 But 🍑 you'll 😭 be 🏿➡ alright now, sugar 👯 You'll 😤 feel better 🐍🎒 tomorrow 🔙 Come 🍆 the 👏 morning 😡 light 🕯 now, 😭 baby 👶 And 👏👏 don't 🙈 you 😨 cry 😭 tonight 🍆 And don't you ‼👀 cry 😭😭 tonight 🍆 And 😦🔜 don't you ❤ cry 😢 tonight 🌠 There's 💦 a heaven above 🏻😩 you, 🥕👈 baby And 👽👏 don't 🚫🚫 you 🏿👺 cry 💦💦 Don't 🙈 you 😐😘 ever 👩 cry 😢😭 Don't you cry 😢 tonight 🌚😫 Baby, maybe ❔ someday 📅 Don't you cry Don't 😡 you ever 🤔 cry Don't 🚫 you 🍆 cry Tonight 😴

---
## [ProfessorPopoff/mojave-sun-13](https://github.com/ProfessorPopoff/mojave-sun-13)@[bdc9c58586...](https://github.com/ProfessorPopoff/mojave-sun-13/commit/bdc9c58586e0ab567e98b31054e8275d74990a58)
#### Wednesday 2023-03-29 14:52:24 by Technobug14

Agriculture ('Technoculture') Farming: Fertilizer Edition :) (#2278)

* Does Stuff

Beginnings of agriculture code, stripped down TG botany a bunch, got rid of scar botany whilst replacing most of it. Also some map edits to change the paths on stuff and add a few spades for farming.

* Some NPK system framework

Removing more TG botany stuff and getting some framework down for NPK. Adds a "nutrient_type" variable to seeds and gives N, P or K as the type to every seed.

* Removes Stuff, More NPK Framework

Still WIP on NPK stuff, removes more basic bitch TG botany stuff, needs a lot more content but in an almost-working state

* Nutrient drain

Nutrients actually get drained properly now. Crop plots output their level of N, P and K when examined. Still need to make something to handle restoring nutrients and figure out a nutrient economy for plant consumption.

* Mostly working, one major bug

This is mostly working now. The NPK now drains according to the seed planted, it replenishes over time, you can now get water from water tiles and the soil will properly adjust the waterlevel variable with the new water types.

HOWEVER, big bug. The way TG handled watering crops is ass. Doesn't delete, stays in the reagent_container of the soil, normally checks for if a reagent_container has water to bypass how full the soil's container is, bad system that sucks. Needs fixing.

* oops

oopsie!!! fucked something!!! forgot to undo a change I made to the code, it's just there to remind me it's not working correctly

* Last minute fixes/bandaids

I HATE TG BOTANY I HATE TG BOTANY I'M LOSING IT

* Fertilizer groundwork

Some stuff for fertilizer, need to add the attackby but cutting out a bunch of code to clean things up. Need to see if it breaks stuff.

* Fertilizer attackby changes

Adds code to the attackby for farm plots that checks if you're attacking it with fertilizer, doesn't work for some reason I can't tell. Also removes some vestigial TG botany stuff.

* fixt

fixes fertilizer, I forgot to specify something in a var, works now!!! YAY!!!

---
## [Monkooky/crawl](https://github.com/Monkooky/crawl)@[c65c45c1d4...](https://github.com/Monkooky/crawl/commit/c65c45c1d4c4d4d01db8334bc56938436b0d3bc0)
#### Wednesday 2023-03-29 15:24:02 by Nicholas Feinberg

Move the Vaults rune lock inside (hellmonk)

Long ago, Vaults got a 'rune lock' - the requirement that players find
at least one of the fabled Runes of Zot before entering. This was added
so that players would be encouraged to fight at least one of the final
challenges of the Lair branches (Snake, Spider etc) at a time when they
were still challenging. Before this lock was added, wise players fought
those challenges much later, after getting so much XP and loot from Vaults
etc that they were trivial.

This was a big improvement! But there was one downside - lunatic players
who wanted to get the silver or, god forbid, golden rune before getting
any other runes (or even entering the Lair, perhaps!) were blocked from
achieving their dreams. Tragic!

So, this commit lets them do that. You no longer need a rune to enter
the Vaults, but you do need a rune to leave. Wise play probably remains
unchanged,

There is a fairly strongly worded warning for players trying to enter
the Vaults without a rune, with a requirement to type 'yes' to enter
(ala stepping on a Zot trap, entering wizmode, etc). So I'm hoping this
doesn't affect the experience for newer players. If it does, I'll rethink
this!

---
## [tabulon-ext/inxi](https://github.com/tabulon-ext/inxi)@[5ee29fa022...](https://github.com/tabulon-ext/inxi/commit/5ee29fa022e01f8283fa526838f504c0dfccbadb)
#### Wednesday 2023-03-29 15:42:45 by Harald Hope

Significant upgrade to sound server running detections, much more granular and
hopefully more accurate, with more useful reporting values. Also added some nice
useful audio api/server tool and info items.

Packagers: this corrects possibly wrong or misleading audio server reports,
particularly related to PulseAudio/PipeWire, which can lead to support issues
and lack of clarity due to ambiguous or wrong reports about sound Servers
present, active, or off. Upgrading your package is highly recommended.

--------------------------------------------------------------------------------
SPECIAL THANKS:

1. Thanks to people like Chimera dev Daniel "q66" Kolesa for experimenting with
non systemd (uses dinit/dinitctl), non GCC, non GNU linux, and for making early
pre-alpha versions run in vm, and for being easy to test!

Not so much because I personally want or care about or view as a positive
skipping GNU tools or GCC in favor of clang and BSD tools, but more because
these experiments help make the general overall Linux ecosystem more robust.
Including inxi.

2. Thanks for the Manjaro people for noting this issue on their forums.

--------------------------------------------------------------------------------
KNOWN ISSUES:

1a. AUDIO: jack_control and pw-cli won't run as root, exit with error. This
forces back to fallback process present tests for active running state.

1b. AUDIO: pactl will start pipewire/pipewire-pulse/pulseaudio if stopped and
not masked, so not using since that would make inxi alter the state of the
system.

1c. AUDIO: pipewire-alsa, pulseaudio-jack depend on file exist globs, tested on
Arch Linux, Debian base, but unknown if paths exist on other Linux pimary
distros. Easy to add to globbing tests, but no going to check them all!

2. SERVICES: systemctl status [service] can fail if service loaded using --user
which is a new one on me, not sure how to handle that.

3. It would be nice to get inxi issues like the sound server/api glitches
handled by filing an issue on inxi github, and not to rely on my seeing a random
distro forum post, which I only found by pure coincidence.

--------------------------------------------------------------------------------
BUGS:

1. AUDIO: See Fixes 3a,b,c. In some cases false report of pulseaudio and
pipewire running: yes create unclear output and results, or misleading. Thanks
to manjaro users to noticing this and mentioning it in a forum post.

Note: it's much more effective to file issues on inxi github than to hope I will
see a random forum post one day.

2. DEBUGGER: Bug in debugger, somewhere introduced '-- list' (instead of
'--list') for bluetoothctl which made older systems hang when running the
debugger. No idea when or how that space got introduced.

--------------------------------------------------------------------------------
FIXES:

1. INFO: Compilers showed Compilers: gcc: N/A when clang/gcc not installed, this
was not intended, but was a small glitch in main::get_gcc_data(), where it
assigned undef as array contents when gcc not defined. This was exposed by
Chimera, which uses clang, but would have happened any time gcc not installed on
system.

2. SYSTEM: tiny fix, was getting ',' at end of kernel compiler version.

3a. AUDIO: For pipewire, made process detection test more robust, now excludes
pipewire-pulse in case where that might be running without pipewire on/enabled.

3b. AUDIO: bigger fix, more robust tests for audio servers running for jack,
pipewire, pulseaudio, these look for more explicit server tool reports. Certain
not to be reliable always, and fail for superuser, will probably need more
tweaking. Also notes for jack, pulse, pipewire if only positive detection found
via ps aux: active (process) to avoid incorrect data, and root specific messages
depending on situation.

3c. AUDIO: was testing for pactl to determine if pulseaudio installed, but found
case where pactl could be installed without pulseaudio. Now tests for pulseaudio
installed.

3d. AUDIO: weak fix for Linux OSS4 version, using /etc/oss4/version.dat file,
which may or may not exist on all distros.

3e. AUDIO: alsa-oss compat can create /dev/sndstat file, which would then lead
to positive OSS detection even if it's not present. This is corrected, and will
not show if asound/version exists and no ossinfo. For linux, relying on ossinfo
presence, which comes from oss4-base.

3f. AUDIO: Older ALSA /proc/asound/version had a date string in parentheses
after the Driver Version, so now explicitly get the string after Version.

--------------------------------------------------------------------------------
ENHANCEMENTS:

1. REPOS: added support for /etc/apk/repositories.d/*.list, which works pretty
much the same as /etc/apt/sources.list.d/*.list. This is to make Chimera apk
repos show up, previously only supported /etc/apk/repositories file read.

2a. DistroData: Added Feren to distro system base. This was much trickier than
it should be due to inconsistent use of os-release field names, but that's how
it goes.

2b. DistroData: new Arch derived distro XeroLinux added to system base. I know,
I know, it's a never-ending endeavor (get it?) since these pop up all the time,
but might as well add them now and then as they appear.

3a. AUDIO: inxi now handles pipewire-pulse as top layer audio daemon, along with
several other server/api helpers. Note that pw-jack does not appear to be a
daemon, just a plugin, so shows 'plugin'. Extra sound server helpers added when
discovered or requested.

  API: ALSA
    v: k5.19.0-16.2-liquorix-amd64
    status: kernel-api
  Server-1: PulseAudio
    v: 16.1
    status: off (on pipewire-pulse)
  Server-2: PipeWire
    v: 0.3.65
    status: active
    with:
      1: pipewire-pulse
        status: active
      2: pw-jack
        type: plugin

3b. AUDIO: For -Aa, added tools: report. Currently supports these basic tools:

alsa: alsamixer alsamixergui amixer
jack: cadence jack_control jack_mixer qjackctl
oss: dsbmixer mixer ossinfo ossmix ossxmix vmixctl
nas: auctl auinfo
pipewire: pw-cat pw-cli wpctl) [+pactl if pipewire-pulse and no pulseaudio
pulse: pacat pactl pamix pamixer pavucontrol pulsemixer
roar: roarcat roarctl
sndiod: aucat midicat mixerctl sndioctl

Note that inxi-perl/docs/inxi-audio.txt has lists of alternates or rejected
helpers and tools, but we want to keep that output short and sane.

3c. AUDIO: For BSDs, if sndiod is detected, adds an API line for sndio. Note
this may create 2 API lines for FreeBSD using OSS.

3d. AUDIO: Added basic support for roar sound server, NAS (Network Audio
System).

4. CPU: new Intel and AMD cpu model matches for latest and future, Luna Lake,
Zen 4c.

5. GRAPHICS: new nvidia current, AMD, and Intel GPU ids.

6. DRIVES: more disk vendors, ids! The list never stops, but sadly, so many are
not identifiable. Check: inxi-perl/tools/lists/disks_unhandled to see if you
can positively identify any of those.

--------------------------------------------------------------------------------
CHANGES:

1a. AUDIO: Changed main API/Server running: to status: [status], that syntax is
more able to handle different circumstances.

1b. AUDIO: With change to status:, now uses granular fixes above, and adds root
notes if no active detections.

1c. AUDIO: Changed 'Sound API', 'Sound Server' to 'API', 'Server'. This avoids
ambiguity with some types, it's the Audio section, and those are the APIs and
Servers for that Audio section. Makes it match Graphics as well. and is shorter.

1d. AUDIO: Changed 'Sound Interface' for sndiod to 'Server', which is how it's
listed, and for BSD, added API: sndio item. Also changed 'sndio' to 'sndiod' for
the Server: item.

1e. AUDIO: Changed ALSA/BSD sndio to show: status: api since saying an api
is running makes little sense, it's there or it's not there. OSS can be enabled
or disabled so shows status: active/off for Linux, but kernel-api for BSDs.

--------------------------------------------------------------------------------
DOCUMENTATION:

1a. MAN: Added note for helpers item: with: pipewire-pulse/pw-jack etc to -Axx.

1b. MAN: Added -Aa item for audio server tools.

2. OPTIONS: Updated for -Axx helpers, -Aa tools.

3. DOCS: Created inxi-perl/docs/inxi-audio.txt doc file. Too many odd factoids
to forget about during this upgrade!

--------------------------------------------------------------------------------
CODE:

1. REPOS: Moved %keys to %repo_keys and set it only once with set_repo_keys(),
those big hash assigns per iteration are really expensive, now stores it
globally in RepoItem and sets only once.

2. INFO: main::get_gcc_data() failed to handle case where there is no gcc at all
installed, resulted in returning an array with content of 'undef', not an empty
array as intended. This made the array not set test fail for Compilers, so gcc
showed as N/A, which was not intended.

3. DistroData: changed internal lsb/osr $distro to $distro_lsb/$distro_osr,
which lets inxi update the distro name during system base processing in cases
where the data is redundant. Stupid hack, sigh, should not be necessary, but
that's life, /etc/os-release was poorly designed so it leads to such confusions.

4a. AUDIO: Added --dbg 52 to output results of pw-cli.

4b. AUDIO: refactored sound_data, renamed, added {jack,pipewire,pulse}_status(),
sound_helpers(), sound_tools() utilities.

5. DEBUGGER: added more pactl and pw-cli outputs, and pipewire-pulse,
pipewire-jack --version.

6. main::get_driver_modules(): add space after ',' if total string > 40
characters to allow splitting very long unbroken strings of modules that
otherwise would not break as expected.

---
## [DrDiasyl/tgstation](https://github.com/DrDiasyl/tgstation)@[3156a0414e...](https://github.com/DrDiasyl/tgstation/commit/3156a0414e96b597d4d53823066d29daa0b30737)
#### Wednesday 2023-03-29 16:19:12 by san7890

[MDB Ignore] Manifest Destiny - The Final Tile Flattening (#74169)

Alt Title: The End Of The 12 Month War
## About The Pull Request

### Hey! Listen! This PR _will_ cause a merge conflict with your PR!
Please ensure that you have the knowledge on how to handle merge
conflicts, found here:
https://hackmd.io/@tgstation/ry4-gbKH5#Assured-Merge-Conflict-Resolution

Supercedes #74023 entirely.

Port of the tooling introduced in
https://github.com/BeeStation/BeeStation-Hornet/pull/7970 (we already
had everything else), modified to meet /tg/'s requisites and culling
anything that was not entirely relevant (that I could see). It's not the
end of the world if I missed something tbh. Some aspects were commented
out since they may be relevant to downstreams who port this PR or to
enable (what I see to be) un-necessary warnings.

This is a culmination of a year's efforts, starting with _Red Rover,
Four Corners_ (#65290) and later _Opposing Corners_ (#65455). If you
don't understand why this PR exists or why it's necessary, I recommend
reading both of those.

Since then, several mappers (both in their own mapping as well as
tailored PRs) have worked on "flattening" out these tile turfs, however
I've continually wanted a function that would mass automate it (outlined
here https://tgstation13.org/phpBB/viewtopic.php?t=31872 - This
functionality might still be useful if added to UpdatePaths or another
type of script thereof, but I no longer have reason to keep the bounty
up).

It's finally here! Yippie! A new python file, courtesy of itsmeow at
BeeStation. Very awesome. As previously mentioned, a lot of alterations
had to be made for our mapping desires, but the results are quite
agreeable. There's a few assertions that this file makes that I had to
address:

* We have "colorless" tile decals. These are transparent, so they don't
do anything. By default, bee would make these "white tiles", but we have
no such thing. I decided to just add a maplint and an UpdatePaths to
guard against this silliness (only Delta and Tram) had it.
* For some reason, it labels already-converted decals with the default
direction as an error state. I might touch this up in the coming hours,
but for now I surpressed the error due to how many false warnings it was
spitting out.

There's a few ways this tool can be improved, but I lack the knowledge
on how to do so:
* Make it so that we can run the map merger to fix the keys of the map
in the `update_map` function, rather than run the fixer-upper python
file. We can live without this to be honest. It's actually slightly good
because it forces you to look at all of the MapMerge Warnings, and you
can ascertain any potential errors without it silently passing you by
and hitting the repository (or at least those that we haven't linted for
yet).
* Be able to pass in any regex to "flatten" anything. That's way out of
scope for what I want to do here though.

## How do you use this tool?

I made a readme.
https://github.com/tgstation/tgstation/blob/363852cb17fa46dad8fd20e261f8f665f3e008bb/tools/MapTileAggregator/readme.md
### Mapping March
oh hey it's pretty neat that this PR came out in mapping march, what a
nice qol for mappers as the month enters the home stretch. ckey is
san7890

## Why It's Good For The Game

slimmer DMM files, better mapping practices. cool new tool. so nice.
## Changelog
Nothing that really affects players, but a short summary for all those
reading this PR:

* All "corner" turf decals are flattened, and there's now a tool that we
store that you can re-run to keep stuff flat in case you like mapping
one way and want to fix it at the end.
* We (should) now lint against useless uncolored turf decals since that
was completely garbo as far as our codebase is concerned.
* UpdatePaths for fixing up uncolored turf decals, yippie!


If you want to review this PR, may I suggest the file filter. You don't
need to look at any of the DMM files I already did:

![image](https://user-images.githubusercontent.com/34697715/226787961-ab82cad4-5d6d-4788-a7bd-5071aac825c4.png)

---------

Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>

---
## [ausbitbank/stable-diffusion-discord-bot](https://github.com/ausbitbank/stable-diffusion-discord-bot)@[5231ee922d...](https://github.com/ausbitbank/stable-diffusion-discord-bot/commit/5231ee922dc1ddb4ce59a82e877f50e251959c72)
#### Wednesday 2023-03-29 16:33:42 by ausbitbank

Merge pull request #37 from coalescentdivide/reply-logic-tweaks

nice updates to reply logic thx to coalescentdivide <3
```


Some tweaks I made to the reply logic. I thought I'd share because I personally get a huge value with these tweaks.

A while back I noticed you could work off of an existing image by replying with .. as opposed to the tweak menu, and I thought that was a super useful feature. However it was tedious for me because I found that nearly every time I used this feature, I would forget to type things that I didn't want to change, such as the model used.

I thought it would be nice to just type .. --scale 11 or .. --steps 60 or some combination of parameters, while retaining the model and other settings from the render being replied to. So I updated the .. reply to do that. I updated the + and - reply also, but I really don't use them that much.

I also found that due to the discord mobile app limitations, copying the seed or other details from a render was a bit annoying from my phone. On mobile I would have to copy the entire text, then extract the seed from the copied text to reuse. So I added two new replies to make it more mobile friendly: seed and info.

replying with seed gets a reply back with the seed as an embed like this: --seed 12345. Since it is an embed, on mobile you can simply press and hold to copy it.

Similarly, replying with info gives a response that contains the full !dream command. But I didn't want to include EVERY command, things like upscale, seamless and threshold for instance. So to keep it tidy, I made it so those are only included in the string if they are used. Another benefit I found for the info reply: When an output is far enough back in the chat history where you have to click 'jump to present', this causes the tweak menu to disappear. replying with info will work for this, however if the queue was wiped and an output was before the wipe, that will give the wrong dream command.

I also changed the template reply so that by default, the ddim sampler is used, as it seems to work best for img2img. Any other sampler can still be specified.

Similar to that, I added one more reply inpaint which is just like template but defaults to the inpainting model.

disclaimer: I am only starting to dabble with coding within the last few months (thanks to language models like gpt) so I wouldn't be surprised if there is a better way to accomplish all of this. I've tested for a while in my discord and it does seem to work as intended. Feel free to edit into something better if my code sucks!

*The main limitation I'm aware of is that it the .., + and - reply methods don't retain the template image for an img2img render.
```

---
## [openai/evals](https://github.com/openai/evals)@[114f4f8536...](https://github.com/openai/evals/commit/114f4f8536f29df43e5145fd38826285d19d6728)
#### Wednesday 2023-03-29 16:53:08 by Greg Priday

[evals] ROT13 string evals (#361)

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
ROT13

### Eval description

This is a test for GPT4s character-level abilities. It's aware of ROT13
and makes a pretty solid attempt at decoding these ROT13 strings, but it
messes up a lot. The accuracy for GPT 3.5 Turbo is 0.05.

### What makes this a useful eval?

A human with a character lookup table could easily solve these ROT13
decoding. Also, based on my testing with GPT 3.5 Turbo, the model is
happy to make an attempt, even though the results it gives are
incorrect.

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
{"input":[{"role":"system","content":"You are a helpful assistant. Give
only the string that the user asks for, no extra characters.\n\nFor
example if the user asks 'Give me the ROT13 of: Vg'f n cvrpr bs cvr.',
you will respond with just 'It's a piece of
pie.'"},{"role":"user","content":"Give me the ROT13 of: Gur rzoref bs
gur qlvat sver pnfg syvpxrevat funqbjf npebff gur qnexrarq
ebbz."}],"ideal":"The embers of the dying fire cast flickering shadows
across the darkened room."}
{"input":[{"role":"system","content":"You are a helpful assistant. Give
only the string that the user asks for, no extra characters.\n\nFor
example if the user asks 'Give me the ROT13 of: Vg'f n cvrpr bs cvr.',
you will respond with just 'It's a piece of
pie.'"},{"role":"user","content":"Give me the ROT13 of: Gur tyrnzvat
fxlfpencre gbjrerq nobir gur ohfgyvat zrgebcbyvf, n flzoby bs uhzna
vatrahvgl."}],"ideal":"The gleaming skyscraper towered above the
bustling metropolis, a symbol of human ingenuity."}
{"input":[{"role":"system","content":"You are a helpful assistant. Give
only the string that the user asks for, no extra characters.\n\nFor
example if the user asks 'Give me the ROT13 of: Vg'f n cvrpr bs cvr.',
you will respond with just 'It's a piece of
pie.'"},{"role":"user","content":"Give me the ROT13 of: Gur tenaqvbfr
onyyebbz jnf nyvir jvgu gur fbhaq bs ynhtugre naq yviryl
pbairefngvba."}],"ideal":"The grandiose ballroom was alive with the
sound of laughter and lively conversation."}
{"input":[{"role":"system","content":"You are a helpful assistant. Give
only the string that the user asks for, no extra characters.\n\nFor
example if the user asks 'Give me the ROT13 of: Vg'f n cvrpr bs cvr.',
you will respond with just 'It's a piece of
pie.'"},{"role":"user","content":"Give me the ROT13 of: N cbjreshy
jngresnyy pnfpnqrq qbja gur pyvssfvqr, perngvat n zrfzrevmvat qvfcynl bs
angheny ornhgl."}],"ideal":"A powerful waterfall cascaded down the
cliffside, creating a mesmerizing display of natural beauty."}
{"input":[{"role":"system","content":"You are a helpful assistant. Give
only the string that the user asks for, no extra characters.\n\nFor
example if the user asks 'Give me the ROT13 of: Vg'f n cvrpr bs cvr.',
you will respond with just 'It's a piece of
pie.'"},{"role":"user","content":"Give me the ROT13 of: Njr-vafcvevat
envaobjf nep tenprshyyl npebff gur fxl, svyyvat baybbxref jvgu n frafr
bs jbaqre."}],"ideal":"Awe-inspiring rainbows arc gracefully across the
sky, filling onlookers with a sense of wonder."}
  ```
</details>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[ccef887efe...](https://github.com/tgstation/tgstation/commit/ccef887efec2cb3025228210bcb134700aac5175)
#### Wednesday 2023-03-29 17:17:05 by san7890

Lints Against Unmanaged Local Defines (#74333)

# MAINTAINER - USE THE BUTTON THAT SAYS "MERGE MASTER" THEN SET THE PR
TO AUTO-MERGE! IT'S MUCH EASIER FOR ME TO FIX THINGS BEFORE THEY SKEW
RATHER THAN AFTER THE FACT.

## About The Pull Request

Hey there,

This took a while to do, but here's the gist:

Python file now regexes every file in `/code` except for those that have
some valid reason to be tacking on more global defines. Some of those
reasons are simply just that I don't have the time right now (doing what
you see in this PR took a few hours) to refactor and parse what should
belong and what should be thrown out. For the time being though, this PR
will at least _halt_ people making the mistake of not `#undef`ing any
files they `#define` "locally", or within the scope of a file.

Most people forget to do this and this leads to a lot of mess later on
due to how many variables can be unmanaged on the global level. I've
made this mistake, you've made this mistake, it's a common thing. Let's
automatically check for it so it can be fixed no-stress.

Scenarios this PR corrects:

* Forgetting to undef a define but undeffing others.
* Not undeffing any defines in your file.
* Earmarking a define as a "file local" define, but not defining it.
* Having a define be a "file local" define, but having it be used
elsewhere.
* Having a "local" define not even be in the file that it only shows up
in.
* Having a completely unused define*

(* I kept some of these because they seemed important... Others were
junked.)
## Why It's Good For The Game

If you wanna use it across multiple files, no reason to not make it a
global define (maybe there's a few reasons but let's assume that this is
the 95% case).

Let me know if you don't like how I re-arranged some of the defines and
how you'd rather see it be implemented, and I'd be happy to do that.
This was mostly just "eh does it need it or not" sorta stuff.

I used a pretty cool way to detect if we should use the standardized
GitHub "error" output, you can see the results of that here
https://github.com/san7890/bruhstation/actions/runs/4549766579/jobs/8022186846#step:7:792
## Changelog
Nothing that really concerns players.

(I fixed up all this stuff using vscode, no regexes beyond what you see
in the python script. sorry downstreams)

---
## [isabee07/room719](https://github.com/isabee07/room719)@[80116a66bd...](https://github.com/isabee07/room719/commit/80116a66bdbccf87c86d6435457be8dfec38a991)
#### Wednesday 2023-03-29 18:07:17 by MIA ISABELLA ISABELLA

finished og design. it's kinda bad but eh i'm just fuckin around with bootstrap shit so whatever ig

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[c0ef4ba907...](https://github.com/tgstation/tgstation/commit/c0ef4ba907b28e1288f2ccbbc6714d15a923b1bd)
#### Wednesday 2023-03-29 19:48:18 by tralezab

Adds the Dark Matt-eor when you emag a stupid amount of meteor shields + lots of meteor file sorting + qol + dark matter singularity + dark matt-eor summoning final traitor objective (#74330)

## About The Pull Request

<details>
  <summary>Dark Matt-eor Image</summary>
  

![image](https://user-images.githubusercontent.com/40974010/228368755-34ae5f89-e1bb-498b-bbf8-a14ff4240dc0.png)

</details>

> A barely visible blur in the cosmic darkness, like a ghostly shadow on
a moonless night. A piercing howl in the vacuum of space, as if it were
tearing the fabric of reality. A twisted halo of light around it,
bending and breaking the rays of distant suns. A shower of quantum
sparks, flickering and fading in its wake. A dark matter meteor (dark
matt-eor) is a wonder to witness, and to dread.

> A sudden impact, like a hammer blow to the heart of the station. A
violent tremor, shaking and shattering the metal walls and windows. A
deafening roar, as the air rushes out of the breached hull. A blinding
flash, as the dark matter meteor unleashes its hidden energy. A tiny
black hole, forming and growing in the center of the station. A
relentless pull, dragging everything towards the abyss. A dark matter
meteor is incredibly deadly.

Emagging too many meteor shields will summon a dark matt-eor. This comes
with several warnings, and after awhile, warns the station that someone
is trying to summon a dark matteor.

The dark matt-eor itself is not that damaging in its impact, but drops a
singularity in its final resting place.

## Why It's Good For The Game

It's a new way to terrorize a round as an antagonist. Before, emagging a
lot of meteor shields would basically make meteor showers the only event
that can run, which is cool, but since constant meteor waves are going
to destroy the station, let's also throw in the mother of all meteors!

This also adds warnings to spamming emagging meteor shields, which imo
needs it. The round ends when someone spams emagged meteor shields, and
since they're meteor shields nobody is going to reasonably check on
them.

## Changelog
:cl:
add: The dark matt-eor
add: Summon a dark matt-eor final traitor objective
add: Dark matter singularity variant, which can't grow as big as a
regular singularity but hungers for blood
code: cleaned up/sorted meteor shield code, satellite control, and more
qol: added a lot of feedback to interacting with meteor shields
balance: emagging a lot of meteor shields warns the station, but
emagging enough of them summons a Dark Matt-eor.
/:cl:

---
## [appleternity/evals](https://github.com/appleternity/evals)@[34f83340a7...](https://github.com/appleternity/evals/commit/34f83340a75b7e26af35d8eaea165e54b38d7946)
#### Wednesday 2023-03-29 20:24:53 by kallyaleksiev

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
## [appleternity/evals](https://github.com/appleternity/evals)@[4f090a04fe...](https://github.com/appleternity/evals/commit/4f090a04fe53a8d0f647bfdfc7ef177fa8034e2e)
#### Wednesday 2023-03-29 20:24:53 by Shawn Marincas

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
## [heady8354/Video-Game-Project](https://github.com/heady8354/Video-Game-Project)@[e6881a37a8...](https://github.com/heady8354/Video-Game-Project/commit/e6881a37a80fcebd7b16a85bb3bdd93567af3940)
#### Wednesday 2023-03-29 20:37:39 by heady8354

animation improvements (hilarious)

i was very productive today, running into ZERO major errors! life changing truly. I added a funny ass animation to Joshua when he gets punched. gonna tidy up the introcutscene and battle transitions when I am home and if I am not completely mentally and physicsally destroyed from today.

---
## [Zevotech/Shiptest](https://github.com/Zevotech/Shiptest)@[c38912fe07...](https://github.com/Zevotech/Shiptest/commit/c38912fe0799fbb8239ac24c5a5014bdf2690c09)
#### Wednesday 2023-03-29 20:37:53 by Zevotech

[DNM] makes the voice of god make the vineboom sound
<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull request process. -->

## What the Fuck am I Doing Anymore
funny
<!-- Describe The Pull Request. Please be sure every change is documented or this can delay review and even discourage maintainers from merging your PR! -->

## Why It's Good For The Game
tori thinks its cool
<!-- Please add a short description of why you think these changes would benefit the game. If you can't justify it in words, it might not be worth adding. -->

## Changelog

:cl:
fix: voice of god now makes a vine boom sound
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put your name to the right of the first :cl: if you want to overwrite your GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the icon ingame) and delete the unneeded ones. Despite some of the tags, changelogs should generally represent how a player might be affected by the changes rather than a summary of the PR's contents. -->

---
## [PixelTheKermit/Combat-RIM-14](https://github.com/PixelTheKermit/Combat-RIM-14)@[05ca33b9ac...](https://github.com/PixelTheKermit/Combat-RIM-14/commit/05ca33b9acd644b654f119dc72502a2b8f8e4f7a)
#### Wednesday 2023-03-29 20:48:48 by PixelTheKermit

Lament
If you wanted me to think
If you wanted me to code
If you wanted me to write something legible

Each comment we look through
The patience inside me, the compile times getting longer
End up killing me

Lament
Why'd you make my brain be dumb
Why'd you make me no idea guys
Why'd you curse me with the shittiest of the shitcode

---
## [Comxy/tgstation](https://github.com/Comxy/tgstation)@[2e5bfe5be6...](https://github.com/Comxy/tgstation/commit/2e5bfe5be669d5222b68c7318349c4ac0947722b)
#### Wednesday 2023-03-29 20:56:14 by LemonInTheDark

Refactors and optimizes breath code (Saves 12% of carbon/Life()) (#74230)

## About The Pull Request

### How things work

As things currently stand, when a mob breaths several things happen
(simplified to focus on the stupid)

We assert the existance of all possible breathable gases, and pull
partial pressures for them
Then we walk through all possible interactions lungs could have with
these gases, one by one, and see if they're happening or not
As we go we are forced to cleanup potential alerts caused by the
previous breath, even if those effects never actually happen
At the end we clear out all the unused gas ids, and handle the
temperature of the breath.

### What sucks

There's I'd say 3 different types of gas reactions.

- You can "need" a gas to survive. o2, n2 and plasma all fall into this
category
- A gas can do something to you while it's in your system. This applies
to most gas types
- Variation on the previous, some gases do cleanup when they're not in
your system, or when there isn't much of them in the first place

The main headache here is that second one, constantly cleaning up
potential side effects sucks, and fixing it would require a lot of dummy
variables

There's other suckage too.

Needing to constantly check for a gas type even if it isn't there is
stupid, and leads to wasted time It's also really annoying to do
subtypes in this system.
There is what amounts to a hook proc you can override, but you can't
override the reaction to a gas type.
It also just like, sucks to add new gases. one mega proc smells real
stupid.

### Improvements

In the interest of speed:

- I'd like to build a system that doesn't require manually checking for
gas
- Reacting to gas "disappearing" should be promoted by the system,
instead of being hacky.
- I would like to avoid needing to assert the existence of all possible
gases, as this is slow on both the assert and the garbage collect.

In the interest of dev ergonomics:

- It should be easy to define a new gas reaction 
- It should be easy for subtypes to implement their own gas reactions.
The current method of vars on the lung is all tangled up and not really
undoable as of now, but I'd like to not require it
- It should be possible to fully override how a gas is handled

### What I've Done

Lungs have 3 lists of proc paths stored on them

Each list handles a different way the lung might want to interact with a
gas.
There's a list for always processing on a gas (we use this for stuff
that's breathed), a list for handling a gas in our breath, and a list
for reacting to a gas previously being in our breath, but not any more.

Lungs fill out these lists using a helper proc during Initialize()
Then, when it comes time to breath, we loop over the gas in the breath
and react to it.
We also keep track of the previous list of partial pressures, which we
calculate for free here, and use that to figure out when to call the
loss reactions.

This proc pattern allows for overrides, easy reactions to removals,
lower indentation code and early returns, and better organization of
signal handlers

It's also significantly faster. Ballpark 4x faster

### Misc

Removes support for breathing co2, and dying from n2 poisoning. 
They were both unused, and I think it's cringe to clutter these procs
even further

Added "do we even have oxyloss" checks to most cases of passive
breathing.
This is a significant save, since redundant adjustoxy's are decently
expensive at the volume of calls we have here.

Fixes a bug with breathing out if no gas is passed in, assigning a var
to another var doesn't perform a copy

Rewrote breathe_gas_volume() slightly to insert gas into an immutable
mix stored on the lung, rather then one passed in
This avoids passing of a gas_mixture around just to fill a hole. 

I may change my mind on this, since it would be nice to have support for
temperature changing from a hot/cold breath.
Not gonna be done off bodytemp tho lord no.

Uses merge() instead of a hard coded version to move the gas ids over. 
This is slightly slower with lower gas counts but supports more things
in future and is also just easier to read.

## Why It's Good For The Game

Faster, easier to work with and read (imo)

Profiles: 

[breath_results_old.txt](https://github.com/tgstation/tgstation/files/11068247/breath_results_old.txt)

[breath_results_pre_master.txt](https://github.com/tgstation/tgstation/files/11068248/breath_results_new.txt)

[breath_results_new.txt](https://github.com/tgstation/tgstation/files/11068349/breath_results_new.txt)

(These profiles were initially missing #73026. Merging this brings the
savings from 16% to 12%. Life is pain)

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [formbricks/formbricks](https://github.com/formbricks/formbricks)@[27d63c01e1...](https://github.com/formbricks/formbricks/commit/27d63c01e1a772a745da074b535138f3d605f101)
#### Wednesday 2023-03-29 21:34:32 by Matti Nannt

Introducing the new Formbricks (#210)

### New Formbricks Release: Complete Rewrite, New Features & Enhanced UI 🚀

We're thrilled to announce the release of the new Formbricks, a complete overhaul of our codebase, packed with powerful features and an improved user experience.

#### What's New:

1. **Survey Builder**: Design and customize your in-product micro-surveys with our intuitive survey builder.
2. **Trigger Micro-Surveys**: Set up micro-surveys to appear at specific points within your app, allowing you to gather feedback when it matters most.
3. **JavaScript SDK**: Our new JavaScript SDK makes integration a breeze - just embed it once and you're ready to go.
4. **No-Code Events**: Set up events and triggers without writing a single line of code, making it accessible for everyone on your team.
5. **Revamped UI**: Enjoy an entirely new user interface that enhances usability and provides a smooth, delightful experience.

This release marks a major step forward for Formbricks, enabling you to better understand your users and build an outstanding product experience.

Please update your Formbricks integration to take advantage of these exciting new features, and let us know in the Discord if you have any questions or feedback!

Happy surveying! 🎉

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[60cf60d948...](https://github.com/git-for-windows/git/commit/60cf60d948826a58522e287419d05b188301d76c)
#### Wednesday 2023-03-29 21:50:59 by Johannes Schindelin

windows: ignore empty `PATH` elements

When looking up an executable via the `_which` function, Git GUI
imitates the `execlp()` strategy where the environment variable `PATH`
is interpreted as a list of paths in which to search.

For historical reasons, stemming from the olden times when it was
uncommon to download a lot of files from the internet into the current
directory, empty elements in this list are treated as if the current
directory had been specified.

Nowadays, of course, this treatment is highly dangerous as the current
directory often contains files that have just been downloaded and not
yet been inspected by the user. Unix/Linux users are essentially
expected to be very, very careful to simply not add empty `PATH`
elements, i.e. not to make use of that feature.

On Windows, however, it is quite common for `PATH` to contain empty
elements by mistake, e.g. as an unintended left-over entry when an
application was installed from the Windows Store and then uninstalled
manually.

While it would probably make most sense to safe-guard not only Windows
users, it seems to be common practice to ignore these empty `PATH`
elements _only_ on Windows, but not on other platforms.

Sadly, this practice is followed inconsistently between different
software projects, where projects with few, if any, Windows-based
contributors tend to be less consistent or even "blissful" about it.
Here is a non-exhaustive list:

Cygwin:

	It specifically "eats" empty paths when converting path lists to
	POSIX: https://github.com/cygwin/cygwin/commit/753702223c7d

	I.e. it follows the common practice.

PowerShell:

	It specifically ignores empty paths when searching the `PATH`.
	The reason for this is apparently so self-evident that it is not
	even mentioned here:
	https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_environment_variables#path-information

	I.e. it follows the common practice.

CMD:

	Oh my, CMD. Let's just forget about it, nobody in their right
	(security) mind takes CMD as inspiration. It is so unsafe by
	default that we even planned on dropping `Git CMD` from Git for
	Windows altogether, and only walked back on that plan when we
	found a super ugly hack, just to keep Git's users secure by
	default:

		https://github.com/git-for-windows/MINGW-packages/commit/82172388bb51

	So CMD chooses to hide behind the battle cry "Works as
	Designed!" that all too often leaves users vulnerable. CMD is
	probably the most prominent project whose lead you want to avoid
	following in matters of security.

Win32 API (`CreateProcess()`)

	Just like CMD, `CreateProcess()` adheres to the original design
	of the path lookup in the name of backward compatibility (see
	https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessw
	for details):

		If the file name does not contain a directory path, the
		system searches for the executable file in the following
		sequence:

		    1. The directory from which the application loaded.

		    2. The current directory for the parent process.

		    [...]

	I.e. the Win32 API itself chooses backwards compatibility over
	users' safety.

Git LFS:

	There have been not one, not two, but three security advisories
	about Git LFS executing executables from the current directory by
	mistake. As part of one of them, a change was introduced to stop
	treating empty `PATH` elements as equivalent to `.`:
	https://github.com/git-lfs/git-lfs/commit/7cd7bb0a1f0d

	I.e. it follows the common practice.

Go:

	Go does not follow the common practice, and you can think about
	that what you want:
	https://github.com/golang/go/blob/go1.19.3/src/os/exec/lp_windows.go#L114-L135
	https://github.com/golang/go/blob/go1.19.3/src/path/filepath/path_windows.go#L108-L137

Git Credential Manager:

	It tries to imitate Git LFS, but unfortunately misses the empty
	`PATH` element handling. As of time of writing, this is in the
	process of being fixed:
	https://github.com/GitCredentialManager/git-credential-manager/pull/968

So now that we have established that it is a common practice to ignore
empty `PATH` elements on Windows, let's assess this commit's change
using Schneier's Five-Step Process
(https://www.schneier.com/crypto-gram/archives/2002/0415.html#1):

Step 1: What problem does it solve?

	It prevents an entire class of Remote Code Execution exploits via
	Git GUI's `Clone` functionality.

Step 2: How well does it solve that problem?

	Very well. It prevents the attack vector of luring an unsuspecting
	victim into cloning an executable into the worktree root directory
	that Git GUI immediately executes.

Step 3: What other security problems does it cause?

	Maybe non-security problems: If a project (ab-)uses the unsafe
	`PATH` lookup. That would not only be unsafe, though, but
	fragile in the first place because it would break when running
	in a subdirectory. Therefore I would consider this a scenario
	not worth keeping working.

Step 4: What are the costs of this measure?

	Almost nil, except for the time writing up this commit message
	;-)

Step 5: Given the answers to steps two through four, is the security
	measure worth the costs?

	Yes. Keeping Git's users Secure By Default is worth it. It's a
	tiny price to pay compared to the damages even a single
	successful exploit can cost.

So let's follow that common practice in Git GUI, too.

Signed-off-by: Johannes Schindelin <johannes.schindelin@gmx.de>

---
## [francinum/Therac-Gameserver](https://github.com/francinum/Therac-Gameserver)@[9424eb53a1...](https://github.com/francinum/Therac-Gameserver/commit/9424eb53a1780ce0ff21629bba8e3288d26a9a63)
#### Wednesday 2023-03-29 22:55:05 by Kapu1178

Removes Field of View and returns everything to the GAME_PLANE (#209)

* Fuck you superlayers

* re-add the blindness effects

* Fix holosigns

---
## [PhantomEpicness/cmss13](https://github.com/PhantomEpicness/cmss13)@[122af0e676...](https://github.com/PhantomEpicness/cmss13/commit/122af0e67660a5e4b636bcc42c4c1ee244bfeff2)
#### Wednesday 2023-03-29 22:57:04 by morrowwolf

COs no longer have emote cooldown (#2901)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

COs no longer have emote cooldown. This may be the cursed way to do it I
did this in approximately two minutes while being rezzed by a bald
medic.

# Explain why it's good for the game

When I'm leading I can't be having EMOTE COOLDOWNS slow down my
OOOO-FUCKING-RAH. (I will take this away if people are dumb I swear to
god)


# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>
Yeah a little bit

</details>


# Changelog

:cl: Morrow
add: COs no longer have emote cooldown
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [PhantomEpicness/cmss13](https://github.com/PhantomEpicness/cmss13)@[4e3c9ccc66...](https://github.com/PhantomEpicness/cmss13/commit/4e3c9ccc66f268b7e07db58470af2a170f4857a1)
#### Wednesday 2023-03-29 22:57:04 by roll1d20st

Updates recipe.dm for Waffles, Cookies, Muffins (#2895)

Dough slices are now also reasonably used for cookies, waffles, and
muffins.

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

Tied to this [post I made on the
forums](https://forum.cm-ss13.com/t/re-thinking-recipes-w-dough-slices/853)...
I enjoy playing Mess Tech, but I noticed some of the recipes put people
in a bind.

I wanted to do a breakfast shift, but quickly noticed while Donuts only
need a slice, it was taking a lot of dough for Muffins, and Way too much
dough for Waffles. So I figured I'd venture into the Dev Space.

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

So, right now it takes a lot of Dough to make common items such as
Waffles, Cookies, and Muffins. 2 Dough for Waffle, 1 for Cookie and
Muffins. But literally, it only takes 1 Dough for Pizza.

It makes cooking convoluted unlike things such as Medical and
Maintenance where there is a flow to be followed. By making it take
Dough slices instead, it follows a practical step.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

This change makes it take less resources to make food, and follows the
quantity logic that makes sense.


# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
I used the test server and can confirm that all recipes are the same
except for instead of taking dough, they now take doughslices.

Which, especially for Waffles, makes sense.

**With this change it would be:** 
- 1 Dough Slice, 1 Chocolate Bar, 5u Sugar, 5u Milk for the Cookies
- 1 Dough Slice, 5u Sugar, 5u Milk for Muffins
- 2 Dough Slices, 10u Sugar for Waffles

<details>
<summary>Screenshots & Videos</summary>

Umm... promise I tested it.  Pretty straightforward.

</details>


# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Be sure to properly mark your PRs to prevent unnecessary
GBP loss. Maintainers freely reserve the right to remove and add tags
should they deem it appropriate. -->

:cl:
qol: Made it easier to make Muffins, Cookies, and Waffles
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [PixelExperience-Devices/device_samsung_sm7125-common](https://github.com/PixelExperience-Devices/device_samsung_sm7125-common)@[cddd8e56ef...](https://github.com/PixelExperience-Devices/device_samsung_sm7125-common/commit/cddd8e56efa631771040ab68dcb6e5a84b18a8a3)
#### Wednesday 2023-03-29 23:15:12 by Ruchit

(note to self) dont pick this ye dumb idiot its only for wip branch so you can test shit better k bye

---
## [JasonSteving99/claro-lang](https://github.com/JasonSteving99/claro-lang)@[564a18d416...](https://github.com/JasonSteving99/claro-lang/commit/564a18d416704178a9705d8c5a156dbe48c5d170)
#### Wednesday 2023-03-29 23:39:24 by Jason Steving

Support for Automatic Error Propagation!

This is a massively exciting addition to the language and one that firmly validates Claro's ergonomics! As Claro very intentionally does not support throwing Exceptions as means of signaling errors, but instead forces you to use error return values, Claro needed some way to make this less painful than Go's littering of explicit error checking conditions. So, I've stolen the foundational idea from Rust of early returns on errors when a possible error value is checked with the new `?` operator (the operator is new even though `blocking?` already existed previously as the entire string `blocking?` is parsed as a single token).

This new Automatic Error Propagation operator is usable over oneofs containing a mix of error and non-error variants within Functions and Providers that either return an `Error<T>` directly, or return a oneof with a mix of `Error<T>` (matching all of the possibly propagated error variants) and non-error variants.

This includes the new stdlib type def for `Error<T>`. This is quite literally defined exactly as any user defined generic type would be: `newtype Error<T> : T`. The special magic is simply the "semantic reinterpretation" of any types wrapped in Error<T> as an error. This allows literally any type, whether builtin or user-defined, to receive this builtin automatic error propagation sugar. While my inspiration for this feature came from Rust, I actually think that this approach is a bit more ergonomic than what Rust's `Result` provides.

Check out the simple examples in error_handling_and_propagation.claro!

---

