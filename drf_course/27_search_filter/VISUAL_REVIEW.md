# Visual lecture review — lesson 27

Reviewed paused video frames in Brave at: [02:24](https://www.youtube.com/watch?v=746ar4atUB8&t=144s), [05:25](https://www.youtube.com/watch?v=746ar4atUB8&t=325s), [08:26](https://www.youtube.com/watch?v=746ar4atUB8&t=506s), [10:50](https://www.youtube.com/watch?v=746ar4atUB8&t=650s).
This is a sampled visual review, not full viewing, audio analysis or a transcript.
The sample times were checked against the actual video player's time; unusable screenshots were excluded.

## What was visible

The view uses SearchFilter and search_fields=['city']; the browser requests a search for Bokaro and shows matching students.

## Vocabulary to recognize

`SearchFilter`, `search_fields`, `search`, `city`, `Bokaro`.

## How this project follows the lesson

The companion searches both name and city, an explicit extension. Compare ?search=Ranchi with exact filtering from lesson 26.

## Try it in this project

Try `/api/students/?search=Ranchi` and a partial name. [views.py](api/views.py) searches name and city; the sampled view only searched city. SearchFilter's default is case-insensitive contains matching.

## Reading the code

Each Python source has a `NOTES ABOUT THE COMPLETE CODE ABOVE` comment block below the code.
Read [lecture notes](LECTURE_NOTES.md) for the concept and [README](README.md) for setup.
The code and explanations are original companion material. Unsampled steps, exact constants,
and spoken explanations are not claimed to be verified. [Full research scope](../RESEARCH.md).
