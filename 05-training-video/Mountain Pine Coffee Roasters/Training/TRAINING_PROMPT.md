# Training Video to Documentation Task

I have a training video where Marcus explains how to calibrate our coffee roaster.
I need to turn this into proper training documentation.

## Step 1: Transcribe the Video

Use cc-transcribe on `videos/roaster_calibration.mp4`

```bash
cc-transcribe videos/roaster_calibration.mp4 -o transcript.txt
```

## Step 2: Create Training Manual

Turn the transcript into a structured training document:
- Add clear section headings
- Number all steps
- Highlight safety warnings (anything about burns, heat, timing)
- Note any tips or best practices Marcus mentions
- Remove filler words and rambling - make it clean
- Keep Marcus's voice/personality where it helps

Save as `output/Roaster_Calibration_Manual.md`

## Step 3: Create Quick Reference

Make a 1-page checklist version:
- Just the numbered steps
- Key temperatures/times
- Common troubleshooting
- No explanations - just the essentials

Save as `output/Roaster_Calibration_Checklist.md`

## Step 4: Generate PDFs

Use cc-markdown to create professional versions:

```bash
cc-markdown output/Roaster_Calibration_Manual.md -o output/Roaster_Calibration_Manual.pdf --theme blueprint
cc-markdown output/Roaster_Calibration_Checklist.md -o output/Roaster_Calibration_Checklist.pdf --theme blueprint
```
