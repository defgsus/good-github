## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2021-03-25](docs/good-messages/2021/2021-03-25.md)


3,257,513 events, 1,591,449 push events, 2,464,207 commit messages, 181,759,700 characters


## [sergeirocks100/Skyrat-tg@e3b36b1a33...](https://github.com/sergeirocks100/Skyrat-tg/commit/e3b36b1a33017c8deae7a1b8aae0bdc36667513e)
##### 2021-03-25 00:59:20 by SkyratBot

[MIRROR] Moth tourist bots -- They ask for your hat (#4152)

* Moth tourist bots -- They ask for your hat (#57563)

Adds a rare, once per restaurant venue, chance for a moth tourist bot to show up. Asks for the hat, gloves, or shoes you have on.

Closes #57541 if this is merged first, somehow. It includes the testing fix (since I needed to multiply all the weights to allow for rare bots anyway).

Wings are randomized.

I thought it was funny, and it's infrequent enough for the gag to hopefully not lose its magic.

Also a good test bench for the code to allow more dynamic customers. A lot of supporting code was added to make more customizable customers without influencing the surface area of the venue code too much.

Co-authored-by: ATH1909 <42606352+ATH1909@ users.noreply.github.com>

* Moth tourist bots -- They ask for your hat

* Update _customer.dm

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>
Co-authored-by: ATH1909 <42606352+ATH1909@ users.noreply.github.com>
Co-authored-by: Gandalf2k15 <jzo123@hotmail.com>

---
## [bminor/binutils-gdb@08c428aff4...](https://github.com/bminor/binutils-gdb/commit/08c428aff4a793b63c7dd2229ae172879623e3a2)
##### 2021-03-25 01:02:02 by Nick Alcock

libctf: eliminate dtd_u, part 5: structs / unions

Eliminate the dynamic member storage for structs and unions as we have
for other dynamic types.  This is much like the previous enum
elimination, except that structs and unions are the only types for which
a full-sized ctf_type_t might be needed.  Up to now, this decision has
been made in the individual ctf_add_{struct,union}_sized functions and
duplicated in ctf_add_member_offset.  The vlen machinery lets us
simplify this, always allocating a ctf_lmember_t and setting the
dtd_data's ctt_size to CTF_LSIZE_SENT: we figure out whether this is
really justified and (almost always) repack things down into a
ctf_stype_t at ctf_serialize time.

This allows us to eliminate the dynamic member paths from the iterators and
query functions in ctf-types.c in favour of always using the large-structure
vlen stuff for dynamic types (the diff is ugly but that's just because of the
volume of reindentation this calls for).  This also means the large-structure
vlen stuff gets more heavily tested, which is nice because it was an almost
totally unused code path before now (it only kicked in for structures of size
>4GiB, and how often do you see those?)

The only extra complexity here is ctf_add_type.  Back in the days of the
nondeduplicating linker this was called a ridiculous number of times for
countless identical copies of structures: eschewing the repeated lookups of the
dtd in ctf_add_member_offset and adding the members directly saved an amazing
amount of time.  Now the nondeduplicating linker is gone, this is extreme
overoptimization: we can rip out the direct addition and use ctf_member_next and
ctf_add_member_offset, just like ctf_dedup_emit does.

We augment a ctf_add_type test to try adding a self-referential struct, the only
thing the ctf_add_type part of this change really perturbs.

This completes the elimination of dtd_u.

libctf/ChangeLog
2021-03-18  Nick Alcock  <nick.alcock@oracle.com>

	* ctf-impl.h (ctf_dtdef_t) <dtu_members>: Remove.
	<dtd_u>: Likewise.
	(ctf_dmdef_t): Remove.
	(struct ctf_next) <u.ctn_dmd>: Remove.
	* ctf-create.c (INITIAL_VLEN): New, more-or-less arbitrary initial
	vlen size.
	(ctf_add_enum): Use it.
	(ctf_dtd_delete): Do not free the (removed) dmd; remove string
	refs from the vlen on struct deletion.
	(ctf_add_struct_sized): Populate the vlen: do it by hand if
	promoting forwards.  Always populate the full-size
	lsizehi/lsizelo members.
	(ctf_add_union_sized): Likewise.
	(ctf_add_member_offset): Set up the vlen rather than the dmd.
	Expand it as needed, repointing string refs via
	ctf_str_move_pending. Add the member names as pending strings.
	Always populate the full-size lsizehi/lsizelo members.
	(membadd): Remove, folding back into...
	(ctf_add_type_internal): ... here, adding via an ordinary
	ctf_add_struct_sized and _next iteration rather than doing
	everything by hand.
	* ctf-serialize.c (ctf_copy_smembers): Remove this...
	(ctf_copy_lmembers): ... and this...
	(ctf_emit_type_sect): ... folding into here. Figure out if a
	ctf_stype_t is needed here, not in ctf_add_*_sized.
	(ctf_type_sect_size): Figure out the ctf_stype_t stuff the same
	way here.
	* ctf-types.c (ctf_member_next): Remove the dmd path and always
	use the vlen.  Force large-structure usage for dynamic types.
	(ctf_type_align): Likewise.
	(ctf_member_info): Likewise.
	(ctf_type_rvisit): Likewise.
	* testsuite/libctf-regression/type-add-unnamed-struct-ctf.c: Add a
	self-referential type to this test.
	* testsuite/libctf-regression/type-add-unnamed-struct.c: Adjusted
	accordingly.
	* testsuite/libctf-regression/type-add-unnamed-struct.lk: Likewise.

---
## [Aokiare/dracula@5626793282...](https://github.com/Aokiare/dracula/commit/562679328282dc51b373d885f144b4d4d8c2dfbd)
##### 2021-03-25 02:58:47 by aokiare

i fucking hate blurple jesus christ discord is so uglyt  god damn

recolors:D

---
## [fesh0r/mame-full@f2f52b28ff...](https://github.com/fesh0r/mame-full/commit/f2f52b28ff8f23c6778aa516d782a947e5679b66)
##### 2021-03-25 04:14:26 by r09

fmtowns_cd.xml: 13 new dumps, 12 replacements, 5 missing floppies added (#7874)

* Added the missing floppy image to OASYS/Win 2.0 (still not working due to lack of DD floppy support). [cyo.the.vile]
* Replaced the psydet5 and psydetf1 floppy images with cleaner unmodified copies. [cherokee]

New working software list additions (fmtowns_cd.xml)
-----------------------------------
Alice no Yakata 3 (1995-05-16) [redump.org]
Battle [redump.org]
Ehon Writer V1.1 L10 [redump.org]
Half Moon ni Kawaru made - Ramiya Ryou no Nijiiro Tamatebako [redump.org, wiggy2k]
Never Land [redump.org]
Oto to E no Deru Eigo Jisho No. 2 - English in Dream [redump.org]
Populous II - Trials of the Olympian Gods - Expert [redump.org]
Running Girls - Hashiri Onna II + Rance 4.1 / 4.2 Hint Disk [redump.org]
Soreike! Anpanman - Tanoshii Eigo Asobi [redump.org]
Toshiyuki Yoshino - Lullaby of BirdLand [redump.org]
True Heart (alt) [redump.org]
Viper GTS [redump.org]

New not working software list additions (fmtowns_cd.xml)
-----------------------------------
Scavenger 4 (HME-217B) [redump.org]

Replaced software list items (fmtowns_cd.xml)
----------------------------
Hanafuda de Pon! [redump.org]
Indiana Jones and the Fate of Atlantis [redump.org]
King's Quest V - Absence Makes the Heart Go Yonder [redump.org]
Kyan Kyan Collection - Daifugouhen [redump.org]
Kyuukyoku Tiger [redump.org]
Legends of Valour - Gouyuu no Densetsu [redump.org]
Life &amp; Death II - The Brain [redump.org]
Menzoberranzan - Yami no Monshou [redump.org]
Oshiete Noobow [redump.org]
Princess Danger [redump.org]
Scavenger 4 (HME-217A) [redump.org]
Wrestle Angels Special [redump.org]

Software list items promoted to working (fmtowns_cd.xml)
---------------------------------------
Nobunaga no Yabou - Sengoku Gun'yuuden [cherokee]
Windows 3.1 L11 [cyo.the.vile]

---
## [JJawesomeJJ/jjawesome-3d@bc9d6dcf4a...](https://github.com/JJawesomeJJ/jjawesome-3d/commit/bc9d6dcf4aa1c2eec24d1f28b6a2b7e60679c19f)
##### 2021-03-25 05:03:14 by zhaolijie

-water----normal life --
--single life how long will continue
--No mater how sadness of the life remember you are petty unique boy
--fight young man the futher may be darkness but don't be fear,remember the beauty will always wait for you in the some which is not far away --2020-12-15

---
## [home-assistant/home-assistant.io@5ddb6529c1...](https://github.com/home-assistant/home-assistant.io/commit/5ddb6529c13dd4ba8f5aa364b2560740a77bf178)
##### 2021-03-25 09:50:39 by elyobelyob

I found that a 4pm or other non midnight required buffering. (#16182)

* Update history_stats.markdown

---
title: History Stats
description: Instructions about how to integrate historical statistics into Home Assistant.
ha_category:
  - Utility
  - Sensor
ha_iot_class: Local Polling
ha_release: 0.39
ha_quality_scale: internal
ha_domain: history_stats
---

The `history_stats` sensor platform provides quick statistics about another integration or platforms, using data from the [`history`](/integrations/history/) integration.

It can track how long the integration has been in a specific state, in a custom time period.

Examples of what you can track:

- How long you were at home this week
- How long the lights were ON yesterday
- How long you watched TV today

## Configuration

To enable the history statistics sensor, add the following lines to your `configuration.yaml`:

{% raw %}

```yaml
# Example configuration.yaml entry
sensor:
  - platform: history_stats
    name: Lamp ON today
    entity_id: light.my_lamp
    state: 'on'
    type: time
    start: '{{ now().replace(hour=0, minute=0, second=0) }}'
    end: '{{ now() }}'
```

{% endraw %}

{% configuration %}
entity_id:
  description: The entity you want to track.
  required: true
  type: string
state:
  description: The states you want to track.
  required: true
  type: [list, string]
name:
  description: Name displayed on the frontend. Note that it is used by Home Assistant to generate sensor's `object_id` so it is advisable to choose a unique one and change name for frontend using [customization](/docs/configuration/customizing-devices/#friendly_name) or via [Lovelace](/lovelace/entities/#name).
  required: false
  default: unnamed statistics
  type: string
type:
  description: "The type of sensor: `time`, `ratio`, or `count`."
  required: false
  default: time
  type: string
start:
  description: When to start the measure (timestamp or datetime).
  required: false
  type: template
end:
  description: When to stop the measure (timestamp or datetime).
  required: false
  type: template
duration:
  description: Duration of the measure.
  required: false
  type: time
{% endconfiguration %}

<div class='note'>

  You have to provide **exactly 2** of `start`, `end` and `duration`.
<br/>
  You can use [template extensions](/topics/templating/#home-assistant-template-extensions) such as `now()` or `as_timestamp()` to handle dynamic dates, as shown in the examples below.

</div>

## Sensor type

Depending on the sensor type you choose, the `history_stats` integration can show different values:

- **time**: The default value, which is the tracked time, in hours
- **ratio**: The tracked time divided by the length of your period, as a percentage
- **count**: How many times the integration you track was changed to the state you track

## Time periods

The `history_stats` integration will execute a measure within a precise time period. You should always provide 2 of the following :
- When the period starts (`start` variable)
- When the period ends (`end` variable)
- How long is the period (`duration` variable)

As `start` and `end` variables can be either datetimes or timestamps, you can configure almost any period you want.

### Duration

The duration variable is used when the time period is fixed. Different syntaxes for the duration are supported, as shown below.

```yaml
# 6 hours
duration: 06:00
```

```yaml
# 1 minute, 30 seconds
duration: 00:01:30
```

```yaml
# 2 hours and 30 minutes
duration:
  # supports seconds, minutes, hours, days
  hours: 2
  minutes: 30
```

<div class='note'>

  If the duration exceeds the number of days of history stored by the `recorder` component (`purge_keep_days`), the history statistics sensor will not have all the information it needs to look at the entire duration. For example, if `purge_keep_days` is set to 7, a history statistics sensor with a duration of 30 days will only report a value based on the last 7 days of history.

</div>

### Examples

Here are some examples of periods you could work with, and what to write in your `configuration.yaml`:

**Today**: starts at 00:00 of the current day and ends right now.

{% raw %}

```yaml
    start: '{{ now().replace(hour=0, minute=0, second=0) }}'
    end: '{{ now() }}'
```

{% endraw %}

**Yesterday**: ends today at 00:00, lasts 24 hours.

{% raw %}

```yaml
    end: '{{ now().replace(hour=0, minute=0, second=0) }}'
    duration:
      hours: 24
```

{% endraw %}

**This morning (6AM - 11AM)**: starts today at 6, lasts 5 hours.

{% raw %}

```yaml
    start: '{{ now().replace(hour=6, minute=0, second=0) }}'
    duration:
      hours: 5
```

{% endraw %}

**Current week**: starts last Monday at 00:00, ends right now.

Here, last Monday is _today_ as a timestamp, minus 86400 times the current weekday (86400 is the number of seconds in one day, the weekday is 0 on Monday, 6 on Sunday).

{% raw %}

```yaml
    start: '{{ as_timestamp( now().replace(hour=0, minute=0, second=0) ) - now().weekday() * 86400 }}'
    end: '{{ now() }}'
```

{% endraw %}

**Next 4pm **: ends today at 00:00, lasts 30 days. Easy one.

{% raw %}

```yaml
    end: '{{ now().replace(hour=0, minute=0, second=0) }}'
    duration:
      days: 30
```

{% endraw %}

**Last 30 days**: ends today at 00:00, lasts 30 days. Easy one.

{% raw %}

```yaml
    end: '{{ now().replace(hour=0, minute=0, second=0) }}'
    duration:
      days: 30
```

{% endraw %}


** 4PM always in the future**: ends in the future at 16:00, starts 24 hours before.

{% raw %}

```yaml
    end: '{{ (now().replace(minute=0,second=0) + timedelta(hours=8)).replace(hour=16) }}'
    duration:
      hours: 24
```

{% endraw %}

**All your history** starts at timestamp = 0, and ends right now.

{% raw %}

```yaml
    start: '{{ 0 }}'
    end: '{{ now() }}'
```

{% endraw %}

<div class='note'>

  The `/developer-tools/template` page of your Home Assistant UI can help you check if the values for `start`, `end` or `duration` are correct. If you want to check if your period is right, just click on your component, the `from` and `to` attributes will show the start and end of the period, nicely formatted.

</div>

* $pm - 4pm example implemented

* Tweak

* Update source/_integrations/history_stats.markdown

Very happy with this change ...

Co-authored-by: Franck Nijhof <frenck@frenck.nl>

* Update source/_integrations/history_stats.markdown

Co-authored-by: Franck Nijhof <frenck@frenck.nl>

---
## [dloe/TheLastArray@ae6427a2b6...](https://github.com/dloe/TheLastArray/commit/ae6427a2b62034a4df7b6d954bad312218266662)
##### 2021-03-25 15:12:26 by Necko21

god damn it all

Pushing UI changes because im getting bullied and made fun of. My team hates me

---
## [docker/docker.github.io@c6ef1e671d...](https://github.com/docker/docker.github.io/commit/c6ef1e671d637edfac4106988e14a7198317d278)
##### 2021-03-25 16:03:19 by Andrew Grosser

Added important disambiguation to swarm mode (#10987)

* Added important disambiguation to swarm mode

This really needs to be added, I had no idea people gave up on docker/swarm because of a misunderstanding, but it's common enough we need to clarify it.

From Docker's public #swarm slack channel:
```
andrew grosser  4:45 PM
Hey @channel I am about to give a talk in San Francisco to a bunch of devops experts about swarm using my ingress and reverse proxy controller https://github.com/sfproductlabs/roo and one of the organizers said swarm was deprecated, is that so? It's so much easier than kubernetes, I can't imagine losing it.
sfproductlabs/roo
A zero config distributed edge-router & reverse-proxy (supporting multiple letsencrypt/https hosts). No dependencies.
Stars
40
Language
Go
<https://github.com/sfproductlabs/roo|sfproductlabs/roo>sfproductlabs/roo | Apr 9th | Added by GitHub
4:46
Is there something we don't know?
james_wells  4:48 PM
As of the most recent official Docker release, no Swarm is still officially part of Docker...  They merely added native support for Kubernetes
andrew grosser  4:49 PM
:pray: Phew, is there an EOL?
4:49
Thanks @james_wells
4:50
I think they going to get the grenade launchers out if I can't answer these questions
james_wells  4:51 PM
Now that is a good question and my guess is that no, there is no plan to remove it, at least before Docker 3.
andrew grosser  4:52 PM
Amazing thx, I have a system that is a startups dream and is personally saving me more than 10x using swarm, so praying it stays
bmitch:docker:  4:53 PM
Classic container deployed swarm is deprecated (I believe). Swarm mode that's integrated into the engine is still being developed by Mirantis with no EOL set.
4:53
So if someone says swarm is deprecated, make sure to ask "which swarm" they are referring to.
andrew grosser  4:54 PM
Ok thanks @bmitch
4:54
Think that's a brand thing we'll need to help change
james_wells  4:56 PM
@bmitch I am not sure I understand what you are sayin there.  Could you please explain the differences
bmitch:docker:  4:56 PM
See the disambiguation section: https://hub.docker.com/r/dockerswarm/swarm
james_wells  4:57 PM
Excellent.  Thank you sir
andrew grosser  5:02 PM
Thanks
bmitch:docker:  5:02 PM
See also this link where they are getting ready to archive the standalone swarm, aka classic swarm. https://github.com/docker/classicswarm/issues/2985#issuecomment-640486361
justincormackjustincormack
Comment on #2985 Why have all issues been closed?
The vast majority of issues were from 5 years ago when it was being actively developed, and the recent ones were all mistakes for swarmkit, other than some issues I resolved. Many were issues in components or Moby or other software and may be resolved. It is GitHubs (reasonable) recommendation that you close issues and PRs before archiving a repository so that people know they are not being worked on, and I was also looking to see if anyone came forward to say that they were still working on things or, indeed, actively using Swarm Classic.
<https://github.com/docker/classicswarm|docker/classicswarm>docker/classicswarm | Jun 8th | Added by GitHub
james_wells  5:08 PM
That is really unfortunate...  Kubernetes is simply too expensive IMNSHO, Swarm is nice and lightweight.
andrew grosser  5:08 PM
Both the different swarms point to the same point in the documentation in the disambiguation @bmitch
bmitch:docker:  5:09 PM
Swarm mode, aka swarmkit is alive and well.
andrew grosser  5:10 PM
Whoa I can see why they were confused
bmitch:docker:  5:10 PM
If you type docker swarm init you are not running classic swarm
andrew grosser  5:11 PM
Can someone inside docker add this to the swarm docs page? I think it's important
5:12
I think something talking about 2014 was EOLd but this is still current and alive would help.
bmitch:docker:  5:12 PM
Docker themselves isn't maintaining it, that team went to Mirantis, so someone over there would need to submit the PR
andrew grosser  5:12 PM
OK, could I?
bmitch:docker:  5:13 PM
Docs are in GitHub
andrew grosser  5:13 PM
Thanks
```

* Minor edit to the wording to clarify the diff

* Minor update

Co-authored-by: Usha Mandya <47779042+usha-mandya@users.noreply.github.com>

---
## [wincent/liferay-portal@d63caa5140...](https://github.com/wincent/liferay-portal/commit/d63caa5140206e6dbee0091f48ad989c9e8a370f)
##### 2021-03-25 17:28:28 by Greg Hurrell

LPS-127081 Port "render.es.js" to TS

Note this requires some horrible ugly casts for `Liferay`, because
globals are nasty and all that. Figuring out how to declare that as an
ambient type in some central location in the context of project
references is going to be complicated enough, based on my reading of:

    https://github.com/microsoft/TypeScript/issues/29002

that I am going to leave it for a separate commit.

There are a couple of `any` in here too, which I don't like (we've
mostly been able to get away without any `any` at all in
`frontend-js-react-web`) but I want to close up shop for the day so I am
going to commit this and push what I have.

---
## [Aman-Tibrewal/Predictive-Component@af659b9577...](https://github.com/Aman-Tibrewal/Predictive-Component/commit/af659b95772df3eac04dc018d547faed3d88eff0)
##### 2021-03-25 20:38:10 by Aman-Tibrewal

FINAL COMMIT

With 7 Models

Life is better now!

This mess was an interesting experience

Dont revert to the commit 2 steps before this, you'll enjoy the mess though.

---

