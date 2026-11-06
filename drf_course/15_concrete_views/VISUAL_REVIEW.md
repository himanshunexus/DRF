# Visual lecture review — lesson 15

Reviewed paused video frames in Brave at: [06:31](https://www.youtube.com/watch?v=p45ZPhYUR2w&t=391s), [14:41](https://www.youtube.com/watch?v=p45ZPhYUR2w&t=881s), [22:50](https://www.youtube.com/watch?v=p45ZPhYUR2w&t=1370s), [29:22](https://www.youtube.com/watch?v=p45ZPhYUR2w&t=1762s).
This is a sampled visual review, not full viewing, audio analysis or a transcript.
The sample times were checked against the actual video player's time; unusable screenshots were excluded.

## What was visible

The lecture shows separate StudentList, StudentCreate and StudentRetrieve classes before combined ListCreateAPIView and RetrieveUpdateDestroyAPIView classes. URL examples switch between the variants.

## Vocabulary to recognize

`ListAPIView`, `CreateAPIView`, `RetrieveAPIView`, `ListCreateAPIView`, `RetrieveUpdateDestroyAPIView`, `StudentListCreate`.

## How this project follows the lesson

Add single-operation concrete views with separate practice URLs, preserving the existing combined CRUD endpoint.

## Try it in this project

Compare [single_views.py](api/single_views.py) against lesson 14. ListAPIView/CreateAPIView already contain the verb handlers. Try the same `/api/practice/` routes, then use the combined `/api/students/` interface.

## Reading the code

Each Python source has a `NOTES ABOUT THE COMPLETE CODE ABOVE` comment block below the code.
Read [lecture notes](LECTURE_NOTES.md) for the concept and [README](README.md) for setup.
The code and explanations are original companion material. Unsampled steps, exact constants,
and spoken explanations are not claimed to be verified. [Full research scope](../RESEARCH.md).
