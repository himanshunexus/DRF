# Visual lecture review — lesson 30

Reviewed paused video frames in Brave at: [02:35](https://www.youtube.com/watch?v=wTFjIXlduVs&t=155s), [05:49](https://www.youtube.com/watch?v=wTFjIXlduVs&t=349s), [09:03](https://www.youtube.com/watch?v=wTFjIXlduVs&t=543s), [11:39](https://www.youtube.com/watch?v=wTFjIXlduVs&t=699s).
This is a sampled visual review, not full viewing, audio analysis or a transcript.
The sample times were checked against the actual video player's time; unusable screenshots were excluded.

## What was visible

MyLimitOffsetPagination is selected by pagination_class. The final sample sets default_limit=5, mylimit/myoffset query names and max_limit=3.

## Vocabulary to recognize

`MyLimitOffsetPagination`, `LimitOffsetPagination`, `default_limit`, `mylimit`, `myoffset`, `max_limit`.

## How this project follows the lesson

Added the same query names, with default_limit=3 and max_limit=3 so the default does not exceed the cap. Main route retains limit/offset.

## Try it in this project

Try `/api/practice/pagination/?mylimit=2&myoffset=2`; then request mylimit=99 and observe the cap of 3. [mypaginations.py](api/mypaginations.py) keeps the default inside that cap. The original route uses limit/offset.

## Reading the code

Each Python source has a `NOTES ABOUT THE COMPLETE CODE ABOVE` comment block below the code.
Read [lecture notes](LECTURE_NOTES.md) for the concept and [README](README.md) for setup.
The code and explanations are original companion material. Unsampled steps, exact constants,
and spoken explanations are not claimed to be verified. [Full research scope](../RESEARCH.md).
