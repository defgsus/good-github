## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-07-10](docs/good-messages/2023/2023-07-10.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,198,860 were push events containing 3,555,726 commit messages that amount to 302,313,900 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 74 messages:


## [xxyzz/wikitextprocessor](https://github.com/xxyzz/wikitextprocessor)@[51ba4081f4...](https://github.com/xxyzz/wikitextprocessor/commit/51ba4081f4923186b485e3e73a4db64d0a979e2f)
#### Monday 2023-07-10 00:36:48 by Kristian Järventaus

More type-checking stuff, luaexec.py

I am doing luaexec out of the way because it's the most
annoying part to type-check, because there is no way
to integrate the type-checking with the Lua stuff other
than by brute force.

There's a couple of
```
ctx.NAMESPACE_DATA
    .get("Template", {"id": None})
    .get("id"))
```
style monstrosities I modified out of the original,
because the typechecking with TypedDictionaries
are so finnicky; I *know* the {"id": None} could just
be {}, but we're initializing a dictionary anyhow,
and putting the "id" in there makes mypy shut up.

Technically it could done with a final `["id"]`,
because we can pretty much trust NAMESPACE_DATA,
but just in case we get something weird from
NAMESPACE_DATA a `.get("id")` is a final sentinel.

---
## [Selene-Amanita/bevy](https://github.com/Selene-Amanita/bevy)@[fb4c21e3e6...](https://github.com/Selene-Amanita/bevy/commit/fb4c21e3e62b3789e8e768ac63dc2205ddec698f)
#### Monday 2023-07-10 00:46:33 by Ida "Iyes

