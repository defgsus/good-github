## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-06-11](docs/good-messages/2022/2022-06-11.md)


1,470,488 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,470,488 were push events containing 2,119,258 commit messages that amount to 116,970,866 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 25 messages:


## [stemnic/binutils-gdb](https://github.com/stemnic/binutils-gdb)@[80c0a3bf1b...](https://github.com/stemnic/binutils-gdb/commit/80c0a3bf1b949403521d186fc04ed9052ea1d7d4)
#### Saturday 2022-06-11 00:00:06 by Andrew Burgess

gdb/testsuite: remove definition of true/false from gdb_compiler_info

Since pretty much forever the get_compiler_info function has included
these lines:

    # Most compilers will evaluate comparisons and other boolean
    # operations to 0 or 1.
    uplevel \#0 { set true 1 }
    uplevel \#0 { set false 0 }

These define global variables true (to 1) and false (to 0).

It seems odd to me that these globals are defined in
get_compiler_info, I guess maybe the original thinking was that if a
compiler had different true/false values then we would detect it there
and define true/false differently.

I don't think we should be bundling this logic into get_compiler_info,
it seems weird to me that in order to use $true/$false a user needs to
first call get_compiler_info.

It would be better I think if each test script that wants these
variables just defined them itself, if in the future we did need
different true/false values based on compiler version then we'd just
do:

  if { [test_compiler_info "some_pattern"] } {
    # Defined true/false one way...
  } else {
    # Defined true/false another way...
  }

But given the current true/false definitions have been in place since
at least 1999, I suspect this will not be needed any time soon.

