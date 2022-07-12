## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-07-11](docs/good-messages/2022/2022-07-11.md)


1,684,071 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,684,071 were push events containing 2,485,101 commit messages that amount to 190,519,215 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 35 messages:


## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[b74df4cbdd...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/b74df4cbdd0c2618a4d8477a74a233fc883b7c19)
#### Monday 2022-07-11 00:17:10 by SkyratBot

[MIRROR] Revisiting The Goliath: Or, that time I dripped out the SBC Starfury just because [MDB IGNORE] (#14813)

* Revisiting The Goliath: Or, that time I dripped out the SBC Starfury just because (#68126)

Drips the SHIT out of the SBC Starfury while not completely overhauling it. Touches everything NOT in engineering or southward (because I love how scuffed that part is and refuse to touch it on principle) - Also converts one map varedit into a real boy subtype, and moves tiny fans to their own file.

Mandatory disclosure on the gameplay changes:
Fighters 1 and 3 are now NOT in the hangar, and are now attached to the formerly unused gunnery rooms.
Cryo now works. Yeah. I know.
You can actually open the anesthetic closet now.
Everyone now shares three spawners. This doesn't reduce the amount of people who can play when this rolls, as I've adjusted var/uses in accordance: it just reduces clutter.
A few of the horizontal double airlocks have been compacted into glass_large airlocks.
The bar windows now actually have grilles like they were meant to.
Four turbines have shown up. They aren't functional*, they just look like gunnery and conveniently fit in the spots. I'm sure this is space OSHA compliant.
The map is ever so slightly smaller, vertically. This should distance us from an edge case where somehow all space levels are too cluttered for this to spawn properly, for the time being.

*Technically there's nothing stopping you from using them besides the amount of time it'd take for the operatives to kick your ass

This map was originally designed wayyy back before we even had the computer sprites we have now, (#27760 if you want to see SOUL) and it shows. While it will never have it's SM again, we can at least make the thing much nicer to look at.

* Revisiting The Goliath: Or, that time I dripped out the SBC Starfury just because

Co-authored-by: BluBerry016 <50649185+unit0016@users.noreply.github.com>

---
## [KhaoticPluto/Prototype](https://github.com/KhaoticPluto/Prototype)@[88215214c5...](https://github.com/KhaoticPluto/Prototype/commit/88215214c59d85cc9782a8eea54ffec6f0c33203)
#### Monday 2022-07-11 00:46:01 by xyndall

fixing the models

oh god it was an annoying as thing, luckily i got a new process that is much better and less finiky and yeah

---
## [davidcloak/StaticFiles](https://github.com/davidcloak/StaticFiles)@[622f106b30...](https://github.com/davidcloak/StaticFiles/commit/622f106b3019c25fe2836d74e8d19606927479f2)
#### Monday 2022-07-11 00:56:35 by davidcloak

FUCK YOU WINDSTREAM searchguide redirect FUCKING ANNOYING

---
## [bitchard/the-road](https://github.com/bitchard/the-road)@[ac1c9b5c12...](https://github.com/bitchard/the-road/commit/ac1c9b5c12d2a334672e606b565e6f49cc06c2a4)
#### Monday 2022-07-11 01:04:57 by bitchard

Replacment of my mistake

What a learning experience and I left it all in because I'm not ashamed of it. That's how we learn and I'm not perfect and don't ever want to be so enjoy my total screw-up.

---
## [Alexandah/mOuSe_prototype](https://github.com/Alexandah/mOuSe_prototype)@[df9aba7e60...](https://github.com/Alexandah/mOuSe_prototype/commit/df9aba7e601cb5e63a7f491956000db3c7294b70)
#### Monday 2022-07-11 02:10:29 by Alexander Davis

Added a few more test pages. Began working on creating a selection mode for DOM hopper that may prove more useful on standard janky webpages: selecting interactable nodes. Some nodes are interactable by default (input, etc), so that's a no brainer. However, much of the time, the 5 iq fucks known as web devs will spite semantics by using divs with an onclick listener instead of a goddamn button. But it gets worse! Javascript has no getEventListeners method! It doesn't even visibly keep track of them! So I am going to have to override the default behavior of the addEventListener method to keep a dict of dom nodes and their associated event listeners, which I will then use in my getEventListeners method. I'll also have to preemptively inject this script into the page before any other scripts run, to force them to use the updated add event listener method. Gotta love js. Jokes aside, this should be a fun challenge.

---
## [JiskTH/raider3.5](https://github.com/JiskTH/raider3.5)@[a099818692...](https://github.com/JiskTH/raider3.5/commit/a099818692113e4b076860da3778169ace3030da)
#### Monday 2022-07-11 04:45:19 by Jisk

Add a rejoin toggle.

Don't we all hate the idiots that rejoin and get god mode or some shit?

---
## [blazerpaul15/kernel_xiaomi_mt6785](https://github.com/blazerpaul15/kernel_xiaomi_mt6785)@[bc89026182...](https://github.com/blazerpaul15/kernel_xiaomi_mt6785/commit/bc89026182e0c2328e5b48ca357eb340bc99d93a)
#### Monday 2022-07-11 04:47:13 by Peter Zijlstra

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
## [primaryodors/podock](https://github.com/primaryodors/podock)@[8df80f619b...](https://github.com/primaryodors/podock/commit/8df80f619b15558bdaabc38b336f3f9dc0f278b4)
#### Monday 2022-07-11 05:49:46 by Julie Gagnon

I am up way too late. I mean, I get why my roommate is finally breaking up with his delusional long distance girlfriend, but goddamn did he have to choose to yell at her on the phone at quarter to 11 the night before I start my new job with a 7am meeting. Creezus jucking feist.

---
## [vega128/positron_miatoll](https://github.com/vega128/positron_miatoll)@[7b087e4930...](https://github.com/vega128/positron_miatoll/commit/7b087e49305414cb392dd1477898e7d8c98cdfb1)
#### Monday 2022-07-11 05:55:29 by bsp-open

Update to July release

Contributors list:
Aakanksha Doda <adoda@codeaurora.org>
Aalique Grahame <agrahame@codeaurora.org>
Aaron Lu <aaron.lu@intel.com>
Aaron Tomlin <atomlin@redhat.com>
Abdul Muqtadeer Ahmed <amuqtade@codeaurora.org>
Abel Wu <wuyun.wu@huawei.com>
Abhay Swaroop <aswaroop@codeaurora.org>
Abhijeet Dharmapurikar <adharmap@codeaurora.org>
Abhijit Pradhan <abhijit@codeaurora.org>
abhinav kumar <abhikuma@codeaurora.org>
Abhinav Kumar <abhikuma@codeaurora.org>
Abhiram Jogadenu <ajogaden@codeaurora.org>
Abhishek Ambure <aambure@codeaurora.org>
Abhishek Arpure <aarpure@codeaurora.org>
Abhishek Singh <absingh@codeaurora.org>
Abhishek Singh <absingh@qti.qualcomm.com>
Adam Manzanares <adam.manzanares@wdc.com>
Adesh Keremane <adeshk@codeaurora.org>
Adil Saeed Musthafa <adilm@codeaurora.org>
Adithya R <gh0strider.2k18.reborn@gmail.com>
Aditya Bavanari <abavanar@codeaurora.org>
Aditya Kodukula <akodukul@codeaurora.org>
Aditya Sathish <asathish@codeaurora.org>
Adrian Salido <salidoa@google.com>
Adwait Nayak <adwait@codeaurora.org>
Aggarwal Nishank <naggar@codeaurora.org>
Aggarwal, Nishank <naggar@codeaurora.org>
Agrawal Ashish <ashishka@codeaurora.org>
Agrawal, Ashish <ashishka@codeaurora.org>
Ahmad Kholaif <akholaif@codeaurora.org>
Ajay Agarwal <ajaya@codeaurora.org>
Ajit Pal Singh <ajitpals@codeaurora.org>
Ajit Pandey <ajitp@codeaurora.org>
Ajit Vaishya <ajitv@codeaurora.org>
Akash Patel <akashp@codeaurora.org>
Akhil P Oommen <akhilpo@codeaurora.org>
akosigi <akosigi@codeaurora.org>
Akshay Kosigi <akosigi@codeaurora.org>
Alan Chen <alache@codeaurora.org>
Albert I <kras@raphielgang.org>
Alesaiko <solcmdr@gmail.com>
Alessio Balsini <balsini@android.com>
Alessio Balsini <balsini@google.com>
Alexander Potapenko <glider@google.com>
Alexander Winkowski <dereference23@outlook.com>
Alexei Starovoitov <ast@fb.com>
Alex Naidis <alex.naidis@paranoidandroid.co>
Ali Saidi <alisaidi@amazon.com>
Alok Kumar <alokkuma@codeaurora.org>
aloksing <aloksing@codeaurora.org>
Alok Singh <aloksing@codeaurora.org>
Al Viro <viro@zeniv.linux.org.uk>
Aman Gupta <amangupt@codeaurora.org>
Amar Singhal <asinghal@codeaurora.org>
Amar Singhal <asinghal@qca.qualcomm.com>
Amir Patel <amirp@codeaurora.org>
Amir Vajid <avajid@codeaurora.org>
Amit Shukla <shukla@codeaurora.org>
Amruta Kulkarni <amrukulk@codeaurora.org>
Anand Kumar <anandkumar@codeaurora.org>
Ananya Barat <abarat@codeaurora.org>
Ananya Gupta <anangupt@codeaurora.org>
Andi Kleen <ak@linux.intel.com>
Andrea Parri <andrea.parri@amarulasolutions.com>
Andrejs Hanins <ahanins@gmail.com>
Andrew Chant <achant@google.com>
Andrew Morton <akpm@linux-foundation.org>
Andrey Ignatov <rdna@fb.com>
Andrzej Perczak <linux@andrzejperczak.com>
Andy Shevchenko <andriy.shevchenko@linux.intel.com>
AngeloGioacchino Del Regno <kholk11@gmail.com>
Aniket Kumar Lata <alata@codeaurora.org>
Aniket Randive <arandive@codeaurora.org>
Anirban Sirkhell <anirban@codeaurora.org>
Aniruddha Paul <paulani@codeaurora.org>
Anirudh Ghayal <aghayal@codeaurora.org>
anisha agarwal <anishaa@codeaurora.org>
Anish Nataraj <anishn@codeaurora.org>
Anjaneedevi Kapparapu <akappara@codeaurora.org>
Ankita Bajaj <bankita@codeaurora.org>
Ankit Gupta <guptaank@codeaurora.org>
Ankit Kumar <ankkuma@codeaurora.org>
Anna-Maria Gleixner <anna-maria@linutronix.de>
Antonio Quartulli <a@unstable.cc>
Anurag Chouhan <achouhan@codeaurora.org>
Anver sadhique <akurun@codeaurora.org>
Aravind Narasimhan <aravindn@codeaurora.org>
Archana Ramachandran <archanar@codeaurora.org>
Ard Biesheuvel <ard.biesheuvel@linaro.org>
Arif Hussain <arifhussain@codeaurora.org>
Arjan van de Ven <arjan@linux.intel.com>
arnav_s <arnav_s@codeaurora.org>
Arnav Sharma <arnav_s@codeaurora.org>
Arnd Bergmann <arnd@arndb.de>
Arun Khandavalli <akhandav@codeaurora.org>
Arun Khandavalli <akhandav@qti.qualcomm.com>
Arunk Khandavalli <akhandav@codeaurora.org>
Arun Kumar Khandavalli <akhandav@codeaurora.org>
Arun Mirpuri <amirpuri@codeaurora.org>
Ashish Kumar Dhanotiya <adhanoti@codeaurora.org>
Ashok Kumar <aponnaia@codeaurora.org>
Ashok Kumar Ponnaiah <aponnaia@codeaurora.org>
Ashok Ponnaiah <aponnaia@codeaurora.org>
Ashwini Muduganti <amudug@codeaurora.org>
Ashwini Oruganti <ashfall@google.com>
Ashwini Patil <apati@codeaurora.org>
Asish Bhattacharya <asishb@codeaurora.org>
Asodi T,Venkateswara Reddy <vasodi@codeaurora.org>
Author: Neil Zhao <nwzhao@codeaurora.org>
Avinash Chandra <avicha@codeaurora.org>
Baila, Shashikala Prabhu <csbaila@codeaurora.org>
Balaganapathy Palanisamy <bpalanis@codeaurora.org>
Balamurugan Mahalingam <bmahalin@codeaurora.org>
Bala Venkatesh <bjavvaji@codeaurora.org>
Bala Venkatesh <bjavvaji@qti.qualcomm.com>
Banajit Goswami <bgoswami@codeaurora.org>
Baowei Liu <baowei@codeaurora.org>
Bapiraju Alla <balla@codeaurora.org>
Basamma Yakkanahalli <ybasamma@codeaurora.org>
Ben Romberger <bromberg@codeaurora.org>
Ben Wang <benw@codeaurora.org>
Bhalchandra Gajare <gajare@codeaurora.org>
Bharat Bhushan Chakravarty <bchakrav@codeaurora.org>
Bharat Kumar M <mbkumar@codeaurora.org>
Bhargav Shah <bhargv@codeaurora.org>
Bhargav Shah <c_bhargv@qti.qualcomm.com>
Biao Long <blong@codeaurora.org>
bings <bings@codeaurora.org>
Blagovest Kolenichev <bkolenichev@codeaurora.org>
Boqun Feng <boqun.feng@gmail.com>
Borislav Petkov <bp@suse.de>
Bruno Martins <bgcngm@gmail.com>
Bruno Wolff III <bruno@wolff.to>
Catalin Marinas <catalin.marinas@arm.com>
c_cgodav <cgodav@codeaurora.org>
celtare21 <celtare21@gmail.com>
Chaitanya Kiran Godavarthi <cgodav@codeaurora.org>
Chaitanya Pratapa <cpratapa@codeaurora.org>
Chaithanya Garrepalli <cgarre@codeaurora.org>
Chandana Kishori Chiluveru <cchiluve@codeaurora.org>
Chandrasekaran Manishekar <cmshekar@codeaurora.org>
Chandrasekaran, Manishekar <cmshekar@codeaurora.org>
Chandrasekaran Manishekar <cmshekar@qti.qualcomm.com>
Chandrasekaran, Manishekar <cmshekar@qti.qualcomm.com>
Chandru Neginahal <cnegin@codeaurora.org>
Chaoli Zhou <zchaoli@codeaurora.org>
Chao Yu <yuchao0@huawei.com>
Cheng Jian <cj.chengjian@huawei.com>
chenguo <chenguo@codeaurora.org>
Chen Jie <chenjie6@huawei.com>
Chiawei Wang <chiaweiwang@google.com>
Chinmay Agarwal <chinagar@codeaurora.org>
Chouhan, Anurag <achouhan@codeaurora.org>
Chouhan Lokesh <c_lchouh@qti.qualcomm.com>
c_hpothu <c_hpothu@codeaurora.org>
Chris Guo <chenguo@codeaurora.org>
Chris Guo <kangxu@codeaurora.org>
Chris Lew <clew@codeaurora.org>
Christian Hesse <mail@eworm.de>
Christophe Leroy <christophe.leroy@csgroup.eu>
Christopher Chopp <cchopp@codeaurora.org>
Christoph Hellwig <hch@lst.de>
Chris Ye <lzye@google.com>
ckosuru <kosuru@codeaurora.org>
c_manjee <manjee@codeaurora.org>
CNSS_WLAN Service <cnssbldsw@qualcomm.com>
Colin Ian King <colin.king@canonical.com>
Cong Tang <congt@codeaurora.org>
Conner Huff <chuff@codeaurora.org>
Connor O'Brien <connoro@google.com>
Cosmin Tanislav <demonsingur@gmail.com>
cpratapa <cpratapa@codeaurora.org>
c_priys <priys@codeaurora.org>
Da Hoon Pyun <dpyun@codeaurora.org>
Dan Carpenter <dan.carpenter@oracle.com>
Daniel Borkmann <daniel@iogearbox.net>
Daniel Bristot de Oliveira <bristot@redhat.com>
Daniel Kahn Gillmor <dkg@fifthhorseman.net>
Daniel Kim <kimdan@codeaurora.org>
Daniel Mentz <danielmentz@google.com>
Daniel Micay <danielmicay@gmail.com>
Daniel Rosenberg <drosen@google.com>
Danny Lin <danny@kdrag0n.dev>
DARAM SUDHA <dsudha@qti.qualcomm.com>
darkhz <kmachanwenw@gmail.com>
David Benjamin <davidben@google.com>
davidchao <davidchao@google.com>
David Dai <daidavid1@codeaurora.org>
Davide Garberi <dade.garberi@gmail.com>
David Herrmann <dh.herrmann@gmail.com>
Davidlohr Bueso <dave@stgolabs.net>
David Ng <dave@codeaurora.org>
Debashis Dutt <ddutt@codeaurora.org>
Debasis Das <ddas@codeaurora.org>
Dede Dindin Qudsy <xtrymind@gmail.com>
Deeksha Gupta <deegupta@codeaurora.org>
Deeksha Gupta <quic_deegupta@quicinc.com>
Deepak Dhamdhere <ddhamdhe@codeaurora.org>
Deepak Dhamdhere <ddhamdhe@qca.qualcomm.com>
Deepthi Gowri <deepthi@codeaurora.org>
Deepthi Gunturi <dgunturi@codeaurora.org>
Demon000 <demonsingur@gmail.com>
Derek Chen <chenche@codeaurora.org>
Dhanalakshmi Siddani <dsiddani@codeaurora.org>
Dhananjay Kumar <dhakumar@codeaurora.org>
Dhanashri Atre <datre@codeaurora.org>
Dhanashri Atre <datre@qca.qualcomm.com>
D Harilakshmi <kmudda@codeaurora.org>
Dhaval Patel <pdhaval@codeaurora.org>
Diab Neiroukh <lazerl0rd@thezest.dev>
dianlujitao <dianlujitao@lineageos.org>
Diep Quynh <remilia.1505@gmail.com>
Dieter Luecking <dieterl@codeaurora.org>
Dietmar Eggemann <dietmar.eggemann@arm.com>
Disha Das <dishad@codeaurora.org>
Dominik Brodowski <linux@dominikbrodowski.net>
donglian <dongliang.yao@codeaurora.org>
Doug Berger <opendmb@gmail.com>
dpyun <dpyun@codeaurora.org>
Dundi Raviteja <dundi@codeaurora.org>
Dustin Brown <dustinb@codeaurora.org>
Dyneteve <dyneteve@pixelexperience.org>
Edayilliam Jayadev <ejayadev@codeaurora.org>
Edhar, Mahesh Kumar <c_medhar@qti.qualcomm.com>
Edhar, Mahesh Kumar <MAHESH@codeaurora.org>
el3xyz <el3xyz@protonmail.com>
Elena Reshetova <elena.reshetova@intel.com>
Erfan Abdi <erfangplus@gmail.com>
Eric Biggers <ebiggers@google.com>
Eric Dumazet <edumazet@google.com>
Eric Sandeen <sandeen@sandeen.net>
E V Ravi <evenka@codeaurora.org>
Faiz Nabi Kuchay <fkuchay@codeaurora.org>
Fangrui Song <maskray@google.com>
Florian Pfister <fpfister@codeaurora.org>
Forenche <prahul2003@gmail.com>
Frank Liu <qiliu@codeaurora.org>
Frank Werner-Krippendorf <mail@hb9fxq.ch>
Ganesh Kondabattini <ganeshk@codeaurora.org>
Ganesh Kondabattini <ganeshk@qti.qualcomm.com>
gaolez <gaolez@codeaurora.org>
Gao Xiang <gaoxiang25@huawei.com>
Gao Xiang <hsiangkao@redhat.com>
Garmond Leung <garmondl@codeaurora.org>
gaurank kathpalia <gkathpal@codeaurora.org>
Gaurank Kathpalia <gkathpal@codeaurora.org>
Gaurav Jindal <gjindal@codeaurora.org>
gbian <gbian@codeaurora.org>
Geert Uytterhoeven <geert@linux-m68k.org>
Geert Uytterhoeven <geert+renesas@glider.be>
Gerrit - the friendly Code Review server <code-review@localhost>
Git User <gituser@localhost>
glider@google.com <glider@google.com>
Govind Singh <govinds@codeaurora.org>
Govind Singh <govinds@qti.qualcomm.com>
Gowri, Deepthi <deepthi@codeaurora.org>
Greg Kroah-Hartman <gregkh@google.com>
Greg Kroah-Hartman <gregkh@linuxfoundation.org>
guangde <guangde@codeaurora.org>
Guisen Yang <guiseny@codeaurora.org>
Guolei Bian <gbian@codeaurora.org>
Guo Xuenan <guoxuenan@huawei.com>
Gupta, Kapil <kapgupta@codeaurora.org>
Gupta, Kapil <kapgupta@qti.qualcomm.com>
Gurumoorthi Gnanasambandhan <gguru@codeaurora.org>
Gururaj Pandurangi <panduran@codeaurora.org>
Gustavo A. R. Silva <gustavoars@kernel.org>
Gustavo A. R. Silva <gustavo@embeddedor.com>
Gyanranjan Hazarika <gyanranj@codeaurora.org>
Hang Lu <hangl@codeaurora.org>
hangtian <hangtian@codeaurora.org>
Hangtian Zhu <hangtian@codeaurora.org>
Hanumantha Reddy Pothula <c_hpothu@codeaurora.org>
Hanumantha Reddy Pothula <c_hpothu@qti.qualcomm.com>
Hanumanth Reddy Pothula <c_hpothu@codeaurora.org>
Hanumanth Reddy Pothula <c_hpothu@qti.qualcomm.com>
Hardik Kantilal Patel <hkpatel@codeaurora.org>
Hariharan Basuthkar <hbasuthk@codeaurora.org>
Harilakshmi Deshkumar <hdeshk@codeaurora.org>
Hari Veerubhotla <vsubrahm@codeaurora.org>
Harprit Chhabada <harpritchhabada@codeaurora.org>
Harshal Ahire <hahire@codeaurora.org>
Haynes Mathew George <hgeorge@codeaurora.org>
Hema Aparna Medicharla <haparna@qti.qualcomm.com>
Hemant Kumar <hemantk@codeaurora.org>
Himanshu Agarwal <himanaga@codeaurora.org>
Himanshu Agarwal <himanaga@qti.qualcomm.com>
Himanshu Batra <hbatra@codeaurora.org>
Hong Shi <hongsh@codeaurora.org>
Houston Hoffman <hhoffman@codeaurora.org>
Houston Hoffman <hhoffman@qca.qualcomm.com>
hqu <hqu@codeaurora.org>
Hsiu-Chang Chen <hsiuchangchen@google.com>
Hugo Lefeuvre <hle@owl.eu.com>
Hu Wang <huw@codeaurora.org>
Hyeonggon Yoo <42.hyeyoo@gmail.com>
hyeongseok.kim <hyeongseok@gmail.com>
Hyeongseok Kim <hyeongseok@gmail.com>
Hyeongseok.Kim <Hyeongseok@gmail.com>
Hyunchul Lee <hyc.lee@gmail.com>
idkwhoiam322 <idkwhoiam322@raphielgang.org>
Ilie Halip <ilie.halip@gmail.com>
Ilya Ponetayev <i.ponetaev@ndmsystems.com>
Ingo Molnar <mingo@elte.hu>
Isaac J. Manjarres <isaacm@codeaurora.org>
Ishank Jain <ijain@codeaurora.org>
Ivan Vecera <ivan@cera.cz>
Jackie Liu <liuyun01@kylinos.cn>
Jaegeuk Kim <jaegeuk@google.com>
Jaewon Kim <jaewon31.kim@samsung.com>
Jagadeesh Ponduru <jponduru@codeaurora.org>
Jakub Kicinski <jakub.kicinski@netronome.com>
James Tucker <jftucker@gmail.com>
Jan Beulich <JBeulich@suse.com>
Jan Kara <jack@suse.cz>
Jann Horn <jannh@google.com>
Jann Horn <jann@thejh.net>
Jan Stancek <jstancek@redhat.com>
Jason A. Donenfeld <Jason@zx2c4.com>
Jason Low <jason.low2@hp.com>
Jason Yan <yanaijie@huawei.com>
J. Avila <elavila@google.com>
Jayachandran S <jsreekum@codeaurora.org>
Jayachandran Sreekumaran <jsreekum@codeaurora.org>
Jebaitedneko <16777012+Jebaitedneko@users.noreply.github.com>
Jeevan Kukkalli <jeevank@codeaurora.org>
Jeffin Mammen <jmammen@codeaurora.org>
Jeff Johnson <jjohnson@codeaurora.org>
Jeff Johnson <jjohnson@qca.qualcomm.com>
Jenhao Chen <jenhaochen@google.com>
Jens Axboe <axboe@kernel.dk>
Jerin Jacob <jerinj@marvell.com>
Jesse Chan <jc@linux.com>
Jeya R <jeyr@codeaurora.org>
jge <jge@codeaurora.org>
Jiachao Wu <jiacwu@codeaurora.org>
Jia Ding <jiad@codeaurora.org>
jiad <jiad@codeaurora.org>
Jiani Liu <jianil@codeaurora.org>
jianmin <jianminz@codeaurora.org>
Jianmin Zhu <jianminz@codeaurora.org>
Jimmy Hu <hhhuuu@google.com>
Jingxiang Ge <jge@codeaurora.org>
jinweic chen <jinweic@codeaurora.org>
Jinwei Chen <jinweic@codeaurora.org>
Jiri Slaby <jslaby@suse.cz>
Jishnu Prakash <jprakash@codeaurora.org>
jitiphil <jitiphil@codeaurora.org>
JJ Lee <leejj@google.com>
Joe Holden <jwh@zorins.us>
Joel Fernandes (Google) <joel@joelfernandes.org>
Joe Perches <joe@perches.com>
Johannes Berg <johannes.berg@intel.com>
Johannes Weiner <hannes@cmpxchg.org>
John Dias <joaodias@google.com>
Jonathan Avila <avilaj@codeaurora.org>
Jonathan Neuschäfer <j.neuschaefer@gmx.net>
Jonglin Lee <jonglin@google.com>
Jörg Thalheim <joerg@higgsboson.tk>
Josh Kirsch <jkirsch@codeaurora.org>
Josh Poimboeuf <jpoimboe@redhat.com>
Josh Soref <jsoref@gmail.com>
jsreekum <jsreekum@codeaurora.org>
Juhyung Park <qkrwngud825@gmail.com>
Julian Liu <wlootlxt123@gmail.com>
Julien Thierry <julien.thierry@arm.com>
Jun Wang <junwan@codeaurora.org>
Jürg Billeter <j@bitron.ch>
Juri Lelli <juri.lelli@redhat.com>
Justin Tee <justint@codeaurora.org>
Jyoti Kumari <jyotkuma@codeaurora.org>
Jyoti Kumari <quic_jyotkuma@quicinc.com>
Kabilan Kannan <kabilank@codeaurora.org>
Kabilan Kannan <kabilank@qca.qualcomm.com>
Kai Chen <kaichen@codeaurora.org>
Kai Liu <kaliu@codeaurora.org>
kaliu <kaliu@qti.qualcomm.com>
Kalyan Muddala <kmudda@codeaurora.org>
Kalyan Tallapragada <ktallapr@codeaurora.org>
Kamal Agrawal <kamaagra@codeaurora.org>
Kanchanapally, Vidyullatha <vkanchan@qti.qualcomm.com>
Kapil Gupta <kapgupta@codeaurora.org>
Kapil Gupta <kapgupta@qti.qualcomm.com>
Karthick S <skarthic@qti.qualcomm.com>
Karthikeyan Mani <kmani@codeaurora.org>
Karthik Kantamneni <vkantamn@codeaurora.org>
Karunakar Dasineni <karuna@codeaurora.org>
karuna <karuna@codeaurora.org>
Kaushik, Sushant <skaushik@codeaurora.org>
Kaustubh Pandey <kapandey@codeaurora.org>
Kazuki Hashimoto <kazukih@tuta.io>
kdrag0n <dragon@khronodragon.com>
Kees Cook <keescook@chromium.org>
Ke Huang <keh@codeaurora.org>
Keshav Singh <kmudda@codeaurora.org>
Kevin Brodsky <kevin.brodsky@arm.com>
Keyur Parekh <kparekh@codeaurora.org>
Khusika Dhamar Gusti <khusikadhamar@gmail.com>
Kiran Gunda <kgunda@codeaurora.org>
Kiran Kumar Lokere <klokere@codeaurora.org>
Kiran Kumar Lokere <klokere@qca.qualcomm.com>
Kiran Venkatappa <kiranv@codeaurora.org>
Kirill Tkhai <ktkhai@virtuozzo.com>
Komal Seelam <kseelam@codeaurora.org>
Komal Seelam <kseelam@qti.qualcomm.com>
Konamki, Sreelakshmi <c_skonam@qti.qualcomm.com>
Kondabattini, Ganesh <ganeshk@codeaurora.org>
Krishna Kumaar Natarajan <kknatara@codeaurora.org>
Krishna Kumaar Natarajan <kknatara@qca.qualcomm.com>
Krishna Manikandan <mkrishn@codeaurora.org>
Krishna Rao <kcrao@codeaurora.org>
Krishna Reddy <reddyk@codeaurora.org>
Kris Muthusamy <kmuthusa@codeaurora.org>
Kristof Petho <kristof.petho@gmail.com>
Krunal Soni <ksoni@codeaurora.org>
Krunal Soni <ksoni@qca.qualcomm.com>
Kuba Wojciechowski <nullbytepl@gmail.com>
Kumar Kathirvel <kkathirv@codeaurora.org>
Kunlei Zhang <kunleiz@codeaurora.org>
kunleiz <kunleiz@codeaurora.org>
Kyle Lin <kylelin@google.com>
Lakshit Tyagi <ltyagi@codeaurora.org>
Lakshman Chaluvaraju <lchalu@codeaurora.org>
Lance Roy <ldr709@gmail.com>
Laura Abbott <labbott@redhat.com>
Laxminath Kasam <lkasam@codeaurora.org>
Leo Chang <leochang@codeaurora.org>
Leo Chang <schang@qca.qualcomm.com>
Leo Liou <leoliou@google.com>
Liangwei Dong <liangwei@codeaurora.org>
Liangwei Dong <liangwei@qti.qualcomm.com>
LibXZR <xzr467706992@163.com>
lifeng <lifeng@codeaurora.org>
Li Feng <lifeng@codeaurora.org>
Lihua Liu <lihual@codeaurora.org>
lihual <lihual@codeaurora.org>
Li Li <dualli@google.com>
Lin Bai <lbai@codeaurora.org>
Lincoln Tran <linctran@codeaurora.org>
Lingutla Chandrasekhar <clingutla@codeaurora.org>
Linus Torvalds <torvalds@linux-foundation.org>
Linux Build Service Account <lnxbuild@localhost>
Linux Build Service Account <lnxbuild@quicinc.com>
lixiang <lixiang@codeaurora.org>
Lucas Stach <l.stach@pengutronix.de>
Luca Stefani <luca.stefani.ge1@gmail.com>
lucaswei <lucaswei@google.com>
Luis Ressel <aranea@aixah.de>
LuK1337 <priv.luk@gmail.com>
L.W.Reek <syphyr@gmail.com>
lybxlpsv <lybxlpsv@yahoo.com>
Maarten Lankhorst <maarten.lankhorst@linux.intel.com>
Madan Koyyalamudi <mkoyya@codeaurora.org>
Madhvapathi Sriram <msriram@codeaurora.org>
Mahesh A Saptasagar <msapta@codeaurora.org>
Mahesh Kumar Kalikot Veetil <mkalikot@codeaurora.org>
Mahesh Kumar Kalikot Veetil <mkalikot@qca.qualcomm.com>
Mainak Sen <smainak@codeaurora.org>
Manaf Meethalavalappu Pallikunhi <manafm@codeaurora.org>
Mangesh Kunchamwar <mangeshk@codeaurora.org>
Manikandan Mohan <manikand@codeaurora.org>
Manikandan Mohan <manikand@qca.qualcomm.com>
Manikanta Pubbisetty <mpubbise@codeaurora.org>
Manisha Agarwal <maniagar@codeaurora.org>
Manish Chaturvedi <mchaturv@codeaurora.org>
Manishekar Chandrasekaran <cmshekar@codeaurora.org>
Manjeet Singh <manjee@codeaurora.org>
Manjunathappa Prakash <prakashpm@codeaurora.org>
Manjunathappa Prakash <prakashp@qca.qualcomm.com>
Manoj Ekbote <mekbote@codeaurora.org>
Marco Ballesio <balejs@google.com>
Marco Elver <elver@google.com>
Marco Zhang <zhangx@codeaurora.org>
Maria Yu <aiquny@codeaurora.org>
Mark Brown <broonie@kernel.org>
Mark Salyzyn <salyzyn@google.com>
Martijn Coenen <maco@android.com>
Martin Liu <liumartin@google.com>
Masahiro Yamada <yamada.masahiro@socionext.com>
Ma Shimiao <mashimiao.fnst@cn.fujitsu.com>
Masti, Narayanraddi <c_nmasti@qti.qualcomm.com>
Masti, Narayanraddi <nmasti@codeaurora.org>
Mathias Krause <minipli@googlemail.com>
Mathias Krause <minipli@grsecurity.net>
Matthew Wilcox <willy@infradead.org>
Matt Roper <matthew.d.roper@intel.com>
Maulik Shah <mkshah@codeaurora.org>
Mayank Rana <mrana@codeaurora.org>
Md Mansoor Ahmed <mansoor@codeaurora.org>
Mel Gorman <mgorman@techsingularity.net>
Meng Wang <mengw@codeaurora.org>
Meng Wang <mwang@codeaurora.org>
Michael Adisumarta <madisuma@codeaurora.org>
Miguel de Dios <migueldedios@google.com>
Miguel Ojeda <miguel.ojeda.sandonis@gmail.com>
Mikk Mar <mikkmar@airmail.cc>
Milap Gajjar <migajjar@codeaurora.org>
Mimi Wu <mimiwu@google.com>
Minchan Kim <minchan@google.com>
Min Liu <minliu@codeaurora.org>
Mohammed Javid <mjavid@codeaurora.org>
Mohammed <mjavid@codeaurora.org>
Mohammed Nayeem Ur Rahman <mohara@codeaurora.org>
Mohammed Siddiq <msiddiq@codeaurora.org>
Mohit Khanna <mkhanna@codeaurora.org>
Mohit Khanna <mkhannaqca@codeaurora.org>
Mohit Khanna <mkhanna@qca.qualcomm.com>
Mohit Sharma <smohit@codeaurora.org>
Mukul Sharma <mukul@codeaurora.org>
mukul sharma <mukul@qti.qualcomm.com>
Mukul Sharma <mukul@qti.qualcomm.com>
Muralidharan M <murm@codeaurora.org>
Nachiket Kukade <nkukade@codeaurora.org>
Nadav Amit <namit@vmware.com>
Naga <nbethala@codeaurora.org>
nakul kachhwaha <nkachhwa@codeaurora.org>
Nalla Kartheek <karthe@codeaurora.org>
Naman Padhiar <npadhiar@codeaurora.org>
Namjae Jeon <namjae.jeon@samsung.com>
Nandha Kishore Easwaran <nandhaki@codeaurora.org>
Nandini Suresh <snandini@codeaurora.org>
narayan <nsubramh@codeaurora.org>
Nathan Chancellor <natechancellor@gmail.com>
Nathan Chancellor <nathan@kernel.org>
Naveen Rawat <naveenrawat@codeaurora.org>
Naveen Rawat <nrawat@codeaurora.org>
Naveen Rawat <nrawat@qca.qualcomm.com>
Neeraj Soni <neersoni@codeaurora.org>
Neeraj Upadhyay <neeraju@codeaurora.org>
Neha Bisht <nbisht21@codeaurora.org>
NeilBrown <neilb@suse.com>
Neil Zhao <nwzhao@codeaurora.org>
Nicholas Piggin <npiggin@gmail.com>
Nick C <ctwoon@suicide.today>
Nick Desaulniers <ndesaulniers@google.com>
Nijun Gong <ngong@codeaurora.org>
Nirav Shah <nnshah@codeaurora.org>
Nirav Shah <nnshah@qti.qualcomm.com>
Nisha Menon <nmenon@codeaurora.org>
Nishank Aggarwal <naggar@codeaurora.org>
Nitesh Shah <niteshs@codeaurora.org>
Nitesh Shrivastav <nshrivas@codeaurora.org>
Nitin Rawat <nitirawa@codeaurora.org>
nixiaoming <nixiaoming@huawei.com>
nobelj <nobelj@codeaurora.org>
Noralf Trønnes <noralf@tronnes.org>
Norbert Lange <nolange79@gmail.com>
nshrivas <nshrivas@codeaurora.org>
nwzhao <nwzhao@codeaurora.org>
Oleg Matcovschi <omatcovschi@google.com>
Oleg Nesterov <oleg@redhat.com>
Om Prakash Tripathi <otripath@codeaurora.org>
Orhan K AKYILDIZ <oka@codeaurora.org>
Orhan K AKYILDIZ <oka@qca.qualcomm.com>
Padma Raghunathan <padmar@codeaurora.org>
Padma, Santhosh Kumar <skpadma@codeaurora.org>
Pali Rohár <pali@kernel.org>
Pallavi <pallavim@codeaurora.org>
Pamidipati, Vijay <vpamidip@codeaurora.org>
Panchajanya1999 <panchajanya@azure-dev.live>
Pankaj Singh <pansin@codeaurora.org>
Paras Nagda <pnagda@codeaurora.org>
Park Ju Hyung <qkrwngud825@gmail.com>
Patrick Bellasi <patrick.bellasi@arm.com>
Patrick Daly <pdaly@codeaurora.org>
Patrick Tjin <pattjin@google.com>
Paul E. McKenney <paulmck@kernel.org>
Paul E. McKenney <paulmck@linux.vnet.ibm.com>
Paul Kocialkowski <contact@paulk.fr>
Paul Lawrence <paullawrence@google.com>
Paul Zhang <paulz@codeaurora.org>
Pavankumar Kondeti <pkondeti@codeaurora.org>
Pavankumar Nandeshwar <pnandesh@codeaurora.org>
Pavel Tatashin <pasha.tatashin@soleen.com>
Peng Xu <pxu@codeaurora.org>
Peng Xu <pxu@qca.qualcomm.com>
Peter Collingbourne <pcc@google.com>
Peter Georg <peter.georg@physik.uni-regensburg.de>
Peter Zijlstra <a.p.zijlstra@chello.nl>
Peter Zijlstra (Intel) <peterz@infradead.org>
Peter Zijlstra <peterz@infradead.org>
Peter Ziljstra <peterz@infradead.org>
Petri Gynther <pgynther@google.com>
phadiman <phadiman@codeaurora.org>
Phani Kumar Uppalapati <phaniu@codeaurora.org>
Philip Cuadra <philipcuadra@google.com>
Poddar, Siddarth <siddpodd@codeaurora.org>
Poddar, Siddarth <siddpodd@qti.qualcomm.com>
Pooventhiran G <pooventh@codeaurora.org>
Prabha Pandey <prabha@codeaurora.org>
Pradeep Reddy POTTETI <c_ppotte@qti.qualcomm.com>
Pradeep Reddy POTTETI <ppotte@codeaurora.org>
Pradhan, Abhijit <abhijit@codeaurora.org>
Pradosh Das <prados@codeaurora.org>
Pragaspathi Thilagaraj <tpragasp@codeaurora.org>
Prakash Dhavali <pdhavali@codeaurora.org>
Prakash Dhavali <pdhavali@qca.qualcomm.com>
Prakash Manjunathappa <prakashpm@codeaurora.org>
Pramod Simha <psimha@codeaurora.org>
Pranita Solanke <psolanke@codeaurora.org>
Prasad Kumpatla <nkumpat@codeaurora.org>
Prashant Bhole <bhole_prashant_q7@lab.ntt.co.jp>
Prashanth Bhatta <bhattap@codeaurora.org>
Prashanth Bhatta <bhattap@qca.qualcomm.com>
Prateek Patil <pratpati@codeaurora.org>
Pratham Pratap <prathampratap@codeaurora.org>
Prathyusha Guduri <gprathyu@codeaurora.org>
Pratik Gandhi <prgandhi@codeaurora.org>
Preetam Singh Ranawat <apranawat@codeaurora.org>
Priyadarshnee S <priys@codeaurora.org>
Prudhvi Yarlagadda <pyarlaga@codeaurora.org>
psimha <psimha@codeaurora.org>
Puja Gupta <pujag@codeaurora.org>
qcabuildsw <qcabuildsw@localhost>
qctecmdr <qctecmdr@localhost>
qctecmdr Service <qctecmdr@qualcomm.com>
Qian Cai <cai@lca.pw>
Qiwei Cai <qcai@codeaurora.org>
Quentin Perret <quentin.perret@arm.com>
Qun Zhang <qunz@codeaurora.org>
Rachit Kankane <rkankane@codeaurora.org>
Radha krishna Simha Jiguru <rjiguru@codeaurora.org>
Radha Krishna Simha Jiguru <rjiguru@codeaurora.org>
Radhika Sriram <radhsrir@codeaurora.org>
Rafael J. Wysocki <rafael.j.wysocki@intel.com>
Raghavendar rao l <rlomte@codeaurora.org>
Rajasekaran Kalidoss <rkalidos@codeaurora.org>
Rajeev Kumar <rajekuma@codeaurora.org>
Rajeev Kumar <rajekuma@qca.qualcomm.com>
Rajeev Kumar Sirasanagandla <rsirasan@codeaurora.org>
Rajesh Chauhan <rajeshc@codeaurora.org>
Rajiv Ranjan <rrajiv@codeaurora.org>
Rakesh Pillai <pillair@codeaurora.org>
Rakesh Sunki <rsunki@codeaurora.org>
Rakesh Sunki <rsunki@qca.qualcomm.com>
Rakib Mullick <rakib.mullick@gmail.com>
Rakshith Suresh Patkar <rpatkar@codeaurora.org>
Ralf Herz <rherz@codeaurora.org>
Ramii Ahmed <ramy@ahmedramy.com>
Ramlal Karra <rkarra@codeaurora.org>
Ram Prakash Gupta <rampraka@codeaurora.org>
Ramprasad Katkam <katkam@codeaurora.org>
Ramu Gottipati <ramug@codeaurora.org>
Randall Huang <huangrandall@google.com>
Randy Dunlap <rdunlap@infradead.org>
Rapherion Rollerscaperers <rapherion@raphielgang.org>
Rathees kumar Chinannan <rrchinan@codeaurora.org>
Ratnam Rachuri <c_rrachu@qti.qualcomm.com>
Ratnam Rachuri <rrachu@codeaurora.org>
Ravi Joshi <ravij@codeaurora.org>
Ravi Joshi <ravij@qca.qualcomm.com>
Ravi Kumar Bokka <brkum@codeaurora.org>
Ray Chi <raychi@google.com>
razorloves <razorloves@gmail.com>
René van Dorst <opensource@vdorst.com>
Revathi Uddaraju <revathiu@codeaurora.org>
Rhythm Patwa <rpatwa@codeaurora.org>
Ricardo Mendoza <ricmm@pantacor.com>
Rick Yiu <rickyiu@google.com>
Ritesh Kumar <riteshk@codeaurora.org>
Rob Herring <robh@kernel.org>
Robin Murphy <robin.murphy@arm.com>
Roderick Colenbrander <roderick.colenbrander@sony.com>
Rohan Dutta <drohan@codeaurora.org>
Rohit kumar <rohitkr@codeaurora.org>
Rohit Kumar <rohitkr@codeaurora.org>
Roman Gushchin <guro@fb.com>
Romed Schur <rschur@codeaurora.org>
Ronak Vijay Raheja <rraheja@codeaurora.org>
Rongjing Liao <liaor@codeaurora.org>
Ruben Columbus <rcolumbu@codeaurora.org>
ruchi agrawal <ruchagra@codeaurora.org>
Ruchi, Agrawal <ruchagra@codeaurora.org>
Ryan Hsu <ryanhsu@codeaurora.org>
Ryan Hsu <ryanhsu@qca.qualcomm.com>
Sachin Ahuja <sahuja@codeaurora.org>
Sachin Ahuja <sahuja@qti.qualcomm.com>
Sachin Mohan Gadag <sgadag@codeaurora.org>
SaidiReddy Yenuga <manjee@codeaurora.org>
SaidiReddy Yenuga <saidir@codeaurora.org>
Sai Harshini Nimmala <snimmala@codeaurora.org>
Saket Jha <sakejha@codeaurora.org>
Salendarsingh Gaud <sgaud@codeaurora.org>
Salvatore Mesoraca <s.mesoraca16@gmail.com>
Sameer Thalappil <sameert@codeaurora.org>
Sami Tolvanen <samitolvanen@google.com>
Samuel Ahn <sahn@codeaurora.org>
Samuel Ahn <sahn@qca.qualcomm.com>
Samuel Ahn <sahn@qti.qualcomm.com>
Samuel Holland <samuel@sholland.org>
Samuel Neves <sneves@dei.uc.pt>
Samyak Jain <samyjain@codeaurora.org>
sandeep puligilla <spuligil@codeaurora.org>
Sandeep puligilla <spuligil@codeaurora.org>
Sandeep Puligilla <spuligil@codeaurora.org>
Sandeep Puligilla <spuligil@qca.qualcomm.com>
Sandeep Singh <sandsing@codeaurora.org>
Sandhya Mahadevan <smahade@codeaurora.org>
Sanjay Devnani <sdevnani@qca.qualcomm.com>
Santosh Anbu <sanbu@codeaurora.org>
Sarada Prasanna Garnayak <sgarna@codeaurora.org>
Saravana Kannan <saravanak@google.com>
Sathish Kumar <ksathis@codeaurora.org>
Sathyanarayanan Esakkiappan <sesakkia@codeaurora.org>
Sathyanarayanan <padmar@codeaurora.org>
Satish Singh <c_ssing@qca.qualcomm.com>
Satish Singh <ssing@codeaurora.org>
Satsih Singh <ssing@codeaurora.org>
Satya Durga Srinivasu Prabhala <satyap@codeaurora.org>
Satya Krishna Pindiproli <satyak@codeaurora.org>
Saurav Kumar <sauravk@codeaurora.org>
Sean Tranchetti <stranche@codeaurora.org>
Sebastian Andrzej Siewior <bigeasy@linutronix.de>
Selvaraj, Sridhar <sselvara@codeaurora.org>
Sen, Devendra <dsen@codeaurora.org>
Sergey Ivanov <seriv@cs.umd.edu>
Service qcabuildsw <qcabuildsw@localhost>
Shaakir Mohamed <smohamed@codeaurora.org>
Shaikh Shadul <sshadu@codeaurora.org>
Shakeel Butt <shakeelb@google.com>
Shaleen Agrawal <shalagra@codeaurora.org>
Shalini Manjunatha <shalma@codeaurora.org>
Shaokun Zhang <zhangshaokun@hisilicon.com>
Sharad Sangle <assangle@codeaurora.org>
Sharath Chandra Vurukala <sharathv@codeaurora.org>
Shashikala Prabhu <pshashik@codeaurora.org>
Shashi Kant Maurya <smaury@codeaurora.org>
Shaun Kelsey <shaunkelsey@google.com>
sheenam monga <quic_shemonga@quicinc.com>
sheenam monga <shebala@codeaurora.org>
Shiva Krishna Pittala <spittala@codeaurora.org>
Shivani Soni <soni@codeaurora.org>
Shiva Sankar Gajula <sgajula@codeaurora.org>
Shiv Maliyappanahalli <smaliyap@codeaurora.org>
Shravya Samala <shravyas@codeaurora.org>
Shreedhar Parande <sparande@codeaurora.org>
Shwetha G K <skempa@codeaurora.org>
Siddarth Poddar <siddpodd@codeaurora.org>
Siddeswar Aluganti <salugant@codeaurora.org>
Siena Richard <sienar@codeaurora.org>
Sivakanth Vaka <svaka@codeaurora.org>
Sivakumar Vaddi <c_svadd@qti.qualcomm.com>
Sivasri Kumar Vanka <sivasri@codeaurora.org>
skylar chang <chiaweic@codeaurora.org>
Skylar Chang <chiaweic@codeaurora.org>
Smita Ghosh <smitag@codeaurora.org>
snandini <snandini@codeaurora.org>
Sneh Shah <snehshah@codeaurora.org>
sokchetra eung <eung@codeaurora.org>
Soumya Bhat <soumyab@codeaurora.org>
Soumya Managoli <smanag@codeaurora.org>
Sourav Mohapatra <mohapatr@codeaurora.org>
spuligil <spuligil@codeaurora.org>
Sravan Goud <sgoud@codeaurora.org>
Sravan Kumar Kairam <sgoud@codeaurora.org>
Sreelakshmi Konamki <c_skonam@qti.qualcomm.com>
Sreelakshmi Konamki <skonam@codeaurora.org>
Sridhar Selvaraj <sselvara@codeaurora.org>
Srikanth Marepalli <marepall@codeaurora.org>
Srikanth Marepalli <srimarep@codeaurora.org>
srikanthreddy ponogoti <sponogot@codeaurora.org>
Srikar Dronamraju <srikar@linux.vnet.ibm.com>
Srinivas Dasari <dasaris@codeaurora.org>
Srinivas Dasari <dasaris@qti.qualcomm.com>
Srinivas Girigowda <sgirigow@codeaurora.org>
Srinivas Girigowda <sgirigow@qca.qualcomm.com>
Srinivas Pitla <spitla@codeaurora.org>
Sriram Madhvapathi <msriram@codeaurora.org>
Stanley Chu <stanley.chu@mediatek.com>
Stephan Raj Ignatious Durairaj <signat@codeaurora.org>
Stephen Boyd <sboyd@codeaurora.org>
Stephen Boyd <swboyd@chromium.org>
Steve Muckle <smuckle@google.com>
Steven Rostedt (VMware) <rostedt@goodmis.org>
stonez <stonez@codeaurora.org>
Subash Abhinov Kasiviswanathan <subashab@codeaurora.org>
Subhajeet Muhuri <subhajeet.muhuri@gmail.com>
Subhani Shaik <subhanis@codeaurora.org>
Subhash Madyastha <spandesh@codeaurora.org>
Subhranil Choudhury <subhrani@codeaurora.org>
Subrat Dash <sdash@codeaurora.org>
Subrat Mishra <subratm@codeaurora.org>
Sudarshan Rajagopalan <sudaraja@codeaurora.org>
Sudheer Papothi <spapothi@codeaurora.org>
Sujin Panicker <spanic@codeaurora.org>
Sultan Alsawaf <sultan@kerneltoast.com>
Sultan Alsawaf <sultanxda@gmail.com>
sumedh baikady <sbaikady@codeaurora.org>
Sumedh Baikady <sbaikady@codeaurora.org>
Sumeet Rao <sumeetr@codeaurora.org>
Sungjong Seo <sj1557.seo@samsung.com>
Sunil Kumar Paidimarri <hisunil@codeaurora.org>
sunil paidimarri <hisunil@codeaurora.org>
Sunil Paidimarri <hisunil@codeaurora.org>
Surabhi Vishnoi <svishnoi@codeaurora.org>
Suraj Jaiswal <jsuraj@codeaurora.org>
Suren Baghdasaryan <surenb@google.com>
Surendar Karka <skarka@codeaurora.org>
Suresh Nandini <snandini@codeaurora.org>
Surya Prakash Raajen <sraajen@codeaurora.org>
Surya Prakash Sivaraj <suryapra@codeaurora.org>
Surya Prakash <sraajen@codeaurora.org>
Sushant Kaushik <skaushik@qti.qualcomm.com>
Swathi K <kataka@codeaurora.org>
Swathi Sridhar <swatsrid@codeaurora.org>
Swetha Chikkaboraiah <schikk@codeaurora.org>
syed touqeer pasha <spasha@codeaurora.org>
Szymon Lukasz <noh4hss@gmail.com>
Takashi Iwai <tiwai@suse.de>
Tallapragada Kalyan <ktallapr@codeaurora.org>
Tallapragada <ktallapr@codeaurora.org>
Tang Yingying <yintang@codeaurora.org>
Tanya Dixit <tdixit@codeaurora.org>
tbalden <illespal@gmail.com>
Tejun Heo <tj@kernel.org>
Tetsuhiro Kohada <kohada.t2@gmail.com>
Tetsuhiro Kohada <kohada.tetsuhiro@dc.mitsubishielectric.co.jp>
Tetsuhiro Kohada <Kohada.Tetsuhiro@dc.MitsubishiElectric.co.jp>
TeYuan Wang <kamewang@google.com>
tfyu <tfyu@codeaurora.org>
Thadeu Lima de Souza Cascardo <cascardo@canonical.com>
Thierry Strudel <tstrudel@google.com>
Thomas Backlund <tmb@mageia.org>
Thomas Gleixner <tglx@linutronix.de>
Thomas Gschwantner <tharre3@gmail.com>
Thomas Hellstrom <thellstrom@vmware.com>
Thotakura Srinivas <c_tsrini@qti.qualcomm.com>
Tiger Yu <tfyu@codeaurora.org>
Tim Murray <timmurray@google.com>
Tingting Lin <tinlin@codeaurora.org>
tinlin <tinlin@codeaurora.org>
Todd Kjos <tkjos@google.com>
Toke Høiland-Jørgensen <toke@redhat.com>
Trinath Thammishetty <tthamish@codeaurora.org>
Tushnim Bhattacharyya <tushnimb@codeaurora.org>
Tushnim Bhattacharyya <tushnimb@qca.qualcomm.com>
Tycho Andersen <tycho@tycho.ws>
Tyler Nijmeh <tylernij@gmail.com>
Uma Mehta <umamehta@codeaurora.org>
Uraj Sasan <usasan@codeaurora.org>
URAJ SASAN <usasan@codeaurora.org>
Utkarsh Bhatnagar <ubhatnag@codeaurora.org>
UtsavBalar1231 <utsavbalar1231@gmail.com>
Vaisakh Murali <mvaisakh@statixos.com>
Vaishnavi Kommaraju <vkommara@codeaurora.org>
Valdis Kletnieks <valdis.kletnieks@vt.edu>
Varsha Mishra <varsham@codeaurora.org>
Varuneshwar Petlozu <vpetlozu@codeaurora.org>
Varun Reddy Yeturu <varunreddy.yeturu@codeaurora.org>
Varun Reddy Yeturu <vyeturu@qca.qualcomm.com>
Vasantha Balla <vballa@codeaurora.org>
Vasily Averin <vvs@virtuozzo.com>
Vatsal Bucha <vbucha@codeaurora.org>
Veerabhadrarao Badiganti <vbadigan@codeaurora.org>
Veerendranath Jakkam <vjakkam@codeaurora.org>
Venkata krishna Sundararajan <vsundara@codeaurora.org>
Venkata Sharath Chandra Manchala <vmanchal@codeaurora.org>
Venkateswara Swamy Bandaru <vbandaru@codeaurora.org>
Venkat Karthik Kantamneni <vkantamn@codeaurora.org>
Vevek Venkatesan <vevekv@codeaurora.org>
Vidyakumar Athota <vathota@codeaurora.org>
Vidyullatha Kanchanapally <vidyullatha@codeaurora.org>
Vidyullatha, Kanchanapally <vidyullatha@codeaurora.org>
Vidyullatha Kanchanapally <vkanchan@qti.qualcomm.com>
Vignesh Kulothungan <vigneshk@codeaurora.org>
Vignesh Mohan <vignmoha@codeaurora.org>
Vignesh U <uvignesh@codeaurora.org>
Vignesh Viswanathan <viswanat@codeaurora.org>
Vijaya Kuamr Muniyappa <vtmuni@codeaurora.org>
Vijayakumar Badiger <vbadig@codeaurora.org>
Vijayanand Jitta <quic_vjitta@quicinc.com>
Vijay Pamidipati <vpamidip@codeaurora.org>
VIJAY RAJ <vijaraj@codeaurora.org>
Vikram Kandukuri <Vikram.Kandukuri@codeaurora.org>
Vikrampal <palv@codeaurora.org>
Vikram Panduranga <vpandura@codeaurora.org>
Vinay Adella <vadella@codeaurora.org>
Vinayak Menon <vinmenon@codeaurora.org>
Vinay Gannevaram <vganneva@codeaurora.org>
Vincent Palomares <paillon@google.com>
Viresh Kumar <viresh.kumar@linaro.org>
Vishwajith Upendra <vishwaji@codeaurora.org>
Visudha Sathurappan <vsathura@codeaurora.org>
Visweswara Tanuku <vtanuku@codeaurora.org>
Vivek Chettri <vchettri@codeaurora.org>
Vivek Natarajan <nataraja@codeaurora.org>
Vivek <vchettri@codeaurora.org>
Viyom Mittal <viyomitt@codeaurora.org>
Vlastimil Babka <vbabka@suse.cz>
Volodymyr Zhdanov <wight554@gmail.com>
vtanuku <vtanuku@codeaurora.org>
Vulupala Shashank Reddy <vulupa@codeaurora.org>
wadesong <wadesong@codeaurora.org>
Waiman Long <longman@redhat.com>
Walter Yang <yandongy@codeaurora.org>
wangdong12 <wangdong12@xiaomi.com>
Wei Song <wadesong@codeaurora.org>
Wei Wang <wvw@google.com>
Weiyin Jiang <wjiang@codeaurora.org>
Wei Yongjun <weiyongjun1@huawei.com>
Wen Gong <wgong@codeaurora.org>
Wilco Dijkstra <wdijkstr@arm.com>
Will Deacon <will.deacon@arm.com>
Will Deacon <will@kernel.org>
Willem de Bruijn <willemb@google.com>
Will Huang <wilhuang@codeaurora.org>
Will McVicker <willmcvicker@google.com>
Wilson Sung <wilsonsung@google.com>
Woody Lin <woodylin@google.com>
Wu Gao <wugao@codeaurora.org>
Wu Gao <wugao@qti.qualcomm.com>
Xianting Tian <tian.xianting@h3c.com>
Xiaojun Sang <xsang@codeaurora.org>
Xiaoyu Ye <benyxy@codeaurora.org>
xNombre <kartapolska@gmail.com>
xsang <xsang@codeaurora.org>
Xun Luo <xunl@qca.qualcomm.com>
y <amirp@codeaurora.org>
yangerkun <yangerkun@huawei.com>
Yang Shi <yang.shi@linux.alibaba.com>
Yang Shi <yang.shi@windriver.com>
Yangtao Li <tiny.windzz@gmail.com>
Yaowei Bai <baiyaowei@cmss.chinamobile.com>
Yaroslav Furman <yaro330@gmail.com>
Yeshwanth Sriram Guntuka <quic_ysriramg@quicinc.com>
yeshwanth sriram guntuka <ysriramg@codeaurora.org>
Yeshwanth Sriram Guntuka <ysriramg@codeaurora.org>
YH_Lin <yhli@google.com>
yidongh <yidongh@codeaurora.org>
YiHo Cheng <yihocheng@google.com>
Yingying Tang <yintang@codeaurora.org>
yuanl <yuanl@codeaurora.org>
Yuanyuan Liu <yuanliu@codeaurora.org>
Yuanyuan Liu <yuanliu@qca.qualcomm.com>
Yuanyuan Zhong <zyy@motorola.com>
YueHaibing <yuehaibing@huawei.com>
Yue Hu <huyue2@yulong.com>
Yue Ma <yuem@codeaurora.org>
Yue Ma <yuem@qca.qualcomm.com>
Yunfei Zhang <yunfeiz@codeaurora.org>
Yun park <yunp@codeaurora.org>
Yun Park <yunp@codeaurora.org>
Yun Park <yunp@qca.qualcomm.com>
Yu Ouyang <yuo@codeaurora.org>
Yury Norov <yury.norov@gmail.com>
Yu Tian <yutian@codeaurora.org>
Yu Wang <quic_yyuwang@quicinc.com>
Yu Wang <yyuwang@codeaurora.org>
Yu Zhang(Yuriy) <quic_yuzha@quicinc.com>
Zachariah Kennedy <zkennedy87@gmail.com>
zding <zding@codeaurora.org>
Zelong Ren <zeloren@codeaurora.org>
Zhang Qian <zhangq@codeaurora.org>
Zhaoyang Liu <zhaoyang@codeaurora.org>
Zhou Song <zhous@codeaurora.org>
Zhu Jianmin <jianminz@codeaurora.org>
Ziqi Chen <ziqichen@codeaurora.org>

Change-Id: I430517d403f6057bda3b6236b8dd5424decf0922

---
## [y2kbadbug/freebsd-ports-y2kbadbug](https://github.com/y2kbadbug/freebsd-ports-y2kbadbug)@[f526cbc7a9...](https://github.com/y2kbadbug/freebsd-ports-y2kbadbug/commit/f526cbc7a984b86870cc86dd6d92a3fde1b248a9)
#### Monday 2022-07-11 08:02:51 by Jochen Neumeister

*/wordpress*: Update to Version 6.0

Welcome to “Arturo”

Say hello to “Arturo” and WordPress 6.0, inspired by Grammy-winning jazz musician, Arturo O’Farrill. Known for his influence on contemporary Latin jazz, Arturo has pressed more than 15 albums spanning a body of work across five decades.

Take some time to explore WordPress 6.0, built to help you unlock your creative aspirations and make your site-building experience more intuitive. And check out some of Arturo’s inspirational sounds that span Afro Cuban jazz, contemporary Latin jazz, and so much more.

With nearly 1,000 enhancements and bug fixes, the second major release of 2022 is here. Download it now! As of today, WordPress powers more than 42% of websites worldwide.1

Site owners and administrators should upgrade to take full advantage of the many stability, performance, and usability enhancements today. WordPress content creators will enjoy a suite of new features geared toward improving the writing and designing experiences.

Full Changelog see: https://wordpress.org/news/2022/05/arturo/

Sponsored by:	Netzkommune GmbH

---
## [Twilight153/File](https://github.com/Twilight153/File)@[b79cd552dd...](https://github.com/Twilight153/File/commit/b79cd552dd98913dc989bc5ea0beacf78d46a904)
#### Monday 2022-07-11 08:50:06 by Twilight153

Update README.md

Storing food the wrong way means it can spoil more quickly-and eating it might literally make you sick (and no one wants food poisoning). If you were to open your refrigerator right now, would you be guilty of putting some food in the wrong place? Probably. But don't worry, we can help. It turns out, all those drawers, nooks and specialty shelves really do matter, and they can make a big difference in keeping your food safe and extending the life of your groceries. Storing your food in the right place and keeping your fridge organized means you'll spend less time digging around a messy fridge and get more bang for your grocery buck. If you keep your eggs in that cute spot on the fridge door or shove your grocery haul anywhere you can find space, keep reading for an easy organization strategy that'll keep your food fresher longer.

Don't Miss: 7-Day Budget Meal Plan and Shopping List

1. Fill the door with condiments-not eggs.
A Consumer Reports study found that the refrigerator door is the warmest part of your fridge by a few degrees. (Think about it: How often do you pop the door open for a nibble here and there?) Milk and eggs require colder temperatures, so resist the urge to store them here-even if there is a perfectly shaped compartment for each one. Instead, load up the door with items that can handle warmer temps like condiments, salad dressings and butter.

2. Raw meat belongs on the bottom.
The most valuable real estate in your fridge-i.e., the coldest shelf-should be reserved for foods that spoil the easiest, according to the University of Illinois Extension. Save this area for raw meat, poultry and seafood. Bonus: Keeping those packages here keeps the occasional leak from dripping down and contaminating other areas of the fridge. (To avoid extra cleanup, thaw raw meat on a plate.)

3. Know that coldest isn't best.
Just because you can set your refrigerator to 25 degrees doesn't mean you should. According to the FDA, 40 degrees is the optimal fridge temperature. It's warm enough to keep your food from freezing and cool enough to prevent bacteria growth. You also want plenty of room for all that cold air to flow, so avoid packing food too tightly on the shelves.

4. Leave some foods out.
To fridge or not to fridge? The answer is no for a handful of foods. For example, bananas turn brown and mushy, honey crystallizes, and potatoes and tomatoes take a texture hit. Learn the best way to store all your fruits and vegetables, including what goes in the fridge.

5. Save the middle shelf for dairy.
A Purdue University study found that temperatures don't fluctuate as much here as they do on the top shelf. This makes the middle an ideal place for foods that go bad easily like eggs, cream, yogurt and milk. The second shelf is also a prime spot for leftovers that have already been cooked. Just make sure they're stored in shallow containers (rather than a giant container) which not only saves space, but helps keep the food cold.

6. First in, first out.
One of the most important rules you can follow when storing your food is to make you obey FIFO, first in, first out. That means apples you bought on Tuesday should get buried under apples from Sunday so the older ones get grabbed first. It's a rule followed in food service kitchens and grocery stores to make sure that food that's not as fresh gets used up first. And it's much easier to apply this at home if you stock the newer food behind the older food when you bring it home.

7. Put prepared foods on the top shelf.
Heat rises, so it makes sense that this is the warmest area of your fridge's main compartment. "I store items here that need to be kept cool but not necessarily held at a specific temperature," says Lauren Manaker, M.S., R.D., a South Carolina-based registered dietitian. Reserve this space for packaged goods with preservatives that keep them from going bad quickly. Think: spreads, jarred sauces, nut butters, juice and water.

8. Use the high-humidity drawer for vegetables.
The drawers toward the bottom of your fridge are sealed by gaskets at the top to create a moisture-controlled zone. Often, you can set the humidity level. A high-humidity drawer is the best spot for leafy greens, fresh herbs, broccoli, carrots and other veggies that can easily dry out and wilt. But if you notice too much moisture building up, it's OK to leave the drawer cracked open just a little bit, or set the humidity level lower.

9. Fruits go in the low-humidity drawer.
Setting a drawer to low-humidity opens vents that let air circulate more freely among the contents and keeps moisture down. Use it to store fruits that don't need a lot of moisture to stay fresh such as apples, oranges, grapes and berries. The extra airflow also keeps fruits from ripening too quickly. Ethylene, a hormone given off by produce that can ripen surrounding fruits and veggies, won't build up in this breathable drawer.

10. Use the deli drawer for cooked meat and cheese.
Despite the preservatives, cured meats and sliced cheeses can still go bad after a few days, according to the USDA. The deli drawer is set up to receive additional cold air flow to keep foods very cold without freezing. Separating these foods from others also prevents cross-contamination in case spoilage occurs.

---
## [20kdc/OC-KittenOS](https://github.com/20kdc/OC-KittenOS)@[0f333b9c2f...](https://github.com/20kdc/OC-KittenOS/commit/0f333b9c2f12ef543095641150e44bc0a3ea3741)
#### Monday 2022-07-11 09:46:56 by 20kdc

Fuck you, Microsoft. (Minecraft MP is no longer playable as of this date without migration)

---
## [crawl/qw](https://github.com/crawl/qw)@[3750f78535...](https://github.com/crawl/qw/commit/3750f78535b9a5fd013401a1ef12a83b7d161e27)
#### Monday 2022-07-11 09:58:34 by gammafunk

feat: Improvement for mp-related handling

Detect when we'll need MP to use god powers and de-value equipment like
items with guardian spirit or Mad Mage's Maulers that tend to quickly
deplete our MP. Also don't try to use potions of magic with MP-draining
ghost moths around. I've given Mad Mage's Maulers a bonus of 200 utility
when we don't have an MP-using god, since it seems like it'd be a strong
effect. Further tuning will require some example qw games with it.

---
## [LandSandBoat/server](https://github.com/LandSandBoat/server)@[69b7bb4322...](https://github.com/LandSandBoat/server/commit/69b7bb43228902ad0fb0648d8ec9f4fabe0241a4)
#### Monday 2022-07-11 10:02:39 by NeuromancerXI

Fixes SQL Async Causes High CPU Load
Noticed very high CPU Load on an idle server instance. With the guidance
of zach2good, added a sleep condition to prevent the process from
running wild and eating CPU for breakfast, lunch, and dinner.

Co-authored-by: Zach Toogood <zrtoogood@gmail.com>

---
## [waldner/linuxkit](https://github.com/waldner/linuxkit)@[b343b8a147...](https://github.com/waldner/linuxkit/commit/b343b8a147262a2a96f05202aa00f9e23932ef5a)
#### Monday 2022-07-11 10:38:10 by Davide Brini

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
## [sunofang/Foundation-19](https://github.com/sunofang/Foundation-19)@[a54b8e5040...](https://github.com/sunofang/Foundation-19/commit/a54b8e5040aab5f12f0cd7d21a46c0603b714e73)
#### Monday 2022-07-11 12:53:52 by Bierkraan

Eta-10 sprite fix, some smaller stuff too (#144)

* balance?

* add reactor startup manual, fix sprites for lockers of all kinds

* MTF See No Evil (not being used for now), no more alien MTF

* map fix, janitor uniform

* Eta-10 helmet works!

* fixed

* SM Crystal hotfix

* Remove supermatter, for real

* No more blood sucking artifact, sprite fix for Eta-10

---
## [Comxy/tgstation](https://github.com/Comxy/tgstation)@[707fbfac7e...](https://github.com/Comxy/tgstation/commit/707fbfac7e11837865d70587011aa8197b1d0c35)
#### Monday 2022-07-11 13:26:07 by san7890

[MDB Ignore] Shifts all (sane) varedited signs to directionals  (#68004)

* [MDB Ignore] Shifts all (sane) varedited signs to directionals

Hey there,

So we have these cool new sign directionals now, but we still have all of the old pixel-shifted pre-fabrications lying around. So, I added an UpdatePaths (as well as Updated the Paths) to be a bit better at using directionals, because directionals are pretty neato.

This should update every single var_edit that used the proper 32 pixelshift (some of them used 28, and I'm unable to account for that automatically with current tooling) into a proper subtype. Mappers tend to learn by looking at well established maps, so it's always important to ensure that the well-established maps use the most recent tooling (i.e.: bring them up to the surface) and avoid needless excess lines in maps.

* The Commit With All The Maps

OH GOD OH FUCK

* Renames the UpdatePaths

---
## [omertuc/assisted-service](https://github.com/omertuc/assisted-service)@[97ad180a76...](https://github.com/omertuc/assisted-service/commit/97ad180a7610c65d42efd96e839567cb15423965)
#### Monday 2022-07-11 14:19:47 by Omer Tuchfeld

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
## [bendk/uniffi-rs](https://github.com/bendk/uniffi-rs)@[d139204827...](https://github.com/bendk/uniffi-rs/commit/d139204827632f64513320fc2843362b2986c2ca)
#### Monday 2022-07-11 14:48:37 by Ben Dean-Kawamura

Store macro metadata in the cdylib file

The nice thing about this system is that the metadata is always bundled
together with the build output.  This makes it easier to ensure that the
generated scaffolding matches up with the dylib that it's going to be link to.
This avoids the work that `rebuild_metadata()` needed to do.  Metadata
is serialized with bincode to keep the binary size reasonable.

The downside is that we need to parse a dylib, which feels slightly
risky. However, it seems less risky overall to me, since we don't have
to worry about tracking the JSON files -- especially after fixing the
recent the sccache issue.  Also, extracting the symbol data with the
goblin crate is not that bad, see `macro_metadata/extract.rs` for how
it's done.

In order to use the macro metadata, you now need to specify `--cdylib
[path-to-library]` when running `uniffi-bindgen`.  This is annoying, but it
will be simpler once the proc-macros can handle all parts of the interface.
At that point, we can make `uniffi-bindgen` accept either a UDL path or a cdylib
path as it's positional arg.

I didn't add support for external bindings to pass in a cdylib path, since
adding an argument to that function would be a breaking change, then we would
need to do another breaking change to make the param `udl_or_cdylib_file`.  If
external bindings really want to, they can call
`uniffi_bindgen::interface::macro_metadata::add_to_ci` directly.

Added the `uniffi-bindgen dump-json` command that inputs a cdylib path and
prints the matadata as JSON.

I tested that `dump-json` works properly on the following targets:
  - x86_64-unknown-linux-gnu (ELF 64-bit)
  - i686-unknown-linux-gnu (ELF 32-bit)
  - x86_64-apple-darwin (Mach-O 64-bit)
  - x86_64-pc-windows-gnu (DLL 64-bit)
  - i686-pc-windows-gnu (DLL 32-bit)

This seems like good enough coverage to me, although there are a lot of other
systems that would be nice to test on.  The limiting factor was setting up the
cross-compilation toolchains on my machine.  Maybe we should add some more CI
platforms that just run macro-metadata-related tests.

Updated the testing code to pass the cydlib path, rather than the
directory that contains it.

Added an enum that covers all Metadata types.  This is what we serialize
in the cdylib.

---
## [bevyengine/bevy](https://github.com/bevyengine/bevy)@[4847f7e3ad...](https://github.com/bevyengine/bevy/commit/4847f7e3adc835053a8907dd578c342b4bd395e2)
#### Monday 2022-07-11 15:28:52 by ira

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
## [ThakaRashard/bubblegumpop00](https://github.com/ThakaRashard/bubblegumpop00)@[d0d93b514c...](https://github.com/ThakaRashard/bubblegumpop00/commit/d0d93b514c30e3628201cbbb5d9a3aafb5813c0e)
#### Monday 2022-07-11 15:54:37 by ThakaRashard

##Perspectives on Acquaintance Rape David G. Curtis, Ph.D., B.C.E.T.S.

Perspectives on Acquaintance Rape
David G. Curtis, Ph.D., B.C.E.T.S.
Clinical Associate, Long Island Psychological Associates, P.C.


I. What is Acquaintance Rape?

Acquaintance rape, which is also referred to as "date rape" and "hidden rape," has been increasingly recognized as a real and relatively common problem within society. Much of the attention that has been focused on this issue has emerged as part of the growing willingness to acknowledge and address issues associated with domestic violence and the rights of women in general in the past three decades. Although the early and mid 1970's saw the emergence of education and mobilization to combat rape, it was not until the early 1980's that acquaintance rape began to assume a more distinct form in the public consciousness. The scholarly research done by psychologist Mary Koss and her colleagues is widely recognized as the primary impetus for raising awareness to a new level.

The publication of Koss' findings in the popular Ms. magazine in 1985 informed millions of the scope and severity of the problem. By debunking the belief that unwanted sexual advances and intercourse were not rape if they occurred with an acquaintance or while on a date, Koss compelled women to reexamine their own experiences. Many women were thus able to reframe what had happened to them as acquaintance rape and became better able to legitimize their perceptions that they were indeed victims of a crime. The results of Koss' research were the basis of the book by Robin Warshaw, first published in 1988, entitled I Never Called it Rape.

For current purposes, the term acquaintance rape will be defined as being subjected to unwanted sexual intercourse, oral sex, anal sex, or other sexual contact through the use of force or threat of force. Unsuccessful attempts are also subsumed within the term "rape." Sexual coercion is defined as unwanted sexual intercourse, or any other sexual contact subsequent to the use of menacing verbal pressure or misuse of authority (Koss, 1988).

II. Legal Perspectives on Acquaintance Rape

The electronic media have developed an infatuation with trial coverage in recent years. Among the trials which have received the most coverage have been those involving acquaintance rape. The Mike Tyson/Desiree Washington and William Kennedy Smith/Patricia Bowman trials garnered wide scale television coverage and delivered the issue of acquaintance rape into living rooms across America. Another recent trial which received national attention involved a group of teenaged boys in New Jersey who sodomized and sexually assaulted a mildly retarded 17-year old female classmate. While the circumstances in this instance differed from the Tyson and Smith cases, the legal definition of consent was again the central issue of the trial. Although the Senate Judiciary Committee hearings on the Supreme Court nomination of Judge Clarence Thomas were obviously not a rape trial, the focal point of sexual harassment during the hearings expanded national consciousness regarding the demarcations of sexual transgression. The sexual assault which took place at the Tailhook Association of Navy Pilots annual convention in 1991 was well documented. At the time of this writing, events involving sexual harassment, sexual coercion, and acquaintance rape of female Army recruits at the Aberdeen Proving Grounds and other military training facilities are being investigated.

As these well publicized events indicate, an increased awareness of sexual coercion and acquaintance rape has been accompanied by important legal decisions and changes in legal definitions of rape. Until recently, clear physical resistance was a requirement for a rape conviction in California. A 1990 amendment now defines rape as sexual intercourse "where it is accomplished against a person's will by means of force, violence, duress, menace, or fear of immediate and unlawful bodily injury." The important additions are "menace" and "duress," as they include consideration of verbal threats and implied threat of force (Harris, in Francis, 1996). The definition of "consent" has been expanded to mean "positive cooperation in act or attitude pursuant to an exercise of free will. A person must act freely and voluntarily and have knowledge of the nature of the act or transaction involved." In addition, a prior or current relationship between the victim and the accused is not sufficient to imply consent. Most states also have provisions which prohibit the use of drugs and/or alcohol to incapacitate a victim, rendering the victim unable to deny consent.

Acquaintance rape remains a controversial topic because of lack of agreement upon the definition of consent. In an attempt to clarify this definition, in 1994, Antioch College in Ohio adopted what has become an infamous policy delineating consensual sexual behavior. The primary reason this policy has stirred such an uproar is that the definition of consent is based on continuous verbal communication during intimacy. The person initiating the contact must take responsibility for obtaining the other participant's verbal consent as the level of sexual intimacy increases. This must occur with each new level. The rules also state that "If you have had a particular level of sexual intimacy before with someone, you must still ask each and every time." (The Antioch College Sexual Offense Policy, in Francis, 1996).

This attempt to remove ambiguity from the interpretation of consent was hailed by some as the closest thing yet to an ideal of "communicative sexuality." As is often the case with ground breaking social experimentation, it was ridiculed and lampooned by the majority of those who responded to it. Most criticism centered on reducing the spontaneity of sexual intimacy to what seemed like an artificial contractual agreement.

III. Social Perspectives on Acquaintance Rape

Feminists have traditionally devoted much attention to issues such as pornography, sexual harassment, sexual coercion, and acquaintance rape. The sociological dynamics which influence the politics of sexual equality tend to be complicated. There is no single position taken by feminists on any of the aforementioned issues; there are differing and often conflicting opinions. Views on pornography, for example, are divided between two opposing camps. Libertarian feminists, on one hand, distinguish between erotica (with themes of healthy consensual sexuality) and pornography (material that combines the "graphic sexually explicit" with depictions which are "actively subordinating, treating unequally, as less than human, on the basis of sex." (MacKinnon, in Stan, 1995). Socalled "protectionist" feminists tend not to make such a distinction and view virtually all sexually-oriented material as exploitative and pornographic.

Views on acquaintance rape also appear quite capable of creating opposing camps. Despite the violent nature of acquaintance rape, the belief that many victims are actually willing, consenting participants is held by both men and women alike. "Blaming the victim" seems to be an all too prevalent reaction to acquaintance rape. Prominent authors have espoused this idea in editorial pages, Sunday Magazine sections, and popular journal articles. Some of these authors are women (a few identify themselves as feminists) who appear to justify their ideas by drawing conclusions based on their own personal experiences and anecdotal evidence, not wide-scale, systematic research. They may announce that they too have probably been raped while on a date to illustrate their own inevitable entanglement in the manipulation and exploitation which are part of interpersonal relations. It has also been implied that a natural state of aggression between men and women is normal, and that any woman who would go back to a man's apartment after a date is "an idiot." While there may be a certain degree of cautionary wisdom in the latter part of this statement, such views have been criticized for being overly simplistic and for simply submitting to the problem.

There has been a recent flurry of these literary exchanges on acquaintance rape between women's rights advocates, who have been working to raise public awareness, and a relatively small group of revisionists who perceive that the feminist response to the problem has been alarmist. In 1993, The Morning After: Sex, Fear, and Feminism on Campus by Katie Roiphe was published. Roiphe alleged that acquaintance rape was largely a myth created by feminists and challenged the results of the Koss study. Those who had responded and mobilized to meet the problem of acquaintance rape were called "rape-crisis feminists." This book, including excerpted in many major women's magazines, argued that the magnitude of the acquaintance rape problem was actually very small. Myriad critics were quick to respond to Roiphe and the anecdotal evidence she gave to her claims.

IV. Research Findings

The research of Koss and her colleagues has served as the foundation of many of the investigations on the prevalence, circumstances, and aftermath of acquaintance rape within the past dozen or so years. The results of this research have served to create an identity and awareness of the problem. Equally as important has been the usefulness of this information in creating prevention models. Koss acknowledges that there are some limitations to the research. The most significant drawback is that her subjects were drawn exclusively from college campuses; thus, they were not representative of the population at large. The average age of the subjects was 21.4 years. By no means does this negate the usefulness of the findings, especially since the late teens and early twenties are the peak ages for the prevalence of acquaintance rape. The demographic profile of the 3,187 female and 2,972 male students in the study was similar to the makeup of the overall enrollment in higher education within the United States. Here are some of the most important statistics:

Prevalence

One in four women surveyed was victim of rape or attempted rape.
An additional one in four women surveyed was touched sexually against her will or was victim of sexual coercion.
84 percent of those raped knew their attacker.
57 percent of those rapes happened while on dates.
One in twelve male students surveyed had committed acts that met the legal definitions of rape or attempted rape.
84 percent of those men who committed rape said that what they did was definitely not rape.
Sixteen percent of the male students who committed rape and ten percent of those who attempted a rape took part in episodes involving more than one attacker.
Responses of the Victim

Only 27 percent of those women whose sexual assault met the legal definition of rape thought of themselves as rape victims.
42 percent of the rape victims did not tell anyone about their assaults.
Only five percent of the rape victims reported the crime to the police.
Only five percent of the rape victims sought help at rape-crisis centers.
Whether they had acknowledged their experience as a rape or not, thirty percent of the women identified as rape victims contemplated suicide after the incident.
82 percent of the victims said that the experience had permanently changed them.
V. Myths About Acquaintance Rape

There are a set of beliefs and misunderstandings about acquaintance rape that are held by a large portion of the population. These faulty beliefs serve to shape the way acquaintance rape is dealt with on both personal and societal levels. This set of assumptions often presents serious obstacles for victims as they attempt to cope with their experience and recovery.

Myth

Reality

A woman who gets raped usually deserves it, especially if she has agreed to go to a man's house or park with him.	No one deserves to be raped. Being in a man's house or car does not mean that a woman has agreed to have sex with him.
If a woman agrees to allow a man to pay for dinner, drinks, etc., then it means she owes him sex.	Sex is not an implied payback for dinner or other expense no matter how much money has been spent.
Acquaintance rape is committed by men who are easy to identify as rapists.	Women are often raped by "normal" acquaintances who resemble "regular guys."
Women who don't fight back haven't been raped.	Rape occurs when one is forced to have sex against their will, whether they have decided to fight back or not.
Intimate kissing or certain kinds of touching mean that intercourse is inevitable.	Everyone's right to say "no" should be honored, regardless of the activity which preceded it.
Once a man reaches a certain point of arousal, sex is inevitable and they can't help forcing themselves upon a woman.	Men are capable of exercising restraint in acting upon sexual urges.
Most women lie about acquaintance rape because they have regrets after consensual sex.	Acquaintance rape really happens - to people you know, by people you know.
Women who say "No" really mean "Yes."	This notion is based on rigid and outdated sexual stereotypes.
Certain behaviors such as drinking or dressing in a sexually appealing way make rape a woman's responsibility.	Drinking or dressing in a sexually appealing way are not invitations for sex.
VI. Who are the Victims?

Although it is not possible to make accurate predictions about who will be subjected to acquaintance rape and who won't, there is some evidence that certain beliefs and behaviors may increase the risk of becoming a victim. Women who subscribe to "traditional" views of men occupying a position of dominance and authority relative to women (who are seen as passive and submissive) may be at increased risk. In a study where the justifiability of rape was rated based on fictional dating scenarios, women with traditional attitudes tended to view the rape as acceptable if the women had initiated the date (Muehlenhard, in Pirog-Good and Stets, 1989). Drinking alcohol or taking drugs appears to be associated with acquaintance rape. Koss (1988) found that at least 55 percent of the victims in her study had been drinking or taking drugs just before the attack. Women who are raped within dating relationships or by an acquaintance are seen as "safe" victims because they are unlikely to report the incident to authorities or even view it as rape. Not only did a mere five percent of the women who had been raped in the Koss study report the incident, but 42 percent of them had sex again with their assailants.

The company one keeps may be a factor in predisposing women to an increased risk of sexual assault. An investigation of dating aggression and the features of college peer groups (Gwartney-Gibbs & Stockard, in Pirog-Good and Stets, 1989) supports this idea. The results indicate that those women who characterized the men in their mixed-sex social group as occasionally displaying forceful behavior towards women were significantly more likely themselves to be victims of sexual aggression. Being in familiar surroundings does not provide security. Most acquaintance rapes take place in either the victim's or the assailant's home, apartment, or dormitory.

VII. Who Commits Acquaintance Rape?

Just as with the victim, it is not possible to clearly identify individual men who will be participants in acquaintance rape. As a body of research begins to accumulate, however, there are certain characteristics which increase the risk factors. Acquaintance rape is not typically committed by psychopaths who are deviant from mainstream society. It is often expressed that direct and indirect messages given to boys and young men by our culture about what it means to male (dominant, aggressive, uncompromising) contribute to creating a mindset which is accepting of sexually aggressive behavior. Such messages are constantly sent via television and film when sex is portrayed as a commodity whose attainment is the ultimate male challenge. Notice how such beliefs are found within the vernacular of sex: "I'm going to make it with her," "Tonight's the night I'm going to score," "She's never had anything like this before," "What a piece of meat," "She's afraid to give it up."

Nearly everyone is exposed to this sexually biased current by various media, yet this does not account for individual differences in sexual beliefs and behaviors. Buying into stereotypical attitudes regarding sex roles tends to be associated with justification of intercourse under any circumstances. Other characteristics of the individual seem to facilitate sexual aggression. Research designed to determine traits of sexually aggressive males (Malamuth, in Pirog-Good and Stets, 1989) indicated that high scores on scales measuring dominance as a sexual motive, hostile attitudes towards women, condoning the use of force in sexual relationships, and the amount of prior sexual experience were all significantly related to self-reports of sexually aggressive behavior. Furthermore, the interaction of several of these variables increased the chance that an individual had reported sexually aggressive behavior. The inability to appraise social interactions, as well as prior parental neglect or sexual or physical abuse early in life may also be linked with acquaintance rape (Hall & Hirschman, in Wiehe and Richards, 1995). Finally, taking drugs or alcohol is commonly associated with sexual aggression. Of the men who were identified as having committed acquaintance rape, 75 percent had taken drugs or alcohol just prior to the rape (Koss, 1988).

VIII. The Effects of Acquaintance Rape

The consequences of acquaintance rape are often far-reaching. Once the actual rape has occurred and has been identified as rape by the survivor, she is faced with the decision of whether to disclose to anyone what has happened. In a study of acquaintance rape survivors (Wiehe & Richards, 1995), 97 percent informed at least one close confidant. The percentage of women who informed the police was drastically lower, at 28 percent. A still smaller number (twenty percent) decided to prosecute. Koss (1988) reports that only two percent of acquaintance rape survivors report their experiences to the police. This compared with the 21 percent who reported rape by a stranger to the police. The percentage of survivors reporting the rape is so low for several reasons. Self-blame is a recurring response which prevents disclosure. Even if the act has been conceived as rape by the survivor, there is often an accompanying guilt about not seeing the sexual assault coming before it was too late. This is often directly or indirectly reinforced by the reactions of family or friends in the form of questioning the survivor's decisions to drink during a date or to invite the assailant back to their apartment, provocative behavior, or previous sexual relations. People normally relied upon for support by the survivor are not immune to subtly blaming the victim. Another factor which inhibits reporting is the anticipated response of the authorities. Fear that the victim will again be blamed adds to apprehension about interrogation. The duress of reexperiencing the attack and testifying at a trial, and a low conviction rate for acquaintance rapists, are considerations as well.

The percentage of survivors who seek medical assistance after an attack is comparable to the percentage reporting to police (Wiehe & Richards, 1995). Serious physical consequences often emerge and are usually attended to before the emotional consequences. Seeking medical help can also be a traumatic experience, as many survivors feel like they are being violated all over again during the examination. More often than not, attentive and supportive medical staff can make a difference. Survivors may report being more at ease with a female physician. The presence of a rape-crisis counselor during the examination and the long periods of waiting that are often involved with it can be tremendously helpful. Internal and external injury, pregnancy, and abortion are some of the more common physical aftereffects of acquaintance rape.

Research has indicated that the survivors of acquaintance rape report similar levels of depression, anxiety, complications in subsequent relationships, and difficulty attaining pre-rape levels of sexual satisfaction to what survivors of stranger rape report (Koss & Dinero, 1988). What may make coping more difficult for victims of acquaintance rape is a failure of others to recognize that the emotional impact is just as serious. The degree to which individuals experience these and other emotional consequences varies based on factors such as the amount of emotional support available, prior experiences, and personal coping style. The way that a survivor's emotional harm may translate into overt behavior also depends on individual factors. Some may become very withdrawn and uncommunicative, others may act out sexually and become promiscuous. Those survivors who tend to deal the most effectively with their experiences take an active role in acknowledging the rape, disclosing the incident to appropriate others, finding the right help, and educating themselves about acquaintance rape and prevention strategies.

One of the most serious psychological disorders which can develop as the result of acquaintance rape is Posttraumatic Stress Disorder (PTSD). Rape is just one of many possible causes of PTSD, but it (along with other forms of sexual assault) is the most common cause of PTSD in American women (McFarlane & De Girolamo, in van der Kolk, McFarlane, & Weisaeth, 1996). PTSD as it relates to acquaintance rape is defined as in the Diagnostic and Statistical Manual of Mental Disorders-Fourth Edition as "the development of characteristic symptoms following exposure to an extreme traumatic stressor involving direct personal experience of an event that involves actual or threatened death or serious injury, or other threat to one's physical integrity" (DSM-IV, American Psychiatric Association, 1994). A person's immediate response to the event includes intense fear and helplessness. Symptoms which are part of the criteria for PTSD include persistent reexperiencing of the event, persistent avoidance of stimuli associated with the event, and persistent symptoms of increased arousal. This pattern of reexperiencing, avoidance, and arousal must be present for at least one month. There must also be an accompanying impairment in social, occupational, or other important realm of functioning (DSM-IV, APA, 1994).

If one takes note of the causes and symptoms of PTSD and compares them to thoughts and emotions which might be evoked by acquaintance rape, it is not difficult to see a direct connection. Intense fear and helplessness are likely to be the core reactions to any sexual assault. Perhaps no other consequence is more devastating and cruel than the fear, mistrust, and doubt triggered by the simple encounters and communication with men which are a part of everyday living. Prior to the assault, the rapist had been indistinguishable from non rapists. After the rape, all men may be seen as potential rapists. For many victims, hypervigilance towards most men becomes permanent. For others, a long and difficult recovery process must be endured before a sense of normalcy returns.

IX. Prevention

The following section has been adapted from I Never Called It Rape, by Robin Warshaw. Prevention is not just the responsibility of the potential victims, that is, of women. Men may try to use acquaintance rape myths and false stereotypes about "what women really want" to rationalize or excuse sexually aggressive behavior. The most widely used defense is to blame the victim. Education and awareness programs, however, can have a positive effect in encouraging men to take increased responsibility for their behavior. Despite this optimistic statement, there will always be some individuals who won't get the message. Although it may be difficult, if not impossible, to detect someone who will commit acquaintance rape, there are some characteristics which can signal trouble. Emotional intimidation in the form of belittling comments, ignoring, sulking, and dictating friends or style of dress may indicate high levels of hostility. Projecting an overt air of superiority or acting as if one knows another much better than the one actually does may also be associated with coercive tendencies. Body posturing such as blocking a doorway or deriving pleasure from physically startling or scaring are forms of physical intimidation. Harboring negative attitudes toward women in general can be detected in the need to speak derisively of previous girlfriends. Extreme jealousy and an inability to handle sexual or emotional frustration without anger may reflect potentially dangerous volatility. Taking offense at not consenting to activities which could limit resistance, such as drinking or going to a private or isolated place, should serve as a warning.

Many of these characteristics are similar to each other and contain themes of hostility and intimidation. Maintaining an awareness of such a profile may facilitate quicker, clearer, and more resolute decision-making in problematic situations. Practical guidelines which may be helpful in decreasing the risk of acquaintance rape are available. Expanded versions, as well as suggestions about what to do if rape occurs, may be found in Intimate Betrayal: Understanding and Responding to the Trauma of Acquaintance Rape (Wiehe & Richards, 1995) and I Never Called It Rape (Warshaw, 1994).

References

American Psychiatric Association, (1994). Diagnostic and statistical manual of mental disorders (4th ed.). Washington, DC: Author.

Francis, L., Ed. (1996) Date rape: Feminism, philosophy, and the law. University Park, PA: Pennsylvania State University Press.

Gwartney-Gibbs, P. & Stockard, J. (1989). Courtship aggression and mixed-sex peer groups In M.A. Pirog-Good & J.E. Stets (Eds.)., Violence in dating relationships: Emerging social issues (pp. 185-204). New York, NY: Praeger.

Harris, A.P. (1996). Forcible rape, date rape, and communicative sexuality. In L. Francis (Ed.)., Date rape: Feminism, philosophy, and the law (pp. 51-61). University Park, PA: Pennsylvania State University Press.

Koss, M.P. (1988). Hidden rape: Sexual aggression and victimization in the national sample of students in higher education. In M.A. Pirog-Good & J.E. Stets (Eds.)., Violence in dating relationships: Emerging social issues (pp. 145168). New York, NY: Praeger.

Koss, M.P. & Dinero, T.E. (1988). A discriminant analysis of risk factors among a national sample of college women. Journal of Consulting and Clinical Psychology, 57, 133-147.

Malamuth, N.M. (1989). Predictors of naturalistic sexual aggression. In M.A. Pirog-Good & J.E. Stets (Eds.)., Violence in dating relationships: Emerging social issues (pp. 219- 240). New York, NY: Praeger.

McFarlane, A.C. & DeGirolamo, G. (1996). The nature of traumatic stressors and the epidemiology of posttraumatic reactions. In B.A. van der Kolk, A.C. McFarlane & L. Weisaeth (Eds.)., Traumatic stress: The effects of overwhelming experience on mind, body, and society (pp. 129-154). New York, NY: Guilford.

Muehlenhard, C.L. (1989). Misinterpreted dating behaviors and the risk of date rape. In M.A. Pirog-Good & J.E. Stets (Eds.)., Violence in dating relationships: Emerging social issues (pp. 241-256). New York, NY: Praeger.

Stan, A.M., Ed. (1995). Debating sexual correctness: Pornography, sexual harassment, date rape, and the politics of sexual equality. New York, NY: Delta.

Warshaw, R. (1994). I never called it rape. New York, NY: HarperPerennial.

Wiehe, V.R. & Richards, A.L. (1995). Intimate betrayal: Understanding and responding to the trauma of acquaintance rape. Thousand Oaks, CA: Sage.

David G. Curtis, Ph.D., B.C.E.T.S., is a Clinical and School Psychologist. As a consulting psychologist with Long Island Psychological Associates, P.C. in New York he is involved with the evaluation and treatment of survivors of traumatic events. Dr. Curtis is also a school psychologist in the Merrick School District. He is the author and coordinator of the District's Crisis Response Plan. He is a Board Certified Expert in Traumatic Stress and Diplomate of the American Academy of Experts in Traumatic Stress, where he also serves on the Scientific Advisory Board. Dr. Curtis has held an Adjunct Professor position at Hofstra University. He has presented at various conferences on topics such as Attention Deficit Disorder and Psychological Inhibitors of Athletic Performance. He is a member of the American Psychological Association, the Association for the Advancement of Behavior Therapy, the Nassau County Psychological Association, and the Suffolk County Psychological Association.

©1997 by The American Academy of Experts in Traumatic Stress, Inc.

---
## [CryDeS/Angel-Arena-Reborn](https://github.com/CryDeS/Angel-Arena-Reborn)@[24633a752b...](https://github.com/CryDeS/Angel-Arena-Reborn/commit/24633a752b5738342b0364e0ebb34764f2e2d41b)
#### Monday 2022-07-11 15:57:01 by Dunkan

Patch 25.06.2022

Hero changes:

Abaddon
	- 1 skill self damage	changed from 30/35/40/45/50/55/60 to 50
	- 2 skill cast point  changed from 0.452 to 0.3
	- 2 skill duration  changed from  13 to 15
	- 3 skill movement speed changed from 25 to 15/17/19/21/23/25/25"

Abyssal Underlord
	- 2 skill root duration 	1.0/1.2/1.4/1.5/1.6/1.7/2.1" to 1.0/1.2/1.3/1.4/1.5/1.6/1.7

Alkchmist
	- shard skill Berserk Potion bonus ms 0 to 30

Ancient Аpparation
	- 2 skill shard damage changed from 40 to 150
	- 2 skill shard attack speed slow changed from 20 to 50

Dragon Knight
	- Fireball damage changed from 75 to 150

Furion
	- 1 skill Cooldown changed from 14/13/12/11/10/9/8 to 15
	- 3 skill treant health changed from 550/650/750/850/950/1050/1150 to 550/600/650/700/750/850/1100
	- 3 skill treant damage changed from 45/55/65/75/85/95/105 to 25/30/45/55/60/65/105
	- 4 skill Cooldown changed from 50 to 65

Huskar
	- 4 skill health damage changed from 45 to 20/22/25/27/33/36/45

Chaos Knight
 	- 3 skill crit chance changed from 30 to 25
 	- 3 skill crit max changed from 190/220/250/280/310/350/400 to 170/190/220/250/290/320/350
 	- 3 skill lifesteal changed from 30/35/40/45/50/55/60 to 25/30/35/40/45/50/55

Crystal Maiden's

 	- 3 skill mana per cast 10/15/20/25/30/35/40

Centaur
 	- 1 skill stun duration changed from 2.0 to 2.0/2.1/2.2/2.3/2.4/2.5/2.6
Charon
        - Ultimate root can be dispelled

Dawnbreaker
 	- 4 skill damage of pulsation changed from 30/50/70/80/90/100/110 to 50/75/100/125/150/175/200
 	- 4 skill heal of pulsation changed from 50/70/90/110/130/150/170 to 50/75/100/125/150/175/200
 	- 4 skill damage changed from 130/160/190/220/250/280/310 to 200/300/400/500/600/700/800

Medusa
	- Cold Blooded Cooldown changed from 6 to 10

Marci
	- 4 skill Cooldown changed from 110/100/90/80/70/60/50 to 80/75/70/65/60/55/50
	- 4 skill between flurries changed from 1.75 to 1.55/1.50/1.45/1.40/1.35/1.30/1.25
	- 4 skill attack Stacks changed from 3/4/5/6/7/8/9 to 4/5/6/7/8/9/10
	- talent 25lvl silence duration changed from 1.5sec to 0.5sec

Primal Beast
	- Added to Angel Arena

Techies
	- Added techies skill frm dota

Undying
	- 4 skill Cooldown changed from 40 to 60
	- Shard Cooldown ultimate changed from 35 to 20

Item changes:

Tome of heroes
	- stack start game 5
	- delay before the start of the game 600sec
	- Max stack 40
	- Cooldown stack 20sec
	- Cost changed from 1250 to 1500

Ethereal Blade
	- Craft changed from Ghost scepter + Recipe to Mystic staff + Ghost scepter + Recipe

Gem
	- cast range changed from 300 to 500
	- active skill radius changed from 300 to 500
	- duration active skill changed from 4 to 8
	- Cooldown active skill changed from 12 to 30

Bosses:

Keymaster
	- now Ignores terrain
	- ms changed from 365 to 400

Creeps:

Satyr hand
	- 3 skill magic amplify changed from 50 to 20

Fixes:
Storm Spirit 1 skill damage fixed
Earth Spirit ultimate fixed
Elder Titan ultimate fixed
Abyssal Underlord ultimate fixed
Omniknight 3 skill and ultimate fixed
Pudge 3 skill fixed
Templar Assassin 3 skill fixed
Shadow Fiend aghanim fixed
Hoodwink shard skill fixed
Morphlimg 1 skill fixed
Swift blink range fixed
Overwhelming blink range fixed
Arcane blink range fixed

---
## [CryDeS/Angel-Arena-Reborn](https://github.com/CryDeS/Angel-Arena-Reborn)@[d8f9d1967b...](https://github.com/CryDeS/Angel-Arena-Reborn/commit/d8f9d1967bd2f6737f03a9504564c0728ec1adfe)
#### Monday 2022-07-11 15:57:01 by Dunkan

Patch2

Hero changes:

Abaddon
	- 1 skill self damage	changed from 30/35/40/45/50/55/60 to 50
	- 2 skill cast point  changed from 0.452 to 0.3
	- 2 skill duration  changed from  13 to 15
	- 3 skill movement speed changed from 25 to 15/17/19/21/23/25/25"

Abyssal Underlord
	- 2 skill root duration 	1.0/1.2/1.4/1.5/1.6/1.7/2.1" to 1.0/1.2/1.3/1.4/1.5/1.6/1.7

Alkchmist
	- shard skill Berserk Potion bonus ms 0 to 30

Ancient Аpparation
	- 2 skill shard damage changed from 40 to 150
	- 2 skill shard attack speed slow changed from 20 to 50

Dragon Knight
	- Fireball damage changed from 75 to 150

Furion
	- 1 skill Cooldown changed from 14/13/12/11/10/9/8 to 15
	- 3 skill treant health changed from 550/650/750/850/950/1050/1150 to 550/600/650/700/750/850/1100
	- 3 skill treant damage changed from 45/55/65/75/85/95/105 to 25/30/45/55/60/65/105
	- 4 skill Cooldown changed from 50 to 65

Huskar
	- 4 skill health damage changed from 45 to 20/22/25/27/33/36/45

Chaos Knight
 	- 3 skill crit chance changed from 30 to 25
 	- 3 skill crit max changed from 190/220/250/280/310/350/400 to 170/190/220/250/290/320/350
 	- 3 skill lifesteal changed from 30/35/40/45/50/55/60 to 25/30/35/40/45/50/55

Crystal Maiden's

 	- 3 skill mana per cast 10/15/20/25/30/35/40

Centaur
 	- 1 skill stun duration changed from 2.0 to 2.0/2.1/2.2/2.3/2.4/2.5/2.6

Dawnbreaker
 	- 4 skill damage of pulsation changed from 30/50/70/80/90/100/110 to 50/75/100/125/150/175/200
 	- 4 skill heal of pulsation changed from 50/70/90/110/130/150/170 to 50/75/100/125/150/175/200
 	- 4 skill damage changed from 130/160/190/220/250/280/310 to 200/300/400/500/600/700/800

Medusa
	- Cold Blooded Cooldown changed from 6 to 10

Marci
	- 4 skill Cooldown changed from 110/100/90/80/70/60/50 to 80/75/70/65/60/55/50
	- 4 skill between flurries changed from 1.75 to 1.55/1.50/1.45/1.40/1.35/1.30/1.25
	- 4 skill attack Stacks changed from 3/4/5/6/7/8/9 to 4/5/6/7/8/9/10
	- talent 25lvl silence duration changed from 1.5sec to 0.5sec

Primal Beast
	- Added to Angel Arena

Techies
	- Added techies skill frm dota

Undying
	- 4 skill Cooldown changed from 40 to 60
	- Shard Cooldown ultimate changed from 35 to 20

Item changes:

Tome of heroes
	- stack start game 5
	- delay before the start of the game 600sec
	- Max stack 40
	- Cooldown stack 20sec
	- Cost changed from 1250 to 1500

Ethereal Blade
	- Craft changed from Ghost scepter + Recipe to Mystic staff + Ghost scepter + Recipe

Gem
	- cast range changed from 300 to 500
	- active skill radius changed from 300 to 500
	- duration active skill changed from 4 to 8
	- Cooldown active skill changed from 12 to 30

Bosses:

Keymaster
	- now Ignores terrain
	- ms changed from 365 to 400

Creeps:

Satyr hand
	- 3 skill magic amplify changed from 50 to 20

Fixes:
Storm Spirit 1 skill damage fixed
Earth Spirit ultimate fixed
Elder Titan ultimate fixed
Abyssal Underlord ultimate fixed
Omniknight 3 skill and ultimate fixed
Pudge 3 skill fixed
Templar Assassin 3 skill fixed
Shadow Fiend aghanim fixed
Hoodwink shard skill fixed
Morphlimg 1 skill fixed
Swift blink range fixed
Overwhelming blink range fixed
Arcane blink range fixed

---
## [CoderGang2/ReeqyHub](https://github.com/CoderGang2/ReeqyHub)@[4ebbe1ac91...](https://github.com/CoderGang2/ReeqyHub/commit/4ebbe1ac91b666f53ecdb874245acb9a8185140f)
#### Monday 2022-07-11 16:03:08 by Ivory

Auto Script Create your mom lol im so funny ha ha ha ha if you are not laughing i will come to your house and fuck your mom

---
## [RavZen/android_frameworks_base](https://github.com/RavZen/android_frameworks_base)@[4f678219b0...](https://github.com/RavZen/android_frameworks_base/commit/4f678219b071dda266d3ef9e00371b59bdfec34b)
#### Monday 2022-07-11 16:12:56 by Joey Huab

PixelPropsUtils: Spoof play store once again

* Diablo Immortal fuck you

---
## [rathena/rathena](https://github.com/rathena/rathena)@[d617d9f083...](https://github.com/rathena/rathena/commit/d617d9f08381442b14cb69da6ef5251a12817cd3)
#### Monday 2022-07-11 17:05:48 by Aleos

Updates SC_CHANGEUNDEAD behavior (#6867)

* Fixes #6834.
* Versus Players
- Animation will be properly displayed for Blessing/Increase Agility when the target has Change Undead active (buffs are not applied even though animation is displayed).
- Target can no longer be killed through the single damage applied by Blessing/Increase Agility and Change Undead.
- If the target has Curse and Stone active, only Curse is removed by Blessing first (buffs are not applied).
- Shadow or Undead armor have no impact on Blessing or Increase Agility at all.
* Versus Monsters
- Blessing is applied normally to the target as long as it's not an Undead element or Demon race.
- Blessing does not cancel out Curse or Stone.
Thanks to @Playtester!

---
## [microsoft/terminal](https://github.com/microsoft/terminal)@[9ccd6ecd74...](https://github.com/microsoft/terminal/commit/9ccd6ecd744890b856f3d8a39ff0616c0e34d4fb)
#### Monday 2022-07-11 17:43:31 by Mike Griese

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
## [ARF-SS13/byond-docker](https://github.com/ARF-SS13/byond-docker)@[e6cc3ebf1f...](https://github.com/ARF-SS13/byond-docker/commit/e6cc3ebf1f8ac7fcdc150e56e1be0dcd36bb4b33)
#### Monday 2022-07-11 18:34:11 by GremlingSS

Cock and ball torture (CBT) is a sexual activity involving application of pain or constriction to the male genitals. This may involve directly painful activities, such as wax play, genital spanking, squeezing, ball-busting, genital flogging, urethral play, tickle torture, erotic electrostimulation or even kicking.[1] The recipient of such activities may receive direct physical pleasure via masochism, or emotional pleasure through erotic humiliation, or knowledge that the play is pleasing to a sadistic dominant. Many of these practices carry significant health risks.

---
## [TheBoondock/tgstation](https://github.com/TheBoondock/tgstation)@[763a10d1cc...](https://github.com/TheBoondock/tgstation/commit/763a10d1cc44c91720101d422d8709ad1aa0644d)
#### Monday 2022-07-11 18:56:59 by distributivgesetz

Resonance cascade polishening, bugfixes and better logging (#67488)

This PR rewrites almost all messages related to cascade events. Some messages felt kinda clunky to read or could have been written better. Overall, the new messages add to the experience as a cascade being a terrifying event in a way that I felt the old ones missed, and they make the event feel overall a lot sharper.

While looking at the resonance cascade code, I noticed that there a lot of stuff about cascades in the air which was not touched on. So, as I do, this PR evolved into a polish and roundup PR for cascades. There was a lot of stuff still hanging out relating to the event, and although the big backend of it sits, there was still a bit left to be completed. Therefore this PR deserves more the title of the "Resonance cascade POLISHENING" instead of the "REFLAVAHRING". But yeah, you ever go on a massive tangent before?

---
## [WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/FEDERAL-USE-AND-DISTRIBUTION-ONLY](https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/FEDERAL-USE-AND-DISTRIBUTION-ONLY)@[49e4da37eb...](https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/FEDERAL-USE-AND-DISTRIBUTION-ONLY/commit/49e4da37eb63f745db2f77d85a779f3d7f1346a8)
#### Monday 2022-07-11 19:09:21 by WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER

Create 1940-rapid-transit-RECEIPTS

19:40, the year the Rapid transit authority was understood. 

Check the count of references here:
>>     https://en.wikipedia.org/wiki/Interborough_Rapid_Transit_Company 

Then check the count of references here:
>>    https://en.wikipedia.org/wiki/IRT_Powerhouse 

Also watch this documentary and look at what happens when you catch a [F], they ask why unless they need guidance.
see also: 19:40 in that documentary and what happens after with blow your mind as well.

https://www.fbi.gov/video-repository/newss-chasing-the-dragon-the-life-of-an-opiate-addict/file_view 

Look what happens to the lady on the couch watching Jerry spring-her documentary or whatever.

>> they didn’t really ask any questions before entering either - and YEP

>> GUESS WHAT- they ALL do work 24/7 in:  HK :) , TKY ; )*, INDIA : )* , NEPAL : ( , AND [ 90849565 HK EST ++ ]

///

##########################################################

 >> 6.24.2020 email - ASHLEY.HUMPHRIES@WILSONELSER.COM

 
THIS PAGE IS BEING MONITORED BY SEVERAL DEPARTMENTS AS PART OF A FEDERAL BANK AND SECURITIES FRAUD INVESTIGATION.

https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER


 >> AFTER THE LEASES WERE TRANSFERRED TO STATE FARM, AND NO I DIDN'T FOLLOW HER.
- people go to PRISON FOR THAT as well -- NO DIFFERENT THAN A HEROIN SALESMAN DEPOSITING ASSETS AT A BANK.


PLAINTIFF ASSIGNED LEASES AND RENTS ON MAY 15TH TO STATE FARM LIFE INSURANCE COMPANY - INCLUDING THEIR TAX RISKS AS IMPLIED
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=19MVPFXy0G0QvnmRLGpYIQ==

 
EXHIBIT(S)  - AC0  (Motion #001)
ACRIS Detailed Document Information (2019000021408)2019010800475001
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=ze6a1KA9akRV9TGfXXJT/g==

 
EXHIBIT(S)  - AC1  (Motion #001)
ACRIS Detailed Document Information (2020000155422)2020052000291003
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=bVk8sIt7n3kGwHqebPg0fw==

 
EXHIBIT(S)  - AC2  (Motion #001)
ACRIS Detailed Document Information (2020000155421)2020052000291002
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=wTG2YD2PqXuxmoKqFiESrw==


ACRIS Detailed Document Information (2020000155422)2020052000291003
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=au8qh7Dn66hrVmJ9DX_PLUS_bdg==
EXHIBIT(S)  - AC4  (Motion #001)

ACRIS Detailed Document Information (2020000155423)2020052000291004
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=/yhElCiKJ0BGv2DF/MOn4g==

 
EXHIBIT(S)  - ACR  (Motion #002)
ACRIS.NYC.GOV >> ASSIGNMENT OF LEASE AND RENTS ON FILED ON MAY 26TH
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=gcMSDaFzm0ynPeXZKSHgLQ==


-------- Forwarded Message --------
Subject: 	xmas, interborough rapid transit, does not auto-loop.
Date: 	Mon, 11 Jul 2022 18:28:49 +0000 (UTC)
From: 	Bo Dincer <bo.dincer@yahoo.com>
Reply-To: 	bo.dincer@yahoo.com <bo.dincer@yahoo.com>
To: 	Baris Dincer <bdincer66@icloud.com>, MILTON MCKENZIE <ms60710444266@yahoo.com>, baris.dincer@jjay.cuny.edu <baris.dincer@jjay.cuny.edu>




/S/ BO DINCER

    ----- Forwarded Message -----
    From: "Bo Dincer" <bo.dincer@yahoo.com>
    To: "usdoj@public.govdelivery.com" <usdoj@public.govdelivery.com>, "irs@service.govdelivery.com" <irs@service.govdelivery.com>, "usttb@public.govdelivery.com" <usttb@public.govdelivery.com>, "financialeducation@info.consumerfinance.gov" <financialeducation@info.consumerfinance.gov>, "DHSOIG@public.govdelivery.com" <DHSOIG@public.govdelivery.com>, "Office of Inspector General (VETERANS AFFAIRS)" <vaoig@messages.va.gov>, "PENSION BENEFIT GURANTEES" <pbgc@subscriptions.pbgc.gov>, "USPSOIG@public.govdelivery.com" <USPSOIG@public.govdelivery.com>, "cdfifund@service.govdelivery.com" <cdfifund@service.govdelivery.com>, "subscribe@subscribe.ftc.gov" <subscribe@subscribe.ftc.gov>, "vatax@public.govdelivery.com" <vatax@public.govdelivery.com>, "tigta@service.govdelivery.com" <tigta@service.govdelivery.com>, "Small Business Administration" <news@updates.sba.gov>, "DOT INSPECTOR GENERAL" <news@updates.oig.dot.gov>, "Office of the Special Inspector General for the Troubled Asset Relief Program "(SIGTARP)" <sigtarp@service.govdelivery.com>, "HUDOIG@info.hudoig.gov" <HUDOIG@info.hudoig.gov>, "Council of the Inspectors General on Integrity and Efficiency" <CIGIE@public.govdelivery.com>, "CBPMEDIARELATIONS" <CBPMEDIARELATIONS@cbp.dhs.gov>, "AZCBPPublicAffairs@cbp.dhs.gov" <AZCBPPublicAffairs@cbp.dhs.gov>, "Constituentservices@doc.nyc.gov" <Constituentservices@doc.nyc.gov>, "OFCCP-Public@dol.gov" <OFCCP-Public@dol.gov>, "foia@eeoc.gov" <foia@eeoc.gov>, "NYCTLservicing@tcmfund.com" <NYCTLservicing@tcmfund.com>, "matthew.schimmel@cigie.gov" <matthew.schimmel@cigie.gov>, "laura.nichols@cigie.gov" <laura.nichols@cigie.gov>, "SOCIAL SECURITY ADMINISTRATION" <subscriptions@subscriptions.treas.gov>, "Hon. Nancy T. Sunshine" <kcco-efile@nycourts.gov>, "CUIT Communications" <cuit-communications@columbia.edu>, "CommissionerCrenshaw@sec.gov" <CommissionerCrenshaw@sec.gov>, "CommissionerLee@sec.gov" <CommissionerLee@sec.gov>, "usmint-support@usmcatalog.com" <usmint-support@usmcatalog.com>, "ofac_feedback@treasury.gov" <ofac_feedback@treasury.gov>, "ServiceECF@law.nyc.gov" <ServiceECF@law.nyc.gov>, "JPINN@LAW.NYC.GOV" <JPINN@LAW.NYC.GOV>, "nschaier@law.nyc.gov" <nschaier@law.nyc.gov>, "hadkins@mtagservices.com" <hadkins@mtagservices.com>, "GREGORY.L.DAVIS@cbp.dhs.gov" <GREGORY.L.DAVIS@cbp.dhs.gov>, "esanford@mtagservices.com" <esanford@mtagservices.com>, "jmeeks@station31partners.com" <jmeeks@station31partners.com>, "kshadle@tcmfund.com" <kshadle@tcmfund.com>, "dcarter@mtagservices.com" <dcarter@mtagservices.com>, "nchini@bainbridge.com" <nchini@bainbridge.com>, "gmichaud@mtagservices.com" <gmichaud@mtagservices.com>, "LANDON.R.HUTCHENS@cbp.dhs.gov" <LANDON.R.HUTCHENS@cbp.dhs.gov>, "TAMMY.T.MELVIN@cbp.dhs.gov" <TAMMY.T.MELVIN@cbp.dhs.gov>, "usmint-support@pfsweb.com" <usmint-support@pfsweb.com>, "ANTHONY.BUCCI@cbp.dhs.gov" <Anthony.bucci@cbp.dhs.gov>, "JOHN.B.MENNELL@cbp.dhs.gov" <JOHN.B.MENNELL@cbp.dhs.gov>, "Martin.Rowland@parks.nyc.gov" <Martin.Rowland@parks.nyc.gov>, "dernwein@tcmfund.com" <dernwein@tcmfund.com>, "asimmons@mtagservices.com" <asimmons@mtagservices.com>, "cshugg@sylint.com" <cshugg@sylint.com>, "isabel.zisselsberger@kpmg.com" <isabel.zisselsberger@kpmg.com>, "ITACKEL@cbp.dhs.gov" <ITACKEL@cbp.dhs.gov>, "RICHARD.J.PAUZA@CBP.DHS.GOV" <RICHARD.J.PAUZA@CBP.DHS.GOV>, "JAMES.E.BURNS@cbp.dhs.gov" <JAMES.E.BURNS@cbp.dhs.gov>, "electronicfilings@ftc.gov" <electronicfilings@ftc.gov>, "usdoj@public.govdelivery.GOV" <usdoj@public.govdelivery.GOV>, "irs@service.govdelivery.GOV" <irs@service.govdelivery.GOV>, "subscription.service@subscriptions.ssa.gov" <subscription.service@subscriptions.ssa.gov>, "steven.p.bansbach@cbp.dhs.gov" <steven.p.bansbach@cbp.dhs.gov>, "usattorneys@public.govdelivery.com" <usattorneys@public.govdelivery.com>, "OJJDP@public.govdelivery.com" <OJJDP@public.govdelivery.com>, "fundingnews@public.govdelivery.com" <fundingnews@public.govdelivery.com>, "Civil.Feedback@usdoj.gov" <Civil.Feedback@usdoj.gov>, "CivilRightsDivision@usdoj.gov" <CivilRightsDivision@usdoj.gov>, "premerger@usdoj.gov" <premerger@usdoj.gov>, "Criminal.Division@usdoj.gov" <Criminal.Division@usdoj.gov>, "privacy@usdoj.gov" <privacy@usdoj.gov>, "dea@public.govdelivery.com" <dea@public.govdelivery.com>, "NewYork.ATR@usdoj.gov" <NewYork.ATR@usdoj.gov>, "ATR.International@usdoj.gov" <ATR.International@usdoj.gov>, "ATR.TEA@usdoj.gov" <ATR.TEA@usdoj.gov>, "ATR.MEP.Information@usdoj.gov" <ATR.MEP.Information@usdoj.gov>, "ATR.EXO@usdoj.gov" <ATR.EXO@usdoj.gov>, "ATR.EAG@usdoj.gov" <ATR.EAG@usdoj.gov>, "ATR.CPA@usdoj.gov" <ATR.CPA@usdoj.gov>, "Chicago.ATR@usdoj.gov" <Chicago.ATR@usdoj.gov>, "ATR.Appellate@usdoj.gov" <ATR.Appellate@usdoj.gov>, "antitrust.atr@usdoj.gov" <antitrust.atr@usdoj.gov>, "jessica.rosenbaum@usdoj.gov" <jessica.rosenbaum@usdoj.gov>, "mross@stratford.k12.ia.us" <mross@stratford.k12.ia.us>, "yolanda.choates@cbp.dhs.gov" <yolanda.choates@cbp.dhs.gov>, "tameka.link@dc.gov" <Tameka.Link@dc.gov>, "OVC@public.govdelivery.com" <OVC@public.govdelivery.com>, "latonia.battlewhite@dc.gov" <latonia.battlewhite@dc.gov>, "syncia.sabain@dc.gov" <syncia.sabain@dc.gov>, "charles.akinboyewa@dc.gov" <charles.akinboyewa@dc.gov>, "sandra.thalley@dc.gov" <sandra.thalley@dc.gov>, "Robert.Greene@dc.gov" <Robert.Greene@dc.gov>, "USAID-Industry-Liaison@subscribe.usaid.gov" <USAID-Industry-Liaison@subscribe.usaid.gov>, "donotreply@info.consumerfinance.gov" <donotreply@info.consumerfinance.gov>, "SanFran.ATR@usdoj.gov" <SanFran.ATR@usdoj.gov>, "ATR.TFS@usdoj.gov" <ATR.TFS@usdoj.gov>, "nsd.public@usdoj.gov" <nsd.public@usdoj.gov>, "AskSMART@usdoj.gov" <AskSMART@usdoj.gov>, "ocdetf.foia@usdoj.gov" <ocdetf.foia@usdoj.gov>, "MRUFOIA.Requests@usdoj.gov" <MRUFOIA.Requests@usdoj.gov>, "ogis@nara.gov" <ogis@nara.gov>, "National.FOIAPortal@usdoj.gov" <National.FOIAPortal@usdoj.gov>, "Nicole.Colbert@dc.gov" <Nicole.Colbert@dc.gov>, "ServiceDesk@doc.nyc.gov" <ServiceDesk@doc.nyc.gov>, "OGIS" <OGIS+noreply@nara.gov>, "asiegel@mtagservices.com" <asiegel@mtagservices.com>, "Doreen.Deterville@dc.gov" <Doreen.Deterville@dc.gov>, "Terrence.Davis@dc.gov" <Terrence.Davis@dc.gov>, "renee.alexander@dc.gov" <renee.alexander@dc.gov>, "keena.blackmon@dc.gov" <keena.blackmon@dc.gov>, "valerie.butler@dc.gov" <valerie.butler@dc.gov>, "Charles.akinbeyowa@dc.gov" <Charles.akinbeyowa@dc.gov>, "eric.glover@dc.gov" <eric.glover@dc.gov>
    Cc: "Baris Dincer" <bdincer66@icloud.com>
    Sent: Sun, Jul 10, 2022 at 6:19 PM
    Subject: I recommended a $150MMM fine To MRS. SCHOCK to 8209 for the
    I recommended a $150MMM fine To MRS. SCHOCK to 8209 for the OX. V

        On Sat, Jul 9, 2022 at 11:22 PM, Bo Dincer
        <bo.dincer@yahoo.com> wrote:
        The essesnce if stupidity in DEED. 

        /S/ BO DINCER

            On Sat, Jul 9, 2022 at 7:05 PM, B D2022
            <ms60710444266@yahoo.com> wrote:

            LOOK HOW QUICKLY THEY MOVE ONCE I FILE THEIR CERTIFICATES OF OCCUPANCY AND THE LOAN DOCKETS - 50074 EST ++

            A LOT OR A LITTLE MONEY LAURIE -- HOW MUCH YOU OWE THE STATE FARM LIFE INSURANCE COMPANY IF EVERYONE SIMULTANEOUSLY NEEDS TO CASH OUT THEIR WHOLE LIFE PLANS - AT THE SAME TIME?
               



            ### NOTWITHSTANDING THE US. DEPT OF JUSTICE.
            18 U.S. Code § 1512 - Tampering with a witness, victim, or an informant<br>

            *** Fwd: Fwd: [ USC Title 18.1512 ] [USC Title 18.225, USC Title 18.21, USC Title 18.4, USC Title 18.3, USC Title 18.2]<br>

            NYSCEF MATTER 153974/2020 WHILE THEY CASUALLY VIOLATED MY CIVIL RIGHTS<br>

            NO COMPLAINTS HAVE BEEN FILED IN MY BUILDING<br>

            - PER DEPARTMENT OF BUILDINGS RECORD CONTRARY TO THOSE "COMPLAINTS" WHICH ARE UN-TRUE.<br>
            <https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=AgwH2omenQPCvT0OYOE3Rg==><br>

            ---

            AUTOMATIC CHARGES - THOSE VIDEO.MOV DISTRIBUTIONS WERE ANNEXED IN NYSCEF 153974 2020



            § 250.60 Dissemination of an unlawful surveillance image in the first degree.

             

            A person is guilty of dissemination of an unlawful surveillance image in the first

            degree when:

            1. He or she, with knowledge of the unlawful conduct by which an image or images

            of the sexual or other intimate parts of another person or persons were obtained and

            such unlawful conduct would satisfy the essential elements of the crime of unlawful

            surveillance in the first or second degree, as defined, respectively, in section

            250.50 or 250.45 of this article, sells or publishes such image or images; or

            2. Having created a surveillance image in violation of section 250.45 or 250.50 of

            this article, or in violation of the law in any other jurisdiction which includes

            all of the essential elements of either such crime, or having acted as an accomplice

            to such crime, or acting as an agent to the person who committed such crime, he or

            she intentionally disseminates such unlawfully created image; or

            3. He or she commits the crime of dissemination of an unlawful surveillance image

            in the second degree and has been previously convicted within the past ten years of

            dissemination of an unlawful surveillance image in the first or second degree.

             

            Dissemination of an unlawful surveillance image in the first degree is a class E

            felony.

             
            1 question:
            do you see any other WINDOWS that are being pointed at by ANY CAMERA…
            and also about 3 feet INTO my doorway?

            https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=NvtIUa5jls0V4/OF7/XlGg==
            https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=Lngso0WNLftWLKYEefK/1g==
            https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=Lngso0WNLftWLKYEefK/1g==
            https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=Lngso0WNLftWLKYEefK/1g==
            https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=Lngso0WNLftWLKYEefK/1g==
            https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=bXBaW2kDQDla5S7so80SWQ==
            https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=eBNPxpSr6MPq4D6vZlHhFw==
            https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=afk_PLUS_APpOl2QvqQsHkLKRzQ==
            https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=s4pVOpSOZBIzM2sgaTdRbw==
            https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=XPryqv5meaV7bzTN56trNg==
            https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=7MTKIiZbuHxIsfAB_PLUS_NCbhQ==
            https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=a381V1elefjBsYvNcJNF_PLUS_g==
            https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=vHZxloVck876_PLUS_Ia2LIFPcQ==
            https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=KTL0yzgVgcS6EcWzXNocTQ==
            https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=cve65PXNBCtdxjJFkfwUnw==
            https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=z2F2ttm8P0R5cJjBcSGnfg==
            https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=VSsX7GwaPDSiYc0MUlD5qw==
            https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=rwJsp5trwCp8p5UEfE1zJg==
            https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=fC4jf3UUfVL4Nxd1UZFe7w==
            https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=g3G/uVrDZNeOAh9/cIVZMQ==
            https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=JxfYNYNM64O3GvWBB39vDQ==
            https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=95qV/5SZ/JLyUXzmCTpzrA==
            https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=thOx3vHzDXJ1LG9IEQ962g==
            https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=beoPSi5TWTAsiW/5XVap2w==
            https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=jm1IylJSTPOfy12gVXgMlw==
            https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=VQw/ASQ6kIMGlirWBZM8zA==
            https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=upAzS2FC6bICOGxa73ptdg==
            https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=zXega0sLahw5fVuBTVtpnw==
            https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=UAXjpRh1KO2_PLUS_8KsdF1TuQA==
            https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=yMXQNekW7te0QA5jjAvP2w==
            https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=XkdNmKBghAAqMUItDdrwxA==
            https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=cWLErrXbEw5qtOLVeWU/7g==
            https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=DnmjCPN_PLUS_DIIELjZFua7gWQ==

            …

             

            From: ms60710444266 [mailto:ms60710444266@yahoo.com]
            Sent: Monday, February 07, 2022 1:30 AM
            To: REDACTED
            Cc: 'cweiss@ingramllp.com'; 'MICHAEL CAPOZZI (mcapozzi@ingramllp.com)'; 'MOLLY WEISS'; 'slaskowitz@ingramllp.com'; 'ADMINISTRATION@MSKYLINE.COM (ADMINISTRATION@MSKYLINE.COM)'; 'MANHATTAN SKYLINE, LLC. (ADMINISTRATOR@MSKYLINE.COM)'; anne@thehighlandpartners.com; 'ANDRES REYNOSO (AREYNOSO@mskyline.com)'; 'DONALD ZUCKER (DZUCKER@MSKYLINE.COM)'; 'JOSEPH GIAMBOI (jgiamboi@mskyline.com)'; 'ZUCKER ORGANIZATION (jgiamboi@mskyline.com)'; 'Joseph Giamboi, ESQ (joseph.giamboi@brooklaw.edu)'; 'LATOYA BRITTON (LBRITTON@MSKYLINE.COM)'; 'MSKYLINE BROKER (leftbank@mskylinerentals.com)'; 'LEGAL@MSKYLINE.COM'; 'LEGALASST@MSKYLINE.COM'; 'LZUCKER@MSKYLINE.COM'
            Subject: FW: PLUS... : https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=NvtIUa5jls0V4/OF7/XlGg==
            Importance: High
            Sensitivity: Private

---
## [GwynethLlewelyn/acme.sh](https://github.com/GwynethLlewelyn/acme.sh)@[1bc2cebb0b...](https://github.com/GwynethLlewelyn/acme.sh/commit/1bc2cebb0b4912699d13b36258bc9a9749830eb4)
#### Monday 2022-07-11 21:00:08 by Gwyneth Llewelyn

Docs: add links to TLSA/DANE acronyms

Don't you hate when you get an acronym that you've never heard before, and that everybody assumes that you _should_ know what they're talking about? Well, so do I. A few more links to the meaning of those acronyms are always welcome, I think.
Note to self: this is to try if the push triggers the expected GitHub Action with 'my' DNS configuration...

---
## [hpfr/doom-emacs](https://github.com/hpfr/doom-emacs)@[bb9407e80c...](https://github.com/hpfr/doom-emacs/commit/bb9407e80c3fedc3029520400a4b10bd6bc17b3a)
#### Monday 2022-07-11 21:32:04 by TEC

fix(mu4e): support mu 1.8

Thanks to some combination of ignorance and obstinance, mu4e has thrown
compatibility to the wind and completely ignored the exitance of
define-obsolete-function-alias. Coupled with the inconsistent/partial
function renaming, this has made the mu4e 1.6⟶1.8 change particularly
annoying to deal with.

By suffering the pain of doing the mu4e author's work for them, we can
use defalias to give backwards compatibility a good shot for about 60
functions. Some mu4e~x functions are now mu4e--x, others are unchanged,
and then you've got a few odd changes like mu4e~proc -> mu4e--server and
mu4e-search-rerun. The form of message :from entries has also changed,
and a new (mu4e) entrypoint added supplanting mu4e~start.

Close: #6511
Co-authored-by: Rahguzar <aikrahguzar@gmail.com>

---
## [ShlomiRex/godot-docs](https://github.com/ShlomiRex/godot-docs)@[b872229427...](https://github.com/ShlomiRex/godot-docs/commit/b872229427dddb9b749f46af597e85e25cf2955a)
#### Monday 2022-07-11 21:58:12 by Rémi Verschelde

Remove controversial satirical piece 🔥

This piece was written back in 2014 before open sourcing Godot, and while its
intent is to be sarcastic, it leaves ample room for misinterpretation.

The intended meaning of this piece was, and always has been, the following:

Exploitative game mechanics suck. Games are a beautiful and artful medium
which can provide players with a wide range of experiences: entertainment,
enlightenment, joy, sadness... Games can be just for fun or they can bear
a message. They can connect people with each other or open the player's mind.

Make games worth your players' time and their money, and do your best to do so
while running a successful and respectful business. Hugs <3

---
## [WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/FEDERAL-USE-AND-DISTRIBUTION-ONLY](https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/FEDERAL-USE-AND-DISTRIBUTION-ONLY)@[dc9e3f3c5f...](https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/FEDERAL-USE-AND-DISTRIBUTION-ONLY/commit/dc9e3f3c5fd6a53da2be1001bfef6baef100088e)
#### Monday 2022-07-11 22:16:22 by WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER

https://user-images.githubusercontent.com/108204659/178367794-e3c398b8-1f0a-4686-9e3a-3e927090dfe3.png

https://user-images.githubusercontent.com/108204659/178367794-e3c398b8-1f0a-4686-9e3a-3e927090dfe3.png

 SIGINT (signals intelligence) is information gained by the collection and analysis of the electronic signals and... is distributed internally to as many agencies as they feel necessary on a need to know basis, so once it goes into that system - you never know who's watching you and will continue your life always thinking about that - until you get hit like a 12:58 if you are a criminal, which is commented prominently by the FBI in the examples below, but NOT by any member of the NSA.
    
    
FOR EXAMPLE:    "...this RAP SHEET, sucks... like a glass pipe zucker" ™
SOURCE:     https://www.youtube.com/watch?v=pzhD2MyeIbY&t=1258s

☆ ☆ ☆ ☆ ☆
rap sheet /ˈrap SHēt/ noun    INFORMAL    •NORTH AMERICAN
a criminal record.
ex:     "he had not joined a gang or acquired a rap sheet"
SRC:    https://languages.oup.com/google-dictionary-en

THIS IS WHAT HAPPENS IF IN OUR CURRENT ERA YOU COMMIT, OR COMMITED A FELONY (AKA, A 1212-5858)
    • THE INEVITABLE OCCURS, DEPENDING ON THE SEVEREITY AND FREQUENCY OBSERVED.
    - ESPECIALLY WHEN THE LOCAL AND STATE REGULATORS AWAIT ORDERS IF THEY KNOW AND DON'T UNDERSTAND HOW MANY 12-12-5858s WERE VIOLATED. 
    
    IN FACT, IS THE WAY THE FEDERAL AGENCIES FUNCTION - UNTIL THEY ARE "SATISFIED"\


SO IN THAT CASE, THERE IS NO WIGGLE ROOM FOR A KNOWN LIST OF RECORDS AS SEEN IN THE RAP SHEET IN THE VIDEO ABOVE.... WHEREBY THE COMMENTARY IS STATED NOT AS AN INDICTMENT, BUT A LIST OF CHARGES WHICH CAN BE VERIFIED BY COMMENTARY IN FOR EXAMPLE, AN SEC FILING, OR FOR EXAMPLE, A FILING IN A NEW YORK SUPREME COURT AND THE COMMENTARY AND STATEMENTS THAT ARE ANNEXED AS EXHIBITS CAN CAUSE SERIOUS CONSEQUENCES.

 FOR EXAMPLE, IF THEY HAVE A VIDEO OF SOMEONE WATCHING A VIDEO
- OR HAVE LOGGED SOMEONE WATCHING A MURDER VIDEO "LIEK IN ENEMY OF THE STATE STARRING WILL SMITH" WITHOUT TELLING THE AUTHORITIES, IS SOMETHING THAT IS GENRALLY NOT PERMITTED BY LAW, THE VIOLATION OF THE CRIMINAL CODE AND IF IT WERE FILMED INSIDE OF AN APARTMENT WOULD ALSO VIOLATE OTHER LAWS AS WELL.

[ A FELONY ] --- IRRESPECTIVE OF WHAT FELONY COMMITTED, AND THE INDIVIDUAL, OR INDIVIDUALS ARE LEFT LIKE SOUNDING LIKE THIS SOURCE BELOW, BUT THANKFULLY ARE LEFT TALKING TO THEMSELVES IN A PADDED ROOM LIKE THE LADY IN A YELLOW JUMPSUIT IN A 6 FT BY 8FT METAL ROOM. THIS IS VERY IMPORTANT AS AS IT ALSO ASSISTS TO NOT IMPEDE INTELLIGENT COMMUNICATIONS BY AND BETWEEN INTELLIGENT PEEOPLE.

SOURCE 1: https://youtu.be/pzhD2MyeIbY?t=1928  


SOURCE 2: https://www.youtube.com/watch?v=pzhD2MyeIbY&t=1258s
    
THIS is how FEDERAL AGENTS GENERALLY  ".. MOVE IN..." WHEN THEY FEEL PUBLIC INFORMATION SATISFIES THEIR REQUIREMENTS.

FOR EXAMPLE:    "... President Harry S. Truman officially formed the NSA to perform a specialized discipline known as signals intelligence (SIGINT). SIGINT is intelligence gathering by interception of signals -- either communications between people or through electronic signals not directly used in communication..." SOURCE: https://www.techtarget.com/searchsecurity/definition/National-Security-Agency)
    
    IN THIS VIDEO, THE INDIVIDUALS ARE VERY WELL INTRODUCED, HOWEVER IF THEY IMPEDE COMMUNICATIONS TO A FEDERAL AGENCY ARE NO DIFFERENT THAN THE 1212-5858s as seen in the video in SOURCE 2: https://www.youtube.com/watch?v=pzhD2MyeIbY&t=1258s

THE RAPID TRANSIT AUTHORITY BUILDING HAS FOUR DIGITS THAT ARE PROMIMENTLY REPRESENTED AS FOLLOWS:

IS KNOWN AS MY FAVORITE BUILDING IN MANHATTAN AND BECAUSE THEY KNOW I DON'T MISS A SPOT, EVEN MARKED THIS LOCATION FOR ME, FOR PUBLIC INFORMATION ONLY.
    ☆ ☆ ☆ ☆ ☆
    LOCATION 1:    https://www.youtube.com/watch?v=pzhD2MyeIbY&t=1940
    LOCATION 2:    https://youtu.be/pzhD2MyeIbY?t=1182
    
    AND ALSO, BY THE WAY - ONLY ONE AGENCY.
    Also watch this documentary and look at what happens when you catch a [FELONY] - 
    - they ask only when they need guidance, unless they are already equipped with all the information they need.
    
    HERE IS ANOTHER DOCUMENTARY THAT IS ALSO PUBLISHED - AND COMBINES ALL OF THESE ADVANCED LAWS AND TECHNOLOGY INTO ONE COMPACT VIDEO.


AND DUALLY REPRESENTED AS TWO LCOATIONS WHICH ARE CONFIDENTIAL UNTIL THEY ARE NOT
- JUST LIKE THE NSA, DOESN'T EXIST...
    
SOURCE:    https://www.fbi.gov/video-repository/newss-chasing-the-dragon-the-life-of-an-opiate-addict/file_view 

SOURCE:    https://www.techtarget.com/whatis/definition/SIGINT-signals-intelligence

---
## [josephfrazier/Reported-Web](https://github.com/josephfrazier/Reported-Web)@[0ec59081cc...](https://github.com/josephfrazier/Reported-Web/commit/0ec59081cc2c28999b878521bb2d943f390b5a75)
#### Monday 2022-07-11 23:23:03 by Joseph Frazier

Disable zoom on mobile devices to avoid unescapeable map issue (#346)

This fixes https://github.com/josephfrazier/Reported-Web/issues/344 by
preventing zoom entirely, on mobile devices:

> From https://reportedcab.slack.com/archives/C9VNM3DL4/p1657204889174239?thread_ts=1656783831.210109&cid=C9VNM3DL4:
>
> > > UPDATE: you appear to have fixed #2 by disabling pinching, but this also makes map view crash easily (on my first two tries, once it crashed and sent me back to Reported login, then it crashed and sent me to a Chrome "Can't open this page" (edited)
> >
> >
> > I don't think I've made any changes relating to pinching or the map in at least a year (if you're curious, you can see the list of changes here), so I'm not sure how to explain the difference in behavior you're seeing.
> > That said, I can try to discuss the issue:
> > > (2) map view issue #1: The only ways to get out of map view are (1) click one of the buttons on the bottom, or (2) touch the grayed-out part of the underlying page. If neither of those is visible, you can't get out of map view. This means that if you pinch the map out (expand it), even accidentally, so that the margin around the map itself is no longer visible, there is no way to get out of map view, you have to reload the page (and re-upload your photo or maybe start the whole report over, I can't remember). (You can't pinch it back in if the entire window is full of map.)
> >
> >
> > I'm curious how you were previously able to pinch-zoom the map/page such that neither the buttons or the margin were visible. When I try (on Android), I can either pinch the map, which only zooms the map while leaving the rest of the page alone, or I can pinch the margin, which zooms the entire page, but the margin is still visible because I'm pinching it.
> > Perhaps things behave differently on iOS?
>
> > Actually the map zoom issue is: if you are zoomed out at all when you enter map view (which you often are, especially on an iPad, and you may not realize it), you’re screwed, because you can’t zoom in (in order to see the buttons or margins, the things you have to click in order to get out of map view) if the only things your fingers can touch are the map itself
>
> > ohhh, I see now, and I was able to reproduce that issue. I wonder if there's a way to detect the zoom level, and prompt the user to zoom back out all the way before they can open the map
> > (side note, I think we're using "zoom in" and "zoom out" with opposite meanings. To me "zooming in" makes the things on screen bigger, and "zooming out" makes them smaller)

---

