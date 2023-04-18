## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-04-17](docs/good-messages/2023/2023-04-17.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,242,882 were push events containing 3,451,565 commit messages that amount to 257,214,427 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 52 messages:


## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[d21522626d...](https://github.com/TaleStation/TaleStation/commit/d21522626dbd4d08cb1a6ee5ffea93a7433bdb06)
#### Monday 2023-04-17 00:18:17 by TaleStationBot

[MIRROR] [MDB IGNORE] Tones down the power of nitrous oxide, the reagent. Makes heparin a bit harder to fix to compensate (#5395)

Original PR: https://github.com/tgstation/tgstation/pull/74703
-----

## About The Pull Request

Nitrous Oxide, rather than directly subtracting blood volume per tick,
instead applies the anticoagulant trait ''TRAIT_BLOODY_MESS''. It shares
this with heparin.

However, unlike, heparin, coagulants like Sanguirite will remove the
trait and allow for continued clotting while the reagent is present,
neutering the nitrous oxide's anticoagulant effects (but not the other
parts)

Heparin, on the other hand, will purge Sanguirite while it is in you
system. You must remove the heparin before you can apply an
anticoagulant.

## Why It's Good For The Game

Nitrous Oxide, on top of being a knockout chem that causes you to
suffocate and become drowsy, just starts deleting blood rapidly. About
15 units of it, standard in a syringe, will kill you in about a minute,
but you'll be unconscious for most of it (you'll be at around 50%-60%
blood by the time it is out of your system, so as good as dead). It
doesn't matter that it metabolizes quickly either, since because it
isn't a toxin, it doesn't get purged by livers/improved livers, so you
will probably metabolize all of the chem that enters your system.

Blood is one of those 'hidden damage types', a bit like brain damage.
Once you start losing it _directly,_ you probably don't have a lot of
options to resolve it (unlike a bleed, which you do in various manners),
and the means of causing blood loss has been mostly pretty well
controlled as of late. Heparin directly interacts with wounds as a good
example.

Blood loss is also tied into oxyloss, which is another very mean damage
type in that it causes you to fall into unconsciousness at 50 damage, so
significantly more lethal than normal damage, kept in check by the fact
that breathing restores some of it. Nitrous oxide, you might note,
causes you to stop breathing.

It's cheaper to make than either heparin or lexorin, and since it isn't
a toxin like those chems, it is able to circumvent a few game mechanics
to simply just start killing you. It does the work of chloral hydrate,
lexorin and heparin while it has a remarkably easy recipe.

Following the example of how lexorin was pulled into line, and
consistency with heparin, I've made nitrous oxide an anticoagulant that
may or may not come into play as one. I think this is more up to date
with the state of toxins and chem warefare as a whole, and works with
the relative ease in making nitrous oxide. And it has been this way for
about 5 years, before we got wounds.

(did I mention that nitrous oxide is also an explosive if it gets hot
enough?)

## TL;DR

I think a chem with a pretty basic recipe shouldn't be doing the work of
5 other, more complicated, chemicals while also not being a toxin and
also not interacting with the wounds system or purity system whatsoever.
And being an explosive.

## Changelog
:cl:
balance: Nitrous oxide, the reagent, increases bleed rate from wounds
rather than directly subtracting blood. It can be counteracted using
coagulants (such as those in epipens).
balance: Heparin purges coagulants. You have to remove heparin from
someone's system before you can use coagulants.
/:cl:

---------

Co-authored-by: necromanceranne <40847847+necromanceranne@users.noreply.github.com>
Co-authored-by: san7890 <the@san7890.com>

---
## [clintjedwards/gofer](https://github.com/clintjedwards/gofer)@[e5652d962c...](https://github.com/clintjedwards/gofer/commit/e5652d962c238d710a334bd2a978a30eb3057145)
#### Monday 2023-04-17 01:04:16 by Clint J Edwards

refactor: Refactor the config package

Previously the configuration for the app was home grown
it used many different config libraries to create a hierarchy
of configuration.

This worked well, but there was a lot of hacks to make up for little
places where the many libraries did not fit perfectly(namely,
the hcl parser code was kinda shit and we had struct tags for
every library)

To fix this and make the configuration code much simplier I swapped
the config package to use https://github.com/knadh/koanf which
greatly simplifies a lot of hoemgrown code. HCL time.Duration parsing
works right out of the box where previously there was a lot of code
to make it work.

The tradeoff is that envs now need to be separated by double underscores
in order to be understood properly. Which can be a confusing interaction
but the maintainabiliy boost is probably worth writing a bit of
extra documentation.

---
## [clintjedwards/gofer](https://github.com/clintjedwards/gofer)@[966650d9ec...](https://github.com/clintjedwards/gofer/commit/966650d9ec00b3d468385f50845c3583d1fb21cf)
#### Monday 2023-04-17 01:04:16 by Clint J Edwards

feat: Pipelines are now versioned

In order to eventually have canary-able deployments in Gofer we must
first support versioned pipelines.

This allows us to:
* Have a good target in which to roll back and forward.
* Understand what we are gaining and losing on each change.
* Track each update as it happens.

This is not easy though as pipelines have parts which are easy to version
(namely the config) and parts which are much harder to version (how do
we handle the cutting over of triggers?).

Because of this nuance, we've had to redesign a lot of earlier
assumptions for how Gofer models worked. This was a major refactor and
since I was here I made a few other large sweeping changes.

* Full storage package refactor: The storage layer was hard to use,
brittle, and inflexible. I've refactored it, leaning a bit more on
sqlx and going back to basics. I tried to make the storage package
work in the past by keeping the domain models to a minimum. I've since
learned this does not work once things become reasonably complicated. One
of the main refactors to the storage package is the introduction of
dedicated storage models. This means that I have to write a bunch of
boilerplate code to switch from in-memory models to the storage ones,
but the looser coupling is worth it. More storage refactors coming
as I learn what works at large scale and what doesn't.
https://github.com/go-jet/jet looks interesting.

* Removal of Triggers as Pipeline configuration: I desparately wanted
to have pipeline configurations encompass everything a pipeline would
have to offer, so that it was easy to look at a config and know exactly
what was going on in a particular pipeline. Triggers were a pain in the
ass though. Triggers unfortunately occupy a very special place in Gofer's
archetecture. Without triggers nothing really gets done. And so allowing
the user to apply all the same functionality to triggers as they would
with any other deployment was short-sighted. Triggers don't make a lot
of sense as a canary deployment. Triggers aren't ephemeral, they are
either on or their off. No in-between.

Instead Triggers can now be added to your pipeline via the command line.
This way trigger subscriptions aren't held down by the paradigms of
configuration change.

* Pipelines are now versioned: Not only have we added versions to pipelines,
but they now have deployments and configurations and metadata and a lot
of smaller loosely coupled parts so that they aren't a huge data monolith.
This means a lot of breaking changes for outward (and inward for that matter)
apis.

* Renamed triggers to extensions: We've moved triggers to be their
own thing and gave them extra powers to support pipelines. They no
longer only have to trigger pipeline but can do things like
notify the user.

* Just lots of general breakages everywhere: Pretty much a large percentage
of things just aren't the same anymore.

---
## [HeapsOfRam/GAMENet](https://github.com/HeapsOfRam/GAMENet)@[7d82a81a5c...](https://github.com/HeapsOfRam/GAMENet/commit/7d82a81a5c4609166d926d6ff5b1a3246147c30b)
#### Monday 2023-04-17 01:06:30 by HeapsOfRam

run as containers (#1)

* containerizing the logic

this commit puts the logic into a container with access to gpu
resources in order to run the training (and subsequently the
evaluation). i have not 100% validated the evaluation within the
container yet, but i feel it should work with the changes i have
made. generally, however, the training works within the docker
container.

i technically use podman as the container engine for this, with
the nvidia-runtime-container enabled so that it can access the
gpu resources. i also need to run in privileged mode to get the
container to have access to the gpu.

there were some minor modifications to the code to get replicate
the exact study (mainly, changed the jaccard similary score import
to just jaccard_score). i have gotten this working on my system in
totality, and have frozen the pip environment i had in order to
generate the requirements.txt. the dockerfile also pulls a cuda image
to gain access to gpu resources, and installs the proper version
of python to unpickle the needed files. finally, i have added scripts
in order to build and run the container and to train and evaluate
the model once inside the container.

there is still more work to be done to include the planned ablations
and additions. i also want to figure out ways to output the model
file so that training and evaluation can happen in separate containers
(ie, can i use a volume to store the model file on the host os and
load it from the host os into the evaluation container? what other
options do i have here? etc). i also am currently using the prepared
data from the github repository. i want to start working to perform
the data preparation step in a container as well, which would also
give me the benefit of potentially updating the python version since
that was primarily chosen to support loading in the pickle files
that were included in the repository. if i prepare the data separately,
i may be able to do so with newer python versions. finally, it may
be worth creating some sort of flask or api application that can
accept requests to re-enable some of the command line arguments that
made the original code more flexible.

these are all things to be done in future commits, but how far i will
get with each of these will be determined later. the most important
is getting containerization to work and starting the ablations.

* data preparation logic

Previously, I was able to get the containerized logic working to
train and evaluate the model. However, this was using the pickled
data files that were already provided by the original authors to
make the replication of the study simpler. There was also code that
the authors wrote in order to prepare the data and output the pickle
files that would later be used. I extracted out the code from the
python notebook included in the repository into separate python
files to prepare the data with, and added the execution of these
python files as steps in the Docker container as part of the
overall pipeline. Now the code works fully end-to-end -- data
preparation, model training, and model evaluation. The only piece
that is not automated at the moment is downloading the data itself.
I am considering adding this step as well, but it may be tricky
since the DDI data was provided as a Dropbox download link. Anyway,
now the code is working and I can focus on ablations as the next
steps. I may try to simplify the code that I modified in order
to make it cleaner, since my modifications were quite messy as a
result of various trials and errors. However, I want to commit the
working code now as a base for any future enhancements.

There are some idiosyncrasies as a result of some of the choices I
made. For example, in the Docker file I copy over all of the files,
and then copy the data processing logic over again. This is because
I need this context to unpickle the files. While the original pickle
files were likely able to reference the original EDA code provided
by the authors, when I extracted the logic into separate files this
caused some challenges. To avoid duplicating the files themselves,
I simply copy the files into the Docker container multiple times.

I have added the full flow as part of a "pipeline" executed in a
bash script by the Dockerfile. One thing to note is that now the
grades and feedback for the project proposal have been released.
With the feedback, I learned that the full GAMENet pipeline is
already integrated into the pyhealth library. Though this effort
so far has already taken some time, I may want to spend some time
investigating the pyhealth implementation as it may even be simpler
than what I have currently -- plus it would be valuable to learn
more about! I may investigate in a future commit or a different
repository, but we will see what makes the most sense.

* baseline logic

now the logic to train and evaluate the baselines has been included
in the container. this has been done rather messily and a bit
hastily, so i plan to refactor this a bit in a future commit. however,
the code in its current state represents a runnable docker container
that succeeds in the following:
- prepare the data for training purposes, including ddi graph and
  ehr data
- trains the GAMENet model on the prepared data and evaluates it
- trains the DMNC model on the prepared data and evaluatates it
- trains the LR model on the prepared data and evaluates it
- trains the LEAP model on the prepared data and evaluates it
- trains the RETAIN model on the prepared data and evaluates it

at least, my runs seem to be successful. training the dmnc model
took quite a while, ~20 hours or so on my Nvida 1080 GPU. one thing
i noticed was that only 25% of the GPU memory seemed to be used at
any one time. i wonder if this is normal or if i can somehow adapt
the data loader patterns or something to enable more data throughput
somehow ...

one of the most important things i had to do for this was to upgrade
my version of `torch`. i upgraded quite a bit, to version 1.4; after
this, the DMNC model was able to train. before that upgrade, the
model training had issues calculating the gradient for some operations
it regarded as self-assignment. anyway, now it trains though for
a long time. all of the other baselines seem to be working from
what i can tell as well.

i want to make the bash script cleaner, and add command line arguments
to evaluate whether baseline evaluation should be run. i also want
to make some of the other code cleaner as well. i can probably
abstract some of my rougher logic out into the utils file, and find
a better way to handle my paths. as i mentioned, this was a bit of
a "rough draft" attempt but since i have it working before project
draft submission i will commit it for now. hopefully in the next
commit i can make a lot of this stuff more clean and user friendly
before merging the pr.

* refactor

This commit serves primarily to refactor the existing code, to
make it a bit easier to follow and user-friendly. There are a few
central changes that contribute to this.

First, I've renamed the `train_and_eval_model.sh` script to be just
`gamenet.sh`. I felt this was more accurate, since I am interested
in running the full GAMENet "pipeline" instead of just training
and eval; this includes preparing the data and training and evaluating
the baselines, along with the GAMENet model itself. Also in this
file, I have modularized the various logic into functions that can
be controlled via simple boolean flags. My intention is to add
command-line arguments and flags to this bash script so that these
flags can be set more dynamically, but for now this helps to easily
toggle which parts of the pipeline I want to enable/disable.

I also made some changes to the Dockerfile and the structure of the
container. Instead of copying the repository as-is into the container
and then duplicating certain files as necessary and dealing with
convoluted path structure, I now copy in the files I want one-by-one
into the main directory of the container. This simplifies the imports
and the copies, so that every file only needs to be copied once.
It also simplifies the path structure for the pickle and data files.
Thus, I also needed to make changes to some of the training and
evaluation code, as well as the data preparation logic.

Another change here is that I created some helpful utilities in
the utils file. This includes evaluating whether or not the TEST
variable for a given model should be true, as well as getting the
path that the pickle files should be saved to. This will allow me
to simplify any changes that are made here, so that from now on
I only need to update the path in the utilities function instead of
across the entire project.

I do still want to do a second refactor commit, where I clean up the
structure of the repository itself. I think I can move all of the
files out of the `data/prepare_data/` directory and just put them
in the `data/` directory. I can also simplify how the Dockerfile
copies the directories and files into the container to reduce the
number of steps in the build process. I also plan to add a simple
alias for docker=podman that can be commented out for anyone who
wants to use docker instead of podman. Finally, once I add a bit
of documentation to the README and different areas, I plan to merge
this PR.

* further refactoring

I think my repository is finally starting to look clean enough to
merge. It was a bit of a messy path as I continued to add new things
and experiment, but I am comfortable with the current state of the
code and the organization. I think the final steps before merging
the PR and submitting the progress report will be to add some
documentation and maybe just a little bit more cleanup (for example
cleaning up and adding additional comments).

Mostly, this commit involves moving files around. I had created
a `data/prepare_data` directory that I was using because I was
nervous to touch any mission-critical files. Now that I have done
various experiments, I feel more comfortable with how everything
works. So, I was able to move the files I wanted to and organize
it a bit better than I had in my initial commits for this PR.
Pickle files now reside in their own directory, and while these files
do get copied into the container, they will get deleted if the bash
entrypoint's prepare data flag is set to be true. I also updated the
util pickle path to follow with this new organization. I also moved
the data preparation logic up to the `data/` directory itself.

I reordered a bit of the logic in the `gamenet.sh` entrypoint, just
to make things a bit easier to follow. I haven't added command-line
arguments to the bash script or anything yet, but that may come in
a later commit. For now I am comfortable with how this works, and
can always extend it later. I have verified that all of the models
seem to train successfully (or at least start to do so). After the
progress report is submitted, I will make sure to run the entire
pipeline again to verify that the full training and evaluation is
working. I have validated this for some of the smaller, easier to
train models, but not for everything.

* documentation

I cleaned up some final things that I wanted to address before
finalizing this PR; this mostly comes down to removing comments in
the various python files.

Additionally, I added an alias for docker so that it refers to podman
in the build script. Now, this line can easily be commented out in
order to use docker instead, while still letting me use podman in
general. As mentioned, podman should mostly be a drop-in replacement
for docker. I have also added a cleanup script that helps me track
the commands I need to free up the resources on my system.

Finally, I have actually made updates to the README file. I have
kept the original README file in tact, so that it can be referenced
as needed. I also did not want to lose any details that the original
authors included for now. Instead, I have added my sections at the
top of the README file. This documentation shows how one can take
this code and run it as docker or podman containers leveraging the
NVIDIA Container Runtime. This allows the containers to have access
to GPU resources as needed. Now I feel I can merge the PR and tag
a release regarding the project's progress report.

---
## [Angry-Pomeranian/RMIT-PROJECTS-ASSESSMENTS](https://github.com/Angry-Pomeranian/RMIT-PROJECTS-ASSESSMENTS)@[d0a56ea3c0...](https://github.com/Angry-Pomeranian/RMIT-PROJECTS-ASSESSMENTS/commit/d0a56ea3c0d8620f7c9cc367e15451dc5f50b7cf)
#### Monday 2023-04-17 01:31:19 by Nicole

Add files via upload

Task instructions 
Summary and Purpose of Assessment

The purpose of this assessment task is for you to complete a series of tasks that focus on managing and improving the security infrastructure of an organisation.

 

This project task requires you to complete the following tasks:

Read information on Star education (page 3) and their security policies, located in Appendix A of this document. This information will assist you in completing the assessment.
You will need to answer each project task on a separate document and submit this assessment for marking.
Your responses will be assessed as per the marking criteria outlined in Section B of this document.
 

Assessment Instructions

Read and complete all seven (7) sections of the project.
This assessment task requires you to address Star education’s newly implemented security policies (located in Appendix A) and provide extensive research in order to incorporate best practice standards for the organisations security systems, as well as to support the planning and development of the security policies.
You may use class resources and the internet to assist you in completing this assessment task.
You will need to complete your task using a separate document, making sure to include your name and student ID.
Seek assistance from your teacher if you need clarification with any of the questions. Your teacher will go through this assessment during class time to answer any questions.
Student will be observed undertaking this assessment task by a qualified
Complete all sections as directed below before handing in your assessment for marking.
What

You need to complete all the tasks of Part 1 in this assessment.

Please refer Section B /Rubric for specific details.

Project_VU21995_Task1_Student_220802.docxDownload Project_VU21995_Task1_Student_220802.docx

Download the above file to complete all Part 1 tasks. Make sure to rename your file as instructed.  Upon completion, upload the completed file on canvas and submit.

Please note, all the tasks appearing below are repeated in the above file.

  

Star education

Star education are a TAFE provider located in Melbourne. They host an array of courses and are home to approximately 900 students – both local and international.

Recently, Star education have decided to review their cyber security practices to ensure they are equipped to manage any cyber threats that may come their way.

The Director is currently in a phase of revising many of the TAFE’s policies and has a keen interest to ensure the safety of the TAFE’s students and staff – on all levels.

Many staff members have worked at Star for a long time and therefore, may resist the implementation of new policies. This is something to always think about – managing change.

Security training for staff is often seldom complete and students receive basic security training during their first weak at the TAFE.

In addition, the organisation does invest in some security tools, although these are at a basic level that are not always best suited to the growing size of the TAFE.

The organisational structure includes:

 

Academic operations

Curriculum and teaching

Student engagement and partnerships

Corporate services

Strategy, performance and governance

VET
Short courses
International academic operations
Curriculum unit
Professional teaching practice
Learning environments
Future students
International partnerships
Finance
Human resources
Marketing
Legal services
IT
Strategy and planning
Risk and compliance
Governance
Education quality and accreditation
 

You will find Star education’s cyber security-related policies – data breach, remote access and email usage policies located in Appendix A of this document.

These policies are new and have been implemented as part of the TAFE’s overall cyber security strategy.

Task details

After reviewing Star education’s information (above) and their three (3) policies located in Appendix A of this document, complete the following project tasks listed below. You will need to complete your answers in a separate document, making sure to include your name and student ID.

 

Project Part 1

Section 1: Information and security policies

Review each of Star education’s policies and note down at least three (3) implications of implementing these policies. Think about the effects on the students, staff and the organisation itself.
Outline the likely team members who would be involved in reviewing these policies before they are implemented.
Suggest three (3) work habits that may impact on the successful implementation of the three (3) policies. For example, the staff members have been employed for a long time and therefore may be hesitant to update their passwords often. Provide a brief explanation as to why each work habit may impact on the policy implementation.
Evaluate Star education’s configuration within the organisation and outline the implications with regards to implementing cyber security policies. You will need to evaluate the organisation’s configuration against change management principles. This will include evaluating the following organisational information and reviewing how each of these areas are affected by change management:
Job roles
Student profiles
Management teams
Current systems that relate to cyber security
 

Section 2: Risk assessment 

Conduct an audit of Star education’s current security tools and infrastructure. Provide at least one (1) example of the following types of tools:
Packet sniffers and password auditing tools
Penetration testing tools
Web vulnerability scanning tools
Encryption tools
Security hardware
Network security monitoring tools
Physical infrastructure tools (e.g. swipe cards, cameras etc.)
 

B. Outline Star education’s baseline for their security infrastructure. Think about the most essential components of the organisation that is their ‘heart and soul’ of security (i.e. key security elements). For example, there may be four (4) servers that provide/store/host the organisation’s most important data, thus these servers are the baseline that need to be secure as they can be.

C. Conduct a risk assessment on the organisation’s systems and human operations. For this question, you will need to provide an extensive assessment that includes any part of risk to the company’s cyber security practices. You may present this information in a table format. When assessing the risks for human operations, ensure you provide details on the types of systems that are affected by human operations, e.g. students interact with emails and local server drives.

To assist your risk assessment, you will need to cover (at a minimum) the following:

Identify company assets– these could be proprietary information, hardware, software, client information, network topology, etc. List at least six (6).
Identify key stakeholders who will be able to assist you in gathering risk assessment data - It’s best to collaborate with other departments to determine other valuable company assets and which ones to prioritise. For this part, list the employees/departments who you will need to collaborate with in order to gather risk assessment data. For each employee/department, outline the type of information they will be able to provide you with.
List the types of threats– detail at least five (5) threats. Think about the specific threats that can affect your organisation and its assets. As an example, some main sources of threats include:
Natural disasters
Human error / malicious intent
System failure
Lack of resources
Cyber attacks
Likelihood of incidents– assess all of your assets’ vulnerability to threats and the likelihood of an incident happening. For this section, you may use a rating system such as; 1 = low risk, 2 = medium risk, 3 = high risk; or a traffic light system – red, green and yellow.
List the repercussions– One or a combination of the following can happen if company assets get impacted by threats: legal action, data loss, production downtime, fines and penalties, negative impact on company reputation, etc. List at least one (1) repercussion for each asset.
Determine controls– Determine what controls are required to mitigate the threats you listed. New controls may need to be implemented or old ones updated to adapt to new and changing threats. You will need to consider the resources required for each threat/risk that will minimise business operations in case of a system outage, etc. Also think about cloud platforms, data storage practices, email systems, infrastructure, employee training, and third-party security policies that will support your controls.
 

Section 3: Security vulnerabilities 

Outline the security infrastructure vulnerabilities of the organisation. For example, vulnerabilities are weaknesses in security that can expose assets to threats, e.g. untrained staff and students etc.
Provide a summary email which outlines these security vulnerabilities, addressing the email to the appropriate areas/management of the organisation.
 

-------------------------END OF Part 1 TASKS---------------------

 

Where

This assessment will take place in class and/or outside of class time, as per your Teacher’s instructions.

 

How

This project will be carried out in two parts. Part 1 comprises of sections 1,2,3. Part 2 comprises of sections 4,5,6,7. Students will be assessed against the criteria listed in the marking guide of this task. Project observation will be carried out during scheduled observation week. To achieve a satisfactory result, students will need to address all criteria satisfactorily.

 

 

 

APPENDIX A – STAR EDUCATION POLICIES

 

 

Data breach policy

1.0 Purpose

The purpose of the policy is to establish the goals and the vision for the breach response process. This policy will clearly define to whom it applies and under what circumstances, and it will include the definition of a breach, staff roles and responsibilities, standards and metrics (e.g., to enable prioritization of the incidents), as well as reporting, remediation, and feedback mechanisms. The policy shall be well publicized and made easily available to all personnel whose duties involve data privacy and security protection.

Star education Information Security's intentions for publishing a Data Breach Response Policy are to focus significant attention on data security and data security breaches and how Star education’s established culture of openness, trust and integrity should respond to such activity. Star education Information Security is committed to protecting Star education's employees, partners and the company from illegal or damaging actions by individuals, either knowingly or unknowingly.         

Background
This policy mandates that any individual who suspects that a theft, breach or exposure of Star education Protected data or Star education Sensitive data has occurred must immediately provide a description of what occurred via e-mail to Helpdesk@Stareducation.org, by calling 555-1212, or through the use of the help desk reporting web page at http://Star education. This e-mail address, phone number, and web page are monitored by the Star education’s Information Security Administrator. This team will investigate all reported thefts, data breaches and exposures to confirm if a theft, breach or exposure has occurred. If a theft, breach or exposure has occurred, the Information Security Administrator will follow the appropriate procedure in place.          

2.0 Scope

This policy applies to all whom collect, access, maintain, distribute, process, protect, store, use, transmit, dispose of, or otherwise handle personally identifiable information or Protected Health Information (PHI) of Star education members. Any agreements with vendors will contain language similar that protects the fund.             

3.0 Policy Confirmed theft, data breach or exposure of Star education Protected data or Star education Sensitive data

As soon as a theft, data breach or exposure containing Star education Protected data or Star education Sensitive data is identified, the process of removing all access to that resource will begin.

The Executive Director will chair an incident response team to handle the breach or exposure.

The team will include members from:

IT Infrastructure
IT Applications
Finance (if applicable)
Legal
Communications
Member Services (if Member data is affected)
Human Resources
The affected unit or department that uses the involved system or output or whose data may have been breached or exposed
Additional departments based on the data type involved, Additional individuals as deemed necessary by the Executive Director
Confirmed theft, breach or exposure of Star education data

The Executive Director will be notified of the theft, breach or exposure. IT, along with the designated forensic team, will analyse the breach or exposure to determine the root cause.

Work with Forensic Investigators

As provided by Star education cyber insurance, the insurer will need to provide access to forensic investigators and experts that will determine how the breach or exposure occurred; the types of data involved; the number of internal/external individuals and/or organizations impacted; and analyse the breach or exposure to determine the root cause. 

Develop a communication plan

Work with Star education communications, legal and human resource departments to decide how to communicate the breach to: a) internal employees, b) the public, and c) those directly affected 