Given that the definitions of true/false are so simple, right now my
suggestion is just to define them in each test script that wants
them (there's not that many).  If we ever did need more complex logic
then we can always add a function in gdb.exp that sets up these
globals, but that seems overkill for now.

There should be no change in what is tested after this commit.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[95ffcd4e19...](https://github.com/tgstation/tgstation/commit/95ffcd4e19304af76653ff2b33084092246e4b16)
#### Saturday 2022-06-11 00:02:24 by YakumoChen

Moves the FUCKING LIGHT FIXTURES on tiles with surgery beds (#67644)

Moves around some wall objects in surgery rooms on both Meta and Box, primarily so that there aren't light fixtures on the same tiles as surgery beds. I moved a few unrelated things for QOL.

EVERY MOTHER FUCKING TIME I DO SURGERY I ALWAYS SMASH THE FUCKING LIGHT TUBE BY ACCIDENT AND IT PISSES ME THE FUCK OFF. WHY WOULD YOU PUT A THING THERE THAT JUTS OUT OVER THE FUCKING BED AND GETS IN THE WAY OF CLICKING ON THE SPACEMAN SPRITE FUCK GOD DAMN IT.

---
## [aidanmorgan/morsdle](https://github.com/aidanmorgan/morsdle)@[9b825f300c...](https://github.com/aidanmorgan/morsdle/commit/9b825f300c09ccebc86844a267e98203f79e8a2c)
#### Saturday 2022-06-11 00:19:01 by Aidan Morgan

So it turns out, sitting around in Donnelley River, with absolutely no internet access and reading "Algorithms to Live By" gives you some weird inspiration around the most efficient way to encode and lookup a morse code table given just a memcmp as your instruction.

Well that and a day of drinking the amazing beer at Wild Hop, what can I say.

---
## [awesome-github-repo/Auxio](https://github.com/awesome-github-repo/Auxio)@[d80c49f11f...](https://github.com/awesome-github-repo/Auxio/commit/d80c49f11fac13e5d20ce9bc87c2f6369a30db06)
#### Saturday 2022-06-11 00:30:12 by OxygenCobalt

image: add image group

Add a new view called ImageGroup that will handle all advanced image
hacks from now on.

This includes the indicator (which is now animated), any selection
indicators, and the weirdness of the album song image. All of that
is now handled by ImageGroup. This is the culmination of probably
a day and a half of wrangling with android insanity and having to
remove a lot of what I liked about the indicator in order to make
this work on a basic level.

The only major bug I am currently aware of with this is that the
indicator is bugged out on Lollipop devices due to bad vectors.
Again.

I never want to do this again. I cannot believe that adding a basic
indicator took this long and required so much stupid hacks and
inefficient code. And then google wonders why android apps are so
visually unappealing and janky and laggy. Hm. Must be that devs aren't
using the brand new FooBarBlasterFlow library!

---
## [Tokorizo/Pariah-Station-1](https://github.com/Tokorizo/Pariah-Station-1)@[36209e7774...](https://github.com/Tokorizo/Pariah-Station-1/commit/36209e7774c5a54832c32784099cf59c1f0be158)
#### Saturday 2022-06-11 00:49:39 by FinancialGoose

Fixes conveyor runtime (#65788)

Conveyor would runtime whenever it is right clicked with an item

Fixes #64595 (Runtime on conveyor for right clicking)

fixes a runtime with conveyor where right clicking it with any item would cause a runtime

Mothblocks rant from the issue report below, you've been warned:

Because right-clicking in BYOND is horse-shit. It pipes it all through the normal Click and only tells you it's a right-click through a flag. This means that on anything that isn't prepared, right-clicking is the same as left-clicking, which is terrible UX that only exists in SS13.

Nothing should return ..() from attackby_secondary, because the default is the legacy behavior of making right-click pass as left-click (which I want to kill ASAP, once nothing uses the stupid flags anymore).

Remove else return ..(), and make this whole thing do return SECONDARY_ATTACK_CANCEL_ATTACK_CHAIN.

---
## [exzork/Grasscutter](https://github.com/exzork/Grasscutter)@[fbaeaee4b5...](https://github.com/exzork/Grasscutter/commit/fbaeaee4b5aa82fe10897b60ea642d4428e8abd8)
#### Saturday 2022-06-11 00:53:06 by Kimi

another translation patches because i fucked it up

i hate myself

---
## [tabulon-ext/inxi](https://github.com/tabulon-ext/inxi)@[35e8a95055...](https://github.com/tabulon-ext/inxi/commit/35e8a95055d30a5ed876dc629ab24abc8c87f0a7)
#### Saturday 2022-06-11 10:04:23 by Harald Hope

Rollout of advanced microarchitecture info continues, added AMD/Intel gfx
devices, CPU built dates, process nodes, generation (in some cases, where it
makes sense), etc.

Please note: the 3.3.16 > 17 releases require manual matching table updates. If
you think disk or ram vendor, CPU or GPU process, release date, generation, etc,
information is not correct:

* FIRST: do the research, confirm it's wrong, using wikichips, techpowerup,
wikipedia links, but also be aware, sometimes these slightly contradict each-
other, so research. Don't make me do all your work for you.

* Show the relelevant data, like cpu model/stepping, to correct the issue, or
model name string.

* There are 4 main manually updated matching tables, which use either raw regex
to generate the match based on the model name (ram, disk vendors), or vendor id
matching (ram vendors), product id matching (gpu data), or cpu family / model /
stepping id matching. Each of these has its own matching tool at:
  inxi-perl/tools/[tool-name].pl
which is used to generate either raw data used by the functions (ids for gpu
data), or which contains the master copy of the function used to generate the
regex matches (cp_cpu_arch/set_ram_vendors/set_disk_vendors).

* Please use pinxi and inxi-perl branch for this data, inxi is only released
when next stable is done, all development is done in inxi-perl branch. All
development for the data or functions these tools are made for occurs in the
tools, not in pinxi, and those results are moved into pinxi from the tools.

* Saying something "doesn't work" is not helpful, provide the required data for
the feature that needs updating, or ideally, find the correct answer yourself
and do the research and then provide the updated data for matching.

--------------------------------------------------------------------------------
KNOWN ISSUES:

1. GPU/CPU process node sizes are marketing, not engineering, terms, but
work-around is to list the fab too so you at least know which set of marketing
terms you're dealing with. As of around 7nm, most of the fabs are not using nm
in their names anymore, TSMC is using n7, Intel 7, for example. While these
marketing terms do reflect changes from the previous process node, more
efficient, faster, faster per watt, and so on, and these changes are often quite
significant, 10-30%, or more, they do not reflect the size of the transistor
gate like they used to up until about 350nm. Intel will move to A20 for the node
after 4 or 5, 2nm, meaning 20 angstroms.

Intel suggested million transistors per mm^2 as an objective measure (currently
around 300+ million!! as of ~7nm), but TSMC didn't take them up on it.

GlobalFoundries (GF) stepped away from these ultra small processes at around
14nm, so you won't see GF very often in the data. AMD spun off its chip fabs to
GF aound 2009, so you don't see AMD as foundry after GF was formed. ATI always
used TSMC so GPU data for AMD/ATI is I think all TSMC. Intel has always been its
own foundry.

2. Wayland drops all its data and can't be detected if sudo or su is used to run
inxi. That's unfortunate, but goes along with their dropping support for > 1
user, which was one of the points of wayland, same reason you can do desktop
sharing or ssh desktop forwarding etc. This means inxi doesn't show wayland as
Display protocol, it is just blank, if you use su, or sudo start. This makes
some internal inxi wayland triggers then fail. Still looking to see if there is
a fix or workaround for this.

3. In sensors, a new syntax for k10-pci temp, Tctl, which unfortunately is the
only temp type present for AMD family 17h (zen) and newer cpus, but that is not
an actual cpu temp, it's:
https://www.kernel.org/doc/html/v5.12/hwmon/k10temp.html

"Tctl is the processor temperature control value, used by the platform to
control cooling systems. Tctl is a non-physical temperature on an arbitrary
scale measured in degrees. It does _not_ represent an actual physical
temperature like die or case temperature."

Even worse, it replaced Tdie, which was, correctly, temp1_input, and, somewhat
insanely, the non real cpu temp is now temp1_input, and if present, the real
Tdie cpu temp is temp2_input. I don't know how to work around this problem.

--------------------------------------------------------------------------------
BUGS:

1. Fallback test for Intel cpu arch was not doing anything, used wrong variable
name.

2. A very old bug, thanks mrmazda for spotting this one, runlevel in case of
init 3 > init 5 showed 35, not 5. Doesn't show on systemd stuff often since it
doesn't use runlevels in this way, but this bug has been around a really long
time.

3. SensorItem::gpu_data was always logging its data, missing the if $b_log.

--------------------------------------------------------------------------------
FIXES:

1. Fixed some disk vendor detection rules.

2. Failing to return default target for systemd/systemctl when no:
 /etc/systemd/system/default.target
file exists. Corrected to use systemctl get-default as fallback if file doesn't
exist.

3. Fixed indentation for default: runlevel, should be child of runlevel: /
target:

4. Fixed corner case where systemd has no /proc/1/comm file but is still the
init system. Added fallback check for /run/systemd/units, if that exists, safe
to assume systemd is running init.

5. Fixed subtle case, -h/--recommends/--version/--version-short should not print
to -y1 width, but rather to the original or modified widths >= 80 cols.
Corrected this in print_basic() by using max-cols-basic.

6. Forgot to add --pkg, --edid, and --gpu to debugger run_self() tool.

7. Fixed broken sandisk vendor id.

--------------------------------------------------------------------------------
ENHANCEMENTS:

1. Added AMD and Intel GPU microarchitecture detections for -Gx. These are not
as easy as Nvidia because there is no one reliable data source for product ids.

2. Going with the -Ga process: .. built: item, -Ca will show process: [node] and
built: years and sometimes gen: if available. Geeky, sure, not always perfect,
or correct, but will generally be close. Due to difficultly in finding reliable
release > build end years for example, not all cpus have all this data.

Using CPU generation,where that data is available and makes sense. Like AMD
Zen+ is zen gen: 2, for example,. Because Intel microarch names are often
marketing driven, not engineering, it's too difficult to assign gen consistently
based only on model names. Shows for Core intels like: gen: core 3

That will cover most consumer Intel CPU users currently.

3. Added initial Zen 3+ and Zen 4 ids for cp_cpu_arch(). There is very little
info on these yet, so I'm going on what may prove to be incomplete or wrong
data.

4. Added GPU process, build years for -Ga.

5. Added fallback test for gpus that we don't have product IDs for yet because
dbs have not been updated. Only used for cases where it's the newest gpu series
and no prodoct IDs have been found.

6. Added AMD am386 support to cp_cpu_arch... ok ok, inxi takes 9 minutes to
execute on that, but there you have it.

7. Added unverified Hyprland wayland compositor detection.

8. By request, added --version-short/--vs, which outputs version info in one
line if used together with other options and if not short form. With any normal
line option, will output version (date) info first line, without any other
option, will output 1 line version info and exit.

9. More disk vendors, ids! Much easier with new tool disk_vendors.pl.

--------------------------------------------------------------------------------
CHANGES:

1. Deprecated --nvidia/--nv in favor of more consistent --gpu, that's easier to
work with multiple vendors for advanced gpu architecture. Note for non nvidia,
--gpu only adds codename, if available and different from arch name. For nvidia,
it adds a lot more data.

2. Changed inxi-perl/tools tool names to more clearly reflect what function they
serve.

3. Going with runlevel fixes, changed 'runlevel:' to be 'target:' if systemd.
Also changed incorrect 'target:' for 'default:'.

--------------------------------------------------------------------------------
DOCUMENTATION:

1. Updated man, help, docs/inxi-data.txt for new gpu data and tools, and to
indicate switch to more generic --gpu trigger for advanced gpu data, instead of
the now deprecated --nvidia/--nv, which probably will go down as the shortest
lasting option documented, though of course inxi always keeps legacy syntax
working, behind the scenes, it's just removed from the -h and man page in favor
of --gpu. Also updated to show AMD/Intel/Nvidia now, since the data now roughly
works for all three main gpus.

2. Updated pinxi README.txt to reflect the tools and how to use them and what
they are for.

3. --help, man, updated for target/runlevel, default: changes for init data.

4. Updated configuration html and man for --fake-data-dir.

--------------------------------------------------------------------------------
CODE:

1. Upgraded tools/gpu_ids.pl to handle nvidia, intel, or amd data, added data
files in tools/lists/ for amd. First changed name from ids.pl to gpu_ids.pl

2. New data files added for amd/intel pci ids, and a new tool to merge them and
prep them for gpu_ids.pl -j amd|intel handling. All work. Took a while to get
these things sorted, but don't want to get stuck in future with manual updates,
it needs to be automated as much as possible, same as with disk_vendors.pl etc,
if I'm going to try to maintain this over time.

3. Made all gpu data file names use consistent formats, and made disk data files
also follow this format.

4. Changed raw_ids.pl to gpu_raw.pl, trying to keep things easy to remember and
consistent here.

5. Refactored core gpu data logic, now all types use the same sub, and just
assign various data depending on the type.

6. Changed vendors.pl name to disk_vendors.pl

7. Big redo of array/hash handling in OutputHandler, was partially by reference,
now is completely by reference. All Items now use and return $rows array ref as
well, from start to finish, unlike previously, where @rows was copied
repeatedly.

8. Going along with 7, made most internal passing of hash/arrays use hash/array
references instead, where it makes sense, and doesn't make the code harder to
work with.

9. Refactored WeatherItem, split apart the parts from output to be more like
normal Items in terms of error handling etc.

10. Added 'ref' return option for reader() and grabber(). Only useful for very
large data sets, added also default 'arr' if no value is provided for that
argument.

11. Switched some features to use grabber/reader by ref on the off chance that
will dump some execution time.

12. A few places added qr/.../ precompiled regex, in simple form, for loops,
maybe it helps a little. I don't know.

13. Added global $fake_data_dir, this can be changed via configuration item:
FAKE_DATA_DIR or one time by --fake-data-dir.

14. Created data directory, and initial data items. cpu is the fake data used to
test CPU info. More will be added as data is checked and sanitized.

---
## [FireRedz/kurarin](https://github.com/FireRedz/kurarin)@[d4b47a8e8f...](https://github.com/FireRedz/kurarin/commit/d4b47a8e8f6852b94a978b09118a41ae8018a4ef)
#### Saturday 2022-06-11 10:08:01 by FireRedz

holy fucking shit how did i not notice that (Important)

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[8d88e0c60a...](https://github.com/mrakgr/The-Spiral-Language/commit/8d88e0c60a6041ca023ca93185316cac3a1f5b74)
#### Saturday 2022-06-11 10:35:06 by Marko Grdinić

"10:10am. Let me finish my morning reading and then I will get started.

https://www.bilibilicomics.com/mc480/175541?from=manga_detail

The coloring in Egg of the Elf is something that grows on me the more I read it.

10:35am. Let me start. I've slacked enough.

https://news.ycombinator.com/item?id=31699468
AI Could Defeat All of Us Combined

///

What a limited imagination of how an AI would take over. The scenarios seem to be centered around an extrapolation of "What if a really smart human were trapped inside a computer?" The amount of anthropomorphism is astounding.
The author misses an even scarier prospect - people will want to run such an AI. They will be absolutely giddy at the prospect of running such an AI and it won't be anything like a really smart human trapped in a computer.

AI is already laying the groundwork if you look around today. Every other tweet is a DALL-E[1] image. They are everywhere. DALL-E is increasing its reach while simultaneously signaling that it is an area of research worth pursuing. In effect kicking off the next generation of image generating AIs.

Generation is an apt term. We can utilize the language of organisms with ease. DALL-E lives by way of people invoking it, and reproduces by electro-memeticly - someone else viewing the output and deciding to run DALL-E themselves. It undergoes variation and selection. As new research takes place, and produces new models, they succeed by producing images which further its reproduction, or it doesn't and the model is an evolutionary dead-end.

AI physiologically lives on the cost to run it, and evolves at the rate of research applied. Computational reserves and mindshare are presently fertile new expanses for AI, but what occurs when resources are constrained and inter-AI conflict rises? I expect the result to look similar to competition between parasites for a host - a complex multi-way battle for existence. But no, nothing like a deranged dictator scenario. Leave that for the movies.

1. or variant thereof

///

Yesterday I found this comment to be pretty good so let me highlight it. The article itself does not seem to be worth reading.

I am amazed at how much /ic/ seems to be losing its shit over it.

10:40am. Let me get started. Let me resume the tutorial from yesterday.

https://youtu.be/9Q8PwcDzb8Y?t=2056
How to Make Earth in Blender (Cycles)

https://youtu.be/9Q8PwcDzb8Y?t=2010

Hmmm, I am confused how he gets such diffuse lighting from the sun's reflection.

...Yeah, it does not make sense for the ocean to be a perfect mirror like it is now. At this scale, the waves should act as micro facets. I've cranked up the roughness using a color ramp and now it seems better.

https://stock.adobe.com/search?k=deep+space+hdri

Adobe has a lot HDRIs.

https://www.youtube.com/watch?v=sksfsOSlGkQ
6 FREE SPACE HDRI ENVIRONMENT MAPS

Only one of the images in here would be good for my purpose. The rest have planets and objects in them.

11am. Ah, goddamit. let me import the one I made months ago myself.

https://www.reddit.com/r/blender/comments/hdg44i/360_actual_night_sky_hdri_using_nasa_data/

I want to get NASA's maps, but it site seems to be down.

https://stock.adobe.com/search?k=deep+space+hdri&asset_id=266760651

> Must not be used for merchandise for sale. How annoying.

https://nasa3d.arc.nasa.gov/

Finally, I accessed the NASA site!

11:20am. Just where did andrew find those maps of the Earth? He says it is from NASA, but I can't find it. It is not that easy to find resources. Various sites have stock photos of deep space, and they require a subscription, but I am having surprising trouble just finding something I could get directly. I really will end up using the limbo asset.

https://www.youtube.com/watch?v=GG7aydoWxb0
JOURNEY TO GALAXY CENTER (EPIC ZOOM) IN 4KHDR | MILKY WAY GIGAPIXEL PICTURE.

https://blenderartists.org/t/high-resolution-milky-way-hdri-or-background-image-willing-to-pay/1176021/6

https://www.nasa.gov/multimedia/imagegallery/index.html

Oh finally something good. Those photo sites all want to take a chunk out of my wallet.

https://images.nasa.gov/

https://images.nasa.gov/details-PIA03653

It is not an HDRI though. Well, is that really such a problem. I could always composit it.

https://visibleearth.nasa.gov/images/57747/blue-marble-clouds

He probably got the cloud map from here.

11:40am. This is too much of a hassle. Forget outside resources. I'll just make my own. For now let me use the limbo HDRI.

The stars are too big. I'll definitely have to work on my own, but nevermind that for now. I'll procedurally generate something else later.

https://youtu.be/9Q8PwcDzb8Y?t=2277

Hmmm, do you not need the cryptomatte to get the object index. There is even a normal pass. Remember when I was looking for a way to get the camera normal. This could be it. Though it might be the world normals.

11:50am. You know what, I am an idiot. I do not need a HDRI. I can just use a plane and put an regular image on it. It is not like I am going to be rotating around the space. In that case, who cares.

Still, finding something I can use commercially without paying is a challenge. I should procedurally generate the env texture.

12pm. Sigh, it is so annoying to do the nebulae. I forgot how much time procedural texture generation can take. I absolutely must use a photo.

I did the stars, but when I rotate I get weird effects.

https://mymodernmet.com/nasa-photos-online/
NASA Lets You Download Thousands of High-Resolution Space Images for Free

I am just going to composit this thing. I am absolutely on the wrong track if I say I want to make my space procedurally.

https://images.nasa.gov/details-PIA12348

Let me go with this. This is beautiful.

Hmmm, is this really not an HDRI. It does look like one based on the distortion near the bottom.

Nope, it is definitely not an HDRI. The sides don't even mirror correctly. And and the top and bottom there is huge distortion. It does not matter. My aiming for an illustration makes things a lot easier. 3d offers a lot to a 2d artist.

I think it is finally time I get familiar with compositing.

12:20pm. What happened now is what happens when you know about something, but haven't fully ingrained it. It is really obvious that I should be compositing, but I am getting hung up on trying to get a HDRI.

https://youtu.be/a1weKAFJx3k
Demystifying Blender Cycles' Render Passes: Normal Pass

I should get familiar with passes. I am really wondering what the object index is. I'll try putting a few cubes into the scene just to see what comes out.

12:20pm. Hmmm, object index shows nothing. The normal pass shows the, well not the camera normals, but the object normals. It is pretty useless. But I should figure out how the object index works.

12:30pm. For an updated workflow I could just try using the cryptomattes, but I want to see what he does.

Yeah, this is the right way. I should just use the images from NASA as they are free, or other free photos and composit them. That is what I need to focus on. If I start getting anxious about HDRIs or even worse, try to do them procedurally I am going to be here for a long time. Rather than doing them procedurally, even just painting the nebulae on CSP would be better as I'll be able to make steady progress instead of fiddling with noise. But that would still take too much time, I'd need to dedicate at least a few days to do it.

The reason pros are fast is because they use assets, not because they can do everything on their own much quicker than the others. I need to focus on that.

Let me have breakfast here."

---
## [CavenderHub/CavenderHub](https://github.com/CavenderHub/CavenderHub)@[5ff3f4cacb...](https://github.com/CavenderHub/CavenderHub/commit/5ff3f4cacbbdc7d4b901a9e0432794714502d17d)
#### Saturday 2022-06-11 11:52:06 by CavenderHub

CAVENDERHUB 

game:GetService("StarterGui"):SetCore("SendNotification", 		{ 			Title = "1XLII HUB", 			Text = "Load : 1XLII HUB", 			Icon = "", 		} ) wait(2) game:GetService("StarterGui"):SetCore("SendNotification", 		{ 			Title = "1XLII HUB", 			Text = "Load : BLOX FRUIT", 			Icon = "", 		} ) wait(2) game:GetService("StarterGui"):SetCore("SendNotification", 		{ 			Title = "1XLII HUB", 			Text = "loading.....", 			Icon = "", 		} ) wait(3) Old_World = false New_World = false Three_World = false local placeId = game.PlaceId if placeId == 2753915549 then Old_World = true elseif placeId == 4442272183 then New_World = true elseif placeId == 7449423635 then 	Three_World = true end local DINOHUB = Instance.new("ScreenGui") local OPENCLOSE = Instance.new("TextButton") DINOHUB.Name = "DINOHUB" DINOHUB.Parent = game.CoreGui DINOHUB.ZIndexBehavior = Enum.ZIndexBehavior.Sibling OPENCLOSE.Name = "OPENCLOSE" OPENCLOSE.Parent = DINOHUB OPENCLOSE.BackgroundColor3 = Color3.fromRGB(20, 20, 20) OPENCLOSE.BorderSizePixel = 0 OPENCLOSE.Position = UDim2.new(0.120833337, 0, 0.0952890813, 0) OPENCLOSE.Size = UDim2.new(0.0447916649, 0, 0.0845824406, 0) OPENCLOSE.Font = Enum.Font.DenkOne OPENCLOSE.Text = "1xliihub" OPENCLOSE.TextColor3 = Color3.fromRGB(96, 255, 16) OPENCLOSE.TextScaled = true OPENCLOSE.TextSize = 14.000 OPENCLOSE.TextWrapped = true OPENCLOSE.MouseButton1Click:Connect(function() game.CoreGui:FindFirstChild("1xliiUI").Enabled = not game.CoreGui:FindFirstChild("1xliiUI").Enabled end) do if game:GetService("CoreGui"):FindFirstChild("1xliiUI") then game:GetService("CoreGui").DinoUI:Destroy() end end game:GetService("Players").LocalPlayer.Idled:connect(function() game:GetService("VirtualUser"):Button2Down(Vector2.new(0,0),workspace.CurrentCamera.CFrame) wait(1) game:GetService("VirtualUser"):Button2Up(Vector2.new(0,0),workspace.CurrentCamera.CFrame) end) _G.Color = Color3.fromRGB(16,255,24) if not game:IsLoaded() then repeat game.Loaded:Wait() until game:IsLoaded() end repeat wait() until game:GetService("Players") if not game:GetService("Players").LocalPlayer.Character:FindFirstChild("HumanoidRootPart") then repeat wait() until game:GetService("Players").LocalPlayer.Character:FindFirstChild("HumanoidRootPart") end wait(1) do local ui = game.CoreGui:FindFirstChild("1xliiUI") if ui then ui:Destroy() end end local UserInputService = game:GetService("UserInputService") local TweenService = game:GetService("TweenService") local function MakeDraggable(topbarobject, object) local Dragging = nil local DragInput = nil local DragStart = nil local StartPosition = nil local function Update(input) local Delta = input.Position - DragStart local pos = UDim2.new( StartPosition.X.Scale, StartPosition.X.Offset + Delta.X, StartPosition.Y.Scale, StartPosition.Y.Offset + Delta.Y ) local Tween = TweenService:Create(object, TweenInfo.new(0.2), {Position = pos}) Tween:Play() end topbarobject.InputBegan:Connect( function(input) if input.UserInputType == Enum.UserInputType.MouseButton1 or input.UserInputType == Enum.UserInputType.Touch then Dragging = true DragStart = input.Position StartPosition = object.Position input.Changed:Connect( function() if input.UserInputState == Enum.UserInputState.End then Dragging = false end end ) end end ) topbarobject.InputChanged:Connect( function(input) if input.UserInputType == Enum.UserInputType.MouseMovement or input.UserInputType == Enum.UserInputType.Touch then DragInput = input end end ) UserInputService.InputChanged:Connect( function(input) if input == DragInput and Dragging then Update(input) end end ) end local library = {} function library:AddWindow(text,keybind) local bind = keybind or Enum.KeyCode.RightControl local ff = false local currenttab = "" local DoctorShiba = Instance.new("ScreenGui") DoctorShiba.Name = "1xliiUI" DoctorShiba.Parent = game.CoreGui DoctorShiba.ZIndexBehavior = Enum.ZIndexBehavior.Sibling local Main = Instance.new("Frame") Main.Name = "Main" Main.Parent = DoctorShiba Main.AnchorPoint = Vector2.new(0.5, 0.5) Main.BackgroundColor3 = Color3.fromRGB(30, 28, 39) Main.BackgroundTransparency = 0.100 Main.BorderSizePixel = 0 Main.ClipsDescendants = true Main.Position = UDim2.new(0.499526083, 0, 0.499241292, 0) Main.Size = UDim2.new(0, 600, 0, 350) local Top = Instance.new("Frame") Top.Name = "Top" Top.Parent = Main Top.BackgroundColor3 = Color3.fromRGB(255, 255, 255) Top.BackgroundTransparency = 1.000 Top.BorderSizePixel = 0 Top.Size = UDim2.new(0, 600, 0, 20) local Page = Instance.new("Frame") Page.Name = "Page" Page.Parent = Main Page.BackgroundColor3 = Color3.fromRGB(25, 23, 35) Page.BackgroundTransparency = 0.100 Page.BorderSizePixel = 0 Page.Size = UDim2.new(0, 125, 0, 350) local NameHub = Instance.new("TextLabel") NameHub.Name = "NameHub" NameHub.Parent = Page NameHub.BackgroundColor3 = Color3.fromRGB(255, 255, 255) NameHub.BackgroundTransparency = 1.000 NameHub.Position = UDim2.new(0.113333493, 0, 0, 0) NameHub.Size = UDim2.new(0, 110, 0, 20) NameHub.Font = Enum.Font.GothamSemibold NameHub.Text = text NameHub.TextColor3 = Color3.fromRGB(16,255,24) NameHub.TextSize = 11.000 NameHub.TextXAlignment = Enum.TextXAlignment.Left local User = Instance.new("Frame") User.Name = "User" User.Parent = Page User.BackgroundColor3 = Color3.fromRGB(255, 255, 255) User.BackgroundTransparency = 1.000 User.Position = UDim2.new(0, 0, 0.8, 30) User.Size = UDim2.new(0, 125, 0, 40) local UserText = Instance.new("TextLabel") UserText.Name = "UserText" UserText.Parent = User UserText.BackgroundColor3 = Color3.fromRGB(255, 255, 255) UserText.BackgroundTransparency = 1.000 UserText.Position = UDim2.new(0.354999989, 0, 0, 11) UserText.Size = UDim2.new(0, 80, 0, 20) UserText.Font = Enum.Font.Gotham UserText.Text = tostring(game.Players.LocalPlayer.Name) spawn(function() while wait() do pcall(function() wait(0.1) game:GetService('TweenService'):Create( UserText,TweenInfo.new(1,Enum.EasingStyle.Linear,Enum.EasingDirection.InOut), {TextColor3 = Color3.fromRGB(255, 0, 0)} ):Play() wait(.5) game:GetService('TweenService'):Create( UserText,TweenInfo.new(1,Enum.EasingStyle.Linear,Enum.EasingDirection.InOut), {TextColor3 = Color3.fromRGB(255, 155, 0)} ):Play() wait(.5) game:GetService('TweenService'):Create( UserText,TweenInfo.new(1,Enum.EasingStyle.Linear,Enum.EasingDirection.InOut), {TextColor3 = Color3.fromRGB(255, 255, 0)} ):Play() wait(.5) game:GetService('TweenService'):Create( UserText,TweenInfo.new(1,Enum.EasingStyle.Linear,Enum.EasingDirection.InOut), {TextColor3 = Color3.fromRGB(0, 255, 0)} ):Play() wait(.5) game:GetService('TweenService'):Create( UserText,TweenInfo.new(1,Enum.EasingStyle.Linear,Enum.EasingDirection.InOut), {TextColor3 = Color3.fromRGB(0, 255, 255)} ):Play() wait(.5) game:GetService('TweenService'):Create( UserText,TweenInfo.new(1,Enum.EasingStyle.Linear,Enum.EasingDirection.InOut), {TextColor3 = Color3.fromRGB(0, 155, 255)} ):Play() wait(.5) game:GetService('TweenService'):Create( UserText,TweenInfo.new(1,Enum.EasingStyle.Linear,Enum.EasingDirection.InOut), {TextColor3 = Color3.fromRGB(255, 0, 255)} ):Play() wait(.5) game:GetService('TweenService'):Create( UserText,TweenInfo.new(1,Enum.EasingStyle.Linear,Enum.EasingDirection.InOut), {TextColor3 = Color3.fromRGB(255, 0, 155)} ):Play() wait(.5) end) end end) UserText.TextScaled = true UserText.TextSize = 11.000 UserText.TextWrapped = true UserText.TextXAlignment = Enum.TextXAlignment.Left local UITextSizeConstraint = Instance.new("UITextSizeConstraint") UITextSizeConstraint.Parent = UserText UITextSizeConstraint.MaxTextSize = 11 local UserImage = Instance.new("ImageLabel") UserImage.Name = "UserImage" UserImage.Parent = User UserImage.BackgroundColor3 = Color3.fromRGB(225, 225, 225) UserImage.Position = UDim2.new(0, 10, 0, 9) UserImage.Size = UDim2.new(0, 25, 0, 25) UserImage.Image = "https://www.roblox.com/headshot-thumbnail/image?userId="..game.Players.LocalPlayer.UserId.."&width=420&height=420&format=png" local UserImageCorner = Instance.new("UICorner") UserImageCorner.CornerRadius = UDim.new(0, 100) UserImageCorner.Name = "UserImageCorner" UserImageCorner.Parent = UserImage local ScrollPage = Instance.new("ScrollingFrame") ScrollPage.Name = "ScrollPage" ScrollPage.Parent = Page ScrollPage.Active = true ScrollPage.BackgroundColor3 = Color3.fromRGB(255, 255, 255) ScrollPage.BackgroundTransparency = 1.000 ScrollPage.BorderSizePixel = 0 ScrollPage.Position = UDim2.new(0, 0, 0.086, 0) ScrollPage.Size = UDim2.new(0, 125, 0, 290) ScrollPage.CanvasSize = UDim2.new(0, 0, 0, 0) ScrollPage.ScrollBarThickness = 0 local PageList = Instance.new("UIListLayout") PageList.Name = "PageList" PageList.Parent = ScrollPage PageList.SortOrder = Enum.SortOrder.LayoutOrder PageList.Padding = UDim.new(0, 7) local PagePadding = Instance.new("UIPadding") PagePadding.Name = "PagePadding" PagePadding.Parent = ScrollPage PagePadding.PaddingTop = UDim.new(0, 5) PagePadding.PaddingLeft = UDim.new(0, 28) local TabFolder = Instance.new("Folder") TabFolder.Name = "TabFolder" TabFolder.Parent = Main MakeDraggable(Top,Main) local uihide = false UserInputService.InputBegan:Connect(function(input) if input.KeyCode == bind then if uihide == false then uihide = true Main:TweenSize(UDim2.new(0, 0, 0, 0),"In","Quad",0.2,true) else uihide = false Main:TweenSize(UDim2.new(0, 600, 0, 350),"Out","Quad",0.2,true) end end end) local uitab = {} function uitab:AddTab(text,image) local Image = image or 6023426915 local PageButton = Instance.new("TextButton") PageButton.Name = "PageButton" PageButton.Parent = ScrollPage PageButton.BackgroundColor3 = Color3.fromRGB(255, 255, 255) PageButton.BackgroundTransparency = 1.000 PageButton.BorderSizePixel = 0 PageButton.Position = UDim2.new(0.224000007, 0, 0.029787235, 0) PageButton.Size = UDim2.new(0, 97, 0, 20) PageButton.AutoButtonColor = false PageButton.Font = Enum.Font.GothamSemibold PageButton.Text = text PageButton.TextColor3 = Color3.fromRGB(225, 225, 225) PageButton.TextSize = 11.000 PageButton.TextXAlignment = Enum.TextXAlignment.Left local PageImage = Instance.new("ImageLabel") PageImage.Name = "PageImage" PageImage.Parent = PageButton PageImage.BackgroundColor3 = Color3.fromRGB(255, 255, 255) PageImage.BackgroundTransparency = 1.000 PageImage.Position = UDim2.new(0, -20, 0, 3) PageImage.Size = UDim2.new(0, 15, 0, 15) PageImage.Image = "rbxassetid://"..tostring(Image) local MainTab = Instance.new("Frame") MainTab.Name = "MainTab" MainTab.Parent = TabFolder MainTab.BackgroundColor3 = Color3.fromRGB(30, 28, 39) MainTab.BorderSizePixel = 0 MainTab.Position = UDim2.new(0.208333328, 0, 0, 0) MainTab.Size = UDim2.new(0, 475, 0, 350) MainTab.Visible = false local ScrollTab = Instance.new("ScrollingFrame") ScrollTab.Name = "ScrollTab" ScrollTab.Parent = MainTab ScrollTab.BackgroundColor3 = Color3.fromRGB(255, 255, 255) ScrollTab.BackgroundTransparency = 1.000 ScrollTab.BorderSizePixel = 0 ScrollTab.Position = UDim2.new(0, 0, 0.057, 0) ScrollTab.Size = UDim2.new(0, 475, 0, 330) ScrollTab.CanvasSize = UDim2.new(0, 0, 0, 0) ScrollTab.ScrollBarThickness = 3 local TabList = Instance.new("UIListLayout") TabList.Name = "TabList" TabList.Parent = ScrollTab TabList.SortOrder = Enum.SortOrder.LayoutOrder TabList.Padding = UDim.new(0, 5) local TabPadding = Instance.new("UIPadding") TabPadding.Name = "TabPadding" TabPadding.Parent = ScrollTab TabPadding.PaddingLeft = UDim.new(0, 10) TabPadding.PaddingTop = UDim.new(0, 10) PageButton.MouseButton1Click:Connect(function() currenttab = MainTab.Name for i,v in next, TabFolder:GetChildren() do if v.Name == "MainTab" then v.Visible = false end end MainTab.Visible = true for i,v in next, ScrollPage:GetChildren() do if v:IsA("TextButton") then TweenService:Create( v, TweenInfo.new(0.3,Enum.EasingStyle.Quad,Enum.EasingDirection.Out), {TextColor3 = Color3.fromRGB(225, 225, 225)} ):Play() end TweenService:Create( PageButton, TweenInfo.new(0.3,Enum.EasingStyle.Quad,Enum.EasingDirection.Out), {TextColor3 = Color3.fromRGB(16,255,24)} ):Play() end end) if ff == false then TweenService:Create( PageButton, TweenInfo.new(0.3,Enum.EasingStyle.Quad,Enum.EasingDirection.Out), {TextColor3 = Color3.fromRGB(16,255,24)} ):Play() for i,v in next, TabFolder:GetChildren() do if v.Name == "MainTab" then v.Visible = false end MainTab.Visible = true end ff = true end game:GetService("RunService").Stepped:Connect(function() pcall(function() ScrollPage.CanvasSize = UDim2.new(0,0,0,PageList.AbsoluteContentSize.Y + 10) ScrollTab.CanvasSize = UDim2.new(0,0,0,TabList.AbsoluteContentSize.Y + 30) end) end) local main = {} function main:Button(text,callback) local Button = Instance.new("TextButton") Button.Name = "Button" Button.Parent = ScrollTab Button.BackgroundColor3 = Color3.fromRGB(50, 48, 59) Button.BackgroundTransparency = 0.1 Button.BorderSizePixel = 0 Button.Size = UDim2.new(0, 455, 0, 30) Button.AutoButtonColor = false Button.Font = Enum.Font.Gotham Button.Text = text Button.TextColor3 = Color3.fromRGB(225, 225, 225) Button.TextSize = 11.000 Button.TextWrapped = true local ButtonCorner = Instance.new("UICorner") ButtonCorner.Name = "ButtonCorner" ButtonCorner.CornerRadius = UDim.new(0, 5) ButtonCorner.Parent = Button Button.MouseEnter:Connect(function() TweenService:Create( Button, TweenInfo.new(0.4,Enum.EasingStyle.Quad,Enum.EasingDirection.Out), {TextColor3 = Color3.fromRGB(16,255,24)} ):Play() end) Button.MouseLeave:Connect(function() TweenService:Create( Button, TweenInfo.new(0.4,Enum.EasingStyle.Quad,Enum.EasingDirection.Out), {TextColor3 = Color3.fromRGB(225, 225, 225)} ):Play() end) Button.MouseButton1Click:Connect(function() callback() Button.TextSize = 0 TweenService:Create( Button, TweenInfo.new(0.4,Enum.EasingStyle.Back,Enum.EasingDirection.Out), {TextSize = 11} ):Play() end) end function main:Toggle(text,config,callback) local ToggleImage = Instance.new("Frame") local Toggle = Instance.new("TextButton") Toggle.Name = "Toggle" Toggle.Parent = ScrollTab Toggle.BackgroundColor3 = Color3.fromRGB(50, 48, 59) Toggle.BackgroundTransparency = 0.1 Toggle.BorderSizePixel = 0 Toggle.AutoButtonColor = false Toggle.Size = UDim2.new(0, 455, 0, 30) Toggle.Font = Enum.Font.SourceSans Toggle.Text = "" Toggle.TextColor3 = Color3.fromRGB(0, 0, 0) Toggle.TextSize = 14.000 local ToggleCorner = Instance.new("UICorner") ToggleCorner.Name = "ToggleCorner" ToggleCorner.CornerRadius = UDim.new(0, 5) ToggleCorner.Parent = Toggle local ToggleLabel = Instance.new("TextLabel") ToggleLabel.Name = "ToggleLabel" ToggleLabel.Parent = Toggle ToggleLabel.BackgroundColor3 = Color3.fromRGB(255, 255, 255) ToggleLabel.BackgroundTransparency = 1.000 ToggleLabel.Position = UDim2.new(0, 13, 0, 0) ToggleLabel.Size = UDim2.new(0, 410, 0, 30) ToggleLabel.Font = Enum.Font.Gotham ToggleLabel.Text = text ToggleLabel.TextColor3 = Color3.fromRGB(225, 225, 225) ToggleLabel.TextSize = 11.000 ToggleLabel.TextXAlignment = Enum.TextXAlignment.Left ToggleImage.Name = "ToggleImage" ToggleImage.Parent = Toggle ToggleImage.BackgroundColor3 = Color3.fromRGB(70, 68, 79) ToggleImage.Position = UDim2.new(0, 425, 0, 5) ToggleImage.BorderSizePixel = 0 ToggleImage.Size = UDim2.new(0, 20, 0, 20) local ToggleImageCorner = Instance.new("UICorner") ToggleImageCorner.Name = "ToggleImageCorner" ToggleImageCorner.CornerRadius = UDim.new(0, 5) ToggleImageCorner.Parent = ToggleImage local ToggleImage2 = Instance.new("Frame") ToggleImage2.Name = "ToggleImage2" ToggleImage2.Parent = ToggleImage ToggleImage2.AnchorPoint = Vector2.new(0.5, 0.5) ToggleImage2.BackgroundColor3 = Color3.fromRGB(16,255,24) ToggleImage2.Position = UDim2.new(0, 10, 0, 10) ToggleImage2.Visible = false local ToggleImage2Corner = Instance.new("UICorner") ToggleImage2Corner.Name = "ToggleImageCorner" ToggleImage2Corner.CornerRadius = UDim.new(0, 5) ToggleImage2Corner.Parent = ToggleImage2 Toggle.MouseEnter:Connect(function() TweenService:Create( ToggleLabel, TweenInfo.new(0.4,Enum.EasingStyle.Quad,Enum.EasingDirection.Out), {TextColor3 = Color3.fromRGB(16,255,24)} ):Play() end) Toggle.MouseLeave:Connect(function() TweenService:Create( ToggleLabel, TweenInfo.new(0.4,Enum.EasingStyle.Quad,Enum.EasingDirection.Out), {TextColor3 = Color3.fromRGB(225, 225, 225)} ):Play() end) if config == nil then config = false end local toggled = config or false Toggle.MouseButton1Click:Connect(function() if toggled == false then toggled = true ToggleImage2.Visible = true ToggleImage2:TweenSize(UDim2.new(0, 21, 0, 21),"In","Quad",0.1,true) else toggled = false ToggleImage2:TweenSize(UDim2.new(0, 0, 0, 0),"In","Quad",0.1,true) wait(0.1) ToggleImage2.Visible = false end callback(toggled) end) if config == true then ToggleImage2.Visible = true ToggleImage2:TweenSize(UDim2.new(0, 21, 0, 21),"In","Quad",0.1,true) toggled = true callback(toggled) end end function main:Textbox(text,holder,disappear,callback) local Textboxx = Instance.new("Frame") local TextboxxCorner = Instance.new("UICorner") local TextboxTitle = Instance.new("TextLabel") local Textbox = Instance.new("TextBox") local TextboxCorner = Instance.new("UICorner") Textboxx.Name = "Textboxx" Textboxx.Parent = ScrollTab Textboxx.BackgroundColor3 = Color3.fromRGB(50, 48, 59) Textboxx.Size = UDim2.new(0, 455, 0, 30) TextboxxCorner.CornerRadius = UDim.new(0, 5) TextboxxCorner.Name = "TextboxxCorner" TextboxxCorner.Parent = Textboxx TextboxTitle.Name = "TextboxTitle" TextboxTitle.Parent = Textboxx TextboxTitle.BackgroundColor3 = Color3.fromRGB(255, 255, 255) TextboxTitle.BackgroundTransparency = 1.000 TextboxTitle.Position = UDim2.new(0, 15, 0, 0) TextboxTitle.Size = UDim2.new(0, 300, 0, 30) TextboxTitle.Font = Enum.Font.Gotham TextboxTitle.Text = text TextboxTitle.TextColor3 = Color3.fromRGB(225, 225, 225) TextboxTitle.TextSize = 11.000 TextboxTitle.TextXAlignment = Enum.TextXAlignment.Left Textbox.Name = "Textbox" Textbox.Parent = Textboxx Textbox.BackgroundColor3 = Color3.fromRGB(30, 28, 39) Textbox.Position = UDim2.new(0, 310, 0, 5) Textbox.Size = UDim2.new(0, 140, 0, 20) Textbox.Font = Enum.Font.Gotham Textbox.Text = holder Textbox.TextColor3 = Color3.fromRGB(225, 225, 225) Textbox.TextSize = 11.000 Textbox.FocusLost:Connect(function() if #Textbox.Text > 0 then callback(Textbox.Text) end if disappear then Textbox.Text = "" else Textbox.Text = holder end end) TextboxCorner.Name = "TextboxCorner" TextboxCorner.CornerRadius = UDim.new(0, 5) TextboxCorner.Parent = Textbox end function main:Dropdown(text,table,callback) local Dropdown = Instance.new("Frame") local UICorner = Instance.new("UICorner") local DropButton = Instance.new("TextButton") local Droptitle = Instance.new("TextLabel") local DropScroll = Instance.new("ScrollingFrame") local DropdownList = Instance.new("UIListLayout") local DropdownPadding = Instance.new("UIPadding") local DropImage = Instance.new("ImageLabel") Dropdown.Name = "Dropdown" Dropdown.Parent = ScrollTab Dropdown.Active = true Dropdown.BackgroundColor3 = Color3.fromRGB(50, 48, 59) Dropdown.ClipsDescendants = true Dropdown.Size = UDim2.new(0, 455, 0, 30) UICorner.CornerRadius = UDim.new(0, 5) UICorner.Parent = Dropdown DropButton.Name = "DropButton" DropButton.Parent = Dropdown DropButton.BackgroundColor3 = Color3.fromRGB(255, 255, 255) DropButton.BackgroundTransparency = 1.000 DropButton.Size = UDim2.new(0, 455, 0, 30) DropButton.Font = Enum.Font.SourceSans DropButton.Text = "" DropButton.TextColor3 = Color3.fromRGB(0, 0, 0) DropButton.TextSize = 14.000 Droptitle.Name = "Droptitle" Droptitle.Parent = Dropdown Droptitle.BackgroundColor3 = Color3.fromRGB(255, 255, 255) Droptitle.BackgroundTransparency = 1.000 Droptitle.Position = UDim2.new(0.0281690136, 0, 0, 0) Droptitle.Size = UDim2.new(0, 410, 0, 30) Droptitle.Font = Enum.Font.Gotham Droptitle.Text = text.." : " Droptitle.TextColor3 = Color3.fromRGB(225, 225, 225) Droptitle.TextSize = 11.000 Droptitle.TextXAlignment = Enum.TextXAlignment.Left DropImage.Name = "DropImage" DropImage.Parent = Dropdown DropImage.BackgroundColor3 = Color3.fromRGB(255, 255, 255) DropImage.BackgroundTransparency = 1.000 DropImage.Position = UDim2.new(0, 425, 0, 5) DropImage.Rotation = 0 DropImage.Size = UDim2.new(0, 20, 0, 20) DropImage.Image = "rbxassetid://5012539403" DropScroll.Name = "DropScroll" DropScroll.Parent = Droptitle DropScroll.Active = true DropScroll.BackgroundColor3 = Color3.fromRGB(255, 255, 255) DropScroll.BackgroundTransparency = 1.000 DropScroll.BorderSizePixel = 0 DropScroll.Position = UDim2.new(-0.0317460336, 0, 1, 0) DropScroll.Size = UDim2.new(0, 455, 0, 70) DropScroll.CanvasSize = UDim2.new(0, 0, 0, 2) DropScroll.ScrollBarThickness = 2 DropdownList.Name = "DropdownList" DropdownList.Parent = DropScroll DropdownList.SortOrder = Enum.SortOrder.LayoutOrder DropdownList.Padding = UDim.new(0, 5) DropdownPadding.Name = "DropdownPadding" DropdownPadding.Parent = DropScroll DropdownPadding.PaddingTop = UDim.new(0, 5) local isdropping = false for i,v in next,table do local DropButton2 = Instance.new("TextButton") DropButton2.Name = "DropButton2" DropButton2.Parent = DropScroll DropButton2.BackgroundColor3 = Color3.fromRGB(255, 255, 255) DropButton2.BackgroundTransparency = 1.000 DropButton2.Size = UDim2.new(0, 455, 0, 30) DropButton2.AutoButtonColor = false DropButton2.Font = Enum.Font.Gotham DropButton2.TextColor3 = Color3.fromRGB(225, 225, 225) DropButton2.TextSize = 11.000 DropButton2.Text = tostring(v) DropButton2.MouseEnter:Connect(function() TweenService:Create( DropButton2, TweenInfo.new(0.2, Enum.EasingStyle.Quad, Enum.EasingDirection.Out), {TextColor3 = Color3.fromRGB(16,255,24)} ):Play() end) DropButton2.MouseLeave:Connect(function() TweenService:Create( DropButton2, TweenInfo.new(0.2, Enum.EasingStyle.Quad, Enum.EasingDirection.Out), {TextColor3 = Color3.fromRGB(225, 225, 225)} ):Play() end) DropButton2.MouseButton1Click:Connect(function() TweenService:Create( Dropdown, TweenInfo.new(0.2, Enum.EasingStyle.Quad, Enum.EasingDirection.Out), {Size = UDim2.new(0, 455, 0, 30)} ):Play() TweenService:Create( DropImage, TweenInfo.new(0.3, Enum.EasingStyle.Linear, Enum.EasingDirection.Out), {Rotation = 0} ):Play() Droptitle.Text = text.." : "..tostring(v) callback(v) isdropping = not isdropping DropScroll.CanvasSize = UDim2.new(0,0,0,DropdownList.AbsoluteContentSize.Y + 10) end) end DropButton.MouseButton1Click:Connect(function() if isdropping == false then isdropping = true TweenService:Create( Dropdown, TweenInfo.new(0.2, Enum.EasingStyle.Quad, Enum.EasingDirection.Out), {Size = UDim2.new(0, 455, 0, 100)} ):Play() TweenService:Create( DropImage, TweenInfo.new(0.4, Enum.EasingStyle.Quad, Enum.EasingDirection.Out), {Rotation = -180} ):Play() DropScroll.CanvasSize = UDim2.new(0,0,0,DropdownList.AbsoluteContentSize.Y + 10) else isdropping = false TweenService:Create( Dropdown, TweenInfo.new(0.2, Enum.EasingStyle.Quad, Enum.EasingDirection.Out), {Size = UDim2.new(0, 455, 0, 30)} ):Play() TweenService:Create( DropImage, TweenInfo.new(0.4, Enum.EasingStyle.Quad, Enum.EasingDirection.Out), {Rotation = 0} ):Play() DropScroll.CanvasSize = UDim2.new(0,0,0,DropdownList.AbsoluteContentSize.Y + 10) end end) DropScroll.CanvasSize = UDim2.new(0,0,0,DropdownList.AbsoluteContentSize.Y + 10) local drop = {} function drop:Clear() Droptitle.Text = tostring(text).." :" TweenService:Create( Dropdown, TweenInfo.new(0.2, Enum.EasingStyle.Quad, Enum.EasingDirection.Out), {Size = UDim2.new(0, 455, 0, 30)} ):Play() isdropping = false for i, v in next, DropScroll:GetChildren() do if v:IsA("TextButton") then v:Destroy() end end end function drop:Add(t) local DropButton2 = Instance.new("TextButton") DropButton2.Name = "DropButton2" DropButton2.Parent = DropScroll DropButton2.BackgroundColor3 = Color3.fromRGB(255, 255, 255) DropButton2.BackgroundTransparency = 1.000 DropButton2.Size = UDim2.new(0, 455, 0, 30) DropButton2.AutoButtonColor = false DropButton2.Font = Enum.Font.Gotham DropButton2.TextColor3 = Color3.fromRGB(225, 225, 225) DropButton2.TextSize = 11.000 DropButton2.Text = tostring(t) DropButton2.MouseButton1Click:Connect(function() TweenService:Create( Dropdown, TweenInfo.new(0.2, Enum.EasingStyle.Quad, Enum.EasingDirection.Out), {Size = UDim2.new(0, 455, 0, 30)} ):Play() TweenService:Create( DropImage, TweenInfo.new(0.3, Enum.EasingStyle.Linear, Enum.EasingDirection.Out), {Rotation = 0} ):Play() Droptitle.Text = text.." : "..tostring(t) callback(t) isdropping = not isdropping DropScroll.CanvasSize = UDim2.new(0,0,0,DropdownList.AbsoluteContentSize.Y + 10) end) end return drop end function main:Slider(text,min,max,set,callback) set = (math.clamp(set,min,max)) if set > max then set = max end local Slider = Instance.new("Frame") local UICorner = Instance.new("UICorner") local SliderTitle = Instance.new("TextLabel") local SliderValue = Instance.new("TextLabel") local SliderButton = Instance.new("TextButton") local Bar1 = Instance.new("Frame") local Bar = Instance.new("Frame") local UICorner_2 = Instance.new("UICorner") local CircleBar = Instance.new("Frame") local UICorner_3 = Instance.new("UICorner") local UICorner_4 = Instance.new("UICorner") Slider.Name = "Slider" Slider.Parent = ScrollTab Slider.BackgroundColor3 = Color3.fromRGB(50, 48, 59) Slider.Size = UDim2.new(0, 455, 0, 40) UICorner.CornerRadius = UDim.new(0, 5) UICorner.Parent = Slider SliderTitle.Name = "SliderTitle" SliderTitle.Parent = Slider SliderTitle.BackgroundColor3 = Color3.fromRGB(255, 255, 255) SliderTitle.BackgroundTransparency = 1.000 SliderTitle.Position = UDim2.new(0.0283286124, 0, 0, 0) SliderTitle.Size = UDim2.new(0, 290, 0, 20) SliderTitle.Font = Enum.Font.Gotham SliderTitle.Text = text SliderTitle.TextColor3 = Color3.fromRGB(225, 225, 225) SliderTitle.TextSize = 11.000 SliderTitle.TextXAlignment = Enum.TextXAlignment.Left SliderValue.Name = "SliderValue" SliderValue.Parent = Slider SliderValue.BackgroundColor3 = Color3.fromRGB(255, 255, 255) SliderValue.BackgroundTransparency = 1.000 SliderValue.Position = UDim2.new(0.887778878, 0, 0, 0) SliderValue.Size = UDim2.new(0, 40, 0, 20) SliderValue.Font = Enum.Font.Gotham SliderValue.Text = tostring(set and math.floor( (set / max) * (max - min) + min) or 0) SliderValue.TextColor3 = Color3.fromRGB(225, 225, 225) SliderValue.TextSize = 11.000 SliderButton.Name = "SliderButton" SliderButton.Parent = Slider SliderButton.BackgroundColor3 = Color3.fromRGB(255, 255, 255) SliderButton.BackgroundTransparency = 1.000 SliderButton.Position = UDim2.new(0, 10, 0, 25) SliderButton.Size = UDim2.new(0, 435, 0, 5) SliderButton.AutoButtonColor = false SliderButton.Font = Enum.Font.SourceSans SliderButton.Text = "" SliderButton.TextColor3 = Color3.fromRGB(0, 0, 0) SliderButton.TextSize = 14.000 Bar1.Name = "Bar1" Bar1.Parent = SliderButton Bar1.BackgroundColor3 = Color3.fromRGB(30, 28, 39) Bar1.Size = UDim2.new(0, 435, 0, 5) Bar.Name = "Bar" Bar.Parent = Bar1 Bar.BackgroundColor3 = Color3.fromRGB(16,255,24) Bar.Size = UDim2.new(set/max, 0, 0, 5) UICorner_2.CornerRadius = UDim.new(0, 100) UICorner_2.Parent = Bar CircleBar.Name = "CircleBar" CircleBar.Parent = Bar CircleBar.BackgroundColor3 = Color3.fromRGB(255, 255, 255) CircleBar.Position = UDim2.new(1, -2, 0, -2) CircleBar.AnchorPoint = Vector2.new(0, 0.1) CircleBar.Size = UDim2.new(0, 10, 0, 10) UICorner_3.CornerRadius = UDim.new(0, 100) UICorner_3.Parent = CircleBar UICorner_4.CornerRadius = UDim.new(0, 100) UICorner_4.Parent = Bar1 local mouse = game.Players.LocalPlayer:GetMouse() local uis = game:GetService("UserInputService") if Value == nil then Value = set pcall(function() callback(Value) end) end SliderButton.MouseButton1Down:Connect(function() Value = math.floor((((tonumber(max) - tonumber(min)) / 435) * Bar.AbsoluteSize.X) + tonumber(min)) or 0 pcall(function() callback(Value) end) Bar.Size = UDim2.new(0, math.clamp(mouse.X - Bar.AbsolutePosition.X, 0, 435), 0, 5) CircleBar.Position = UDim2.new(0, math.clamp(mouse.X - Bar.AbsolutePosition.X - 2, 0, 425), 0, -2) moveconnection = mouse.Move:Connect(function() SliderValue.Text = Value Value = math.floor((((tonumber(max) - tonumber(min)) / 435) * Bar.AbsoluteSize.X) + tonumber(min)) pcall(function() callback(Value) end) Bar.Size = UDim2.new(0, math.clamp(mouse.X - Bar.AbsolutePosition.X, 0, 435), 0, 5) CircleBar.Position = UDim2.new(0, math.clamp(mouse.X - Bar.AbsolutePosition.X - 2, 0, 425), 0, -2) end) releaseconnection = uis.InputEnded:Connect(function(Mouse) if Mouse.UserInputType == Enum.UserInputType.MouseButton1 then Value = math.floor((((tonumber(max) - tonumber(min)) / 435) * Bar.AbsoluteSize.X) + tonumber(min)) pcall(function() callback(Value) end) Bar.Size = UDim2.new(0, math.clamp(mouse.X - Bar.AbsolutePosition.X, 0, 435), 0, 5) CircleBar.Position = UDim2.new(0, math.clamp(mouse.X - Bar.AbsolutePosition.X - 2, 0, 425), 0, -2) moveconnection:Disconnect() releaseconnection:Disconnect() end end) end) releaseconnection = uis.InputEnded:Connect(function(Mouse) if Mouse.UserInputType == Enum.UserInputType.MouseButton1 then Value = math.floor((((tonumber(max) - tonumber(min)) / 435) * Bar.AbsoluteSize.X) + tonumber(min)) SliderValue.Text = Value end end) end function main:Seperator(text) local Seperator = Instance.new("Frame") local Sep1 = Instance.new("Frame") local SepLabel = Instance.new("TextLabel") local Sep2 = Instance.new("Frame") Seperator.Name = "Seperator" Seperator.Parent = ScrollTab Seperator.BackgroundColor3 = Color3.fromRGB(255, 255, 255) Seperator.BackgroundTransparency = 1.000 Seperator.ClipsDescendants = true Seperator.Size = UDim2.new(0, 455, 0, 20) Sep1.Name = "Sep1" Sep1.Parent = Seperator Sep1.BackgroundColor3 = Color3.fromRGB(16,255,24) Sep1.BorderSizePixel = 0 Sep1.Position = UDim2.new(0, 0, 0, 10) Sep1.Size = UDim2.new(0, 150, 0, 1) SepLabel.Name = "SepLabel" SepLabel.Parent = Seperator SepLabel.BackgroundColor3 = Color3.fromRGB(255, 255, 255) SepLabel.BackgroundTransparency = 1.000 SepLabel.Position = UDim2.new(0, 95, 0, 0) SepLabel.Size = UDim2.new(0, 255, 0, 20) SepLabel.Font = Enum.Font.Gotham SepLabel.Text = text SepLabel.TextColor3 = Color3.fromRGB(225,225,225) SepLabel.TextSize = 11.000 Sep2.Name = "Sep2" Sep2.Parent = Seperator Sep2.BackgroundColor3 = Color3.fromRGB(16,255,24) Sep2.BorderSizePixel = 0 Sep2.Position = UDim2.new(0, 305, 0, 10) Sep2.Size = UDim2.new(0, 150, 0, 1) end function main:Line() local Line = Instance.new("Frame") local Linee = Instance.new("Frame") Line.Name = "Line" Line.Parent = ScrollTab Line.BackgroundColor3 = Color3.fromRGB(255, 255, 255) Line.BackgroundTransparency = 1.000 Line.ClipsDescendants = true Line.Size = UDim2.new(0, 455, 0, 20) Linee.Name = "Linee" Linee.Parent = Line Linee.BackgroundColor3 = Color3.fromRGB(16,255,24) Linee.BorderSizePixel = 0 Linee.Position = UDim2.new(0, 0, 0, 10) Linee.Size = UDim2.new(0, 455, 0, 1) end function main:Label(text) local Label = Instance.new("TextLabel") local PaddingLabel = Instance.new("UIPadding") local labell = {} Label.Name = "Label" Label.Parent = ScrollTab Label.BackgroundColor3 = Color3.fromRGB(255, 255, 255) Label.BackgroundTransparency = 1.000 Label.Size = UDim2.new(0, 455, 0, 20) Label.Font = Enum.Font.Gotham Label.TextColor3 = Color3.fromRGB(225, 225, 225) Label.TextSize = 11.000 Label.Text = text Label.TextXAlignment = Enum.TextXAlignment.Left PaddingLabel.PaddingLeft = UDim.new(0,10) PaddingLabel.Parent = Label PaddingLabel.Name = "PaddingLabel" function labell:Set(newtext) Label.Text = newtext end return labell end return main end return uitab end -- Script local SOMEXHUB = library:AddWindow("1XLII HUB | BETA",Enum.KeyCode.RightControl) local AutoFarm = SOMEXHUB:AddTab("AutoFarm") local Stats = SOMEXHUB:AddTab("Stats") local Auto = SOMEXHUB:AddTab("Auto") local tp = SOMEXHUB:AddTab("Teleport") local Raid = SOMEXHUB:AddTab("Raid") local Shop = SOMEXHUB:AddTab("Shop") local Misc = SOMEXHUB:AddTab("Misc") local Setting = SOMEXHUB:AddTab("Setting") local Cr = SOMEXHUB:AddTab("Credit") -- AutoFarm AutoFarm:Label("WELCOME TO 1XLII HUB SCRIPT") Time = AutoFarm:Label("Server Time") function UpdateTime() local GameTime = math.floor(workspace.DistributedGameTime+0.5) local Hour = math.floor(GameTime/(60^2))%24 local Minute = math.floor(GameTime/(60^1))%60 local Second = math.floor(GameTime/(60^0))%60 Time:Set("Hour : "..Hour.." Minute : "..Minute.." Second : "..Second) end spawn(function() while true do UpdateTime() wait() end end) Client = AutoFarm:Label("FPS Server") function UpdateClient() local Ping = game:GetService("Stats").Network.ServerStatsItem["Data Ping"]:GetValueString() local Fps = workspace:GetRealPhysicsFPS() Client:Set("Fps : "..Fps.." Ping : "..Ping) end spawn(function() while true do wait(.1) UpdateClient() end end) AutoFarm:Line() AutoFarm:Toggle("Auto Set Spawn ",true,function(x) _G.Set = x end) spawn(function() while wait() do if _G.Set then pcall(function() local args = { [1] = "SetSpawnPoint" } game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer(unpack(args)) end) end end end) AutoFarm:Line() Wapon = {} for i,v in pairs(game.Players.LocalPlayer.Backpack:GetChildren()) do if v:IsA("Tool") then table.insert(Wapon ,v.Name) end end for i,v in pairs(game.Players.LocalPlayer.Character:GetChildren()) do if v:IsA("Tool") then table.insert(Wapon, v.Name) end end local SelectWeapon = AutoFarm:Dropdown("Select Weapon",Wapon,function(Value) SelectToolWeapon = Value SelectToolWeaponOld = Value end) AutoFarm:Button("Refresh Weapon",function() 	SelectWeapon:Clear() 	for i,v in pairs(game.Players.LocalPlayer.Backpack:GetChildren()) do 		if v:IsA("Tool") then 			SelectWeapon:Add(v.Name) 		end 	end 	for i,v in pairs(game.Players.LocalPlayer.Character:GetChildren()) do 		if v:IsA("Tool") then 			SelectWeapon:Add(v.Name) 		end 	end end) AutoFarm:Line() AutoFarm:Toggle("AutoFarm Level",false,function(vu) _G.AutoFarm = vu 	if _G.AutoFarm and SelectToolWeapon == "" then ui:Notification("AutoFarm","SelectWeapon First ",2) 	else 		Auto_Farm = vu Magnet = vu 		SelectMonster = "" 		if vu == false then 			wait(1) 			totarget(game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame) 		end 	end end) Auto:Toggle("AutoFarm Bone",false,function(vu) if not Three_World and vu then else _G.AutoFarmBone = vu _G.MainAutoFarmBone = vu end end) spawn(function() while wait() do if _G.AutoFarmBone and Three_World then if game:GetService("Workspace").Enemies:FindFirstChild("Reborn Skeleton [Lv. 1975]") or game:GetService("Workspace").Enemies:FindFirstChild("Living Zombie [Lv. 2000]") or game:GetService("Workspace").Enemies:FindFirstChild("Demonic Soul [Lv. 2025]") or game:GetService("Workspace").Enemies:FindFirstChild("Posessed Mummy [Lv. 2050]") then for i,v in pairs(game.Workspace.Enemies:GetChildren()) do if _G.AutoFarmBone and (v.Name == "Reborn Skeleton [Lv. 1975]" or v.Name == "Living Zombie [Lv. 2000]" or v.Name == "Demonic Soul [Lv. 2025]" or v.Name == "Posessed Mummy [Lv. 2050]") and v:FindFirstChild("HumanoidRootPart") and v:FindFirstChild("Humanoid") and v.Humanoid.Health > 0 then repeat wait() if (v.HumanoidRootPart.Position - game.Players.LocalPlayer.Character.HumanoidRootPart.Position).magnitude > 300 then Farmtween = toTarget(v.HumanoidRootPart.Position,v.HumanoidRootPart.CFrame) MagnetFarmBone = false elseif (v.HumanoidRootPart.Position - game.Players.LocalPlayer.Character.HumanoidRootPart.Position).magnitude <= 300 then if Farmtween then Farmtween:Stop() end PosFarmBone = v.HumanoidRootPart.CFrame EquipWeapon(SelectToolWeapon) if not game.Players.LocalPlayer.Character:FindFirstChild("HasBuso") then local args = { [1] = "Buso" } game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer(unpack(args)) end game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame = v.HumanoidRootPart.CFrame * CFrame.new(0, 30, 0) game:GetService('VirtualUser'):CaptureController() game:GetService('VirtualUser'):Button1Down(Vector2.new(0,0),workspace.CurrentCamera.CFrame) game:GetService('VirtualUser'):Button1Up(Vector2.new(0,0),workspace.CurrentCamera.CFrame) MagnetFarmBone = true end until not _G.AutoFarmBone or not v.Parent or v.Humanoid.Health <= 0 MagnetFarmBone = false end end else MagnetFarmBone = false Questtween = toTarget(CFrame.new(-9506.14648, 172.130661, 6101.79053).Position,CFrame.new(-9506.14648, 172.130661, 6101.79053)) if (CFrame.new(-9506.14648, 172.130661, 6101.79053).Position - game.Players.LocalPlayer.Character.HumanoidRootPart.Position).magnitude <= 300 then if Questtween then Questtween:Stop() end game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame = CFrame.new(-9506.14648, 172.130661, 6101.79053, -0.999731541, 0, -0.0231563263, 0, 1, 0, 0.0231563263, 0, -0.999731541) end end end end end) AutoFarm:Toggle("AutoFarm Ectoplasm",false,function(A) if New_World then _G.AutoFramEctoplasm = A else end end) spawn(function() while wait() do if _G.AutoFramEctoplasm and New_World then if game.Workspace.Enemies:FindFirstChild("Ship Deckhand [Lv. 1250]") or game.Workspace.Enemies:FindFirstChild("Ship Engineer [Lv. 1275]") or game.Workspace.Enemies:FindFirstChild("Ship Steward [Lv. 1300]") or game.Workspace.Enemies:FindFirstChild("Ship Officer [Lv. 1325]") then for i,v in pairs(game.Workspace.Enemies:GetChildren()) do if string.find(v.Name, "Ship") then repeat wait() Usefastattack = true if string.find(v.Name, "Ship") then if (v.HumanoidRootPart.Position - game.Players.LocalPlayer.Character.HumanoidRootPart.Position).magnitude > 300 then Farmtween = toTarget(v.HumanoidRootPart.Position,v.HumanoidRootPart.CFrame) StatrMagnetEctoplasm = false elseif (v.HumanoidRootPart.Position - game.Players.LocalPlayer.Character.HumanoidRootPart.Position).magnitude <= 300 then if Farmtween then Farmtween:Stop() end EquipWeapon(SelectToolWeapon) PosMonEctoplasm = v.HumanoidRootPart.CFrame Usefastattack = true if not game.Players.LocalPlayer.Character:FindFirstChild("HasBuso") then local args = { [1] = "Buso" } game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer(unpack(args)) end StatrMagnetEctoplasm = true game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame = v.HumanoidRootPart.CFrame * CFrame.new(0, 10, 10) game:GetService'VirtualUser':CaptureController() game:GetService'VirtualUser':Button1Down(Vector2.new(1280, 672)) end else StatrMagnetEctoplasm = false if (CFrame.new(920.14447, 129.581833, 33442.168).Position - game.Players.LocalPlayer.Character.HumanoidRootPart.Position).magnitude > 300 then Farmtween = toTarget(CFrame.new(920.14447, 129.581833, 33442.168).Position,CFrame.new(920.14447, 129.581833, 33442.168)) elseif (CFrame.new(920.14447, 129.581833, 33442.168).Position - game.Players.LocalPlayer.Character.HumanoidRootPart.Position).magnitude <= 300 then if Farmtween then Farmtween:Stop() end game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame = CFrame.new(920.14447, 129.581833, 33442.168, -0.999913812, 0, -0.0131403487, 0, 1, 0, 0.0131403487, 0, -0.999913812) end end until _G.AutoFramEctoplasm == false or not v.Parent or v.Humanoid.Health <= 0 Usefastattack = false StatrMagnetEctoplasm = false if (CFrame.new(920.14447, 129.581833, 33442.168).Position - game.Players.LocalPlayer.Character.HumanoidRootPart.Position).magnitude > 300 then Farmtween = toTarget(CFrame.new(920.14447, 129.581833, 33442.168).Position,CFrame.new(920.14447, 129.581833, 33442.168)) elseif (CFrame.new(920.14447, 129.581833, 33442.168).Position - game.Players.LocalPlayer.Character.HumanoidRootPart.Position).magnitude <= 300 then if Farmtween then Farmtween:Stop() end game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame = CFrame.new(920.14447, 129.581833, 33442.168, -0.999913812, 0, -0.0131403487, 0, 1, 0, 0.0131403487, 0, -0.999913812) end end end else if (CFrame.new(920.14447, 129.581833, 33442.168).Position - game.Players.LocalPlayer.Character.HumanoidRootPart.Position).magnitude > 300 then Farmtween = toTarget(CFrame.new(920.14447, 129.581833, 33442.168).Position,CFrame.new(920.14447, 129.581833, 33442.168)) elseif (CFrame.new(920.14447, 129.581833, 33442.168).Position - game.Players.LocalPlayer.Character.HumanoidRootPart.Position).magnitude <= 300 then if Farmtween then Farmtween:Stop() end game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame = CFrame.new(920.14447, 129.581833, 33442.168, -0.999913812, 0, -0.0131403487, 0, 1, 0, 0.0131403487, 0, -0.999913812) end end end end end) AutoFarm:Toggle("AutoFarm Chest",false,function(v) 	AutoFarmChest = v end) _G.MagnitudeAdd = 0 spawn(function() 		while wait() do 			pcall(function() 				if AutoFarmChest then 					for i,v in pairs(game:GetService("Workspace"):GetChildren()) do 						if v.Name:find("Chest") then 							if game:GetService("Workspace"):FindFirstChild(v.Name) then 								if (v.Position - game.Players.LocalPlayer.Character.HumanoidRootPart.Position).Magnitude <= 5000+_G.MagnitudeAdd then 									repeat wait() 										if game:GetService("Workspace"):FindFirstChild(v.Name) then 											SlowtoTarget(v.CFrame) 										end 									until AutoFarmChest == false or not v.Parent 									_G.MagnitudeAdd = _G.MagnitudeAdd+1500 								end 							end 						end 					end 				end 			end) 		end 	end) AutoFarm:Line() local Bosslist = {} for i, v in pairs(game.ReplicatedStorage:GetChildren()) do if string.find(v.Name, "Boss") then if v.Name ~= "Ice Admiral [Lv. 700] [Boss]" then table.insert(Bosslist, v.Name) end end end for i, v in pairs(game.workspace.Enemies:GetChildren()) do if string.find(v.Name, "Boss") then if v.Name ~= "Ice Admiral [Lv. 700] [Boss]" then table.insert(Bosslist, v.Name) end end end SelectBoss = "" local BossName = AutoFarm:Dropdown("Select Boss",Bosslist,function(Value) 	SelectBoss = Value 	Don = false end) AutoFarm:Button("Refresh Boss",function() Boss = {} BossName:Clear() 		for i, v in pairs(game.ReplicatedStorage:GetChildren()) do 			if string.find(v.Name, "Boss") then 				if v.Name == "Ice Admiral [Lv. 700] [Boss]" then 				else 					BossName:Add(v.Name) 				end 			end 		end 		for i, v in pairs(game.workspace.Enemies:GetChildren()) do 			if string.find(v.Name, "Boss") then 				if v.Name == "Ice Admiral [Lv. 700] [Boss]" then 				else 					BossName:Add(v.Name) 				end 			end 		end end) AutoFarm:Toggle("AutoFarm Boss",false,function(Value) 		local args = { 			[1] = "AbandonQuest" 		} 		game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer(unpack(args)) 		FramBoss = Value 	end) spawn(function() 	while wait() do 		if FramBoss then 			AutoFramBoss() 		end 	end end) AutoFarm:Toggle("AutoFarm All Boss",false,function(Value) 		KillAllBoss = Value 		MsBoss = "" 		KillBossuseGet = false 	end) spawn(function() 	while wait() do 		if KillAllBoss then 			AutoFramAllBoss() 		end 	end end) 	 -- Stats Stats:Toggle("Melee",false,function(Value) melee = Value end) Stats:Toggle("Defense",false,function(value) defense = value end) Stats:Toggle("Sword",false,function(value) sword = value end) Stats:Toggle("Gun",false,function(value) gun = value end) Stats:Toggle("Devil Fruit",false,function(value) demonfruit = value end) Stats:Line() PointStats = 1 Stats:Slider("Point",1,100,PointStats,nil,function(value) PointStats = value end) spawn(function() 		while wait() do 			if game.Players.localPlayer.Data.Points.Value >= PointStats then 				if melee then 					local args = { 						[1] = "AddPoint", 						[2] = "Melee", 						[3] = PointStats 					} 					game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer(unpack(args)) 				end 				if defense then 					local args = { 						[1] = "AddPoint", 						[2] = "Defense", 						[3] = PointStats 					} 					game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer(unpack(args)) 				end 				if sword then 					local args = { 						[1] = "AddPoint", 						[2] = "Sword", 						[3] = PointStats 					} 					game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer(unpack(args)) 				end 				if gun then 					local args = { 						[1] = "AddPoint", 						[2] = "Gun", 						[3] = PointStats 					} 					game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer(unpack(args)) 				end 				if demonfruit then 					local args = { 						[1] = "AddPoint", 						[2] = "Demon Fruit", 						[3] = PointStats 					} 					game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer(unpack(args)) 				end 			end 		end 	end) -- Auto Auto:Toggle("Auto New World",false,function(value) _G.AutoNew = value end) spawn(function() while wait(.1) do if _G.AutoNew then if Old_World then local MyLevel = game.Players.localPlayer.Data.Level.Value if MyLevel >= 700 and OldWorld then _G.AutoFarm = false Auto_Farm = false SelectWeapon = "Key" repeat wait() totarget(CFrame.new(4849.29883, 5.65138149, 719.611877)) until not _G.AutoNew or (game.Players.LocalPlayer.Character.HumanoidRootPart.Position - CFrame.new(4849.29883, 5.65138149, 719.611877).Position).Magnitude <= 10 wait(0.5) game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer("DressrosaQuestProgress","Detective") wait(0.5) if game.Players.LocalPlayer.Backpack:FindFirstChild("Key") then local tool = game.Players.LocalPlayer.Backpack:FindFirstChild("Key") wait(.4) game.Players.LocalPlayer.Character.Humanoid:EquipTool(tool) end repeat wait() totarget(CFrame.new(1347.7124, 37.3751602, -1325.6488)) until not _G.AutoNew or (game.Players.LocalPlayer.Character.HumanoidRootPart.Position - CFrame.new(1347.7124, 37.3751602, -1325.6488).Position).Magnitude <= 10 wait(0.5) Click() if game.Workspace.Enemies:FindFirstChild("Ice Admiral [Lv. 700] [Boss]") and game.Workspace.Map.Ice.Door.CanCollide == false and game.Workspace.Map.Ice.Door.Transparency == 1 then CheckBoss = true EquipWeapon(SelectToolWeapon) if not game.Players.LocalPlayer.Character:FindFirstChild("HasBuso") then game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer("Buso") end for i,v in pairs(game.Workspace.Enemies:GetChildren()) do if CheckBoss and v:IsA("Model") and v:FindFirstChild("Humanoid") and v:FindFirstChild("HumanoidRootPart") and v.Humanoid.Health > 0 and v.Name == "Ice Admiral [Lv. 700] [Boss]" then if not game.Players.LocalPlayer.Character:FindFirstChild("HasBuso") then game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer("Buso") end repeat wait(.1) pcall(function() v.HumanoidRootPart.Size = Vector3.new(50, 50, 50) v.HumanoidRootPart.BrickColor = BrickColor.new("White") v.HumanoidRootPart.CanCollide = false totarget(v.HumanoidRootPart.CFrame*CFrame.new(0, 10, 10)) Click() end) until not CheckBoss or not v.Parent or v.Humanoid.Health <= 0 end end CheckBoss = false wait(0.5) repeat wait() totarget(CFrame.new(-1166.23743, 7.65220165, 1728.36487)) until (game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame - CFrame.new(-1166.23743, 7.65220165, 1728.36487).Position).Magnitude <= 10 wait(0.5) game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer("TravelDressrosa") else if game.Players.LocalPlayer.Backpack:FindFirstChild("Key") then local tool = game.Players.LocalPlayer.Backpack:FindFirstChild("Key") wait(.4) game.Players.LocalPlayer.Character.Humanoid:EquipTool(tool) end totarget(CFrame.new(1347.7124, 37.3751602, -1325.6488)) end end end end end end) Auto:Toggle("Auto Third World",false,function(vu) _G.AutoThird = vu end) spawn(function() pcall(function() while wait() do if _G.AutoThird then if game:GetService("Players").LocalPlayer.Data.Level.Value >= 1500 and world2 then _G.AutoFarm = false Auto_Farm = false if game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer("ZQuestProgress").KilledIndraBoss == false then if game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer("BartiloQuestProgress","Bartilo") == 3 then if game:GetService("Players").LocalPlayer.Data.SpawnPoint.Value == "Bar" then if game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer("TalkTrevor","1") == 0 then if game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer("ZQuestProgress","Check") == 0 then if (CFrame.new(-1926.3221435547, 12.819851875305, 1738.3092041016).Position - game.Players.LocalPlayer.Character.HumanoidRootPart.Position).Magnitude <= 10 then wait(1.1) Usefastattack = false game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer("ZQuestProgress","Begin") else Usefastattack = false totarget(CFrame.new(-1926.3221435547, 12.819851875305, 1738.3092041016)) end if game:GetService("Workspace").Enemies:FindFirstChild("rip_indra [Lv. 1500] [Boss]") then for i,v in pairs(game:GetService("Workspace").Enemies:GetChildren()) do if v.Name == "rip_indra [Lv. 1500] [Boss]" then repeat game:GetService("RunService").Heartbeat:wait() Usefastattack = true pcall(function() EquipWeapon(SelectToolWeapon) totarget(v.HumanoidRootPart.CFrame * CFrame.new(0,25,25)) require(game:GetService("Players").LocalPlayer.PlayerScripts.CombatFramework).activeController.hitboxMagnitude = 1000 game:GetService'VirtualUser':CaptureController() game:GetService'VirtualUser':Button1Down(Vector2.new(1280, 672)) game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer("TravelZou") sethiddenproperty(game.Players.LocalPlayer, "SimulationRadius", math.huge) end) until _G.AutoThird == false or v.Humanoid.Health <= 0 or not v.Parent Usefastattack = false end end elseif not game:GetService("Workspace").Enemies:FindFirstChild("rip_indra [Lv. 1500] [Boss]") and (CFrame.new(-26880.93359375, 22.848554611206, 473.18951416016).Position - game.Players.LocalPlayer.Character.HumanoidRootPart.Position).Magnitude <= 1000 then totarget(CFrame.new(-26880.93359375, 22.848554611206, 473.18951416016)) Usefastattack = false end elseif game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer("ZQuestProgress","Check") ~= 0 then if game:GetService("Workspace").Enemies:FindFirstChild("Don Swan [Lv. 1000] [Boss]") or game:GetService("ReplicatedStorage"):FindFirstChild("Don Swan [Lv. 1000] [Boss]") then if game:GetService("Workspace").Enemies:FindFirstChild("Don Swan [Lv. 1000] [Boss]") then for i,v in pairs(game:GetService("Workspace").Enemies:GetChildren()) do if v.Name == "Don Swan [Lv. 1000] [Boss]" then repeat game:GetService("RunService").Heartbeat:wait() pcall(function() Usefastattack = true EquipWeapon(SelectToolWeapon) totarget(v.HumanoidRootPart.CFrame * CFrame.new(0,25,25)) require(game:GetService("Players").LocalPlayer.PlayerScripts.CombatFramework).activeController.hitboxMagnitude = 1000 game:GetService'VirtualUser':CaptureController() game:GetService'VirtualUser':Button1Down(Vector2.new(1280, 672)) sethiddenproperty(game.Players.LocalPlayer, "SimulationRadius", math.huge) end) until _G.AutoThird == false or v.Humanoid.Health <= 0 or not v.Parent Usefastattack = false end end else if (CFrame.new(2284.912109375, 15.537666320801, 905.48291015625).Position - game.Players.LocalPlayer.Character.HumanoidRootPart.Position).Magnitude > 1000 then game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer("requestEntrance",Vector3.new(2284.912109375, 15.537666320801, 905.48291015625)) wait() end Usefastattack = false totarget(CFrame.new(2284.912109375, 15.537666320801, 905.48291015625)) end elseif _G.AutoThird and not game:GetService("Workspace").Enemies:FindFirstChild("Don Swan [Lv. 1000] [Boss]") and not game:GetService("ReplicatedStorage"):FindFirstChild("Don Swan [Lv. 1000] [Boss]") then bithop() elseif not _G.AutoThird and not game:GetService("Workspace").Enemies:FindFirstChild("Don Swan [Lv. 1000] [Boss]") and not game:GetService("ReplicatedStorage"):FindFirstChild("Don Swan [Lv. 1000] [Boss]") then if (CFrame.new(2284.912109375, 15.537666320801, 905.48291015625).Position - game.Players.LocalPlayer.Character.HumanoidRootPart.Position).Magnitude > 1000 then game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer("requestEntrance",Vector3.new(2284.912109375, 15.537666320801, 905.48291015625)) wait() end Usefastattack = false totarget(CFrame.new(2284.912109375, 15.537666320801, 905.48291015625)) end end elseif game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer("TalkTrevor","1") ~= 0 then for i,v in pairs(game:GetService("Workspace"):GetChildren()) do if string.find(v.Name, "Fruit") then if v:IsA("Tool") then if (v.Handle.Position - game.Players.LocalPlayer.Character.HumanoidRootPart.Position).Magnitude <= 20000 then v.Handle.CFrame = game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame end end end end if game.Players.LocalPlayer.Backpack:FindFirstChild("Quake Fruit") or game.Players.LocalPlayer.Backpack:FindFirstChild("Human: Buddha Fruit") or game.Players.LocalPlayer.Backpack:FindFirstChild("String Fruit") or game.Players.LocalPlayer.Backpack:FindFirstChild("Bird: Phoenix Fruit") or game.Players.LocalPlayer.Backpack:FindFirstChild("Rumble Fruit") or game.Players.LocalPlayer.Backpack:FindFirstChild("Paw Fruit") or game.Players.LocalPlayer.Backpack:FindFirstChild("Gravity Fruit") or game.Players.LocalPlayer.Backpack:FindFirstChild("Dough Fruit") or game.Players.LocalPlayer.Backpack:FindFirstChild("Shadow Fruit") or game.Players.LocalPlayer.Backpack:FindFirstChild("Venom Fruit") or game.Players.LocalPlayer.Backpack:FindFirstChild("Control Fruit") or game.Players.LocalPlayer.Backpack:FindFirstChild("Dragon Fruit") or game.Players.LocalPlayer.Character:FindFirstChild("Quake Fruit") or game.Players.LocalPlayer.Character:FindFirstChild("Human: Buddha Fruit") or game.Players.LocalPlayer.Character:FindFirstChild("String Fruit") or game.Players.LocalPlayer.Character:FindFirstChild("Bird: Phoenix Fruit") or game.Players.LocalPlayer.Character:FindFirstChild("Rumble Fruit") or game.Players.LocalPlayer.Character:FindFirstChild("Paw Fruit") or game.Players.LocalPlayer.Character:FindFirstChild("Gravity Fruit") or game.Players.LocalPlayer.Character:FindFirstChild("Dough Fruit") or game.Players.LocalPlayer.Character:FindFirstChild("Shadow Fruit") or game.Players.LocalPlayer.Character:FindFirstChild("Venom Fruit") or game.Players.LocalPlayer.Character:FindFirstChild("Control Fruit") or game.Players.LocalPlayer.Character:FindFirstChild("Dragon Fruit") then game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer("TalkTrevor","1") game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer("TalkTrevor","2") game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer("TalkTrevor","3") end end else totarget(CFrame.new(-379.70889282227, 73.0458984375, 304.84692382813)) game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer("SetSpawnPoint") end else if game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer("BartiloQuestProgress","Bartilo") == 0 then if string.find(game.Players.LocalPlayer.PlayerGui.Main.Quest.Container.QuestTitle.Title.Text, "Swan Pirates") and string.find(game.Players.LocalPlayer.PlayerGui.Main.Quest.Container.QuestTitle.Title.Text, "50") and game.Players.LocalPlayer.PlayerGui.Main.Quest.Visible == true then if game.Workspace.Enemies:FindFirstChild("Swan Pirate [Lv. 775]") then for i,v in pairs(game.Workspace.Enemies:GetChildren()) do if v.Name == "Swan Pirate [Lv. 775]" then PosMonBarto = v.HumanoidRootPart.CFrame pcall(function() repeat wait() for k,x in pairs(game.Workspace.Enemies:GetChildren()) do if x.Name == "Swan Pirate [Lv. 775]" then x.Humanoid:ChangeState(11) sethiddenproperty(game.Players.LocalPlayer, "SimulationRadius", math.huge) x.HumanoidRootPart.CanCollide = false sethiddenproperty(game.Players.LocalPlayer, "SimulationRadius", math.huge) x.HumanoidRootPart.Size = Vector3.new(30, 30, 30) sethiddenproperty(game.Players.LocalPlayer, "SimulationRadius", math.huge) x.HumanoidRootPart.CFrame = PosMonBarto sethiddenproperty(game.Players.LocalPlayer, "SimulationRadius", math.huge) end end Usefastattack = true EquipWeapon(SelectToolWeapon) v.HumanoidRootPart.CanCollide = false v.HumanoidRootPart.Size = Vector3.new(35, 35, 35) totarget( v.HumanoidRootPart.CFrame * CFrame.new(0,15,0)) game:GetService'VirtualUser':CaptureController() game:GetService'VirtualUser':Button1Down(Vector2.new(1280, 672)) until not v.Parent or v.Humanoid.Health <= 0 or game.Players.LocalPlayer.PlayerGui.Main.Quest.Visible == false Usefastattack = false end) end end else Usefastattack = false totarget(CFrame.new(1057.92761, 137.614319, 1242.08069)) end else Usefastattack = false totarget(CFrame.new(-456.28952, 73.0200958, 299.895966)) wait(1.1) game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer("StartQuest","BartiloQuest",1) end elseif game.Players.LocalPlayer.Data.Level.Value >= 800 and game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer("BartiloQuestProgress","Bartilo") == 1 then if game.Workspace.Enemies:FindFirstChild("Jeremy [Lv. 850] [Boss]") then Ms = "Jeremy [Lv. 850] [Boss]" for i,v in pairs(game.Workspace.Enemies:GetChildren()) do if v.Name == Ms then repeat wait() Usefastattack = true EquipWeapon(SelectToolWeapon) v.HumanoidRootPart.CanCollide = false v.HumanoidRootPart.Size = Vector3.new(35, 35, 35) totarget(v.HumanoidRootPart.CFrame * CFrame.new(0,15,0)) game:GetService'VirtualUser':CaptureController() game:GetService'VirtualUser':Button1Down(Vector2.new(1280, 672)) until not v.Parent or v.Humanoid.Health <= 0 Usefastattack = false end end elseif game.ReplicatedStorage:FindFirstChild("Jeremy [Lv. 850] [Boss]") then Usefastattack = false totarget(CFrame.new(-456.28952, 73.0200958, 299.895966)) wait(1.1) game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer("BartiloQuestProgress","Bartilo") wait(1) totarget(CFrame.new(2099.88159, 448.931, 648.997375)) wait(2) else totarget(CFrame.new(2099.88159, 448.931, 648.997375)) end wait(15) if not game.Workspace.Enemies:FindFirstChild("Jeremy [Lv. 850] [Boss]") then bithop() end elseif game.Players.LocalPlayer.Data.Level.Value >= 800 and game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer("BartiloQuestProgress","Bartilo") == 2 then totarget(CFrame.new(-1850.49329, 13.1789551, 1750.89685)) Usefastattack = false wait(1.5) game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame = CFrame.new(-1858.87305, 19.3777466, 1712.01807) wait(1.5) game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame = CFrame.new(-1803.94324, 16.5789185, 1750.89685) wait(1.5) game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame = CFrame.new(-1858.55835, 16.8604317, 1724.79541) wait(1.5) game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame = CFrame.new(-1869.54224, 15.987854, 1681.00659) wait(1.5) game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame = CFrame.new(-1800.0979, 16.4978027, 1684.52368) wait(1.5) game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame = CFrame.new(-1819.26343, 15.795166, 1717.90625) wait(1.5) game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame = CFrame.new(-1813.51843, 15.8604736, 1724.79541) wait(1.5) end end else game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer("TravelZou") end end end end end) end) spawn(function() pcall(function() while wait(.1) do wait(5) if _G.AutoThird and New_World and game:GetService("Players").LocalPlayer.Data.Level.Value >= 1500 then if game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer("BartiloQuestProgress","Bartilo") == 3 then if game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer("TalkTrevor","1") ~= 0 then if not game.Players.LocalPlayer.Backpack:FindFirstChild("Quake Fruit") and not game.Players.LocalPlayer.Backpack:FindFirstChild("Human: Buddha Fruit") and not game.Players.LocalPlayer.Backpack:FindFirstChild("String Fruit") and not game.Players.LocalPlayer.Backpack:FindFirstChild("Bird: Phoenix Fruit") and not game.Players.LocalPlayer.Backpack:FindFirstChild("Rumble Fruit") and not game.Players.LocalPlayer.Backpack:FindFirstChild("Paw Fruit") and not game.Players.LocalPlayer.Backpack:FindFirstChild("Gravity Fruit") and not game.Players.LocalPlayer.Backpack:FindFirstChild("Dough Fruit") and not game.Players.LocalPlayer.Backpack:FindFirstChild("Shadow Fruit") and not game.Players.LocalPlayer.Backpack:FindFirstChild("Venom Fruit") and not game.Players.LocalPlayer.Backpack:FindFirstChild("Control Fruit") and not game.Players.LocalPlayer.Backpack:FindFirstChild("Dragon Fruit") and not game.Players.LocalPlayer.Character:FindFirstChild("Quake Fruit") and not game.Players.LocalPlayer.Character:FindFirstChild("Human: Buddha Fruit") and not game.Players.LocalPlayer.Character:FindFirstChild("String Fruit") and not game.Players.LocalPlayer.Character:FindFirstChild("Bird: Phoenix Fruit") and not game.Players.LocalPlayer.Character:FindFirstChild("Rumble Fruit") and not game.Players.LocalPlayer.Character:FindFirstChild("Paw Fruit") and not game.Players.LocalPlayer.Character:FindFirstChild("Gravity Fruit") and not game.Players.LocalPlayer.Character:FindFirstChild("Dough Fruit") and not game.Players.LocalPlayer.Character:FindFirstChild("Shadow Fruit") and not game.Players.LocalPlayer.Character:FindFirstChild("Venom Fruit") and not game.Players.LocalPlayer.Character:FindFirstChild("Control Fruit") and not game.Players.LocalPlayer.Character:FindFirstChild("Dragon Fruit") then bithop() end end end end end end) end) Auto:Line() Auto:Toggle("Auto Superhuman",nil,function(vu) 		Superhuman = vu 		if vu then 			local args = { 				[1] = "BuyElectro" 			} 			game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer(unpack(args)) 		end 	end) Auto:Toggle("Auto Death Step",nil,function(vu) 		DeathStep = vu 		if vu then 			local args = { 				[1] = "BuyBlackLeg" 			} 			game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer(unpack(args)) 		end 	end) Auto:Toggle("Auto Dragon Talon",nil,function(vu) 		DargonTalon = vu 		if vu then 			local args = { 				[1] = "BlackbeardReward", 				[2] = "DragonClaw", 				[3] = "2" 			} 			game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer(unpack(args)) 		end 	end) Auto:Toggle("Auto Electric Clow",nil,function(vu) 		Electricclow = vu 		if vu then 			local args = { 				[1] = "BuyElectro" 			} 			game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer(unpack(args)) 		end 	end) 	spawn(function() 		while wait(.25) do 			if Superhuman and game.Players.LocalPlayer:FindFirstChild("WeaponAssetCache") then 				if game.Players.LocalPlayer.Backpack:FindFirstChild("Combat") or game.Players.LocalPlayer.Character:FindFirstChild("Combat") then 					local args = { 						[1] = "BuyElectro" 					} 					game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer(unpack(args)) 				end 				if game.Players.LocalPlayer.Character:FindFirstChild("Superhuman") or game.Players.LocalPlayer.Backpack:FindFirstChild("Superhuman") then 					SelectToolWeapon = "Superhuman" 				end 				if game.Players.LocalPlayer.Backpack:FindFirstChild("Black Leg") and game.Players.LocalPlayer.Backpack:FindFirstChild("Black Leg").Level.Value <= 299 then 					SelectToolWeapon = "Black Leg" 				end 				if game.Players.LocalPlayer.Backpack:FindFirstChild("Electro") and game.Players.LocalPlayer.Backpack:FindFirstChild("Electro").Level.Value <= 299 then 					SelectToolWeapon = "Electro" 				end 				if game.Players.LocalPlayer.Backpack:FindFirstChild("Fishman Karate") and game.Players.LocalPlayer.Backpack:FindFirstChild("Fishman Karate").Level.Value <= 299 then 					SelectToolWeapon = "Fishman Karate" 				end 				if game.Players.LocalPlayer.Backpack:FindFirstChild("Dragon Claw") and game.Players.LocalPlayer.Backpack:FindFirstChild("Dragon Claw").Level.Value <= 299 then 					SelectToolWeapon = "Dragon Claw" 				end 				if game.Players.LocalPlayer.Backpack:FindFirstChild("Black Leg") and game.Players.LocalPlayer.Backpack:FindFirstChild("Black Leg").Level.Value >= 300 then 					local args = { 						[1] = "BuyFishmanKarate" 					} 					game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer(unpack(args)) 				end 				if game.Players.LocalPlayer.Character:FindFirstChild("Black Leg") and game.Players.LocalPlayer.Character:FindFirstChild("Black Leg").Level.Value >= 300 then 					local args = { 						[1] = "BuyFishmanKarate" 					} 					game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer(unpack(args)) 				end 				if game.Players.LocalPlayer.Backpack:FindFirstChild("Electro") and game.Players.LocalPlayer.Backpack:FindFirstChild("Electro").Level.Value >= 100 then 					local args = { 						[1] = "BuyBlackLeg" 					} 					game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer(unpack(args)) 				end 				if game.Players.LocalPlayer.Character:FindFirstChild("Electro") and game.Players.LocalPlayer.Character:FindFirstChild("Electro").Level.Value >= 300 then 					local args = { 						[1] = "BuyBlackLeg" 					} 					game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer(unpack(args)) 				end 				if game.Players.LocalPlayer.Backpack:FindFirstChild("Fishman Karate") and game.Players.LocalPlayer.Backpack:FindFirstChild("Fishman Karate").Level.Value >= 300 then 					if SuperhumanFull and game.Players.LocalPlayer.Data.Fragments.Value < 1500 then 						if game.Players.LocalPlayer.Data.Level.Value > 1100 then 							RaidsSelected = "Flame" 							AutoRaids = true 							RaidsArua = true 						end 					else 						AutoRaids = false 						RaidsArua = false 						local args = { 							[1] = "BlackbeardReward", 							[2] = "DragonClaw", 							[3] = "2" 						} 						game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer(unpack(args)) 					end 				end 				if game.Players.LocalPlayer.Character:FindFirstChild("Fishman Karate") and game.Players.LocalPlayer.Character:FindFirstChild("Fishman Karate").Level.Value >= 300 then 					if SuperhumanFull and game.Players.LocalPlayer.Data.Fragments.Value < 1500 then 						if game.Players.LocalPlayer.Data.Level.Value > 1100 then 							RaidsSelected = "Flame" 							AutoRaids = true 							RaidsArua = true 						end 					else 						AutoRaids = false 						RaidsArua = false 						local args = { 							[1] = "BlackbeardReward", 							[…

---
## [Contrabang/Paradise](https://github.com/Contrabang/Paradise)@[6082c95eb3...](https://github.com/Contrabang/Paradise/commit/6082c95eb300a9f05b5422060db79f55fe91b9b3)
#### Saturday 2022-06-11 12:21:51 by LightFire53

Relocates The Entertainment Offices and Custodial Closet on DeltaStation (#17480)

* Location, Location, Location!

* Lights and Pipes

I am so sorry for how hacky that disposal piping is

* TFW Disposals

* Oh god, what if there is a fire?!

* And a light switch...

Maybe the final commit? Taking bets on if I managed to forget something else

* If you bet on the requests console

You would be right.

* Bigger, Better, Janitor

* Bloody requests console...

---
## [KMRH47/BTQuickie](https://github.com/KMRH47/BTQuickie)@[8da302a5ae...](https://github.com/KMRH47/BTQuickie/commit/8da302a5ae978fcec9eb61a421b021d88cb869bf)
#### Saturday 2022-06-11 13:23:02 by Karsten

This is my largest commit yet. Please forgive me.

From this day on, all future commits in this repository will be of adequate size (I promise!) :angel:

To be honest, I can't muster the energy to document each individual file change, so I'll make it brief:

- The application now has a context menu!
Just right click that juicy icon to see all the different possibilities!

- Settings
1) CUSTOM HOTKEY(s)!: You can now bind your own hotkey instead of using the default one I created in a jiffy (WIN+SHIFT+K).
2) Adjust discovery time (the time in milliseconds the app should search for Bluetooth devices)

- UI updated slightly

- Some other negligible functionality that nobody will notice

Also, I tried to clean the code base and implement some sweet tricks here and there... Personally, I ain't satisfied, but I'll keep working hard to reach omnipotence.

Thanks for joining my TED talk.

---
## [philippines69/carlcastroarchives](https://github.com/philippines69/carlcastroarchives)@[b35f3972a3...](https://github.com/philippines69/carlcastroarchives/commit/b35f3972a3feb546066b2eb101e66001804489fc)
#### Saturday 2022-06-11 14:22:20 by philippines69

Update from Forestry.io
philippines69 created _posts/2022-06-11-sometimes-I-fuckin-hate-my-friends/.gitkeep

---
## [CavenderHub/CavenderHub](https://github.com/CavenderHub/CavenderHub)@[447a2920e8...](https://github.com/CavenderHub/CavenderHub/commit/447a2920e8364e78e05f0d0474a6c2c2a2ecb555)
#### Saturday 2022-06-11 14:39:56 by CavenderHub

BONKHUB

local function loading() 	local Loading = Instance.new("ScreenGui") 	local Blur = Instance.new("Frame") 	local Main = Instance.new("Frame") 	local UICorner = Instance.new("UICorner") 	local Logo = Instance.new("ImageLabel") 	local UICorner_2 = Instance.new("UICorner") 	local Load = Instance.new("Frame") 	local UICorner_3 = Instance.new("UICorner") 	local Bar = Instance.new("Frame") 	local UICorner_4 = Instance.new("UICorner") 	local BAR1 = Instance.new("Frame") 	local UICorner_5 = Instance.new("UICorner") 	local TextLabel = Instance.new("TextLabel") 	local Top = Instance.new("Frame") 	local UICorner_6 = Instance.new("UICorner") 	local TextLabel_2 = Instance.new("TextLabel") 	local TextLabel_3 = Instance.new("TextLabel") 	--Properties: 	Loading.Name = "Loading" 	Loading.Parent = game.CoreGui 	Loading.ZIndexBehavior = Enum.ZIndexBehavior.Sibling 	Blur.Name = "Blur" 	Blur.Parent = Loading 	Blur.BackgroundColor3 = Color3.fromRGB(0, 0, 0) 	Blur.BackgroundTransparency = 1 	Blur.Size = UDim2.new(1, 0, 1, 0) 	Main.Name = "Main" 	Main.Parent = Blur 	Main.AnchorPoint = Vector2.new(0.5, 0.5) 	Main.BackgroundColor3 = Color3.fromRGB(45, 45, 45) 	Main.ClipsDescendants = true 	Main.Position = UDim2.new(0.5, 0, 0.499241263, 0) 	Main.Size = UDim2.new(0, 500, 0, 300) 	UICorner.Parent = Main 	Logo.Name = "Logo" 	Logo.Parent = Main 	Logo.BackgroundColor3 = Color3.fromRGB(45, 45, 45) 	Logo.Position = UDim2.new(0.400000006, 0, 0.163333327, 0) 	Logo.Size = UDim2.new(0, 100, 0, 100) 	Logo.Image = "https://www.roblox.com/library/9879865083/sss-1" 	UICorner_2.CornerRadius = UDim.new(0, 100) 	UICorner_2.Parent = Logo 	Load.Name = "Load" 	Load.Parent = Main 	Load.BackgroundColor3 = Color3.fromRGB(35, 35, 35) 	Load.Position = UDim2.new(0, 15, 0, 170) 	Load.Size = UDim2.new(0, 470, 0, 115) 	UICorner_3.Parent = Load 	Bar.Name = "Bar" 	Bar.Parent = Load 	Bar.BackgroundColor3 = Color3.fromRGB(25, 25, 25) 	Bar.Position = UDim2.new(0, 15, 0, 80) 	Bar.Size = UDim2.new(0, 440, 0, 15) 	UICorner_4.CornerRadius = UDim.new(0, 5) 	UICorner_4.Parent = Bar 	BAR1.Name = "BAR1" 	BAR1.Parent = Bar 	BAR1.BackgroundColor3 = Color3.fromRGB(255,0,0) 	BAR1.Size = UDim2.new(0, 0, 0, 15) 	UICorner_5.CornerRadius = UDim.new(0, 5) 	UICorner_5.Parent = BAR1 	TextLabel.Parent = Load 	TextLabel.BackgroundColor3 = Color3.fromRGB(255, 255, 255) 	TextLabel.BackgroundTransparency = 1.000 	TextLabel.Position = UDim2.new(0.0319148935, 0, 0.173913032, 0) 	TextLabel.Size = UDim2.new(0, 440, 0, 25) 	TextLabel.Font = Enum.Font.GothamSemibold 	TextLabel.Text = "Loading" 	TextLabel.TextColor3 = Color3.fromRGB(225, 225, 225) 	TextLabel.TextSize = 16.000 	spawn(function() 		for i = 1,5 do 			wait(0.5) 			TextLabel.Text = "Loading." 			wait(0.5) 			TextLabel.Text = "Loading.." 			wait(0.5) 			TextLabel.Text = "Loading..." 		end 	end) 	Top.Name = "Top" 	Top.Parent = Main 	Top.BackgroundColor3 = Color3.fromRGB(35, 35, 35) 	Top.Size = UDim2.new(0, 500, 0, 30) 	UICorner_6.Parent = Top 	TextLabel_2.Parent = Top 	TextLabel_2.BackgroundColor3 = Color3.fromRGB(255, 255, 255) 	TextLabel_2.BackgroundTransparency = 1.000 	TextLabel_2.Position = UDim2.new(0.0299999993, 0, 0, 0) 	TextLabel_2.Size = UDim2.new(0, 61, 0, 30) 	TextLabel_2.Font = Enum.Font.GothamSemibold 	TextLabel_2.Text = " CAVENDER" 	TextLabel_2.TextColor3 = Color3.fromRGB(225, 225, 225) 	TextLabel_2.TextSize = 17.000 	TextLabel_3.Parent = Top 	TextLabel_3.BackgroundColor3 = Color3.fromRGB(255, 255, 255) 	TextLabel_3.BackgroundTransparency = 1.000 	TextLabel_3.Position = UDim2.new(0.151999995, 0, 0, 0) 	TextLabel_3.Size = UDim2.new(0, 61, 0, 30) 	TextLabel_3.Font = Enum.Font.GothamSemibold 	TextLabel_3.Text = " HUB" 	TextLabel_3.TextColor3 = Color3.fromRGB(255,0,0) 	TextLabel_3.TextSize = 17.000 	TextLabel_3.TextXAlignment = Enum.TextXAlignment.Left 	 	BAR1:TweenSize(UDim2.new(0,440,0,15),"Out","Linear",5,true) 	wait(5) Main:TweenSize(UDim2.new(0,0,0,0),"Out","Quad",0.4,true) wait(0.6) 	 	do 		local Load = game.CoreGui:FindFirstChild("Loading") 		if Load then 			Load:Destroy() 		end 	end end loading() local ScreenGui = Instance.new("ScreenGui") local ImageButton = Instance.new("ImageButton") ScreenGui.Parent = game.Players.LocalPlayer:WaitForChild("PlayerGui") ScreenGui.ZIndexBehavior = Enum.ZIndexBehavior.Sibling ImageButton.Parent = ScreenGui ImageButton.BackgroundColor3 = Color3.fromRGB(0, 0, 0) ImageButton.BorderSizePixel = 0 ImageButton.Position = UDim2.new(0.1208337, 0, 0.0952890813, 0) ImageButton.Size = UDim2.new(0, 50, 0, 50) ImageButton.Image = "" ImageButton.MouseButton1Down:connect(function() game:GetService("VirtualInputManager"):SendKeyEvent(true,305,false,game) game:GetService("VirtualInputManager"):SendKeyEvent(false,305,false,game) end) _G.FastAttack = true _G.AutoHaki = true _G.WalkOnWater = true Magnet = true do local GUI = game.CoreGui:FindFirstChild("CavenderHUB");if GUI then GUI:Destroy();end;if _G.Color == nil then _G.Color = Color3.fromRGB(255, 0, 0) end end local UserInputService = game:GetService("UserInputService") local TweenService = game:GetService("TweenService") local function MakeDraggable(topbarobject, object) local Dragging = nil local DragInput = nil local DragStart = nil local StartPosition = nil local function Update(input) local Delta = input.Position - DragStart local pos = UDim2.new(StartPosition.X.Scale, StartPosition.X.Offset + Delta.X, StartPosition.Y.Scale, StartPosition.Y.Offset + Delta.Y) local Tween = TweenService:Create(object, TweenInfo.new(0.15), {Position = pos}) Tween:Play() end topbarobject.InputBegan:Connect( function(input) if input.UserInputType == Enum.UserInputType.MouseButton1 or input.UserInputType == Enum.UserInputType.Touch then Dragging = true DragStart = input.Position StartPosition = object.Position input.Changed:Connect( function() if input.UserInputState == Enum.UserInputState.End then Dragging = false end end ) end end ) topbarobject.InputChanged:Connect( function(input) if input.UserInputType == Enum.UserInputType.MouseMovement or input.UserInputType == Enum.UserInputType.Touch then DragInput = input end end ) UserInputService.InputChanged:Connect( function(input) if input == DragInput and Dragging then Update(input) end end ) end local Update = {} function Update:Window(text,logo,keybind) local uihide = false local abc = false local logo = logo or 0 local currentpage = "" local keybind = keybind or Enum.KeyCode.RightControl local yoo = string.gsub(tostring(keybind),"Enum.KeyCode.","") local SHADOWHUB = Instance.new("ScreenGui") SHADOWHUB.Name = "SHADOWHUB" SHADOWHUB.Parent = game.CoreGui SHADOWHUB.ZIndexBehavior = Enum.ZIndexBehavior.Sibling local Main = Instance.new("Frame") Main.Name = "Main" Main.Parent = SHADOWHUB Main.ClipsDescendants = true Main.AnchorPoint = Vector2.new(0.5,0.5) Main.BackgroundColor3 = Color3.fromRGB(45, 45, 45) Main.Position = UDim2.new(0.5, 0, 0.5, 0) Main.Size = UDim2.new(0, 0, 0, 0) Main:TweenSize(UDim2.new(0, 656, 0, 400),"Out","Quad",0.4,true) local MCNR = Instance.new("UICorner") MCNR.Name = "MCNR" MCNR.Parent = Main local Top = Instance.new("Frame") Top.Name = "Top" Top.Parent = Main Top.BackgroundColor3 = Color3.fromRGB(35, 35, 35) Top.Size = UDim2.new(0, 656, 0, 27) local TCNR = Instance.new("UICorner") TCNR.Name = "TCNR" TCNR.Parent = Top local Logo = Instance.new("ImageLabel") Logo.Name = "Logo" Logo.Parent = Top Logo.BackgroundColor3 = Color3.fromRGB(255, 255, 255) Logo.BackgroundTransparency = 1.000 Logo.Position = UDim2.new(0, 10, 0, 1) Logo.Size = UDim2.new(0, 25, 0, 25) Logo.Image = "http://www.roblox.com/asset/?id=779739843"..tostring(logo) local Name = Instance.new("TextLabel") Name.Name = "Name" Name.Parent = Top Name.BackgroundColor3 = Color3.fromRGB(255, 255, 255) Name.BackgroundTransparency = 1.000 Name.Position = UDim2.new(0.0609756112, 0, 0, 0) Name.Size = UDim2.new(0, 61, 0, 27) Name.Font = Enum.Font.GothamSemibold Name.Text = text Name.TextColor3 = Color3.fromRGB(255, 255, 255) Name.TextSize = 17.000 local Hub = Instance.new("TextLabel") Hub.Name = "Hub" Hub.Parent = Top Hub.BackgroundColor3 = Color3.fromRGB(255, 255, 255) Hub.BackgroundTransparency = 1.000 Hub.Position = UDim2.new(0, 110, 0, 0) Hub.Size = UDim2.new(0, 81, 0, 27) Hub.Font = Enum.Font.GothamSemibold Hub.Text = " HUB" Hub.TextColor3 = _G.Color Hub.TextSize = 17.000 Hub.TextXAlignment = Enum.TextXAlignment.Left local BindButton = Instance.new("TextButton") BindButton.Name = "BindButton" BindButton.Parent = Top BindButton.BackgroundColor3 = Color3.fromRGB(255, 255, 255) BindButton.BackgroundTransparency = 1.000 BindButton.Position = UDim2.new(0.847561002, 0, 0, 0) BindButton.Size = UDim2.new(0, 100, 0, 27) BindButton.Font = Enum.Font.GothamSemibold BindButton.Text = "[ "..string.gsub(tostring(keybind),"Enum.KeyCode.","").." ]" BindButton.TextColor3 = Color3.fromRGB(100, 100, 100) BindButton.TextSize = 11.000 BindButton.MouseButton1Click:Connect(function () BindButton.Text = "[ ... ]" local inputwait = game:GetService("UserInputService").InputBegan:wait() local shiba = inputwait.KeyCode == Enum.KeyCode.Unknown and inputwait.UserInputType or inputwait.KeyCode if shiba.Name ~= "Focus" and shiba.Name ~= "MouseMovement" then BindButton.Text = "[ "..shiba.Name.." ]" yoo = shiba.Name end end) local Tab = Instance.new("Frame") Tab.Name = "Tab" Tab.Parent = Main Tab.BackgroundColor3 = Color3.fromRGB(35, 35, 35) Tab.Position = UDim2.new(0, 5, 0, 30) Tab.Size = UDim2.new(0, 150, 0, 365) local TCNR = Instance.new("UICorner") TCNR.Name = "TCNR" TCNR.Parent = Tab local ScrollTab = Instance.new("ScrollingFrame") ScrollTab.Name = "ScrollTab" ScrollTab.Parent = Tab ScrollTab.Active = true ScrollTab.BackgroundColor3 = Color3.fromRGB(255, 255, 255) ScrollTab.BackgroundTransparency = 1.000 ScrollTab.Size = UDim2.new(0, 150, 0, 365) ScrollTab.CanvasSize = UDim2.new(0, 0, 0, 0) ScrollTab.ScrollBarThickness = 0 local PLL = Instance.new("UIListLayout") PLL.Name = "PLL" PLL.Parent = ScrollTab PLL.SortOrder = Enum.SortOrder.LayoutOrder PLL.Padding = UDim.new(0, 15) local PPD = Instance.new("UIPadding") PPD.Name = "PPD" PPD.Parent = ScrollTab PPD.PaddingLeft = UDim.new(0, 10) PPD.PaddingTop = UDim.new(0, 10) local Page = Instance.new("Frame") Page.Name = "Page" Page.Parent = Main Page.BackgroundColor3 = Color3.fromRGB(35, 35, 35) Page.Position = UDim2.new(0.245426834, 0, 0.075000003, 0) Page.Size = UDim2.new(0, 490, 0, 365) local PCNR = Instance.new("UICorner") PCNR.Name = "PCNR" PCNR.Parent = Page local MainPage = Instance.new("Frame") MainPage.Name = "MainPage" MainPage.Parent = Page MainPage.ClipsDescendants = true MainPage.BackgroundColor3 = Color3.fromRGB(255, 255, 255) MainPage.BackgroundTransparency = 1.000 MainPage.Size = UDim2.new(0, 490, 0, 365) local PageList = Instance.new("Folder") PageList.Name = "PageList" PageList.Parent = MainPage local UIPageLayout = Instance.new("UIPageLayout") UIPageLayout.Parent = PageList UIPageLayout.SortOrder = Enum.SortOrder.LayoutOrder UIPageLayout.EasingDirection = Enum.EasingDirection.InOut UIPageLayout.EasingStyle = Enum.EasingStyle.Quad UIPageLayout.FillDirection = Enum.FillDirection.Vertical UIPageLayout.Padding = UDim.new(0, 15) UIPageLayout.TweenTime = 0.400 UIPageLayout.GamepadInputEnabled = false UIPageLayout.ScrollWheelInputEnabled = false UIPageLayout.TouchInputEnabled = false MakeDraggable(Top,Main) UserInputService.InputBegan:Connect(function(input) if input.KeyCode == Enum.KeyCode[yoo] then if uihide == false then uihide = true Main:TweenSize(UDim2.new(0, 0, 0, 0),"In","Quad",0.4,true) else uihide = false Main:TweenSize(UDim2.new(0, 656, 0, 400),"Out","Quad",0.4,true) end end end) local uitab = {} function uitab:Tab(text) local TabButton = Instance.new("TextButton") TabButton.Parent = ScrollTab TabButton.Name = text.."Server" TabButton.Text = text TabButton.BackgroundColor3 = Color3.fromRGB(255, 255, 255) TabButton.BackgroundTransparency = 1.000 TabButton.Size = UDim2.new(0, 130, 0, 23) TabButton.Font = Enum.Font.GothamSemibold TabButton.TextColor3 = Color3.fromRGB(255, 255, 255) TabButton.TextSize = 15.000 TabButton.TextTransparency = 0.500 local MainFramePage = Instance.new("ScrollingFrame") MainFramePage.Name = text.."_Page" MainFramePage.Parent = PageList MainFramePage.Active = true MainFramePage.BackgroundColor3 = Color3.fromRGB(255, 255, 255) MainFramePage.BackgroundTransparency = 1.000 MainFramePage.BorderSizePixel = 0 MainFramePage.Size = UDim2.new(0, 490, 0, 365) MainFramePage.CanvasSize = UDim2.new(0, 0, 0, 0) MainFramePage.ScrollBarThickness = 0 local UIPadding = Instance.new("UIPadding") local UIListLayout = Instance.new("UIListLayout") UIPadding.Parent = MainFramePage UIPadding.PaddingLeft = UDim.new(0, 10) UIPadding.PaddingTop = UDim.new(0, 10) UIListLayout.Padding = UDim.new(0,15) UIListLayout.Parent = MainFramePage UIListLayout.SortOrder = Enum.SortOrder.LayoutOrder TabButton.MouseButton1Click:Connect(function() for i,v in next, ScrollTab:GetChildren() do if v:IsA("TextButton") then TweenService:Create( v, TweenInfo.new(0.3,Enum.EasingStyle.Quad,Enum.EasingDirection.Out), {TextTransparency = 0.5} ):Play() end TweenService:Create( TabButton, TweenInfo.new(0.3,Enum.EasingStyle.Quad,Enum.EasingDirection.Out), {TextTransparency = 0} ):Play() end for i,v in next, PageList:GetChildren() do currentpage = string.gsub(TabButton.Name,"Server","").."_Page" if v.Name == currentpage then UIPageLayout:JumpTo(v) end end end) if abc == false then for i,v in next, ScrollTab:GetChildren() do if v:IsA("TextButton") then TweenService:Create( v, TweenInfo.new(0.3,Enum.EasingStyle.Quad,Enum.EasingDirection.Out), {TextTransparency = 0.5} ):Play() end TweenService:Create( TabButton, TweenInfo.new(0.3,Enum.EasingStyle.Quad,Enum.EasingDirection.Out), {TextTransparency = 0} ):Play() end UIPageLayout:JumpToIndex(1) abc = true end game:GetService("RunService").Stepped:Connect(function() pcall(function() MainFramePage.CanvasSize = UDim2.new(0,0,0,UIListLayout.AbsoluteContentSize.Y + 20) ScrollTab.CanvasSize = UDim2.new(0,0,0,PLL.AbsoluteContentSize.Y + 20) end) end) local main = {} function main:Button(text,callback) local Button = Instance.new("Frame") local UICorner = Instance.new("UICorner") local TextBtn = Instance.new("TextButton") local UICorner_2 = Instance.new("UICorner") local Black = Instance.new("Frame") local UICorner_3 = Instance.new("UICorner") Button.Name = "Button" Button.Parent = MainFramePage Button.BackgroundColor3 = _G.Color Button.Size = UDim2.new(0, 470, 0, 31) UICorner.CornerRadius = UDim.new(0, 5) UICorner.Parent = Button TextBtn.Name = "TextBtn" TextBtn.Parent = Button TextBtn.BackgroundColor3 = Color3.fromRGB(45, 45, 45) TextBtn.Position = UDim2.new(0, 1, 0, 1) TextBtn.Size = UDim2.new(0, 468, 0, 29) TextBtn.AutoButtonColor = false TextBtn.Font = Enum.Font.GothamSemibold TextBtn.Text = text TextBtn.TextColor3 = Color3.fromRGB(225, 225, 225) TextBtn.TextSize = 15.000 UICorner_2.CornerRadius = UDim.new(0, 5) UICorner_2.Parent = TextBtn Black.Name = "Black" Black.Parent = Button Black.BackgroundColor3 = Color3.fromRGB(0, 0, 0) Black.BackgroundTransparency = 1.000 Black.BorderSizePixel = 0 Black.Position = UDim2.new(0, 1, 0, 1) Black.Size = UDim2.new(0, 468, 0, 29) UICorner_3.CornerRadius = UDim.new(0, 5) UICorner_3.Parent = Black TextBtn.MouseEnter:Connect(function() TweenService:Create( Black, TweenInfo.new(0.4,Enum.EasingStyle.Quad,Enum.EasingDirection.Out), {BackgroundTransparency = 0.7} ):Play() end) TextBtn.MouseLeave:Connect(function() TweenService:Create( Black, TweenInfo.new(0.4,Enum.EasingStyle.Quad,Enum.EasingDirection.Out), {BackgroundTransparency = 1} ):Play() end) TextBtn.MouseButton1Click:Connect(function() TextBtn.TextSize = 0 TweenService:Create( TextBtn, TweenInfo.new(0.4,Enum.EasingStyle.Quad,Enum.EasingDirection.Out), {TextSize = 15} ):Play() callback() end) end function main:Toggle(text,config,callback) config = config or false local toggled = config local Toggle = Instance.new("Frame") local UICorner = Instance.new("UICorner") local Button = Instance.new("TextButton") local UICorner_2 = Instance.new("UICorner") local Label = Instance.new("TextLabel") local ToggleImage = Instance.new("Frame") local UICorner_3 = Instance.new("UICorner") local Circle = Instance.new("Frame") local UICorner_4 = Instance.new("UICorner") Toggle.Name = "Toggle" Toggle.Parent = MainFramePage Toggle.BackgroundColor3 = _G.Color Toggle.Size = UDim2.new(0, 470, 0, 31) UICorner.CornerRadius = UDim.new(0, 5) UICorner.Parent = Toggle Button.Name = "Button" Button.Parent = Toggle Button.BackgroundColor3 = Color3.fromRGB(45, 45, 45) Button.Position = UDim2.new(0, 1, 0, 1) Button.Size = UDim2.new(0, 468, 0, 29) Button.AutoButtonColor = false Button.Font = Enum.Font.SourceSans Button.Text = "" Button.TextColor3 = Color3.fromRGB(0, 0, 0) Button.TextSize = 11.000 UICorner_2.CornerRadius = UDim.new(0, 5) UICorner_2.Parent = Button Label.Name = "Label" Label.Parent = Toggle Label.BackgroundColor3 = Color3.fromRGB(255, 255, 255) Label.BackgroundTransparency = 1.000 Label.Position = UDim2.new(0, 1, 0, 1) Label.Size = UDim2.new(0, 468, 0, 29) Label.Font = Enum.Font.GothamSemibold Label.Text = text Label.TextColor3 = Color3.fromRGB(255, 255, 255) Label.TextSize = 15.000 ToggleImage.Name = "ToggleImage" ToggleImage.Parent = Toggle ToggleImage.BackgroundColor3 = Color3.fromRGB(225, 225, 225) ToggleImage.Position = UDim2.new(0, 415, 0, 5) ToggleImage.Size = UDim2.new(0, 45, 0, 20) UICorner_3.CornerRadius = UDim.new(0, 10) UICorner_3.Parent = ToggleImage Circle.Name = "Circle" Circle.Parent = ToggleImage Circle.BackgroundColor3 = Color3.fromRGB(227, 60, 60) Circle.Position = UDim2.new(0, 2, 0, 2) Circle.Size = UDim2.new(0, 16, 0, 16) UICorner_4.CornerRadius = UDim.new(0, 10) UICorner_4.Parent = Circle Button.MouseButton1Click:Connect(function() if toggled == false then toggled = true Circle:TweenPosition(UDim2.new(0,27,0,2),"Out","Sine",0.2,true) TweenService:Create( Circle, TweenInfo.new(0.4,Enum.EasingStyle.Quad,Enum.EasingDirection.Out), {BackgroundColor3 = _G.Color} ):Play() else toggled = false Circle:TweenPosition(UDim2.new(0,2,0,2),"Out","Sine",0.2,true) TweenService:Create( Circle, TweenInfo.new(0.4,Enum.EasingStyle.Quad,Enum.EasingDirection.Out), {BackgroundColor3 = Color3.fromRGB(227, 60, 110)} ):Play() end pcall(callback,toggled) end) if config == true then toggled = true Circle:TweenPosition(UDim2.new(0,27,0,2),"Out","Sine",0.4,true) TweenService:Create( Circle, TweenInfo.new(0.4,Enum.EasingStyle.Quad,Enum.EasingDirection.Out), {BackgroundColor3 = _G.Color} ):Play() pcall(callback,toggled) end end function main:Dropdown(text,option,callback) local isdropping = false local Dropdown = Instance.new("Frame") local UICorner = Instance.new("UICorner") local DropTitle = Instance.new("TextLabel") local DropScroll = Instance.new("ScrollingFrame") local UIListLayout = Instance.new("UIListLayout") local UIPadding = Instance.new("UIPadding") local DropButton = Instance.new("TextButton") local DropImage = Instance.new("ImageLabel") Dropdown.Name = "Dropdown" Dropdown.Parent = MainFramePage Dropdown.BackgroundColor3 = Color3.fromRGB(45, 45, 45) Dropdown.ClipsDescendants = true Dropdown.Size = UDim2.new(0, 470, 0, 31) UICorner.CornerRadius = UDim.new(0, 5) UICorner.Parent = Dropdown DropTitle.Name = "DropTitle" DropTitle.Parent = Dropdown DropTitle.BackgroundColor3 = Color3.fromRGB(255, 255, 255) DropTitle.BackgroundTransparency = 1.000 DropTitle.Size = UDim2.new(0, 470, 0, 31) DropTitle.Font = Enum.Font.GothamSemibold DropTitle.Text = text.. " : " DropTitle.TextColor3 = Color3.fromRGB(225, 225, 225) DropTitle.TextSize = 15.000 DropScroll.Name = "DropScroll" DropScroll.Parent = DropTitle DropScroll.Active = true DropScroll.BackgroundColor3 = Color3.fromRGB(255, 255, 255) DropScroll.BackgroundTransparency = 1.000 DropScroll.BorderSizePixel = 0 DropScroll.Position = UDim2.new(0, 0, 0, 31) DropScroll.Size = UDim2.new(0, 470, 0, 100) DropScroll.CanvasSize = UDim2.new(0, 0, 0, 0) DropScroll.ScrollBarThickness = 3 UIListLayout.Parent = DropScroll UIListLayout.SortOrder = Enum.SortOrder.LayoutOrder UIListLayout.Padding = UDim.new(0, 5) UIPadding.Parent = DropScroll UIPadding.PaddingLeft = UDim.new(0, 5) UIPadding.PaddingTop = UDim.new(0, 5) DropImage.Name = "DropImage" DropImage.Parent = Dropdown DropImage.BackgroundColor3 = Color3.fromRGB(255, 255, 255) DropImage.BackgroundTransparency = 1.000 DropImage.Position = UDim2.new(0, 445, 0, 6) DropImage.Rotation = 180.000 DropImage.Size = UDim2.new(0, 20, 0, 20) DropImage.Image = "rbxassetid://6031090990" DropButton.Name = "DropButton" DropButton.Parent = Dropdown DropButton.BackgroundColor3 = Color3.fromRGB(255, 255, 255) DropButton.BackgroundTransparency = 1.000 DropButton.Size = UDim2.new(0, 470, 0, 31) DropButton.Font = Enum.Font.SourceSans DropButton.Text = "" DropButton.TextColor3 = Color3.fromRGB(0, 0, 0) DropButton.TextSize = 14.000 for i,v in next,option do local Item = Instance.new("TextButton") Item.Name = "Item" Item.Parent = DropScroll Item.BackgroundColor3 = Color3.fromRGB(255, 255, 255) Item.BackgroundTransparency = 1.000 Item.Size = UDim2.new(0, 460, 0, 26) Item.Font = Enum.Font.GothamSemibold Item.Text = tostring(v) Item.TextColor3 = Color3.fromRGB(225, 225, 225) Item.TextSize = 13.000 Item.TextTransparency = 0.500 Item.MouseEnter:Connect(function() TweenService:Create( Item, TweenInfo.new(0.3,Enum.EasingStyle.Quad,Enum.EasingDirection.Out), {TextTransparency = 0} ):Play() end) Item.MouseLeave:Connect(function() TweenService:Create( Item, TweenInfo.new(0.3,Enum.EasingStyle.Quad,Enum.EasingDirection.Out), {TextTransparency = 0.5} ):Play() end) Item.MouseButton1Click:Connect(function() isdropping = false Dropdown:TweenSize(UDim2.new(0,470,0,31),"Out","Quad",0.3,true) TweenService:Create( DropImage, TweenInfo.new(0.3,Enum.EasingStyle.Quad,Enum.EasingDirection.Out), {Rotation = 180} ):Play() callback(Item.Text) DropTitle.Text = text.." : "..Item.Text end) end DropScroll.CanvasSize = UDim2.new(0,0,0,UIListLayout.AbsoluteContentSize.Y + 10) DropButton.MouseButton1Click:Connect(function() if isdropping == false then isdropping = true Dropdown:TweenSize(UDim2.new(0,470,0,131),"Out","Quad",0.3,true) TweenService:Create( DropImage, TweenInfo.new(0.3,Enum.EasingStyle.Quad,Enum.EasingDirection.Out), {Rotation = 0} ):Play() else isdropping = false Dropdown:TweenSize(UDim2.new(0,470,0,31),"Out","Quad",0.3,true) TweenService:Create( DropImage, TweenInfo.new(0.3,Enum.EasingStyle.Quad,Enum.EasingDirection.Out), {Rotation = 180} ):Play() end end) local dropfunc = {} function dropfunc:Add(t) local Item = Instance.new("TextButton") Item.Name = "Item" Item.Parent = DropScroll Item.BackgroundColor3 = Color3.fromRGB(255, 255, 255) Item.BackgroundTransparency = 1.000 Item.Size = UDim2.new(0, 470, 0, 26) Item.Font = Enum.Font.GothamSemibold Item.Text = tostring(t) Item.TextColor3 = Color3.fromRGB(225, 225, 225) Item.TextSize = 13.000 Item.TextTransparency = 0.500 Item.MouseEnter:Connect(function() TweenService:Create( Item, TweenInfo.new(0.3,Enum.EasingStyle.Quad,Enum.EasingDirection.Out), {TextTransparency = 0} ):Play() end) Item.MouseLeave:Connect(function() TweenService:Create( Item, TweenInfo.new(0.3,Enum.EasingStyle.Quad,Enum.EasingDirection.Out), {TextTransparency = 0.5} ):Play() end) Item.MouseButton1Click:Connect(function() isdropping = false Dropdown:TweenSize(UDim2.new(0,470,0,31),"Out","Quad",0.3,true) TweenService:Create( DropImage, TweenInfo.new(0.3,Enum.EasingStyle.Quad,Enum.EasingDirection.Out), {Rotation = 180} ):Play() callback(Item.Text) DropTitle.Text = text.." : "..Item.Text end) end function dropfunc:Clear() DropTitle.Text = tostring(text).." : " isdropping = false Dropdown:TweenSize(UDim2.new(0,470,0,31),"Out","Quad",0.3,true) TweenService:Create( DropImage, TweenInfo.new(0.3,Enum.EasingStyle.Quad,Enum.EasingDirection.Out), {Rotation = 180} ):Play() for i,v in next, DropScroll:GetChildren() do if v:IsA("TextButton") then v:Destroy() end end end return dropfunc end function main:Slider(text,min,max,set,callback) local Slider = Instance.new("Frame") local slidercorner = Instance.new("UICorner") local sliderr = Instance.new("Frame") local sliderrcorner = Instance.new("UICorner") local SliderLabel = Instance.new("TextLabel") local HAHA = Instance.new("Frame") local AHEHE = Instance.new("TextButton") local bar = Instance.new("Frame") local bar1 = Instance.new("Frame") local bar1corner = Instance.new("UICorner") local barcorner = Instance.new("UICorner") local circlebar = Instance.new("Frame") local UICorner = Instance.new("UICorner") local slidervalue = Instance.new("Frame") local valuecorner = Instance.new("UICorner") local TextBox = Instance.new("TextBox") local UICorner_2 = Instance.new("UICorner") Slider.Name = "Slider" Slider.Parent = MainFramePage Slider.BackgroundColor3 = _G.Color Slider.BackgroundTransparency = 0 Slider.Size = UDim2.new(0, 470, 0, 51) slidercorner.CornerRadius = UDim.new(0, 5) slidercorner.Name = "slidercorner" slidercorner.Parent = Slider sliderr.Name = "sliderr" sliderr.Parent = Slider sliderr.BackgroundColor3 = Color3.fromRGB(45, 45, 45) sliderr.Position = UDim2.new(0, 1, 0, 1) sliderr.Size = UDim2.new(0, 468, 0, 49) sliderrcorner.CornerRadius = UDim.new(0, 5) sliderrcorner.Name = "sliderrcorner" sliderrcorner.Parent = sliderr SliderLabel.Name = "SliderLabel" SliderLabel.Parent = sliderr SliderLabel.BackgroundColor3 = Color3.fromRGB(255, 255, 255) SliderLabel.BackgroundTransparency = 1.000 SliderLabel.Position = UDim2.new(0, 15, 0, 0) SliderLabel.Size = UDim2.new(0, 180, 0, 26) SliderLabel.Font = Enum.Font.GothamSemibold SliderLabel.Text = text SliderLabel.TextColor3 = Color3.fromRGB(225, 225, 225) SliderLabel.TextSize = 16.000 SliderLabel.TextTransparency = 0 SliderLabel.TextXAlignment = Enum.TextXAlignment.Left HAHA.Name = "HAHA" HAHA.Parent = sliderr HAHA.BackgroundColor3 = Color3.fromRGB(255, 255, 255) HAHA.BackgroundTransparency = 1.000 HAHA.Size = UDim2.new(0, 468, 0, 29) AHEHE.Name = "AHEHE" AHEHE.Parent = sliderr AHEHE.BackgroundColor3 = Color3.fromRGB(255, 255, 255) AHEHE.BackgroundTransparency = 1.000 AHEHE.Position = UDim2.new(0, 10, 0, 35) AHEHE.Size = UDim2.new(0, 448, 0, 5) AHEHE.Font = Enum.Font.SourceSans AHEHE.Text = "" AHEHE.TextColor3 = Color3.fromRGB(0, 0, 0) AHEHE.TextSize = 14.000 bar.Name = "bar" bar.Parent = AHEHE bar.BackgroundColor3 = Color3.fromRGB(35, 35, 35) bar.Size = UDim2.new(0, 448, 0, 5) bar1.Name = "bar1" bar1.Parent = bar bar1.BackgroundColor3 = _G.Color bar1.BackgroundTransparency = 0 bar1.Size = UDim2.new(set/max, 0, 0, 5) bar1corner.CornerRadius = UDim.new(0, 5) bar1corner.Name = "bar1corner" bar1corner.Parent = bar1 barcorner.CornerRadius = UDim.new(0, 5) barcorner.Name = "barcorner" barcorner.Parent = bar circlebar.Name = "circlebar" circlebar.Parent = bar1 circlebar.BackgroundColor3 = Color3.fromRGB(225, 225, 225) circlebar.Position = UDim2.new(1, -2, 0, -3) circlebar.Size = UDim2.new(0, 10, 0, 10) UICorner.CornerRadius = UDim.new(0, 100) UICorner.Parent = circlebar slidervalue.Name = "slidervalue" slidervalue.Parent = sliderr slidervalue.BackgroundColor3 = _G.Color slidervalue.BackgroundTransparency = 0 slidervalue.Position = UDim2.new(0, 395, 0, 5) slidervalue.Size = UDim2.new(0, 65, 0, 18) valuecorner.CornerRadius = UDim.new(0, 5) valuecorner.Name = "valuecorner" valuecorner.Parent = slidervalue TextBox.Parent = slidervalue TextBox.BackgroundColor3 = Color3.fromRGB(35, 35, 35) TextBox.Position = UDim2.new(0, 1, 0, 1) TextBox.Size = UDim2.new(0, 63, 0, 16) TextBox.Font = Enum.Font.GothamSemibold TextBox.TextColor3 = Color3.fromRGB(225, 225, 225) TextBox.TextSize = 9.000 TextBox.Text = set TextBox.TextTransparency = 0 UICorner_2.CornerRadius = UDim.new(0, 5) UICorner_2.Parent = TextBox local mouse = game.Players.LocalPlayer:GetMouse() local uis = game:GetService("UserInputService") if Value == nil then Value = set pcall(function() callback(Value) end) end AHEHE.MouseButton1Down:Connect(function() Value = math.floor((((tonumber(max) - tonumber(min)) / 448) * bar1.AbsoluteSize.X) + tonumber(min)) or 0 pcall(function() callback(Value) end) bar1.Size = UDim2.new(0, math.clamp(mouse.X - bar1.AbsolutePosition.X, 0, 448), 0, 5) circlebar.Position = UDim2.new(0, math.clamp(mouse.X - bar1.AbsolutePosition.X - 2, 0, 438), 0, -3) moveconnection = mouse.Move:Connect(function() TextBox.Text = Value Value = math.floor((((tonumber(max) - tonumber(min)) / 448) * bar1.AbsoluteSize.X) + tonumber(min)) pcall(function() callback(Value) end) bar1.Size = UDim2.new(0, math.clamp(mouse.X - bar1.AbsolutePosition.X, 0, 448), 0, 5) circlebar.Position = UDim2.new(0, math.clamp(mouse.X - bar1.AbsolutePosition.X - 2, 0, 438), 0, -3) end) releaseconnection = uis.InputEnded:Connect(function(Mouse) if Mouse.UserInputType == Enum.UserInputType.MouseButton1 then Value = math.floor((((tonumber(max) - tonumber(min)) / 448) * bar1.AbsoluteSize.X) + tonumber(min)) pcall(function() callback(Value) end) bar1.Size = UDim2.new(0, math.clamp(mouse.X - bar1.AbsolutePosition.X, 0, 448), 0, 5) circlebar.Position = UDim2.new(0, math.clamp(mouse.X - bar1.AbsolutePosition.X - 2, 0, 438), 0, -3) moveconnection:Disconnect() releaseconnection:Disconnect() end end) end) releaseconnection = uis.InputEnded:Connect(function(Mouse) if Mouse.UserInputType == Enum.UserInputType.MouseButton1 then Value = math.floor((((tonumber(max) - tonumber(min)) / 448) * bar1.AbsoluteSize.X) + tonumber(min)) TextBox.Text = Value end end) TextBox.FocusLost:Connect(function() if tonumber(TextBox.Text) > max then TextBox.Text = max end bar1.Size = UDim2.new((TextBox.Text or 0) / max, 0, 0, 5) circlebar.Position = UDim2.new(1, -2, 0, -3) TextBox.Text = tostring(TextBox.Text and math.floor( (TextBox.Text / max) * (max - min) + min) ) pcall(callback, TextBox.Text) end) end function main:Textbox(text,disappear,callback) local Textbox = Instance.new("Frame") local TextboxCorner = Instance.new("UICorner") local Textboxx = Instance.new("Frame") local TextboxxCorner = Instance.new("UICorner") local TextboxLabel = Instance.new("TextLabel") local txtbtn = Instance.new("TextButton") local RealTextbox = Instance.new("TextBox") local UICorner = Instance.new("UICorner") Textbox.Name = "Textbox" Textbox.Parent = MainFramePage Textbox.BackgroundColor3 = _G.Color Textbox.BackgroundTransparency = 0 Textbox.Size = UDim2.new(0, 470, 0, 31) TextboxCorner.CornerRadius = UDim.new(0, 5) TextboxCorner.Name = "TextboxCorner" TextboxCorner.Parent = Textbox Textboxx.Name = "Textboxx" Textboxx.Parent = Textbox Textboxx.BackgroundColor3 = Color3.fromRGB(45, 45, 45) Textboxx.Position = UDim2.new(0, 1, 0, 1) Textboxx.Size = UDim2.new(0, 468, 0, 29) TextboxxCorner.CornerRadius = UDim.new(0, 5) TextboxxCorner.Name = "TextboxxCorner" TextboxxCorner.Parent = Textboxx TextboxLabel.Name = "TextboxLabel" TextboxLabel.Parent = Textbox TextboxLabel.BackgroundColor3 = Color3.fromRGB(255, 255, 255) TextboxLabel.BackgroundTransparency = 1.000 TextboxLabel.Position = UDim2.new(0, 15, 0, 0) TextboxLabel.Text = text TextboxLabel.Size = UDim2.new(0, 145, 0, 31) TextboxLabel.Font = Enum.Font.GothamSemibold TextboxLabel.TextColor3 = Color3.fromRGB(225, 225, 225) TextboxLabel.TextSize = 16.000 TextboxLabel.TextTransparency = 0 TextboxLabel.TextXAlignment = Enum.TextXAlignment.Left txtbtn.Name = "txtbtn" txtbtn.Parent = Textbox txtbtn.BackgroundColor3 = Color3.fromRGB(255, 255, 255) txtbtn.BackgroundTransparency = 1.000 txtbtn.Position = UDim2.new(0, 1, 0, 1) txtbtn.Size = UDim2.new(0, 468, 0, 29) txtbtn.Font = Enum.Font.SourceSans txtbtn.Text = "" txtbtn.TextColor3 = Color3.fromRGB(0, 0, 0) txtbtn.TextSize = 14.000 RealTextbox.Name = "RealTextbox" RealTextbox.Parent = Textbox RealTextbox.BackgroundColor3 = Color3.fromRGB(35, 35, 35) RealTextbox.BackgroundTransparency = 0 RealTextbox.Position = UDim2.new(0, 360, 0, 4) RealTextbox.Size = UDim2.new(0, 100, 0, 24) RealTextbox.Font = Enum.Font.GothamSemibold RealTextbox.Text = "" RealTextbox.TextColor3 = Color3.fromRGB(225, 225, 225) RealTextbox.TextSize = 11.000 RealTextbox.TextTransparency = 0 RealTextbox.FocusLost:Connect(function() callback(RealTextbox.Text) if disappear then RealTextbox.Text = "" end end) UICorner.CornerRadius = UDim.new(0, 5) UICorner.Parent = RealTextbox end function main:Label(text) local Label = Instance.new("TextLabel") local PaddingLabel = Instance.new("UIPadding") local labelfunc = {} Label.Name = "Label" Label.Parent = MainFramePage Label.BackgroundColor3 = Color3.fromRGB(255, 255, 255) Label.BackgroundTransparency = 1.000 Label.Size = UDim2.new(0, 470, 0, 20) Label.Font = Enum.Font.GothamSemibold Label.TextColor3 = Color3.fromRGB(225, 225, 225) Label.TextSize = 16.000 Label.Text = text Label.TextXAlignment = Enum.TextXAlignment.Left PaddingLabel.PaddingLeft = UDim.new(0,15) PaddingLabel.Parent = Label PaddingLabel.Name = "PaddingLabel" function labelfunc:Set(newtext) Label.Text = newtext end return labelfunc end function main:Seperator(text) local Seperator = Instance.new("Frame") local Sep1 = Instance.new("Frame") local Sep2 = Instance.new("TextLabel") local Sep3 = Instance.new("Frame") Seperator.Name = "Seperator" Seperator.Parent = MainFramePage Seperator.BackgroundColor3 = Color3.fromRGB(255, 255, 255) Seperator.BackgroundTransparency = 1.000 Seperator.Size = UDim2.new(0, 470, 0, 20) Sep1.Name = "Sep1" Sep1.Parent = Seperator Sep1.BackgroundColor3 = _G.Color Sep1.BorderSizePixel = 0 Sep1.Position = UDim2.new(0, 0, 0, 10) Sep1.Size = UDim2.new(0, 80, 0, 1) Sep2.Name = "Sep2" Sep2.Parent = Seperator Sep2.BackgroundColor3 = Color3.fromRGB(255, 255, 255) Sep2.BackgroundTransparency = 1.000 Sep2.Position = UDim2.new(0, 185, 0, 0) Sep2.Size = UDim2.new(0, 100, 0, 20) Sep2.Font = Enum.Font.GothamSemibold Sep2.Text = text Sep2.TextColor3 = Color3.fromRGB(255, 255, 255) Sep2.TextSize = 14.000 Sep3.Name = "Sep3" Sep3.Parent = Seperator Sep3.BackgroundColor3 = _G.Color Sep3.BorderSizePixel = 0 Sep3.Position = UDim2.new(0, 390, 0, 10) Sep3.Size = UDim2.new(0, 80, 0, 1) end function main:Line() local Linee = Instance.new("Frame") local Line = Instance.new("Frame") Linee.Name = "Linee" Linee.Parent = MainFramePage Linee.BackgroundColor3 = Color3.fromRGB(255, 255, 255) Linee.BackgroundTransparency = 1.000 Linee.Position = UDim2.new(0, 0, 0.119999997, 0) Linee.Size = UDim2.new(0, 470, 0, 20) Line.Name = "Line" Line.Parent = Linee Line.BackgroundColor3 = _G.Color Line.BorderSizePixel = 0 Line.Position = UDim2.new(0, 0, 0, 10) Line.Size = UDim2.new(0, 470, 0, 1) end return main end return uitab end -- Function's ----------------------------------------------------------------------------------------- spawn(function() while wait(.1) do if _G.AutoHaki then if game.Players.LocalPlayer.Character:FindFirstChild("HasBuso") then else local args = { [1] = "Buso" } game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer(unpack(args)) end end if _G.AutoHakiObs then if game.Players.LocalPlayer.PlayerGui.ScreenGui:FindFirstChild("ImageLabel") then else wait(1) local virtualUser = game:GetService('VirtualUser') virtualUser:CaptureController() virtualUser:SetKeyDown('0x65') wait(2) virtualUser:SetKeyUp('0x65') end end end end) spawn(function() pcall(function() while wait() do if _G.WalkOnWater or _G.Auto_Farm_Level then if game:GetService("Players").LocalPlayer.Character.HumanoidRootPart.CFrame.Y <= 1 then if not game:GetService("Workspace"):FindFirstChild("Water") then local Water = Instance.new("Part", game:GetService("Workspace")) Water.Name = "Water" Water.Size = Vector3.new(15,0.5,15) Water.Anchored = true Water.Material = "Neon" Water.Color = _G.Color game:GetService("Workspace").Water.CFrame = CFrame.new(game:GetService("Players").LocalPlayer.Character.HumanoidRootPart.CFrame.X,game:GetService("Workspace").Camera["Water;"].CFrame.Y,game:GetService("Players").LocalPlayer.Character.HumanoidRootPart.CFrame.Z) else game:GetService("Workspace").Water.CFrame = CFrame.new(game:GetService("Players").LocalPlayer.Character.HumanoidRootPart.CFrame.X,game:GetService("Workspace").Camera["Water;"].CFrame.Y,game:GetService("Players").LocalPlayer.Character.HumanoidRootPart.CFrame.Z) end elseif game:GetService("Players").LocalPlayer.Character.HumanoidRootPart.CFrame.Y >= 1 and game:GetService("Workspace"):FindFirstChild("Water") then game:GetService("Workspace"):FindFirstChild("Water"):Destroy() end else if game:GetService("Workspace"):FindFirstChild("Water") then game:GetService("Workspace"):FindFirstChild("Water"):Destroy() end end end end) end) spawn(function() game:GetService("RunService").Heartbeat:Connect(function() if _G.Auto_Farm_Level or Auto_Bone or TeleportPly or NextIsland then if not game:GetService("Workspace"):FindFirstChild("LOL") then local LOL = Instance.new("Part") LOL.Name = "LOL" LOL.Parent = game.Workspace LOL.Anchored = true LOL.Transparency = 1 LOL.Size = Vector3.new(30,0.5,30) elseif game:GetService("Workspace"):FindFirstChild("LOL") then game.Workspace["LOL"].CFrame = game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame * CFrame.new(0, -3.6, 0) end else if game:GetService("Workspace"):FindFirstChild("LOL") then game:GetService("Workspace"):FindFirstChild("LOL"):Destroy() end end end) end) spawn(function() game:GetService("RunService").Stepped:Connect(function() if _G.Auto_Farm_Level or Auto_Bone or TeleportPly or NextIsland then for _, v in pairs(game.Players.LocalPlayer.Character:GetDescendants()) do if v:IsA("BasePart") then v.CanCollide = false end end end end) end) game:GetService("RunService").Heartbeat:Connect(function() for i,v in pairs(game:GetService("Workspace")["_WorldOrigin"]:GetChildren()) do pcall(function() if v.Name == ("CurvedRing") or v.Name == ("SlashHit") or v.Name == ("DamageCounter") or v.Name == ("SwordSlash") or v.Name == ("SlashTail") or v.Name == ("Sounds") then v:Destroy() end end) end end) local CameraShaker = require(game.ReplicatedStorage.Util.CameraShaker) CombatFrameworkR = require(game:GetService("Players").LocalPlayer.PlayerScripts.CombatFramework) y = debug.getupvalues(CombatFrameworkR)[2] spawn(function() game:GetService("RunService").RenderStepped:Connect(function() if _G.FastAttack then if typeof(y) == "table" then pcall(function() CameraShaker:Stop() y.activeController.timeToNextAttack = (math.huge^math.huge^math.huge) y.activeController.timeToNextAttack = 0 y.activeController.hitboxMagnitude = 150 y.activeController.timeToNextBlock = 0 y.activeController.focusStart = 0 y.activeController.increment = 3 y.activeController.blocking = false y.activeController.attacking = false y.activeController.humanoid.AutoRotate = true end) end end end) end) spawn(function() while task.wait() do pcall(function() if Magnet then CheckQuest() for i,v in pairs(game:GetService("Workspace").Enemies:GetChildren()) do if _G.Auto_Farm_Level and MagnetActive and v.Name == Mon and (Mon == "Factory Staff [Lv. 800]" or Mon == "Monkey [Lv. 14]" or Mon == "Dragon Crew Warrior [Lv. 1575]" or Mon == "Dragon Crew Archer [Lv. 1600]") and v:FindFirstChild("Humanoid") and v:FindFirstChild("HumanoidRootPart") and v.Humanoid.Health > 0 and (v.HumanoidRootPart.Position - game:GetService("Players").LocalPlayer.Character.HumanoidRootPart.Position).Magnitude <= 300 then v.HumanoidRootPart.Size = Vector3.new(80,80,80) v.HumanoidRootPart.CFrame = PosMon v.Humanoid:ChangeState(14) v.HumanoidRootPart.CanCollide = false v.Head.CanCollide = false if v.Humanoid:FindFirstChild("Animator") then v.Humanoid.Animator:Destroy() end sethiddenproperty(game:GetService("Players").LocalPlayer,"SimulationRadius",math.huge) elseif _G.Auto_Farm_Level and MagnetActive and v.Name == Mon and v:FindFirstChild("Humanoid") and v:FindFirstChild("HumanoidRootPart") and v.Humanoid.Health > 0 and (v.HumanoidRootPart.Position - game:GetService("Players").LocalPlayer.Character.HumanoidRootPart.Position).Magnitude <= 300 then v.HumanoidRootPart.Size = Vector3.new(80,80,80) v.HumanoidRootPart.CFrame = PosMon v.Humanoid:ChangeState(14) v.HumanoidRootPart.CanCollide = false v.Head.CanCollide = false if v.Humanoid:FindFirstChild("Animator") then v.Humanoid.Animator:Destroy() end sethiddenproperty(game:GetService("Players").LocalPlayer,"SimulationRadius",math.huge) elseif Auto_Bone and BoneMagnet then if (v.Name == "Reborn Skeleton [Lv. 1975]" or v.Name == "Living Zombie [Lv. 2000]" or v.Name == "Demonic Soul [Lv. 2025]" or v.Name == "Posessed Mummy [Lv. 2050]") and (v.HumanoidRootPart.Position - MainMonBone.Position).Magnitude <= 300 then v.Head.CanCollide = false v.HumanoidRootPart.CanCollide = false v.Humanoid:ChangeState(14) v.HumanoidRootPart.Size = Vector3.new(80,80,80) v.HumanoidRootPart.CFrame = MainMonBone elseif v.Humanoid:FindFirstChild("Animator") then v.Humanoid.Animator:Destroy() if sethiddenproperty then sethiddenproperty(game.Players.LocalPlayer, "SimulationRadius", 10000) end sethiddenproperty(game.Players.LocalPlayer, "SimulationRadius", math.huge) elseif _G.AutoDoughtBoss and MagnetDought then if (v.Name == "Cookie Crafter [Lv. 2200]" or v.Name == "Cake Guard [Lv. 2225]" or v.Name == "Baking Staff [Lv. 2250]" or v.Name == "Head Baker [Lv. 2275]") and (v.HumanoidRootPart.Position - PosMonDoughtOpenDoor.Position).Magnitude <= 300 and v:FindFirstChild("Humanoid") and v:FindFirstChild("HumanoidRootPart") and v.Humanoid.Health > 0 then v.HumanoidRootPart.Size = Vector3.new(80,80,80) v.Humanoid:ChangeState(14) v.HumanoidRootPart.CanCollide = false v.Head.CanCollide = false v.HumanoidRootPart.CFrame = PosMonDoughtOpenDoor if v.Humanoid:FindFirstChild("Animator") then v.Humanoid.Animator:Destroy() end sethiddenproperty(game:GetService("Players").LocalPlayer, "SimulationRadius", math.huge) end end end end end end) end end) -- Main Script's local Library = Update:Window("CAVENDER","",Enum.KeyCode.RightControl); Main = Library:Tab("Main") Stats = Library:Tab("Stats") Shop = Library:Tab("Shop") Island = Library:Tab("Island") Player = Library:Tab("Player") Dungeon = Library:Tab("Dungeon") Misc = Library:Tab("Misc") Main:Seperator("Main") ------------------------------------------------------------------------------------------- function CheckLevel() local Lv = game:GetService("Players").LocalPlayer.Data.Level.Value if Old_World then if Lv == 1 or Lv <= 9 or SelectMonster == "Bandit [Lv. 5]" then -- Bandit Ms = "Bandit [Lv. 5]" NameQuest = "BanditQuest1" QuestLv = 1 NameMon = "Bandit" CFrameQ = CFrame.new(1060.9383544922, 16.455066680908, 1547.7841796875) CFrameMon = CFrame.new(1038.5533447266, 41.296249389648, 1576.5098876953) elseif Lv == 10 or Lv <= 14 or SelectMonster == "Monkey [Lv. 14]" then -- Monkey Ms = "Monkey [Lv. 14]" NameQuest = "JungleQuest" QuestLv = 1 NameMon = "Monkey" CFrameQ = CFrame.new(-1601.6553955078, 36.85213470459, 153.38809204102) CFrameMon = CFrame.new(-1448.1446533203, 50.851993560791, 63.60718536377) elseif Lv == 15 or Lv <= 29 or SelectMonster == "Gorilla [Lv. 20]" then -- Gorilla Ms = "Gorilla [Lv. 20]" NameQuest = "JungleQuest" QuestLv = 2 NameMon = "Gorilla" CFrameQ = CFrame.new(-1601.6553955078, 36.85213470459, 153.38809204102) CFrameMon = CFrame.new(-1142.6488037109, 40.462348937988, -515.39227294922) elseif Lv == 30 or Lv <= 39 or SelectMonster == "Pirate [Lv. 35]" then -- Pirate Ms = "Pirate [Lv. 35]" NameQuest = "BuggyQuest1" QuestLv = 1 NameMon = "Pirate" CFrameQ = CFrame.new(-1140.1761474609, 4.752049446106, 3827.4057617188) CFrameMon = CFrame.new(-1201.0881347656, 40.628940582275, 3857.5966796875) elseif Lv == 40 or Lv <= 59 or SelectMonster == "Brute [Lv. 45]" then -- Brute Ms = "Brute [Lv. 45]" NameQuest = "BuggyQuest1" QuestLv = 2 NameMon = "Brute" CFrameQ = CFrame.new(-1140.1761474609, 4.752049446106, 3827.4057617188) CFrameMon = CFrame.new(-1387.5324707031, 24.592035293579, 4100.9575195313) elseif Lv == 60 or Lv <= 74 or SelectMonster == "Desert Bandit [Lv. 60]" then -- Desert Bandit Ms = "Desert Bandit [Lv. 60]" NameQuest = "DesertQuest" QuestLv = 1 NameMon = "Desert Bandit" CFrameQ = CFrame.new(896.51721191406, 6.4384617805481, 4390.1494140625) CFrameMon = CFrame.new(984.99896240234, 16.109552383423, 4417.91015625) elseif Lv == 75 or Lv <= 89 or SelectMonster == "Desert Officer [Lv. 70]" then -- Desert Officer Ms = "Desert Officer [Lv. 70]" NameQuest = "DesertQuest" QuestLv = 2 NameMon = "Desert Officer" CFrameQ = CFrame.new(896.51721191406, 6.4384617805481, 4390.1494140625) CFrameMon = CFrame.new(1547.1510009766, 14.452038764954, 4381.8002929688) elseif Lv == 90 or Lv <= 99 or SelectMonster == "Snow Bandit [Lv. 90]" then -- Snow Bandit Ms = "Snow Bandit [Lv. 90]" NameQuest = "SnowQuest" QuestLv = 1 NameMon = "Snow Bandit" CFrameQ = CFrame.new(1386.8073730469, 87.272789001465, -1298.3576660156) CFrameMon = CFrame.new(1356.3028564453, 105.76865386963, -1328.2418212891) elseif Lv == 100 or Lv <= 119 or SelectMonster == "Snowman [Lv. 100]" then -- Snowman Ms = "Snowman [Lv. 100]" NameQuest = "SnowQuest" QuestLv = 2 NameMon = "Snowman" CFrameQ = CFrame.new(1386.8073730469, 87.272789001465, -1298.3576660156) CFrameMon = CFrame.new(1218.7956542969, 138.01184082031, -1488.0262451172) elseif Lv == 120 or Lv <= 149 or SelectMonster == "Chief Petty Officer [Lv. 120]" then -- Chief Petty Officer Ms = "Chief Petty Officer [Lv. 120]" NameQuest = "MarineQuest2" QuestLv = 1 NameMon = "Chief Petty Officer" CFrameQ = CFrame.new(-5035.49609375, 28.677835464478, 4324.1840820313) CFrameMon = CFrame.new(-4931.1552734375, 65.793113708496, 4121.8393554688) elseif Lv == 150 or Lv <= 174 or SelectMonster == "Sky Bandit [Lv. 150]" then -- Sky Bandit Ms = "Sky Bandit [Lv. 150]" NameQuest = "SkyQuest" QuestLv = 1 NameMon = "Sky Bandit" CFrameQ = CFrame.new(-4842.1372070313, 717.69543457031, -2623.0483398438) CFrameMon = CFrame.new(-4955.6411132813, 365.46365356445, -2908.1865234375) elseif Lv == 175 or Lv <= 179 or SelectMonster == "Dark Master [Lv. 175]" then -- Dark Master Ms = "Dark Master [Lv. 175]" NameQuest = "SkyQuest" QuestLv = 2 NameMon = "Dark Master" CFrameQ = CFrame.new(-4842.1372070313, 717.69543457031, -2623.0483398438) CFrameMon = CFrame.new(-5148.1650390625, 439.04571533203, -2332.9611816406) elseif Lv == 180 or Lv <= 209 or SelectMonster == "Prisoner [Lv. 190]" then -- Prisoner Ms = "Prisoner [Lv. 190]" NameQuest = "PrisonerQuest" QuestLv = 1 NameMon = "Prisoner" CFrameQ = CFrame.new(5309.3584, 2.1345036, 474.173645, -0.273264647, -9.34814608e-08, -0.961938918, 3.1041214e-09, 1, -9.80620527e-08, 0.961938918, -2.97828677e-08, -0.273264647) CFrameMon = CFrame.new(5393.40723, 15.6333637, 486.675385, -0.748236716, 2.00700012e-09, -0.663431823, -8.54028226e-09, 1, 1.26571456e-08, 0.663431823, 1.51364361e-08, -0.748236716) elseif Lv == 210 or Lv <= 249 or SelectMonster == "Dangerous Prisoner [Lv. 210]" then -- Dangerous Ms = "Dangerous Prisoner [Lv. 210]" NameQuest = "PrisonerQuest" QuestLv = 2 NameMon = "Dangerous Prisoner" CFrameQ = CFrame.new(5309.3584, 2.1345036, 474.173645, -0.273264647, -9.34814608e-08, -0.961938918, 3.1041214e-09, 1, -9.80620527e-08, 0.961938918, -2.97828677e-08, -0.273264647) CFrameMon = CFrame.new(5393.40723, 15.6333637, 486.675385, -0.748236716, 2.00700012e-09, -0.663431823, -8.54028226e-09, 1, 1.26571456e-08, 0.663431823, 1.51364361e-08, -0.748236716) elseif Lv == 250 or Lv <= 274 or SelectMonster == "Toga Warrior [Lv. 250]" then -- Toga Warrior Ms = "Toga Warrior [Lv. 250]" NameQuest = "ColosseumQuest" QuestLv = 1 NameMon = "Toga Warrior" CFrameQ = CFrame.new(-1577.7890625, 7.4151420593262, -2984.4838867188) CFrameMon = CFrame.new(-1872.5166015625, 49.080215454102, -2913.810546875) elseif Lv == 275 or Lv <= 299 or SelectMonster == "Gladiator [Lv. 275]" then -- Gladiator Ms = "Gladiator [Lv. 275]" NameQuest = "ColosseumQuest" QuestLv = 2 NameMon = "Gladiator" CFrameQ = CFrame.new(-1577.7890625, 7.4151420593262, -2984.4838867188) CFrameMon = CFrame.new(-1521.3740234375, 81.203170776367, -3066.3139648438) elseif Lv == 300 or Lv <= 324 or SelectMonster == "Military Soldier [Lv. 300]" then -- Military Soldier Ms = "Military Soldier [Lv. 300]" NameQuest = "MagmaQuest" QuestLv = 1 NameMon = "Military Soldier" CFrameQ = CFrame.new(-5316.1157226563, 12.262831687927, 8517.00390625) CFrameMon = CFrame.new(-5369.0004882813, 61.24352645874, 8556.4921875) elseif Lv == 325 or Lv <= 374 or SelectMonster == "Military Spy [Lv. 325]" then -- Military Spy Ms = "Military Spy [Lv. 325]" NameQuest = "MagmaQuest" QuestLv = 2 NameMon = "Military Spy" CFrameQ = CFrame.new(-5316.1157226563, 12.262831687927, 8517.00390625) CFrameMon = CFrame.new(-5984.0532226563, 82.14656829834, 8753.326171875) elseif Lv == 375 or Lv <= 399 or SelectMonster == "Fishman Warrior [Lv. 375]" then -- Fishman Warrior Ms = "Fishman Warrior [Lv. 375]" NameQuest = "FishmanQuest" QuestLv = 1 NameMon = "Fishman Warrior" CFrameQ = CFrame.new(61122.65234375, 18.497442245483, 1569.3997802734) CFrameMon = CFrame.new(60844.10546875, 98.462875366211, 1298.3985595703) if Auto_Farm and (CFrameMon.Position - game.Players.LocalPlayer.Character.HumanoidRootPart.Position).Magnitude > 3000 then game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer("requestEntrance",Vector3.new(61163.8515625, 11.6796875, 1819.7841796875)) end elseif Lv == 400 or Lv <= 449 or SelectMonster == "Fishman Commando [Lv. 400]" then -- Fishman Commando Ms = "Fishman Commando [Lv. 400]" NameQuest = "FishmanQuest" QuestLv = 2 NameMon = "Fishman Commando" CFrameQ = CFrame.new(61122.65234375, 18.497442245483, 1569.3997802734) CFrameMon = CFrame.new(61738.3984375, 64.207321166992, 1433.8375244141) if Auto_Farm and (CFrameMon.Position - game.Players.LocalPlayer.Character.HumanoidRootPart.Position).Magnitude > 3000 then game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer("requestEntrance",Vector3.new(61163.8515625, 11.6796875, 1819.7841796875)) end elseif Lv == 450 or Lv <= 474 or SelectMonster == "God's Guard [Lv. 450]" then -- God's Guard Ms = "God's Guard [Lv. 450]" NameQuest = "SkyExp1Quest" QuestLv = 1 NameMon = "God's Guard" CFrameQ = CFrame.new(-4721.8603515625, 845.30297851563, -1953.8489990234) CFrameMon = CFrame.new(-4628.0498046875, 866.92877197266, -1931.2352294922) if Auto_Farm and (CFrameMon.Position - game.Players.LocalPlayer.Character.HumanoidRootPart.Position).Magnitude > 3000 then game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer("requestEntrance",Vector3.new(-4607.82275, 872.54248, -1667.55688)) end elseif Lv == 475 or Lv <= 524 or SelectMonster == "Shanda [Lv. 475]" then -- Shanda Ms = "Shanda [Lv. 475]" NameQuest = "SkyExp1Quest" QuestLv = 2 NameMon = "Shanda" CFrameQ = CFrame.new(-7863.1596679688, 5545.5190429688, -378.42266845703) CFrameMon = CFrame.new(-7685.1474609375, 5601.0751953125, -441.38876342773) if Auto_Farm and (CFrameMon.Position - game.Players.LocalPlayer.Character.HumanoidRootPart.Position).Magnitude > 3000 then game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer("requestEntrance",Vector3.new(-7894.6176757813, 5547.1416015625, -380.29119873047)) end elseif Lv == 525 or Lv <= 549 or SelectMonster == "Royal Squad [Lv. 525]" then -- Royal Squad Ms = "Royal Squad [Lv. 525]" NameQuest = "SkyExp2Quest" QuestLv = 1 NameMon = "Royal Squad" CFrameQ = CFrame.new(-7903.3828125, 5635.9897460938, -1410.923828125) CFrameMon = CFrame.new(-7654.2514648438, 5637.1079101563, -1407.7550048828) elseif Lv == 550 or Lv <= 624 or SelectMonster == "Royal Soldier [Lv. 550]" then -- Royal Soldier Ms = "Royal Soldier [Lv. 550]" NameQuest = "SkyExp2Quest" QuestLv = 2 NameMon = "Royal Soldier" CFrameQ = CFrame.new(-7903.3828125, 5635.9897460938, -1410.923828125) CFrameMon = CFrame.new(-7760.4106445313, 5679.9077148438, -1884.8112792969) elseif Lv == 625 or Lv <= 649 or SelectMonster == "Galley Pirate [Lv. 625]" then -- Galley Pirate Ms = "Galley Pirate [Lv. 625]" NameQuest = "FountainQuest" QuestLv = 1 NameMon = "Galley Pirate" CFrameQ = CFrame.new(5258.2788085938, 38.526931762695, 4050.044921875) CFrameMon = CFrame.new(5557.1684570313, 152.32717895508, 3998.7758789063) elseif Lv >= 650 or SelectMonster == "Galley Captain [Lv. 650]" then -- Galley Captain Ms = "Galley Captain [Lv. 650]" NameQuest = "FountainQuest" QuestLv = 2 NameMon = "Galley Captain" CFrameQ = CFrame.new(5258.2788085938, 38.526931762695, 4050.044921875) CFrameMon = CFrame.new(5677.6772460938, 92.786109924316, 4966.6323242188) end end if New_World then if Lv == 700 or Lv <= 724 or SelectMonster == "Raider [Lv. 700]" then -- Raider Ms = "Raider [Lv. 700]" NameQuest = "Area1Quest" QuestLv = 1 NameMon = "Raider" CFrameQ = CFrame.new(-427.72567749023, 72.99634552002, 1835.9426269531) CFrameMon = CFrame.new(68.874565124512, 93.635643005371, 2429.6752929688) elseif Lv == 725 or Lv <= 774 or SelectMonster == "Mercenary [Lv. 725]" then -- Mercenary Ms = "Mercenary [Lv. 725]" NameQuest = "Area1Quest" QuestLv = 2 NameMon = "Mercenary" CFrameQ = CFrame.new(-427.72567749023, 72.99634552002, 1835.9426269531) CFrameMon = CFrame.new(-864.85009765625, 122.47104644775, 1453.1505126953) elseif Lv == 775 or Lv <= 799 or SelectMonster == "Swan Pirate [Lv. 775]" then -- Swan Pirate Ms = "Swan Pirate [Lv. 775]" NameQuest = "Area2Quest" QuestLv = 1 NameMon = "Swan Pirate" CFrameQ = CFrame.new(635.61151123047, 73.096351623535, 917.81298828125) CFrameMon = CFrame.new(1065.3669433594, 137.64012145996, 1324.3798828125) elseif Lv == 800 or Lv <= 874 or SelectMonster == "Factory Staff [Lv. 800]" then -- Factory Staff Ms = "Factory Staff [Lv. 800]" NameQuest = "Area2Quest" QuestLv = 2 NameMon = "Factory Staff" CFrameQ = CFrame.new(635.61151123047, 73.096351623535, 917.81298828125) CFrameMon = CFrame.new(533.22045898438, 128.46876525879, 355.62615966797) elseif Lv == 875 or Lv <= 899 or SelectMonster == "Marine Lieutenant [Lv. 875]" then -- Marine Lieutenant Ms = "Marine Lieutenant [Lv. 875]" NameQuest = "MarineQuest3" QuestLv = 1 NameMon = "Marine Lieutenant" CFrameQ = CFrame.new(-2440.9934082031, 73.04190826416, -3217.7082519531) CFrameMon = CFrame.new(-2489.2622070313, 84.613594055176, -3151.8830566406) elseif Lv == 900 or Lv <= 949 or SelectMonster == "Marine Captain [Lv. 900]" then -- Marine Captain Ms = "Marine Captain [Lv. 900]" NameQuest = "MarineQuest3" QuestLv = 2 NameMon = "Marine Captain" CFrameQ = CFrame.new(-2440.9934082031, 73.04190826416, -3217.7082519531) CFrameMon = CFrame.new(-2335.2026367188, 79.786659240723, -3245.8674316406) elseif Lv == 950 or Lv <= 974 or SelectMonster == "Zombie [Lv. 950]" then -- Zombie Ms = "Zombie [Lv. 950]" NameQuest = "ZombieQuest" QuestLv = 1 NameMon = "Zombie" CFrameQ = CFrame.new(-5494.3413085938, 48.505931854248, -794.59094238281) CFrameMon = CFrame.new(-5536.4970703125, 101.08577728271, -835.59075927734) elseif Lv == 975 or Lv <= 999 or SelectMonster == "Vampire [Lv. 975]" then -- Vampire Ms = "Vampire [Lv. 975]" NameQuest = "ZombieQuest" QuestLv = 2 NameMon = "Vampire" CFrameQ = CFrame.new(-5494.3413085938, 48.505931854248, -794.59094238281) CFrameMon = CFrame.new(-5806.1098632813, 16.722528457642, -1164.4384765625) elseif Lv == 1000 or Lv <= 1049 or SelectMonster == "Snow Trooper [Lv. 1000]" then -- Snow Trooper Ms = "Snow Trooper [Lv. 1000]" NameQuest = "SnowMountainQuest" QuestLv = 1 NameMon = "Snow Trooper" CFrameQ = CFrame.new(607.05963134766, 401.44781494141, -5370.5546875) CFrameMon = CFrame.new(535.21051025391, 432.74209594727, -5484.9165039063) elseif Lv == 1050 or Lv <= 1099 or SelectMonster == "Winter Warrior [Lv. 1050]" then -- Winter Warrior Ms = "Winter Warrior [Lv. 1050]" NameQuest = "SnowMountainQuest" QuestLv = 2 NameMon = "Winter Warrior" CFrameQ = CFrame.new(607.05963134766, 401.44781494141, -5370.5546875) CFrameMon = CFrame.new(1234.4449462891, 456.95419311523, -5174.130859375) elseif Lv == 1100 or Lv <= 1124 or SelectMonster == "Lab Subordinate [Lv. 1100]" then -- Lab Subordinate Ms = "Lab Subordinate [Lv. 1100]" NameQuest = "IceSideQuest" QuestLv = 1 NameMon = "Lab Subordinate" CFrameQ = CFrame.new(-6061.841796875, 15.926671981812, -4902.0385742188) CFrameMon = CFrame.new(-5720.5576171875, 63.309471130371, -4784.6103515625) elseif Lv == 1125 or Lv <= 1174 or SelectMonster == "Horned Warrior [Lv. 1125]" then -- Horned Warrior Ms = "Horned Warrior [Lv. 1125]" NameQuest = "IceSideQuest" QuestLv = 2 NameMon = "Horned Warrior" CFrameQ = CFrame.new(-6061.841796875, 15.926671981812, -4902.0385742188) CFrameMon = CFrame.new(-6292.751953125, 91.181983947754, -5502.6499023438) elseif Lv == 1175 or Lv <= 1199 or SelectMonster == "Magma Ninja [Lv. 1175]" then -- Magma Ninja Ms = "Magma Ninja [Lv. 1175]" NameQuest = "FireSideQuest" QuestLv = 1 NameMon = "Magma Ninja" CFrameQ = CFrame.new(-5429.0473632813, 15.977565765381, -5297.9614257813) CFrameMon = CFrame.new(-5461.8388671875, 130.36347961426, -5836.4702148438) elseif Lv == 1200 or Lv <= 1249 or SelectMonster == "Lava Pirate [Lv. 1200]" then -- Lava Pirate Ms = "Lava Pirate [Lv. 1200]" NameQuest = "FireSideQuest" QuestLv = 2 NameMon = "Lava Pirate" CFrameQ = CFrame.new(-5429.0473632813, 15.977565765381, -5297.9614257813) CFrameMon = CFrame.new(-5251.1889648438, 55.164535522461, -4774.4096679688) elseif Lv == 1250 or Lv <= 1274 or SelectMonster == "Ship Deckhand [Lv. 1250]" then -- Ship Deckhand Ms = "Ship Deckhand [Lv. 1250]" NameQuest = "ShipQuest1" QuestLv = 1 NameMon = "Ship Deckhand" CFrameQ = CFrame.new(1040.2927246094, 125.08293151855, 32911.0390625) CFrameMon = CFrame.new(921.12365722656, 125.9839553833, 33088.328125) if Auto_Farm and (CFrameMon.Position - game.Players.LocalPlayer.Character.HumanoidRootPart.Position).Magnitude > 20000 then game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer("requestEntrance",Vector3.new(923.21252441406, 126.9760055542, 32852.83203125)) end elseif Lv == 1275 or Lv <= 1299 or SelectMonster == "Ship Engineer [Lv. 1275]" then -- Ship Engineer Ms = "Ship Engineer [Lv. 1275]" NameQuest = "ShipQuest1" QuestLv = 2 NameMon = "Ship Engineer" CFrameQ = CFrame.new(1040.2927246094, 125.08293151855, 32911.0390625) CFrameMon = CFrame.new(886.28179931641, 40.47790145874, 32800.83203125) if Auto_Farm and (CFrameMon.Position - game.Players.LocalPlayer.Character.HumanoidRootPart.Position).Magnitude > 20000 then game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer("requestEntrance",Vector3.new(923.21252441406, 126.9760055542, 32852.83203125)) end elseif Lv == 1300 or Lv <= 1324 or SelectMonster == "Ship Steward [Lv. 1300]" then -- Ship Steward Ms = "Ship Steward [Lv. 1300]" NameQuest = "ShipQuest2" QuestLv = 1 NameMon = "Ship Steward" CFrameQ = CFrame.new(971.42065429688, 125.08293151855, 33245.54296875) CFrameMon = CFrame.new(943.85504150391, 129.58183288574, 33444.3671875) if Auto_Farm and (CFrameMon.Position - game.Players.LocalPlayer.Character.HumanoidRootPart.Position).Magnitude > 20000 then game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer("requestEntrance",Vector3.new(923.21252441406, 126.9760055542, 32852.83203125)) end elseif Lv == 1325 or Lv <= 1349 or SelectMonster == "Ship Officer [Lv. 1325]" then -- Ship Officer Ms = "Ship Officer [Lv. 1325]" NameQuest = "ShipQuest2" QuestLv = 2 NameMon = "Ship Officer" CFrameQ = CFrame.new(971.42065429688, 125.08293151855, 33245.54296875) CFrameMon = CFrame.new(955.38458251953, 181.08335876465, 33331.890625) if Auto_Farm and (CFrameMon.Position - game.Players.LocalPlayer.Character.HumanoidRootPart.Position).Magnitude > 20000 then game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer("requestEntrance",Vector3.new(923.21252441406, 126.9760055542, 32852.83203125)) end elseif Lv == 1350 or Lv <= 1374 or SelectMonster == "Arctic Warrior [Lv. 1350]" then -- Arctic Warrior Ms = "Arctic Warrior [Lv. 1350]" NameQuest = "FrostQuest" QuestLv = 1 NameMon = "Arctic Warrior" CFrameQ = CFrame.new(5668.1372070313, 28.202531814575, -6484.6005859375) CFrameMon = CFrame.new(5935.4541015625, 77.26016998291, -6472.7568359375) if Auto_Farm and (CFrameMon.Position - game.Players.LocalPlayer.Character.HumanoidRootPart.Position).Magnitude > 20000 then game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer("requestEntrance",Vector3.new(-6508.5581054688, 89.034996032715, -132.83953857422)) end elseif Lv == 1375 or Lv <= 1424 or SelectMonster == "Snow Lurker [Lv. 1375]" then -- Snow Lurker Ms = "Snow Lurker [Lv. 1375]" NameQuest = "FrostQuest" QuestLv = 2 NameMon = "Snow Lurker" CFrameQ = CFrame.new(5668.1372070313, 28.202531814575, -6484.6005859375) CFrameMon = CFrame.new(5628.482421875, 57.574996948242, -6618.3481445313) elseif Lv == 1425 or Lv <= 1449 or SelectMonster == "Sea Soldier [Lv. 1425]" then -- Sea Soldier Ms = "Sea Soldier [Lv. 1425]" NameQuest = "ForgottenQuest" QuestLv = 1 NameMon = "Sea Soldier" CFrameQ = CFrame.new(-3054.5827636719, 236.87213134766, -10147.790039063) CFrameMon = CFrame.new(-3185.0153808594, 58.789089202881, -9663.6064453125) elseif Lv >= 1450 or SelectMonster == "Water Fighter [Lv. 1450]" then -- Water Fighter Ms = "Water Fighter [Lv. 1450]" NameQuest = "ForgottenQuest" QuestLv = 2 NameMon = "Water Fighter" CFrameQ = CFrame.new(-3054.5827636719, 236.87213134766, -10147.790039063) CFrameMon = CFrame.new(-3262.9301757813, 298.69036865234, -10552.529296875) end end if Three_World then if Lv == 1500 or Lv <= 1524 or SelectMonster == "Pirate Millionaire [Lv. 1500]" then -- Pirate Millionaire Ms = "Pirate Millionaire [Lv. 1500]" NameQuest = "PiratePortQuest" QuestLv = 1 NameMon = "Pirate Millionaire" CFrameQ = CFrame.new(-289.61752319336, 43.819011688232, 5580.0903320313) CFrameMon = CFrame.new(-435.68109130859, 189.69866943359, 5551.0756835938) elseif Lv == 1525 or Lv <= 1574 or SelectMonster == "Pistol Billionaire [Lv. 1525]" then -- Pistol Billoonaire Ms = "Pistol Billionaire [Lv. 1525]" NameQuest = "PiratePortQuest" QuestLv = 2 NameMon = "Pistol Billionaire" CFrameQ = CFrame.new(-289.61752319336, 43.819011688232, 5580.0903320313) CFrameMon = CFrame.new(-236.53652954102, 217.46676635742, 6006.0883789063) elseif Lv == 1575 or Lv <= 1599 or SelectMonster == "Dragon Crew Warrior [Lv. 1575]" then -- Dragon Crew Warrior Ms = "Dragon Crew Warrior [Lv. 1575]" NameQuest = "AmazonQuest" QuestLv = 1 NameMon = "Dragon Crew Warrior" CFrameQ = CFrame.new(5833.1147460938, 51.60498046875, -1103.0693359375) CFrameMon = CFrame.new(6301.9975585938, 104.77153015137, -1082.6075439453) elseif Lv == 1600 or Lv <= 1624 or SelectMonster == "Dragon Crew Archer [Lv. 1600]" then -- Dragon Crew Archer Ms = "Dragon Crew Archer [Lv. 1600]" NameQuest = "AmazonQuest" QuestLv = 2 NameMon = "Dragon Crew Archer" CFrameQ = CFrame.new(5833.1147460938, 51.60498046875, -1103.0693359375) CFrameMon = CFrame.new(6831.1171875, 441.76708984375, 446.58615112305) elseif Lv == 1625 or Lv <= 1649 or SelectMonster == "Female Islander [Lv. 1625]" then -- Female Islander Ms = "Female Islander [Lv. 1625]" NameQuest = "AmazonQuest2" QuestLv = 1 NameMon = "Female Islander" CFrameQ = CFrame.new(5446.8793945313, 601.62945556641, 749.45672607422) CFrameMon = CFrame.new(5792.5166015625, 848.14392089844, 1084.1818847656) elseif Lv == 1650 or Lv <= 1699 or SelectMonster == "Giant Islander [Lv. 1650]" then -- Giant Islander Ms = "Giant Islander [Lv. 1650]" NameQuest = "AmazonQuest2" QuestLv = 2 NameMon = "Giant Islander" CFrameQ = CFrame.new(5446.8793945313, 601.62945556641, 749.45672607422) CFrameMon = CFrame.new(5009.5068359375, 664.11071777344, -40.960144042969) elseif Lv == 1700 or Lv <= 1724 or SelectMonster == "Marine Commodore [Lv. 1700]" then -- Marine Commodore Ms = "Marine Commodore [Lv. 1700]" NameQuest = "MarineTreeIsland" QuestLv = 1 NameMon = "Marine Commodore" CFrameQ = CFrame.new(2179.98828125, 28.731239318848, -6740.0551757813) CFrameMon = CFrame.new(2198.0063476563, 128.71075439453, -7109.5043945313) elseif Lv == 1725 or Lv <= 1774 or SelectMonster == "Marine Rear Admiral [Lv. 1725]" then -- Marine Rear Admiral Ms = "Marine Rear Admiral [Lv. 1725]" NameQuest = "MarineTreeIsland" QuestLv = 2 NameMon = "Marine Rear Admiral" CFrameQ = CFrame.new(2179.98828125, 28.731239318848, -6740.0551757813) CFrameMon = CFrame.new(3294.3142089844, 385.41125488281, -7048.6342773438) elseif Lv == 1775 or Lv <= 1799 or SelectMonster == "Fishman Raider [Lv. 1775]" then -- Fishman Raide Ms = "Fishman Raider [Lv. 1775]" NameQuest = "DeepForestIsland3" QuestLv = 1 NameMon = "Fishman Raider" CFrameQ = CFrame.new(-10582.759765625, 331.78845214844, -8757.666015625) CFrameMon = CFrame.new(-10553.268554688, 521.38439941406, -8176.9458007813) elseif Lv == 1800 or Lv <= 1824 or SelectMonster == "Fishman Captain [Lv. 1800]" then -- Fishman Captain Ms = "Fishman Captain [Lv. 1800]" NameQuest = "DeepForestIsland3" QuestLv = 2 NameMon = "Fishman Captain" CFrameQ = CFrame.new(-10583.099609375, 331.78845214844, -8759.4638671875) CFrameMon = CFrame.new(-10789.401367188, 427.18637084961, -9131.4423828125) elseif Lv == 1825 or Lv <= 1849 or SelectMonster == "Forest Pirate [Lv. 1825]" then -- Forest Pirate Ms = "Forest Pirate [Lv. 1825]" NameQuest = "DeepForestIsland" QuestLv = 1 NameMon = "Forest Pirate" CFrameQ = CFrame.new(-13232.662109375, 332.40396118164, -7626.4819335938) CFrameMon = CFrame.new(-13489.397460938, 400.30349731445, -7770.251953125) elseif Lv == 1850 or Lv <= 1899 or SelectMonster == "Mythological Pirate [Lv. 1850]" then -- Mythological Pirate Ms = "Mythological Pirate [Lv. 1850]" NameQuest = "DeepForestIsland" QuestLv = 2 NameMon = "Mythological Pirate" CFrameQ = CFrame.new(-13232.662109375, 332.40396118164, -7626.4819335938) CFrameMon = CFrame.new(-13508.616210938, 582.46228027344, -6985.3037109375) elseif Lv == 1900 or Lv <= 1924 or SelectMonster == "Jungle Pirate [Lv. 1900]" then -- Jungle Pirate Ms = "Jung…

---
## [jaaat4u/NikoKernel](https://github.com/jaaat4u/NikoKernel)@[d6a96b3638...](https://github.com/jaaat4u/NikoKernel/commit/d6a96b3638419a6fd942a479ee3ca96e72dfa6ad)
#### Saturday 2022-06-11 16:52:06 by Linus Torvalds

gpiolib: acpi: use correct format characters

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
Signed-off-by: Devang Chaudhary <devangsingh369@gmail.com>

---
## [ItsSelis/VOREStation](https://github.com/ItsSelis/VOREStation)@[38724d4d4c...](https://github.com/ItsSelis/VOREStation/commit/38724d4d4c140fb4bfc92444ba3e5dd182ca7df9)
#### Saturday 2022-06-11 16:56:04 by VerySoft

[WIP] pAI tweaks and upgrades

Changes some things around! 

Removes the 'wipe' button from pAI's interface, since I think there being an instant 'kill player' button is pretty lame, especially since most pAIs activate on their own without a master. They're easy enough to kill or contain without this, so I don't see it as necessary. If you want to kill your pAI friend just eat them. :U

Removes the 'pAI Suicide' verb, and renames the 'Wipe Personality' to 'Enter Storage' and moved it from the OOC tab to the pAI Commands tab. Killing a pAI deletes the card and all that, where the 'Enter Storage' verb deletes the card and spawns a new one that can be used, which! I think it more appropriate.

Makes it so that, when damaged, pAIs will slowly regenerate while folded up, at a rate of 0.5 brute and burn per life tick, where previously it had been impossible to recover health outside of admin intervention.

Updated the Universal Translator with many of the newer languages that aren't obviously for events or hivemind type things.

Added the same emotes that humans can use to pAIs

Added an alternative pAI card style, and rearranged the expressions for the cards a little bit, and added one more.

Plan to add more pAI chassis to play with

---
## [saint-lascivious/munin-pihole-plugins](https://github.com/saint-lascivious/munin-pihole-plugins)@[efe605117e...](https://github.com/saint-lascivious/munin-pihole-plugins/commit/efe605117e470d09875b0657ea257e18088ce2d8)
#### Saturday 2022-06-11 18:24:32 by Hayden Pearce

munin-pihole-plugins: olympic level yoga hand-holding, 06.08.00

yet more general usability and configuration QOL additions

read below if not otherwise consumed by apathy
believe me, i know how challenging it is not to be

the tl;dr keynotes here are essentially:
 - infinitely more flexible and configurable
 - marginally safer user configuration

Changes to be committed:
 - modified:   README.md
   list and describe EXTERNAL_CONFIG_DIR and EXTERNAL_CONFIG_FILE
   adjust some verbiage regarding var values that are arrays
   (double quote quotation is required)
 - modified:   etc/bash_completion.d/munin-pihole-plugins
   bump version to 06.08.00
   add EXTERNAL_CONFIG_DIR and EXTERNAL_CONFIG_FILE
 - modified:   script/munin-pihole-plugins
   bump version to 06.08.00
   increase external configuration flexibility
   (add EXTERNAL_CONFIG_DIR and EXTERNAL_CONFIG_FILE)
   (creating either/both if required)
   dance a silly /dev/null dance with shellcheck's source parser
   (shellcheck's 'source' parsing is reasonably limited)
   (it does not cope well with sourcing a compound variable)
   (better this than ~500 identical user reported issues)
   (though very old versions of shellcheck may still complain)
   modify_external_var is now transmogrify
   (you've gotta have cool/witty function names, right?)
   add an rfc3339 compliant datetime alias
   (YYYY-MM-DD HH:MM:SS±00:00)
   (used where standard human readable datetimes are desired)
   ('date' without modifiers may produce a locale specific datetime)
   (i don't care who thinks which format is better or worse)
   (i just want a standard human readable format)
   adjust transmogrify to make use of EXTERNAL_* variables
   (nothing else uses the function at this time)
   (but it needed to be split out regardless)
   allow transmogrify to be passed a path or file
   (only variable_fun uses it right now)
   (it's better off generic even if it doesn't /need/ to be)
   ensure transmogrify encapsulates values in double quotes
   (required for arrays, i should have caught this earlier)
   (i never personally modify, nor tested, PLUGIN_LIST)
   (...i suspect very few people ever do)
   (someone however did, special thanks to user CJuarez79)
   perform more hand-holding relative to expected values
   (ensure DNS_PORT is a positive integer of valid range)
   (complain if non-integer)
   (complain if integer but integer is oob)
   (abort safe in either case)
   (special thanks to user Keiran N for pointing this out)
   fix a rare gremlin when transmogrifying a config file
   (config file existence was improperly asserted until now)
 - modified:   usr/share/munin/plugins/pihole_
   bump version to 06.08.00
   (no functional changes)

saint's musings:
 - this s/bag of shit/very fine bash script/g is now ~1100 SLOC
 - i'm not sure what's scarier, that this project is approximately
   eleven hundred source lines of code, or that it contains about
   two hundred lines of comments when nothing is commented in-line
   and everything is "simply" preceeded with a "brief" description
   of its function and/or usage

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[b290055923...](https://github.com/mrakgr/The-Spiral-Language/commit/b2900559235fbdb592e6f17429af737c13a6217a)
#### Saturday 2022-06-11 19:14:19 by Marko Grdinić

"1:30pm. Done with breakfast and chores. Let me finish Birdie Wing and then I will resume the tutorial. I've looked into what object IDs do and it turns out there is a node in the compositor that can use them as masks. Cryptomattes would be easier to use so I'll just go with them instead.

1:50pm. That was fun. Let me resume.

https://youtu.be/a1weKAFJx3k
Demystifying Blender Cycles' Render Passes: Normal Pass

Let me watch this. Then I'll get back to the tutorial by Andrew.

https://youtu.be/a1weKAFJx3k?t=21
>It is one of the most important passes that one could have and be blessed with as a compositor, and you'll see why.

This caught my interest. I have absolutely no idea what it could be good for.

> Add rim light, in compositing.

Huh really?

https://www.youtube.com/c/TheInfinites/search?query=uv%20pass

I am tempted to watch the UV pass video, but let me skip it for now. The normal pass video was interesting.

https://youtu.be/9Q8PwcDzb8Y?t=2432

Focus me on this. Right now I do not know how he did the spread out effect from the sun. I got some of that thanks to the roughness, but it is different from him. For him it works even on the land.

https://youtu.be/9Q8PwcDzb8Y?t=2490

Let me get to this point. I should incorporate the sun. This one I am going to have to follow step by step.

https://youtu.be/9Q8PwcDzb8Y?t=2490

For him the light is much softer as it goes around the rim of Earth. It makes sense that it would be like this for me, but maybe some of that extra lighting is due to atmospheric deflection. I have no choice, let me back track.

https://youtu.be/9Q8PwcDzb8Y?t=229

This soft look of the light came for him fairly naturally. Hmmm, could this have something to do with him starting with a regular sphere and then subdiving it. Let me open a new project.

2:20pm. https://youtu.be/9Q8PwcDzb8Y?t=229

I do not know. It is just naturally soft for him. To get this kind of effect I have to ramp up the sun angle in the settings to 20 degrees.

Ok, let me go with that then. I do not think he touched the light apart from this.

2:40pm. Hmmm, let me load up the image. I can just put in the camera UVs. No, I'll composit it. Discipline me.

2:50pm. Right now I am stuggling to figure out how to crop the huge image directly in the compositor.

https://youtu.be/wInEHit1yk0
Blender Compositor Crop Node: Baltimore

If possible, I'd like to avoid having to go into CSP just for this.

https://youtu.be/wInEHit1yk0?t=257

Yeah, when I put in the crop node everything disappeared for me as well. So what is the deal with that?

https://youtu.be/wInEHit1yk0?t=281

Hmmm, I see.

3:10pm. Damn it, this is so annoying. How do I crop that big image so it maintains the aspect ratio. AT first I thought I would just to a part of it, but I changed my mind. I really like the detail in the full image, but I do not want to stretch it.

https://youtu.be/tG-I0kgJHhQ
Blender Beginners Tutorial: How To Crop Rotate Shape And Scale A Video Clip Recorded At An An Angle

Let me watch this.

https://youtu.be/tG-I0kgJHhQ?t=258

What the hell am I looking at here? The video editor.

https://docs.blender.org/manual/en/latest/compositing/types/distort/scale.html

I am really getting bogged down.

> Stretch distorts the image so that it fits into the render size. Fit scales the image until the bigger axis “fits” into the render size. Crop cuts the image so that it is the same aspect ratio as the render size.

What is the difference between fit and stretch?

Ah, fit will fit one of the axes, but it won't stretch the image. If it is not big enough one the sides, it will leave it empty.

3:30pm. Ok, I have a handle on it. First I use the `crop` node with `crop image size` and `relative` settings turned on. Then I pass that into scale that has the crop setting. That works rather well. This allows me to crop parts of the image. The original image is 4k, it is just too big, so I only take 0.7 to 1 from left to right.

...Let me do it in quarters instead of 30%s.

That should give me 2000x4000 cuttouts which the scale node will then crop. It will allow me to reuse the image from different angles and add some variety to it. It feels a bit low ress, but that will all go away once I do style transfer.

3:40pm. Right now I am just stuck admiring the viewer node. It really looks quite nice.

Let me get a move on. I am satisfied with this as my background.

4pm. I did a render, and put a sun where it should be. I won't let it render for full. I'll do that only once I am done. Still even after a minute the image quality is good.

https://youtu.be/9Q8PwcDzb8Y?t=2504

This kind of workflow has been completely superseeded by cryptomattes. Back when he did that video, that functionality was not available in Blender.

4:10pm. https://youtu.be/9Q8PwcDzb8Y?t=2587

I find this confusing, what is he trying to do here?

4:25pm. The way the blur works is really confusing. The regular gaussian constrains it to a box, but the fast one for some reason gets mirrored when I do not want it to. Also because I composited the background I can no longer mix it easily into the original image.

I have no idea what the environment is suppose to be doing.

I though I understood it - all the objects are black while rest is not, but the alpha already gives me that. I can just get the alpha to use it as a mask for the background. So then why is he adding the blurred sun to the environment?

https://docs.blender.org/manual/en/latest/render/layers/passes.html

> Environment
> Emission from the directly visible background. When the film is set to transparent, this can be used to get the environment color and composite it back in.

Wait, that gray might not be alpha, but instead it is probably the 0.02 strength white background that I put to just give the back of the world just a little lighting.

Let me test that. Let me try making it green.

Yeah, that is it. Ok. It shows up as green even though I have it transparent in the compositor.

He himself made it transparent in the compositor.

I think I understand it. He wants to mix the light from the sun into the background directly. I see.

Ok, I can play it like that.

4:35pm. Ok, then, first of all, I want to make my own sun pure white, and merge it back into the image. Then I want to light up the background. Then I can composite the lighted background with the image.

Let me take just a short break.

5pm. Seriously, why is blur leaking from the other side. I do not get this, but nevermind.

https://youtu.be/9Q8PwcDzb8Y?t=2633

The kind of blur he has is different from mine. It has rigid borders.

https://youtu.be/9Q8PwcDzb8Y?t=3071
> It is applying it still underneath the earth. What did he intend?

https://youtu.be/9Q8PwcDzb8Y?t=3293

I am not interested in this part since I will be putting it into the style transfer NN anyway. Let me just watch till the end and then I will do the glare properly.

https://youtu.be/9Q8PwcDzb8Y?t=3660

Isn't it great that I have cryptomates and can just grab the Atmo directly?

5:35pm. I finally finished watching the tutorial. I think I can make some things more efficiently than him. I am going to do the blurs and the glares, but skip the photoshop filters. Let me just do this.

6:05pm. I can't believe I am still trying to get the filter under control.

6:20pm. And I am still doing it. I can't believe it. The brightness of the sun can in fact influence the brightness of the rest of the image. I am only changing the sun intensity, but it is affecting the background by making it darker.

7:05pm. Done with lunch. The reason why the blur is so annoying to do is because Andrew made the sphere too small at the start. Trying to turn it into a large blur therefore leads into all sorts of issues.

I admit, I really have no idea why every filter except the Gaussian one ends up being boxy. They look like absolute shit. But that is just a part of the problem which the sun being too small for the effect I am going for.

8pm. I am going to skip the moon. It was not planned in my original composition, and I have enough material as is. I really wonder how I am going to fit the golden city into the composition.

Ah, I see. I just had an idea to do them on a separate render layer. Yes, indeed, that would make things easier for me. I never tried using two separate layers, but it would better if I did so this time otherwise I will have all sorts of rendering difficulties.

I can always move them to the same one after I am done.

8:20pm. Time for fun. I wanted to make more progress today, but I am going at my usual snail's pace. I guess I am not there yet. Today I did learn quite a bit about the compositor. This scene is only my third serious project, I'll get it down finely at some point. I knew I'd manage to get this far, but tomorrow, that is when things will get serious. I've been thinking about this for a while, but I am still not sure how I am going to architect the city properly. I'll have to look at references tomorrow and think about it seriously."

---
## [Winter/SemanticReleaseTestsConsole](https://github.com/Winter/SemanticReleaseTestsConsole)@[7ca9c4c48e...](https://github.com/Winter/SemanticReleaseTestsConsole/commit/7ca9c4c48ea704fd3d01806bb86e54101e3ec789)
#### Saturday 2022-06-11 19:34:45 by Edward

fix(dockerfile): just fucking work you dumb piece of shit why the flying fuck does this not work on god damn github actions

---
## [Winter/SemanticReleaseTestsConsole](https://github.com/Winter/SemanticReleaseTestsConsole)@[98c89178ef...](https://github.com/Winter/SemanticReleaseTestsConsole/commit/98c89178eff692f9790e7e4bbd67e08beae63422)
#### Saturday 2022-06-11 20:14:39 by Edward

fix(linux-musl-arm64): I'm literally losing all my brain cells not that I had any to begin with but for fuck sake will this stupid thing just work why the flying fuckity fuck is this cunt fuck of a fuck not fucking fucking the fuck its because its retarded thats why it fucking works when I run it locally it has the platform, it has the fucking retarded shit buildx looks like it's workinng so why is it being so mentally disabled

---
## [tf2cheater2013/Fedoraware](https://github.com/tf2cheater2013/Fedoraware)@[5a23d95aca...](https://github.com/tf2cheater2013/Fedoraware/commit/5a23d95aca96005b454a9a9b75ba2ac9ae603c83)
#### Saturday 2022-06-11 20:35:39 by Johnathon Walnut

Merge pull request #380 from femboy-boop/patch-2

fuck you baan

---
## [Aliscans/crawl](https://github.com/Aliscans/crawl)@[1352289c90...](https://github.com/Aliscans/crawl/commit/1352289c90d15a53f9c472dac9343ad61d9104a7)
#### Saturday 2022-06-11 22:02:09 by Nicholas Feinberg

New species: Meteoran

Time pressure often creates exciting gameplay and interesting
tradeoffs. Baseline Dungeon Crawl uses the Zot Clock to add a
very weak form of time pressure, but there's so much variety
between the playstyles of different species and backgrounds
that a tight clock for some would be almost impossible for
others.

So, let's try limiting that gameplay to just one species!
Meteorae have an exciting variety of bonuses - great attributes
and aptitudes across the board, passive mapping, and exploration
healing, regaining HP and MP when viewing new territory. In
exchange, they have one big downside: instead of getting 6,000
turns of Zot clock for each floor, they get 600!

The big concern here is whether this species can be made fun
without also being made wildly, boringly 'overpowered'. Lots of
levers and knobs to tweak, so let's give it a shot!

Extra notes:
- Meteorae are humanoid beings. (In the night sky, they look
  like dots because they're very far up.) Hat tip to Neil Gaiman's
  Stardust.
- This commit has a silly 'flavour' gimmick where Meteorae's LOS
  radius decreases by 2 when they have less than 50 turns left
  of Zot clock, and again when they have less than 10. Darkness
  is closing in...
- Meteorae glow in the dark. Permanent backlit status (not halo!):
  +enemy to hit, -stealth, disables invis. Suppressed in forms.
  Seems funny.

Credit to hellmonk for the initial version of this species and
pushing to make 'em happen. :)

---
## [D4C-420/https-github.com-D4C-420-tgstation](https://github.com/D4C-420/https-github.com-D4C-420-tgstation)@[cd294e9040...](https://github.com/D4C-420/https-github.com-D4C-420-tgstation/commit/cd294e9040505e73e46384d6166015afa43217f3)
#### Saturday 2022-06-11 22:15:16 by vincentiusvin

Scipaper rebalancing: Nitrium and halon shell removal. Nitrous added. Emphasis on BZ. (#66738)

Similar in spirit to #65707, with some more changes.

Restructured the gaseous experiments to:

    Nitrous (practice experiment)
    BZ (mainstay experiment)
    Hyper-Nob (lategame/once-in-a-while experiment)

Added a mining partner.

Moved adv weaponry lock to normal weaponry under reactionless. Toned down t3 reactionless.

BZ locks adv engi. Medbay unbridled by toxin gasses now.

Removed Xenobio's BZ Can.
Why It's Good For The Game

My original intent with papers was expanding the difficulty range of toxins. Both to things harder than tritium (nob, nitrium, etc) and also to things easier than tritium (bz, reactionless, etc).

In that process, I feel that i strayed a bit to the harder side, this PR is an attempt to tone down the overall difficulty of some of the gaseous experiments a notch.

Nitrous now takes place of the old BZ, BZ takes place of old nitrium/halon, and noblium stays because it's difficulty is in a pretty good spot for a relatively unimportant but nice to have tech.

While we're at it, I also added more emphasis to BZ production to toxins instead of tritium. This will hopefully incentivize people to try the department out. There is a risk of this being a bit of a chore, but I believe that the relevant atmos gameplay loop is strong enough to have it be fun. You need to check on the chamber, turn on pipes, adjust the input rate, and many more that makes it significantly more fun to do.

We do this by:

    Locking advanced engineering with BZ (organs and implants lock lifted). Depending on feedback i wont mind changing this around if you want to suggest another node as long as it's of similar or very slightly less importance.

    Getting rid of xeno's BZ can. Some xeno players need it for making slimes sleep, with their roundstart supply removed there should be a significant demand for the BZ production in toxins to go online asap.

If you have been paying attention to our PRs, i have been working to make BZ production as seamless and quick as possible in toxins. My five map prs #66454 #66198 #66064 #66010 #65857 have been building up to this. You can make BZ relatively quickly with the new freezer chamber in place. Probably even faster than ordering it in cargo, which is a fine ballpark to use if you want to make changes to it.

If you want to know how to operate it, here is a wiki guide in place https://tgstation13.org/wiki/User:Vincentius_vin/Sandbox#BZ_Synthesis. We will move it to the main toxins page once the rest of the page is finished, pictures are added, 

Made adv engi tech node require bz shells as an experiment, organs no longer need it.
Adv mining no longer requires adv engi.
Removed nitrium and halon shell, implant experiment lock lifted because of the former.
Relocked sec 1 tech node to need pressure bombs, sec 2 no longer needs tritium bomb.
Made advanced pressure bombs easier to do without funny fusion gases.
Added a new mining partner that accepts smaller (even non-atmos/non-ordnance related) bombs
Added more options to purchase nodes in the paper partners. Your point gain stays the same though.
Removed roundstart BZ can from xenobio.

---
## [D4C-420/https-github.com-D4C-420-tgstation](https://github.com/D4C-420/https-github.com-D4C-420-tgstation)@[245ec35dae...](https://github.com/D4C-420/https-github.com-D4C-420-tgstation/commit/245ec35dae59d0edc92663ccb8012b27d5e1a198)
#### Saturday 2022-06-11 22:15:16 by LemonInTheDark

Removes (in) smoke and foam reactions (#67270)

* Removes smoke and foam reactions

Turns out when you let reagents react in foam/smoke, people put bombs in
them.

This behavior was initially added to just smoke, accidentially in
(56f7ac0c0a29e8f898c4aab35947d027952b43f7) accidentialy (thalpy tried to
make both foam and smoke instant react, but instead made smoke's temporary
holder reagent instant instead. hhhhhhh)

Assuming this was intentional it was then extended to foam in
(1879e2d338c9bf5f191cef6c39944b26a41e6092)

Basically, we're idiots. Anyway lets just walk this all back to instant
reaction on smoke/foam formation. Hate you people

* Removes another source of gunpowder smoke

Temporal told me about this. Gunpowder uses an ex_act signal as a
starter, and that also counts for smoke objects.

Really don't want instant detonation smoke bombs, so let's just... not
shall we?

---
## [ray314/BreadmonBot](https://github.com/ray314/BreadmonBot)@[342bdd46c2...](https://github.com/ray314/BreadmonBot/commit/342bdd46c2f9d79d0c8a28ba2ffb00e1a4509aba)
#### Saturday 2022-06-11 22:57:43 by ray314

Merge pull request #8 from mattmular/feature

fuck you git

---

