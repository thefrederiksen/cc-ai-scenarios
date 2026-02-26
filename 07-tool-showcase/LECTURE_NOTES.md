# Lecture Notes: Tool Showcase

## Overview

This course demonstrates the cc-tools available in Claude Code through hands-on examples.

---

## Demo 1: YouTube Transcript Tool

We will use the YouTube tool to extract a transcript from a video.

**Video:** https://www.youtube.com/watch?v=JYqfVE-fykk

**Command:**
```bash
cc-youtube-info transcript "https://www.youtube.com/watch?v=JYqfVE-fykk" -o transcript.txt
```

**What this demonstrates:**
- Extracting transcripts from YouTube videos
- Converting video content to searchable text
- Foundation for summarization and analysis workflows

---

## Demo 2: cc-markdown (PDF Generation)

Convert markdown documents to professional PDFs.

**Command:**
```bash
cc-markdown sample_report.md -o report.pdf --theme boardroom
```

---

## Demo 3: cc-transcribe (Audio/Video Transcription)

Transcribe local audio and video files.

**Command:**
```bash
cc-transcribe video.mp4 -o transcript.txt
```

---

## Demo 4: cc-crawl4ai (Web Scraping)

Extract content from web pages.

**Command:**
```bash
cc-crawl4ai "https://example.com" --output content.txt
```

---

## Demo 5: cc-image-gen (Image Generation)

Generate images from text descriptions.

**Command:**
```bash
cc-image-gen "description of image" -o image.png
```

---

## Demo 6: cc-tts (Text to Speech)

Convert text to natural speech audio.

**Command:**
```bash
cc-tts "Your text here" -o audio.mp3
```

---

## Demo 7: cc-ocr (Optical Character Recognition)

Extract text from images.

**Command:**
```bash
cc-ocr image.jpg
```

---

## Key Takeaways

1. Claude Code is a toolbox, not just a chatbot
2. Tools can be chained together for complex workflows
3. Each tool has a specific purpose - learn when to use which
