## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2021-02-28](docs/good-messages/2021/2021-02-28.md)


2,069,530 events, 1,184,680 push events, 1,701,507 commit messages, 94,575,058 characters


## [staebal/lsss-wip@2af768b86e...](https://github.com/staebal/lsss-wip/commit/2af768b86e3a5cfaa5cf4b66e3dacbb2fc04dff2)
##### 2021-02-28 01:26:27 by Tyler

Bug fixes and credits update from design session

Apparently I forgot how parenting works in DOTS. That was such a stupid bug! I get that maybe someone would want to separate parenting from positioning, but at the same time, does that really justify needing to add two components to an entity to parent something?

Overall, the design session lead to a better mouse look, a material for the k-wings, a sound effect for the k-wings that is very satisfying (it sounds different from within the cockpit in a realistic way that I wasn't expecting), and more bugfixes.

I'll be slowly updating the designs throughout the week, but for now I need to get some more documentation done while my mind is weekend fresh.

I'm really cutting this close to a February release, and I really wish I had some help, but such is life I guess.

---
## [NetBSD/pkgsrc@2a41e5986e...](https://github.com/NetBSD/pkgsrc/commit/2a41e5986e311f9345f6116e08a4a32f79af891d)
##### 2021-02-28 08:38:58 by nia

games: add abbayedesmorts.

Cross-platform port of the indie game l'Abbaye des Morts.

In the 13th century, the Cathars, clerics who preached about the poverty of
Christ and defended life without material aspirations, were treated as
heretics by the Catholic Church and expelled out of the Languedoc region in
France. One of them, called Jean Raymond, found an old church in which to
hide from crusaders, not knowing that beneath its ruins lay buried an ancient
evil.

l'Abbaye des Morts has been inspired by the tragic history of the Cathars
and platform games for ZX Spectrum computers like Manic Miner, Jet Set Willy
or Dynamite Dan.

Faith will be your only weapon in this platformer styled like a ZX Spectrum
game. Black backgrounds, 1 color sprites and 1 bit sounds are a proper fit
for a raw story. The lack of details turn on the player's imagination,
creating a unique experience for each player.

---
## [elias97850/spark@acc3629b07...](https://github.com/elias97850/spark/commit/acc3629b071119b40d3827677454177fdd95f5bd)
##### 2021-02-28 09:10:27 by elias

Current: Limited chars of textfields, organized and cleaned up

Next: Complexity of password, full name for the users?, "Forgot Password" UI, Firebase accounts, more UX and comments.

Comment: I wasn't going to work on this today, I was going to "take a break", buuuuut... here I am ^.^
I just feel like I'm not doing shit if I'm just watching series all day, idk, and this felt productive xD. AS LONG AS I CAN EVADE AN EXISTENTIAL CRISIS then it's all good.
Hello from the past, hope you have/you're having/you had a great day! And here... https://youtu.be/HLiCZbhZdsM, an adventure awaits, but drink water and take care! << might be a bit cringe xD but it's because I'm listening to that song right now, so put it on 2:40 and read from "Hello from... take care!" and imagine me screaming and waving with a smile from half a mile a way as the sun sets. (I know, I'm very self-aware of how weird all this is xD, it is 5:05am, and I haven't slept, the life of a programmer? Maybe just the life of someone with a fucked up sleeping schedule) BYE!

---
## [nsheetz/perks@75af619d5e...](https://github.com/nsheetz/perks/commit/75af619d5e2705c0a1d048ef17aed1fd10c8db03)
##### 2021-02-28 11:02:47 by nsheetz

visual cleanup

-Remove great big title row taking up valuable page-inches and put more info in the <title>
-Replace "locked items" (since "locked" means something else for most of the UI) with "spoilers", which was really the point of adding this feature anyway.
-Typo fix in target zone toolbox
-Align hub enable label text right because it damn looks better. Still can't get it anywhere near the checkbox though. Curse you sometimes, bootstrap!
-Add missing close-quote on collector count label class that was fucking all kinds of things up while I was trying to manipulate that part of the DOM
-Hide hub-enable input if hubs are locked and spoilers are hidden, or if hubs are unlocked and maxed items are hidden.

---
## [mrakgr/The-Spiral-Language@5ca9169b58...](https://github.com/mrakgr/The-Spiral-Language/commit/5ca9169b58f4065fa6f68fbcece8aed838f061c2)
##### 2021-02-28 12:01:57 by Marko Grdinić

"9:50am. Let me finish chilling and then I will start.

10:10am. Let me start. I need to focus.

I set out to carve out my own path, and I am going to accept all that comes with it. By the end of next week I will know where I stand with respect with Spiral. Most likely the feedback will be poor.

Ideally, I'd have had a good time with everyone seeing the advantages of Spiral right away. That would have been my golden ticket to a brighter timeline.

To make the annoyance of actually reaching out to sponsors even remotely worth it, the path should be smooth. I should not have to think especially hard how to convince them of its benefits. But that way of thinking is just naive. Even though the benefits of having sponsors are so mediocre to the alternative.

The demonic path beckons to me.

I cannot rely on humans. I must draw out the power of the machines and make it my own. I should slaughter and pilage to get my resources.

10:20am. This world is unfair. It would be so much better for everyone around if I could get benefits from Spiral based on its technical merits. But even though my skills are such a perfect fit for supporting the efforts of these hardware companies, I can already see the future where nothing comes from that.

I made that ML library in 2018 for nothing.

In the end, I'll get my benefits from being able to make UIs and concurrency.

10:25am.

```
inl children l c =
    inl len = listm.length l
    inl in_front = a64.init len (fun _ => 0)
    inl prev_widget = a64.init len (fun _ => None)
    inl disp = disposablem.composite.create()
    listm.fold (fun i x =>
        inl subs = subscribe x fun x =>
            match a64.index prev_widget i with
            | None => loop.forDown' (nearFrom: i to: 0) (fun i => a64.set in_front i (a64.index in_front i + 1))
            | Some: x => removeWidget x c
            addWidget x (a64.index in_front i) c
            a64.set prev_widget i (Some: x)
        disposablem.composite.add disp subs
        i+1
        ) 0 l
    |> fun _ => Some: toDisposable disp
```

10:30am. Doing a bit of cleaning and optimization.

...I really am scared of reverse UIs. Teaching agents poker will be a piece of cake in contrast to teaching them how to interact with the world. I am going to have to draw out all my programming skill to deal with this.

But if I could just deal with this I will be able to do anything.

10:30am. Right now, I could be considered an expert programmer in terms of skill, but I not...a what? A true AI practitioner? A true seeker of the Singularity?

I must go further. There is a level beyond the one I am currently. I am still too green to get what I want.

Until I reach that level, this journal which is my inheritance will continue.

At some point I will reach the threeshold of skill and make my passage into the shadows, but until then I might as well continue being a fool.

10:35am. What bothers me the most right now?

The fact that moving and deleting files is so messed up in Spiral! It is like having a bunch of garbage backing up the front porch. I can't stand it.

Damn it. Once I manage to finish DREAM and agent training has started on NL Holdem, I am going to make some time, even a whole month if need be to iron the kinks out.

Right now, I did a really good thing with those streams, but the very top level is such a mess.

I am sending those errors to the server in a mutable fashion, I keep stale data around, I do the deletions directly. Some of the memoization optimizations are working against me...

This just cannot stand. Even though I spent so much time working on this, I clearly haven't done it properly yet.

10:45am. I did it for the sake of the ML library, but it really is such a joy to work on a language. After tasting bitter limitation in 2016, Spiral is giving me so much freedom right now.

But if I want to gain benefits from that, I am going to have to keep working at it.

...

Let me focus on the task at hand.

Before I can make my first UI, I need to put something else into the library. For buttons, I should do the event handler.

```
        def f(args):
            args.text = "X"
            label.text = "The button has been pressed."
        btn.fbind("on_press",f)
```

Let me try out `fbind`.

```
btn.fbind("on_press",f)
```

Yes, this works. Ok.

```
open rx
prototype on_press m : (() -> ()) -> m -> disposable
```

Let me make the prototype this. I'll ignore the first argument which is just the control itself.

How do I create observables from a callback?

```
q = rx.disposable.disposable.Disposable(lambda *x: print("qwe"))
x = rx.disposable.serialdisposable.SerialDisposable()
x.disposable = q
x.disposable = q
x.disposable = q
x.disposable = q
```

This gets disposed once. Ok, I see.

```
// Creates a disposable.
inl create (f : () -> ()) : disposable = $"rx.disposable.disposable.Disposable(!f)"
```

This should do nicely.

https://kivy.org/doc/stable/api-kivy.event.html#kivy.event.EventDispatcher.unbind_uid

Actually instead of assuming the uid is u64, I should just leave it as an object.

11:15am.

```
inl bind_zero (event_name : string) (f : () -> ()) x =
    inl uid : obj = $"!x.fbind(!event_name,lambda x: !f())"
    disposablem.create fun () => $"!x.unbind_uid(!event_name,!uid)"
```

Made this helper. Ok...

```
instance on_press button = helpers.bind_zero "on_press"
```

Let me move them in their own module.

For now just being able to respond to button presses is enough.

11:20am. Focus me. What comes next?

...Besides realizing it is the end of the month, so I should download High Rise Invasion to spent a bit of my budget?

Let me make a lithe test file. It is too early to run anything, but I should be able to write out a simple UI and see if the types match. That is what I should do here.

```
-(orientation Vertical)
```

Whops, I got the - wrong.

```
inl (~-) f x c = f x c . None
inl (~+) f x c = Some: subscribe x (fun x => f x c)
inl (~@) f x c = Some: (f x c : disposable)
inl (~#) f x c =
```

This is how I should have done it.

Ok...

```
        children [

            ]
```

Ah, crap. I should have allowed empty lists.

```fs
let sequence_body d = (many1 (indent (col d) (=) (sepBy1 operators (skip_op ";"))) |>> List.concat) d
```

Let me remove that outer `remove1`.

Yeah, that should do it.

This is worth a patch.

```
open kivy
open lithe
inl UI =
    boxlayout [
        -orientation Vertical
        children [
            label [-text "Press the button."]
            button [
                -text "Press me."
                @on_press (fun () => $"print(\"The button has been pressed.\")")
                ]
            ]
        ]
```

This actually matches. It compiles down to an `() -> observable widget`.

Why don't I run it? I need to make an app, set the root and run this.

```
inl main () =
    inl app = appm.create()
    inl _ = rx.subscribe UI (appm.root app)
    appm.run app
```

This seems good.

Let me give it a try.

```
        v1 = kivy.uix.label.Label()
        v2 = rx.disposable.compositedisposable.CompositeDisposable()
            ^
------------------------------------------------------------

c:\Users\Marko\Source\Repos\The Spiral Language\Spiral Compilation Tests\cython_experiments\rx1\lithe_test.pyx:13:13: undeclared name not builtin: rx
```

Keeping track of imports sure is annoying.

```
Error compiling Cython file:
------------------------------------------------------------
...
        v1 = kivy.uix.button.Button()
        v2 = rx.disposable.compositedisposable.CompositeDisposable()
        v1.text = "Press me."
        v3 = Closure2()
        v4 = v1.fbind("on_press",lambda x: v3())
        del v3
           ^
------------------------------------------------------------

c:\Users\Marko\Source\Repos\The Spiral Language\Spiral Compilation Tests\cython_experiments\rx1\lithe_test.pyx:48:12: can not delete variable 'v3' referenced in nested scope
```

You son of a bitch.

I am talking to the Cython compiler.

```
open rx
inl bind_zero (event_name : string) (f : () -> ()) x =
    inl f (x : obj) = f ()
    inl uid : obj = $"!x.fbind(!event_name,!f)"
    disposablem.create fun () => $"!x.unbind_uid(!event_name,!uid)"
```

Let me try this for the time being.

```
def __call__(self, object v2):
```

It is telling me that this takes a single argument.

11:55am. Mhhh, no there is something wrong. This v2 is the `observer`. Maybe it should also take in the scheduler?

```
 AttributeError: module 'kivy.uix' has no attribute 'boxlayout'
```

Ah, the problem was in subscribe. I need to pass it the optional arg as well.

But how will I get around the problem of the Cython lambdas being broken?

12pm.

```
inl create forall a. (f : observer a -> disposable) : observable a = $"rx.create(!f)"
```

Actually, I meant to say create. This is not working for me. I am going to have to put in var args into the language.

```
def qwe(* a) : pass
```

Thankfully this is valid syntax.

```
inl create forall a. (f : observer a -> disposable) : observable a = inl f (x : tuple) = f $"!x[0]" in $"rx.create(!f)"
```

Let me do it like this.

12:10pm. Wonderful.

The UI shows up! And the solution I have now is more efficient that partially applying closures. Hopefully I won't run into functions that require callbacks which have both tuple and dict arguments. That would suck."

---
## [MariaMod/Young-Maria@62a5f1da4a...](https://github.com/MariaMod/Young-Maria/commit/62a5f1da4aa44a9065271ac2953c159f5ff1a719)
##### 2021-02-28 17:39:03 by MilkyNail (MariaMod)

Add files via upload

Family Bitch mode update:
- Now, when you start with the Family Bitch perk, the farm is already discovered + you have 50 points of relationship with Ralf, and you didn't see the very first scene with him (when you obtain the collar) + granddad has already seen you with him
- Added a new item to the Dog girl magazine - a realistic dog dildo. Use it to add some FB Corruption for 20 Energy. The only blowjob is available for now
- Now, you can use the cheat codes menu on your Smartphone while in FB mode. The cheat for Corruption will add FB Corruption points (but only in FB mode!)
Other changes:
- Added gifs for a Library scene. The one you see when reading erotic books
- Increased the chance to get pregnant. Base chance - 5% instead of 1% and 15% instead of 2% if you started with the "Blessed mother" perk (you don't have to restart the game)
- Now reading in the Library is not so useless. For 30 points of Energy (instead of 20) you can choose a new book - 'Social literature' and it will give you +1 to all family members' Relationship. Also, I changed the structure of this passage to add more books easier in the future
- Added two scenes by Rachael. When you go to the school detention with non-consensual content enabled and not corrupted enough, you'll see the rape scenes (with male and female teachers). This counts as a 'first interaction,' and you won't see the standard first scene

---
## [mrakgr/The-Spiral-Language@6f51ab3d1f...](https://github.com/mrakgr/The-Spiral-Language/commit/6f51ab3d1f29e4b9931d5bd4925f9990d701c456)
##### 2021-02-28 17:47:26 by Marko Grdinić

"2:15pm. Done with breakfast and chores. Let me start.

2:30pm. I am thinking how to implement the loop.

```fs
let update =
    pump
    |> Observable.scanInit init (fun model msg ->
        match msg with
        | Increment -> { model with Count = model.Count + model.Step }
        | Decrement -> { model with Count = model.Count - model.Step }
        | Reset -> init
        | SetStep n -> { model with Step = n }
        | TimerToggled on -> { model with TimerOn = on }
        | TimedTick -> if model.TimerOn then { model with Count = model.Count + model.Step } else model
        )
    |> Observable.publishInitial init
```

This is how I did in the first example...

```fs
        let start_stream = Subject.Synchronize(Subject.broadcast,ThreadPoolScheduler.Instance)
        let state =
            let init = {server_count=0; client_count=0}
            start_stream
            |> Observable.map (fun StartExample ->
                Observable.using (fun () ->
                    run [|server (AddServer >> msg_stream.OnNext); client (AddClient >> msg_stream.OnNext)|]
                    |> Disposable.compose (Disposable.Create(fun () -> server_stream.OnNext None; client_stream.OnNext None))
                    ) <| fun _ ->
                // Note: The follwoing mostly works fine, but can drop initial messages. It does not happen during
                // the first subscription so it is only a small problem, but for a correct agent based implementation, check out
                // the 05_ZeroMQ example.
                msg_stream |> Observable.scanInit init (fun model msg ->
                    let update (f : _ ISubject) i x = f.OnNext(Some(i, x)); i+1
                    match msg with
                    | AddServer x -> {model with server_count=update server_stream model.server_count x}
                    | AddClient x -> {model with client_count=update client_stream model.client_count x}
                    )
                )
            |> Observable.switch
            |> Observable.publishInitial init
            |> Observable.refCount
            |> Observable.observeOn ui_scheduler
```

This is how I did in the zeromq example.

```fs
        let state =
            start_stream
            |> Observable.switchMap (fun StartExample ->
                Observable.using (fun () ->
                    // I changed to using an agent because on the weather example it is possible for messages to be sent before
                    // the Observable.scan is ready. This error is present in the 04_Zero_HelloWorld example.
                    let agent = FSharpx.Control.AutoCancelAgent.Start(fun mailbox -> async {
                        let line_counts = Array.zeroCreate l.Length
                        let rec loop () = async {
                            let! (Add(i,x)) = mailbox.Receive()
                            let count = line_counts.[i]
                            (snd streams.[i]).OnNext(Some(count, x))
                            line_counts.[i] <- count + 1
                            do! loop()
                            }
                        do! loop ()
                        })
                    l |> Array.mapi (fun i (_,f) -> f (fun x -> agent.Post(Add(i,x))))
                    |> Messaging.run
                    |> Disposable.compose (Disposable.Create(fun () -> streams |> Array.iter (fun (_,x) -> x.OnNext None)))
                    |> Disposable.compose agent
                    ) (fun _ -> Observable.neverWitness ())
                )
```

This seemed easier back when I first wrote it.

I am going to do things differently. This time. I ma not going to do scanInit or publish the observable.

I'll simplify things to their limit.

2:45pm.

```
inl UI dispatch (state : rx.observable state) =
    inl (~+) f g = +f (rx.map g state)
    boxlayout [
        -orientation Vertical
        children [
            label [-text "Press the button."]
            button [
                +text (fun x => x.button_text)
                @on_press (fun () => $"print(\"The button has been pressed.\")")
                ]
            ]
        ]
```

Let me modify the + operator.

```
inl (~+) x f g c = Some: subscribe x (fun x => f (g x) c)
```

How about this?

```
inl UI dispatch (state : rx.observable state) =
    inl (~+) x = +state x
    boxlayout [
        -orientation Vertical
        children [
            label [-text "Press the button."]
            button [
                +text (fun x => x.button_text)
                @on_press (fun () => $"print(\"The button has been pressed.\")")
                ]
            ]
        ]
```

```
inl (~#) x f g c =
    inl disp = disposablem.serial.create()
    inl x = subscribe x (fun x => disposablem.serial.set disp (f (g x) c))
    inl d = disposablem.composite.create()
    listm.iter (disposablem.composite.add d) [x; toDisposable disp]
    toDisposable d
```

Let me do this one like so as well. Now I should have full satisfaction.

```
inl ui dispatch (state : rx.observable state) =
    inl (~+) x = +state x
    boxlayout [
        -orientation Vertical
        children [
            label [-text "Press the button."]
            button [
                +text (fun x => x.button_text)
                @on_press (fun () => dispatch Clicked)
                ]
            ]
        ]
```

Now let me work towards implementing this.

Let me make the loop.

3:35pm.

```
inl loop init model view =
    inl subject = subjectm.createBehavior init
    inl state = mut init
    inl dispatch msg =
        inl x = model *state msg
        state <- x
        inl f (dt : obj) = subjectm.onNext subject x
        !!!!Import("kivy.clock")
        $"kivy.clock.Clock.schedule_once(!f)" : ()

    view dispatch (subjectm.toObservable subject)
```

I wonder if there is a way of getting the value from the subject without subscribing to it.

```
q = rx.subject.behaviorsubject.BehaviorSubject(4)
print(q.value)
```

Oh this works. Great!

4:15pm. I did a large refactoring.

```
inl loop init model view =
    inl subject = subjectm.behavior init
    inl dispatch msg =
        inl x = model (subjectm.value subject) msg
        inl f (dt : obj) = onNext subject x
        !!!!Import("kivy.clock")
        $"kivy.clock.Clock.schedule_once(!f)" : ()

    view dispatch (toObservable subject)
```

And here is how this comes out now. Let me try compiling it.

...It works the first time. Nice.

Let me make it a bit more elaborate.

4:30pm.

```
inl view dispatch (state : rx.observable state) =
    inl (~+) x = +state x
    boxlayout [
        -orientation Vertical
        children [
            label [-text "Press the button."]
            button [
                +text fun {times_clicked} =>
                    if times_clicked = 0 then "Click me."
                    else $"f\"The button has been clicked {!times_clicked} times.\""
                @on_press (fun () => dispatch Clicked)
                ]
            ]
        ]
```

This works now. Fixed a little type error to get here.

```
inl x = model (subjectm.value subject) msg
```

Actually, using the subject value is not optimal here. In concurrent settings that could result in me getting a stale value.

4:35pm. No, let me go with this for now.

```
    inl dispatch msg =
        inl f (dt : obj) = onNext subject (model (subjectm.value subject) msg)
        !!!!Import("kivy.clock")
        $"kivy.clock.Clock.schedule_once(!f)" : ()
```

Actually, let me go with this. This will be the ideal way of doing it.

4:40pm. Phew.

With this I've implemented the Elm pattern.

```
open kivy
open lithe

union msg =
    | Clicked

type state = {
    times_clicked : u32
    }

inl model (x : state) = function
    | Clicked => {x with times_clicked#=((+) 1)}

let view dispatch (state : _ state) =
    inl (~+) x = +state x
    boxlayout [
        -orientation Vertical
        children [
            label [-text "Press the button."]
            button [
                +text fun {times_clicked} =>
                    if times_clicked = 0 then "Click me."
                    else $"f\"The button has been clicked {!times_clicked} times.\""
                @on_press (fun () => dispatch Clicked)
                ]
            ]
        ]

inl main () =
    rx.rxImports()
    inl app = appm.create()
    inl _ = rx.subscribe (loop {times_clicked=0} model view) (appm.root app)
    appm.run app
```

Just look at this beauty.

```
inl RxImports =
    !!!!Import("rx")
    !!!!Import("rx.operators")
    !!!!Import("rx.disposable")
    !!!!Import("rx.subject")
```

I do not like having imports outside like this.

Let me distribute them.

4:50pm. Done. No need for those inits anymore. I'll have to do that in the PyTorch library as well, but I'll toe that line when it comes to it. Let me take a short break here.

5:25pm. I am back. Let me put lithe in its own folder just to highlight that it is its own library.

```
packages: |core-
modules:
    rx/
        types-
        disposablem
        subjectm
        main-
    kivy/
        types-
        helpers
        appm
        buttonm
        labelm
        boxlayoutm
    lithe/
        main-
    rx_test
    kivy_test
    lithe_test
```

This is how the project file looks now. In Spiral it is not a good idea to split things up too much. When writing bindings I should favor large modules with lots of functions.

```
// A lot of the functionality here could be adapted without much difficulty for other libraries, but
// this particular instance of Lithe has functionality specific to the Kivy UI library for the Python language.
```

Let me add this note.

Ok...

Lithe itself is essentially complete. I've done all of its core functionality and did the functional declarative UI toy example. This is a tremendous achievement.

In order to increase the breadth of functionality, all I need to do now is add more controls and bindings to their properties.

5:35pm. Right now I am thinking what comes next.

5:40pm. There are some things lacking in the Lithe library. Foremost, I am missing commands. But I don't have a good view of how those should be implemented. Nor do I have a particular use case I could try it out right now.

What should my next goal be? I could do that counter sure. But, I know I can do that and I do not want to waste time doing arbitrary things for the sake of exercise.

Exercise serves the purpose of preparation for challenges one cannot take on. If you can take on the challenges, then you don't need practice. Make the challenge itself the practice.

6:05pm. Right now I am thinking how to rank poker hands of all things.

I really should be thinking about game UIs instead, but my mind goes where it wants. At any rate, I will be able to handle ranking the games.

6:40pm. Done with lunch.

I am still thinking. I need to focus on getting the Leduc poker game done. This will without a doubt be my next goal.

Being able to integrate games with UI is something that would have astonished the me of 2016. This time I will do it. I will exceed my old high.

Normies love to harp about social skills - well, UIs are the social skills of the programming domain. I just need to level them up and I will get to where I want to be."

---

