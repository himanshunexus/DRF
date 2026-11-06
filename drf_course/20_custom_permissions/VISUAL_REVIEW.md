# Visual lecture review — lesson 20

Reviewed paused video frames in Brave at: [02:41](https://www.youtube.com/watch?v=UUts-Bmh6w0&t=161s), [06:03](https://www.youtube.com/watch?v=UUts-Bmh6w0&t=363s), [09:24](https://www.youtube.com/watch?v=UUts-Bmh6w0&t=564s), [12:06](https://www.youtube.com/watch?v=UUts-Bmh6w0&t=726s).
This is a sampled visual review, not full viewing, audio analysis or a transcript.
The sample times were checked against the actual video player's time; unusable screenshots were excluded.

## What was visible

The code moves from SessionAuthentication/IsAuthenticated to an imported MyPermission class. The sampled frames do not show that custom class's implementation.

## Vocabulary to recognize

`MyPermission`, `custompermissions`, `permission_classes`, `SessionAuthentication`.

## How this project follows the lesson

The companion's IsStaffOrReadOnly is an explicitly original policy, not a reconstruction of the unseen MyPermission body.

## Try it in this project

Read [permissions.py](api/permissions.py). IsStaffOrReadOnly permits safe reads and restricts writes to staff. This is our documented exercise policy; the sampled frames only establish the instructor's MyPermission name, not its body.

## Reading the code

Each Python source has a `NOTES ABOUT THE COMPLETE CODE ABOVE` comment block below the code.
Read [lecture notes](LECTURE_NOTES.md) for the concept and [README](README.md) for setup.
The code and explanations are original companion material. Unsampled steps, exact constants,
and spoken explanations are not claimed to be verified. [Full research scope](../RESEARCH.md).
