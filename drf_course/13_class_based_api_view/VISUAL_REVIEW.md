# Visual lecture review — lesson 13

Reviewed paused video frames in Brave at: [05:17](https://www.youtube.com/watch?v=IlGguIgO5x4&t=317s), [11:54](https://www.youtube.com/watch?v=IlGguIgO5x4&t=714s), [18:30](https://www.youtube.com/watch?v=IlGguIgO5x4&t=1110s), [23:48](https://www.youtube.com/watch?v=IlGguIgO5x4&t=1428s).
This is a sampled visual review, not full viewing, audio analysis or a transcript.
The sample times were checked against the actual video player's time; unusable screenshots were excluded.

## What was visible

StudentAPI inherits APIView, handles an optional pk for retrieval, and uses request.data in post. Later samples show the browsable API's update forms.

## Vocabulary to recognize

`StudentAPI`, `APIView`, `get`, `post`, `pk`, `format`, `Response`.

## How this project follows the lesson

Keep explicit APIView methods. Explain that the companion separates collection and detail classes instead of branching on optional pk in one class.

## Try it in this project

Compare the explicit get/post/put/patch/delete methods in [views.py](api/views.py) with lesson 12's if/elif function. The lecture's optional-pk class is split into collection/detail classes here to keep each handler short.

## Reading the code

Each Python source has a `NOTES ABOUT THE COMPLETE CODE ABOVE` comment block below the code.
Read [lecture notes](LECTURE_NOTES.md) for the concept and [README](README.md) for setup.
The code and explanations are original companion material. Unsampled steps, exact constants,
and spoken explanations are not claimed to be verified. [Full research scope](../RESEARCH.md).