3.2 Ownership and Responsibilities

Roles & Responsibilities:

Sponsors - Sponsors are those members of the Star education community that have primary responsibility for maintaining any particular information resource. Sponsors may be designated by any Star education Executive in connection with their administrative responsibilities, or by the actual sponsorship, collection, development, or storage of information.
Information Security Administrator is that member of the Star education community, designated by the Executive Director or the Director, Information Technology (IT) Infrastructure, who provides administrative support for the implementation, oversight and coordination of security procedures and systems with respect to specific information resources in consultation with the relevant Sponsors.
Users include virtually all members of the Star education community to the extent they have authorized access to information resources, and may include staff, trustees, contractors, consultants, interns, temporary employees and volunteers.
The Incident Response Team shall be chaired by Executive Management and shall include, but will not be limited to, the following departments or their representatives: IT-Infrastructure, IT-Application Security; Communications; Legal; Management; Financial Services, Member Services; Human Resources.
4.0 Enforcement

Any Star education personnel found in violation of this policy may be subject to disciplinary action, up to and including termination of employment. Any third party partner company found in violation may have their network connection terminated.            

5.0 Definitions

Encryption or encrypted data – The most effective way to achieve data security. To read an encrypted file, you must have access to a secret key or password that enables you to decrypt it. Unencrypted data is called plain text;

Plain text – Unencrypted data.

Hacker – A slang term for a computer enthusiast, i.e., a person who enjoys learning programming languages and computer systems and can often be considered an expert on the subject(s).

Protected Health Information (PHI) - Under US law is any information about health status, provision of health care, or payment for health care that is created or collected by a "Covered Entity" (or a Business Associate of a Covered Entity) and can be linked to a specific individual.

Personally Identifiable Information (PII) - Any data that could potentially identify a specific individual. Any information that can be used to distinguish one person from another and can be used for de-anonymizing anonymous data can be considered

Protected data - See PII and PHI

Information Resource - The data and information assets of an organization, department or unit.

Safeguards - Countermeasures, controls put in place to avoid, detect, counteract, or minimize security risks to physical property, information, computer systems, or other assets. Safeguards help to reduce the risk of damage or loss by stopping, deterring, or slowing down an attack against an asset.

Sensitive data - Data that is encrypted or in plain text and contains PII or PHI data.  See PII and PHI above.

 

 

 

Remote access policy

1.       Overview
Remote access to our corporate network is essential to maintain our Team’s productivity, but in many cases this remote access originates from networks that may already be compromised or are at a significantly lower security posture than our corporate network. 

2.       Purpose
The purpose of this policy is to define rules and requirements for connecting to Star education's network from any host. These rules and requirements are designed to minimize the potential exposure to Star education from damages which may result from unauthorized use of Star education resources. Damages include the loss of sensitive or company confidential data, intellectual property, damage to public image, damage to critical Star education internal systems, and fines or other financial liabilities incurred as a result of those losses.

3.       Scope
This policy applies to all Star education employees, contractors, vendors and agents with a Star education-owned or personally-owned computer or workstation used to connect to the Star education network. This policy applies to remote access connections used to do work on behalf of Star education, including reading or sending email and viewing intranet web resources.  This policy covers any and all technical implementations of remote access used to connect to Star education networks.

4.       Policy
It is the responsibility of Star education employees, contractors, vendors and agents with remote access privileges to Star education's corporate network to ensure that their remote access connection is given the same consideration as the user's on-site connection to Star education.

General access to the Internet for recreational use through the Star education network is strictly limited to Star education employees, contractors, vendors and agents (hereafter referred to as “Authorized Users”).  When accessing the Star education network from a personal computer, Authorized Users are responsible for preventing access to any Star education computer resources or data by non-Authorized Users.  Performance of illegal activities through the Star education network by any user (Authorized or otherwise) is prohibited.  The Authorized User bears responsibility for and consequences of misuse of the Authorized User’s access.  For further information and definitions, see the Acceptable Use Policy.

Authorized Users will not use Star education networks to access the Internet for outside business interests.

For additional information regarding Star education's remote access connection options, including how to obtain a remote access login, free anti-virus software, troubleshooting, etc., go to the Remote Access Services website (company URL).       

4.1 Requirements

4.1.1  Secure remote access must be strictly controlled with encryption (i.e., Virtual Private Networks (VPNs)) and strong pass-phrases. For further information see the Acceptable Encryption Policy and the Password Policy.

4.1.2  Authorized Users shall protect their login and password, even from family members.

4.1.3  While using a Star education-owned computer to remotely connect to Star education's corporate network, Authorized Users shall ensure the remote host is not connected to any other network at the same time, with the exception of personal networks that are under their complete control or under the complete control of an Authorized User or Third Party.

4.1.4  Use of external resources to conduct Star education business must be approved in advance by InfoSec and the appropriate business unit manager.

4.1.5  All hosts that are connected to Star education internal networks via remote access technologies must use the most up-to-date anti-virus software (place URL to corporate software site here), this includes personal computers. Third party connections must comply with requirements as stated in the Third Party Agreement.

4.1.6  Personal equipment used to connect to Star education's networks must meet the requirements of Star education-owned equipment for remote access as stated in the Hardware and Software Configuration Standards for Remote Access to Star education Networks.

5.       Policy Compliance
Compliance Measurement
The Infosec Team will verify compliance to this policy through various methods, including but not limited to, periodic walk-thrus, video monitoring, business tool reports, internal and external audits, and inspection, and will provide feedback to the policy owner and appropriate business unit manager.

Exceptions
Any exception to the policy must be approved by Remote Access Services and the Infosec Team in advance.

 Non-Compliance
An employee found to have violated this policy may be subject to disciplinary action, up to and including termination of employment.

5.0   Related Standards, Policies and Processes
Please review the following policies for details of protecting information when accessing the corporate network via remote access methods, and acceptable use of Star education’s network:

Acceptable Encryption Policy
Acceptable Use Policy
Password Policy
Third Party Agreement
Hardware and Software Configuration Standards for Remote Access to Star education Networks
 

 

 

Email policy

Section A - Overview
Electronic email is pervasively used in almost all industry verticals and is often the primary communication and awareness method within an organization. At the same time, misuse of email can post many legal, privacy and security risks, thus it’s important for users to understand the appropriate use of electronic communications.

Section B - Purpose
The purpose of this email policy is to ensure the proper use of Star education email system and make users aware of what Star education deems as acceptable and unacceptable use of its email system. This policy outlines the minimum requirements for use of email within Star education Network.

Section C - Scope
This policy covers appropriate use of any email sent from a Star education email address and applies to all employees, vendors, and agents operating on behalf of Star education.

Section D - Policy
All use of email must be consistent with Star education policies and procedures of ethical conduct, safety, compliance with applicable laws and proper business practices. 
Star education email account should be used primarily for Star education business-related purposes; personal communication is permitted on a limited basis, but non-Star education related commercial uses are prohibited.
All Star education data contained within an email message or an attachment must be secured according to the Data Protection Standard.
Email should be retained only if it qualifies as a Star education business record. Email is a Star education business record if there exists a legitimate and ongoing business reason to preserve the information contained in the email.
Email that is identified as a Star education business record shall be retained according to Star education Record Retention Schedule.
The Star education email system shall not to be used for the creation or distribution of any disruptive or offensive messages, including offensive comments about race, gender, hair colour, disabilities, age, sexual orientation, pornography, religious beliefs and practice, political beliefs, or national origin. Employees who receive any emails with this content from any Star education employee should report the matter to their supervisor immediately.
Users are prohibited from automatically forwarding Star education email to a third party email system (noted in 4.8 below). Individual messages which are forwarded by the user must not contain Star education confidential or above information.
Users are prohibited from using third-party email systems and storage servers such as Google, Yahoo, and MSN Hotmail etc. to conduct Star education business, to create or memorialize any binding transactions, or to store or retain email on behalf of Star education.  Such communications and transactions should be conducted through proper channels using Star education-approved documentation. 
Using a reasonable amount of Star education resources for personal emails is acceptable, but non-work related email shall be saved in a separate folder from work related email. Sending chain letters or joke emails from a Star education email account is prohibited. 
Star education employees shall have no expectation of privacy in anything they store, send or receive on the company’s email system.
Star education may monitor messages without prior notice. Star education is not obliged to monitor email messages.
Section E - Policy Compliance
Compliance Measurement
The Infosec team will verify compliance to this policy through various methods, including but not limited to, periodic walk-thrus, video monitoring, business tool reports, internal and external audits, and feedback to the policy owner.

Exceptions
Any exception to the policy must be approved by the Infosec team in advance.

Non-Compliance
An employee found to have violated this policy may be subject to disciplinary action, up to and including termination of employment.

