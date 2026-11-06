# Visual lecture review — lesson 06

Reviewed paused video frames in Brave at: [10:56](https://www.youtube.com/watch?v=i6M7x541Zx8&t=656s), [24:37](https://www.youtube.com/watch?v=i6M7x541Zx8&t=1477s), [49:14](https://www.youtube.com/watch?v=i6M7x541Zx8&t=2954s).
This is a sampled visual review, not full viewing, audio analysis or a transcript.
The sample times were checked against the actual video player's time; unusable screenshots were excluded.

## What was visible

A slide explicitly defines StudentSerializer using Serializer with name, roll and city fields. A later code frame shows a separate myapp.py client using requests.get against a stuinfo detail URL and printing student dictionaries.

## Vocabulary to recognize

`StudentSerializer`, `Serializer`, `CharField`, `IntegerField`, `name`, `roll`, `city`, `myapp.py`, `requests.get`, `stuinfo`.

## How this project follows the lesson

Simplify this serialization-only serializer and add a standalone HTTP client plus stuinfo aliases. Keep the existing collection URLs for compatibility.

## Try it in this project

Read [serializers](api/serializers.py), [views](api/views.py), then [myapp.py](myapp.py). Start the server and run `python myapp.py` in a second terminal. Try `/stuinfo/` and `/stuinfo/1/`. Serialization is output here; saving arrives in lesson 8.

## Reading the code

Each Python source has a `NOTES ABOUT THE COMPLETE CODE ABOVE` comment block below the code.
Read [lecture notes](LECTURE_NOTES.md) for the concept and [README](README.md) for setup.
The code and explanations are original companion material. Unsampled steps, exact constants,
and spoken explanations are not claimed to be verified. [Full research scope](../RESEARCH.md).
