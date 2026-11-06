# Visual lecture review — lesson 29

Reviewed paused video frames in Brave at: [06:36](https://www.youtube.com/watch?v=CNcca44LEBE&t=396s), [14:51](https://www.youtube.com/watch?v=CNcca44LEBE&t=891s), [23:06](https://www.youtube.com/watch?v=CNcca44LEBE&t=1386s), [29:42](https://www.youtube.com/watch?v=CNcca44LEBE&t=1782s).
This is a sampled visual review, not full viewing, audio analysis or a transcript.
The sample times were checked against the actual video player's time; unusable screenshots were excluded.

## What was visible

MyPageNumberPagination has page_size=5, then page_query_param='p' and page_size_query_param='records'. A slide covers maximum page size and last-page strings.

## Vocabulary to recognize

`MyPageNumberPagination`, `PageNumberPagination`, `page_size`, `page_query_param`, `page_size_query_param`, `max_page_size`.

## How this project follows the lesson

Added a practice endpoint with p/records and page size 5. The cap of 10 is our bounded companion setting; the original route retains page/page_size.

## Try it in this project

Read [mypaginations.py](api/mypaginations.py). Try `/api/practice/pagination/?p=1&records=2`, follow next, then request `p=last`. The original `/api/students/` retains page/page_size so you can compare conventions.

## Reading the code

Each Python source has a `NOTES ABOUT THE COMPLETE CODE ABOVE` comment block below the code.
Read [lecture notes](LECTURE_NOTES.md) for the concept and [README](README.md) for setup.
The code and explanations are original companion material. Unsampled steps, exact constants,
and spoken explanations are not claimed to be verified. [Full research scope](../RESEARCH.md).