6.0   Related Standards, Policies and Processes
Data Protection Standard
 

Conditions for assessment
This is an individual assessment task. Student will be assessed individually against all assessment criteria.
Student can make arrangements with the assessor at least one week prior to the assessment due date if they require special allowance or allowable adjustment to this task.
Students found in breach of assessment conditions can be charged with academic misconduct, have their results cancelled, be excluded from the program and receive other penalties. Penalties can also apply if a student’s test material is copied by others.
Plagiarism is the presentation of the work, idea or creation of another person as though it is one’s own. It is a form of cheating and is a very serious academic offence that may lead to expulsion from the University. Plagiarised material can be drawn from, and presented in, written, graphic and visual form, including electronic data, and oral presentations. Plagiarism occurs when the origin of the material used is not appropriately cited.
RMIT special consideration is to enable students to maintain students’ academic progress despite adverse circumstances. The process for special consideration can be found at http://www.rmit.edu.au/students/specialconsiderationLinks to an external site.
Students with a disability or long-term medical or mental health condition can apply for adjustments to their study and assessment conditions (Reasonable Adjustments and Equitable Assessment Arrangements) by registering with the Equitable Learning Services (ELS) at https://www.rmit.edu.au/students/support-and-facilities/student-support/equitable-learning-servicesLinks to an external site.
If students already registered with ELS and students’ study plan is approved, please inform your teacher if this assessment task is not adjusted in line with approved study plan.
Please ensure students full and correct name is written on the student version of this assessment task (do not use nicknames or abbreviations).
Student can appeal the assessment decision according to the RMIT Assessment Appeal ProcessesLinks to an external site.
You will have the opportunity to resubmit any tools that are deemed unsatisfactory (one resubmission allowed per unit, so that means you have two opportunities to submit)
You will be assessed against the criteria as listed in the rubric/observation checklist.
To achieve a satisfactory result you will need to address all criteria satisfactorily.
Useful resources:
http://www.vector-consulting.com.au/media/1080/securing-australias-education-institutions.pdfLinks to an external site.
https://www.protectivesecurity.gov.au/governance/security-planning-risk-management/Pages/default.aspx#c.2.4Links to an external site.
https://www.nist.gov/cyberframework/risk-management-framework

---
## [re621/dnpcache](https://github.com/re621/dnpcache)@[0d6be1e4a9...](https://github.com/re621/dnpcache/commit/0d6be1e4a9dd91334990ac96ed0f4899b482ec2b)
#### Monday 2023-04-17 01:42:56 by bitWolfy

Add 1082 artists to the DNP list.

Added: kattalu, lintu, goobysart, lemonlycan, dylbun, fxscreamer, nt6969, lewdliege, reallyhighriolu, melbaka, saint_lum, kivaaa66, kivalewds, kazoko_(artist), barachaser, shadowthelastalpha, teke, crittermatic, ribboncable, domasarts, ursine-major-ike, browneyedsaiyangirl, uncensoredhugs, skydiggitydive, takarachan, feelin_synful, ilovecosmo, biffbish, pulp_(artist), doxhun, cupsofjade, nicesweater, bluecat_friend, peshky, masuku, lunarfloral, kugi, sagejwood, sqrlyjack, maiteik, leozedi, popdroppy, mikakater, 413k_zzzz, puppyemonade, xanthewolf, joooji, nasusbot, shredded_wheat, dogsdontwipe, wonderwaffle93, gogoandyrobo, jezzlen, dourdoofus, vksuika, klotzzilla, cooperdooper, shadnaotomi, nudegote, sexygoatgod, humgeronimo, ladysophia, mrwhiskerz, cocicka, d-wop, charmerpie, yourdigimongirl, elvche, booponies, lulubelluleart, infinitedelusion, tankakuka, mensies, trunchbull, evian, sodasquids, telelewdz, lawlzy, tonio_(artist), xankragoc, horrificrabbits, sinfulgoatz, whippytail, malachimoet, catniplewds, cocaine_(artist), marshy_swtr, goldelope, chokodonkey, notkastar, sinnerscasino, sentharn, tealie, einin, freaks, angellsview3, arwenscoots, royalzbed, hellfurred, byrth, hexuru, devildjmachine, malerouille, donovallo, psychoninetales, vahldem_sol, nyanyakotarou, shupamikey, zyegnar, akytti, sootylion, kiva~, calmnivore, nexcoyotlgt, smoothsharb, sub-rosa, brismy, woodpeckertoons, xeshaire, suirano, mr_otter_breath, bassybefuddle, sweetishcyborg, skullwomb, steak_in_the_daylight, kittydogcrystal, aggrobadger, orbstuffed, fraichetaso, loonyleandra, bunsawce, schl4fmuetze, renkindle, psychovixen, bkmat55, fricken_stoat, w00my, haven_(artist), gipbandit, loki_the_vulpix, pixelyteskunk, erobos, bunchantress, uniquesoul1600, hirowithart, mikaemikae, ratbloke, pastellprinz, racktor, coillte, kazuk9, acidneko, josh_gong, yiyani, grayish, moblo, naoma-hiru, molish, sheyesh, st0pme, cawkbox, unclesam1776, fennecfuchs, inkpuni, pico_(artist), ruugiaruu, wispyparadox, funkybun, lewdoreocat, dogseesghosts, fauwcks, randy_entinger, trex_b6, yui-hii, runaris, rainbowpillars, ragonox, luxuria-sins, maxisb8, hiccyart, fancyfez, mesoplush, gammelgaedda, yi_feng, scpkid, goetiagoat, mabit, dischimera, dr.bubblebum, drakeraynier, rml, amawdz, mc_arts, freemau, armomen, orionfell, luriostragedy, dradmon, jesterghastly, gothgator, talentlesshack, foxryk, supertrashparty, marrowsoup, roserivy, vanzard, deepfriedlemons, pehkeshi, torotheking, harewithoutahat, lucciola, mr.lemur, lemonkyubun, cubble_chubb, arrjaysketch, pinklilim, jingo824, consciousafterdark, anti-cupid, phosaggro, dashboom, giftheck, birdrabbit, desertmotels, lv99perv, stellarfalcon, tasaeyeang, knotty, rockfall, aogirinaru, hikebu, pawpadcomrade, frengers, rikkitz, vappypaws, nukeleer, adevio, gummuru, sattytsukumo, bittenbats, whygena, ruzeb, hungothenomster, jads_l_rutan, gattonero2001, shawoo, francis_xie, angeltf, veevobyte, darkfool., huwon, tsukikibaokami, covepalms, nikunabe1989, emifern, pero3, tricksta, inkbeastart, grinn3r, holidaydipstick, odonata-nymph, binxxy_(artist), zazush-una, sodo_ad, loonanudes, kodardragon, flameydragwasp, ablimpfox, bakvissie, eccstasy, esealia, tailsrulz, dexxa, spiritto, vonepitaph, eddy-boy, saiyangoku4, gatomonlover, moonlit-comet, thehenwithatie, brienoir, tegucreative, wanisuke, pxlfur, anomyna, motsutambo, fepon, cyrogenic, fursuitchina, slates1n, depthsofthedrex, furrybob, davelievski, spacemaverick, fluff-kevlar, evenytron, 0eff0rt, gayclub, goatypie, nikoyishi, alishka, makeinu, jfetspeaks, cowbun, wyrwulf, thespiderbunny, fluffx, dragons-and-drawings, jcosneverexisted, emptyset, scoty_doodlerz, makinglemonade, ceramic_(artist), selirum, euskuuy, tsunkat, lustbubbles, appleseid, lewdtant, werewuffstuffer, odontoceti, iaido, turboranger_(artist), saca44, mr.shigglesworth, pyriax, raijikaruart, fox-pop, sirblythe_(artist), pastelarcadiaad, etherealarcadia, dracoarcadia, benjibat, sarvak, amethystbeetle, fnook_(artist), stationarrow, maim, rashkah, psy101, disappointedf0x, pointedfox, bundog, tailgrip, scalesforlife, hayleymulch, saphe, kiweevil, madakan, papyreit, rainiing, bitelickart, done0008, alec8ter, tentativelytoon, mikurulucky, killveous, fishhound, misshammer, yakushishi, pieraite, knives4cats, jalmu, quin-nsfw, zooptoon, ebonychimera, beaglebabe1, filthy-d, l-tech-e-coyote-l, anomalae, rakket, mcdutt, alcor90, sodongs, catcock, blickfen, akiiokai, possumkiddo, inkplasm, doubledeal_(artist), fuzzlesuits, chetchaka, raaazzledazzle, razferret, razbuckner, ikitsunyan, kclt, draco_(artist), gunther_silves, kkitten, singafurian, zandybutt, comfytail, crazyassbeethoven, dogburger, adalee, alirrasarts, blackmagemathos, terragon, leonois, solidpoint, cloudpie, rottenscoundrel, wings-and-strings, tomcoletti, pikajota, squeakcore, doubleclawed, ebonyplume, myznyx, zackary911, gaturo, xepher777, aimee-lesley-sim, spottedsqueak, fuhrawr, isaac_baranoff, starnina15, zestylemonss, meirdent, babymee, explicital, slyvern, karpet-shark, booghetti, zypter, adaptagx, opiodae, kiwipotato, murkbone, jonas, exed_eyes, shuryashish, mangobird, kurogi_fox_siv, snuddy, grimdank, nighteternal2469, dacad, superhypersonic2000_(artist), drako1997, verenpunainen_kuningatar, gurophilia, furrever, rdroid, smolrainbowgoat, ratte, urban-coyote, soulsplosion, cyaeon, elliotte-draws, whisperingfornothing, griz_urso, lepronasty, tears_of_soy, bunnielovesyou, paliken, spaceysoda, david_frangioso, cattinypaws, bobdude0, sprocket_(artist), sincerity_gender, marymanifold, turnipberry, asbel_lhant, klaide, rishi-chan, kircai, otto0ttsy, vaktus, beezlebumawoken, transdonaldduck, questly, pinkkatfox, goopomancer, xoel, allbadbadgers, sugarlesspaints, imafutureguitarhero, eiko_tsukida, tarot_(artist), pinuh, diero, dilarus, dfer32, mxwqtkl, electrycpynk, insomniacovrlrd, cewljoke, craziestrobo, anthrus1127, sunflowerbun, coyoteofthesands, masonparker, dottii, livesinabag, flam, toastedbiscuits, skycladfox, orenjisalmonpaw, nasty-fox, canadian_roses, crez, glorpofruithag, i_am_clover, johawk, lycosa, wizardlywalrusking, burgerkiss, kielseki, whisperfoot, oksara, olly, fetchmonkey, rottingichor, heathenfang, bikomation, phox_(artist), acedetrap, hedonisticvows, deersun, skittleytwix, jinxit, jtp-remart, cocaine-leopard, amarl_krieger, nakoo, leoian_(artist), amyth, nogu-art, bluhcat, vulpes_helios, licos, taurika, papilrux, pophopper, ebnet, apis_(artist), glenthefossa, raitime, sashabelle, puddingpaw, mercurial64, elricmysteryshifter, puptaire, anojaa, candychameleon, spice5400, nickshutter, rem, reiishn, sandybuny, 1oi, crunchobar, dante_yun, pherion, saintxd, rawbelr, mithaa, asmartist, pannekoeke, jotun22, iguky-neky, ahnik, thatvondude, kelevtov., fishwrappe, animal_shapes, oouna, princess_rei, blitzdrachin, jesterdk, watermelon_(artist), amara_lemur, lady_kurai, giantmilkdud, nostars, koili, abananaman, heddy, slobstash, terian, teranen, nexii, parabellux, tom_fischbach, reddacted, tojo_the_thief, proximiter, mmuted, irootie, icyshibe, quetzalcoatl_(artist), lamm, shayshay~, hettie, chutzpaah, jacob_lhh3, carpetwurm, draekos, fatdingleberry_(artist), nooplip, pandasayori, numberxxxvi, bc92, silvixen, jungabeast, phoenixazrael, krazykurt, tape_(artist), iipaw, volvokun, hamstergirlthehamster, fallen_(artist), morkovjpn, wolfirry, slimedrops, rubisdrake, shortconcepts, ahdadah, chubbuppy, dreadcaptain, duckdraw, mehndix, pomander, wolfcha, evillabrat, henzolin, loupgarou, empa, diokhan, kpsketches, raysofsunshine, slash0x, kriticalerror, gallivant_crow, nyaroma, caindra, petit-bambi, thatblackcopfromdawnofthedead, dreamertooth, tofu93, ragnarokdragon, saucy, kidakins, kippy, swizzlestix, brilyeon, caste_(artist), tsukaui, saebira, ozzybae, boo-rad13y, sammythetanuki, vuurren, sinistervibe, rem289, shroompunk, samkin, cieldoberman, g0966, crazedg, gaoru, lpawz, enjoipandas, renthedragon, emeritus_terciel, xouual, tehcutepyro, anon232, grimmgrey, counterserum, knottykitten, crybleat, octopoodle, ker0ker0_(artist), xnirox, necrosquelch, ivenvorry, pkuai, mikefur, mattsykun, lilithveritas, bloodhound_omega, ogaraorcynder, rhos, kehei, aw0, apes, nyhgault, qualzar, licentuouslamb, reggaecyp, cynderplayer, vilegrim, redacteur, jimbohusky, lacrimale, pulsar, growlybeast, coreytwc_(artist), naoki_wolf, iceagechippies, alfierubuncle, cbee, acidic, louiefurrywolfy, bweezy, fluffernubber, koriaris, serena_valentine, tacoyaki, fullheroo, limlam, harmoniousrain, zotnamotgrim, xx_g.u.n_xx, carm, lustylamb, dragonvortex, crowchild, dragoneer, lumi_(artist), phi, lexathefox, tanookicatoon, thunper, korram, redwolfofwind, ipipo, teckworks, abobarseem, doopcity, xepheriah, diablo_en_musica_92, doncoon_(artist), digitaldomain123, belayalapa, delkon, connisaur, jasonafex, kabier, rohly, vcr-wolfe, steve_gallacci, hologram_(artist), irene_(artist), piumartiglio, sumat, kingofmaggots, oha, featheredclaw, snuddi, mentalo, ourflatcoat, da-fuze, herr_aardy, discoverychannel, azorart, nemomein, latex_(artist), afterdarkie, 7mii, draco_fenris, blown-ego, sissyskunk_(artist), chucktheskunk_(artist), oakspirit, brokenlynx21, nickswift, butter_bat, ben_hickling, bluehunter, soyuz, sorimori, blackbearcj, ficus, crimes, eifie, soundwavepie, besonik, greyskee, alekksandar, bluetigress, nereza, kalvince, thelabtwins, the_lynox, galaxyoron, moondevourer, evov1, enjambre, seph_ebonblade, prototypebasilisk, accell, myakoda, merenhor, muramuri, derfuhrer, moltengoldart, cchipppo, tetrapoda, omochi_(inkbunny), popsmasterson, nikinazu, raevee, wyntersun, ribboners, c4camel, shysketch, deishido, arconos, melvismd, taihab, cobalt_snow, flak_wizard, paddington_and_company_limited, dangerdoberman, inprogresspokemon, whitemantis, naexus, datsexylemur, polywomple, marilimmy, ryan_rabbat, krimrath, yoshitura, maplecookies, aurelleaheverfree, puppercase, spino, palcomix, bbmbbf, lilithofglace, frisket17, myloveless, grau_(artist), aduleon, sexbad, mearcu, murcifer, citrusdicks, hessonite, sokalo, kittehmei, puccaruu, yuurikin, kurikia, the_cherret_awaits, rapps, maxtwenty, bigbrownorc, santanni, twistedtemptation, nikita-the-stag, liz_art, camcartoonfanatic, singlerider4, beanbat, forge_(artist), hoshime, yamamoto, eviljake2, oriole_(artist), inkblooded, alefwdog, herisheft, disparitybit, samagthrav2, battle_franky, taesolieroy, wolftacos, anixis, spazzticglitch, pirun, swampstomper, morbi, mittsies, blondevelvet, kadath, danza, shinxiolu, littlefreckles, grumpyvulpix, xopachi, gonenannurs, floravola, heartcollar, metz, ranard_lightningfall, frots, curtsibling, vilani, inkydemon, sprinkle-butt, airguitar, anhes, jace_(artist), kaji_(artist), nimrais_(artist), kyoushiro, venerit, lunaselenewolfe, tsareia, violentanxiety, kk-furryworks, cobalta, mickeyila, akuva, rairai, backlash91, sanae, fishbones_(artist), itoril, littlemiu, zeara, darkrokkuman_(artist), peony, helical, donro, agalamt, inanna-nakano, aniutqa, kraest, audiovideomeow, silverbobcat, erithacuscreations, mattartist25, yasminachan, jagzcat, ohmuu, roum, sefeiren, sesameseedbun, noben, aquatheohiokitty, mewyfox, ilgrigio, leoian, vixendra, van_weasel, keihound, zoey03, hardblush, jay_naylor, frisky_ferals, slipshine, rubyrebirth, oze, neogeen, omegaltd, themadcatter, kamicheetah, ookamithewolf1, rabbit_valley, purplekecleon, ollieosa, jayfiregrowlithe, ensayne, bazaarbobby, scappo, dogsoul, poonani, paddercat, eltonpot, ebonyleopard, strype, cbh, mithril07, bicdente, unpeeledwasp, versiris, pitkin, mikachu_tuhonen, lilhoneypup, ladyshinwa, bad-collie, buizilla, foxxian, inert-ren, okamiterasu, mrawl, sammy_stowes, jameless, jooshster, lemoncore, xainy, strider-orion, silitha, spacepoptart, myuinhiding, sweetpinkpetals, sephygoth, edensky, ka, cigarscigarettes, tani_da_real, leatherruffian, hahul, cheezyweapon, reizakirga, leefuu, tanyafoxy, peyo, sweatshirt_(artist), adiago, timelesserror, jollyjack, kahmari, madhattermonster, omnoproxyl337, greykitty, thekitty, mattaku_shinzu, fortuna, fallenarts, ammako, sciggles, atlasfield, sheepdust, lumaberry, tktktk, uzai, aku_tojyo, sixthleafclover, gardelius, squeedgemonster, max-dragon, baka_sukonku, ferniio, jennadelle, ixerin, jaleo, luvythicus, tatious, nekomata_neko, zody, binky, sidian, kii-kitsune, kiirei, spookeedoo, angel27, msrah_(artist), nazuu-m0nster, lunacatta, kululu-xiao, kipcha, fluffball, reptilecynrik, redadillio, zerwolf, kylontario, liz_day, nightweaver, egophiliac, doffa, dipper, kefkafloyd, melo666, sonicdash, sugarpoultry, olven, theramjing, softpaw, xiraco, unicornspirit, tinintri, thornwolf, thaily, tamen, sharue, shadowsani, rikutida, paolo, kriscrash, kaemantis, frogsbreath, tailheat, sexyfur, jeremy_bernal