bevy_audio: ECS-based API redesign (#8424)

# Objective

Improve the `bevy_audio` API to make it more user-friendly and
ECS-idiomatic. This PR is a first-pass at addressing some of the most
obvious (to me) problems. In the interest of keeping the scope small,
further improvements can be done in future PRs.

The current `bevy_audio` API is very clunky to work with, due to how it
(ab)uses bevy assets to represent audio sinks.

The user needs to write a lot of boilerplate (accessing
`Res<Assets<AudioSink>>`) and deal with a lot of cognitive overhead
(worry about strong vs. weak handles, etc.) in order to control audio
playback.

Audio playback is initiated via a centralized `Audio` resource, which
makes it difficult to keep track of many different sounds playing in a
typical game.

Further, everything carries a generic type parameter for the sound
source type, making it difficult to mix custom sound sources (such as
procedurally generated audio or unofficial formats) with regular audio
assets.

Let's fix these issues.

## Solution

Refactor `bevy_audio` to a more idiomatic ECS API. Remove the `Audio`
resource. Do everything via entities and components instead.

Audio playback data is now stored in components:
- `PlaybackSettings`, `SpatialSettings`, `Handle<AudioSource>` are now
components. The user inserts them to tell Bevy to play a sound and
configure the initial playback parameters.
- `AudioSink`, `SpatialAudioSink` are now components instead of special
magical "asset" types. They are inserted by Bevy when it actually begins
playing the sound, and can be queried for by the user in order to
control the sound during playback.

Bundles: `AudioBundle` and `SpatialAudioBundle` are available to make it
easy for users to play sounds. Spawn an entity with one of these bundles
(or insert them to a complex entity alongside other stuff) to play a
sound.

Each entity represents a sound to be played.

There is also a new "auto-despawn" feature (activated using
`PlaybackSettings`), which, if enabled, tells Bevy to despawn entities
when the sink playback finishes. This allows for "fire-and-forget" sound
playback. Users can simply
spawn entities whenever they want to play sounds and not have to worry
about leaking memory.

## Unsolved Questions

I think the current design is *fine*. I'd be happy for it to be merged.
It has some possibly-surprising usability pitfalls, but I think it is
still much better than the old `bevy_audio`. Here are some discussion
questions for things that we could further improve. I'm undecided on
these questions, which is why I didn't implement them. We should decide
which of these should be addressed in this PR, and what should be left
for future PRs. Or if they should be addressed at all.

### What happens when sounds start playing?

Currently, the audio sink components are inserted and the bundle
components are kept. Should Bevy remove the bundle components? Something
else?

The current design allows an entity to be reused for playing the same
sound with the same parameters repeatedly. This is a niche use case I'd
like to be supported, but if we have to give it up for a simpler design,
I'd be fine with that.

### What happens if users remove any of the components themselves?

As described above, currently, entities can be reused. Removing the
audio sink causes it to be "detached" (I kept the old `Drop` impl), so
the sound keeps playing. However, if the audio bundle components are not
removed, Bevy will detect this entity as a "queued" sound entity again
(has the bundle compoenents, without a sink component), just like before
playing the sound the first time, and start playing the sound again.

This behavior might be surprising? Should we do something different?

### Should mutations to `PlaybackSettings` be applied to the audio sink?

We currently do not do that. `PlaybackSettings` is just for the initial
settings when the sound starts playing. This is clearly documented.

Do we want to keep this behavior, or do we want to allow users to use
`PlaybackSettings` instead of `AudioSink`/`SpatialAudioSink` to control
sounds during playback too?

I think I prefer for them to be kept separate. It is not a bad mental
model once you understand it, and it is documented.

### Should `AudioSink` and `SpatialAudioSink` be unified into a single
component type?

They provide a similar API (via the `AudioSinkPlayback` trait) and it
might be annoying for users to have to deal with both of them. The
unification could be done using an enum that is matched on internally by
the methods. Spatial audio has extra features, so this might make it
harder to access. I think we shouldn't.

### Automatic synchronization of spatial sound properties from
Transforms?

Should Bevy automatically apply changes to Transforms to spatial audio
entities? How do we distinguish between listener and emitter? Which one
does the transform represent? Where should the other one come from?

Alternatively, leave this problem for now, and address it in a future
PR. Or do nothing, and let users deal with it, as shown in the
`spatial_audio_2d` and `spatial_audio_3d` examples.

---

## Changelog

Added:
- `AudioBundle`/`SpatialAudioBundle`, add them to entities to play
sounds.

Removed:
 - The `Audio` resource.
 - `AudioOutput` is no longer `pub`.

Changed:
 - `AudioSink`, `SpatialAudioSink` are now components instead of assets.

## Migration Guide

// TODO: write a more detailed migration guide, after the "unsolved
questions" are answered and this PR is finalized.

Before:

```rust

/// Need to store handles somewhere
#[derive(Resource)]
struct MyMusic {
    sink: Handle<AudioSink>,
}

fn play_music(
    asset_server: Res<AssetServer>,
    audio: Res<Audio>,
    audio_sinks: Res<Assets<AudioSink>>,
    mut commands: Commands,
) {
    let weak_handle = audio.play_with_settings(
        asset_server.load("music.ogg"),
        PlaybackSettings::LOOP.with_volume(0.5),
    );
    // upgrade to strong handle and store it
    commands.insert_resource(MyMusic {
        sink: audio_sinks.get_handle(weak_handle),
    });
}

fn toggle_pause_music(
    audio_sinks: Res<Assets<AudioSink>>,
    mymusic: Option<Res<MyMusic>>,
) {
    if let Some(mymusic) = &mymusic {
        if let Some(sink) = audio_sinks.get(&mymusic.sink) {
            sink.toggle();
        }
    }
}
```

Now:

```rust
/// Marker component for our music entity
#[derive(Component)]
struct MyMusic;

fn play_music(
    mut commands: Commands,
    asset_server: Res<AssetServer>,
) {
    commands.spawn((
        AudioBundle::from_audio_source(asset_server.load("music.ogg"))
            .with_settings(PlaybackSettings::LOOP.with_volume(0.5)),
        MyMusic,
    ));
}

fn toggle_pause_music(
    // `AudioSink` will be inserted by Bevy when the audio starts playing
    query_music: Query<&AudioSink, With<MyMusic>>,
) {
    if let Ok(sink) = query.get_single() {
        sink.toggle();
    }
}
```

---
## [ATP-Engineer/Paradise](https://github.com/ATP-Engineer/Paradise)@[a3dc32cf34...](https://github.com/ATP-Engineer/Paradise/commit/a3dc32cf344dbd441e85f6cbb694b166dc1f5e4b)
#### Monday 2023-07-10 00:55:02 by ATP-Engineer

Fixes issue where Turret Control sprites arent actually updated in previous PR (#21538)

* Removes actual turret file

FUCK

* Fixes turret controllers not actually being changed

GOD DAMNIT.

---
## [sxjeru/Hbm-s-Nuclear-Tech-CI](https://github.com/sxjeru/Hbm-s-Nuclear-Tech-CI)@[b443c3449d...](https://github.com/sxjeru/Hbm-s-Nuclear-Tech-CI/commit/b443c3449d37db0017d86a1fe71cf92de3da026f)
#### Monday 2023-07-10 01:18:28 by Bob

fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you

---
## [zzzmike/cmss13](https://github.com/zzzmike/cmss13)@[d045a5d654...](https://github.com/zzzmike/cmss13/commit/d045a5d6547dcda9fc04be9b6cd50d2ff44e672f)
#### Monday 2023-07-10 01:41:05 by Drathek

Larva Queue Late Joiner Nerf (#3803)

# About the pull request

This PR makes it so players who haven't played yet have their join time
recorded, and that is used for their initial sorting value rather than
0. This means late joiners will be at the back of the line as if they
had just died.

This PR also fixes an oversight where ghosting as a facehugger would
count as death. Even though they really shouldn't be ghosting when
alive, they still shouldn't be penalized as far as the queue is
concerned.

# Explain why it's good for the game

Its not; its a bad experience for everyone that hasn't even gotten one
life in the round. However it seems I'm in the minority thinking that a
xeno shouldn't squander their first life and that death shouldn't bear
more consequences.

# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

The new informational message if you press join as xeno while currently
ineligible to be a xeno candidate:

![image](https://github.com/cmss13-devs/cmss13/assets/76988376/9fb295c2-e654-4843-9e3e-bf37f2c8755e)

</details>


# Changelog
:cl: Drathek
del: Remove first life priority for larva queue
fix: Fix ghosting as a facehugger counting as death for the larva queue
/:cl:

---
## [newstools/2023-metro](https://github.com/newstools/2023-metro)@[cfd790c9b6...](https://github.com/newstools/2023-metro/commit/cfd790c9b66b94938f19220735f3afb198067da8)
#### Monday 2023-07-10 01:47:44 by Billy Einkamerer

Created Text For URL [metro.co.uk/2023/07/09/man-infuriates-cheater-brother-by-laughing-at-his-new-ironic-tattoo-19094067/?ico=mosaic_home]

---
## [smeenai/craftinginterpreters](https://github.com/smeenai/craftinginterpreters)@[78243642e1...](https://github.com/smeenai/craftinginterpreters/commit/78243642e15178d70391d6c8dea4dc50c8ffd352)
#### Monday 2023-07-10 02:00:59 by Shoaib Meenai

[clox] Implement strings and string operations

This completes Chapters 19.1 through 19.4.

I'm using a flexible array member instead of a separate heap-allocated
string, as suggested in Challenge 19.1. This precludes Challenge 19.2,
where we avoid heap-allocating literals, but from my experience with
jlox-in-cpp I think that optimization is more trouble than its worth
(and I'm not implementing it in jlox-in-rust either).

I'm also reworking BINARY_OP a bit to enable reusing it for the
arithmetic portion of OP_ADD, rather than needing to duplicate its code
for that.

Making objVal a function instead of a macro turns out to be a bit
annoying here, since we have to cast the argument to `Obj *` explicitly.
I'll think about how to improve that later.

---
## [acdc-digital/Medex-Public-MITP](https://github.com/acdc-digital/Medex-Public-MITP)@[d36be3477f...](https://github.com/acdc-digital/Medex-Public-MITP/commit/d36be3477f8fa0e7999de2656b2eea206de8c514)
#### Monday 2023-07-10 02:44:44 by Matthew Simon

aider: work in progress

# Context:
USER: It looks like you're encountering a Python error related to calling a function with an unexpected keyword argument, specifically request_kwargs. This is happening when calling the partition_via_api() function. This can often be due to changes in the function definition (like its parameters) in recent updates of the codebase or its dependencies. Here’s what the error looked like.

File "/Users/matthewsimon/miniconda3/lib/python3.10/site-packages/langchain/document_loaders/unstructured.py", line 71, in load
elements = self._get_elements()
File "/Users/matthewsimon/miniconda3/lib/python3.10/site-packages/langchain/document_loaders/unstructured.py", line 177, in _get_elements
return get_elements_from_api(
File "/Users/matthewsimon/miniconda3/lib/python3.10/site-packages/langchain/document_loaders/unstructured.py", line 141, in get_elements_from_api
return partition_via_api(
TypeError: partition_via_api() got an unexpected keyword argument 'request_kwargs'

It looks like you're encountering a Python error related to calling a function with an unexpected keyword argument, specifically request_kwargs. This is happening when calling the partition_via_api() function. This can often be due to changes in the function definition (like its parameters) in recent updates of the codebase or its dependencies.

Here are a few steps to troubleshoot this issue:

Check the function definition: Look up the function definition for partition_via_api(). You should be able to find this function in the langchain/document_loaders/unstructured.py file. Make sure the parameters you are passing match the parameters defined in the function. If request_kwargs is not in the function definition, then this is likely the source of your problem.
Check for updates: If the function definition and the function call seem to match, ensure that you are using the correct versions of your dependencies. It's possible that a recent update changed the function parameters.
Check the documentation: If the function is part of a library you're using, check the documentation for that function to see if it's been updated or deprecated. You may need to adjust your code to reflect the changes.
Check for changes in your codebase: If this is a function from your own codebase, check if recent changes might have altered the function signature. Check your code's version control history (if applicable) to see if there's been any recent change in this function.
USER: While access to the hosted Unstructured API will remain free, API Keys will soon be required to make requests. To prevent any disruption, get yours here now and start using it today!

Checkout the rest of the readme below to get started making API calls. We'd love to hear your feedback, let us know how it goes in our community slack. And stay tuned for improvements to both quality and performance!

General Pre-Processing Pipeline for Documents

This repo implements a pre-processing pipeline for the following documents. Currently, the pipeline is capable of recognizing the file type and choosing the relevant partition function to process the file.

Category	Document Types
Plaintext	.txt, .eml, .msg, .xml, .html, .md, .rst, .json, .rtf
Images	.jpeg, .png
Documents	.doc, .docx, .ppt, .pptx, .pdf, .odt, .epub, .csv, .tsv, .xlsx
🚀 Unstructured API
Try our hosted API! It's freely available to use with any of the filetypes listed above. This is the easiest way to get started. If you'd like to host your own version of the API, jump down to the Developer Quickstart Guide.

 curl -X 'POST' \
  'https://api.unstructured.io/general/v0/general' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -H 'unstructured-api-key: <YOUR API KEY>'
  -F 'files=@sample-docs/family-day.eml' \
  | jq -C . | less -R
Parameters
Strategies
Four strategies are available for processing PDF/Images files: hi_res, fast, ocr_only and auto. fast is the default strategy and works well for documents that do not have text embedded in images.

On the other hand, hi_res is the better choice for PDFs that may have text within embedded images, or for achieving greater precision of element types in the response JSON. Please be aware that, as of writing, hi_res requests may take 20 times longer to process compared to the fast option. See the example below for making a hi_res request.

 curl -X 'POST' \
  'https://api.unstructured.io/general/v0/general' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'files=@sample-docs/layout-parser-paper.pdf' \
  -F 'strategy=hi_res' \
  | jq -C . | less -R
The ocr_only strategy runs the document through Tesseract for OCR. Currently, hi_res has difficulty ordering elements for documents with multiple columns. If you have a document with multiple columns that do not have extractable text, we recommend using the ocr_only strategy. Please be aware that ocr_only will fall back to another strategy if Tesseract is not available.

For the best of all worlds, auto will determine when a page can be extracted using fast or ocr_only mode, otherwise it will fall back to hi_res.

OCR languages
You can also specify what languages to use for OCR with the ocr_languages kwarg. See the Tesseract documentation for a full list of languages and install instructions. OCR is only applied if the text is not already available in the PDF document.

curl -X 'POST' \
  'https://api.unstructured.io/general/v0/general' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'files=@sample-docs/english-and-korean.png' \
  -F 'strategy=ocr_only' \
  -F 'ocr_languages=eng'  \
  -F 'ocr_languages=kor'  \
  | jq -C . | less -R
Coordinates
When elements are extracted from PDFs or images, it may be useful to get their bounding boxes as well. Set the coordinates parameter to true to add this field to the elements in the response.

 curl -X 'POST' \
  'https://api.unstructured.io/general/v0/general' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'files=@sample-docs/layout-parser-paper.pdf' \
  -F 'coordinates=true' \
  | jq -C . | less -R
PDF Table Extraction
To extract the table structure from PDF files using the hi_res strategy, ensure that the pdf_infer_table_structure parameter is set to true. This setting includes the table's text content in the response. By default, this parameter is set to false to avoid the expensive reading process.

 curl -X 'POST' \
  'https://api.unstructured.io/general/v0/general' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'files=@sample-docs/layout-parser-paper.pdf' \
  -F 'strategy=hi_res' \
  -F 'pdf_infer_table_structure=true' \
  | jq -C . | less -R
Encoding
You can specify the encoding to use to decode the text input. If no value is provided, utf-8 will be used.

curl -X 'POST'
 'https://api.unstructured.io/general/v0/general' \
 -H 'accept: application/json'  \
 -H 'Content-Type: multipart/form-data' \
 -F 'files=@sample-docs/fake-power-point.pptx' \
 -F 'encoding=utf_8' \
 | jq -C . | less -R
XML Tags
When processing XML documents, set the xml_keep_tags parameter to true to retain the XML tags in the output. If not specified, it will simply extract the text from within the tags.

curl -X 'POST'
 'https://api.unstructured.io/general/v0/general' \
 -H 'accept: application/json'  \
 -H 'Content-Type: multipart/form-data' \
 -F 'files=@sample-docs/fake-xml.xml' \
 -F 'xml_keep_tags=true' \
 | jq -C . | less -R
Developer Quick Start
Using pyenv to manage virtualenv's is recommended
Mac install instructions. See here for more detailed instructions.

brew install pyenv-virtualenv
pyenv install 3.8.17
Linux instructions are available here.

Create a virtualenv to work in and activate it, e.g. for one named document-processing:

pyenv  virtualenv 3.8.17 document-processing
pyenv activate document-processing

See the Unstructured Quick Start for the many OS dependencies that are required, if the ability to process all file types is desired.

Run make install
Start a local jupyter notebook server with make run-jupyter
OR
just start the fast-API locally with make run-web-app
Using the API locally
After running make run-web-app (or make docker-start-api to run in the container), you can now hit the API locally at port 8000. The sample-docs directory has a number of example file types that are currently supported.

For example:

 curl -X 'POST' \
  'http://localhost:8000/general/v0/general' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'files=@sample-docs/family-day.eml' \
  | jq -C . | less -R
The response will be a list of the extracted elements:

[
  {
    "element_id": "db1ca22813f01feda8759ff04a844e56",
    "coordinates": null,
    "text": "Hi All,",
    "type": "UncategorizedText",
    "metadata": {
      "date": "2022-12-21T10:28:53-06:00",
      "sent_from": [
        "Mallori Harrell <mallori@unstructured.io>"
      ],
      "sent_to": [
        "Mallori Harrell <mallori@unstructured.io>"
      ],
      "subject": "Family Day",
      "filename": "family-day.eml"
    }
  },
...
...
The output format can also be set to text/csv to get the data in csv format rather than json:

 curl -X 'POST' \
  'http://localhost:8000/general/v0/general' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'files=@sample-docs/family-day.eml' \
  -F 'output_format="text/csv"'
The response will be a list of the extracted elements in csv format:

"type,text,element_id,filename,page_number,url,sent_from,sent_to,subject,sender\n
UncategorizedText,\"Hi,\",bc50944723f014607ad612b6983944a7,alert.eml,1,,['Mallori Harrell <mallori@unstructured.io>'],['Mallori Harrell <mallori@unstructured.io>'],ALERT: Stolen Lunch,Mallori Harrell <mallori@unstructured.io>\n
NarrativeText,\"It has come to our attention that as of 9:00am this morning, Harold's lunch is missing. If this was done in error please return the lunch immediately to the fridge on the 2nd floor by noon.\",51944d1f63f9472edb165fb3c9e5c525,alert.eml,1,,['Mallori Harrell <mallori@unstructured.io>'],['Mallori Harrell <mallori@unstructured.io>'],ALERT: Stolen Lunch,Mallori Harrell <mallori@unstructured.io>\n
NarrativeText,\"If the lunch has not been returned by noon, we will be reviewing camera footage to determine who stole Harold's lunch.\",8e8f9e2e50e39e072fda08d277aa77b9,alert.eml,1,,['Mallori Harrell <mallori@unstructured.io>'],['Mallori Harrell <mallori@unstructured.io>'],ALERT: Stolen Lunch,Mallori Harrell <mallori@unstructured.io>\n
NarrativeText,The perpetrators will be PUNISHED to the full extent of our employee code of conduct handbook.,736a826679b971f594103fd9751e5c8f,alert.eml,1,,['Mallori Harrell <mallori@unstructured.io>'],['Mallori Harrell <mallori@unstructured.io>'],ALERT: Stolen Lunch,Mallori Harrell <mallori@unstructured.io>\n
UncategorizedText,\"Thank you for your time,\",3eeae5f64dab54c52dd5fff779808071,alert.eml,1,,['Mallori Harrell <mallori@unstructured.io>'],['Mallori Harrell <mallori@unstructured.io>'],ALERT: Stolen Lunch,Mallori Harrell <mallori@unstructured.io>\n
Title,Unstructured Technologies,d5b612de8cd918addd9569b0255b65b2,alert.eml,1,,['Mallori Harrell <mallori@unstructured.io>'],['Mallori Harrell <mallori@unstructured.io>'],ALERT: Stolen Lunch,Mallori Harrell <mallori@unstructured.io>\n
Title,Data Scientist,46b174f1ec7c25d23e5e50ffff0cc55b,alert.eml,1,,['Mallori Harrell <mallori@unstructured.io>'],['Mallori Harrell <mallori@unstructured.io>'],ALERT: Stolen Lunch,Mallori Harrell <mallori@unstructured.io>\n"
Parallel Mode for PDFs
As mentioned above, processing a pdf using hi_res is currently a slow operation. One workaround is to split the pdf into smaller files, process these asynchronously, and merge the results. You can enable parallel processing mode with the following env variables:

UNSTRUCTURED_PARALLEL_MODE_ENABLED - set to true to process individual pdf pages remotely, default is false.
UNSTRUCTURED_PARALLEL_MODE_URL - the location to send pdf page asynchronously, no default setting at the moment.
UNSTRUCTURED_PARALLEL_MODE_THREADS - the number of threads making requests at once, default is 3.
UNSTRUCTURED_PARALLEL_MODE_SPLIT_SIZE - the number of pages to be processed in one request, default is 1.
UNSTRUCTURED_PARALLEL_RETRY_ATTEMPTS - the number of retry attempts, default is 1.
UNSTRUCTURED_PARALLEL_RETRY_BACKOFF_TIME - the backoff time in seconds for each retry attempt, default is 1.0.
Generating Python files from the pipeline notebooks
You can generate the FastAPI APIs from your pipeline notebooks by running make generate-api.

💫 Instructions for using the Docker image
The following instructions are intended to help you get up and running using Docker to interact with unstructured-api. See here if you don't already have docker installed on your machine.

NOTE: we build multi-platform images to support both x86_64 and Apple silicon hardware. Docker pull should download the corresponding image for your architecture, but you can specify with --platform (e.g. --platform linux/amd64) if needed.

We build Docker images for all pushes to main. We tag each image with the corresponding short commit hash (e.g. fbc7a69) and the application version (e.g. 0.5.5-dev1). We also tag the most recent image with latest. To leverage this, docker pull from our image repository.

docker pull quay.io/unstructured-io/unstructured-api:latest
Once pulled, you can launch the container as a web app on localhost:8000.

docker run -p 8000:8000 -d --rm --name unstructured-api quay.io/unstructured-io/unstructured-api:latest --port 8000 --host 0.0.0.0
Security Policy
See our security policy for information on how to report security vulnerabilities.

Learn more
Section	Description
Unstructured Community Github	Information about Unstructured.io community projects
Unstructured Github	Unstructured.io open source repositories
Company Website	Unstructured.io product and company info

---
## [acdc-digital/Medex-Public-MITP](https://github.com/acdc-digital/Medex-Public-MITP)@[fe7280a93b...](https://github.com/acdc-digital/Medex-Public-MITP/commit/fe7280a93b19564d591c0f4436cbfaa67f8f262f)
#### Monday 2023-07-10 02:44:44 by Matthew Simon

aider: Added a function `retrieve_from_index` to retrieve documents from the index based on a query.

# Context:
USER: I'd like the retriever to be a function call from openai, similar to an agent call searching the index. Here's an example only for reference: "OpenAI functions
Certain OpenAI models (like gpt-3.5-turbo-0613 and gpt-4-0613) have been fine-tuned to detect when a function should to be called and respond with the inputs that should be passed to the function. In an API call, you can describe functions and have the model intelligently choose to output a JSON object containing arguments to call those functions. The goal of the OpenAI Function APIs is to more reliably return valid and useful function calls than a generic text completion or chat API.

The OpenAI Functions Agent is designed to work with these models.

Install openai,google-search-results packages which are required as the langchain packages call them internally

pip install openai google-search-results

from langchain import LLMMathChain, OpenAI, SerpAPIWrapper, SQLDatabase, SQLDatabaseChain
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")
search = SerpAPIWrapper()
llm_math_chain = LLMMathChain.from_llm(llm=llm, verbose=True)
db = SQLDatabase.from_uri("sqlite:///../../../../../notebooks/Chinook.db")
db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)
tools = [
    Tool(
        name = "Search",
        func=search.run,
        description="useful for when you need to answer questions about current events. You should ask targeted questions"
    ),
    Tool(
        name="Calculator",
        func=llm_math_chain.run,
        description="useful for when you need to answer questions about math"
    ),
    Tool(
        name="FooBar-DB",
        func=db_chain.run,
        description="useful for when you need to answer questions about FooBar. Input should be in the form of a question containing full context"
    )
]

agent = initialize_agent(tools, llm, agent=AgentType.OPENAI_FUNCTIONS, verbose=True)

agent.run("Who is Leo DiCaprio's girlfriend? What is her current age raised to the 0.43 power?")

    > Entering new  chain...

    Invoking: `Search` with `{'query': 'Leo DiCaprio girlfriend'}`

    Amidst his casual romance with Gigi, Leo allegedly entered a relationship with 19-year old model, Eden Polani, in February 2023.
    Invoking: `Calculator` with `{'expression': '19^0.43'}`

    > Entering new  chain...
    19^0.43```text
    19**0.43
    ```
    ...numexpr.evaluate("19**0.43")...

    Answer: 3.547023357958959
    > Finished chain.
    Answer: 3.547023357958959Leo DiCaprio's girlfriend is reportedly Eden Polani. Her current age raised to the power of 0.43 is approximately 3.55.

    > Finished chain.

    "Leo DiCaprio's girlfriend is reportedly Eden Polani. Her current age raised to the power of 0.43 is approximately 3.55.""

---
## [JeromeFitz/websites](https://github.com/JeromeFitz/websites)@[2b5ab8c179...](https://github.com/JeromeFitz/websites/commit/2b5ab8c179a289e82de6c8aa8c7128888b5c6a00)
#### Monday 2023-07-10 03:02:12 by Jerome Fitzgerald

⚡️  NICE-58 performance updates (#1703)

Would like to finally move a parallel website outside of this repo into here, heh:

## Commits

- ⚡️  dont use esm import for radix-ui [b]
- ⚡️  i actually think this hurts perf now ☉_☉ [b]
- ⚡️  cx (!twMerge); 404 link home 
- ⚡️  (next) dynamic !ssr is not ... well working
- ⚡️  siteColors; next/dynamic; cx-vs-twMerge
- 📌  (deps) `@types.node@18.11.9`
- ♻️  moving files around again
- 🚨  (tailwind) tap-dance around siteColors narrowed list
- ⚡️  tsup build; lhci improvements; tailwind
- ⚡️  icon first visually, second in html
- ⚡️  (notion) !EmojiWrapper for now
  - Aye, since `notion` is pretty much _the reason_ for the website, delaying the imports for `node-emoji|emoji-regex` ends up doing nothing but causing more threads to happen.
  - Turning off for now. Instead should pass a configuration setting if people want this or not.
  - I say yes, though descriptors leave a lot to be desired, especially as visually it is better with spacing
  - Acceptable performance hit/trade-off in my estimation. But geez, that was hard to figure out, haha.
- 🐛  (next) Image.client, and optimizations
  - Pass `sizes` 😑 haha how was this also turned off?
- 🚚  (next) static is redundant, + favicon/manifest
  - No need for PWA but some things are nice
- 🔐  (next) _privateFolders
- 🔧  (tsconfig) shared for dev|prod split due to aggressive next
- ⚡️  (next) preconnects, final meta stuff, ship 🚀
  - Ah yes, forgot the `preconnect` hack 🤣
  - Added some more meta stuff too while we were here
  - Altered some sizing on large screens
- 👷  (e2e) npx not pnpm for random installs
  - This should not break `pnpm|turbo` cache -- right? 🙏🏻 

## Breakdown

- Site Architecture movement
- `next/dynamic` should be sparesly used I think
  - If SSR _can_ load it, and it is not a heavy `css|js` hit, this would degrade non-js browsers
- `Emoji` This is not the way to do this, heh
  - yes `node-emoji` (`41.1kB`) and `emoji-regex` (`28.5kB`) are hits
  - but they serve a repetitive purpose _throughout_
  - this visual to html swap works but requires some trade-offs that I do not like
  - need to officially confirm about wrapping emojis with `alt` text too
- `twMerge` is a `~6kB` hit, but it does a lot of _good_
  -  Went through and made everything `cx` official
  - Only 1-2 needed `twMerge` still -- and can be done
- Move away from `framer-motion` until we can determine actual site use
  - `Loading` is not enough of a warranted reason
- Unused `css` from Radix-UI imports
  - On Development we go very dynamic in ensuring everything is available to us
  - For Production we should limit the amount of `css` where possible
  - This is not the _best_ way to go about this as it is confusing, but on the right track at least  
  - Need to tap-dance around dynamic imports and the _now_ excluded colors


## Stats

Good news, we are starting from a Vercel RES of `100` on everything

The thing to hyper-focus on at the moment is Google:
- Lighthouse (`pnpm lhci` w/ PR stats) & PageSpeed Insights (`https://pagespeed.web.dev/`)

**Before:**
- Performance: 92
- Accessibility: 97
- Best Practices: 100
- SEO: 100

`*` Accessibility:   This is/was due to Radix-UI Pills where we follow their lead on 4 BG 11 Text
  - Passes their tests, not Google
  - To appease we drop to 3 BG (though should be 4 BG on Light)

**After:**
- Performance: 98
- Accessibility: 100
- Best Practices: 100
- SEO: 100

## Next Steps

Final port of un-shared stuff -- though we can probably just transpile or way past this short-term

SEO
  - Misleading as we need to plant-based beef up the Next Metadata generation
  - Recommendation: `/${slug}/seo` and continue to keep separate in KV
  - Also KV is probably not ideal and should we move to Postgres? TOO MNAY QUESTIONS
    - Upstash has no problems, but if we did Vercel we would hit their limits (through Upstash ... 🥴)
    
    
 ## Outcome

Aye, I'll take it. We have to do a `skip ci` to put `@main` back of the gh-action workflows:

<img width="1000" alt="image" src="https://github.com/JeromeFitz/websites/assets/3099369/480dd040-d619-40fc-a3ee-869f2f45cc2f">


<img width="1000" alt="image" src="https://github.com/JeromeFitz/websites/assets/3099369/035cfe93-4939-4dee-a774-0bc97eeaad1a">

<img width="1000" alt="image" src="https://github.com/JeromeFitz/websites/assets/3099369/73c4cd10-7bd6-4bfa-85de-553a11eb9d89">

---
## [Elchanz3/android_kernel_samsung_sdm845_2](https://github.com/Elchanz3/android_kernel_samsung_sdm845_2)@[2864b20b26...](https://github.com/Elchanz3/android_kernel_samsung_sdm845_2/commit/2864b20b2631e217722e4f044b53b2939ae96711)
#### Monday 2023-07-10 03:25:22 by Linus Torvalds

Revert "x86/apic: Include the LDR when clearing out APIC registers"

[ Upstream commit 950b07c14e8c59444e2359f15fd70ed5112e11a0 ]

This reverts commit 558682b5291937a70748d36fd9ba757fb25b99ae.

Chris Wilson reports that it breaks his CPU hotplug test scripts.  In
particular, it breaks offlining and then re-onlining the boot CPU, which
we treat specially (and the BIOS does too).

The symptoms are that we can offline the CPU, but it then does not come
back online again:

    smpboot: CPU 0 is now offline
    smpboot: Booting Node 0 Processor 0 APIC 0x0
    smpboot: do_boot_cpu failed(-1) to wakeup CPU#0

Thomas says he knows why it's broken (my personal suspicion: our magic
handling of the "cpu0_logical_apicid" thing), but for 5.3 the right fix
is to just revert it, since we've never touched the LDR bits before, and
it's not worth the risk to do anything else at this stage.

[ Hotpluging of the boot CPU is special anyway, and should be off by
  default. See the "BOOTPARAM_HOTPLUG_CPU0" config option and the
  cpu0_hotplug kernel parameter.

  In general you should not do it, and it has various known limitations
  (hibernate and suspend require the boot CPU, for example).

  But it should work, even if the boot CPU is special and needs careful
  treatment       - Linus ]

Link: https://lore.kernel.org/lkml/156785100521.13300.14461504732265570003@skylake-alporthouse-com/
Reported-by: Chris Wilson <chris@chris-wilson.co.uk>
Acked-by: Thomas Gleixner <tglx@linutronix.de>
Cc: Bandan Das <bsd@redhat.com>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [ohef/Dungeon-5.0](https://github.com/ohef/Dungeon-5.0)@[74a06bc72b...](https://github.com/ohef/Dungeon-5.0/commit/74a06bc72ba2082f7527ed251416fa2769d7bac9)
#### Monday 2023-07-10 03:39:14 by Omar Hefnawi

Maybe last commit

Honestly an SRPG is quite an undertaking; that and I'm not really
convinced that I'm up to the task in designing it. For now, if there's
one thing is that lager is quite an amazing library that I learnt a lot
from (holy shit meta programming batman)

It works, you need some content; I may update that, in the meantime I'll
just leave this here if you're interested into what I'm up to.

---
## [KingDragoness/ProjectHypatios](https://github.com/KingDragoness/ProjectHypatios)@[54d666fc7e...](https://github.com/KingDragoness/ProjectHypatios/commit/54d666fc7ee613d726101ed44e3cc70fe8b1cf4c)
#### Monday 2023-07-10 03:39:53 by KingDragoness

Hypatios 1.5.5b3 (quality of life improvements, bug fixes, balancing)
• “Avatar” profile picture Mobius Guard due to Aldrich’s link to the Mobius interface.
o This allows for making unique NPCs and random encounters while only having one-character model. This is genius.
• First Mobius guard encounter which he explains the “avatar profile picture sprite”
• Burnt Mobius Guard NPC (“Haider Frederic”)
o Believes in Christianity, born in 2045, on Sixtus-occupied Arabian States (SAS).
 Arab states occupied until early 2060s.
o Random conversations, first ever conversation prioritized (Paradox key)
 Conversation: “God will exist. The chance of God exists will always be greater than it doesn’t exist.”
o Wrapped up in bandages
o Located in level 4 (random encounters, intermezzo)
• Liberal Bot” and “Conservative Bot”
o Random political quotes in funny C# code.
o You can access in level 1 (laptop, random encounters).

---
## [knative-automation/kn-plugin-source-kafka](https://github.com/knative-automation/kn-plugin-source-kafka)@[99928a8922...](https://github.com/knative-automation/kn-plugin-source-kafka/commit/99928a8922add361e326579b19086f422db7ed74)
#### Monday 2023-07-10 03:41:34 by Knative Automation

upgrade to latest dependencies

bumping k8s.io/apimachinery 4fbe8e4...b207ce5:%0A  > b207ce5 Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > 917de35 Bump runc go module v1.1.4 -> v1.1.6%0A  > 53ecdf0 Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 05339fa Update golang.org/x/net to v0.7.0%0A  > eabbfd5 Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 48b8d1f Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 373a5f7 Merge pull request # 114521 from 3point2/automated-cherry-pick-of-# 113283-upstream-release-1.26%0A  > b5e5df6 Fix SPDY proxy authentication with special chars%0A  > 553a2d6 Improve error message when proxy connection fails%0A  > 5d4cdd2 Merge remote-tracking branch 'origin/master' into release-1.26%0A  > 6cbc4a3 Update golang.org/x/net 1e63c2f%0A  > 6561235 Merge pull request # 113699 from liggitt/manjusaka/fix-107415%0A  > dad8cd8 Update workload selector validation%0A  > fe82462 Add extra value validation for matchExpression field in LabelSelector%0A  > 067949d update k8s.io/utils to fix util tracing panic%0A  > 0ceff90 Merge pull request # 112223 from astraw99/fix-ownerRef-validate%0A  > 9e85d3a Merge pull request # 112649 from howardjohn/set/optimize-everything-nothing%0A  > b0dd9ec Fix ownerRef controller validate err%0A  > b03a432 Merge pull request # 113367 from pohly/dep-ginkgo-gomega%0A  > 88a1448 Rename and comment on why sharing is safe%0A  > 4e6bcdb dependencies: update to gomega v1.23.0 and ginkgo v2.4.0 and dependencies%0A  > 3adc870 Optimize `Everything` and `Nothing` label selectors%0A  > 0524d6c Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > 5a0277f Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > 6809593 Merge pull request # 112377 from weilaaa/refactor_sets_use_generic%0A  > 70a38aa Merge pull request # 113106 from pohly/dep-ginkgo-gomega%0A  > f2d9aed refactor sets use generic%0A  > d097f82 dependencies: update to gomega v1.22.1 and ginkgo v2.3.1%0A  > 7b5633b Merge pull request # 112988 from alexzielenski/update-kube-openapi%0A  > b839e82 Merge pull request # 113037 from pacoxu/fsnotify-v1.6.0%0A  > b7d8973 update kube-openapi%0A  > 1dc6ace update fsnotify to v1.6.0%0A  > 78d003c Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > 04898ff Bump golang.org/x/text to v0.3.8%0A  > 79993b2 Merge pull request # 112875 from pohly/update-yaml%0A  > 7379c15 dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > 66e26ac Merge pull request # 112707 from enj/enj/i/https_links%0A  > 882b67d Use https links for k8s KEPs, issues, PRs, etc%0A  > 7fb78ee Merge pull request # 112472 from ialidzhikov/nit/error-msg%0A  > 826a74e Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 22fe889 Improve the error returned from the `LabelSelectorAsSelector` func%0A  > e2f9797 Update to latest k8s.io/utils to pick up changes%0A  > f8159af Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > 612703e Merge pull request # 112352 from pohly/e2e-ginkgo-progress%0A  > 9901884 updated etcd to v3.5.5 and newer otel libraries as well%0A  > 6439059 Merge pull request # 112526 from liggitt/redirect%0A  > 0564b5e e2e: bump ginkgo to v2.2.0%0A  > 2e3bf73 Limit redirect proxy handling to redirected responses%0A  > 6d854d7 Merge pull request # 112349 from pohly/klog-update%0A  > e1e1b7c build: update to klog v2.80.1%0A  > ed93eed Merge pull request # 111768 from weilaaa/feature_add_symmetric_difference_in_sets_string%0A  > 36163c5 Merge pull request # 112193 from jindijamie/master%0A  > b7b9ba4 add symmetric difference in sets%0A  > 31bc292 Merge pull request # 112199 from pohly/klog-update%0A  > 1c318b6 Add an option for aggregator%0A  > 0d0d03e Merge pull request # 111936 from haoruan/bugfix-111928-microtime-marshal-precision%0A  > 145c075 dependencies: update to klog v2.80.0%0A  > 2d64dac Merge pull request # 112089 from zeze1004/fix-typo%0A  > 2187a78 Marshal MicroTime to json and proto at the same precision%0A  > 53c4d51 Merge pull request # 112129 from pohly/e2e-ginkgo-report-after-each%0A  > 30e9977 Fix typo "sturct" to "struct"%0A  > 5e4f25a dependencies: update to ginkgo v2.1.6 and gomega v1.20.1%0A  > 349dcdf Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 16a7f7a Bump prometheus/client_golang to v1.13.0%0A  > 2b9fe2c Merge pull request # 111808 from alvaroaleman/meta-wrapping%0A  > bb48261 Apimachinery meta errors: Support errors.Is and error wrapping%0Abumping google.golang.org/grpc 1c29e07...82c6376:%0A  > 82c6376 Change version to 1.55.0 (# 6211)%0A  > d33f68e googledirectpatph: enable ignore_resource_deletion in bootstrap (# 6243) (# 6246)%0A  > 3fc6e00 authz: Move audit package (# 6218) (# 6219)%0A  > 875c97a examples/features/observability: use observability module v1.0.0 (# 6210)%0A  > aa8c137 authz: add audit logging APIs (# 6158)%0A  > b91b884 gcp/observability: Have o11y module point to grpc 1.54 and opencensus 1.0.0 (# 6209)%0A  > eab9e20 test/kokoro: increase PSM Security test timeout to 4h (# 6193)%0A  > d90621f remove the unnecessary call to ResetTimer and StopTimer (# 6185)%0A  > fe72db9 testing: add helpers to start test service, and retrieve port (# 6187)%0A  > 5a50b97 Revert "Revert "credentials/alts: defer ALTS stream creation until handshake …" (# 6179)%0A  > 89ec960 grpc: read the service config channel once instead of twice (# 6186)%0A  > 6237dfe internal/stubserver: Close Client Conn in error handling of Start (# 6174)%0A  > 06de8f8 alts: Add retry loop when making RPC in ALTS's TestFullHandshake. (# 6183)%0A  > 6eabd7e server: use least-requests loadbalancer for workers (# 6004)%0A  > 8374ff8 Export the unwrapResource method, to allow callers outside of the package (# 6181)%0A  > efb2f45 test/xds: Fix test_grpc import path (# 6180)%0A  > 81b3092 security/advancedtls: add TlsVersionOption to select desired min/max TLS versions (# 6007)%0A  > 17b693d alts: Perform full handshake in ALTS tests. (# 6177)%0A  > 01f8b86 Add documentation on some anti-patterns (# 6034)%0A  > 3489bb7 xdsclient/test: deflake TestWatchResourceTimerCanRestartOnIgnoredADSRecvError (# 6159)%0A  > bfb57b8 testing: delete internal copy of test service proto, and use canonical one (# 6164)%0A  > 10401b9 stats/opencensus: the backend to Sent. Attempt. and Recv. (# 6173)%0A  > b0a8b1b Use string instead of enum for xds resource type (# 6163)%0A  > 1d5b73a xds: add stop to avoid hanging in TestServeWithStop (# 6172)%0A  > ea0a038 xds/xdsclient: ignore resource deletion as per gRFC A53 (# 6035)%0A  > a51779d xdsclient/test: deflake TestTimerAndWatchStateOnSendCallback (# 6169)%0A  > e979919 internal/grpcsync: move CallbackSerializer from xdsclient/internal to here (# 6153)%0A  > c2899dd examples/features/observability: Point o11y example to latest gcp/observability module (# 6162)%0A  > 113d75f gcp/observability: Add isSampled bool to log entries (# 6160)%0A  > 4a12595 stats/opencensus: Switch helper to return Span Context from context (# 6156)%0A  > c3f1d5e gcp/observability: Set the opencensus_task label only for metrics, not tracing and logging (# 6155)%0A  > 42dd7ac Use anypb.New instead of ptypes.MarshalAny (# 6074)%0A  > 415ccdf go.mod: update all dependencies after 1.54 branch cut (# 6132)%0A  > a357baf status: FromError: return entire error message text for wrapped errors (# 6150)%0A  > 44cebb8 xds: enable XDS federation by default (# 6151)%0A  > c018273 examples: Add observability example (# 6149)%0A  > 277bb64 Revert "credentials/alts: defer ALTS stream creation until handshake time (# 6077)" (# 6148)%0A  > 0fdfd40 gcp/observability: Generate unique process identifier unconditionally (# 6144)%0A  > 1d20f1b security/advancedtls: swap from deprecated pkix.CertificateList to x509.RevocationList (# 6054)%0A  > a8a25ce transport: use prefix logging (# 6135)%0A  > 9c25653 cdsbalancer: improve log messages (# 6134)%0A  > a02aae6 CONTRIBUTING.md: remove duplicated bullet point (# 6139)%0A  > cdab8ae clusterresolver: push empty config to child policy upon removal of cluster resource (# 6125)%0A  > 7651e62 transport: add a draining state check before creating streams (# 6142)%0A  > a2ca46c examples: organize READMEs better (# 6121)%0A  > 4efec30 stats/opencensus: remove leading slash for per call metrics (# 6141)%0A  > 78099db gcp/observability: Switch hex encoding to string() method (# 6138)%0A  > 70c5291 observability: remove import replace directive and switch it to point to latest commit (# 6122)%0A  > 66e3533 status: handle wrapped errors (# 6031)%0A  > a75fd73 Change version to 1.55.0-dev (# 6131)%0A  > b638faf stats/opencensus: Add message prefix to metrics names (# 6126)%0A  > c84a500 credentials/alts: defer ALTS stream creation until handshake time (# 6077)%0A  > 6f44ae8 metadata: add benchmark test for FromIncomingContext and ValueFromIncomingContext (# 6117)%0A  > a1e657c client: log last error on subchannel connectivity change (# 6109)%0A  > 36fd0a4 gcp/observability: Add compressed metrics to observability module and synchronize View data with exporter (# 6105)%0A  > 52ca957 xds: make comparison of server configs in bootstrap more reliable (# 6112)%0A  > 7507ea6 gcp/observability: Change logging schema and set queue size limit for logs and batching delay (# 6118)%0A  > 16c3b7d examples: add example for ORCA load reporting (# 6114)%0A  > b458a4f transport: stop always closing connections when loopy returns (# 6110)%0A  > 11e2506 tests: Scale down keepalive test timings (# 6088)%0A  > 5796c40 interop/observability: Pass interop parameters to client/server as-is (# 6111)%0A  > abd4db2 xdsclient/tests: fix flaky test NodeProtoSentOnlyInFirstRequest (# 6108)%0A  > 3633361 tests: support LRS on the same port as ADS (# 6102)%0A  > 0558239 Update CONTRIBUTING.md (# 6089)%0A  > 2260821 go.mod: upgrade golang.org/x/net to address CVE-2022-41723 (# 6106)%0A  > 60a1aa3 testutils: add support for creating endpoint resources with options (# 6103)%0A  > 92d9e77 xds: NACK route configuration if sum of weights of weighted clusters exceeds uint32_max (# 6085)%0A  > d02039b Deflake the integration test. (# 6093)%0A  > 55d8783 gcp/observability: Link logs and traces by logging Trace and Span IDs (# 6056)%0A  > ad4057f transport: stop returning errors that are always nil (# 6098)%0A  > 558e1b6 examples/authz: add token package docstring (# 6095)%0A  > 33df9fc credentials/xds: improve error message upon SAN matching failure (# 6080)%0A  > 3292193 xdsclient: handle race with watch timer handling (# 6086)%0A  > e83e34b xds/resolver/test: use a non-blocking send instead of closing the channel (# 6082)%0A  > b46bdef interop/observability: add GCP Observability Testing Client/Server (# 5979)%0A  > f311684 stats/opencensus: New uncompressed metrics and align with tracing spec (# 6051)%0A  > cc320bf grpc: Log server trailers before writing status (# 6076)%0A  > b9e6d59 xdsclient: send Node proto only on first discovery request on ADS stream (# 6078)%0A  > ae4a231 ringhash: ensure addresses are consistenly hashed across updates (# 6066)%0A  > 52dcd14 xdsclient: move tests from `e2e_test` to `tests` directory (# 6073)%0A  > d8f80bb stats/opencensus: Added client api latency and upgrade go.mod (# 6042)%0A  > a8b3226 gcp/observability: Disable logging and traces on channels to cloud ops backends (# 6022)%0A  > 20141c2 examples: add an example to illustrate authorization (authz) support (# 5920)%0A  > 8c374f7 clusterresolver: cleanup resource resolver implementation (# 6052)%0A  > 1d16ef5 metadata: Lowercase appended metadata (# 6071)%0A  > 8ba23be cmd/protoc-gen-go-grpc: bump -version to 1.3.0 for release (# 6064)%0A  > a1693ec fakeserver: remove ADS and LRS v2 support (# 6068)%0A  > 832ecc2 channelz: use protocmp.Transform() to compare protos (# 6065)%0A  > 28b6bcf xds/xdsclient: improve failure mode behavior (gRFC A57) (# 5996)%0A  > d53f0ec test: move compressor tests out of end2end_test.go (# 6063)%0A  > dba41ef metadata: fix validation issues (# 6001)%0A  > 75bed1d test: move e2e health checking tests out of end2end_test.go (# 6062)%0A  > 0586c51 internal/transport: reduce running time of test from 5s to 1s (# 6061)%0A  > 7437662 internal/transport: Fix flaky keep alive test (# 6059)%0A  > 681b133 admin/test: split channelz imports (# 6058)%0A  > 1093d3a channelz: remove dependency on testing package (# 6050)%0A  > 3775f63 xdsclient/transport: reduce chattiness of logs (# 5992)%0A  > 6fe609d xdsclient: minor cleanup in eds parsing (# 6055)%0A  > 5353eaa testing: add helpers to configure cluster specifier plugin type (# 5977)%0A  > 8702a2e stats/opencensus: Add top level call span (# 6030)%0A  > 85b95dc gcp/observability: Register new views (# 6026)%0A  > abff344 stats/opencensus: Add per call latency metric (# 6017)%0A  > 0f02ca5 gcp/observability: Switch observability module to use new opencensus instrumentation code (# 6021)%0A  > 6d612a3 resolver: update Resolver.Scheme() docstring to mention requirement of lowercase scheme names (# 6014)%0A  > 30d8c0a xds/internal/xdsclient: NACK empty clusters in aggregate clusters (# 6023)%0A  > 081499f xds: remove support for v2 Transport API (# 6013)%0A  > dd12def stats/opencensus: Add OpenCensus traces support (# 5978)%0A  > f4feddb github: update tests to use go version 1.20 (# 6020)%0A  > 8153410 client: Add dial option to disable global dial options (# 6016)%0A  > 55dfae6 resolver: document handling UpdateState errors by resolvers (# 6002)%0A  > ceb3f07 client: Revert dialWithGlobalOption (# 6012)%0A  > d655f40 internal/transport: fix severity of log when receiving a GOAWAY with error code ENHANCE_YOUR_CALM (# 5935)%0A  > b81e8b6 metadata: slightly improve operateHeaders (# 6008)%0A  > e9d9bd0 tests: reduce the degree of stress testing in long running tests (# 6003)%0A  > f855226 github: update codeQL action to v2 (# 6009)%0A  > f69e9ad stats/opencensus: Add OpenCensus metrics support (# 5923)%0A  > 3151e83 cmd/protoc-gen-go-grpc: export consts for full method names (# 5886)%0A  > d6dabba xds/server: reduce chattiness of logs (# 5995)%0A  > 0954097 server: expose API to set send compressor (# 5744)%0A  > a7058f7 xds/csds: switch tests to use the new generic xdsclient API (# 6000)%0A  > 3711154 xdsclient/bootstrap: reduce chattiness of logs (# 5991)%0A  > d103fc7 xdsclient/xdsresource: reduce chattiness of logs (# 5993)%0A  > 6a707eb client: add an option to disable global dial options (# 5990)%0A  > c813c17 Change version to 1.54.0-dev (# 5985)%0A  > 2a1e934 server: after GracefulStop, ensure connections are closed when final RPC completes (# 5968)%0A  > e2d69aa tests: fix spelling of variable (# 5966)%0A  > a6376c9 xds/resolver: cleanup tests to use real xDS client 3/n (# 5953)%0A  > bf8fc46 xds/resolver: cleanup tests to use real xDS client 5/n (# 5955)%0A  > 3930549 resolver: replace resolver.Target.Endpoint field with Endpoint() method (# 5852)%0A  > 894816c grpclb: rename `grpclbstate` package back to `state` (# 5962)%0A  > e5a0237 encoding: fix duplicate compressor names (# 5958)%0A  > 4adb2a7 xds/resolver: cleanup tests to use real xDS client 2/n (# 5952)%0A  > 52a8392 gcp/observability: update method name validation (# 5951)%0A  > 4075ef0 xds: fix panic involving double close of channel in xDS transport (# 5959)%0A  > 7bf6a58 gcp/observability: Cleanup resources allocated if start errors (# 5960)%0A  > bc9728f xds/resolver: cleanup tests to use real xDS client 4/n (# 5954)%0A  > 6e74938 xds/resolver: cleanup tests to use real xDS client (# 5950)%0A  > 9b9b381 server: fix a few issues where grpc server uses RST_STREAM for non-HTTP/2 errors (# 5893)%0A  > ace8082 xdsclient: close func refactor (# 5926)%0A  > 9326362 transport: fix maxStreamID to align with http2 spec (# 5948)%0A  > 4e4d828 xds interop: Fix buildscripts not continuing on a failed test suite (# 5937)%0A  > 379a2f6 *: add missing colon to errorf messages to improve readability (# 5911)%0A  > cde2edc Revert "xds interop: Fix buildscripts not continuing on a failed test suite (# 5932)" (# 5936)%0A  > 78ddc05 xdsclient: fix race in load report implementation (# 5927)%0A  > 2a9e970 xds interop: Fix buildscripts not continuing on a failed test suite (# 5932)%0A  > 9228cff rls: fix a data race involving the LRU cache (# 5925)%0A  > be06d52 binarylog: consistently rename imports for binarylog proto (# 5931)%0A  > bf3ad35 *: update all dependencies (# 5924)%0A  > 6de8f50 transport: drain client transport when streamID approaches maxStreamID (# 5889)%0A  > 42b7b63 stats/opencensus: OpenCensus instrumentation api (# 5919)%0A  > 974a5ef grpc: document defaults in MaxCallMsgSize functions (# 5916)%0A  > 9b73c42 test/xds: add tests for scenarios where authority in resource name is not specified in bootstrap config (# 5890)%0A  > 3b2da53 xdsclient: handle resource not found errors correctly (# 5912)%0A  > f2fbb0e Deprecate use of `ioutil` package (# 5906)%0A  > 8ec85e4 priority: improve and reduce verbosity of logs (# 5902)%0A  > 12b8fb5 test: move e2e HTTP header tests to http_header_end2end_test.go (# 5901)%0A  > f1a9ef9 stream: update ServerStream.SendMsg doc (# 5894)%0A  > c90744f oauth: mark `NewOauthAccess` as deprecated and update examples to use `TokenSource` (# 5882)%0A  > 0e5421c internal/envconfig: add convenience boolFromEnv to improve readability (# 5887)%0A  > 4565dd7 ringhash: allow overriding max ringhash size via environment variable (# 5884)%0A  > 94a65dc rls: deflake tests (# 5877)%0A  > 08479c5 xdsclient: resource agnostic API implementation (# 5776)%0A  > 07ac97c transport: simplify httpClient by moving onGoAway func to onClose (# 5885)%0A  > 5ff7dfc rls: propagate headers received in RLS response to backends (# 5883)%0A  > f94594d interop: add test client for use in xDS federation e2e tests (# 5878)%0A  > 68b388b balancer: support injection of per-call metadata from LB policies (# 5853)%0A  > 4f16fbe examples: update server reflection tutorial (# 5824)%0A  > b2d4d5d test: fix raceyness check to deflake test http server (# 5866)%0A  > 54b7d03 grpc: Add join Dial Option (# 5861)%0A  > 70617b1 vet & github: run vet separately from tests; make vet-proto only check protos (# 5873)%0A  > 81ad1b5 *: update all dependencies (# 5874)%0A  > 357d7af Change version to 1.53.0-dev (# 5872)%0A  > a0e8eb9 test: rename race.go to race_test.go (# 5869)%0A  > ae86ff4 benchmark: fix typo in ClientReadBufferSize feature name (# 5867)%0A  > e53d28f xdsclient: log node ID with verbosity INFO (# 5860)%0A  > 9373e5c transport: Fix closing a closed channel panic in handlePing (# 5854)%0A  > 2f413c4 transport/http2: use HTTP 400 for bad requests instead of 500 (# 5804)%0A  > 5003029 testutils: do a better job of verifying pick_first in tests (# 5850)%0A  > 3e27f89 binarylog: Account for key in metadata truncation (# 5851)%0A  > f54bba9 test/xds: minor cleanup in xDS e2e test (# 5843)%0A  > a9709c3 Added logs for reasons causing connection and transport close (# 5840)%0A  > aba03e1 xds: pass options by value to helper routines which setup the management server in tests (# 5833)%0A  > 638141f examples: add feature/cancellation retry to example test script (# 5846)%0A  > 22c1fd2 deps: update golang.org/x/net to latest in all modules (# 5847)%0A  > 1949035 ringhash: add logs to surface information about ring creation (# 5832)%0A  > f7c110a test: remove use of deprecated WithInsecure() API (# 5836)%0A  > a205447 examples: add new example to show updating metadata in interceptors (# 5788)%0A  > 001d234 rls: Fix regex in rls test (# 5834)%0A  > 7361971 rls: use a regex for the expected error string (# 5827)%0A  > 617d6c8 security/advancedtls: add test for crl cache expiration behavior (# 5749)%0A  > ef51864 grpclb: improve grpclb tests (# 5826)%0A  > fa99649 xdsclient: deflake new transport ack/nack tests (# 5830)%0A  > 99ba982 transport/server: flush GOAWAY before closing conn due to max age (# 5821)%0A  > 20c937e transport: limit AccountCheck tests to fewer streams and iterations to avoid flakes (# 5828)%0A  > 110ed9e xdsclient: resource-type-agnostic transport layer (# 5808)%0A  > c91396d pickfirst: do not return initial subconn while connecting (# 5825)%0A  > 94f0e7f benchmark: add a feature for read and write buffer sizes (# 5774)%0A  > 087387c Deflake Outlier Detection xDS e2e test (# 5819)%0A  > dd123b7 testutils/pickfirst: move helper function to testutils (# 5822)%0A  > be202a2 examples: add an example to illustrate the usage of stats handler (# 5657)%0A  > 9f97673 test: move e2e goaway tests to goaway_test.go (# 5820)%0A  > 0fe49e8 grpc: Improve documentation of read/write buffer size server and dial options (# 5800)%0A  > 09fc1a3 interop: update Go version in docker container used for psm interop (# 5811)%0A  > adfb915 server: fix ChainUnaryInterceptor and ChainStreamInterceptor to allow retrying handlers (# 5666)%0A  > e0a9f11 reflection: split grpc and pb imports (# 5810)%0A  > 6f96f96 reflection: update proto (# 5809)%0A  > 6e43203 reflection: generate protobuf files from grpc-proto (# 5799)%0A  > 0abb6f9 xdsclient: resource type agnostic WatchResource() API (# 5777)%0A  > 3011eaf test/tools: update staticcheck version to latest (# 5806)%0A  > fefb3ec test/tools: update everything to latest versions except staticcheck (# 5805)%0A  > 50be6ae go.mod: update all dependencies (# 5803)%0A  > ff14680 Cap min and max ring size to 4K (# 5801)%0A  > 0238b6e transport: new stream with actual server name (# 5748)%0A  > 817c1e8 passthrough: return error if endpoint is empty and opt.Dialer is nil when building resolver (# 5732)%0A  > 56ac86f xdsclient: wait for underlying transport to close (# 5775)%0A  > 457c2f5 benchmark: use default buffer sizes (# 5762)%0A  > 689d061 Cleanup usages of resolver.Target's Scheme and Authority (# 5761)%0A  > 5331dbd outlierdetection: remove an unused variable in a test (# 5778)%0A  > 81db250 Change version to 1.52.0-dev (# 5784)%0A  > 72812fe gcp/observability: filter logging from cloud ops endpoints calls (# 5765)%0A  > 0ae33e6 xdsclient: remove unused test code (# 5772)%0A  > 824f449 go.mod: upgrade x/text to v0.4 to address CVE (# 5769)%0A  > 7f23df0 xdsclient: switch xdsclient watch deadlock test to e2e style (# 5697)%0A  > 32f969e o11y: Added started rpc metric in o11y plugin (# 5768)%0A  > b597a8e xdsclient: improve authority watchers test (# 5700)%0A  > e41e894 orca: create ORCA producer for LB policies to use to receive OOB load reports (# 5669)%0A  > 36d14db Fix binary logging bug which logs a server header on a trailers only response (# 5763)%0A  > fcb8bdf xds/google-c2p: validate url for no authorities (# 5756)%0A  > 040b795 xdsclient/e2e_test: use SendContext() where appropriate (# 5729)%0A  > 0d6481f target: replace parsedTarget.Scheme to parsedTarget.URL.Scheme (# 5750)%0A  > fdcc01b transport/test: implement staticcheck suggestion (# 5752)%0A  > aa44cca google-c2p: use new-style resource name for LDS subscription (# 5743)%0A  > c858a77 balancer/weightedtarget: fix ConnStateEvltr to ignore transition from TF to Connecting (# 5747)%0A  > 64df652 google-c2p: include federation env var in the logic which determines when to use directpath (# 5745)%0A  > 3c09650 balancer/weightedtarget: use ConnectivityStateEvaluator (# 5734)%0A  > 3fd80b0 Fix flaky test MultipleClientStatsHandler (# 5739)%0A  > 26071c2 google-c2p resolver: add authority entry to bootstrap config (# 5680)%0A  > 9127159 client: synchronously verify server preface in newClientTransport (# 5731)%0A  > f51d212 xdsclient: improve RDS watchers test (# 5692)%0A  > 7c16802 tests: refactor tests to use testutils helper functions (# 5728)%0A  > 28fae96 xdsclient: improve federation watchers test (# 5696)%0A  > f88cc65 xdsclient: improve EDS watchers test (# 5694)%0A  > 439221d xdsclient: add a convenience type to synchronize execution of callbacks (# 5702)%0A  > dbb8e2b xdsclient: improve CDS watchers test (# 5693)%0A  > 79ccdd8 clientconn: go idle if conn closed after preface received (# 5714)%0A  > 778860e testing: update Go to 1.19 (# 5717)%0A  > eb8aa31 weightedtarget: return a more meaningful error when no child policy is reporting READY (# 5391)%0A  > bb3d739 fakeserver: add v3 support to the xDS fakeserver implementation (# 5698)%0A  > 912765f xds: move bootstrap config generating utility package to testutils (# 5713)%0A  > f52b910 o11y: Fixed o11y bug (# 5720)%0A  > 00d1830 Fix o11y typo (# 5719)%0A  > e163a90 xds/xdsclient: add EDS resource endpoint address duplication check (# 5715)%0A  > 9eba574 xds: de-experimentalize google c2p resolver (# 5707)%0A  > 8b3b10b gcp/observability: implement public preview config syntax, logging schema, and exposed metrics (# 5704)%0A  > 8062981 vet: workaround buggy mac git grep behavior (# 5716)%0A  > e81d0a2 xdsclient: improve LDS watchers test (# 5691)%0A  > 7b817b4 client: set grpc-accept-encoding to full list of registered compressors (# 5541)%0A  > c672451 xds/xdsclient: add sum of EDS locality weights check (# 5703)%0A  > c03925d priority: release references to child policies which are removed (# 5682)%0A  > 5fc798b Add binary logger option for client and server (# 5675)%0A  > 12db695 grpc: restrict status codes from control plane (gRFC A54) (# 5653)%0A  > 202d355 Change version to 1.51.0-dev (# 5687)%0A  > 1451c62 internal/transport: optimize grpc-message encoding/decoding (# 5654)%0A  > be4b63b test: minor test cleanup (# 5679)%0A  > d83070e Changed Outlier Detection Env Var to default true (# 5673)%0A  > 54521b2 client: remove trailing null from unix abstract socket address (# 5678)%0A  > 36e4810 orca: cleanup old code, and get grpc package to use new code (# 5627)%0A  > e8866a8 build: harden GitHub Workflow permissions (# 5660)%0A  > 8458251 xdsclient: ignore routes with cluster_specifier_plugin when GRPC_EXPERIMENTAL_XDS_RLS_LB is off (# 5670)%0A  > a238ceb xDS: Outlier Detection Env Var not hardcoded to false (# 5664)%0A  > b1d7f56 transport: Fix deadlock in transport caused by GOAWAY race with new stream creation (# 5652)%0A  > 9c3e589 rls: delegate pick to child policy as long as it is not in TransientFailure (# 5656)%0A  > 7da8a05 xds: Enable Outlier Detection interop tests (# 5632)%0A  > 21f0259 test: loosen metadata error check to reduce dependence on exact library errors (# 5650)%0A  > 552de12 orca: fix package used to reference service to use pb suffix instead of grpc (# 5647)%0A  > 87d1a90 orca: fix package used to reference service to use grpc suffix instead of pb (# 5645)%0A  > 60eecd9 metadata: add ValueFromIncomingContext to more efficiently retrieve a single value (# 5596)%0A  > 2ebd594 Documentation/proxy: update due to Go 1.16 behavior change (# 5630)%0A  > 1530d3b gcp/observability: fix End() to cleanup global state correctly (# 5623)%0A  > f7d2036 xds: add Outlier Detection Balancer (# 5435)%0A  > 182e9df Grab comment from proto file, similar to protoc-gen-go (# 5540)%0A  > 60a3a7e cleanup: fixes for issues surfaced by vet (# 5617)%0A  > 99ae81b roundrobin: optimization of the roundrobin implementation. (# 5607)%0A  > aee9f0e orca: server side custom metrics implementation (# 5531)%0A  > ddcda5f alts: do not set WaitForReady on handshaker RPCs (# 5620)%0A  > d875a0e xdsclient: NACK cluster resource if config_source_specifier in lrs_server is not self (# 5613)%0A  > c351f37 chore: remove duplicate word in comments (# 5616)%0A  > f0f9f00 test/kokoro: enable pod log collection in the buildscripts (# 5608)%0A  > 1dd0256 ringhash: implement a no-op ExitIdle() method (# 5614)%0A  > fe59226 clusterresolver: deflake eds_impl tests (# 5562)%0A  > d5dee5f xds/ringhash: make reconnection logic work for a single subConn (# 5601)%0A  > b225dda transport: update http2 spec document link (# 5597)%0A  > 641dc87 transport: add peer information to http2Server and http2Client context (# 5589)%0A  > 02fbca0 xds/resolver: generate channel ID randomly (# 5591)%0A  > 97cb7b1 xds/clusterresolver: prevent deadlock of concurrent Close and UpdateState calls (# 5588)%0A  > c56f196 internal/fakegrpclb: don't listen on all adapters (# 5592)%0A  > 3f5b7ab internal/transport: fix typo (# 5566)%0A  > c11858e Publish arm64 binaries to GitHub releases (# 5561)%0A  > 802b32e Change version to 1.50.0-dev (# 5585)%0Abumping github.com/prometheus/client_golang 64435fc...254e546:%0A  > 254e546 Merge pull request # 1162 from kakkoyun/cut-1.14.0%0A  > 07d3a81 Merge pull request # 1161 from prometheus/release-1.13%0A  > c8a3d32 Cut v1.14.0%0A  > 870469e Test and support 1.19 (# 1160)%0A  > 53e51c4 Merge pull request # 1157 from prometheus/cut-1.13.1%0A  > b785d0c Fix go_collector_latest_test Fail on go1.19 (# 1136)%0A  > 79ca0eb Added tip from Björn + Grammarly.%0A  > 4d54769 Fix float64 comparison test failure on archs using FMA (# 1133)%0A  > 078f11f Cut 1.13.1 release (+ documenting release process).%0A  > 5f202ee Merge pull request # 1150 from prometheus/sparsehistogram%0A  > ddd7f0e Fix race condition with Exemplar in Counter (# 1146)%0A  > 0859bb8 Merge pull request # 1152 from jessicalins/update-to-custom-reg%0A  > fffb76c Merge branch 'main' into sparsehistogram%0A  > 1f93f64 Fix `CumulativeCount` value of `+Inf` bucket created from exemplar (# 1148)%0A  > 10b0550 Fix race condition with Exemplar in Counter (# 1146)%0A  > a340ca4 Run make format%0A  > e92a8c7 Avoid the term 'sparse' where possible%0A  > 8cc2b6c Fix double-counting bug in promhttp.InstrumentRoundTripperCounter (# 1118)%0A  > dcea97e Fix `CumulativeCount` value of `+Inf` bucket created from exemplar (# 1148)%0A  > 6056615 Update random example to use custom registry%0A  > d31f13b Add SparseBucketsZeroThresholdZero and groom doc comments%0A  > 9801a4e Examples: Replace deprecated WithGoCollections with WithGoCollectorRuntimeMetrics (# 1130)%0A  > 0b7f488 Update simple example to use custom registry%0A  > 58a8ca4 examples: Adjust doc comment for native histograms%0A  > 7c46c15 Clarify documentation around what constructors do (# 1125)%0A  > 9b5c5b8 Update basic example to use custom registry%0A  > 4e71e6f Update prometheus/client_model dependency%0A  > 83d56b1 Extend prometheus.Registry to implement Collector (# 1103)%0A  > 111fae1 Merge branch 'main' into sparsehistogram%0A  > 4c41dfb Clarify exemplar(Add|Observe) by renaming to (add|observe)WithExemplar (# 1122)%0A  > 25bc188 Merge pull request # 1144 from prometheus/beorn7/histogram2%0A  > f73e3cc Fix double-counting bug in promhttp.InstrumentRoundTripperCounter (# 1118)%0A  > 95cf173 Merge branch 'main' into sparsehistogram%0A  > 6942f9e sparse buckets: Fix handling of +Inf/-Inf/NaN observations%0A  > c7aa2a5 Merge pull request # 1113 from prometheus/release-1.13%0A  > ec86ef1 Merge pull request # 1092 from prometheus/beorn7/histogram%0A  > 1e61b8e Update common Prometheus files (# 1111)%0A  > 6141a07 Merge branch 'main' into sparsehistogram%0A  > 8cbcd40 histograms: Move to new exposition protobuf format%0A  > 5a321c7 Merge branch 'foo-commit' into sparsehistogram%0A  > e93e384 Merge branch 'beorn7/release' into sparsehistogram%0A  > e203144 Merge branch 'release-1.12' of github.com:prometheus/client_golang into release-1.12%0A  > 525d042 Merge branch 'main' into sparsehistogram%0A  > a516626 Merge branch 'release-1.12' into beorn7/release%0A  > a27b6d7 Fix conflicts%0A  > 6ba7871 Merge branch 'main' into sparsehistogram%0A  > eb59a7b Histogram: Fix bug with negative schemas (# 1054)%0A  > b237230 Merge branch 'main' into sparsehistogram%0A  > 294cca4 Merge branch 'main' into sparsehistogram%0A  > 70253f4 Fix typo in doc comment%0A  > 5b19c55 Merge branch 'master' into sparsehistogram%0A  > dfbcc28 Merge pull request # 901 from prometheus/beorn7/histogram%0A  > 84fcaff Merge branch 'master' into sparsehistogram%0A  > 263be8d Refactoring of sparse histograms%0A  > 9ef5f90 Allow a zero threshold of zero%0A  > 2409960 Implement strategy to limit the sparse bucket count%0A  > aa6f67a Add TODO about bucket search optimization%0A  > 43f31c2 Merge pull request # 886 from prometheus/beorn7/histogram%0A  > 5aa8534 Merge branch 'master' into sparsehistogram%0A  > 5142344 Pin client_model to the most recent sparsehistogram commit%0A  > 97eb041 Tidy go.sum%0A  > 6c4e0ef Add tests for sparse histogram%0A  > 553ed73 Fix lint warning%0A  > 31318b7 Switch to base-2 buckets%0A  > b7a540a Fix test%0A  > a9df0ba Update prometheus/client_model%0A  > ce36ee3 Merge branch 'master' into beorn7/histogram%0A  > d698336 Merge branch 'master' into beorn7/histogram%0A  > 08104a0 Minor doc comment fixes%0A  > a9d0066 Add note about pow-of-10 precision issue%0A  > d1f5366 Fix span offset%0A  > abe540f Encode sparse histograms in protobuf%0A  > c98db4e Demo sparse histograms%0Abumping knative.dev/eventing 034bec9...8f74094:%0A  > 8f74094 Add handler to auto create Event Types (# 7034)%0A  > 901ef61 Remove check for empty Namespace on resolver (# 7040)%0A  > 95cdbaa We should not limit the EventType creation from the Sources Duck to just brokers (# 7032)%0A  > 7429761 Adjust the Namespace reference to the one from the parent (# 7035)%0A  > cb2a891 update the redeployment script (# 7038)%0A  > ab01938 [main] Upgrade to latest dependencies (# 7025)%0A  > c9dcaf3 Added basic gc loop to kncloudevents clients map (# 6997)%0A  > d6cf96d EventType works with channel (# 7023)%0A  > 365d0b0 Run TLS e2e tests only when Istio is not enabled (# 7029)%0A  > 825a237 Update IMC CRD addressstatus to include `.name` and `.CACerts` fields (# 7026)%0A  > 3190df7 Tracking/reconcile KResource references (# 7014)%0A  > 0f68861 Rename more to Resource, instead of broker (# 7022)%0A  > bccb7d4 Better reflecting the lifecycle of event type … (# 7019)%0A  > 49d4acd Skip ping source TLS rekt test, since extremely flaky (# 7016)%0A  > 8719e18 [main] Upgrade to latest dependencies (# 7012)%0A  > e5ae717 Use HTTP POST when terminating istio proxy (# 7015)%0A  > fea730f Only check if the reference does exist (# 7010)%0A  > 631f4ec Add TLS support for mt-broker-filter (# 6940)%0A  > 45f0a19 Allow wathola components to run with Istio  (# 7011)%0A  > 65f4b1c [main] Format Go code (# 7008)%0A  > 3267b1a test SinkBinding with eventshub TLS receiver as sink (# 6979)%0A  > aad53f4 Updated eventingtls test certs to support IP addresses (# 7006)%0A  > 57d78e0 [main] Update community files (# 7004)%0A  > dfb2243 Support TLS in Trigger and Channel reconciler (# 6988)%0A  > df08b49 Eventing TLS: verify APIServerSource and PingSource sinkURI is https (# 6987)%0A  > d21c1aa [main] Upgrade to latest dependencies (# 6989)%0A  > 70113e8 Deprecate broker field and use KReference for the broker instead (# 6870)%0A  > 4e4647f test update to newest version (# 6990)%0A  > 870ac6b Update MessageDispatcher and FanoutMessageHandler to support sending events to TLS endpoints (# 6983)%0A  > 6dd5d58 Test PingSource with eventshub TLS receiver as sink (# 6965)%0A  > 55f4f28 [main] Upgrade to latest dependencies (# 6982)%0A  > 2a5a9a5 Add more items in the development getting started documentation (# 6978)%0A  > 59118a0 imc-dispatcher starts a TLS server, accepts host based routing on http receiver and path based routing on https receiver (# 6954)%0A  > ee49ada Rework kncloudevents library to support multiple clients (# 6975)%0A  > ee88094 Make ServerManager independent from kncloudevents package (# 6980)%0A  > 6a11c5f [main] Upgrade to latest dependencies (# 6969)%0A  > 8a9a532 Updated DEVELOPMENT.md to provide better instructions on setting up kubernetes (# 6977)%0A  > 390a0c8 Eventing TLS: Test ContainerSource with eventshub TLS receiver as sink (# 6957)%0A  > 5e245ac Fix flaky PingSource TLS unit test (# 6970)%0A  > f9f27c9 Use random names in Channel tests (# 6967)%0A  > d4609a5 Do not parse flags in InitializeEventingFlags (# 6966)%0A  > ef68a0a [main] Update community files (# 6968)%0A  > 4adc287 Add transport-encryption prerequisite for Addressable tests (# 6964)%0A  > deb0ef4 Add field for subscribers & replys CA certs to `SubscriberSpec` and `SubscriptionStatusPhysicalSubscription` (# 6959)%0A  > b81082c Eventing TLS: Test ApiServerSource with eventshub TLS receiver as sink (# 6956)%0A  > cdff269 Adding source duck type to v1b2 (# 6962)%0A  > b47b4ec [main] Upgrade to latest dependencies (# 6958)%0A  > 3315c20 Provide Channels CACerts in Brokers status annotation (# 6952)%0A  > 4b9fdef [main] Upgrade to latest dependencies (# 6955)%0A  > da31970 Improve cert-manager resources for Eventing TLS certs provisioning (# 6953)%0A  > fc5befb Provide subscribers CACerts in triggers status (# 6951)%0A  > 1efab19 Using v1b2 in the reconciler (# 6949)%0A  > c44671c Updating rekt test resources for EventType v1b2 (# 6946)%0A  > e31eb1f Adding testingv1b2 for eventtype (# 6944)%0A  > a9908ef Support TLS in PingSource (# 6929)%0A  > df559c0 Fix typo in flags.IsDisbledTransportEncryption name (# 6941)%0A  > 7073cc9 [main] Upgrade to latest dependencies (# 6939)%0A  > c6bc9bb Eventing TLS: Support K_CA_CERTS env variable injection for SinkBinding subjects (# 6931)%0A  > 24fbfe5 Eventing TLS: support exposing https address in Broker controller (# 6930)%0A  > d18cb42 Add information about retryable error in servermanager (# 6921)%0A  > f92a05b Added Support for K_CA_CERTS in the heartbeats (# 6920)%0A  > b8b43d0 Remove CA certs empty and non nil check, use URL scheme only (# 6928)%0A  > 3c8cc05 Return error directly if one receiver of servermanager fails (# 6919)%0A  > 92ab7f8 [main] Upgrade to latest dependencies (# 6927)%0A  > 5c6fe57 two more for reducing to debug, instead of info (# 6922)%0A  > 6cf9397 less verbose logs on scheduler component  (# 6912)%0A  > 69918f2 Adds ServerManager. Supports http/https message receivers (# 6908)%0A  > d58e259 Install ko using setup-ko in kind e2e tests (# 6910)%0A  > 9cdea5d Eventing TLS: Added Support for setting K_CA_CERTS in the ApiServerSource controller for the adapter (# 6897)%0A  > add8436 Eventing TLS: support exposing https address in InMemoryChannel controller (# 6881)%0A  > 59cfb6d [main] Upgrade to latest dependencies (# 6906)%0A  > 03f2a3d Remove unused test helper (# 6907)%0A  > 7a90c46 Remove eventing-natss from downstream tests (# 6905)%0A  > ba2550b [main] Upgrade to latest dependencies (# 6904)%0A  > 999eead More EventType v1beta2 work (# 6903)%0A  > 66e8257 Remove sanitize HTTP body for `knativeerrordata` extension (# 6902)%0A  > cd50d27 [main] Format Go code (# 6898)%0A  > 0f0a82c [main] Update community files (# 6901)%0A  > 7f4deb5 EventType v1b2 API addition (# 6893)%0A  > 1f917d0 Refactor PingSource adapter client creation (# 6880)%0A  > e2f1c77 [main] Update community files (# 6896)%0A  > 6a5c7ee Eventing TLS: migrate all resolver.URIResolver usages over to AddressableFromDestinationV1 (# 6883)%0A  > 0a12a6c Adds path based routing to message_receiver pkg (# 6873)%0Abumping knative.dev/eventing-kafka 9a4a93a...d047934:%0A  > d047934 Update community files (# 1357)%0A  > d4716b7 upgrade to latest dependencies (# 1355)%0A  > 9ca5fa0 Update community files (# 1354)%0A  > 90a8ba9 upgrade to latest dependencies (# 1353)%0A  > 561d00f upgrade to latest dependencies (# 1352)%0A  > 22b1fff upgrade to latest dependencies (# 1351)%0A  > 77507bf upgrade to latest dependencies (# 1349)%0A  > 6d6530f Update community files (# 1348)%0A  > a6f4f44 upgrade to latest dependencies (# 1344)%0A  > 2558e87 Update community files (# 1346)%0A  > 86dda64 Update dependencies and fix compile issues (# 1345)%0A  > d9a13fc upgrade to latest dependencies (# 1342)%0A  > a3ee5d5 Update community files (# 1343)%0A  > 9c2c601 upgrade to latest dependencies (# 1340)%0A  > 0b7e0ac upgrade to latest dependencies (# 1339)%0A  > 62d8873 upgrade to latest dependencies (# 1338)%0A  > 870d89a Update community files (# 1337)%0Abumping golang.org/x/sys 90c8f94...ca59eda:%0A  > ca59eda windows: use unsafe.Add instead of pointer arithmetic on a uintptr%0A  > 6c52899 windows: return error if DecomposeCommandLine parameter contains NUL%0A  > 9524d49 windows/svc/mgr: Service.Control: populate Status when returning certain errors%0A  > 2a33a30 execabs: let hasExec return false on wasip1%0A  > 39c2d6a unix: add UDP socket option constants on linux%0A  > 1fb6828 unix: convert Iovec.Base to *byte in mkpost.go on solaris%0A  > 3125361 unix: allow overriding GOOS using GOOS_TARGET in mkpost.go%0A  > dbd8f99 windows: add Service.ListDependentServices%0A  > f25ff60 windows: add JobObjectInformationClass consts for QueryInformationJobObject%0A  > 64840c1 unix: add bindings for setattrlist() on macOS%0A  > 90abad3 unix: add AT_EACCESS on Darwin%0A  > 94933fc windows: fix constant values for JobObjectInformationClass%0A  > 00d8004 unix: match ioctl req argument type to libc type%0A  > d0781cc unix: make solaris syscall tests less flaky%0A  > ff18efa unix: change Setrlimit/Prlimit to always call syscall functions%0A  > 494aa49 unix: skip ip related tests if EAFNOSUPPORT raised%0A  > c7a1bf9 unix: define PerfBitWriteBackward%0A  > 1470852 unix: add SetsockoptTCPMD5Sig on linux%0A  > a6bfb89 unix: use unsafe.Slice in anyToSockaddr%0A  > c10701f windows: use unsafe.Slice in (*RawSockaddrAny).Sockaddr on windows%0A  > 6f25076 unix: define extended TCPInfo on Linux%0A  > 10499f4 unix: add ioctlPtr with unsafe.Pointer arg on other unices (cont)%0A  > 92c4c39 unix: add Dup3 on FreeBSD%0A  > 748af6e unix: pass PROT_MPROTECT(PROT_READ|PROT_WRITE) to initial Mmap on netbsd%0A  > 972870e unix/linux: update to Linux kernel 6.2, glibc 2.37 and Go 1.20.1%0A  > cc0b67d unix: use C.ioctl in generated ioctlPtr%0A  > a3b23cc unix: use SYS_PTRACE in generated ptracePtr%0A  > 71a906e unix/linux: add TUN flags and virtio_net_hdr constants%0A  > 2977c77 unix: add ptracePtr that accepts pointer arg as unsafe.Pointer%0A  > 6877dcc execabs: don't override Go 1.19 error with our error%0A  > b13f40e unix: add ioctlPtr with unsafe.Pointer arg on other unices%0A  > 3b9b58b unix: Faccess: check CAP_DAC_OVERRIDE on Linux%0A  > 2da1413 cpu: get hwcap/auxv from the Go 1.21+ runtime%0A  > 4fee21c windows: Add WSALookupService syscall wrappers%0A  > c79a742 unix: fix a use-after-free bug in PtraceIO on freebsd%0Abumping knative.dev/hack f591fea...cc92cdb:%0A  > cc92cdb Replace test-infra with toolbox (# 297)%0A  > fc42790 Update community files (# 296)%0A  > d7586a2 Update e2e kntest link (# 295)%0A  > a861c8e Update community files (# 294)%0A  > 5b7907f Update actions (# 289)%0A  > c133d5d Install Istio for tests (# 291)%0A  > 5812c57 Update community files (# 292)%0A  > 7d81248 Update community files (# 286)%0A  > 6e4569c Update community files (# 285)%0Abumping google.golang.org/api a039966...63d06ab:%0A  > 63d06ab chore(main): release 0.124.0 (# 1990)%0A  > 73f57fe feat(all): auto-regenerate discovery clients (# 1991)%0A  > 8c0e6d9 chore: add yoshi-approver ownership (# 1994)%0A  > 7843046 chore(all): update all (# 1992)%0A  > 94c12ed chore(all): update module github.com/google/s2a-go to v0.1.4 (# 1989)%0A  > 0b4f4af feat(all): auto-regenerate discovery clients (# 1988)%0A  > 2721e1f chore: enable GoApiaryCodegen auto-approve (# 1987)%0A  > a241c25 chore: delete broken AutoApprove (# 1986)%0A  > 3e2d6a6 chore: trigger AutoApprove on reopen as well (# 1985)%0A  > a24a28a chore: give AutoApprove job full write (# 1984)%0A  > 8210800 chore(main): release 0.123.0 (# 1975)%0A  > f31b763 feat(all): auto-regenerate discovery clients (# 1982)%0A  > d27f40f feat(all): auto-regenerate discovery clients (# 1978)%0A  > 94d3d73 chore(ci): fix AutoApprove for discogen (# 1981)%0A  > 98b3073 feat(all): auto-regenerate discovery clients (# 1974)%0A  > d5e0fb2 chore(main): release 0.122.0 (# 1972)%0A  > ab64815 feat(all): auto-regenerate discovery clients (# 1973)%0A  > 8b0974e fix: add better support of array of floats (# 1971)%0A  > cf0df64 chore(main): release 0.121.0 (# 1962)%0A  > c2c2b59 feat(all): auto-regenerate discovery clients (# 1963)%0A  > e44a771 chore(all): update module github.com/google/s2a-go to v0.1.3 (# 1965)%0A  > 2068ba5 feat(all): auto-regenerate discovery clients (# 1961)%0A  > c2018e2 chore(main): release 0.120.0 (# 1956)%0A  > 4e35cac feat(all): auto-regenerate discovery clients (# 1960)%0A  > fcd007a feat(all): auto-regenerate discovery clients (# 1958)%0A  > 289b859 feat(all): auto-regenerate discovery clients (# 1957)%0A  > 409bc9d feat(all): auto-regenerate discovery clients (# 1955)%0A  > 0909f16 chore(main): release 0.119.0 (# 1944)%0A  > 2f54150 chore(deps): update s2a-go to v0.1.2 (# 1954)%0A  > 685ec81 feat: add an option to enable DirectPath xDS (# 1942)%0A  > d85769c feat(all): auto-regenerate discovery clients (# 1953)%0A  > 4cb8eb9 feat(all): auto-regenerate discovery clients (# 1952)%0A  > bf9f3ac chore(all): update google.golang.org/genproto digest to daa745c (# 1949)%0A  > e1eda57 feat(all): auto-regenerate discovery clients (# 1948)%0A  > a0dacd5 feat(all): auto-regenerate discovery clients (# 1947)%0A  > e8b93cb chore(deps): update s2a-go to v0.1.1 (# 1945)%0A  > 690068f feat(all): auto-regenerate discovery clients (# 1943)%0A  > 2d6890a chore(main): release 0.118.0 (# 1940)%0A  > 29dc45a feat(all): auto-regenerate discovery clients (# 1941)%0A  > ac94a0f feat(all): auto-regenerate discovery clients (# 1939)%0A  > 8019ef6 chore(main): release 0.117.0 (# 1931)%0A  > 750c7c8 feat(all): auto-regenerate discovery clients (# 1936)%0A  > 3a98290 chore(all): update all (# 1937)%0A  > 3f62830 chore(deps): bump golang.org/x/crypto (# 1930)%0A  > 2219681 feat(all): auto-regenerate discovery clients (# 1935)%0A  > 2efcb2e feat(all): auto-regenerate discovery clients (# 1932)%0A  > 3c61729 feat: add experimental s2a-go integration (# 1874)%0A  > 587b9e5 chore(main): release 0.116.0 (# 1929)%0A  > 28c8cd5 feat(all): auto-regenerate discovery clients (# 1928)%0A  > feafcdc chore(main): release 0.115.0 (# 1922)%0A  > 34781cf feat(all): auto-regenerate discovery clients (# 1927)%0A  > 33a2dfe feat(all): auto-regenerate discovery clients (# 1924)%0A  > 02cfb82 chore(all): update google.golang.org/genproto digest to dcfb400 (# 1925)%0A  > 8930f0e feat(all): auto-regenerate discovery clients (# 1923)%0A  > 1c955e8 feat(all): auto-regenerate discovery clients (# 1913)%0A  > 7f87838 chore(all): update all (# 1918)%0A  > be028cf chore(gensupport): add idempotency header (# 1916)%0A  > 649bfb9 chore(all): update all (# 1914)%0A  > 5ac4fd7 test: update test due to generator change (# 1912)%0A  > f79df48 chore(main): release 0.114.0 (# 1910)%0A  > 2754ab4 feat(all): auto-regenerate discovery clients (# 1907)%0A  > dc4b77d fix: always reference the internal package. (# 1909)%0A  > b8a2a5e chore(main): release 0.113.0 (# 1901)%0A  > fc221ce feat(all): auto-regenerate discovery clients (# 1900)%0A  > e63383f chore(all): update module google.golang.org/protobuf to v1.29.1 [SECURITY] (# 1906)%0A  > 64b6ee4 feat(idtoken): add support for external_account (# 1897)%0A  > 65cafd4 chore(all): update all (# 1902)%0A  > 63c48a6 feat(transport): add support for setting quota project with envvar (# 1892)%0A  > 225fa6b internal: Refactor cert logic to support OAuth2 token exchange over mTLS (# 1886)%0A  > 8d4d70d chore(main): release 0.112.0 (# 1883)%0A  > 89c274a feat(all): auto-regenerate discovery clients (# 1898)%0A  > 9f18671 feat(all): auto-regenerate discovery clients (# 1896)%0A  > e88ee8a feat(all): auto-regenerate discovery clients (# 1893)%0A  > 5da4d6a feat(all): auto-regenerate discovery clients (# 1887)%0A  > 6bd0840 chore(deps): bump golang.org/x/crypto in /internal/kokoro/discogen (# 1890)%0A  > 2f72016 chore(all): update all (# 1888)%0A  > c886360 feat(all): auto-regenerate discovery clients (# 1885)%0A  > 1aee5cd feat(all): auto-regenerate discovery clients (# 1884)%0A  > 15808d7 feat(all): auto-regenerate discovery clients (# 1882)%0A  > e99d0d5 chore(main): release 0.111.0 (# 1860)%0A  > 70d3954 feat(all): auto-regenerate discovery clients (# 1875)%0A  > f32872c chore(all): update google.golang.org/genproto digest to 637eb22 (# 1877)%0A  > c02cff6 feat(all): auto-regenerate discovery clients (# 1873)%0A  > 7d34d41 feat(all): auto-regenerate discovery clients (# 1872)%0A  > d456fd6 chore(deps): bump golang.org/x/net in /internal/kokoro/discogen (# 1870)%0A  > b7ab21d chore(all): update all (# 1868)%0A  > 7f5f40a feat(all): auto-regenerate discovery clients (# 1866)%0A  > 4056319 chore(all): update module golang.org/x/net to v0.7.0 [SECURITY] (# 1867)%0A  > 8b8b195 feat(all): auto-regenerate discovery clients (# 1863)%0A  > c0f2510 chore(all): update vet.sh to go runtime 1.20 (# 1865)%0A  > 895105a feat(all): auto-regenerate discovery clients (# 1861)%0A  > ba3414e feat(all): auto-regenerate discovery clients (# 1859)%0A  > 892811c chore(main): release 0.110.0 (# 1840)%0A  > 1edc79b chore: update x libs (# 1858)%0A  > 929a393 chore(all): update all (# 1853)%0A  > 1147cb8 fix: Update ECP dependency to v0.2.3 (# 1857)%0A  > 689f934 feat(all): auto-regenerate discovery clients (# 1851)%0A  > 8efd00d fix(internal/gensupport): don't prematurely close timers (# 1856)%0A  > 3fb5b61 fix: Improve error handling for enterprise certificate module (# 1848)%0A  > 8980266 feat(all): auto-regenerate discovery clients (# 1850)%0A  > 3fb8cdc feat(all): auto-regenerate discovery clients (# 1841)%0A  > 1651c38 chore(transport): remove support for go runtimes earlier than 1.16 (# 1844)%0A  > 4b4c9d4 feat(all): auto-regenerate discovery clients (# 1838)%0A  > b3b5f17 chore(main): release 0.109.0 (# 1818)%0A  > c13cc35 feat(all): auto-regenerate discovery clients (# 1836)%0A  > 602b6a4 chore(all): update all (major) (# 1806)%0A  > a5d0daa feat(all): auto-regenerate discovery clients (# 1828)%0A  > 50fc7c4 feat(all): auto-regenerate discovery clients (# 1826)%0A  > 6aad438 feat(all): auto-regenerate discovery clients (# 1825)%0A  > 85d0224 feat(all): auto-regenerate discovery clients (# 1822)%0A  > 884a246 feat(all): auto-regenerate discovery clients (# 1821)%0A  > 5935892 feat(all): auto-regenerate discovery clients (# 1819)%0A  > ba3ba78 feat(all): auto-regenerate discovery clients (# 1817)%0A  > 47f66d6 chore(main): release 0.108.0 (# 1811)%0A  > da48b9a feat(all): auto-regenerate discovery clients (# 1816)%0A  > a12685c feat(all): auto-regenerate discovery clients (# 1813)%0A  > 4df52d2 feat(all): auto-regenerate discovery clients (# 1810)%0A  > f74fbb6 chore(main): release 0.107.0 (# 1803)%0A  > d8084e4 feat(all): auto-regenerate discovery clients (# 1809)%0A  > 4dca4e0 feat: re-enable integrations:v1 (# 1801)%0A  > 86e4009 fix: user Timers over time.After (# 1802)%0A  > bcc345c feat(all): auto-regenerate discovery clients (# 1808)%0A  > de06921 feat(all): auto-regenerate discovery clients (# 1807)%0A  > 935ef64 feat(all): auto-regenerate discovery clients (# 1804)%0A  > 93de455 feat(all): auto-regenerate discovery clients (# 1800)%0A  > ac7eb8f chore(main): release 0.106.0 (# 1786)%0A  > 3944e86 feat(all): auto-regenerate discovery clients (# 1794)%0A  > f6dec99 feat(idtoken): add support for impersonated_service_account creds type (# 1792)%0A  > ddb5c65 test: add buffer to both sides of token expiry validation (# 1797)%0A  > b35900a fix(idtoken): configure validator constructor to use no authentication (# 1789)%0A  > ca86833 chore(all): update all (# 1796)%0A  > a6b0739 chore: skip generating integrations:v1 as it fails generation (# 1793)%0A  > 7bd17b3 feat(all): auto-regenerate discovery clients (# 1790)%0A  > 9fb35f5 feat(all): auto-regenerate discovery clients (# 1788)%0A  > 1569e5b feat(option/internaloption): add new EmbeddableAdapter option (# 1787)%0A  > a7f08e2 feat(all): auto-regenerate discovery clients (# 1784)%0A  > 67aaf4e chore(main): release 0.105.0 (# 1774)%0A  > 5b02761 feat(all): auto-regenerate discovery clients (# 1777)%0A  > c58bf4c feat: support set null map entries for non-simple map values (# 1782)%0A  > e4271df feat(googleapi): add response headers to Error reported by CheckMediaResponse (# 1781)%0A  > 6193507 chore: remove uses of obsolete golang.org/x/xerrors (# 1776)%0A  > 37a2e41 feat(all): auto-regenerate discovery clients (# 1773)%0A  > 9255b0b chore(main): release 0.104.0 (# 1748)%0A  > 4238314 chore: ignore some golang.org/x/* dependencies in renovate (# 1772)%0A  > 029b659 chore(all): update all (# 1768)%0A  > f819644 feat(all): auto-regenerate discovery clients (# 1771)%0A  > 2b596d9 feat(all): auto-regenerate discovery clients (# 1767)%0A  > 3195ce1 feat(all): auto-regenerate discovery clients (# 1766)%0A  > 97a9846 feat(all): auto-regenerate discovery clients (# 1760)%0A  > 8d8f0a7 feat(transport): de-experiment google-c2p resolver (# 1757)%0A  > c213153 fix(transport/grpc): separate resolution of creds and certs (# 1759)%0A  > 629e217 fix(idtoken): increase MaxIdleConnsPerHost to 100 in NewClient (# 1754)%0A  > caf7af0 feat(all): auto-regenerate discovery clients (# 1755)%0A  > e18b504 feat(all): auto-regenerate discovery clients (# 1753)%0A  > dd565a4 feat(all): auto-regenerate discovery clients (# 1752)%0A  > a657f19 feat(all): auto-regenerate discovery clients (# 1751)%0A  > 292129c feat(all): auto-regenerate discovery clients (# 1746)%0A  > 02077fd chore(all): update all (# 1749)%0A  > 567070f docs: document limitation of WithUserAgent (# 1747)%0A  > 561b601 chore(main): release 0.103.0 (# 1738)%0A  > 4248dc3 feat(all): auto-regenerate discovery clients (# 1743)%0A  > ee25e29 feat(googleapi): inject gax apierror.APIError into googleapi.Error (# 1730)%0A  > f8efb95 chore(all): update all (# 1740)%0A  > 9695aa1 feat: rm hard dep on x/sys (# 1742)%0A  > bec0f29 chore(.github): force renovate to use 1.19 (# 1741)%0A  > bbd4259 feat(all): auto-regenerate discovery clients (# 1739)%0A  > de99200 feat(all): auto-regenerate discovery clients (# 1737)%0A  > 0d7f97a chore(main): release 0.102.0 (# 1726)%0A  > 0528475 feat: rely on new compute metadata module directly (# 1736)%0A  > ce57a67 feat(all): auto-regenerate discovery clients (# 1734)%0A  > 1e1eab9 feat(all): auto-regenerate discovery clients (# 1727)%0A  > 0ce5403 test(transport/grpc): fix arg for test failure logs (# 1733)%0A  > 06360d8 feat(all): auto-regenerate discovery clients (# 1725)%0A  > 644a13c chore(main): release 0.101.0 (# 1719)%0A  > f4788b3 feat(all): auto-regenerate discovery clients (# 1723)%0A  > 9ea2ceb chore(all): update all (# 1721)%0A  > 9140608 feat(all): auto-regenerate discovery clients (# 1720)%0A  > 453b81a feat(all): auto-regenerate discovery clients (# 1718)%0A  > d530a93 chore(main): release 0.100.0 (# 1714)%0A  > 37f90e9 feat(internal/gensupport): remove DetermineContentType, use gax-go copy (# 1716)%0A  > b235b1f fix(idtoken): Allow missing age in http response header (# 1715)%0A  > f990a2a feat(all): auto-regenerate discovery clients (# 1717)%0A  > f9e15f2 feat(all): auto-regenerate discovery clients (# 1712)%0A  > e74b770 chore(all): update all (# 1713)%0A  > 977e871 chore(main): release 0.99.0 (# 1710)%0A  > 6b81c83 feat(all): auto-regenerate discovery clients (# 1701)%0A  > 1aa1deb chore(all): update all (# 1707)%0A  > 69fb474 chore: Update ECP dependency to 0.2.0 (# 1704)%0A  > a4ae94d chore(main): release 0.98.0 (# 1700)%0A  > 25b7450 feat(all): auto-regenerate discovery clients (# 1699)%0A  > aa775b4 feat(all): auto-regenerate discovery clients (# 1696)%0A  > faa845a chore(main): release 0.97.0 (# 1694)%0A  > 2c3e863 fix(gensupport): allow initial request for resumable uploads to retry w/ non-nil getBody (# 1690)%0A  > f427ee3 feat(internal/gensupport): wrap retry failures with context and prev error (# 1684)%0A  > 6b0515b fix: build script bash error (# 1697)%0A  > b8f2556 feat(all): auto-regenerate discovery clients (# 1695)%0A  > a87400b feat(all): auto-regenerate discovery clients (# 1693)%0Abumping golang.org/x/text 71a9c9a...48e4a4a:%0A  > 48e4a4a all: fix some comments%0A  > 9db913a go.mod: update to newer x/tools%0A  > 30dadde all: correct comment typos%0Abumping github.com/prometheus/client_model 7bc5445...63fb982:%0A  > 63fb982 Merge pull request # 63 from prometheus/sparsehistogram%0A  > 5c16fa2 Merge pull request # 57 from prometheus/repo_sync%0A  > fdb567d Add note about native histograms to README%0A  > 6b8c742 Update common Prometheus files%0A  > 942d53c Update common Prometheus files%0A  > 7f720d2 Add note about experimental state of native histograms%0A  > f60d1ac Update common Prometheus files%0A  > 1f8dcad Merge pull request # 59 from prometheus/beorn7/histogram%0A  > 6dc836e Merge pull request # 53 from prometheus/repo_sync%0A  > 421ad2b Merge pull request # 58 from prometheus/beorn7/histogram%0A  > a7ff713 Flatten the buckets of native histograms%0A  > 0e1ed89 Merge pull request # 52 from prometheus/repo_sync%0A  > a227486 Update common Prometheus files%0A  > 408689d Merge branch 'master' into sparsehistogram%0A  > 0da3265 Explain Span layout better%0A  > 14ab895 Merge pull request # 51 from prometheus/repo_sync%0A  > bc75c6a Update common Prometheus files%0A  > 61b6c1a Merge pull request # 47 from prometheus/beorn7/histogram%0A  > 8171e83 Add float histograms and gauge histograms to proto spec%0A  > a863571 Merge pull request # 49 from prometheus/repo_sync%0A  > 2fc368c Update common Prometheus files%0A  > 8831f0d Merge branch 'master' into sparsehistogram%0A  > bbaf1cc Switch to base 2 and powers of 2 for resolution%0A  > 675c4e5 Merge pull request # 48 from prometheus/repo_sync%0A  > a3e6551 Update common Prometheus files%0A  > 24db95a Merge remote-tracking branch 'origin/master' into beorn7/histogram%0A  > 147c58e Move .proto file and add caching of protoc and protoc-gen-go during build (# 46)%0A  > 56ab8d9 Update common Prometheus files%0A  > 4b803f3 Experimental encoding for sparse buckets in histogram%0A  > 0255a22 Merge pull request # 43 from roidelapluie/security-dot-md%0A  > 1f48c5c Rename metrics.proto to io_prometheus_client_metrics.proto (# 45)%0A  > 60555c9 Merge pull request # 41 from prometheus/repo_sync%0A  > 1bb3080 Add SECURITY.md%0A  > 1106810 Update common Prometheus files%0Abumping knative.dev/pkg dfad48e...5ef4812:%0A  > 5ef4812 Update community files (# 2762)%0A  > 49e2e56 update google cloud deps (# 2758)%0A  > a5e0b92 upgrade to latest dependencies (# 2757)%0A  > 6eb4b40 Update community files (# 2760)%0A  > eb63a40 Support to set qps and burst via env variable (# 2755)%0A  > 74c4be5 Generate kresource duck type codegen (# 2754)%0A  > 4dbc312 fix boilerplate (# 2753)%0A  > 15605c7 Defaulting Controller options for all kind of webhooks (# 2738)%0A  > 94b81fc Update community files (# 2752)%0A  > 5671699 drop the dynamic type (# 2750)%0A  > 9bda38b Fix some webhook testing tech debt (# 2751)%0A  > ec20442 Update community files (# 2747)%0A  > 05bfcf6 bump k8s dependencies and update min version to v1.25 (# 2745)%0A  > 52ff2ac drop dynamic client wrappers (# 2744)%0A  > a170a07 Eventing TLS: validate that Destination.CACerts is a PEM encoded cert (# 2743)%0A  > dfb4bf0 Drop dynamic wrapper injection code generation (# 2742)%0A  > db8a353 Add SinkCACerts to SourceStatus (# 2733)%0A  > 9049667 Update community files (# 2735)%0A  > aacec7f Update community files (# 2734)%0A  > 300df43 Eventing TLS: Added AddressableFromDestination method on the resolver (# 2717)%0Abumping golang.org/x/net 8e2b117...daac0ce:%0A  > daac0ce go.mod: update golang.org/x dependencies%0A  > 82780d6 http2: don't reuse connections that are experiencing errors%0A  > 0bfab66 ipv4, ipv6: drop redundant skip checks based on GOOS%0A  > 938ff15 ipv4, ipv6, nettest: skip unsupported tests on wasip1%0A  > eb1572c html: another shot at security doc%0A  > 9001ca7 nettest: re-enable unixpacket tests on netbsd/386%0A  > 3d5a8ee internal/socks: permit authenticating with an empty password%0A  > 694cff8 go.mod: update golang.org/x dependencies%0A  > 6960703 http2: log the correct error when retrying in (*Transport).RoundTripOpt%0A  > 9f24bb4 http2: properly discard data received after request/response body is closed%0A  > 08dda57 html: fix package doc typo%0A  > dfa2b5d go.mod: update golang.org/x dependencies%0A  > 8c4ef2f hmtl: add security section to package comment%0A  > 1d46ed8 html: have Render escape comments less often%0A  > 569fe81 html: add "Microsoft Outlook comment" tests%0Abumping github.com/fsnotify/fsnotify 0f4b979...5f8c606:%0A  > 5f8c606 Update ChangeLog%0A  > 8878587 Tweak the docs a bit%0A  > 89b4cf1 Add test for re-adding a renamed file (# 508)%0A  > 85acde2 Update x/sys%0A  > 69c24b0 Update x/sys%0A  > fb07f82 Add test to see what happens if you watch a symlink (# 498)%0A  > 666da9c Clarify doc comment on WatchList() (# 499)%0A  > 123e4e3 Add note about README version%0A  > 61a05ce Update documentation and examples (# 496)%0A  > e180a87 Move some inotify-tests to run on all backends; test that state is cleaned up after Remove (# 494)%0A  > fdf41a3 Move some files around%0A  > 844d71f Port minor test changes from fen-v2 branch; make LICENSE text not ugly%0A  > 5b87f50 windows: simplify a bit (# 493)%0A  > 2bfaa00 all: add Watcher.{sendEvent,sendError} (# 492)%0A  > 8ab3b84 kqueue: don't set up watchers on unreadable files (# 479)%0A  > a4bcdf8 Update changelog%0A  > 4b43fad kqueue: remove timeout from unix.Kevent() (# 480)%0A  > a24f78c windows: test symlinks (# 491)%0A  > f45391f windows: run TestWatchRename/rename_overwriting_existing_file (# 490)%0A  > ee33a65 Use "os.Rename()" in tests instead of "mv"%0A  > 9dd0568 cmd/fsnotify: fix time.Format() string%0A  > 5dcbfba windows: replace syscall with golang.org/x/sys/windows%0A  > 1f8edaf windows: replace "e" with "err" for error variables%0A  > 99715ba windows: increase buffer size from 4K to 64K (# 485)%0A  > a5c5815 ci: update to use Go 1.19, kick off fewer builds, update x/sys (# 484)%0A  > f2d35c3 Remove CLA section in contributing%0A  > 4604469 Need Linux 5.9 for a useful fanotify we can use%0A  > a566bb1 Update CONTRIBUTING.md%0A  > 01dfc6f Remove PULL_REQUEST_TEMPLATE%0A  > a58e868 Run tests in illumos (# 481)%0A  > 666c6a0 Update ChangeLog%0A  > 928895c [bugfix] close handle when remWatch open in getIno (# 288)%0A  > f174f95 windows: update watch paths when renaming directories with sub-watches (# 370)%0A  > 87dc1fa Rewrite tests (# 478)%0A  > 57e6a49 Add {Event,Op}.Has() (# 477)%0A  > 39823aa Document that /proc and /sys won't work%0A  > 60fbf57 Clarify FAQ on goroutines%0A  > ca0e2f4 macos: retry if open() returns EINTR (# 475)%0A  > ff39bb4 Fix lint (# 476)%0A  > 421f529 debian 6 test: deal with multiple packages (# 474)%0A  > a3256ef Remove AUTHORS file%0A  > 0e78fa6 Update README: split out FAQ to "Platform-specific notes"%0A  > 1a7b6ef inotify: don't ignore events for files that don't exist (# 470)%0A  > f0aceb2 Tweak comment regarding relative paths (# 466)%0A  > d9c9fa5 Add cmd/fsnotify (# 463)%0A  > cc15908 kqueue: better error if watching a file fails (# 471)%0A  > c4e64e4 Replace Use of Kthread-blocking Epoll with Poller Read, Remove Per-Event LStats on Linux # 433 (# 434)%0A  > 4b8b298 Test some more things in CI (# 469)%0A  > 548b8fb Add missing changelog for 1.4.{8,9} (# 468)%0A  > 7fe2936 inotify: fix race in Close() (# 465)%0A  > 35b6378 Clarify README on network drives (# 467)%0A  > e56409e Update link to CONTRIBUTING in the README (# 464)%0A  > 4678dfd Update documentation for linux systems (max_user_watches) (# 287)%0A  > 808f582 bump up GitHub Actions (# 461)%0A  > 4193dfd Do not suppress Chmod on non-existent file (# 260)%0A  > 6ae56b7 kqueue: Make watcher.Close() O(n) instead of O(n^2) (# 233)%0A  > adf5320 strings.Builder instead of bytes.Buffer (# 285)%0A  > 217e78e Explicit mutext (un)locking (# 462)%0A  > 1a4f949 Use common error when removing an unwatched file (# 460)%0A  > 5acfdc1 windows: protect access to isClosed with mutex (# 454)%0A  > c56cafd Test Go 1.18%0A  > 37badf6 This project is archived (# 459)%0Abumping knative.dev/client-pkg 4f052f9...f377f06:%0A  > f377f06 Update community files (# 106)%0A  > b93ceb0 Update community files (# 105)%0A  > 83c91f4 Update community files (# 103)%0A  > e5c405e Update community files (# 102)%0A  > eee9b55 Update community files (# 100)%0Abumping github.com/matttproud/golang_protobuf_extensions c182aff...c182aff:%0Abumping golang.org/x/oauth2 e48dfd9...839de22:%0A  > 839de22 google: don't check for IsNotExist for well-known file%0A  > 0690208 go.mod: update golang.org/x dependencies%0A  > 451d5d6 internal: remove repeated definite articles%0A  > cfe200d oauth2: parse RFC 6749 error response%0A  > 3607514 go.mod: update golang.org/x dependencies%0A  > 4abfd87 google: add CredentialsParams.EarlyTokenRefresh%0A  > 1e7f329 oauth2: add ReuseTokenSourceWithExpiry%0A  > 86850e0 oauth2: fix typo%0A  > a6e37e7 google: Updating 3pi documentation%0A  > 54b70c8 google: update missing auth help URL%0A  > 2fc4ef5 README: encourage issues and proposals before changes%0A  > 62b4eed go.mod: update golang.org/x dependencies%0A  > 885f294 google: Add support for OAuth2 token exchange over mTLS%0A  > 6f9c1a1 google: use Credentials instead of deprecated DefaultCredentials%0A  > c82d0e1 google/internal/externalaccount: Removed URL validation for google URLs in ADC files%0A  > adbaf66 go.mod: update golang.org/x dependencies%0A  > e07593a oauth2: remove direct dependency on golang.org/x/net%0A  > 34ffb07 go.mod: update golang.org/x dependencies%0A  > b177c21 go.mod: update golang.org/x dependencies%0A  > 510acbc google/internal/externalaccount: Added check for aws region and security credential environment variables before aws metadata call%0A  > ec4a9b2 google/internal/extern…

---
## [jinuthomas/openpower-vpd-parser](https://github.com/jinuthomas/openpower-vpd-parser)@[debdafffff...](https://github.com/jinuthomas/openpower-vpd-parser/commit/debdafffff07b02f18488daffbc5a026187396a4)
#### Monday 2023-07-10 03:55:20 by jinuthomas

Catching File Exceptions in openpower-vpd-parser

In this commit, I have added code to handle file exceptions
more effectively. By implementing proper exception handling,
we can improve the robustness and reliability of the file
operations within our codebase.

Here are the key changes made in this commit:

  - Introduced a try-catch block around the file operation sections.
  - Within the try block, added code to perform the necessary file
    operations.
  - Implemented catch blocks to handle specific file exceptions.
  - In each catch block, included appropriate error handling logic,
    such as logging the error message or displaying a user-friendly
    error message.
  - Ensured that the catch blocks gracefully handle the exceptions
    and prevent the program from crashing or behaving unexpectedly.

By adding this exception handling code, we can anticipate and handle
potential file-related errors gracefully, providing a smoother
experience for users and preventing any unexpected crashes or data
loss. This would also aid in debugging issues.

Signed-off-by: jinuthomas <jinu.joy.thomas@in.ibm.com>

---
## [MaloTV/space-station-14-mapping](https://github.com/MaloTV/space-station-14-mapping)@[06747e0f7e...](https://github.com/MaloTV/space-station-14-mapping/commit/06747e0f7e7d04cf87e63a359a3a86b1a35442cc)
#### Monday 2023-07-10 04:44:16 by Emisse

some silly paintings and posters (#17872)

* webedit

* Update meta.json

* god is real hes here with us

* so true

* so truers rise

* worst meta.json ive seen in my life

* so true

---
## [2002jai/Sea-Born](https://github.com/2002jai/Sea-Born)@[120b69aaab...](https://github.com/2002jai/Sea-Born/commit/120b69aaabbca03667fcca7b39f55cb1eade910b)
#### Monday 2023-07-10 05:08:51 by jai chauhan

Sea Born

The "Data Science with Seaborn" GitHub repository is a comprehensive and user-friendly resource for individuals interested in data visualization using the Seaborn library in Python. With a wide range of topics covered, this repository serves as a go-to guide for both beginners and experienced data scientists.

From an introduction to Seaborn and its installation instructions to advanced visualization techniques, statistical visualization, and data exploration, each aspect of Seaborn is explored in detail. The repository also includes case studies that demonstrate practical applications of Seaborn in various domains, showcasing its versatility and real-world relevance.

Furthermore, the repository emphasizes the integration of Seaborn with other popular libraries such as Pandas, NumPy, and Scikit-learn, enabling users to seamlessly incorporate Seaborn into their existing data science workflows.

Contributions to the repository are highly encouraged, allowing users to actively participate in improving and expanding the available resources. The guidelines provided make it easy for users to contribute their own examples, case studies, and documentation enhancements.

Whether you are looking to enhance your data visualization skills or explore the power of Seaborn for insightful analysis, this repository is an invaluable asset. Dive in and unleash the potential of Seaborn in your data science projects.

---
## [orthography/tgstation](https://github.com/orthography/tgstation)@[a8e16030f8...](https://github.com/orthography/tgstation/commit/a8e16030f83911aef695ba9f28d565c41c99c3e6)
#### Monday 2023-07-10 05:51:42 by LemonInTheDark

Optimizes timer insertion by 80% (W QDEL_IN micro) (#76214)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

[Reduces timer insertion cost by
80%](https://github.com/tgstation/tgstation/commit/c9e5b285ed74e60108fddd3f6b45d6d3995c92a8)

Timer name generation involved a LOT of string shit, some in ways where
the string only existed for a moment.
This costs a good bit of time, and can be reduced with only minimal
impacts on the end product, so let's do that. Includes a compile flag to
flip it back if we ever have trouble in future.

This is about 0.1s off init, since we do a lot of timer stuff then too

[Removes STOPPABLE flag from QDEL_IN, moves it to a bespoke
macro](https://github.com/tgstation/tgstation/commit/e7a5d7f2a78fcf0dce4742ced258c9505411b202)

Its a waste most of the time, tho I would LOVE to analyze at compile
time to work out if we care
## Why It's Good For The Game

I like it when we don't spend all of our cpu time just setting the name
var on timers. that's good and not bad.
This saves time fucking everywhere. 15% off explosions, 0.1 seconds off
init, bunch of time off foam. it's just good.

Cherry picked out of #76104 since that was too cluttered (sannnnnn)

<!-- Argue for the merits of your changes and how they benefit the game,
especially if they are controversial and/or far reaching. If you can't
actually explain WHY what you are doing will improve the game, then it
probably isn't good for the game in the first place. -->

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [orthography/tgstation](https://github.com/orthography/tgstation)@[5c032cc098...](https://github.com/orthography/tgstation/commit/5c032cc098f9a1d62f9f9dee133ae7c3e4489dca)
#### Monday 2023-07-10 05:51:42 by LemonInTheDark

Adds border smoothing! (Look ma I'm upstreaming) (#76134)

## About The Pull Request

Ok so we currently have 1 (count em) border object that wants to smooth
with other border objects. That's the tram window.

It currently does this manually, via map edits, but that's kinda crappy
so lets be better.

This pr adds a new smoothing mode to handle border objects. 
Unlike other smoothing modes, it returns a bitfield of directions the
border object connects in.

I do this by memorizing a calculation of which dirs "connect" at init,
and reading out of a global list with border object direction, direction
between objects, and if it's a border object, the other object's dir.

I'm doing this primarily because it's become useful for wallening (a
spriter saw the tram thing and is doing the same thing to pod windows,
and I want to support that)

I do think it's potentially useful in other applications too tho, and I
like dehardcoding tram windows.

Also fun bonus (or maybe downside), it's nearly 0 cost because I pulled
the bitmask smoothing define into 2 subdefines, and am swapping the
handler one out to do what I want.
Oh also I got rid of a for loop in smoothing code, redundant and costs
time in list iteration

[Moves tram windows over to the new border object
smoothing](https://github.com/tgstation/tgstation/commit/114873679c94d680788edee9665fa18dba8108c0)

Also replaces some typepath chicanery with a setDir override, for
redundancy in future
Oh and there's a update paths script too, to be nice

## Why It's Good For The Game

More visual possibility in future, fixes a hack we have currently, and
makes some spriters happy.

## Changelog
:cl:
fix: Dehardcodes some stuff with tram windows, they'll be easier to map
with now
refactor: Border objects can now smooth with each other. I'm sure
something cool will come of this
/:cl:

---
## [swuff-star/Starstorm2](https://github.com/swuff-star/Starstorm2)@[445bc5609a...](https://github.com/swuff-star/Starstorm2/commit/445bc5609a01dfa643b0a9f6dfb5f7c890c9ded8)
#### Monday 2023-07-10 06:31:29 by swuff-star

last sec tweaks

[Verse 1]
Nothing, nothing
Nothing inside
And there's no reason to cry
Just fade away like love
Clutching, hanging
By a nail in this life
Desperate always
Always looks that way

[Pre-Chorus]
Free fall from the nest, then glide to the left
A shine catch the eye, so flow to the right
Flying high, realize there are no more mountains to climb

[Chorus]
When there's nothing I can do
Accept, enjoy the view
When there's nothing I can do
I smile

[Verse 2]
Minutes, seconds
And so little time
Give your secrets away?
Well, whisper in my ear
Every living thing will die
From the king of the jungle to butterfly
The only sin is waiting too long
See Queens of the Stone Age Live
Get tickets as low as $40
You might also like
Time & Place
Queens of the Stone Age
Negative Space
Queens of the Stone Age
Straight Jacket Fitting
Queens of the Stone Age
[Chorus]
When there's nothing I can do
I smile
I smile
Wide
Ooh

[Bridge]
Free fall from the nest, then glide to the left
A shine catch the eye, so flow to the right
Flying high, realize there are no more mountains to climb

[Outro]
We live, we die
We fail, we rise
I'm a vulture, so I hear goodbyes
There's no end to life
On and on, always life
On and on, always life

---
## [lessthnthree/tgstation](https://github.com/lessthnthree/tgstation)@[4c99fb2ebb...](https://github.com/lessthnthree/tgstation/commit/4c99fb2ebb26179044c582ae6494338cb2aa35e2)
#### Monday 2023-07-10 07:04:37 by carlarctg

Coroner additions and tweaks (#76534)

## About The Pull Request

Serrated bone shovels can be created with any kind of shovel now, not
just a spade (???)

Serrated bone shovels can be used in place of circular saw in most
surgeries.

Added a duller (still deadly) variant of the serrated bone shovel as
coroner mail.

Autopsy scanners now act as advanced health analyzers on dead and
seemingly-dead people.

Increased the force, throwforce, and wound bonus of inert ritual knives
and scythes.

Coroner gloves can quickly apply medicine like nitrile gloves.
## Why It's Good For The Game

> Serrated bone shovels can be created with any kind of shovel now, not
just a spade (???)

Weird ass bug.

> Serrated bone shovels can be used in place of circular saw in most
surgeries.

It's serrated, it's cool, it's rare, it has a fast toolspeed.

> Added a duller (still deadly) variant of the serrated bone shovel as
coroner mail.

Very thematic for the coroner, should probably also be a heirloom item
but whatevs. Weaker so there's still a reason to seek out the OG.

> Autopsy scanners now act as advanced health analyzers on dead and
seemingly-dead people.

Scanning corpses is pretty important during surgery - it tells you how
much blood they have, organ damage, diseases... these things don't
appear in the surgical computer readout, which means the coroner has to
go out of his cave to pick up a boring light blue meatbag wound scanner.
This also incentivizes coroners to do their job by giving them something
cool that only works on dead bodies.

> Increased the force, throwforce, and wound bonus of inert ritual
knives and scythes.

These two options in the MortiDrobe are pretty frickin' badass,
especially with how SICK the Coroner looks with them, double especially
in combat.


![image](https://github.com/tgstation/tgstation/assets/53100513/98c6f8a5-3e5a-41a9-8a9c-cb6b82ecc0b8)

However, there's the large issue that as actual weapons they're really,
really weak. Not enough damage, when I use them in combat I both feel
badass but also get a nagging feeling in the back of my mind that I'm
intentionally gimping myself, and with only 10 damage I can *really*
feel it. I find it unfair that these are objectively worse than a
welding tool or even a Butcher's Cleaver when they're a lot more
involved to find, and scarce besides. These arguments apply equally to
the Wizard's ritual knife, and the scythe.

Additionally on the scythe, the crew really needs more good ghetto
weaponry that isn't the boring same ol' of baseball bats, spears,
cleavers... and making scythes useful is a great way to help bridge that
gap. They deal a satisfying amount of damage now, with the clear
downside, of course, being that they're bulky and hard to lug around.

> Coroner gloves can quickly apply medicine like nitrile gloves.

'Fast medicine' doesn't just cover sutures, it also covers medical gel.
Specifically, sterilizer gel. I find it annoying that the Coroner is
encouraged to give up his drip for the boring life-saver nitrile gloves,
because the difference in applying time really does make a difference -
it makes gel applying go from annoying to smooth, which is important
considering the whole purpose of sterilizer gel is to make surgeries go
faster. The Coroner has surgery and thus medical locker access to begin
with, so this isn't a balance problem, (and nitrile gloves are found by
the dozen anyways) especially with how rare the coroner gloves are.
## Changelog
:cl:
fix: Serrated bone shovels can be created with any kind of shovel now,
not just a spade (???)
add: Serrated bone shovels can be used in place of circular saw in most
surgeries.
add: Added a duller (still deadly) variant of the serrated bone shovel
as coroner mail.
add: Autopsy scanners now act as advanced health analyzers on dead and
seemingly-dead people.
add: Increased the force, throwforce, and wound bonus of inert ritual
knives and scythes.
add: Coroner gloves can quickly apply medicine like nitrile gloves.
/:cl:

---
## [lessthnthree/tgstation](https://github.com/lessthnthree/tgstation)@[721fd30837...](https://github.com/lessthnthree/tgstation/commit/721fd308378dc6ef7595c1ea4b92d679ba723188)
#### Monday 2023-07-10 07:04:37 by carlarctg

Heavily reworks and resprites first aid analyzers. (#76533)

## About The Pull Request

Heavily reworks and resprites first aid analyzers. They now display if
they're happy, sad, angry, or warning you! Also a 'pricking' animation.

First aid analyzers are now found in all basic and specialized medkits.
Toxin medkits get a new* disease analyzer. Miners get a miner-colored
one in their box.

Scanning yourself with a first aid analyzer will 'create a holo-image
with treatment instructions next to your wounds', doubling the speed of
treatment of scanned wounds!

Health analyzers now have a scanning sound, courtesy of CM.

Refactored some wound code to make treatment duration changes and
changes in the description of wounds easier.

Fixed a dummy parent feature of the health analyzer (Verbose mode)
showing up, uselessly, on the disease and first aid subtypes.

Surgical processors and slime scanners have recieved a similar resprite.
## Why It's Good For The Game

> Heavily reworks and resprites first aid analyzers. They now display if
they're happy, sad, angry, or warning you! Also a 'pricking' animation.

These things have long, long needed some sprite love. Displaying emotion
will make them have a lot more 'weight' to them, same with the prick.
The old, shitty spectrometer sprites have gone directly into the
dumpster.

> First aid analyzers are now found in all basic and specialized
medkits. Toxin medkits get a new* disease analyzer. Miners get a
miner-colored one in their box.

They have also needed some gameplay love! Placing them in these kits is
not going to be a massive game-changer when they were already easily
found around the station in emergency medkits, but it will fill up that
awkward empty slot.

> Scanning yourself with a first aid analyzer will 'create a holo-image
with treatment instructions next to your wounds', doubling the speed of
treatment of scanned wounds!

The biggest gameplay-impacting change in this PR, I *sincerely* believe
this is the perfect solution to first aid analyzers being completely
redundant with eyesight. This lets you/someone else scan your wounds to
speed up treatment, with a neat in-character reason for it -
'holo-images' appearing on your body, like penlights.

This will speed up wound treatment, but I believe that is for the best,
as currently treating wounds is so slow that half the time it's not
worth it (or more accurately, it doesn't feel worth it in comparison to
the effort you're putting in) and you're better off shrugging off minor
wounds. It will do so in a way that requires a modicum of effort, so
it's not just a flat buff across the land.

> Health analyzers and gene scanners now have a scanning sound, courtesy
of CM.

It's a neat sound that will make medbay feel more alive. First aid
analyzers get a beeboop instead.

> Surgical processors and slime scanners have recieved a similar
resprite.

IT'S SPRITE MANIA IN HERE
## Changelog
:cl:
Carlarc, Weird Orb
image: Heavily reworks and resprites first aid analyzers. They now
display if they're happy, sad, angry, or warning you! Also a 'pricking'
animation.
add: First aid analyzers are now found in all basic and specialized
medkits. Toxin medkits get a new* disease analyzer. Miners get a
miner-colored one in their box.
balance: Scanning yourself with a first aid analyzer will 'create a
holo-image with treatment instructions next to your wounds', doubling
the speed of treatment of scanned wounds!
sound: Health analyzers and gene scanners now have a scanning sound,
courtesy of CM.
refactor: Refactored some wound code to make treatment duration changes
and changes in the description of wounds easier.
fix: Fixed a dummy parent feature of the health analyzer (Verbose mode)
showing up, uselessly, on the disease and first aid subtypes.
image: Surgical processors and slime scanners have recieved a similar
resprite.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [lessthnthree/tgstation](https://github.com/lessthnthree/tgstation)@[a2c8cce535...](https://github.com/lessthnthree/tgstation/commit/a2c8cce5359162a8a697ce109801ec268bf0c8a5)
#### Monday 2023-07-10 07:04:37 by John Willard

Bilingual can now choose their language (#76609)

## About The Pull Request

This was one of the tradeoffs for removing other, more consistent
sources of languages, and was requested by Melbert among many others.
This does go against my wanted goal of decreasing the risk of
eavesdropping by other players through just magically knowing a
language, but it is an expensive quirk and it is in their medical
records, which makes it better than language encryption keys or silicon
just innately knowing them.

This also limits Bilingual to only roundstart languages (+Uncommon),
rather than being randomly selected from a list (that had very useless
ones like monkey, podpeople, and beachbum). This is mostly just for
modularity, I didn't want to make it look terrible code-wise and thought
this may be the optimal way to handle it.

This is also me going back on
https://github.com/tgstation/tgstation/pull/71773 - which I had closed
myself.

## Why It's Good For The Game

If we're gonna keep the Bilingual quirk, it might as well be something
players can choose the language of, it's their character and they should
be allowed to decide how their character is, and it is my fault that
this stupid compromise of "getting a random language" was made in the
first place. It never should've happened.
It now actually limits it to roundstart-only languages, so there's no
way you can spy on people who prepare in advance through becoming
podpeople, or monkeys, etc.

## Changelog

:cl:
balance: Bilingual quirk now lets you choose your language between ones
given to roundstart species.
balance: Foreigner and Bilingual are now mutually exclusive languages.
/:cl:

---
## [status-im/status-mobile](https://github.com/status-im/status-mobile)@[9ed68ee7d1...](https://github.com/status-im/status-mobile/commit/9ed68ee7d1b7d59dd8b20c2ee1ffe43bd1c37078)
#### Monday 2023-07-10 07:24:14 by Icaro Motta

Lint & fix some shadowed core Clojure(Script) vars (#16500)

It's well known that shadowing core Clojure vars can lead to unexpected bugs. In
fact, it's a common source of bugs in other languages too. In the status-mobile
repository there are, in total, 562 shadowed vars, ~500 are core vars. Excluding
the "old code" we still have 285 offenders.

In status-mobile I've already seen two bugs caused by shadowed vars, both with
the shadowed var "name". But probably other problems happened in the past, and
others will happen in the future if we don't do something about this. This PR is
also my response to my frustration trying to review PRs and checking for
shadowed vars, humans were not meant for that!

In this commit we are enabling ":shadowed-var" to lint certain (not all) core
vars as errors (not warnings). In future PRs we can gradually unshadow more
vars. For the record, name is shadowed 40 times in the new code and 130 in
total, and type is shadowed 93 times in the new code and 124 in total!

What about non-core vars, should we allow shadowing? There are ~70 non-core
shadowed vars. In my opinion, we should also lint and disallow shadowing
non-core vars, since it may cause the same kind of bugs of shadowing core vars.
But this decision can be left for another moment/issue, after we have fixed the
most prominent problem of shadowing core vars.

Which vars are unshadowed in this PR? I fixed 62 errors and unshadowed
cljs.core/iter, cljs.core/time, cljs.core/count, cljs.core/key,
clojure.core/key.

Resources:

- [clj-kondo linter: shadowed-var](https://github.com/clj-kondo/clj-kondo/blob/master/doc/linters.md#shadowed-var)

---
## [denisk176/Open-Assistant](https://github.com/denisk176/Open-Assistant)@[b9c60ed582...](https://github.com/denisk176/Open-Assistant/commit/b9c60ed582a8ca0855ab4e213a5e921f3a3fc24c)
#### Monday 2023-07-10 07:45:15 by Tobias Pitters

add alpaca gpt4 dataset (#2610)

The inputs can be quite a lot of different versions of `no input`,
therefore don't use the `input` column for that.
In some cases the text in `input` is already in the instruction, in
these cases, we also don't use the `input` column.

I am not quite sure how to concatenate the `instruction` and the `input`
column. In most cases it seems fine to just replace last appearance of
`.`, `!` or `?` with a colon, e.g.:
Instruction: `Identify the odd one out.`
Input: `Twitter, Instagram, Telegram`
or 
Instruction: `How dense is a given material?`
Input: `Steel`

But we also have some questions like:
Instruction: `Given the following synopsis, what is the moral lesson of
this story?`
Input: `Once upon a time, there was a poor young boy who wanted some
candy. He begged his father for money to buy it, but his father said no
and ordered him to go to bed. As he was going to bed, the boy saw a
five-dollar bill on the counter, which he took and bought the candy.`

Where this might not be the best case. Either way, I think the this one
token will not make significant difference the model and therefore I
just concatenate instruction and input with a space.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[730a724cd7...](https://github.com/treckstar/yolo-octo-hipster/commit/730a724cd7e9d24cacef6d248eab27506f635611)
#### Monday 2023-07-10 08:22:04 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [Wulferion/cmss13](https://github.com/Wulferion/cmss13)@[9bbac13b28...](https://github.com/Wulferion/cmss13/commit/9bbac13b2898570be5e448ce50ca110472561630)
#### Monday 2023-07-10 08:53:38 by TotalEpicness

Globber balance overhaul (#3039)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request
Globber came out overtuned as shit and actually replicated some of the
issues that we didn't want like the dreaded ChokePoint Boiler Torture
Rebalances some issues that weren't forseen during the development nor
TM stage of globber. This should be TM'd


General changes:
- Globber C/D 25 seconds > 30 seconds ( the temp nerf PR didnt actually
fix this correctly)
- Fire deals 2x damage instead of 1.5x damage ( this needs significant
testing and will likely be toned down)
- Acid spray doesn't stun at full distances anymore

Depending on TM feedback, I might switch between these two variants of
this overhaul:

Rework variance 1: Keep zoom and current design while maintaining a
little toughness [currently on]
- Armor 25 > 20
-  Zoom halved 4 > 2
-  Dropped health a tier: 650 > 600
- Fire deals 2x damage instead of 1.25x damage
- Globber C/D

Rework variance 2: Embrace the zoom removal
- Directional armor 10 base armor + 20 at the front. Flank a globber to
kill it!
- Slight windup increase 5s > 6s
- Fire damage 1.25x > 1.5x

Fixes:

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

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

:cl: Totalepicness

balance: Rebalances globber, which has come out overtuned. Globber now
has reduced health, armor and zoom along with higher fire damage
multiplier.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: Epicness <coolguyethanw@gmail.com>
Co-authored-by: morrowwolf <darthbane97@gmail.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[e80cf8f358...](https://github.com/tgstation/tgstation/commit/e80cf8f3586e5aeb599e8f54bd35ebafb878e101)
#### Monday 2023-07-10 09:14:16 by Jacquerel

Improved spider web AI (#76637)

## About The Pull Request

The AI I coded for spiders deciding where to make webs when they aren't
otherwise occupied would do so by finding the _closest_ valid tile,
which seemed like a good idea at the time. The problem with that is that
the "closest" algorithm we use has a predictable search pattern which
meant that spiders would always predictably make a diagonal line of webs
pointing South West, which looked very silly.
I've rewritten how they pick targets to introduce some randomness, which
causes them to properly spread out and make a nicer-looking structure:
which serves purely to annoy spacemen who need to pass through this
area.


![image](https://github.com/tgstation/tgstation/assets/7483112/cb01828f-7653-4010-a4f5-2abc6e10b630)

I'll be honest I mostly did this while bored waiting for other PRs which
I require for my other branch to get merged.

## Why It's Good For The Game

This probably only annoyed me to be quite honest and if you left one
alone for long enough it would fill enough space that you couldn't tell
anyway, but it does look nicer now.

## Changelog

:cl:
add: AI-controlled spiders will make more web-shaped webs.
/:cl:

---
## [Time-Green/tgstation](https://github.com/Time-Green/tgstation)@[8c2c72b0ed...](https://github.com/Time-Green/tgstation/commit/8c2c72b0ed7a1fad112fc4da8a8b7de7faa5e114)
#### Monday 2023-07-10 09:26:28 by LemonInTheDark

Duiffel Spotfix (#76442)

## About The Pull Request

Gives duffelbags their proper slot count
They inherited this from backpacks, but I sorta just forgot about that

[Creates "levels" of locked objects, uses that to make locked duffels
work](https://github.com/tgstation/tgstation/pull/76442/commits/c613c00f62fa3ff03bb33737d24da9acbf2050e3)

[c613c00](https://github.com/tgstation/tgstation/pull/76442/commits/c613c00f62fa3ff03bb33737d24da9acbf2050e3)

Turns locked into something that holds defines, this makes life a lot
easier.
Requires a lot of boilerplate because of how many uses of these procs
there are and all the passthrough and shit.

Adds a few outfit subtypes to avoid this class of failure in future.

Renames the args in a few but not all touched procs, one thing at a time

Closes #76407
Closes #76430 Had the lock check in the wrong place
Closes #76441 GOD I HATE TK SO MUCH

Wrote half the pr without glasses so if it's weird gimme some grace
yeah?

## Changelog
:cl:
fix: Fixes some fuck with duffelbags, them not holding enough + issues
with spawning gear in them (job shit and all)
/:cl:

---
## [Time-Green/tgstation](https://github.com/Time-Green/tgstation)@[d85e44c69c...](https://github.com/Time-Green/tgstation/commit/d85e44c69cc06dbeeb3a0de7f76273de45ee3893)
#### Monday 2023-07-10 09:26:28 by ChungusGamer666

SPECIES NUKING 2023: Head flags 3 & Knuckles: Fixes some growing pains with head flags  (#76440)

## About The Pull Request

Fixes https://github.com/tgstation/tgstation/issues/76422
This was caused by me somehow not using the wrapper there and not
noticing it

Also fixes hair gradients and facial hair gradients. I am pretty sure
they were uhh, being hidden behind the actual hair/facial hair. Oops.

Also also fixes spawning yourself as a human as admin and getting random
hair colors. That was just a failure to update the icon after updating
everything, I think?

Additionally, to totally babyproof all of this, ensures that head_flags
involved stuff gets applied AFTER species by creating a new preference
priority, and uses two separate wrappers to apply gradient style and
color.

Here's this absolute hellspawn to prove that everything works.

![image](https://github.com/tgstation/tgstation/assets/82850673/7ed29a68-cb60-4b28-996c-3be0e7331be8)

![image](https://github.com/tgstation/tgstation/assets/82850673/e57128be-0d7c-46ad-90dd-ee25981d0fea)

![image](https://github.com/tgstation/tgstation/assets/82850673/5c3619a8-fe6f-42b3-9fdc-12277d568e8d)

![image](https://github.com/tgstation/tgstation/assets/82850673/fdd13000-2220-47ad-8e02-44bc75a4a907)

Sorry for being so damn good at breaking this codebase.

## Why It's Good For The Game

Bugs are bad they make you mad

## Changelog

:cl:
fix: Hair and facial hair gradients work again now
fix: Facial hair colors apply properly again
fix: Admin spawned characters will get hair color preferences applied
properly
/:cl:

---
## [ieee802dot11ac/gh1milostuff](https://github.com/ieee802dot11ac/gh1milostuff)@[0a5f1c4284...](https://github.com/ieee802dot11ac/gh1milostuff/commit/0a5f1c42840a079604c4dfa4b690456967420c5a)
#### Monday 2023-07-10 09:35:17 by First Last

i just spent *WAY* too long on this shit and it's not even correct. fuck you cisco

---
## [eun0115-sm6125/kernel_realme_r5x](https://github.com/eun0115-sm6125/kernel_realme_r5x)@[212c70ffa1...](https://github.com/eun0115-sm6125/kernel_realme_r5x/commit/212c70ffa10108e7d70ae75ad6777edec11196ca)
#### Monday 2023-07-10 09:43:16 by Wang Han

power: Introduce OnePlus 3 fingerprintd thaw hack

Taken from Oneplus 3, this hack will make fingerprintd recover from suspend quickly.

Small fixes for newer kernels since we're coming from 3.10.108..

Change-Id: I0166e82d51a07439d15b41dbc03d7e751bfa783b
Co-authored-by: Cyber Knight <cyberknight755@gmail.com>
[cyberknight777: forwardport and adapt to 4.14]
Signed-off-by: Shreyansh Lodha <slodha96@gmail.com>
Signed-off-by: Pierre2324 <pdbbasketball@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>
Signed-off-by: Dhruv <dhruvgera61@gmail.com>
Signed-off-by: Cyber Knight <cyberknight755@gmail.com>
Signed-off-by: mcdofrenchfreis <xyzevan@androidist.net>

---
## [rerun-io/rerun](https://github.com/rerun-io/rerun)@[926bf048e2...](https://github.com/rerun-io/rerun/commit/926bf048e28a8f4c637afce3c57d793ec8de8454)
#### Monday 2023-07-10 11:21:06 by Emil Ernerfeldt

Use `camino` crate for UTF8 paths in `re_types_builder` (#2637)

### What
TLDR: camino paths are a more ergonomic, since they implement
`to_string`, `as_str` etc. I think we should use it in more places.

From [the docs of `camino`](https://crates.io/crates/camino):

#### Why camino?
`camino`'s `Utf8PathBuf` and `Utf8Path` types are like the standard
library's `PathBuf` and `Path` types, except
they are guaranteed to only contain UTF-8 encoded data. Therefore, they
expose the ability to get their
contents as strings, they implement `Display`, etc.

The `std::path` types are not guaranteed to be valid UTF-8. This is the
right decision for the standard library,
since it must be as general as possible. However, on all platforms,
non-Unicode paths are vanishingly uncommon for a
number of reasons:
* Unicode won. There are still some legacy codebases that store paths in
encodings like [Shift JIS], but most
  have been converted to Unicode at this point.
* Unicode is the common subset of supported paths across Windows and
Unix platforms. (On Windows, Rust stores paths
as [an extension to UTF-8](https://simonsapin.github.io/wtf-8/), and
converts them to UTF-16 at Win32
  API boundaries.)
* There are already many systems, such as Cargo, that only support UTF-8
paths. If your own tool interacts with any such
system, you can assume that paths are valid UTF-8 without creating any
additional burdens on consumers.
* The ["makefile
problem"](https://www.mercurial-scm.org/wiki/EncodingStrategy#The_.22makefile_problem.22)
asks: given a
Makefile or other metadata file (such as `Cargo.toml`) that lists the
names of other files, how should the names in
the Makefile be matched with the ones on disk? This has *no general,
cross-platform solution* in systems that support
non-UTF-8 paths. However, restricting paths to UTF-8 eliminates this
problem.

[Shift JIS]: https://en.wikipedia.org/wiki/Shift_JIS

Therefore, many programs that want to manipulate paths *do* assume they
contain UTF-8 data, and convert them to `str`s
as necessary. However, because this invariant is not encoded in the
`Path` type, conversions such as
`path.to_str().unwrap()` need to be repeated again and again, creating a
frustrating experience.

Instead, `camino` allows you to check that your paths are UTF-8 *once*,
and then manipulate them
as valid UTF-8 from there on, avoiding repeated lossy and confusing
conversions.


### Checklist
* [x] I have read and agree to [Contributor
Guide](https://github.com/rerun-io/rerun/blob/main/CONTRIBUTING.md) and
the [Code of
Conduct](https://github.com/rerun-io/rerun/blob/main/CODE_OF_CONDUCT.md)
* [x] I've included a screenshot or gif (if applicable)
* [x] I have tested [demo.rerun.io](https://demo.rerun.io/pr/2637) (if
applicable)

- [PR Build Summary](https://build.rerun.io/pr/2637)
- [Docs preview](https://rerun.io/preview/pr%3Aemilk%2Fcamino/docs)
- [Examples
preview](https://rerun.io/preview/pr%3Aemilk%2Fcamino/examples)

---
## [TeodorD420/rustest](https://github.com/TeodorD420/rustest)@[8744738e59...](https://github.com/TeodorD420/rustest/commit/8744738e5955c02834d67db6f14201c28c9ac61c)
#### Monday 2023-07-10 11:24:12 by Arturlang

Updates TGUI and adds bin folder for .bat scripts (#2011)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Updates TGUI and build tools and .vscode files to what TG has.
Does not actually update UI's, but does have fixes for a couple
including the join game UI's tabs not working.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Not needing to have a local installation of yarn to run dev-mode is
nice.
Updating TGUI is a annoying chore that helps in the future when porting
more interfaces
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
code: Adds a bin folder with dev scripts, updates TGUI, .vscode folder
to what TG has.
fix: Fixes the input in the bottom right being white in darkmode, no
more unreadable text
fix: You can now use the tab buttons in the join ship menu.
qol: The outpost mission menu now looks a whole lot better
fix: The input bar no longer randomly becomes white and unreadable on
darkmode
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: Mark Suckerberg <29362068+MarkSuckerberg@users.noreply.github.com>

---
## [zapSNH/ZTheme](https://github.com/zapSNH/ZTheme)@[661067e80b...](https://github.com/zapSNH/ZTheme/commit/661067e80b4ad0c55725a901793752a69a5f5c50)
#### Monday 2023-07-10 11:28:13 by ZapSNH

Changed lots of stuff and added some other stuff

- Added CommNet Icons
- Don't look at `FlightUILinearQuadrant_bg#193x189.png`, worst mistake of my life
- The bar backgrounds on the bottom-left flight panel are now consistent with the docking panel bars
- Made the blue buttons less ugly
- Added some minor icons (kerbal experience, contract difficulty)
- Themed the Timewarp things
- The funds indicator no longer covers the units
- Made the reputation bar look better. Unfortunately, KSP stretches the texture so it's WIDE but it looks awesome nonetheless

---
## [realforest2001/forest-cm13](https://github.com/realforest2001/forest-cm13)@[a48f036428...](https://github.com/realforest2001/forest-cm13/commit/a48f0364283526637b637542b432d91593b2bdf5)
#### Monday 2023-07-10 11:29:40 by QuickLode

Colony Synthetics have less resistance but are faster. (#3821)

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->
While exploring reasons why this role was underplayed one of the things
that came up was its speed. It is dreadfully slow - to the point where
defenders are able to force an engagement against Synthetics. There is
no chance to run from anything faster as a Colony Synthetic. Making it
have to fight often.

Lowering the resistance is something devs wanted, and for gameplay this
is good because a Synthetic shouldn't be forced into a fight unless they
have no other option. Especially not by something as slow as a defender.
Might tweak later but council generally is in agreement with this
change. Little by little!

For the CQC, a Colony Synthetic is not as advanced as a Shipside one,
but still is more than capable of outmanuevering a human. As for the
hilarious UPP Pvt being better than a Colony Synth in CQC I will make a
separate PR

For Fireman, a Synthetic can bend metal, move cars and do many other
'superhuman' feats of stength, they should not struggle at carrying
people, especially shouldn't be worse at carrying people than a Marine.
It's from 1 to 3, to represent the strength yet aging capabilities of
the Colony Synthetic. @morrowwolf forgot this one

- doesn't touch WJ
# Explain why it's good for the game
Less resistance is something devs wanted.
Allows Colony Synthetics an option to avoid certain engagements as now
they are able to outrun some types of Xenomorphs off-weeds. Defenders
should not be able to catch them offweeds.
A Synthetic should have no problem carrying something as light as a
human being - they especially should not have MORE trouble carrying
someone than your standard human doctor.

# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl: QuickLoad
balance: Colony Synthetics are faster but are less resistant. This
allows for the option of avoiding engagements.
balance: Colony Synthetics have slightly better CQC and can carry people
better.
/:cl:

---
## [cilium/linux](https://github.com/cilium/linux)@[935f3709fd...](https://github.com/cilium/linux/commit/935f3709fdac437fdd541759397f2fe9d4771655)
#### Monday 2023-07-10 11:40:10 by Daniel Borkmann

bpf: Add fd-based tcx multi-prog infra with link support

This work refactors and adds a lightweight extension ("tcx") to the tc BPF
ingress and egress data path side for allowing BPF program management based
on fds via bpf() syscall through the newly added generic multi-prog API.
The main goal behind this work which we also presented at LPC [0] last year
and a recent update at LSF/MM/BPF this year [3] is to support long-awaited
BPF link functionality for tc BPF programs, which allows for a model of safe
ownership and program detachment.

Given the rise in tc BPF users in cloud native environments, this becomes
necessary to avoid hard to debug incidents either through stale leftover
programs or 3rd party applications accidentally stepping on each others toes.
As a recap, a BPF link represents the attachment of a BPF program to a BPF
hook point. The BPF link holds a single reference to keep BPF program alive.
Moreover, hook points do not reference a BPF link, only the application's
fd or pinning does. A BPF link holds meta-data specific to attachment and
implements operations for link creation, (atomic) BPF program update,
detachment and introspection. The motivation for BPF links for tc BPF programs
is multi-fold, for example:

  - From Meta: "It's especially important for applications that are deployed
    fleet-wide and that don't "control" hosts they are deployed to. If such
    application crashes and no one notices and does anything about that, BPF
    program will keep running draining resources or even just, say, dropping
    packets. We at FB had outages due to such permanent BPF attachment
    semantics. With fd-based BPF link we are getting a framework, which allows
    safe, auto-detachable behavior by default, unless application explicitly
    opts in by pinning the BPF link." [1]

  - From Cilium-side the tc BPF programs we attach to host-facing veth devices
    and phys devices build the core datapath for Kubernetes Pods, and they
    implement forwarding, load-balancing, policy, EDT-management, etc, within
    BPF. Currently there is no concept of 'safe' ownership, e.g. we've recently
    experienced hard-to-debug issues in a user's staging environment where
    another Kubernetes application using tc BPF attached to the same prio/handle
    of cls_bpf, accidentally wiping all Cilium-based BPF programs from underneath
    it. The goal is to establish a clear/safe ownership model via links which
    cannot accidentally be overridden. [0,2]

BPF links for tc can co-exist with non-link attachments, and the semantics are
in line also with XDP links: BPF links cannot replace other BPF links, BPF
links cannot replace non-BPF links, non-BPF links cannot replace BPF links and
lastly only non-BPF links can replace non-BPF links. In case of Cilium, this
would solve mentioned issue of safe ownership model as 3rd party applications
would not be able to accidentally wipe Cilium programs, even if they are not
BPF link aware.

Earlier attempts [4] have tried to integrate BPF links into core tc machinery
to solve cls_bpf, which has been intrusive to the generic tc kernel API with
extensions only specific to cls_bpf and suboptimal/complex since cls_bpf could
be wiped from the qdisc also. Locking a tc BPF program in place this way, is
getting into layering hacks given the two object models are vastly different.

We instead implemented the tcx (tc 'express') layer which is an fd-based tc BPF
attach API, so that the BPF link implementation blends in naturally similar to
other link types which are fd-based and without the need for changing core tc
internal APIs. BPF programs for tc can then be successively migrated from classic
cls_bpf to the new tc BPF link without needing to change the program's source
code, just the BPF loader mechanics for attaching is sufficient.

For the current tc framework, there is no change in behavior with this change
and neither does this change touch on tc core kernel APIs. The gist of this
patch is that the ingress and egress hook have a lightweight, qdisc-less
extension for BPF to attach its tc BPF programs, in other words, a minimal
entry point for tc BPF. The name tcx has been suggested from discussion of
earlier revisions of this work as a good fit, and to more easily differ between
the classic cls_bpf attachment and the fd-based one.

For the ingress and egress tcx points, the device holds a cache-friendly array
with program pointers which is separated from control plane (slow-path) data.
Earlier versions of this work used priority to determine ordering and expression
of dependencies similar as with classic tc, but it was challenged that for
something more future-proof a better user experience is required. Hence this
resulted in the design and development of the generic attach/detach/query API
for multi-progs. See prior patch with its discussion on the API design. tcx is
the first user and later we plan to integrate also others, for example, one
candidate is multi-prog support for XDP which would benefit and have the same
'look and feel' from API perspective.

The goal with tcx is to have maximum compatibility to existing tc BPF programs,
so they don't need to be rewritten specifically. Compatibility to call into
classic tcf_classify() is also provided in order to allow successive migration
or both to cleanly co-exist where needed given its all one logical tc layer and
the tcx plus classic tc cls/act build one logical overall processing pipeline.

tcx supports the simplified return codes TCX_NEXT which is non-terminating (go
to next program) and terminating ones with TCX_PASS, TCX_DROP, TCX_REDIRECT.
The fd-based API is behind a static key, so that when unused the code is also
not entered. The struct tcx_entry's program array is currently static, but
could be made dynamic if necessary at a point in future. The a/b pair swap
design has been chosen so that for detachment there are no allocations which
otherwise could fail.

The work has been tested with tc-testing selftest suite which all passes, as
well as the tc BPF tests from the BPF CI, and also with Cilium's L4LB.

Kudos also to Nikolay Aleksandrov and Martin Lau for in-depth early reviews
of this work.

  [0] https://lpc.events/event/16/contributions/1353/
  [1] https://lore.kernel.org/bpf/CAEf4BzbokCJN33Nw_kg82sO=xppXnKWEncGTWCTB9vGCmLB6pw@mail.gmail.com
  [2] https://colocatedeventseu2023.sched.com/event/1Jo6O/tales-from-an-ebpf-programs-murder-mystery-hemanth-malla-guillaume-fournier-datadog
  [3] http://vger.kernel.org/bpfconf2023_material/tcx_meta_netdev_borkmann.pdf
  [4] https://lore.kernel.org/bpf/20210604063116.234316-1-memxor@gmail.com

Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>

---
## [cilium/linux](https://github.com/cilium/linux)@[e8e6ce6edd...](https://github.com/cilium/linux/commit/e8e6ce6edd56331f197f711a06305b624f4ba0f1)
#### Monday 2023-07-10 11:40:10 by Daniel Borkmann

bpf: Add generic attach/detach/query API for multi-progs

This adds a generic layer called bpf_mprog which can be reused by different
attachment layers to enable multi-program attachment and dependency resolution.
In-kernel users of the bpf_mprog don't need to care about the dependency
resolution internals, they can just consume it with few API calls.

The initial idea of having a generic API sparked out of discussion [0] from an
earlier revision of this work where tc's priority was reused and exposed via
BPF uapi as a way to coordinate dependencies among tc BPF programs, similar
as-is for classic tc BPF. The feedback was that priority provides a bad user
experience and is hard to use [1], e.g.:

  I cannot help but feel that priority logic copy-paste from old tc, netfilter
  and friends is done because "that's how things were done in the past". [...]
  Priority gets exposed everywhere in uapi all the way to bpftool when it's
  right there for users to understand. And that's the main problem with it.

  The user don't want to and don't need to be aware of it, but uapi forces them
  to pick the priority. [...] Your cover letter [0] example proves that in
  real life different service pick the same priority. They simply don't know
  any better. Priority is an unnecessary magic that apps _have_ to pick, so
  they just copy-paste and everyone ends up using the same.

The course of the discussion showed more and more the need for a generic,
reusable API where the "same look and feel" can be applied for various other
program types beyond just tc BPF, for example XDP today does not have multi-
program support in kernel, but also there was interest around this API for
improving management of cgroup program types. Such common multi-program
management concept is useful for BPF management daemons or user space BPF
applications coordinating internally about their attachments.

Both from Cilium and Meta side [2], we've collected the following requirements
for a generic attach/detach/query API for multi-progs which has been implemented
as part of this work:

  - Support prog-based attach/detach and link API
  - Dependency directives (can also be combined):
    - BPF_F_{BEFORE,AFTER} with relative_{fd,id} which can be {prog,link,none}
      - BPF_F_ID flag as {fd,id} toggle; the rationale for id is so that user
        space application does not need CAP_SYS_ADMIN to retrieve foreign fds
        via bpf_*_get_fd_by_id()
      - BPF_F_LINK flag as {prog,link} toggle
      - If relative_{fd,id} is none, then BPF_F_BEFORE will just prepend, and
        BPF_F_AFTER will just append for attaching
      - Enforced only at attach time
    - BPF_F_REPLACE with replace_bpf_fd which can be prog, links have their
      own infra for replacing their internal prog
    - If no flags are set, then it's default append behavior for attaching
  - Internal revision counter and optionally being able to pass expected_revision
  - User space application can query current state with revision, and pass it
    along for attachment to assert current state before doing updates
  - Query also gets extension for link_ids array and link_attach_flags:
    - prog_ids are always filled with program IDs
    - link_ids are filled with link IDs when link was used, otherwise 0
    - {prog,link}_attach_flags for holding {prog,link}-specific flags
  - Must be easy to integrate/reuse for in-kernel users

The uapi-side changes needed for supporting bpf_mprog are rather minimal,
consisting of the additions of the attachment flags, revision counter, and
expanding existing union with relative_{fd,id} member.

The bpf_mprog framework consists of an bpf_mprog_entry object which holds
an array of bpf_mprog_fp (fast-path structure). The bpf_mprog_cp (control-path
structure) is part of bpf_mprog_bundle. Both have been separated, so that
fast-path gets efficient packing of bpf_prog pointers for maximum cache
efficiency. Also, array has been chosen instead of linked list or other
structures to remove unnecessary indirections for a fast point-to-entry in
tc for BPF.

The bpf_mprog_entry comes as a pair via bpf_mprog_bundle so that in case of
updates the peer bpf_mprog_entry is populated and then just swapped which
avoids additional allocations that could otherwise fail, for example, in
detach case. bpf_mprog_{fp,cp} arrays are currently static, but they could
be converted to dynamic allocation if necessary at a point in future.
Locking is deferred to the in-kernel user of bpf_mprog, for example, in case
of tcx which uses this API in the next patch, it piggybacks on rtnl.

An extensive test suite for checking all aspects of this API for prog-based
attach/detach and link API comes as BPF selftests in this series.

Kudos also to Andrii Nakryiko for API discussions wrt Meta's BPF management.

  [0] https://lore.kernel.org/bpf/20221004231143.19190-1-daniel@iogearbox.net
  [1] https://lore.kernel.org/bpf/CAADnVQ+gEY3FjCR=+DmjDR4gp5bOYZUFJQXj4agKFHT9CQPZBw@mail.gmail.com
  [2] http://vger.kernel.org/bpfconf2023_material/tcx_meta_netdev_borkmann.pdf

Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[a3caec7e3c...](https://github.com/git-for-windows/git/commit/a3caec7e3c3d64cc4020b228b6617ea5ca5b0c11)
#### Monday 2023-07-10 11:51:27 by Johannes Schindelin

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
## [Helg2/tgstation](https://github.com/Helg2/tgstation)@[fc854e7076...](https://github.com/Helg2/tgstation/commit/fc854e70760354181a049aa73f5a2ac06b0b8a49)
#### Monday 2023-07-10 12:46:33 by Watermelon914

Removes TTS voice disable option (#76530)

## About The Pull Request
Removes the TTS voice disable option, which was already unavailable on
TG as it was set to off by default. The reason this was added was so
that downstreams could toggle the config on or off.

## Why It's Good For The Game
I think this option fundamentally undermines the TTS system because it
allows individual players to disable their voice globally, meaning that
players who have TTS enabled will not be able to hear them.

This worsens the experience for players who have TTS enabled and it's
not something I want to include as an option. If players don't like
their voice, they can turn TTS off for themselves so that they don't
hear the voices. If players don't want to customize their voice, they
can quickly choose a random voice, and we can take directions in the
future to make voice randomization consistent with gender so that a male
does not get randomly assigned a female voice and vice versa.

This option is already unavailable on TG servers because it was
primarily added for downstreams, but I don't think giving downstreams
the option to undermine the TTS system is the right direction to take.
Downstreams are still completely free to code this option on their own
codebase.

---------

Co-authored-by: Watermelon914 <3052169-Watermelon914@users.noreply.gitlab.com>

---
## [gportay/iamroot](https://github.com/gportay/iamroot)@[719ea1a580...](https://github.com/gportay/iamroot/commit/719ea1a580a169cbc5a604b4defa2d9857cd8275)
#### Monday 2023-07-10 12:49:36 by Gaël PORTAY

dso: guess the deflib from the binary

According to ld.so(8):

	On some 64-bit architectures, the default paths for 64-bit
	shared objects are /lib64, and then /usr/lib64.

The default library path differs on some 64-bit architectures on the
GNU/Linux systems. This behaviour is driven by the environment variable
IAMROOT_LIBRARY_PATH.

The glibc x86_64 and aarch64 architectures use the directory lib64
instead of lib (i.e. IAMROOT_LIBRARY_PATH=/lib64:/usr/lib64).

The musl library and both FreeBSD and OpenBSD systems use directory lib
only.

Furthermore, this default library path is distro specific on the Linux
systems. Arch Linux (x86_64 only) uses lib, symlinks lib64 to lib and
uses lib32 for its multilib support. Fedora uses distinct directories
for both lib and lib64, lib for 32-bits, lib64 64-bit. It is different
in the Debian world and its multiarch[1] support; it adds a tuple[2]
directory after the lib directory for the architecture.

This makes the magical very tricky to guess the default library path on
the Linux systems; it shall support the following situations:
 1. cross-chroot libc (i.e. from GNU World to musl)
 2. cross-chroot architecture (i.e. form x86-64 to i686 or armv7-a)
 3. execve executables (i.e. shared object with an interpreter)
 4. dlopen libraries (i.e. shared object without an interpreter)

The magic is based on the ELF header to guess if the chroot is a 32-bit
or a 64-bit world and if the operating system and its ABI is a either
UNIX System V or GNU/Linux or even FreeBSD.

The name of the dynamic loader is also needed to detect a Linux world
since the GNU/Linux ELF shared objects can be either UNIX System V or
GNU/Linux (OpenBSD uses UNIX System V as well).

The dynamic loader is in the interpreter segment of the ELF executable
file. However, the none-executable files ELF shared objects (such as
libraries) does not have that segment.

Therefore, it is hard to determine if the chroot world is either a
64-bit GNU/Linux or a musl (or even OpenBSD), and if it has to use
either /lib64:/usr/lib64 or /lib:/usr/lib as default library path
though; as needed by the point 4.

The libc soname is system specific:
 - libc.so.6 for GNU/Linux since glibc 2.0
 - libc.so.5 for Linux libc (former libc based on glibc 1; see the note
   below)
 - libc.so for musl (note: the dynamic loader is a symlink to libc)
 - libc.so.5 for FreeBSD 5.0
 - libc.so.6 for FreeBSD 6.0
 - libc.so.7 for FreeBSD since since 7.0
 - libc.so.96.2 for OpenBSD 7.2
 - libc.so.97.1 for OpenBSD 7.3

It is not ideal to rely on the libc soname as it is subject to collision
between the different operating systems; for example with the libc.so.6
of FreeBSD 6.x.

Hopefully, the libc.so.6 soname is pretty stable as the glibc 2.0 was
released in the early of 1997 (i.e. 26 years ago)[3].

Even better, the GNU libc needs the dynamic loader while the FreeBSD
libc does not; a least since 2.0.7 (tested down to Debian 2.0 Hamm[4];
Debian 1.3 Bo[5] was using the former Linux libc fork, aka libc.so.5).

Debian 2.0 (i386):

	$ curl -O http://archive.debian.org/debian/dists/hamm/main/binary-i386/base/libc6_2.0.7t-1.deb
	$ ar x libc6_2.0.7t-1.deb
	$ tar xf data.tar.gz
	$ readelf -a lib/libc.so.6 | grep -E '(NEEDED|SONAME)'
	 0x00000001 (NEEDED)                     Shared library: [ld-linux.so.2]
	 0x0000000e (SONAME)                     Library soname: [libc.so.6]
	$ file -L lib/libc.so.6
	lib/libc-2.0.7.so: ELF 32-bit LSB shared object, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, stripped, too many notes (256)
	$ lib/ld-linux.so.2 lib/libc.so.6
	GNU C Library production release version 2.0.7, by Roland McGrath et al.
	Compiled by GNU CC version 2.7.2.3.
	Copyright (C) 1992, 93, 94, 95, 96, 97, 98 Free Software Foundation, Inc.
	This is free software; see the source for copying conditions.
	There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A
	PARTICULAR PURPOSE.
	Compiled on a Linux 2.0.33 system on 1998/07/16.
	Available extensions:
		GNU libio by Per Bothner
		BIND-4.9.7-REL
		NIS(YP) NSS modules 0.8 by Thorsten Kukuk
		UFC-crypt, patchlevel 1e by Michael Glad
		linuxthreads-0.6 by Xavier Leroy
	Report bugs using the `glibcbug' script to <bugs@gnu.org>.

Debian 1.3 (i386):

	$ curl -O http://archive.debian.org/debian/dists/bo/main/binary-i386/base/libc5_5.4.33-6.deb
	$ ar x libc5_5.4.33-6.deb
	$ tar xf data.tar.gz
	$ readelf -a lib/libc.so.5 | grep -E '(NEEDED|SONAME)'
	 0x0000000e (SONAME)                     Library soname: [libc.so.5]

Consequently, the default library path may be guessed to dlopen the
shared objects that are not executable files but that are linked against
the GNU libc; as long as the libc.so.6 is the library soname and as long
as it is executable and contains the needed dynamic loader. This hacky
guess has to be updated after every bump of the libc soname or if the
libc ceases to be executable (i.e. no more need to the dynamic loader or
no more interpreter).

This guesses the default library path of the chroot'ed Linux environnement by

Note: According to libc(7):

	Linux libc

	In the early to mid 1990s, there was for a while Linux libc, a
	fork of glibc 1.x created by Linux developers who felt that
	glibc development at the time was not sufficing for the needs of
	Linux. Often, this library was referred to (ambiguously) as just
	“libc”. Linux libc released major versions 2, 3, 4, and 5, as
	well as many minor versions of those releases. Linux libc4 was
	the last version to use the a.out binary format, and the first
	version to provide (primitive) shared library support. Linux
	libc 5 was the first version to support the ELF binary format;
	this version used the shared library soname libc.so.5. For a
	while, Linux libc was the standard C library in many Linux
	distributions.

	However, notwithstanding the original motivations of the Linux
	libc effort, by the time glibc 2.0 was released (in 1997), it
	was clearly superior to Linux libc, and all major Linux
	distributions that had been using Linux libc soon switched back
	to glibc. To avoid any confusion with Linux libc versions, glibc
	2.0 and later used the shared library soname libc.so.6.

	Since the switch from Linux libc to glibc 2.0 occurred long ago,
	man-pages no longer takes care to document Linux libc details.
	Nevertheless, the history is vis‐ ible in vestiges of
	information about Linux libc that remain in a few manual pages,
	in particular, references to libc4 and libc5.

[1]: https://wiki.debian.org/Multiarch
[2]: https://wiki.debian.org/Multiarch/Tuples
[3]: https://linux.die.net/man/7/libc
[4]: http://archive.debian.org/debian/dists/hamm/main/binary-i386/base/libc6_2.0.7t-1.deb
[5]: http://archive.debian.org/debian/dists/bo/main/binary-i386/base/libc5_5.4.33-6.deb

---
## [Lukalukaxxx/langchain](https://github.com/Lukalukaxxx/langchain)@[75fb9d2fdc...](https://github.com/Lukalukaxxx/langchain/commit/75fb9d2fdcc201e80ad9c065a02c6cc9ccf6d716)
#### Monday 2023-07-10 12:50:34 by Stefano Lottini

Cassandra support for chat history using CassIO library (#6771)

### Overview

This PR aims at building on #4378, expanding the capabilities and
building on top of the `cassIO` library to interface with the database
(as opposed to using the core drivers directly).

Usage of `cassIO` (a library abstracting Cassandra access for
ML/GenAI-specific purposes) is already established since #6426 was
merged, so no new dependencies are introduced.

In the same spirit, we try to uniform the interface for using Cassandra
instances throughout LangChain: all our appreciation of the work by
@jj701 notwithstanding, who paved the way for this incremental work
(thank you!), we identified a few reasons for changing the way a
`CassandraChatMessageHistory` is instantiated. Advocating a syntax
change is something we don't take lighthearted way, so we add some
explanations about this below.

Additionally, this PR expands on integration testing, enables use of
Cassandra's native Time-to-Live (TTL) features and improves the phrasing
around the notebook example and the short "integrations" documentation
paragraph.

We would kindly request @hwchase to review (since this is an elaboration
and proposed improvement of #4378 who had the same reviewer).

### About the __init__ breaking changes

There are
[many](https://docs.datastax.com/en/developer/python-driver/3.28/api/cassandra/cluster/)
options when creating the `Cluster` object, and new ones might be added
at any time. Choosing some of them and exposing them as `__init__`
parameters `CassandraChatMessageHistory` will prove to be insufficient
for at least some users.

On the other hand, working through `kwargs` or adding a long, long list
of arguments to `__init__` is not a desirable option either. For this
reason, (as done in #6426), we propose that whoever instantiates the
Chat Message History class provide a Cassandra `Session` object, ready
to use. This also enables easier injection of mocks and usage of
Cassandra-compatible connections (such as those to the cloud database
DataStax Astra DB, obtained with a different set of init parameters than
`contact_points` and `port`).

We feel that a breaking change might still be acceptable since LangChain
is at `0.*`. However, while maintaining that the approach we propose
will be more flexible in the future, room could be made for a
"compatibility layer" that respects the current init method. Honestly,
we would to that only if there are strong reasons for it, as that would
entail an additional maintenance burden.

### Other changes

We propose to remove the keyspace creation from the class code for two
reasons: first, production Cassandra instances often employ RBAC so that
the database user reading/writing from tables does not necessarily (and
generally shouldn't) have permission to create keyspaces, and second
that programmatic keyspace creation is not a best practice (it should be
done more or less manually, with extra care about schema mismatched
among nodes, etc). Removing this (usually unnecessary) operation from
the `__init__` path would also improve initialization performance
(shorter time).

We suggest, likewise, to remove the `__del__` method (which would close
the database connection), for the following reason: it is the
recommended best practice to create a single Cassandra `Session` object
throughout an application (it is a resource-heavy object capable to
handle concurrency internally), so in case Cassandra is used in other
ways by the app there is the risk of truncating the connection for all
usages when the history instance is destroyed. Moreover, the `Session`
object, in typical applications, is best left to garbage-collect itself
automatically.

As mentioned above, we defer the actual database I/O to the `cassIO`
library, which is designed to encode practices optimized for LLM
applications (among other) without the need to expose LangChain
developers to the internals of CQL (Cassandra Query Language). CassIO is
already employed by the LangChain's Vector Store support for Cassandra.

We added a few more connection options in the companion notebook example
(most notably, Astra DB) to encourage usage by anyone who cannot run
their own Cassandra cluster.

We surface the `ttl_seconds` option for automatic handling of an
expiration time to chat history messages, a likely useful feature given
that very old messages generally may lose their importance.

We elaborated a bit more on the integration testing (Time-to-live,
separation of "session ids", ...).

### Remarks from linter & co.

We reinstated `cassio` as a dependency both in the "optional" group and
in the "integration testing" group of `pyproject.toml`. This might not
be the right thing do to, in which case the author of this PR offer his
apologies (lack of confidence with Poetry - happy to be pointed in the
right direction, though!).

During linter tests, we were hit by some errors which appear unrelated
to the code in the PR. We left them here and report on them here for
awareness:

```
langchain/vectorstores/mongodb_atlas.py:137: error: Argument 1 to "insert_many" of "Collection" has incompatible type "List[Dict[str, Sequence[object]]]"; expected "Iterable[Union[MongoDBDocumentType, RawBSONDocument]]"  [arg-type]
langchain/vectorstores/mongodb_atlas.py:186: error: Argument 1 to "aggregate" of "Collection" has incompatible type "List[object]"; expected "Sequence[Mapping[str, Any]]"  [arg-type]

langchain/vectorstores/qdrant.py:16: error: Name "grpc" is not defined  [name-defined]
langchain/vectorstores/qdrant.py:19: error: Name "grpc" is not defined  [name-defined]
langchain/vectorstores/qdrant.py:20: error: Name "grpc" is not defined  [name-defined]
langchain/vectorstores/qdrant.py:22: error: Name "grpc" is not defined  [name-defined]
langchain/vectorstores/qdrant.py:23: error: Name "grpc" is not defined  [name-defined]
```

In the same spirit, we observe that to even get `import langchain` run,
it seems that a `pip install bs4` is missing from the minimal package
installation path.

Thank you!

---
## [githubranjit/Spotify-Clone](https://github.com/githubranjit/Spotify-Clone)@[e8178e64cb...](https://github.com/githubranjit/Spotify-Clone/commit/e8178e64cbd2b64bf851f51363b6380322a5edbe)
#### Monday 2023-07-10 13:01:16 by Ranjit Bhandari

Add files via upload

Vast Music Catalog: Our Spotify clone offers access to an extensive catalog of millions of songs across various genres, artists, and languages.

Personalized Recommendations: Experience the power of our intelligent algorithm that learns your musical preferences over time and suggests tracks, albums, and artists tailored specifically to your taste.

Curated Playlists: Create your own playlists or follow playlists curated by popular artists, influencers, friends, and other users. Perfect for any occasion or mood.

Podcasts: Dive into the world of podcasts and explore a wide range of engaging audio content, from true crime to educational shows, all within our Spotify clone.

Social Interaction: Connect with friends, share your favorite tracks, and collaborate on playlists. Discover what others are listening to, exchange recommendations, and foster a vibrant community of music lovers.

Multi-Device Compatibility: Enjoy a seamless experience across multiple devices, including smartphones, tablets, and desktops. Switch effortlessly between platforms and continue your music journey without interruption.

Offline Listening: Download your favorite tracks and listen to them offline, perfect for situations with limited internet connectivity or when you're on the move.

High-Quality Audio: Immerse yourself in the music with top-notch audio quality. Enjoy crystal-clear clarity and experience the artist's vision exactly as intended.

Easy Navigation: Find your favorite songs, albums, and artists quickly with our powerful search feature. Organize your music library and access your saved tracks and playlists with ease.

Security and Privacy: Rest assured that your personal information and listening habits are protected. Our Spotify clone adheres to industry-standard security protocols, ensuring your data is secure.

---
## [tromey/gdb](https://github.com/tromey/gdb)@[8bcead6966...](https://github.com/tromey/gdb/commit/8bcead69665af3a9f9867cd34c3a1daf22120027)
#### Monday 2023-07-10 13:14:52 by Andrew Burgess

gdb/testsuite: add test for core file with a 0 pid

This patch contains a test for this commit:

  commit c820c52a914cc9d7c63cb41ad396f4ddffff2196
  Date:   Fri Aug 6 19:45:58 2010 +0000

              * thread.c (add_thread_silent): Use null_ptid instead of
              minus_one_ptid while getting rid of stale inferior_ptid.

This is another test that has been carried in the Fedora GDB tree for
some time, and I thought that it would be worth merging to master.  I
don't believe there is any test like this currently in the testsuite.

The original issue was reported in this thread:

  https://inbox.sourceware.org/gdb-patches/AANLkTi=zuEDw6qiZ1jRatkdwHO99xF2Qu+WZ7i0EQjef@mail.gmail.com/

The problem was that when GDB was used to open a vmcore (core file)
image generated by the Linux kernel GDB would (sometimes) crash with
an assertion failure:

  thread.c:884: internal-error: switch_to_thread: Assertion `inf != NULL' failed.

To understand what's going on we need some background; a vmcore file
represents each processor core in the same way that a standard
application core file represents threads.  Thus, we might say, a
vmcore file represents cores as threads.

When writing a vmcore file, the kernel will store the pid of the
process currently running on that core as the thread's lwpid.

However, if a core is idle, with no process currently running on it,
then the lwpid for that thread is stored as 0 in the vmcore file.  If
multiple cores are idle then multiple threads will have a lwpid of 0.

Back in 2010, the original issue reported tried to change the kernel's
behaviour in this thread:

  https://lkml.org/lkml/2010/8/3/75

This change was rejected by the kernel team, the current
behaviour (lwpid of 0) was considered correct.  I've checked the
source of a recent kernel.  The code mentioned in the lkml.org posting
has moved, it's now in the function crash_save_cpu in the file
kernel/kexec_core.c, but the general behaviour is unchanged, an idle
core will have an lwpid of 0, so I think GDB still needs to be able to
handle this case.

When GDB loads a vmcore file (which is handled just like any other
core file) the sections are processed in core_open to generate the
threads for the core file.  The processing is done by calling
add_to_thread_list, a function which looks for sections named .reg/NN
where NN is the lwpid of the thread, GDB then builds a ptid_t for the
new thread and calls add_thread.

Remember, in our case the lwpid is 0.  Now for the first thread this
is fine, if a little weird, 0 isn't usually a valid lwpid, but that's
OK, GDB creates a thread with lwpid of 0 and carries on.

When we find the next thread (core) with lwpid of 0, we attempt to
create another thread with an lwpid of 0.  This of course clashes with
the previously created thread, they have the same ptid_t, so GDB tries
to delete the first thread.

And it was within this thread delete code that we triggered a bug
which would then cause GDB to assert -- when deleting we tried to
switch to a thread with minus_one_ptid, this resulted in a call to
find_inferior_pid (passing in minus_one_ptid's pid, which is -1), the
find_inferior_pid call fails and returns NULL, which then triggered an
assert in switch_to_thread.

The actual details of the why the assert triggered are really not
important.  What's important (I think) is that a vmcore file might
have this interesting lwpid of 0 characteristic, which isn't something
we see in "normal" application core files, and it is this that I think
we should be testing.

Now, you might be thinking: isn't deleting the first thread the wrong
thing to do?  If the vmcore file has two threads that represent two
cores, and both have an lwpid of 0 (indicating both cores are idle),
then surely GDB should still represent this as two threads?  You're
not wrong.  This was mentioned by Pedro in the original GDB mailing
list thread here:

  https://inbox.sourceware.org/gdb-patches/201008061057.03037.pedro@codesourcery.com/

This is indeed a problem, and this problem is still present in GDB
today.  I plan to try and address this in a later commit, however,
this first commit is about getting a test in place to confirm that GDB
at a minimum doesn't crash when loading such a vmcore file.

And so, finally, what's in this commit?

This commit contains a new test.  The test doesn't actually contain a
vmcore file.  Instead I've created a standard application core file
that contains two threads, and then manually edited the core file to
set the lwpid of each thread to 0.

To further reduce the size of the core file (as it will be stored in
git), I've zeroed all of the LOAD-able segments in the core file.
This test really doesn't care about that part of the core file, we
only really care about loading the register's, this is enough to
confirm that the GDB doesn't crash.

Obviously as the core file is pre-generated, this test is architecture
specific.  There are already a few tests in gdb.arch/ that include
pre-generate core files.  Just as those existing tests do, I've
compressed the core file with bzip2, which reduces it to just 750
bytes.  I have structured the test so that if/when this patch is
merged I can add some additional core files for other architectures,
however, these are not included in this commit.

The test simply expands the core file, and then loads it into GDB.
One interesting thing to note is that GDB reports the core file
loading like this:

  (gdb) core-file ./gdb/testsuite/outputs/gdb.arch/core-file-pid0/core-file-pid0.x86-64.core
  [New process 1]
  [New process 1]
  Failed to read a valid object file image from memory.
  Core was generated by `./segv-mt'.
  Program terminated with signal SIGSEGV, Segmentation fault.
  The current thread has terminated
  (gdb)

There's two interesting things here: first, the repeated "New process
1" message.  This is caused because linux_core_pid_to_str reports
anything with an lwpid of 0 as a process, rather than an LWP.  And
second, the "The current thread has terminated" message.  This is
because the first thread in the core file is the current thread, but
when GDB loads the second thread (which also has lwpid 0) this causes
the first thread to be deleted, as a result GDB thinks that the
current (first) thread has terminated.

As I said previously, both of these problems are a result of the lwpid
0 aliasing, which is not being fixed in this commit -- this commit is
just confirming that GDB doesn't crash when loading this core file.

Reviewed-By: Kevin Buettner <kevinb@redhat.com>

---
## [rudo-thomas/tanka](https://github.com/rudo-thomas/tanka)@[904a7c53e8...](https://github.com/rudo-thomas/tanka/commit/904a7c53e8a1afec5af8b05bb11f7da846595a09)
#### Monday 2023-07-10 13:32:14 by Julien Duchesne

Fix `getSnippetHash` not considering all files (#765)

* Fix `getSnippetHash` not considering all files
Made a stupid mistake in the previous PR: https://github.com/grafana/tanka/pull/759

This fixes it and adds another benchmark test to ensure it doesn't happen again.
I also removed the Github Actions benchmark test, as it's not really useful, anytime we change the tests, we'll get erroneous results which will be annoying.
Instead, I added the benchmark tests to the Drone run, we can compare whenever we want.

* linting

* Add changelog, will release straight away

---
## [consul/consul](https://github.com/consul/consul)@[970a64e276...](https://github.com/consul/consul/commit/970a64e2762c8dd8c9e265acb9195f069ea7bb0a)
#### Monday 2023-07-10 13:32:58 by Javi Martín

Enable mousewheel when focusing on the map

Zooming with the mousewheel is useful when you want to use it, but
annoying when you don't want to.

Here we're taking an intermediary approach: by default, the mousewheel
isn't active, but it will be active after focusing on the map, so it can
be used both to scroll and to zoom.

This behavior presents usability issues, though, since we aren't making
users aware of the way the mousewheel works, and even if they were
aware, it could be confusing anyway. However, I currently think it's
better than always enabling or always disabling the mousewheel (might
change my mind, though).

Note that the "focus" event is only used on the map, so if we click on a
marker or navigate to a marker with the keyboard without focusing on the
map first, the mousewheel isn't enabled. The same would happen if we
used the "click" event.

We might use the Leaflet.GestureHandling plugin in the future to deal
with this issue and the scroll on touch screens.

---
## [Blacklion567/Little-Projects-HTML-CSS-JS](https://github.com/Blacklion567/Little-Projects-HTML-CSS-JS)@[39fa157a49...](https://github.com/Blacklion567/Little-Projects-HTML-CSS-JS/commit/39fa157a4914436687465435c441ec0c7f5df1bc)
#### Monday 2023-07-10 13:41:55 by Blacklion567

Little-Projects-HTML-CSS-JS

God has surely promised His grace to the humbled: that is, to those who mourn over and despair of themselves. But a man cannot be thoroughly humbled till he realizes that his salvation is utterly beyond his own powers, counsels, efforts, will and works, and depends absolutely on the will, counsel, pleasure and work of Another -- God alone.

---
## [slowy07/Python-bellshade](https://github.com/slowy07/Python-bellshade)@[d41755a32d...](https://github.com/slowy07/Python-bellshade/commit/d41755a32d2a33e73be4baa7fc6f80fecd76432c)
#### Monday 2023-07-10 14:39:25 by slowy07

fix: revert yang sebelumnya

disini saya ingin merubah kodingan saya berdasarkan hasil review dari @slowy07
"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

Section 1.10.32 of "de Finibus Bonorum et Malorum", written by Cicero in 45 BC
"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"

1914 translation by H. Rackham
"But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure. To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it? But who has any right to find fault with a man who chooses to enjoy a pleasure that has no annoying consequences, or one who avoids a pain that produces no resultant pleasure?"

Section 1.10.33 of "de Finibus Bonorum et Malorum", written by Cicero in 45 BC
"At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat."

1914 translation by H. Rackham
"On the other hand, we denounce with righteous indignation and dislike men who are so beguiled and demoralized by the charms of pleasure of the moment, so blinded by desire, that they cannot foresee the pain and trouble that are bound to ensue; and equal blame belongs to those who fail in their duty through weakness of will, which is the same as saying through shrinking from toil and pain. These cases are perfectly simple and easy to distinguish. In a free hour, when our power of choice is untrammelled and when nothing prevents our being able to do what we like best, every pleasure is to be welcomed and every pain avoided. But in certain circumstances and owing to the claims of duty or the obligations of business it will frequently occur that pleasures have to be repudiated and annoyances accepted. The wise man therefore always holds in these matters to this principle of selection: he rejects pleasures to secure other greater pleasures, or else he endures pains to avoid worse pains."

---
## [neeshacark/Yogstation](https://github.com/neeshacark/Yogstation)@[d1c7dfdc1a...](https://github.com/neeshacark/Yogstation/commit/d1c7dfdc1ae55bfd9fa7f603f415b762ba6a472a)
#### Monday 2023-07-10 14:52:13 by SapphicOverload

IPC tweaks (#19467)

* funny tv head robot go brrrrr

* Update IPC.dm

* not that fast

* fuck it we ball

---
## [aderuelle/linux](https://github.com/aderuelle/linux)@[4a557a5d1a...](https://github.com/aderuelle/linux/commit/4a557a5d1a6145ea586dc9b17a9b4e5190c9c017)
#### Monday 2023-07-10 15:01:23 by Linus Torvalds

sparse: introduce conditional lock acquire function attribute

The kernel tends to try to avoid conditional locking semantics because
it makes it harder to think about and statically check locking rules,
but we do have a few fundamental locking primitives that take locks
conditionally - most obviously the 'trylock' functions.

That has always been a problem for 'sparse' checking for locking
imbalance, and we've had a special '__cond_lock()' macro that we've used
to let sparse know how the locking works:

    # define __cond_lock(x,c)        ((c) ? ({ __acquire(x); 1; }) : 0)

so that you can then use this to tell sparse that (for example) the
spinlock trylock macro ends up acquiring the lock when it succeeds, but
not when it fails:

    #define raw_spin_trylock(lock)  __cond_lock(lock, _raw_spin_trylock(lock))

and then sparse can follow along the locking rules when you have code like

        if (!spin_trylock(&dentry->d_lock))
                return LRU_SKIP;
	.. sparse sees that the lock is held here..
        spin_unlock(&dentry->d_lock);

and sparse ends up happy about the lock contexts.

However, this '__cond_lock()' use does result in very ugly header files,
and requires you to basically wrap the real function with that macro
that uses '__cond_lock'.  Which has made PeterZ NAK things that try to
fix sparse warnings over the years [1].

To solve this, there is now a very experimental patch to sparse that
basically does the exact same thing as '__cond_lock()' did, but using a
function attribute instead.  That seems to make PeterZ happy [2].

Note that this does not replace existing use of '__cond_lock()', but
only exposes the new proposed attribute and uses it for the previously
unannotated 'refcount_dec_and_lock()' family of functions.

For existing sparse installations, this will make no difference (a
negative output context was ignored), but if you have the experimental
sparse patch it will make sparse now understand code that uses those
functions, the same way '__cond_lock()' makes sparse understand the very
similar 'atomic_dec_and_lock()' uses that have the old '__cond_lock()'
annotations.

Note that in some cases this will silence existing context imbalance
warnings.  But in other cases it may end up exposing new sparse warnings
for code that sparse just didn't see the locking for at all before.

This is a trial, in other words.  I'd expect that if it ends up being
successful, and new sparse releases end up having this new attribute,
we'll migrate the old-style '__cond_lock()' users to use the new-style
'__cond_acquires' function attribute.

The actual experimental sparse patch was posted in [3].

Link: https://lore.kernel.org/all/20130930134434.GC12926@twins.programming.kicks-ass.net/ [1]
Link: https://lore.kernel.org/all/Yr60tWxN4P568x3W@worktop.programming.kicks-ass.net/ [2]
Link: https://lore.kernel.org/all/CAHk-=wjZfO9hGqJ2_hGQG3U_XzSh9_XaXze=HgPdvJbgrvASfA@mail.gmail.com/ [3]
Acked-by: Peter Zijlstra <peterz@infradead.org>
Cc: Alexander Aring <aahringo@redhat.com>
Cc: Luc Van Oostenryck <luc.vanoostenryck@gmail.com>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>

---
## [hazelcast/hazelcast](https://github.com/hazelcast/hazelcast)@[566574a5b4...](https://github.com/hazelcast/hazelcast/commit/566574a5b49f423109a4de61f21427838bd8076b)
#### Monday 2023-07-10 15:04:39 by James Holgate

Modify KubernetesClient shutdown behaviour  (#24613) [5.3.z] (#24710)

Backport of: https://github.com/hazelcast/hazelcast/pull/24613

The overall goal of this change is to change the shutdown behaviour of
KubernetesClient so our Stateful Set monitor thread shuts down before
our `ClusterTopologyIntentTracker`, to allow the intent tracker to fully
process all completed messages before Node shutdown.

**The Current Problem**
In its current state, the Stateful Set monitor thread is intended to
shutdown after `Thread#interrupt` is called, triggering the
`Thread#interrupted` check within the main `while(running)` loop of the
Runnable. However, this check is not reached as the call to
`WatchResponse#readLine` from within the main `run()` method is a
blocking call that waits until data is available to read before
proceeding. Since this call waits for non-null data before completing,
the result is always non-null, and therefore this code block never exits
under normal conditions:
```java
while ((message = watchResponse.nextLine()) != null) {
    onMessage(message);
}
```

Since this `while` loop cannot exit, and the `#readLine` method (which
passes to `BufferedReader#readLine` under the hood) is a blocking I/O
operation which cannot be interrupted, this operation does not end when
`Thread#interrupt` is called. This leads to the Stateful Set monitor
thread out-living the `ClusterTopologyIntentTracker`, even if the
StsMonitor is interrupted first. As a result, during shutdown, it is
possible for the StsMonitor to send data to the intent tracker after it
has been destroyed and its executor is no longer accepting tasks.

**The Root of the Problem**
To reach our goal of ensuring that the Stateful Set monitor thread can
no longer send requests to the `ClusterTopologyIntentTracker`, we need
to add synchronization between the two objects that guarantees the
intent tracker shuts down after the StsMonitor thread has completed.
This can be achieved using a simple `CountDownLatch` which is counted
down after the thread has completed, and awaited before shutting down
the tracker.

The main obstacle to achieving this is, as mentioned above, that the
StsMonitor thread cannot be interrupted when waiting for
`WatchResponse#readLine` to complete, and so the thread never completes.
The only way this thread can complete is to either force its
termination, or alter the message reading approach to allow interruption
as intended.

**Identifying Resolution Paths**
We don't want to force termination of our Stateful Set monitor thread as
this could result in message handling being terminated after it has been
received, but not before it has finished being processed. Therefore the
only way we can allow this thread to be interrupted as intended is to
alter the message reading mechanics in a way that allows it to be
interrupted as well.

There is no way for us to know if more messages are pending from the k8s
watch besides waiting for data to be received, so the best we can do is
allow the StsMonitor to finish processing any messages it has already
received (preventing process corruption), but terminate the stream of
new messages it is waiting for before we shutdown the intent tracker.

**Potential Solutions**
So we've identified the root of the problem as our `#readLine` function
blocking through interrupts, so how do we make it interruptible? Sadly
one of the shortcomings of I/O operations in Java is that they usually
cannot be interrupted in the traditional manner, so we have a few
approaches to consider:

1) We could modify the message reading code to use
`BufferedReader#ready` and `Thread#sleep` to periodically check if there
is data to be read before calling any read functions. The problem with
this approach is that A) `#ready` returns true if any data is available,
not just if there is a full line of data to be read; and B) utilizing a
sleep loop can result in delayed message handling at the least, or
busy-waiting overhead at worst.

2) We could use "hacky" solutions to interrupt the
`BufferedReader#readLine` such as closing underlying sockets or
connections, propagating an exception to the reader. The problem with
this solution is that everything related to our reading operation is
handled in `syncrhonized` blocks, and since our shutdown process starts
outside the StsMonitor thread, our calling thread is unable to obtain
these locks (being held by the StsMonitor)!

3) It's possible that we could rewrite the `WatchResponse` mechanics to
use Java NIO magic such as `Selector` for interruptible I/O operations.
The issue with this approach is that it would require fairly significant
refactoring of the related codebase, and may not end up providing the
exact functionality we are looking for in our use case.

4) We can introduce an `Executor` to handle our I/O operations within
the StsMonitor thread, allowing us to wait on a `Future#get` call
instead of our `BufferedReader#readLine` call, where a `Future#get`
operation can be interrupted by the waiting thread being interrupted.
The downside to this solution is we have to introduce an additional
thread on top of the existing StsMonitor thread itself.

**Selecting a Solution**
Considering the above information, I concluded the most sensible
approach was to use (4) and introduce an `Executor` thread for the I/O
operations. By using a separate thread for this call we can be rougher
with it, as we know that worse case scenario we interrupt a message
being read that has not started being processed yet (but we're shutting
down anyway).

This solution also allows for the least amount of underlying code
changes, as our `Future#get` can be interrupted without issue,
maintaining the current approach used for handling the StsMonitor
shutdown. The only downside for this approach is the addition of another
thread alongside the StsMonitor thread, but the actual impact of this
should be minimal as both threads will still be waiting most of the
time, so the only negative impact is being 1 tiny step closer to
possible thread starvation.

Generally I think this is the best solution at hand which allows quick
shutdown of the StsMonitor thread while minimising potential for data
loss or corruption. Combined with the `CountDownLatch` used, this allows
for consistent service shutdown order between the `StsMonitor` thread
and the `ClusterTopologyIntentTracker`.

---
## [Edspirit/tutor](https://github.com/Edspirit/tutor)@[18ce1f2fe4...](https://github.com/Edspirit/tutor/commit/18ce1f2fe432a82fd97711d3d5766e8d47185f9e)
#### Monday 2023-07-10 16:36:08 by Régis Behmo

feat: persistent bind-mounts

This is an important change, where we get remove the previous `--mount`
option, and instead opt for persistent bind-mounts.

Persistent bind mounts have several advantages:
- They make it easier to remember which folders need to be bind-mounted.
- Code is *much* less clunky, as we no longer need to generate temporary
  docker-compose files.
- They allow us to bind-mount host directories *at build time* using the
  buildx `--build-context` option.
- The transition from development to production becomes much easier, as
  images will automatically be built using the host repo.

The only drawback is that persistent bind-mounts are slightly less
portable: when a config.yml file is moved to a different folder, many
things will break if the repo is not checked out in the same path.

For instance, this is how to start working on a local fork of
edx-platform:

    tutor config save --append MOUNTS=/path/to/edx-platform

And that's all there is to it. No, this fork will be used whenever we
run:

    tutor images build openedx
    tutor local start
    tutor dev start

This change is made possible by huge improvements in the build time
performance. These improvements make it convenient to re-build Docker
images often.

Related issues:
https://github.com/openedx/wg-developer-experience/issues/71
https://github.com/openedx/wg-developer-experience/issues/66
https://github.com/openedx/wg-developer-experience/issues/166

---
## [RedCityGame/redcity.ink](https://github.com/RedCityGame/redcity.ink)@[7bc4f9f4a4...](https://github.com/RedCityGame/redcity.ink/commit/7bc4f9f4a40c4e611f3012decf776eb7b60840a3)
#### Monday 2023-07-10 17:38:57 by Umut Dağ

fuck you github, fix Gemfile and drop minima version to 2.5.1

---
## [AnywayFarus/Fluffy-STG](https://github.com/AnywayFarus/Fluffy-STG)@[24cab6d9f9...](https://github.com/AnywayFarus/Fluffy-STG/commit/24cab6d9f91ea45cb420bdac188d3142eebb004b)
#### Monday 2023-07-10 18:14:39 by SkyratBot

Plasma objects no longer violently explode when ignited [MDB IGNORE] (#22216)

* Plasma objects no longer violently explode when ignited (#76492)

## About The Pull Request
This is one of those "can I get away with making a change I want" PRs.

I actually didn't know this had been changed before as it's not exactly
something I mess with often, but I really think it sucks. Plasma stuff
is supposed to ignite and cause fires, not explode (unless in a TTV). I
noticed this when I was poking around and found out that apparently
Disco Inferno just explodes now instead of setting on fire which also
sucks.

I figure there's a few fixes for this problem:

1) Nerf how hard plasma stuff explodes. This is an option, but I kind of
dislike that it does it at all more than anything. The biggest issue is
that just the regular statues explode with 20 LIGHT, which is pretty
fucking massive and basically just delimbs everyone around. I'd have to
nerf it HARD for it to get anywhere near what I think is acceptable.
2) Make a snowflake version of the statue that just ignites on hit with
a torch. I also don't like this because it'll make people think the
regular statues don't explode.
3) This option, which I think is cleaner and just makes sense compared
to the others.

I don't know if @ vincentiusvin still codes, but as far as I can tell
this was their doing, so it's only fair they get to speak up.

Fixes #71894

## Why It's Good For The Game
I don't like it, I think it goes against what we're used to for plasma
stuff (that it starts fires, not makes explosions) and it makes one of
my favorite shuttles boring and stupid. That being said, I'm honestly
not going to fight for this too hard if a lot of people like it, but I
am - as always - open to alternatives.

## Changelog
:cl: Vekter
del: Plasma objects (statues, toilets, etc.) no longer explode when
ignited. They just release plasma like everything else plasma. (This
doesn't impact injecting plasma into cells or dipping cigars in plasma,
those still explode.)
/:cl:

* Plasma objects no longer violently explode when ignited

---------

Co-authored-by: Vekter <TheVekter@users.noreply.github.com>

---
## [AnywayFarus/Fluffy-STG](https://github.com/AnywayFarus/Fluffy-STG)@[c5f60969da...](https://github.com/AnywayFarus/Fluffy-STG/commit/c5f60969da9465d10482ef0c122428fa42bfcb2c)
#### Monday 2023-07-10 18:14:39 by SkyratBot

Rat RP expansion [MDB IGNORE] (#22204)

* Rat RP expansion (#76455)

## About The Pull Request

This fixes a vile and long-standing bug where putting a mouse inside
your hat would not allow the mouse to control your movements, as it
would pop out of the hat whenever it tried to move.
Additionally as a feature this allows a mouse sitting on your head to
convey complicated instructions such as "scream" or "do a flip", via
emoting. Through drift compatibility, the rat's living mech will also
perform this action.

I could have made this into a component but there's no fucking way any
other item is going to have this behaviour, so I didn't.

## Why It's Good For The Game

This feature was already in the game but broken and I want it not to be
broken.
The mouse should be able to control your entire life.

## Changelog

:cl:
fix: Placing a mouse inside your chef hat will once more allow it to
pilot you around.
add: A player-controlled mouse inside your chef hat can compel you to
perform complex actions, such as flipping and spinning. You will obey
because the mouse knows better than you do.
/:cl:

* Rat RP expansion

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [504brandon/FUNKIN-FPS-REFLASHED](https://github.com/504brandon/FUNKIN-FPS-REFLASHED)@[fc536e75ef...](https://github.com/504brandon/FUNKIN-FPS-REFLASHED/commit/fc536e75efc6c78b5fa494860751b9bbd52afd9b)
#### Monday 2023-07-10 18:18:50 by 504brandon

Merge branch 'bugged-stage-and-song-system-(i-hate-my-life)' of https://github.com/504brandon/FUNKIN-FPS-REFLASHED into bugged-stage-and-song-system-(i-hate-my-life)

---
## [504brandon/FUNKIN-FPS-REFLASHED](https://github.com/504brandon/FUNKIN-FPS-REFLASHED)@[bb4303f4f3...](https://github.com/504brandon/FUNKIN-FPS-REFLASHED/commit/bb4303f4f35ebe7733a01ec5d551b00b73141419)
#### Monday 2023-07-10 18:19:53 by [504]brandon

Merge branch 'master' into bugged-stage-and-song-system-(i-hate-my-life)

---
## [504brandon/FUNKIN-FPS-REFLASHED](https://github.com/504brandon/FUNKIN-FPS-REFLASHED)@[bf0732e909...](https://github.com/504brandon/FUNKIN-FPS-REFLASHED/commit/bf0732e909d6e87838fad1c2fd38d99ba914e8e2)
#### Monday 2023-07-10 18:20:00 by [504]brandon

Merge pull request #1 from 504brandon/bugged-stage-and-song-system-(i-hate-my-life)

better shit

---
## [jmakovicka/mame](https://github.com/jmakovicka/mame)@[4a5b8a415f...](https://github.com/jmakovicka/mame/commit/4a5b8a415fee66df01d57b871a8025d0f1f1a2f6)
#### Monday 2023-07-10 18:45:01 by wilbertpol

msx1_cart.xml: Added fourteen working items. (#11412)

* Removed Hopper (Europe) tape-to-cartridge hack.
* Demoted The Holy Quran (v1.00) to not working.

New working software list items (msx1_cart.xml)
-------------------------------
Hole in One Professional (Japan, alt 2) [file-hunter]
Hole in One Professional (Japan, alt 3) [file-hunter]
Hot-Asm (Brazil) [file-hunter]
Hot-Plan (Brazil) [file-hunter]
Hydlide II - Shine of Darkness (Korea) [file-hunter]
Hopper (Arab) [file-hunter]
Hans' Adventure (v1.1) [MSXDev]
Hans' Adventure (v1.0) [MSXDev]
Happy Halloween [Clube MSX]
Happy Square Christmas [303bcn]
Heart Stealer 2 [MSXDev]
Heroes Arena [MSXDev]
Hose Diogo Martinez: The Bussas Quest [MSXDev]
How Many Are The Dumbbells You Lift? [cobinee]

---
## [Hafiz8823/Heart-Disease-Prediction-using-ML-with-GUI](https://github.com/Hafiz8823/Heart-Disease-Prediction-using-ML-with-GUI)@[2a4128e33b...](https://github.com/Hafiz8823/Heart-Disease-Prediction-using-ML-with-GUI/commit/2a4128e33bf39a294a053a82797663496374d105)
#### Monday 2023-07-10 18:55:22 by Hafiz Imran

Heart Disease Prediction using ML with GUI.

Description:

I am thrilled to upload my project on GitHub, titled "Heart Disease Prediction using Machine Learning with GUI." This project aims to predict the likelihood of heart disease in individuals based on various health attributes. With the inclusion of a user-friendly graphical user interface (GUI), this project provides an intuitive way for users to interact with the prediction model.

The project utilizes machine learning algorithms and predictive modeling techniques to analyze a dataset comprising features such as age, gender, blood pressure, cholesterol levels, and other relevant medical parameters. By training the model on this dataset, we can accurately predict the presence or absence of heart disease in individuals.

The code and associated files have been meticulously organized and uploaded to my GitHub repository, ensuring a seamless experience for fellow developers and interested parties. The repository includes the necessary data files, code files, and documentation, enabling others to understand and replicate the analysis with ease.

I encourage you to explore the project, review the code, and provide any feedback or suggestions. This project has been an enriching experience for me to apply machine learning concepts in the healthcare domain, ultimately helping in the early detection and prevention of heart diseases.

Thank you for taking the time to explore my project on GitHub. I am excited to receive any comments or contributions that can further enhance the accuracy and usability of the heart disease prediction model.

---
## [opengamedata/opengamedata-core](https://github.com/opengamedata/opengamedata-core)@[6ce843e47b...](https://github.com/opengamedata/opengamedata-core/commit/6ce843e47ba8d805dfd59e659ee26b43e6a561d9)
#### Monday 2023-07-10 19:01:30 by Luke Swanson

Properly echo the variables to the environment.

Fucking fuckity fuck fuck fuck I don't know how I was this fucking
stupid but I should probably hand in my badge after this one.
Obviously need to echo values diretly into variable names in the
environment, not a random-ass range formatting. Stupid.

---
## [sojourn-13/sojourn-station](https://github.com/sojourn-13/sojourn-station)@[94b32aa82c...](https://github.com/sojourn-13/sojourn-station/commit/94b32aa82cdfdf4b9115d178c89e9cd3a7ede6d2)
#### Monday 2023-07-10 19:03:07 by CDB

Bugfixes. (#4685)

* Bugfixes.

Fixes a few spelling mistakes here and there.

Forged stock-parts boxes claimed they had five parts inside. they did not, they have four, corrected.

Toga for the church had an eronious base-state, unsure who touched it, but fix'd.

Bat'ko had incorrect formatting for its on-suit sprite, fixed.

Numerical garb eroniously claimed to be switchable between grey and red. It was actually purple and red, fixed.

Numerical hats both had the wrong icon name and were using(incorrectly) the old sprites. Fixed.

Duty had a missing icon when loaded with a drum and fempty(Who the FUCK let the duty take drums?)

Fixes the sec-shuttle and also comments out the destination it has towards the space fortress which is...commented back out? Right?

Fixes the apparent sec-shuttle so its walls are properly named after the vessel. To do- give some fucking flavor to the Rocinante and Vasiliy.

* Update body_modifications.dm

Removes the ability to select robo-torsos/groins/heads, this functionality doesn't actually work as intended and wasn't intended to be used in this way. Feel free to re-add if it does get fixed.
fixes #4675

* More bugfixes

Fixes tesla turrets attacking colony bots, SI drones, etc.

Fixes embed chance on the psion knife being greater than 0 and thus being able to embed(and promptly bugging out.)

* Update tesla_turret.dm

Slight tweak to Tesla turret code courtesy of Hex.

* Further bugfixes.

RXbow lacked a proper caliber and could thusly accept 10mm rounds.

RXbow also lacked a casing handling tag, not that it makes a huge difference given its snowflake behavior but it was fixed.  I will suggest to perhaps raise the d amage of the crossbow bolt in another non-bug focused PR.

Artificer rail pistols(slab and myrmidon) didn't have a serial defined, fixed.

* More fixes.

Mop bucket now properly updates its sprite after any change to its reagents takes place.

Kitchen spike no longer erroneously requires a strangle grab instead of a neck_grab.

---
## [gorillamania/AICodeBot](https://github.com/gorillamania/AICodeBot)@[bd6e9157b2...](https://github.com/gorillamania/AICodeBot/commit/bd6e9157b253e9fe293829771d9846ac7f2e36d8)
#### Monday 2023-07-10 19:51:39 by Nick Sullivan

Refine commit message handling and update prompts 📝

In this commit, we've made some improvements to the way we handle commit messages. We've added a step to remove any unwanted quotation marks from the commit message before it's written to a temporary file. This should help keep our commit messages clean and readable. 🧹

We've also made some updates to our prompts file. We've streamlined the 'Her' personality description and made some changes to the commit message instructions. We've switched from a list format to bullet points for better readability, and added some extra information about the length of the commit message. We hope these changes will make the prompts more user-friendly and informative. 📚

Remember, a good commit message is like a good joke - it's all about the delivery! 🎭

---
## [tmedwards/sugarcube-2](https://github.com/tmedwards/sugarcube-2)@[f85119203c...](https://github.com/tmedwards/sugarcube-2/commit/f85119203c420651a75538655b2ae9136833348a)
#### Monday 2023-07-10 20:25:49 by Thomas M. Edwards

UPDATE: `Save` API

Change the disk & base64 load `Promise`'s to resolve with the saves' metadata. Also, cleanup.  Also, also, fuck you Github mobile client, I want my newlines back.

---
## [jasonrohrer/OneLife](https://github.com/jasonrohrer/OneLife)@[88ec9ca99f...](https://github.com/jasonrohrer/OneLife/commit/88ec9ca99fc3a15df629dfa47a06ac9d985d124a)
#### Monday 2023-07-10 20:58:00 by Jason Rohrer

New FORGIVE EVERYONE command (which undoes all curses that you've ever issued).  CurseLog now includes lines for expiring curses (E) and forgiving everyone (A).  CurseDB code no longer worries about old key format (which changed more than 90 days ago).  Fixes #858

---
## [smxi/inxi](https://github.com/smxi/inxi)@[2434d89d0c...](https://github.com/smxi/inxi/commit/2434d89d0c75390511b75ee58ef40aba13f3863b)
#### Monday 2023-07-10 21:18:57 by Harald Hope

New version, new man. Continuing the Memory info rollout started in 3.3.27.

--------------------------------------------------------------------------------
SPECIAL THANKS:

1. Thanks to linuxquestions.org Slackware forums for poking around a bit at the
new Memory total logic.

--------------------------------------------------------------------------------
KNOWN ISSUES:

1a. MEMORY: The memory total: has to be synthesized in some cases, based on some
math and educated guessing. When these guesses fall outside of predetermined
ranges, inxi will show note: est. to let the user know the total was synthesized
and possibly incorrect. For detected virtual machines, inxi does not try to
synthesize the total because a VM can have any amount of RAM assigned.

If superuser, and -m used, shows the real total from dmidecode if any RAM was
found. Not all systems have DMI RAM data however, or have dmidecode installed.
Will fallback to sythetic method in that case, which is usually right.

1b. MEMORY: With the superuser /proc/iomem method, if on a VM and not using even
GiB sized RAM ollocation, and -M is not triggered (which usually lets inxi know
it's a VM), the total will get rounded up or down based on a set of rules. For
example, 2.5 GiB real would become 3 GiB. I don't see any solution to this,
either assume the /proc/iomem is right but needs rounding up, or assume the /sys
block counts are right, or remove the feature.

Shows note: est. in cases where the rounded total is greater than a dynamic
factor difference from the internal total amount.

2. GENERAL/GRAPHICS: The problem of users showing up, requesting a feature, then
not doing any work, research, supplying energy, interest, and dare I say,
passion - nothing, expecting 'someone else' to do the work for them, continues,
sadly, with the recent request for vulkan data for Graphics. This appears to be
a problem more with the modern generation of free software users, I don't
remember this type of attitude 20 years ago, but I did watch it as it started
getting more common. Demotivating to be honest, but maybe one day someone will
show up who actually cares enough to help get the features they want developed.

While I am leaving that up as a low priority feature request, I am not
personally interested in that feature, nor is anyone else I asked, and given how
much raw data there is, and how difficult it is to parse, I'll just leave it as
an existing issue which might get work in a few years time, or not, basically
will require someone showing up who actually actively cares.

--------------------------------------------------------------------------------
BUGS:

1. DISK: total: used: report could have had wrong results for used:, like used
being > total: because the filter lists were missing some file systems for
exclusion. More of a fix than a bug, but users might see it as a bug.

--------------------------------------------------------------------------------
FIXES:

1. INFO: get_gcc_data(): was showing same GCC version as main and alternate.
Failed to filter out the discovered primary, that is. This is because usually
name is gcc-11 but sometimes it's the whole version, like gcc-11.2.0, the full
version string. This is the case in Slackware for example.

2. SHORT: MEMORY: BSD: did not show '%' for memory used percent, just the
number.

3. DRIVES/PARTITIONS: PartitionItem::set_filters() added many more exclude
types, that will help avoid both creating wrong disk used totals, and also not
show label:/uuid: fields for filesystem types that don't have uuid/labels. There
were a lot missing: encrypted, distributed, stackable, remote. Should clean up
wrong disk used values in some cases.

4a. PARTITIONS: PartitionItem::set_filters(). Added a lot of file systems, many
fuse, distributed, stackable types.

4b. PARTITIONS: Extended remote file system ID by fs, and added fuse fs for
local mounts, like gvfs, mtp, ptp and many other variants, that's things like
mounting apple partition, android, iphone, archives, etc. This should correct an
entire class of source: ERR-102 outputs.

--------------------------------------------------------------------------------
ENHANCEMENTS:

1. BATTERY: Added 'power' to battery report. That's the amount of watts its
using at that moment, so not super useful since it's running inxi at that
moment. But the data was there, so might as well show it. Only for -Bxx since it
will be so variable. Shows after the charge/condition item.

2. SYSTEM: DistroData: added Oracle id and system base. Added Springdale/PUIAS
system base support. Note, unusually, Eurolinux, ScientificLinux 'just worked'
re id and system base even though that had never been explicitly added. This is
because their os-release file contains 'centos' string.

3. SYSTEM: DistroData: Added ubuntu mantic minotaur to ubuntu id matching table.
This only really is used by Mint, but there you have it. Also added Debian 14
codename Forky.

4a. MEMORY: Add total RAM from one of following:

* /sys/devices/system/memory (if it's available). This directory has to be
compiled into kernel, so is not always present. This source has advantage of
being user readable. If out of set bounds, shows note: est. to let user know
it's an estimate.

* If superuser and /proc/iomme, gets the total from /proc/iomem using some
tricks and synthetic methods, which in general is pretty accurate, but when out
of the bounds set, shows note: est. to let user know results are only estimates.
This overrides /sys total.

* If -m and dmidecode data found, uses the real RAM module total. For Linux and
superuser. This overrides iomem and /sys totals.

4b. MEMORY: add iGPU RAM from /proc/iomem when detected. Requires sudo/root.

4c. MEMORY: using the real -m/RAM total for memory total when available, since
that is the actual value we want, not the estimated stuff from /proc/iomem or
/sys/devices/system.

5. RAM: added a long time oversight, lack of per array RAM installed size and
occupied slots (modules). Those are now part of the Array line for each set of
modules. Since total already shows in System RAM line above, the granular per
array installed size total only shows if > 1 array is present, ie, almost never.

6. DRIVES: disk vendors, added more matches and vendors. We'll know the world is
changing in a significant way when no new vendors appear for a while, but that's
unlikely in the near term.

7. CPU: cpu_arch(), a few new ids added.

8. GRAPHICS: new amd, intel, nvidia ids, updates to driver version etc.

--------------------------------------------------------------------------------
CHANGES:

1. SHORT: for Memory:, switched to using MiB/GiB/TiB, these numbers are just
getting too big to be readable. This is also dynamic, if both used and available
are the same unit, shows x/y [unit], otherwise shows x [unit]/y [unit].

2. MEMORY: changed gpu: to igpu: to avoid confusing it with standalone gpu.
Since only raspberry pi had gpu ram data before, almost nobody would have seen
this in general anyway.

--------------------------------------------------------------------------------
DOCUMENTATION:

1. MAN/OPTIONS: Updated for -Bxx, battery power now.

2. MAN: updated to better define where the System RAM: total:.. available etc
come from, and what they refer to. Also added explanation in -m section about
what the stuff is, and what the field names refer to.

2a. DOCS: docs/inxi-ram.txt added, and more info moved from inxi-data.txt and
inxi-resources.txt. Goal is to remove both those files and move all their data,
and any new data, into granular inxi-xxx.txt files. Also moved some RAM data
from inx-unit-handling.txt to inxi-ram.txt.

2b. DOCS: docs/inxi-unit-handling.txt: updated with more ram / memory units,
code, etc, to better fit with the concept of the inxi-unit-handling.txt doc.

2c. DOCS: docs/inxi-partitions.txt: updated, added more sources for partition
file system types, cleaned up, more useful as a reference now.

2d. DOCS: docs/inxi-distros.txt: NEW, merged data from inxi-data.txt,
inxi-resources.txt. Updated and added more info.

2e. DOCS: docs/inxi-tools-mapping.txt split off from inxi-tools.txt, makes it
easier to find the mapping functions and features, which are hard to remember.
Also updated and improved its usability. This is kind of a key document because
it's hard to remember all the mapping tools internally, and this also connects
those tools to their relevant granular inxi-xxx.txt docs. Not that it will help
get helpers for these tedious tasks, but one can always dream, can't one?

3. DATA: data/graphics/ added for first vulkaninfo output file.

--------------------------------------------------------------------------------
CODE:

1a. RAM: Fixed an irregularity, for RamItem, it used MiB as internal unit, this
was silly because inxi uses KiB everywhere else. This correction was relatively
easy to do, and allows the values to be used by other parts of inxi, like
MemoryData.

1b. RAM: Added return of ram total for memory.

2a. INFO/RAM/PROCESSES: When MEMORY active, now uses row reference to create the
fields. For INFO, now uses MemoryData::row() to generate the row fields instead
of doing the logic in the info line generator. This simplifies the processing
and allows for more granular control of output.

2b. INFO/RAM/PROCESSES: Added debugger switches --dbg 53 (show raw KiB/count
values for /sys/devices/system/memory and /proc/iomem. Added --dbg 54, which
shows per line size for iomem, in human readable units, and a final summary
report of iomem and /sys data, this speeds up debugging.

2c. INFO/RAM/PROCESSES: Added --fake iomem, --fake sys-mem for debugging and
testing.

3. MEMORY: MemoryData::short_data(): added so one tool generates output for all
sources for short data. Easier to track and make consistent, and to make more
granular and robust.

4. DRIVES/PARTITIONS: PartitionItem::partition_filters(),
PartitionItem::fs_excludes(): refactored into PartitionItem::get_filters(),
PartitionItem::set_filters(). Cleaned up, organized better, made comments much
more useful. Goes with DOCS 2c updates. Now there's just one sub that does this
filter/exclude work, which makes it easier to maintain long term.

5. GLOBAL: Used a trick I just learned, declaring variables in the bracket scope
of a class, but not inside the package/class declaration. This makes it work
like a static variable, which Perl 5.008 doesn't support. You have to use a sub
inside the bracket scope to return the data outside that scope, but that is easy
to do.

6. MACHINE: Added return of b_vm for VM detection in MEMORY.

7. SYSTEM: CompilerVersion: Failed to properly use references when passing
$compiler around, not actually sure why it worked, but now is consistent.

---
## [KudoGT/PracticeDeepLearning](https://github.com/KudoGT/PracticeDeepLearning)@[d0c7d4a66a...](https://github.com/KudoGT/PracticeDeepLearning/commit/d0c7d4a66a5f12d195bb30c84c006df26ccf620d)
#### Monday 2023-07-10 21:34:31 by KudoGt

Create Graduate Admission Prediction using ANN

About Dataset
Context
This dataset is created for prediction of Graduate Admissions from an Indian perspective.

Content
The dataset contains several parameters which are considered important during the application for Masters Programs.
The parameters included are :

GRE Scores ( out of 340 )
TOEFL Scores ( out of 120 )
University Rating ( out of 5 )
Statement of Purpose and Letter of Recommendation Strength ( out of 5 )
Undergraduate GPA ( out of 10 )
Research Experience ( either 0 or 1 )
Chance of Admit ( ranging from 0 to 1 )
Acknowledgements
This dataset is inspired by the UCLA Graduate Dataset. The test scores and GPA are in the older format.
The dataset is owned by Mohan S Acharya.

Inspiration
This dataset was built with the purpose of helping students in shortlisting universities with their profiles. The predicted output gives them a fair idea about their chances for a particular university.

Citation
Please cite the following if you are interested in using the dataset :
Mohan S Acharya, Asfia Armaan, Aneeta S Antony : A Comparison of Regression Models for Prediction of Graduate Admissions, IEEE International Conference on Computational Intelligence in Data Science 2019

I would like to thank all of you for contributing to this dataset through discussions and questions. I am in awe of the number of kernels built on this dataset. Some results and visualisations are fantastic and makes me a proud owner of the dataset. Keep em' coming! Thank You.

---
## [RengaN02/PsychonautStation](https://github.com/RengaN02/PsychonautStation)@[b304b6523f...](https://github.com/RengaN02/PsychonautStation/commit/b304b6523fa1f497800c8ba3818e4d2c01d4eaf4)
#### Monday 2023-07-10 21:36:16 by LemonInTheDark

Converts del logging to proper json, using json objects instead of building a text file (#75636)

## About The Pull Request

It's easier to parse, and makes more sense when you read it. This way
I'll never have to add yet another case to my parser for someone
changing where a space goes or something.

Moves qdel into its own category cause the old name looked ugly (yell if
this is dumb)
Added a bitfield to entries pulled from categories, adds a new flag that
enables pretty printing json lists.


## Why It's Good For The Game

IMPROVES my workflow

## Changelog
:cl:
server: del logging is now done by outputting to a json file again, but
this time we're using ACTUAL json and not just a big text string with
newlines and shit
/:cl:

---------

Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>

---
## [Lufferly/tgstation](https://github.com/Lufferly/tgstation)@[03c964ac45...](https://github.com/Lufferly/tgstation/commit/03c964ac45e727543aac85ad817df89a7555fb31)
#### Monday 2023-07-10 21:58:10 by LemonInTheDark

Reworks Duffel Bags (Zippers) (#76313)

## About The Pull Request

Reworks duffel bags in line with oranges proposed plan.


![image](https://github.com/tgstation/tgstation/assets/58055496/126743dd-d7b8-47e0-bdd8-a0caec39c515)

Basically, instead of just making you slower all the time, they make you
slower while you have them open, but give you the same speed while
they're closed.
As a trade off, opening and closing them takes time, 2.1 seconds
(matches the sound) and 0.5 respectively.


https://github.com/tgstation/tgstation/assets/58055496/555d2cd0-038e-4b0b-a693-0c66dac16f5b

[Adds support for limiting extra storage, uses it to make syndie stuff
cool](https://github.com/tgstation/tgstation/pull/76313/commits/d0b2bbf937435b36de3ba497c48771f563b76684)

[d0b2bbf](https://github.com/tgstation/tgstation/pull/76313/commits/d0b2bbf937435b36de3ba497c48771f563b76684)

Syndicate bags currently ignore downsides by just ignoring the slowdown,
but that's kinda boring so let's just buff em instead.

They now support holding a limited amount of bulky items (3), filtered
down to things that would otherwise constitute going loud (or otherwise
be useful to carry around as a loudish traitor)

I may have gone a bit overboard on what I whitelisted here, lemme know
yeah?

I also did some fenangling with backpack uses of create_storage, I don't
like this pattern it was a bad idea I think.

## Why It's Good For The Game

I'm unsure if these delays enough, I think any length of time is decent
since it means you need to stop moving and focus on it for a bit.
My hope is this will make them a proper sidegrade, rather then something
that goes unused/acts as newbie bait

## Changelog
:cl:
balance: Duffelbags will now only make you slow while they are unzipped.
As a tradeoff, you now need to stand still and zip/unzip them to access
their contents/not move real slow.
/:cl:

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [JohnFulpWillard/tgstation](https://github.com/JohnFulpWillard/tgstation)@[6e288185bc...](https://github.com/JohnFulpWillard/tgstation/commit/6e288185bcc4bb3c55a8588369409fcc4e6f2cbf)
#### Monday 2023-07-10 22:19:29 by Jacquerel

Cuter spiderlings (#76532)

## About The Pull Request

I hate looking at spiderlings. Mostly because they're an extremely fast
mob with no directional sprites or animations, so they appear to be a
rapid floating overlay.
I made some new ones. I don't know if they're objectively better but _I_
like them more.

Before:

![image](https://github.com/tgstation/tgstation/assets/7483112/ef561c4f-6d34-4ed2-a486-cd42f06f5648)

After:

![image](https://github.com/tgstation/tgstation/assets/7483112/7c073166-a956-4f7f-8dac-21d1a0f0a868)

Unlike the old sprites they also have directional states and movement
animations so you can scurry around really fast without being a static
image (maybe they shouldn't be so fast? A question for another PR).
I spent like 30 minutes looking at GAGs and then realised not only would
the colours be a pain in the ass but it doesn't support movement states
anyway.

Additionally I made the "dead spiderling" item inherit the dead
spiderling icon state from that spiderling instead of always being the
generic one.

Oh also I think a typo made baby tarantulas completely invisible.

## Why It's Good For The Game

I hate looking at spiderlings.

## Changelog

:cl:
image: New directional sprites for spiderlings, with movement
animations.
fix: Dead spiderlings will be the same colour as they were when they
were alive.
fix: Tarantula spiderlings are no longer invisible,
/:cl:

---
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[962c06b791...](https://github.com/cockroachdb/cockroach/commit/962c06b79199319c63da1f5ba986c3d33355a642)
#### Monday 2023-07-10 22:26:21 by craig[bot]

Merge #99191

99191: rpc: retain information about failed connections r=aliher1911 a=tbg

Prior to this change, `rpc.Context` did not remember a connection after it
failed. A connection attempt would be created whenever we didn't have a
functioning connection to the given `(nodeID, targetAddress, class)` and
callers would be multiplexed onto it as long as that attempt was not known to
have failed.

The main problem with this setup was that it makes it difficult to provide good
observability because a remote node that just hasn't been dialed yet and one
that is down but between attempts looks the same. We could write code that
periodically tries to fully connect all nodes in the cluster to each other, but
even then exporting good metrics is challenging and while we're currently
comfortable with a densely connected cluster, that may change over time.

An additional challenge was presented by circuit breaking and logging of
attempts. Without state retained, we were limited to a simple retry scheme with
lots of redundant logging. It wasn't easy to log how long a connection had been
unhealthy (as an unhealthy connection was represented as an absent connection),
so in effect folks had to trawl through logs to grab the corresponding
timestamps of first and last failure.

Another piece of complexity were the RPC circuit breakers. These were
implemented at the NodeDialer-level (i.e. one circuit breaker per
`(NodeID,Class`)) but kept in the `rpc.Context` (which generally operates on
`(NodeID, Addr, Class)` because gossip also used them. The library they were
using uses recruitment of client traffic, which also isn't ideal as it could
periodically subject a SQL query to a timeout failure. We'd really prefer it
if the breakers probed without user traffic recruitment.

This PR addresses the above shortcomings:

- state is now retained across restarts on a `(NodeID, Addr, Class)` basis in
  the `rpc.Context. This has a few complications, for example we need to handle
decommissioned nodes, as well as nodes that restart under a new listening
address.
- the NodeDialer-level circuit breakers are removed.
- we're no longer recruiting user traffic for probes. Instead, we adopt the
  `util/circuit` package already used for Replica-level circuit breaking. This
library uses an async background probe to determine when to heal the breaker.

I also think the amount of incidental complexity in the `rpc` package is greatly
reduced as a result of this work.

I ran the `failover/non-system/` suite of tests to validate this change. The results
look good[^res].

[^res]: https://gist.github.com/tbg/5f5c716fa2fe5a21eca4a0c3a4a35069

Epic: CRDB-21710
Release note (ui change): a "Networking" metrics dashboard was added.
Release note (ops change): CockroachDB now exposes the following metrics:
- `rpc.connection.{un,}healthy`: Gauge of healthy/unhealthy connections,
- `rpc.connection.{un,}healthy_nanos`: Gauge of aggregate duration the currently {un,}healthy connections have been {,un}healthy for,
-  `grpc.connection.avg_round_trip_latency`: sum of weighted moving averages of round-trip latencies for all peers (it really only makes sense to consume these on a per-peer basis via prometheus)
- Counters `rpc.connection.heartbeats` and `rpc.connection.failures`.
When the `server.child_metrics.enabled` cluster setting is set, these metrics export per-peer values, meaning they can be used to derive a connectivity graph.
Release note (ops change): logging for intra-node RPC connection failures has improved by reducing frequently and improving information content.

Co-authored-by: Tobias Grieger <tobias.b.grieger@gmail.com>

---
## [swordcube/NovaEngine-Godot-FNF](https://github.com/swordcube/NovaEngine-Godot-FNF)@[b7af35b1af...](https://github.com/swordcube/NovaEngine-Godot-FNF/commit/b7af35b1af1279f2a505bdf6a75689df8d783db9)
#### Monday 2023-07-10 22:52:50 by swordcube

i made alpha bet betetr!!

alpha male andrew tate john decapitation despicable the 4th ohio hitting the griddy among us gigachad california boys fortnite fnf you have been banned from the mickey house clubhouse for inappropriate behavior frfr ong gregory you need to vent big balls in your face mouth eating doritos asmr 2023 no virus at 3:72am 3:296.5am spotify playlist soundcloud youtube music vs impostor v45 revival sonic.exe re-exed new super mario bros wii hi squidward spongebob meme mr krabs shut the fuck up

---
## [itseasytosee/tgstation](https://github.com/itseasytosee/tgstation)@[f2ec16c1e6...](https://github.com/itseasytosee/tgstation/commit/f2ec16c1e6485bdf2035837fb3d42de24900e8b4)
#### Monday 2023-07-10 22:54:35 by Vekter

Plasma objects no longer violently explode when ignited (#76492)

## About The Pull Request
This is one of those "can I get away with making a change I want" PRs.

I actually didn't know this had been changed before as it's not exactly
something I mess with often, but I really think it sucks. Plasma stuff
is supposed to ignite and cause fires, not explode (unless in a TTV). I
noticed this when I was poking around and found out that apparently
Disco Inferno just explodes now instead of setting on fire which also
sucks.

I figure there's a few fixes for this problem:

1) Nerf how hard plasma stuff explodes. This is an option, but I kind of
dislike that it does it at all more than anything. The biggest issue is
that just the regular statues explode with 20 LIGHT, which is pretty
fucking massive and basically just delimbs everyone around. I'd have to
nerf it HARD for it to get anywhere near what I think is acceptable.
2) Make a snowflake version of the statue that just ignites on hit with
a torch. I also don't like this because it'll make people think the
regular statues don't explode.
3) This option, which I think is cleaner and just makes sense compared
to the others.

I don't know if @vincentiusvin still codes, but as far as I can tell
this was their doing, so it's only fair they get to speak up.

Fixes #71894

## Why It's Good For The Game
I don't like it, I think it goes against what we're used to for plasma
stuff (that it starts fires, not makes explosions) and it makes one of
my favorite shuttles boring and stupid. That being said, I'm honestly
not going to fight for this too hard if a lot of people like it, but I
am - as always - open to alternatives.

## Changelog
:cl: Vekter
del: Plasma objects (statues, toilets, etc.) no longer explode when
ignited. They just release plasma like everything else plasma. (This
doesn't impact injecting plasma into cells or dipping cigars in plasma,
those still explode.)
/:cl:

---
## [ThiccThighsS4veLives/OnixClient_Scripts](https://github.com/ThiccThighsS4veLives/OnixClient_Scripts)@[cf4a938a92...](https://github.com/ThiccThighsS4veLives/OnixClient_Scripts/commit/cf4a938a923a6e5fa8e22a3d710c3b63a57aa016)
#### Monday 2023-07-10 23:47:48 by Raspberry

ok a lil fix because i just noticed this (#45)

* Half Life 2 GUI

based on hl2 ep2 gui/portal gui

* comment

* I AM SO FUCKING STUPID

* im so stupid i put my module outside the modules folder

* Update index.json

* Rename half_life_2_gui.lua.txt to half_life_2_gui.lua

* Update index.json

---------

Co-authored-by: EpiclyRaspberry <EpiclyRaspberry@users.noreply.github.com>

---

