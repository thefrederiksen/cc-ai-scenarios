# Scenario 05: Training Video

## The Story

Mountain Pine Coffee Roasters has a problem: Marcus is the only one who knows how to calibrate the roasting equipment. Every time he's sick or on vacation, production stops.

He recorded a 15-minute video of himself explaining the calibration process, but:
- Nobody wants to watch a video every time
- Can't search a video for "what temperature for Ethiopian beans?"
- New hires need a written manual they can reference

He wants to turn that video into proper training documentation.

---

## What the Learner Does

**Phase 1: Transcribe**
- Use cc-transcribe to extract the spoken content
- Get accurate timestamps for each section

**Phase 2: Structure**
- Claude organizes the rambling video into logical sections
- Identifies steps, warnings, and tips
- Creates a proper training document

**Phase 3: Polish**
- Use cc-markdown to create a professional PDF manual
- Include a quick-reference checklist version

---

## Folder Structure

```
Mountain Pine Coffee Roasters/
    Training/
        TRAINING_PROMPT.md
        videos/
            roaster_calibration.mp4       <- The raw training video
        output/
            (empty - Claude creates docs here)
```

---

## CC-Tools Showcased

| Tool | How It's Used |
|------|---------------|
| cc-transcribe | Convert video speech to text with timestamps |
| cc-markdown | Create professional PDF training manual |

### cc-transcribe Deep Dive

```bash
# Basic transcription
cc-transcribe videos/roaster_calibration.mp4

# Output to file
cc-transcribe videos/roaster_calibration.mp4 -o transcript.txt

# With timestamps (useful for longer videos)
cc-transcribe videos/roaster_calibration.mp4 --timestamps
```

---

## What This Teaches

1. **Video to documentation** - Turn any recording into usable training material
2. **Structure extraction** - Claude organizes messy spoken content
3. **Multi-format output** - Same content as full manual + quick reference
4. **Knowledge preservation** - Get critical knowledge out of people's heads

---

## Prompt Draft

```
I have a training video where Marcus explains how to calibrate our coffee roaster.
I need to turn this into proper training documentation.

Step 1: Transcribe the video
Use cc-transcribe on videos/roaster_calibration.mp4

Step 2: Create Training Manual
Turn the transcript into a structured training document:
- Add clear section headings
- Number all steps
- Highlight safety warnings (anything about burns, heat, timing)
- Note any tips or best practices Marcus mentions
- Remove filler words and rambling - make it clean
- Keep Marcus's voice/personality where it helps

Save as output/Roaster_Calibration_Manual.md

Step 3: Create Quick Reference
Make a 1-page checklist version:
- Just the numbered steps
- Key temperatures/times
- Common troubleshooting
- No explanations - just the essentials

Save as output/Roaster_Calibration_Checklist.md

Step 4: Generate PDFs
Use cc-markdown to create professional versions:
- cc-markdown output/Roaster_Calibration_Manual.md -o output/Roaster_Calibration_Manual.pdf --theme blueprint
- cc-markdown output/Roaster_Calibration_Checklist.md -o output/Roaster_Calibration_Checklist.pdf --theme blueprint
```

---

## The Training Video Content

Marcus rambles naturally (as real people do). The video covers:

1. **Pre-check** (2 min)
   - "So first thing, always check the gas line..."
   - Safety warnings about burns
   - Checking the thermocouple

2. **Initial Calibration** (5 min)
   - Setting the drum temperature
   - Why Ethiopian beans need different settings than Brazilian
   - Common mistakes ("I see new guys do this all the time...")

3. **Test Roast** (4 min)
   - Running a small test batch
   - What to listen for (first crack, second crack)
   - How to adjust based on results

4. **Daily vs Weekly Calibration** (2 min)
   - Quick daily checks
   - Full weekly calibration process

5. **Troubleshooting** (2 min)
   - "If the temperature keeps drifting..."
   - When to call for service

---

## Expected Output

1. **Roaster_Calibration_Manual.md/.pdf** (5-8 pages)
   - Clean, structured training document
   - All steps numbered
   - Safety warnings highlighted
   - Tips preserved

2. **Roaster_Calibration_Checklist.md/.pdf** (1 page)
   - Quick reference for daily use
   - Just the steps, no explanations
   - Fits on one laminated page

---

## Generation Needed

### The Video File

We need to generate a realistic training video. Options:

**Option A: Audio only (simpler)**
- Generate an MP4 with just audio
- Marcus narrating the calibration process
- 10-15 minutes of natural, conversational speech

**Option B: Stock footage + audio (better)**
- Use stock footage of coffee roasting
- Overlay with generated narration
- More realistic training video feel

For now, we'll create an audio file with timestamps that cc-transcribe can process.

### Marcus's Speaking Style

Realistic "training video" speech patterns:
- "Okay so..."
- "The thing is..."
- "A lot of people don't realize..."
- "What I always tell new guys is..."
- Occasional tangents
- Safety warnings ("Now be careful here, this is hot")
- Personal anecdotes ("I learned this the hard way back in...")

---

## Success Criteria

After this scenario, learners can:
- Use cc-transcribe to extract spoken content
- Turn unstructured video into structured documentation
- Create multiple document formats from the same source
- Understand the "record -> transcribe -> document" workflow
- See how AI preserves institutional knowledge