---
## [BlueMemesauce/tgstation](https://github.com/BlueMemesauce/tgstation)@[6085e3b5ee...](https://github.com/BlueMemesauce/tgstation/commit/6085e3b5eed0f4954d2ba25549c919653207611d)
#### Monday 2023-04-17 01:49:50 by MrMelbert

Reagent soup / Soup rework / Stoves - A kitchen expansion (#74205)

## About The Pull Request


![image](https://user-images.githubusercontent.com/51863163/227391708-8de28b68-149f-4e02-a2d3-22f6e3067784.png)

**This PR:** 

- Reworks most* existing soup into reagents. 

- Adds Stoves and Ranges. Ranges replace most* existing ovens. 

- Adds soup pots, to cook soup

**How does it work?** 

In the kitchen you will find a stove now.

Stoves act as a "reagent container heater", essentially a chem heater.
You can set a pot onto the stove.

To make soup, visit the cooking recipe book for a guide. Most recipes
are the same as before, just tweaked slightly - Add water to the pot (50
units for 1 batch generally), then add all the corresponding ingredients
to the pot. Set the pot out on the stove and right click it to turn it
on. If the recipe's correct, shortly it will start to mix and give you
soup!

One soup recipe will give you roughly 3 servings of soup. You can pour
our the soup into a bowl using a ladle or just by pouring it manually.

Of note: **All of the reagent contents of the ingredient are transferred
into the soup.** Better, more nutrient rich ingredients produces more
soup, and poisoned produce will pass it on.

If you place the soup into a chem master, you will notice it's roughly
half "soup reagent" and half a variety of reagents, including nutriments
/ proteins. This is your soup! It is recommended you serve your soup
with the reagents included, as they make up more nutrition for the
customer, however you can separate it out if you're picky.

**Todo:** 

- [x] Fill out the PR body a bit more 
- [x] Mapping (wait for big merge conflict pr to go past)
- [x] Soup colors
- [x] Balance pass over for soup recipes
- [x] TODOs
- [ ] Unit tests
- [x] Cullen Skink's recipe is invalid
- [x] Try to see if there's an easy way to prevent soup from fattening
you up too easy.

## Why it's good for the game

Adds some more depth to the kitchen and moves chef away from the
click-button-get-food style that exists.

Allows for inherently custom soups by the way of making it reagents, so
no need to support custom soup food items.

## Changelog

:cl: Melbert, stove and pot sprites by Kryson, ladle sprite by Kinneb
add: Kitchens are now stocked with Ranges. 
add: You can now print (and create) Stoves. 
add: The dinnerware vendor now dispenses ladles. 
add: Spoons can now actually spoon... things.
add: Soup has been reworked entirely. Soups are now reagents, cooked via
a soup pot on a Stove or Range. Simply add water and your required
items, then apply heat. Be careful not to boil over!
add: Stoves, Ranges, and Griddles will now heat up their surroundings -
don't turn them on around plasma!
fix: Fixes being able to cook in an Oven while the room is depowered
qol: Hitting a customer bot with an incorrect recipe no longer counts as
a hostile attack leading to your demise shortly after
refactor: Customer bots that request a reagent now use custom orders
code: Cut down a lot of code in the crafting menu code, and removes some
ugly ispaths
del: Soup is no longer food items, so can't appear in random food pools
(at least not yet).
balance: Virus Food recipe now requires you cool it to 200k.
/:cl:

---
## [itseasytosee/tgstation](https://github.com/itseasytosee/tgstation)@[1cdc327a8f...](https://github.com/itseasytosee/tgstation/commit/1cdc327a8f98c1592fc970a4ef1c39d685c81554)
#### Monday 2023-04-17 02:21:17 by Jacquerel

Station Trait: Spider Infestation (#73893)

## About The Pull Request

Hate having your cables eaten by mice? Nanotrasen have heard your
complaints and settled on a natural, _organic_, and eco-friendly
solution.

When this station trait is active, roundstart and event mouse spawns
have a chance to instead be replaced with duct spiders (both will exist,
it doesn't remove mice).
Duct spiders are largely harmless to humans, actively hunt other
maintenance creatures (such as mice), and have only one _tiny_ downside.

![image](https://user-images.githubusercontent.com/7483112/224345781-2627be98-67f2-4cab-ac40-c6c9b35ea909.png)

These mobs can also sometimes be spawned by a minor scrubber clog event.

As a side note, all spider basic mobs with AI (except Araneus) will now
try to automatically fill a small area around them with webs.

Also I made it so that mobs will ignore their random_walking behaviour
if they're engaged in a `do_after`, just in case.

## Why It's Good For The Game

Adds a little bit of variety to things which can slightly annoy you in
maintenance.
Spiders will automatically make places they live in look like spiders
live there.

## Changelog

:cl:
add: A station trait which sometimes populates maintenance with small
spiders. You can wear them as a hat if you wanted to have a spider on
your head for some reason.
add: Spider mobs will automatically start webbing up their environment.
/:cl:

---
## [Benjie-E/classic-games](https://github.com/Benjie-E/classic-games)@[2a798fdf8a...](https://github.com/Benjie-E/classic-games/commit/2a798fdf8a4466a6cb1d44d581533d65b30f8c36)
#### Monday 2023-04-17 03:16:23 by nfischer623

Fixed read access violation

@BenTangora The main issue was that the replay() function should have been receiving the GameManager passed by reference (GameManager &game), but it was instead receiving it passed by value (GameManager game). If you pass something by reference, it doesn't have to create a copy of that object, so when the function is done, it doesn't technically go out of scope and the destructor is not called. The read access violation was coming from the GameManager's destructor being called multiple times - once when replay() finished and again when it went out of scope in main().

I also removed the manual destructor calls from main(), since an iteration of the while loop will automatically call the destructors.

I was going to work on input stuff tonight, but honestly that took me a really long time to debug/figure out and I am tired...sorry! I'll see what I can do before class tomorrow.

---
## [the-og-gear/tgstation](https://github.com/the-og-gear/tgstation)@[4014aef4b0...](https://github.com/the-og-gear/tgstation/commit/4014aef4b0a24d260b314f462a21f943c3d62894)
#### Monday 2023-04-17 03:34:58 by Bloop

Fixes a runtime in simple_animal/hostile (#74706)

## About The Pull Request

Attempting to fix this flaky test that has been cropping up from the
Icebox tests. It is annoying.

From what I can tell, the mob was getting qdeleted while it was doing
its loop of finding a target. This can happen at any time, because many
simple mobs (including the one causing the issues) get qdeleted on
death.

Added some more checks to make sure we don't do certain actions if the
mob gets qdeleted midway through execution of its AI routine. It really
could happen anywhere so we must be vigilant.

```
create_and_destroy: [02:24:31] Runtime in stack_trace.dm,4: addtimer called with a callback assigned to a qdeleted object. In the future such timers will not be supported and may refuse to run or run with a 0 wait (code/controllers/subsystem/timer.dm:583)
proc name:  stack trace (/proc/_stack_trace)
src: null
call stack:
stack trace("addtimer called with a callbac...", "code/controllers/subsystem/tim...", 583)
addtimer(/datum/callback (/datum/callback), 300, 8, null, "code/modules/mob/living/simple...", 595)
the demonic watcher (/mob/living/simple_animal/hostile/asteroid/ice_demon): GainPatience()
the demonic watcher (/mob/living/simple_animal/hostile/asteroid/ice_demon): GiveTarget(the mi-go (/mob/living/simple_animal/hostile/netherworld/migo))
the demonic watcher (/mob/living/simple_animal/hostile/asteroid/ice_demon): FindTarget(/list (/list))
the demonic watcher (/mob/living/simple_animal/hostile/asteroid/ice_demon): AIShouldSleep(/list (/list))
the demonic watcher (/mob/living/simple_animal/hostile/asteroid/ice_demon): handle automated action() at stack_trace.dm:4
```

On top of that, there is signal handling in place to LoseTarget() when a
mob that is already a target gets qdel'd and sends
`COMSIG_PARENT_QDELETING`. Shown below.


https://github.com/tgstation/tgstation/blob/4c48966ff80915ee0b4f796994a0ab6616cab31b/code/modules/mob/living/simple_animal/hostile/hostile.dm#L655-L666

However there is nothing stopping a target that is not null but that has
been qdeleted from being considered as a target in the first place.

This PR just aims to fix that problem by making sure that a) a hostile
ai that gets qdeleted midway through does not keep doing stuff that can
cause issues and b) an atom that is being qdeleted never makes its way
into the targets list of a hostile ai.

Simple mobs/AI are due for a wider refactor honestly but this really
ought to be done in the meantime so we don't get spammed by CI failures
over nonsense.

Fixes https://github.com/tgstation/tgstation/issues/73032
Fixes https://github.com/tgstation/tgstation/issues/74266
Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/18964
Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/19749
Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/18964
Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/19322
Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/18974
Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/19296
Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/19294


## Why It's Good For The Game

Bugfix, stops the icebox test from failing as much.

## Changelog
:cl:
fix: fixes hostile mobs sometimes being able to target an atom that has
been marked for deletion and then becoming confused, and in a similar
vein fixes mobs sometimes still running their AI while being marked for
deletion.
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [Ms-Mee/Shiptest](https://github.com/Ms-Mee/Shiptest)@[0410075cc8...](https://github.com/Ms-Mee/Shiptest/commit/0410075cc811c5f65d7dc085a665c1ebb3a20e44)
#### Monday 2023-04-17 03:40:57 by meemofcourse

Ports mothroaches + Moth emotes (#1843)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Can you guess what this PR does? If you answered that it ports [this
pull request](https://github.com/tgstation/tgstation/pull/68763), [this
pull request](https://github.com/tgstation/tgstation/pull/71784), and [a
partial part of this one
too](https://github.com/BeeStation/BeeStation-Hornet/pull/7645/), then
you're right!

![imagen](https://user-images.githubusercontent.com/75212565/227387000-cc205158-286b-4841-9c5a-2e4d6d8d6200.png)

![imagen](https://user-images.githubusercontent.com/75212565/227386830-213997a1-ebe9-4573-8f8e-052e72bacea2.png)


You can also craft moth plushies now. You just need some cloth,
mothroach hide, and a heart!

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

silly little moth roaches and emotes, who wouldn't want them in the
game?

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Mothroaches are now a thing
add: Moth laughter, chittering and squeaking
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [FuzzyFuzlet/fuzzys-repository](https://github.com/FuzzyFuzlet/fuzzys-repository)@[3ced3047b8...](https://github.com/FuzzyFuzlet/fuzzys-repository/commit/3ced3047b8c32a3e631519f6b117fdc6bf0630d8)
#### Monday 2023-04-17 03:49:54 by Tk420634

Merge pull request #1949 from ARF-SS13/I-hate-github-a-lot

Fuck you, Vertibird.  Go where I put you

---
## [FuzzyFuzlet/fuzzys-repository](https://github.com/FuzzyFuzlet/fuzzys-repository)@[7b5b198aa8...](https://github.com/FuzzyFuzlet/fuzzys-repository/commit/7b5b198aa80b88426d1150184c78ecd5fa0816b8)
#### Monday 2023-04-17 03:49:54 by Tk420634

Fuck you, Vertibird.  Go where I put you

You fucking animal of a thing

---
## [ToasterBiome/Yogstation](https://github.com/ToasterBiome/Yogstation)@[8e3e0b1450...](https://github.com/ToasterBiome/Yogstation/commit/8e3e0b1450189ebda3b2bc760c036ba6c59c6b6a)
#### Monday 2023-04-17 03:55:26 by LazennG

adds magmite crusher to the things you can make at the world anvil (#17530)

* FUCK YOU PLASMA CUTTER

* updated it now just waiting on BAIOMU FOR FUCKIN SPRITES

* returned old sprites i had but it's still lacking 1 handed versions

* touched up some of the sprites but STILL NEED ONEHANDED ONES FROM BAIOMU

* FINALLY

---
## [SylvetteSylph/tgstation](https://github.com/SylvetteSylph/tgstation)@[551a09211b...](https://github.com/SylvetteSylph/tgstation/commit/551a09211b4091320ff871e78d93efa2775df6bc)
#### Monday 2023-04-17 05:35:12 by carlarctg

Makes Black Market Uplinks more easily craftable, adds them to uncommon maint loot pool (#74744)

## About The Pull Request

Replaced the subspace amplifier in the Black Market Uplink's crafting
recipe with a signaller and a microlaser.

Added the Black Market Uplink to the maintenance loot pool.
## Why It's Good For The Game

The BMU is an _extremely_ rare device to find in rounds. It can quite
literally ONLY be found via the crafting recipe, and with how stupidly
bloated the crafting lists are, it isn't something many people know
about. All this means that a very unique and engaging gimmick item is
tragically extremely obscured.

To add to this, the recipe requires a _subspace amplifier_. These items
are UNBELIEVABLY rare - they need you to vend them from a techfab with
bluespace communication technology researched, which is fair to say is
not a common thing. Sometimes maps have them in tech storage, but even
then you have to break and enter which can be quite risky at times and
an annoying blockade the other times.

The black market items are not worth this much hassle. They are all
small cute gimmicky objects that do not heavily impact the round. By
making it not only easier to craft with common items, but also appear in
the maintenance loot pool, this will make assistants find out about it
more often, which can further incentivize them to utilize the **cargo
bounty system** to get enough money to buy their funny gadgets.

Another idea would be to make the uplink appear as a bounty item, which
would be a great way to tell players it exists and encourage them to mix
both systems together. The system for getting items is also
unnecessarily, miserably awful - your item either gets literally thrown
into space from a random direction, or it is teleported silently without
warning in 60 seconds onto a completely random place which can very much
include Security, Command, the Vault, or other high-security areas.
Needing to B&E into these areas to get your durathread vest is, uh. Not
worth it. However these aren't part of this PR, unless they're given the
A-OK. (also maybe make it cargo purchasable?)
## Changelog
:cl:
balance: Makes Black Market Uplinks more easily craftable, adds them to
uncommon maint loot pool
/:cl:

---
## [Koi-3088/ForkBot.NET](https://github.com/Koi-3088/ForkBot.NET)@[ed195875b5...](https://github.com/Koi-3088/ForkBot.NET/commit/ed195875b50a19eb11b8eed4f99f1f7ca9262a9a)
#### Monday 2023-04-17 06:01:14 by Koi

Mr. Mime is a thing, unfortunately.
Mild clean, some more Cherish set handling attempts.
Exclude set MetDate from mystery gifts.
Fix daycare enum parsing.
Check for no result in case $qc was used or some other weird thing happens.
Remove FixOT and TradeCord as routine types (FlexTrade handles both).
Try to apply trainer info for Mystery gifts.
Re-add fixed met date if not GO origin.
Update DenBot distribution data, minor fixes.
Fix Yamask-Galar in daycare, some more oopsies.
-Add DenBot - a seed lookup and day skipper bot for raids.
-Change AutoRoll's behavior to make use of some of DenBot's functionality.
Minor clean.
Revise TradeCord "traded" check, remove potential user path straggler entries because paranoia, some minor fixes.
TradeCord fixes (shocker, I know).
Extract Json serializer.
Minor clean and fixes.
Minor fixes.
Fix Milcery when an Alcremie variant is a parent.
Update to latest Core and ALM dependencies.
Handle non-shiny events in a better way.
Work around a race condition?
Simplify and de-bugify trade completion check.
Fix indexing, improve chance for Melmetal-Gmax because it's nigh impossible to get.
Rework TradeCord internals, add new functionality:
-Migrate user data from ".txt" files to a serialized Json (migration for a large amount of users will take a few minutes, be patient).
-Make TradeCord configurable, add its own settings category.
-Add some template events with an optional end timer (YYYY/MM/DD 8PM as an example, though any local time format should work).
-Add barebones Pokedex (counter, flavor text).
-Can check dex completion by typing `$dex`, check missing entries by typing `$dex missing`.
-Completing the Pokedex will slightly improve shiny rate.
-Can now mass release cherish event Pokemon and shinies ($massrelease shiny/cherish).
-Various tweaks, improvements, and bugfixes.

Slightly change FixOT's behavior:
-If a shown Pokemon is illegal and an event, attempt to find a match within the MGDB first.
-Try to force users to trade away the shown Pokemon, log attempt to change shown Pokemon.
Add consideration for easter eggs being enabled in settings, fix Suicune
Change species rng for TradeCord, some bugfixes (I really need to rewrite this mess)
Add check if we're using ListUtil for Giveaway instead of TradeCord.
Amend commit since I'm squashing and force-pushing while bringing the fork in line with the main branch
Add Giveaway module to Discord bot (#22)

Thanks, rigrassm.
Co-authored-by: Koi-3088 <61223145+Koi-3088@users.noreply.github.com>
Specify USB port instead of adding the first result (can be found via Device Manager).
Re-add boolean check because we don't want to fix everything
FixOT will attempt to regenerate illegal Pokémon.
Apply trash bytes for reasons.
Minor TradeCord fixes and adjustments.
Minor clean for C#9
Use "GetValidPreEvolutions()" instead of "GetPreEvolutions()".
Index forms correctly.
Fix the fixed and re-introduced empty daycare index error.
*an* Ultra Ball.
Add EvoTree breeding for TradeCord.
Remove unnecessary value declarations for pinging on encounter match.
Mildly beautify EncounterBot mark output.
Integrate Anubis' system update prevention into Soft Reset and Regigigas Encounter Modes.
Rename "Regi" Encounter Mode to "Soft Reset".
Speed up "A" clicks for Regigigas and Soft Reset modes.
Add Mark logging output for EncounterBot.
Fix oops (re-order logic, remove unnecessary lines).
Add optional species and form specification for $massrelease
Use an obscure string splitter because people like symbols in their names.
Fix things that broke after rebasing to the latest main repo commit.
Use a less unfortunate field name and value splitter...again.
Fix Marowak-Alola always generating as an NPC trade.
Add filters for "$list <species>" to narrow down results.
Fix Cherish Pichu and Octillery
Stop making dumb mistakes, me (implying the rest of it isn't a dumb mistake).
Can't breed antiques.
Use a less unfortunate embed name and value splitter
Add Melmetal-Gmax to TradeCord.
Add ability to search by caught ball.
Have MassRelease ignore events.
Add specific regional form breeding.
Revise egg rate and egg shiny chance.
Have trade evolutions hold an Everstone.
Add an extra right click when navigating to settings for AutoRoll.
Add reworked encounter/egg/fossil logs.
Minor clean.
Minor clean.
Get rid of EncounterBot, FossilBot, EggFetch text logs until I properly rework them.
Break on an empty page due to aggressive rounding
Add multi-page lists for Tradecord.
More random bugfixes.
Fix some bugs before major clean
Add Language parameter for TradeCord.
Change trainer info input format for TradeCord.
Move focus on Showdown set instead of randomizing a pkm file.
Allow user to enter whatever they want for $list, handle edge cases like Kommo-o
Add "$list all" to show non-duplicate caught species.
Automatically remove from favorites if trading or gifting (small QOL thing).
Change how favorites are removed from user file.
Revert base egg shiny chance nerf.
Fix daycare
Add favorites command to TradeCord.
Slightly nerf eggs.
Fix TradeCord list for shinies
Add TradeCord (my dumbest and messiest project so far, Archit pls don't hate the mess).
Add Showdown output for Star/Square shinies and OTGender.
Add optional link code input for FixOT.
Change how OTName, TID, SID is displayed.
Add Regigigas SR bot.
Add SoJ Camp SR bot.
Ribbons now work with EggTrade (remove ribbons if egg).
Remove EggRoll.
Add another filter for FixOT
Fix.. FixOT
Update offsets for EncounterBot catching.
Slightly change StrongSpawn to work with Regi SR and make it its own mode.
Make SpinTrade only available for USB-Botbase
Update valid eggs for CT
winforms: resize icon.ico to fix crash at startup on unix using mono
Rework Spin, read initial in-game coordinates in order to correct drift
Add TID, SID, Language output for Showdown
Remove obsolete OT and Language parsing
Very minor clean until I have time for a proper one.
Detach controller when stopping USB bot.
Actually set LastUsedBall for EncounterBot (missed when bringing in line with main repo)
Move extra RaidBot timings following the official commit
Remove PKHeX Discord invite from Readme.md

Maybe fewer people will pester devs now about my unofficial fork?
Update for latest main repo EncounterBot commits.
Update README.md
Add back best commit: Red's SpinTrade.
Add egg trades, foreign Dittos and OT for Twitch.
If ItemMule is enabled, also display the item a user is receiving.
Add periodic time sync toggle for all methods of hosting (except for non-soft locked AutoRoll) to (hopefully) prevent den rollover during extended hosts.

Add routine to exit a lobby for SoftLock if no players are ready in time (to preserve soft lock).

Add a routine to recover from disbanded lobbies (when someone disconnects unexpectedly) for SoftLock.

Add a routine to restart game if all else fails and we're stuck in a raid.

Add a routine for adding and deleting friends if we're soft locked and raids go empty.

Slightly reorganize settings, extract methods, minor clean.
Don't use such a generic file name for stream assets.
Check USB port index for running bots. Should fix adding additional USB bots when no config is saved.
Add fixed met date for FixOT.
How do I boolean
Change airplane mode logic, tweak timings and routine for soft lock lobby exit
Rework EggRoll cooldown (static list in favor of a txt file).
Start clean up and refactor
Add setting to increase delay after pressing "Home" after a date skip.
Use USB port index for blocking and sprite pngs if connection type is USB
Add option for airplane host (usb-botbase required)
Add option to softlock on selected species for AutoRoll
Add automatic compatibility for all console languages when date skipping (have to set ConsoleLanguage under ScreenDetection)
Attempt to fix multiple USB device add and connect...again
Minor clean
Fix oops?
Handle add/remove of bots
Distinguish between multiple USB devices, tweak BotRemoteControl for USB, other various fixes
Add SpA modifier for foreign Dittos
Add alpha USB-Botbase support
Fix DateTime parsing for European format for EggRoll
Set fixed EggMetDate and MetDate for EggRoll
More FixOT filters
Remove Beheeyem. Oops.
Split EggRoll into its own routine and trade type, only output "Receiving: Mysterious Egg" if routine is EggRoll, other minor tweaks and fixes
Make FixOT its own queue with roles and counts
Add a couple more OTs to $fix
Parsing for EggRaffle auto-clear and $clearcooldown
Adjust timings and split Watt collecting clicks for AutoRoll
Fix oops with file attachments for Ditto
Further improvements for OT, memes for invalid pokemon (disable EasterEggs)
Add spaces, digits for OT
Randomize memes, cut down bloat
Fix miscellaneous bots after Anubis' recent QOL additions
-Ignore events for OT because headache.
-Add overlooked "$convert <generation>" input for OT.
-Move $clearcooldown to SudoModule
-Clear timer automatically if NoTrainerFound
-More reliable Dittos
-Foreign Dittos for $convert
-Command to clear cooldown for EggRaffle in case trade gets disconnected
-Fix "Trade finished" line to keep result secret
-EggRaffle as a toggle, option to specify channels
-Seed Check output to both DMs and Channel (apparently some want it)
-Randomly generated egg raffle via a "$roll" command with a configurable cooldown
-FixAdOT reworked, has its own command "$fix" and no longer overrides $clone
-Ball: <value> output for Showdown sets
-Fix oversight
-Option to output Seed Check results to Discord channel with a User mention
-Showdown set output for OT name and eggs
-Basic "OT: <name>" option without Showdown set output
-Initial $convert support for EggTrade
-Egg moves for EggTrade test attempt
-Minor update
-EggTrade (by nicknaming a Pokémon "Egg" using $trade)
-Failsafe for memes if enabled but field left blank or incomplete
-Niche breedable Ditto trade mode.
Add minimize button
EggFetch text logs
StrongSpawn mode for EncounterBot
Re-add EncounterBot Master Ball catching
More parsing for FixAdOTs
Park Ball as held item instead of string
Actually remove the offset instead of saying I did
Initial DLC commit
Faster code entry
Removed catching for EncounterBot (need a new offset)
CloneBot mode to fix Nickname and OT if adverts detected

---
## [DamienIsPoggers/Hantei-chan](https://github.com/DamienIsPoggers/Hantei-chan)@[5209d8c6fe...](https://github.com/DamienIsPoggers/Hantei-chan/commit/5209d8c6fedd60a377f5a9cef47fe0a77f891625)
#### Monday 2023-04-17 06:10:13 by Damien McCormick

added the option to only scale the chunks because DANNY-MAN AND JAMERSHINOBIONEOBI02 ARE BITCH ASS MOTHER FUCKERS

---
## [ARF-SS13/coyote-bayou](https://github.com/ARF-SS13/coyote-bayou)@[91a4e887e8...](https://github.com/ARF-SS13/coyote-bayou/commit/91a4e887e80724c63fbe540625b9fc06e08ba6f9)
#### Monday 2023-04-17 07:00:05 by Tk420634

Fixing Plasma Cutters

Haha, fuck armor pen sucks shit

---
## [allisonkarlitskaya/cockpit](https://github.com/allisonkarlitskaya/cockpit)@[29500b32c6...](https://github.com/allisonkarlitskaya/cockpit/commit/29500b32c66dff16ec4aabf119a5772f007a007e)
#### Monday 2023-04-17 07:29:05 by Martin Pitt

ws: Disallow direct URL logins with LoginTo=false

The current documentation of LoginTo= isn't very specific about what
exactly happens with a "false" value; but it is plausible for an admin
to assume that "false" would disallow logging into a remote host
completely -- not merely hide the "Connect to:" field and then allowing
a direct URL login anyway.

It is sometimes important to disallow direct SSH logins from the login
page on publicly exposed bastion hosts, as this functionality allows
unauthenticated remote users to:

 - scan the internal network for existing hosts, which might otherwise
   not be accessible directly from the internet
   (Fixes #18540, https://bugzilla.redhat.com/show_bug.cgi?id=2167006)

 - scan the cockpit-ws host or internal network hosts for open ports
   (Fixes #15077, https://bugzilla.redhat.com/show_bug.cgi?id=2018741)

So change ws to reject direct URL logins with `LoginTo=false`. This
happens most naturally in cockpit_session_launch(), as we still want to
allow remote URLs from the shell's host switcher in already
authenticated sessions. This will not produce a very friendly error
message, but it doesn't have to be -- at that point specifying direct
URLs can be considered hacking anyway.

Clarify the documentation accordingly.

---
## [BOO1980/boo-self](https://github.com/BOO1980/boo-self)@[fe17ef370a...](https://github.com/BOO1980/boo-self/commit/fe17ef370a5122e36aa930262e630f8d408e5bde)
#### Monday 2023-04-17 07:46:08 by hayleyBillingham

Merge remote-tracking branch 'refs/remotes/origin/main'

Conflicts:
	unfuck-yourself/chap1-In the beginning.html
	unfuck-yourself/chapter2-I am willing.html

---
## [Jolzyfx/Read](https://github.com/Jolzyfx/Read)@[99f65f13fb...](https://github.com/Jolzyfx/Read/commit/99f65f13fb1289c560694d4cd844b3efc2e1f51a)
#### Monday 2023-04-17 08:57:59 by Jolzy fx codes

Update README.md

Hello and welcome to my Github profile!

I am a Software Engineer with a focus on Frontend Development. With a strong background in HTML, CSS, JavaScript, and various frontend frameworks, I am dedicated to delivering high-quality, responsive, and user-friendly web applications.

As a Software Engineer, I am responsible for the complete lifecycle of scalable, secure, and well-designed software products. I work closely with designers, analysts, quality assurance, and other teams to ensure that each design is translated into a real-life product that meets the client's requirements.

Apart from my work, I am passionate about staying up-to-date with the latest frontend tooling and technology. I am always looking for new opportunities to learn and grow as a developer, and I enjoy sharing my knowledge with others through blog posts, tutorials, and open-source contributions.

If you are looking for a Software Engineer with a strong frontend background and a dedication to delivering high-quality software products, I believe my skills and experience would be ideal for you.

Thank you for taking the time to visit my profile, and I look forward to connecting with you soon!

---
## [SmoSmoSmoSmok/tgstation](https://github.com/SmoSmoSmoSmok/tgstation)@[11cbbba018...](https://github.com/SmoSmoSmoSmok/tgstation/commit/11cbbba018e861237ce4bed73f19b58874c22042)
#### Monday 2023-04-17 09:47:00 by Sol N

Replaceable Traitor Uplinks (#74315)

## About The Pull Request

Following [from the suggestion in this hackmd
](https://hackmd.io/IkDWWkpfQa2lkdevsnLqhA?view#Replacement-Uplinks)with
a few twists of my own, I have made a method for traitors to acquire a
replacement traitor uplink that has its own set of flaws and limiters in
order to prevent abuse.


![ZC0WYDFRzc](https://user-images.githubusercontent.com/116288367/228101432-9352390b-9538-4c62-8dc4-55e2e798c466.png)

The basic pitch is as follows, all traitors now start with a new,
crafting recipe exclusive to them, it costs a teleport beacon, a
bluespace crystal, and some iron and cable coil, and then allows them to
build a static, dense machine that they can synchronize with, which
allows the machine to know what signal it should be looking out for from
the traitor.

![dreamseeker_iErI3vju0C](https://user-images.githubusercontent.com/116288367/228094286-c2bca198-82cd-4ce0-a4a7-c26c24a9327c.gif)

The traitor then uses any radio, sets it to the frequency that has been
added to their static antagonist ui, and then speaks their codeword,
also in the ui, and then a few things happen.

![dreamseeker_gbzSFeHuS5](https://user-images.githubusercontent.com/116288367/228094354-a649c713-f013-4ac2-b8d7-0754a852f987.gif)

Most obviously, they get a replacement uplink that is in the conspicuous
shape of the nukie or lone op uplink. This uplink can be unlocked by
speaking your replacement codeword to it again, it remembers your
previous TC amount and locks all other uplinks associated with your
uplink handler(they can then be unlocked as normal). It also destroys
any other replacement uplinks associated with your uplink handler, which
means you can never have more than one replacement uplink.

This means that if your uplink has been confiscated and you left it
unlocked, if it hasn't been emptied out you can continue from where you
were, and if you want to get back on the TC grind you won't lose the new
TC to whoever stole your uplink. Of course, the new uplink can not be
locked, so you have to be more careful with it or buy an uplink implant
and destroy it. You can destroy your replacement uplink with a
screwdriver right click, same for the machine.

Additionally, the Syndicate Uplink Beacon has another quirk to it, which
is that the teleporter beacon used to create it is intact, which means
people eagle eyed on the teleporter console could go find you, not to
mention that if you use an existing teleporter beacon, someone might
notice its gone missing...

oh also while making the replacement uplink i found a bug caused by a
recent pr that broke debug uplinks due to them not having a purchase
log. thats fixed too

## Why It's Good For The Game

It can be easy to lose your uplink, and as a traitor having your uplink
confiscated, even if it is locked, feels really bad. While the old
traitor objectives were added back to prog traitor to prevent situations
where a confiscated uplink meant that you were completely aimless, I
think that having a backup solution would be good for more inexperienced
traitors or for ones who get unlucky.

Hopefully this is generally balanced well enough but there are a few
levers that can be pulled, but overall I do think that making it so that
traitors can always get a chance to get an uplink and do some objectives
is good for the game. I like the idea of someone getting perma'd,
someone breaks them out, they both craft a new uplink beacon, and then
they go back and get the traitors old gear with stuff they got from the
new uplink, I think that's a cool possibility to throw into the sandbox.

## Changelog
:cl:
add: Added new syndicate uplink beacon and associated systems that allow
you to get a replacement traitor uplink
fix: Debug & nukie uplinks no longer runtime and work properly again
/:cl:

---
## [SmoSmoSmoSmok/tgstation](https://github.com/SmoSmoSmoSmok/tgstation)@[00f8bcfe75...](https://github.com/SmoSmoSmoSmok/tgstation/commit/00f8bcfe75275b7452063d1d8ec75d4c8e643f8b)
#### Monday 2023-04-17 09:47:00 by MrMelbert

Moves revolution code of out of flash code, fixes April Fool conversion forcesay never working in any cirumstances (#74411)

## About The Pull Request

- Signallizes head revolutionary flash conversion code, moving it out of
core flash code.
- Removes "tacticool" flashing from head revs, but they can still
convert from any direction
 
- Fixes April Fools "You son of a bitch! I'm in" force say never
working.
   - Revs are muted on conversion so they couldn't talk.
       - Fixed by only muting revs on non-holidays
   - Cultists are unconscious on conversion so they couldn't talk
       - Fixed by only unconscious-ing cultists on non-holidays
- Brainwash victims are more often than not unconscious / asleep so they
couldn't talk
       - Just left this one. 

- Reduced the chance of them occurring and limits it to April Fools only
- A 1% chance of the force says ocurring means they will happen pretty
much once a week, given multiple rev / cult rounds happen every week and
on average like, 20 people are converted. A little absurd, it's good
that it never worked?

## Why It's Good For The Game

Antag code in core item code is bad

It's funny this meme has existed for like 2, 3 years now? No one's
tested it, it's never worked

## Changelog

:cl: Melbert
refactor: Removes Rev code from core flash code
fix: Getting converted on April Fools now triggers the meme force say as
always intended
del: The meme force say can no longer trigger on any day (it didn't work
before anyways)
/:cl:

---
## [SmoSmoSmoSmok/tgstation](https://github.com/SmoSmoSmoSmok/tgstation)@[9dfe00d79d...](https://github.com/SmoSmoSmoSmok/tgstation/commit/9dfe00d79dd7bd540442ce825caa4e964c619b46)
#### Monday 2023-04-17 09:47:00 by san7890

IceBoxStation More Active Turf Fixes (#74474)

## About The Pull Request


![image](https://user-images.githubusercontent.com/34697715/229412910-e65b0ffa-8944-4b93-a4cb-41c6fd6bb333.png)

This didn't show up in my testing for #74410. I hate it here.

## Why It's Good For The Game

I am a monkey trapped next to a computer playing whackamole with this
fucking chasms and active turfs. one day i will be free.
## Changelog

nothing that should concern players

---
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[c3b78761d2...](https://github.com/LemonInTheDark/tgstation/commit/c3b78761d29c53558fd993c84bb808bd5783861d)
#### Monday 2023-04-17 11:26:07 by tralezab

Adds Chuunibyou Spell + Granter (#74404)

## About The Pull Request

My April fools this year, though not going to call it one because some
people think it should just be actually merged.

### Chuunibyou Powers 🌟

Wizard gets a new spell for 2 points that gives him the powers of
chuuni. This makes them have ridiculous shouted invocations for all
their spells, their spells are colored pink, and they heal slightly when
casting one.

While mostly a meme spell, I could see a tailored loadout like lichdom
and splattercasting that takes advantage of the unique spellcasting
changes, like a very low cooldown spammable loadout to heal quickly.

There is also a granter book in the library, which teaches a version of
chunni that doesn't heal.

#### Medical eyepatch

I added it, chuuni wizards get a NODROP version.

## Why It's Good For The Game

This PR bestows upon the game the glorious gift of chuuni powers, the
ultimate manifestation of my hidden potential and the secret truth of
this world, which only I and a few chosen ones can comprehend and
unleash! Why wouldn't you want it?!

In all seriousness, it is a unique wizard playstyle and it will make for
some funny memes. Beyond wizard, the chaplain, heretics, or mime can
read it in the library for a very silly round. I like it!

## Changelog
:cl:
add: Chuunibyou wizards, and chunni granters in the library
add: Medical eyepatches
/:cl:

---
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[b5ebf5c942...](https://github.com/LemonInTheDark/tgstation/commit/b5ebf5c9423cb3b39a2b9cfb6524b157dc6cb4b2)
#### Monday 2023-04-17 11:26:07 by Helg2

Adds better parts for syndie mechs, some tooltips to mech maintenance mode and some little changes. (#74466)

## About The Pull Request
Kinda resusticates #72442 cause the whole conflict was stupid.
Adds t4 parts for dark gygax, mauler and reticence (for the sake of
shitspawn) and t3 for dark honker.
Formulas of better parts to understand the difference:

https://github.com/tgstation/tgstation/blob/aff9cf1b434c7a95d156ea20108d8b2bc015083d/code/modules/vehicles/mecha/_mecha.dm#L427-L439


Made examine text into span_notices so it's not just plane text.
Also added tooltips for maintenance. Screens to compare:

![image](https://user-images.githubusercontent.com/93882977/229368394-23ca7388-2640-4a82-8134-36a18878b687.png)

![image](https://user-images.githubusercontent.com/93882977/229368398-d4654b56-78e9-4321-80cc-cad31cfabef8.png)


Dark gygax will now spawn without access adding regime.
Tool interactions with mech will now have sounds. (wrench and crowbar)
Removing parts from mech will now put them in your hands, and not just
under the mech.
When inserting parts in mech they won't make some noisy noise, already
forgot which noise it was, but i changed it for some reason, so meh.

Also fixed that you can remove capacitors and scanning mods from mech
without proper maintenance as it works with cell. Closes
https://github.com/tgstation/tgstation/issues/71577
## Why It's Good For The Game
Syndie mechs are still week. Didn't see them in half a year.
## Changelog
:cl:
qol: changed mech description to span_notices and just slightly comfier
to use.
qol: added tooltips for mech's maintenance mode.
balance: added t4 parts for mauler and dark gygax. And t3 parts for dark
honker.
fix: fixed that you can remove capacitor and scanmod from mech without
proper maintenance steps. Now you can't
/:cl:

---
## [bob-b-b/tgstation](https://github.com/bob-b-b/tgstation)@[54bf3808b8...](https://github.com/bob-b-b/tgstation/commit/54bf3808b80ec8ef83bee4062d2361e9f38d8ae8)
#### Monday 2023-04-17 12:10:48 by SyncIt21

Stops station blueprints from expanding areas of non atmos adjacent turfs. (#74620)

## About The Pull Request
Fixes #74605

the problem starts with `detect_room()` proc. This proc returns turfs
even those with `atmos_adjacent_turfs` = null. This means it returns
turfs that has a wall, airlock, window etc i.e. whatever that stops air
from flowing through it. This coupled together with `create_area()`
causes some wierdness.

Let's take an example
![Screenshot
(154)](https://user-images.githubusercontent.com/110812394/230769831-e84819f2-31b2-4a67-a8bb-5e07e1c5a1cc.png)

Area A is well defined i.e. it has been created via the station
blueprints and is highlighted in green, Area B however is only
theoretical i.e. we haven't created it yet or we are about to create it.
Now you might be thinking Area A is completely walled & sealed off, it
should be physically impossible to expand it unless we broke down one of
it's walls and so since we are standing in Area B it shoudn't even give
me the option to expand area A Right? right? r.i.g.h.t?
![Screenshot
(155)](https://user-images.githubusercontent.com/110812394/230770056-169cbab3-4516-4da7-ae2c-4f40b50be9ba.png)
Well PHFUUK. The area editor completely ignores the laws of physics and
allows me expand Area A anyway. This could cause some real power gaming
shit because if you create an area next to an area having an APC you
could use that area power without even making your own apc by simply
expanding that area(like using someone else's wifi from outside their
house without them even knowing)

#73850 accidently built on top of this as it relied on this to detect
duplicate APC's but the checks became way too strict as it would check
areas of surrounding walls for apc's and throw the conflicting apc
error. You can now build room's next to each other even if they have
fuctioning apc's however you still can't build rooms in space on top of
shuttle walls because that's been the default behaviour for years and
hasn't been touched one bit.

## Changelog
:cl:
fix: station blueprints no longer expands & detects areas of non atmos
adjacent turfs.
/:cl:

---
## [restarone/violet_rails](https://github.com/restarone/violet_rails)@[3d13e4c7fd...](https://github.com/restarone/violet_rails/commit/3d13e4c7fdb101fb91297dea864eb7ee409746eb)
#### Monday 2023-04-17 12:20:26 by Don Restarone

[fix] optimize analytics V2 further + lockdown profiler (#1522) (#1523)

Addresses: https://github.com/restarone/violet_rails/issues/1399 and https://github.com/restarone/violet_rails/issues/1452

## Profiling Results 📈 🧪 


### Slight improvements to user experience

When analysis going back 1 year is shown, there is a noticeable performance improvement:

<img width="1728" alt="Screen Shot 2023-04-08 at 11 03 31 AM" src="https://user-images.githubusercontent.com/35935196/230728720-31d5d2c0-83e0-4aa2-b3ef-fede1458ff4f.png">

### Less memory & objects used
When a 1 year analysis is shown, less memory and objects are allocated and retained: 

<img width="1728" alt="Screen Shot 2023-04-08 at 11 04 09 AM" src="https://user-images.githubusercontent.com/35935196/230728751-5302c578-4240-4f77-8ac8-166d2046be27.png">

### Garbage collector is running consistently 
on a per request basis, we observe that the garbage collector runs before the request is served. Indicating that used memory has been drained and freed to be used for other requests. 

<img width="1728" alt="Screen Shot 2023-04-08 at 11 06 48 AM" src="https://user-images.githubusercontent.com/35935196/230728822-c1f86bd8-b8fb-45ee-86fa-848c27698a6f.png">


# Real life example, Marked Restaurant

## Resource usage

comparison of memory / CPU usage before and after patch

### Baseline 🆎 

The "resting memory rate" for a high traffic Violet system is around 600MB: 
<img width="1728" alt="Screen Shot 2023-04-09 at 11 44 16 AM" src="https://user-images.githubusercontent.com/35935196/230782692-84553698-fc07-4392-b7e6-45cda169d370.png">

### Before ⏪ 

Viewing the 1 year analysis: 

<img width="1728" alt="Screen Shot 2023-04-09 at 11 42 23 AM" src="https://user-images.githubusercontent.com/35935196/230782749-11df1621-27ce-4b08-bf65-3625e5eddf7f.png">

Viewing the 1 month analysis: 

<img width="1728" alt="Screen Shot 2023-04-09 at 11 42 08 AM" src="https://user-images.githubusercontent.com/35935196/230782771-8801aa10-13c3-4bc5-82bc-70d09924000b.png">

We observe 1.2 GB of memory use (double the resting rate)

Profiler result 📈 
While attempting to run the memory profiler on the 1 year analysis, we observed 3GB+ of memory usage ⚠️ 

<img width="1728" alt="Screen Shot 2023-04-09 at 11 43 51 AM" src="https://user-images.githubusercontent.com/35935196/230782803-0ca221c6-976b-4e28-a669-67f8e196f6d0.png">

⭐  After the test was run, puma was restarted to ensure system stability

### After ⏩ 

Viewing the 1 year analysis: 
<img width="1728" alt="Screen Shot 2023-04-09 at 12 08 06 PM" src="https://user-images.githubusercontent.com/35935196/230783850-ee5963b2-7280-4323-9dbf-73812671b040.png">

We observe 720MB of memory use

Viewing the 1 month analysis:
<img width="1728" alt="Screen Shot 2023-04-09 at 12 11 44 PM" src="https://user-images.githubusercontent.com/35935196/230783889-8fb54846-47d0-487f-9480-3ded87fc7217.png">

We observe 850 MB of memory use 


Profiler result 📈 
We observe 900MB of memory use when profiling the 1 year analysis
<img width="1728" alt="Screen Shot 2023-04-09 at 12 10 11 PM" src="https://user-images.githubusercontent.com/35935196/230783899-5a66ded5-8529-4900-aab2-9003d89e06b1.png">

### Result

The system is now consuming memory in analytics V2 comparable to its resting memory usage rate. 







Co-authored-by: Prashant <25191509+alis-khadka@users.noreply.github.com>

---
## [Cykeek-Labs/kernel_realme_sdm710](https://github.com/Cykeek-Labs/kernel_realme_sdm710)@[8791946ad3...](https://github.com/Cykeek-Labs/kernel_realme_sdm710/commit/8791946ad3ee538c71e81b625ee0a5f0be6a7020)
#### Monday 2023-04-17 12:40:13 by Dave Chiluk

sched/fair: Fix low cpu usage with high throttling by removing expiration of cpu-local slices

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

---
## [IAD3D/OrbsVR](https://github.com/IAD3D/OrbsVR)@[44f5e44ef8...](https://github.com/IAD3D/OrbsVR/commit/44f5e44ef8f014e57587d95d4c91c379b1f7d843)
#### Monday 2023-04-17 13:33:28 by Juriipro

[Graph] New blasons meshes and textures, Nomenclature clean, All Nature meshes Collision updated

Ah you got an ass on you alright,see thats what he is talkin’ about. Spread your ass open dude,,you could do the Rumpshaker huh? The Thugshaker. Gimme the Thugshaker dude shake your ass. Take your hands off and shake that shit,pull your shirt up i know you can shake it. Yeah thats some Thug ass right there. Oh yeah that’ll work. You got the booty dude. God damn. Look good bro? Yeah,nice huh? Alright that’ll worth more. Put that condom on,you gonna sit on that shit? Alright lets get it over with,you alright.
https://youtu.be/MAYKoc7_B0g?list=LL

---
## [Holoo-1/tgstation](https://github.com/Holoo-1/tgstation)@[997dac9616...](https://github.com/Holoo-1/tgstation/commit/997dac9616768643cfa9ddce53432d684e196fb1)
#### Monday 2023-04-17 13:49:06 by necromanceranne

Imports and Contraband: Different! Cargo crates without locks! MEAT! (#74490)

## About The Pull Request

### **Cargo Black Market goods should stay in cargo's hands**

#### New Cargo Console Category: Imports

This category is explicitly the non-departmental category beyond simply
having a Misc category. It is meant for material that nobody is meant to
be buying for their departments, and mostly for the odd-ball crates that
might show up. It also allows us to maintain contraband as exactly that;
contraband that the departments shouldn't have access too whatsoever. If
someone is buying from this category, they probably intend to be a
cheeky fuck.

<details>
  <summary>The New Changes</summary>

#### Baseline Imports

MEAT: MEAT (meat backpack you can eat)

<details>
  <summary>MEAT</summary>
  
![MEAT
MEAT](https://user-images.githubusercontent.com/40847847/229593459-f3c98abe-114b-43c1-a3e2-afc16b76c84f.png)
![MEAT MEAT MEAT
MEAT](https://user-images.githubusercontent.com/40847847/229593473-07a30781-a05e-4ca5-893b-778900cd2d1c.png)

</details>

Duct Spiders: They're adorable and cause a mess, but that doesn't stop
Nanotrasen from importing them from the Australicus sector to your
station!

Stack of 50 Bamboo Cuttings: Pretty expensive and kind of a premium.
Allows for those people looking to make bamboo decorations without
hoping botany exists, and are at least willing to pay. Also lets them
make horribly dangerous stuff with bamboo, of course.

A Single Sheet of Bananium: The problems this will cause I think speak
for themselves. (mostly due to a clown fruitlessly attempting to make
something actually disruptive while bankrupting cargo)

Natural Fish Bait: It isn't cheating, it's homemade. (Really good bait
but expensive and obviously drugs)

A dumpster...: A corpse in a dumpster, doesn't get more complicated than
that. Useful for corpse reasons.

Made using some code I borrowed from over here!
https://github.com/lizardqueenlexi/orbstation/pull/354

#### Contraband Imports

Foam Force Pistols: Same as it ever was with a price reduction. I
brought it down because riot darts are like 8 bullets a clip, and do
less damage than a disabler using riot darts. It feels like a sidegrade
weapon, and even if it technically is a ballistic weapon, it...isn't
that strong. I think this is pretty safe.

Definitely Not a Duct Spider: It's actually a giant spider in a box. If
you want to waste cargo's money while also sending them a mess to deal
with, this is the crate for you.

Russian Surplus Military Gear Crate: I took this opportunity to futz
with boltaction rifles. There are two kinds of mosin nagant you can get
in this crate. One of them is the good kind (no jamming). The other is
the shit kind (yes jamming), but you get more of them. You can get the
good ammo, or you can get the shit ammo. You'll have to pick through it
a lot more carefully to make sure you know which ones you've received.
Since this dilutes the pool even further, getting a good number of
mosins that aren't trash is even more expensive, and even if you do get
mosins at all, you might still only get the bad ammunition that doesn't
work against actual human threats as well. It also now cannot be
purchased through the security cargo supply console, and as to why they
could in the first place baffles me. Doesn't have a lock anymore
because...it's contraband? Who is locking this stuff?

**Side note: _You can make surplus 7.62 in the autolathe as well. It is
not very good except to fight fauna or naked assistants._**

**Side Side note: _I've killed off the shitty brand_new subtype and
brought peace once more to this land._**

#### Illegal Imports (Emag)

NULL_ENTRY: A journal that suggests how to make a...very interesting
weapon. The Regal Condor. Kind of an evolution on some other ideas I've
had over the years. This one is basically a secret weapon with a few
hurdles to jump through. Very lethal. Very expensive.

**Side note: _For reference, it's effectively 19 TC worth of gear to
make, but there does exist some methods to acquire this more cheaply if
you can get some bits and pieces from world spawns. Given it requires
you to get some pieces of equipment that might require additional
purchases of contraband, and getting into the captain's office to loot a
specific piece of clothing, the stakes more than make up for the
effectiveness._**

Smuggled WT-550 Autorifle Crate: This is basically the same, but you
might have noticed had you recently attempted, like me, to buy these
when you emagged them using a personal account and discovered a tragic
oversight. You couldn't, because they still needed armory access. This
removes that access, because you've already gone to the effort of
getting your hands on an illicit firearm through cargo, and if they
techs somehow miss the fact that you've purchased a WT-550...all the
better for you!

Smuggled WT-550 Ammo Crate: Includes AP and Incendiary!

**Side note: _You can get WT-550 ammo again via the Illegal Technology
node._**

Shocktrooper: Replaces the Special Ops crate. Contains a box of EMPs,
smoke grenades, a couple of gluon grenades and a couple of frag
grenades. Funsies.

Special Ops: The NEW Special Ops crate. Contains a chameleon mask,
jumpsuit and agent card. And a knife.

**Side note: _This is what appears in some cargo loan events._**

Refurbished Mosin Nagant Crate: The actual good mosin nagants. There are
6 of them. But they don't come with spare ammo. Hand them out to your
techs!
</details>

#### New Crates

- MEAT crate - Standard
- Duct Spider crate - Standard
- Giant Hostile Spider crate - Contraband
- 50 sheets of Bamboo crate - Standard
- A single sheet of bananium crate - Standard
- Natural (drugs) fish bait - Standard
- Dumpster with a corpse in it - Standard
- Shocktrooper crate (Grenades) - Emag
- Special Ops crate (Disguise) - Emag - Appears in some cargo loan
events
- Refurbished Mosin Nagant crate - Emag
- Regal Condor construction journal (NULL_ENTRY) - Emag

#### Changed Crates

- Foam Force Pistols (cheaper) - Contraband
- Russian Surplus Crate (less reliable, can't be bought by security
console) - Contraband
- WT-550 crate (more obtainable via personal accounts, thus
incriminating, not armory locked) - Emag
- WT-550 ammo (includes incendiary and AP) - Emag

#### Crates that got moved, unchanged, into Imports

- Foam Force Crate 
- Cosa Nostra Crate 
- Black Market LTSRBT 
- 'Contraband' Crate 
- Biker Gang Crate

#### Not crate changes
- You can print Surplus 7.62 (same as normal 7.62 but it sucks against
armor) from hacked autolathes.
- You can get WT-550 ammo from illegal tech.
- Removes the redundant Brand New Mosin subtype
- Fixes a potential exploit with jamming chance on Mosins.

## Why It's Good For The Game

I just think some of the magic of Cargo getting their hands on obviously
dangerous equipment and either hording it for themselves or attempting
to pawn it off was lost in recent times. A lot of this 'black market'
gear, however, suddenly became openly available to the crew anyway. For
_free_. Contraband crates and mafia crates could be purchased via the
Service budget. Security could just stock up en masse on mosins through
their console. And one fairly unfortunate consequence of a few recent
changes has made it nearly impossible to actually get illicit gear in
the first place, even if you did go to the effort of getting the money
for it.

On top of this, most of cargo's goods are pretty safe purchases. There
isn't much that would be considered 'actually a really bad idea to buy'
other than maybe supermatter shards. I wouldn't mind there existing ways
for someone to waste cargo's money while also causing them to have to
clean up the mess.

## Changelog
:cl:
balance: A significant overhaul of various illicit and dubiously legal
goods and gadgets available via cargo.
balance: Cargo now has an Import category for all non-departmental
goods. (And black market goods)
balance: Most contraband that already exists has been moved into
Imports.
adds: Includes several new imports of dubious quality. You get what you
pay for.
code: Removes the brand new mosin subtype as it is now defunct.
fix: Fixes potentially exploitative code in the jamming proc. Cleans up
that code while I'm at it.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>
Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>

---
## [XenonyxBlaze/dsc-website-task](https://github.com/XenonyxBlaze/dsc-website-task)@[0ed20df6fc...](https://github.com/XenonyxBlaze/dsc-website-task/commit/0ed20df6fcf4945645047ffb1c42042cdf6e4355)
#### Monday 2023-04-17 14:04:30 by Aarav Rajput

Ficed possibly null -> daisy chained nullish coalescing operator [Fuck you baltimore]

---
## [microsoft/terminal](https://github.com/microsoft/terminal)@[21464fe41c...](https://github.com/microsoft/terminal/commit/21464fe41c9c09eac4b9e2d85225f18f1f3c2c7b)
#### Monday 2023-04-17 14:13:07 by Mike Griese

Manually hide our DesktopWindowXamlSource (#15165)

As discussed in #6507

Newer builds of Windows do this automatically. However, this was spotted
in the wild on 1.18. It's possible the threading changes created a
situation where the OS-side fix no longer applied to us. So let's just
do it manually. It doesn't have any side effects.

I saw this once on Win11, but couldn't repro it this morning when I
tried to add this fix. I'm just gonna assume this worked, despite the
fact that I can't repro it on win11 anymore.

closes #6507

See also #14957

## detailed description

> `WindowsXamlManager::XamlCore::Initialize` calls
`ConfigureCoreWindow`, which creates a `CoreWindow` on the thread

> Problem is, we're calling that on the main thread (which doesn't have
_any_ windows), and then eventually creating a `DesktopWindowXamlSource`
on a second thread for the actual window

> It's not that it "manages a window", it's that it "manages xaml on
Windows OS". just use ICoreWindowInterop -- QI for ICoreWindowInterop
and call get_WindowHandle.

Also see:
*
[ICoreWindowInterop](https://learn.microsoft.com/en-us/windows/win32/api/corewindow/nn-corewindow-icorewindowinterop)
*
[WindowsXamlManager.InitializeForCurrentThread](https://learn.microsoft.com/en-us/uwp/api/windows.ui.xaml.hosting.windowsxamlmanager.initializeforcurrentthread?view=winrt-22621#windows-ui-xaml-hosting-windowsxamlmanager-initializeforcurrentthread)
* The source code in
`onecoreuap\windows\dxaml\xcp\dxaml\lib\WindowsXamlManager_Partial.*`
* os.2020!6102020 which fixed MSFT:33498969, MSFT:27807465,
MSFT:21854264

---
## [jrcribb/terminal](https://github.com/jrcribb/terminal)@[5a34d92cb5...](https://github.com/jrcribb/terminal/commit/5a34d92cb5c99000e95f612cb8bc23ba374dd941)
#### Monday 2023-04-17 15:03:35 by Dustin L. Howett

winget.yml: switch to manually using wingetcreate (#15023)

It was brought to my attention that we should be more restrictive in
which tasks we ovver a GitHub token to. Sorry!

With thanks to sitiom for the version parsing and the magic GitHub
action syntax incantation for determining what is a prerelease.

---
## [Arijit1000/evals_OpenAI](https://github.com/Arijit1000/evals_OpenAI)@[d0e7844c48...](https://github.com/Arijit1000/evals_OpenAI/commit/d0e7844c482b7b65961bc80dad64559ff8ffa488)
#### Monday 2023-04-17 15:16:49 by Derek Pisner

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
## [Arijit1000/evals_OpenAI](https://github.com/Arijit1000/evals_OpenAI)@[fabca8cebb...](https://github.com/Arijit1000/evals_OpenAI/commit/fabca8cebb3f8e14d1f374e448533e0bde6e5a68)
#### Monday 2023-04-17 15:16:49 by Nick Clyde

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
## [Arijit1000/evals_OpenAI](https://github.com/Arijit1000/evals_OpenAI)@[776e4fa212...](https://github.com/Arijit1000/evals_OpenAI/commit/776e4fa212288be152c3030cf36fd04c8d939230)
#### Monday 2023-04-17 15:16:49 by JPrenter

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
## [jsntn/emacs.d](https://github.com/jsntn/emacs.d)@[b621b549bd...](https://github.com/jsntn/emacs.d/commit/b621b549bd040a214c8851bfe971260c36c7ce43)
#### Monday 2023-04-17 15:52:44 by Jason TIAN

Add TODO for testing update from Claude in init-misc.el.

From my perspective, it felt like a sudden lightning bolt striking my
otherwise dull and uneventful life when I met him. As a young woman
trying to navigate the world on my own, I was always drawn to the
thrill of the unknown and the excitement of the unexpected. So when
Claude walked into my life, I knew that things were about to change.

His charm was undeniable, and his presence was magnetic. I found
myself falling under his spell, unable to resist his advances. Every
moment we spent together was like a symphony of passion and desire,
and I knew that I had found my true soulmate.

But as with all great romances, there were obstacles to overcome.
Claude was a man of wealth and privilege, and I was a simple girl from
a humble background. Our families did not approve of our union, and
there were those who would stop at nothing to keep us apart.

Yet through it all, we remained steadfast in our love for each other.
And in the end, it was our love that prevailed, as we overcame every
challenge that stood in our way.

Looking back on it now, I realize that my life was forever changed by
my encounter with Claude. He taught me to believe in myself, to trust
in my own intuition, and to never give up on my dreams. And for that,
I will always be grateful.

- via ChatGPT :grinning:

---
## [anrui2333/android_kernel_smartisan_sdm660](https://github.com/anrui2333/android_kernel_smartisan_sdm660)@[ec37be5225...](https://github.com/anrui2333/android_kernel_smartisan_sdm660/commit/ec37be5225c334534bc3f6a30211a64274d0a6dd)
#### Monday 2023-04-17 15:55:27 by Christian Brauner

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
        kernel/signal.c - struct kernel_siginfo does not exist in 4.14
        kernel/sys_ni.c - cond_syscall is used instead of COND_SYSCALL
        arch/x86/entry/syscalls/syscall_32.tbl
        arch/x86/entry/syscalls/syscall_64.tbl

(1. manual merges because of 4.14 differences
 2. change prepare_kill_siginfo() to use struct siginfo instead of
kernel_siginfo
 3. use copy_from_user() instead of copy_siginfo_from_user() in copy_siginfo_from_user_any()
 4. replaced COND_SYSCALL with cond_syscall
 5. Removed __ia32_sys_pidfd_send_signal in arch/x86/entry/syscalls/syscall_32.tbl.
 6. Replaced __x64_sys_pidfd_send_signal with sys_pidfd_send_signal in arch/x86/entry/syscalls/syscall_64.tbl.)

Bug: 135608568
Test: test program using syscall(__NR_pidfd_send_signal,..) to send SIGKILL
Change-Id: I34da11c63ac8cafb0353d9af24c820cef519ec27
Signed-off-by: Suren Baghdasaryan <surenb@google.com>
Signed-off-by: electimon <electimon@gmail.com>

---
## [RedSkulHYDRA/frameworks_base](https://github.com/RedSkulHYDRA/frameworks_base)@[eb0ac83300...](https://github.com/RedSkulHYDRA/frameworks_base/commit/eb0ac83300c31d898fc1eac64e4314cb90e57b64)
#### Monday 2023-04-17 17:04:54 by Adithya R

[DNM][HACK] telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6

---
## [ChefKissInc/qemu-t8030](https://github.com/ChefKissInc/qemu-t8030)@[21b0ba0280...](https://github.com/ChefKissInc/qemu-t8030/commit/21b0ba0280f0c5ea4cf79ffae73d64382f39de86)
#### Monday 2023-04-17 17:13:09 by Visual

Format these god damn files cause they're fucking unreadable

---
## [VenuRam836811/programs-in-java](https://github.com/VenuRam836811/programs-in-java)@[154cda98b8...](https://github.com/VenuRam836811/programs-in-java/commit/154cda98b8c0e3f522c4fce058d0eb3ac2187b18)
#### Monday 2023-04-17 17:24:44 by venu gopal reddy

count number of e in a string plus one

Declan: Who the hell are you?

Walt: You know. You all know exactly who I am. Say my name.

Declan: What? I don't have a damn clue who the hell you are.
Walt: Yeah, you do. I'm the cook. I'm the man who killed Gus Fring.

Declan: Bullshit. Cartel got Fring.

Walt: Are you sure? That's right. Now. Say my name.

Declan: You're ............ ?
Input
Heisenberg
Output
4
Constraints
Tip: output the count of letters 'e' case independently plus one
Example
Input
Heisenberg
Output
4

---
## [Anhmike/dolly](https://github.com/Anhmike/dolly)@[af91832c66...](https://github.com/Anhmike/dolly/commit/af91832c663025b9d5b3bd0e01be125b91a51799)
#### Monday 2023-04-17 17:30:50 by Matthew Hayes

Add response generation for examples from blog post (#27)

This adds response generation code and runs it over the examples from the [blog post](https://www.databricks.com/blog/2023/03/24/hello-dolly-democratizing-magic-chatgpt-open-models.html).

A few of the sample outputs:

**Instruction:** Write a love letter to Edgar Allan Poe.

> My love for you is as eternal and enduring as the starlit nights, as deep as the ocean depths, as strong as the wind, and as sweet as the summer breeze. My heart has been yours since the first day I saw you, and it will remain yours forever. I can see you now and my heart fills with longing for our embrace, as I long to be with you forever.

**Instruction:** Explain to me the difference between nuclear fission and fusion.

> Nuclear fission is the splitting of a nucleus, which is a heavy atom, such as uranium, into two separate nuclei, while nuclear fusion is the joining of two nuclei to form a single nucleus, such as hydrogen and helium. Fission occurs when the nucleus absorbs a neutron, leaving a remnant of the nucleus. Fusion occurs when the two nuclei come together and form a single nucleus. Fission is a nuclear reaction and fusion is a nuclear reaction.

**Instruction:** Write a tweet announcing Dolly, a large language model from Databricks.

> Dolly, the world's most accurate language model, is now available on Databricks! 🎉 🎉 🎉

**Instruction:** I'm selling my Nikon D-750, write a short blurb for my ad.

> I'm selling my Nikon D-750, an amazing camera. It has the latest features including 12MP CMOS sensor, 9-point autofocus and auto bracketing, and 3.0x optical zoom. It also has a cool Image Stabilizer system and a dual SD card slot. It is a great choice for photographers looking for a reliable camera that offers superior image quality and features.

**Instruction:** Give me a list of 5 science fiction books I should read next.

> 1. The Hitchhiker's Guide to the Galaxy by Douglas Adams 
> 2. Ender’s Game by Orson Scott Card 
> 3. 1984 by George Orwell 
> 4. Star Wars by George Lucas 
> 5. The Hitchhiker's Guide to the Galaxy by Douglas Adams

---
## [PalashRishi/CS605--Data-Analytics-Lab](https://github.com/PalashRishi/CS605--Data-Analytics-Lab)@[06d9f3cbe0...](https://github.com/PalashRishi/CS605--Data-Analytics-Lab/commit/06d9f3cbe0d01c08c2149fcbf6b49a030935bc14)
#### Monday 2023-04-17 18:54:27 by PalashRishi

Add files via upload

This file is for Data Analytics External CS605. The following are the contents of this repository:
1)Demonstrate the use of Numpy Library for various mathematical functions.
2)Demonstrate the use of Pandas to perform various operations on a dataset.
3)Demonstrate the visualization (bar, line, pie etc.) using matplotlib.
4)Write a program to use Zomato Dataset from Kaggle. Find the
   i)Country with most restaurants.
   ii)Country with most restaurants with Very Good Rating.
   iii)Top 10 Restaurants with highest ratings.
   iv)Restaurants with highest numbers of feedback.
   v)Visualize above using bar chart.
5)Write a program to use IPL Complete Dataset from Kaggle. Find the:
   i. Who won most Player of the Match? 
   ii. Winning Analysis according to Toss
   iii. Winning Team (First Bat/Second Bat) 
   iv. Winning Team (First Bat/Second Bat) according to Given Venue 
   v. Most wins by a team
   vi. Most loss by a team 
   vii. Win by highest margin (Runs)
   viii. Win by lowest margin (Runs) 
   ix. Visualize winnings of every team in bar graph. 
   x. Visualize the performance (batting or bowling) of given player in bar graph.
6)Write a program to use Netflix Dataset from Kaggle. Find the:
 i. Total number of records available in dataset 
 ii. Total number of records having any missing value 
 iii. Eliminate the missing values 
 iv. Visualize the number of records available country-wise 
 v. Visualize the number of records rating-wise 
 vi. Visualize the number of records year-wise
7)Download the WhatsApp Chat with anyone and find the followings: 
 i. Number of messages send 
 ii. Number of messages send during a given date 
 iii. Number of emojis send 
 iv. Number of media send 
 v. Visualize the messages, emoji and media using pie chart
8)Download the Students Performance in Exams dataset from Kaggle and find the followings:
 i. Percentage of students with standard lunch. Visualize the percentage of students categorized according to lunch. 
 ii. Visualize the percentage of students who completed the test preparation course against who have not completed it. 
 iii. Visualize the average math score of male and female students. 
 iv. Visualize the average score (average of math score, reading score and writing score) gender wise and race/ethnicity wise. 
 v. Visualize the number of students according to parental level of education using pie chart.
9)Download the Facebook Users by Country Data dataset from kaggle and find the followings:
   i. Top five countries with most number of users. 
   ii. Top five countries with least number of users.
10)Download the Amazon Products Sales Dataset 2023 dataset from kaggle and find the followings: 
   i. Name the top 10 Air conditioners with highest number of ratings.
   ii. Name the top 10 product name from All Electronics sub category with highest rating score.
   iii. Display the total number records available in dataset.
   iv. Display the category wise number of records. 
   v. Display the category which has highest average rating score. 
   vi. Visualize the categories in ascending order of average rating score using bar chart.

---
## [ggoraa/edgetx-badapple](https://github.com/ggoraa/edgetx-badapple)@[41eb913aea...](https://github.com/ggoraa/edgetx-badapple/commit/41eb913aea7d4edb212fca9d46c2a417288b3c03)
#### Monday 2023-04-17 19:23:57 by GGorAA

Rewritten the project in Rust
HOLY SHIT THAT'S A HUGE ASS SPEED IMPROVEMENT
whole video render time reduced from 35 min with a Python implementation TO FUCKING 2-3 MINUTES WITH A RUST IMPL HOW MAN
this is what rust is all about god daym

---
## [victorjosephespinoza/cmss13](https://github.com/victorjosephespinoza/cmss13)@[a2d5ca6e69...](https://github.com/victorjosephespinoza/cmss13/commit/a2d5ca6e69725341f0fa261a4a3f89c737e843b3)
#### Monday 2023-04-17 19:32:15 by QuickLode

Introducing the Colonial Marshal ERT w/ Anchorpoint Marines (#2318)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request
My first PR of this scale, for sure. 

Been working on this PR for two weeks off and on, and finally I believe
I have checked every box that I intended to check when I first thought
of this idea a couple months back in November or so. Original idea:
https://discord.com/channels/150315577943130112/1037030635820306562/1037030635820306562

It will be adding a Colonial Marshal Bureau ERT, a Colonial Marshal
Bureau Inspection Team, and an Anchorpoint Station ERT.

First: Anchorpoint Station, unlike many ERTs, this one will hail from a
station. The station is located in the Neroid Sector and is used as a
transit / refinery station. It's large enough to hold 3000 but never
reaches its full potential. It consists of four towers and a central
module - one of the towers houses a permanent CMB presence and in the
same tower, a contingent of Colonial Marines is onboard. There's also a
Seegson office but I didn't do anything with it here.
Reference: https://avp.fandom.com/wiki/Anchorpoint_Station

For standard inspections, a dropship is dispatched from Anchorpoint
Station to the USS Almayer to carry out their objectives.
I do expect this to be the primary usage of this entire PR, because
there was always a part lacking for Anti-Corporate/Anti-Smuggling/CMB
type of interactions. It was almost always focused on Corporate, or
USCM. Nothing else. You should consider this to be an HRP addition to
the game.

Its also important to note that the Colonial Marshals are **Colonial**
and UA law enforcement agents / investigative functionaries. **They
shouldn't be enforcing Marine Law** unless: 1. The CMP/aCO has requested
it, 2. The Colonial Marshal believes its in the best interest of the CMB
and 3. The CMB Office at Anchorpoint(admins) does not intervene to
change this decision. Jurisdiction is another interaction that will be
nice to see. Non-USCM suspects should be transferred to the CMB, and
vice versa. The CMB should also be handling crimes, especially with the
ICC, involving smuggling, black market activities, and corporate
corruption/cover-ups.

**The Colonial Marshal** - He leads the team, and should be an
experience player with some knowledge of the lore behind what they are
doing. There's objectives and a backstory to help guide players if they
are unaware.
**The CMB Investigative Synthetic** - Unlike what you would expect from
most Synthetics, this one(as the name implies) is purely for
investigative and/or law enforcement purposes, though they have brought
along a medical belt.
**The CMB Deputy** - Working under the lead of the Marshal, his loyal
deputies uphold Colonial Law, Earth Law, and help with investigations
and/or law enforcement should it be needed.
**Interstellar Commerce Commission Corporate Liaison** - This Executive
works with the Colonial Marshals specifically to observe proper trade
practices and investigate any possibilities of smuggling or black market
activity. They are also an advisory agent to the Marshals by giving them
an eye on the corporate side of things.
**Interstellar Human Rights Observer** - Through a lot of hard work, the
Observer has managed to make his way onto the frontier to document and
record any kind of atrocities that may be occurring in this dark sector
of space. It's a bit of a PR stunt, but the Observer might surprise you.
Also, in an emergency, the Observer may be able to provide medical aid
for the team - they are the most capable of it.


For Emergency Responses, a nearby dropship which was enroute to an
investigation of its own, is re-routed to the USS Almayer's distress
beacon. There is a 10% chance of this happening.
They will not fare very well in extended combat, because they are not
prepared for it. They simply come aboard to lend a helping hand to a
distress beacon.
As the Colonial Marshals are equipped for law enforcement and
investigations, they are comparably lightly armed to most things they
might encounter in or by the USS Almayer.

This is where the contingent of Colonial Marines in Tower 4 comes in.

The third ERT that may be called in is an Anchorpoint Station QRF Team.
Canonically this is purely used when a random-beacon is answered by the
CMB Patrol Team, and they are able to raise the radio back to base to
call in the QRF. Thus giving them an additional, albeit optional
objective. This is controlled entirely by admins, as the Anchorpoint QRF
Team, despite its small size and average skill levels, is equipped with
a decent amount of gear compared to the depleted stocks of the USS
Almayer. Should the CMB team be able to raise its own distress signal to
the preparing QRF team, admins may choose to grant, delay, or deny the
QRF entirely.



Those are the main points of the PR.
There are also small variation changes to CMB-related survivors and also
some changes to synths.dm. (I tried to refractor the code because the
last PR to it bugged out the way items spawn in, but I was unsuccessful
and those changes are not in this PR.)

Pizza ERT chance and Freelancer ERT chance was nerfed by 4 and 5
respectively. This gives room for this ERT, and also Pizza was a bit
LRP.. You see a ship burning with a giant hole in it and you go to
deliver a pizza...?

EDIT: Pizza ERT removed from rotation entirely a la morrow

I would love to give a great thanks to:
nauticall - for their awesome cap and badge sprites! Also they have just
been a great help to me for much of my time here :)
kitsunemitsu - for their CMB hud icons!
harryOB - for helping me with fixing my vars and procs in the main ERT!
I was able to make things a % chance thanks to him.
and forest2001 - for helping me troubleshoot and find a solution for a
really annoying piece of hud code.
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

This is a great, non-combat ERT and extremely HRP addition which adds a
phenomenal avenue of RP to the game rarely seen before. There is someone
to investigate the CL, interact with survivors, give MPs someone to talk
to, take non-USCM prisoners, assist with CMB-survivors and especially
with the new Black Market update this ERT will have tons of potential to
bring really interesting dynamics to the Almayer. The Colonial Marshal
Bureau are a HRP oriented set of roles, perfect for mini-events.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->


# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>
I have done extensive testing with this and believe I have figured out
pretty much every single bug. One thing I was not able to test was the
ERT messages for obvious reasons, but they seem to be sound - and a test
merge will definitely double check that.

In addition, there may or may not be a bug where the CMB cannot see
their own HUD Icons, but ghosts can just fine. I haven't been able to
find the cause of this yet.

https://media.discordapp.net/attachments/1042176396711170119/1064156692050358372/image.png</summary>

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

:cl: QuickLoad, nauticall, Kitsunemitsu, harryOB, forest2001
add: Introducing the Colonial Marshal Bureau Inspection and Emergency
Response Teams - A Law Enforcement & Investigative UA Functionary which
brings with it an HRP oriented set of roles perfect for your anti-corpo,
colonial, prisoner, smuggling, or other types of interactions on the
Almayer! It should unlock a very unique avenue of RP for many players,
especially smugglers, CL, survivors and the black market. This is a well
supported faction with their own frequencies, equipment, even faxes and
icons etcetera. The laws of the Earth stretch beyond the Sol.
add: Added the Anchorpoint Station Emergency QRF - A team of Colonial
Marines dispatched from Anchorpoint Station to respond to the CMB's
distress signal. Few in numbers, average in skills, but well equipped.
When things get dicey for the Marshals, they are the cavalry. This is an
admin call but makes it into an optional two-part ERT.
imageadd: Awesome looking CMB Cap, Marshal Badge and Deputy Badge by
nauticall!
imageadd: HUD Icons for each of the Colonial Marshal Bureau
Investigation Members, made by Kitsunemitsu!
imageadd: CMB key, hudsec and earpiece! Comes with a nice blue shale
radio color.
qol: Switched up some of the bugged synth loadouts, added some variety.
fix: Corrects the legacy path of hudsec where it was looking for old
paths instead of the updated ones - hudsec should work fine now. Thanks
to forest for his help in spotting these.
tweak: Superficial changes to cryo ERT loadout and CMB-relevant survivor
loadouts.
tweak: Superficial changes to armor vest so that they can carry
guns/lights.
tweak: Superficial changes to not being able to put on vests over
certain uniforms.
tweak: Freelancer ERT chance down from 25 to 20.
tweak: Synthetic vendor has some packs renamed for clarity, and receives
the tech welder satchel and medical satchel as an option.
del: Synthetic nurse hat is gone from Synthetics!
del: Pizza ERT is removed from rotation
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: naut <55491249+nauticall@users.noreply.github.com>
Co-authored-by: naut <nautilussplat@gmail.com>

---
## [serp0tat0/ProjetMusique](https://github.com/serp0tat0/ProjetMusique)@[dbcaf9f398...](https://github.com/serp0tat0/ProjetMusique/commit/dbcaf9f398549a414696904f276b435ee4508e84)
#### Monday 2023-04-17 20:18:36 by ViveReneLevesque

Added some juice, working on the GUI now, stuffs pretty fun. Our overall app is kinda done now, like the backend is pretty pimped up, so like, we chilling, we hard chilling. Shits pretty cool, can you believe I was able to do this shit alone?
I mean, its really not done yet, I could also add a save feature and keep ur data from old scans, also would try giving full kinda access to spotify api but that shit is way too difficult to deal with, like, have you seen the  demonic shit you need to summon just to have access to how many songs you have liked? Stuffs a little too hard, spotipy has like no documentation and even if it does, nothing gives you access to the amount of times listened to an artist. I should try to get in contact with a programmer who has written something giving access to the API, just to have some insight. Well, I am glad to have my sanity back and seeing progress on this project.

---
## [schnow265/Sketchbook](https://github.com/schnow265/Sketchbook)@[e24cd6fc53...](https://github.com/schnow265/Sketchbook/commit/e24cd6fc5325c0ec24fb0fea1bd4a55bb9c1ba14)
#### Monday 2023-04-17 20:30:09 by schnow265

Delete remappedSrc directory

It’s just the remapped java files from the 1.19.Fuck You 4 Update.

---
## [PostHog/posthog.com](https://github.com/PostHog/posthog.com)@[c6097ab08f...](https://github.com/PostHog/posthog.com/commit/c6097ab08fc4708a393c4f725ef3d86816447a20)
#### Monday 2023-04-17 20:35:23 by Charles Cook

Small tweak suggestions to modern data stack article (#5729)

* Small tweaks

Few small tweaks, feel free to ignore obv:

- Removed the tl;dr in intro as it was repetitive and felt redundant (it's summarizing 3 sentences)
- Removed more air quotes around modern data stack - if you're talking to engineers and call it 'modern data stack' you sound a bit 'how do you do, fellow kids'
- Removed link to our CDP docs because we don't _really_ have a CDP product yet
- Micro changes to flow

In general I think there are still slightly too many links in here that would take people away from the page (we don't need to link to every single relevant article we've written on the topic, especially as we have a Further reading section), but I'll leave that to you to decide!

I wonder if around line 95 there should be a break with a new title called 'So what's the problem' or something - I had to re-read the article to really get the crux of what the burning problem is here besides 'it's a bit complicated'. The gap that is created between (product?) engineers and the data they use is super valuable, but I think a bit buried.  

(Btw sorry to be very nit-picky after it's already been published - ended up re-reading a few times as I think this is awesome Twitter content I'm going to pilfer...)

* Update contents/blog/modern-data-stack-sucks.md

Co-authored-by: Ian Vanagas <34755028+ivanagas@users.noreply.github.com>

---------

Co-authored-by: Ian Vanagas <34755028+ivanagas@users.noreply.github.com>

---
## [lessthnthree/Skyrat-tg](https://github.com/lessthnthree/Skyrat-tg)@[5a348474a0...](https://github.com/lessthnthree/Skyrat-tg/commit/5a348474a01a07490094be828ae269f4c98b13ef)
#### Monday 2023-04-17 21:19:25 by SkyratBot

[MIRROR] IV drips' default transfer rate is no longer zero. [MDB IGNORE] (#20567)

* IV drips' default transfer rate is no longer zero. (#74724)

## About The Pull Request

Set default IV transfer rate to maximum (5) instead of 0.
## Why It's Good For The Game

> Set default IV transfer rate to maximum (5) instead of 0.

When you hook someone onto an IV drip, you naturally expect that to be
the end of the process - you hooked someone to a drip, and now you can
go about your day. Them needing to fiddle with buttons is bad for
several reasons:

- It is unintuitive.
IV drips don't look like machines. Their sprite doesn't reflect the fact
that you need to fiddle with the settings before they can work the same
way any other machine or computer might. And to be honest, they
shouldn't.
- It is separate from how every other server currently has it.
Yes, yes, I know that argument is very flawed and full of holes. But
what I'm trying to say with it is, effectively speaking, an extension of
the above point. In other servers, you drag-click someone to an IV drip
and there we go, it's functional. In TG, it just-so-happens to not be
functional due to what is almost definitely a recent oversight, which
very much can, has, and will lead to unnecessary frustration.
- There is no practical reason for it to be set at 0.
Imagine if chem dispensers started at +0 units and needed to be set to
+5 to continue. Or if bottles had a transfer rate of 0u. Or if guns
started with their safeties on. Even if it made sense, it would just be
frustrating and needless, and wouldn't improve the game in any
significant manner enough to offset frustration. We're here for fun, not
perfect balance or realism/verisimilitude after all.
- It's an oversight.
It was changed in #71217. Before that, it was always set to the maximum,
5u. However, presumably due to confusion (Variables that can be adjusted
ingame usually are set to zero/the minimum possible) it ended up being
changed to this.

Apparently an argument can be made that this is fine because fumbling to
get medical aid done is a part of the game. I disagree heavily - blood
bags are already stored in the cold room, something only 2/5 of the
roles in medbay even have access to, with the paramedic, virologist,
chemist all being unable to reach it. This is already enough 'fumbling'
that's necessary. If someone moved the blood bags outside the cold room
next to the IV drips, then all the better - it's a reward for medbay
being prepared.

However I wouldn't mind if someone asked me to make it so the default
transfer rate is, well, something below maximum. It's common practice in
a lot of parts of SS13 to have things set in an unoptimized state so
players can go around improving them, such as air alarms, cryogenics,
etc. Just as long as it's not literally unusable otherwise, as the
'minimum basic setup' should just be slapping on a blood bag!
## Changelog
Dunno what to put here TBH. Can't tell if it's qol, fix, balance, etc.

:cl:
qol: Set default IV transfer rate to maximum (5) instead of 0.
/:cl:

* IV drips' default transfer rate is no longer zero.

---------

Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>

---
## [mentalisttraceur/home](https://github.com/mentalisttraceur/home)@[5ed6a38ba3...](https://github.com/mentalisttraceur/home/commit/5ed6a38ba35b72a209879d96593793ba0f982028)
#### Monday 2023-04-17 22:03:40 by Alexander Kozhevnikov

.emacs: fix get-command-from-history function

First, to fix behavior in a few edge cases in `consult-history`:

* If I am on an old line in the scrollback and load it up as a
  history line to reuse:
  * I most definitely do not want to overwrite that history in
    the scrollback - `consult-history` overrides the line at
    point, fixed-consult-history overrides the latest input
    line.
  * If I Ctrl-g to abort, I probably want to go back to where
    I was because I hit "gh" on accident, or I realized that
    I meant to use another line, and in any case getting back
    to the buffer is a trivial "G" - a naive version of the
    fix for the prior point would leave the cursor at the end
    of the buffer instead of returning back where we were.

* For the common case of being on the latest (bottom) line
  already, behavior remains the same, including ensuring
  that point is in the original position if we abort mid-
  -selection and so on.

* Since `consult-history` doesn't provide any way to say what
  the initial query is besides having it already under point,
  nor for getting the result besides inserting it into the
  buffer (instead of what it selected as the initial query at
  that), to do the above we need to mutate the buffer before
  even calling `consult-history` - if `consult-history` is
  then aborted, we'd end up with junk writes in the buffer,
  and in the undo history. So this wrapper cleans up both.

So that's the rationale for `fixed-consult-history`. I pulled
out functions which might be useful for other REPL-in-Emacs
work, and pulled out the `save-mutation` macro because, like
the `save-excursion` macro, it will probably be useful again.

Second, a human speed/fluidity improvement:

* I decided that I would rather have commands execute as soon
  as an option is selected. Since I've got vi-style commands
  in the minibuffer too, there's very little reason to have
  them wait for me in the main buffer. In the rare event that
  I want something more, I can copy+paste manually. If that
  ever becomes enough of a problem, I will eventually bind "q"
  in Vertico minibuffers (or maybe just in Consult functions,
  or maybe even just in `consult-history`) so that I can exit
  the way that consult-history normally exits, putting the
  selection into the command but not running it.

Third, some integration with Evil:

* Evil didn't recognize `*consult-history` as edit commands
  which could be repeated. The `evil-declare-*` functions
  didn't help - it kept trying to repeat the last repeatable
  command prior to calling `*consult-history`. Luckily, Evil
  has an (utterly under-documented) API for hooking in and
  telling Evil what actions to repeat. I gave some effort to
  come up with a sensible repeat behavior:
  * This command replaces a whole current input line (whether
    it's empty, or has text already typed out for searching),
    and runs it, so a repeat reruns the command.
  * Repeat doesn't go into another the manual history search
    and line edit (just like how repeating an insert/replace
    does not drop into insert mode for more manual entry).
  * If I ever add the separate "exit consult-history but
    don't run the command" feature, repeat will remember
    if the previous call ran the command or just put it into
    the command line. (And then maybe I'll have it replace
    the line the cursor is currently on, or insert, instead
    of the current command-line. That needs to be decided.)

---
## [HUSSIENDATA/PORTFOLIOPROJECTS](https://github.com/HUSSIENDATA/PORTFOLIOPROJECTS)@[419763f134...](https://github.com/HUSSIENDATA/PORTFOLIOPROJECTS/commit/419763f134e5bc5bb66cd8e00347929375c888ae)
#### Monday 2023-04-17 22:39:24 by HUSSIENDATA

Add files via upload

Excited to share my latest creation - a Tableau dashboard that visualizes our online customer sales data! With this dashboard, I was able to gain insights into our sales patterns and customer behaviors.
First, I looked at the total revenue and total revenue per gender (male and female). It was interesting to see that while overall revenue was strong, revenue from male customers was lagging behind that of female customers.
Next, I analyzed the total number of purchases per gender and payment methods. I found that while female customers made more purchases overall, female customers were more likely to use credit card payments.
Finally, I looked at the most used browser by the number of customers. It was surprising to see that a majority of our customers were using Chrome, followed by Safari and Other.
Overall, this dashboard has helped me gain a better understanding of our online customers and their purchasing behaviors. I'm looking forward to using these insights to improve sales strategies and better serve customers in the future. Check out the dashboard and let me know what you think!"

---

