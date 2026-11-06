# Visual lecture review — lesson 25

Reviewed paused video frames in Brave at: [08:08](https://www.youtube.com/watch?v=PRPQIdKWYSo&t=488s), [18:19](https://www.youtube.com/watch?v=PRPQIdKWYSo&t=1099s), [28:30](https://www.youtube.com/watch?v=PRPQIdKWYSo&t=1710s), [36:39](https://www.youtube.com/watch?v=PRPQIdKWYSo&t=2199s).
This is a sampled visual review, not full viewing, audio analysis or a transcript.
The sample times were checked against the actual video player's time; unusable screenshots were excluded.

## What was visible

The sampled responses show HTTP 429 with Retry-After, and the lecture switches from a viewset to individual generic view routes.

## Vocabulary to recognize

`HTTP429`, `Retry-After`, `throttled`, `StudentList`, `StudentRetrieve`.

## How this project follows the lesson

Existing throttles demonstrate the limit. Explain that rates/cache scope are companion choices, since those settings are not visible in these samples.

## Try it in this project

Make repeated calls using the configured limits in [settings](config/settings.py) and [throttle classes](api/views.py). Inspect 429 and Retry-After. Development's process-local cache is not a distributed rate limiter; DRF throttling is not a DDoS defense.

## Reading the code

Each Python source has a `NOTES ABOUT THE COMPLETE CODE ABOVE` comment block below the code.
Read [lecture notes](LECTURE_NOTES.md) for the concept and [README](README.md) for setup.
The code and explanations are original companion material. Unsampled steps, exact constants,
and spoken explanations are not claimed to be verified. [Full research scope](../RESEARCH.md).
