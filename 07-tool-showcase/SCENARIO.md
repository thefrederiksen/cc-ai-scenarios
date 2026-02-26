# Scenario 07: Tool Showcase

## The Story

Marcus has heard Claude Code can do more than just answer questions. Someone mentioned "cc-tools" - that Claude can transcribe videos, generate PDFs, do web research, and more.

But he's skeptical. Instead of reading documentation, he wants a hands-on demo:

> "Show me what you can actually do. Give me a quick tour of the tools and let me see them in action."

This scenario walks through the key cc-tools with practical demonstrations.

---

## What the Learner Does

**Phase 1: Ask for the Tour**
- User asks Claude to demonstrate the available tools
- Claude explains what each tool does and offers to demo it

**Phase 2: Watch Live Demos**
- Each tool gets demonstrated with a real, practical example
- User sees actual output, not just descriptions

**Phase 3: Try It Yourself**
- User picks a tool and uses it for their own task
- Hands-on learning cements understanding

---

## Folder Structure

```
07-tool-showcase/
    SCENARIO.md
    demo_files/
        sample_video.mp4          <- Short video for cc-transcribe demo
        sample_webpage.txt        <- URL list for cc-crawl4ai demo
        sample_report.md          <- Markdown for cc-markdown demo
        sample_youtube_url.txt    <- YouTube URL for cc-youtube-info demo
    output/
        (empty - Claude creates demo outputs here)
```

---

## CC-Tools Showcased

| Tool | Demo Task | What User Sees |
|------|-----------|----------------|
| **cc-transcribe** | Transcribe a short video | Spoken words become text |
| **cc-markdown** | Convert markdown to PDF | Professional PDF appears |
| **cc-crawl4ai** | Scrape a webpage | Real content extracted |
| **cc-youtube-info** | Get video transcript | YouTube video -> searchable text |
| **cc-image-gen** | Generate a simple image | Prompt becomes visual |
| **cc-tts** | Convert text to speech | Written text becomes audio |
| **cc-ocr** | Read text from image | Photo becomes text |
| **cc-outlook** | List recent emails | Inbox contents displayed |

---

## What This Teaches

1. **Tool discovery** - See what's available before you need it
2. **Practical demos** - Understand through examples, not documentation
3. **Chaining potential** - See how tools can work together
4. **Confidence building** - Knowing what's possible enables creativity

---

## Prompt Draft

```
I've heard Claude Code has various tools it can use - for transcription, PDF generation, web scraping, etc.

Instead of reading documentation, can you give me a hands-on tour? I want to see each tool actually work, not just hear about it.

For each tool:
1. Tell me what it does in one sentence
2. Show me a quick demo (use the files in demo_files/ if needed)
3. Tell me when I'd actually use this

Start with the tools you think are most useful. Save any outputs to the output/ folder.

After the tour, I want to try one myself - so be ready to help me pick which tool to use for something I actually need.
```

---

## Demo Walkthrough

### Demo 1: cc-transcribe
**What it does:** Turns spoken audio/video into text.

```bash
cc-transcribe demo_files/sample_video.mp4 -o output/transcript.txt
```

**When to use:** Training videos, meeting recordings, interviews, podcasts.

---

### Demo 2: cc-markdown
**What it does:** Converts markdown files to professional PDFs with themes.

```bash
cc-markdown demo_files/sample_report.md -o output/sample_report.pdf --theme boardroom
```

**When to use:** Proposals, reports, documentation, client deliverables.

**Themes available:**
- `boardroom` - Corporate, executive
- `paper` - Minimal, clean
- `blueprint` - Technical documentation
- `terminal` - Developer style
- `thesis` - Academic
- `spark` - Creative
- `obsidian` - Dark mode

---

### Demo 3: cc-crawl4ai
**What it does:** Scrapes web pages and extracts content.

```bash
cc-crawl4ai "https://example.com" --output output/scraped_content.txt
```

**When to use:** Competitor research, gathering information, extracting data from websites.

---

### Demo 4: cc-youtube-info
**What it does:** Gets transcript and metadata from YouTube videos.

```bash
cc-youtube-info "https://youtube.com/watch?v=xxxxx"
```

**When to use:** Research, summarizing long videos, extracting key points from talks.

---

### Demo 5: cc-image-gen
**What it does:** Generates images from text descriptions.

```bash
cc-image-gen "A cozy coffee shop with warm lighting" -o output/coffee_shop.png
```

**When to use:** Marketing materials, social media, visualizing ideas.

---

### Demo 6: cc-tts
**What it does:** Converts text to natural-sounding speech.

```bash
cc-tts "Welcome to Mountain Pine Coffee Roasters" -o output/welcome.mp3
```

**When to use:** Phone greetings, presentations, accessibility.

---

### Demo 7: cc-ocr
**What it does:** Extracts text from images (receipts, signs, documents).

```bash
cc-ocr demo_files/receipt_photo.jpg
```

**When to use:** Receipts, business cards, handwritten notes, signs.

---

### Demo 8: cc-outlook
**What it does:** Reads your Outlook/Microsoft 365 email.

```bash
cc-outlook list --unread
cc-outlook read <message_id>
```

**When to use:** Processing inbox, finding specific emails, email summaries.

---

## Expected Output

After the tour, the output/ folder contains:
- `transcript.txt` - From cc-transcribe demo
- `sample_report.pdf` - From cc-markdown demo
- `scraped_content.txt` - From cc-crawl4ai demo
- `coffee_shop.png` - From cc-image-gen demo
- `welcome.mp3` - From cc-tts demo

Plus the user understands:
- What each tool does
- When to use each one
- How tools can be combined for complex tasks

---

## Demo Files Needed

### sample_video.mp4
Short (30-60 second) video of someone talking. Could be:
- Marcus explaining something about coffee
- A simple "hello this is a test" recording
- Audio-only MP4 is fine

### sample_report.md
A short markdown document to convert:
```markdown
# Q1 Sales Report

## Summary
Sales increased 15% compared to last quarter.

## Key Metrics
- Total revenue: $45,000
- New customers: 12
- Repeat orders: 85%

## Next Steps
- Expand delivery routes
- Launch subscription program
```

### sample_youtube_url.txt
A YouTube URL for a relevant video:
- **Demo Video:** https://www.youtube.com/watch?v=JYqfVE-fykk

---

## Chaining Demo (Bonus)

Show how tools work together:

```
Example: YouTube video -> Transcript -> Summary -> PDF

1. cc-youtube-info gets the transcript
2. Claude summarizes the key points
3. cc-markdown creates a professional PDF
```

This shows the real power - not individual tools, but workflows.

---

## Success Criteria

After this scenario, learners can:
- Name the main cc-tools and what they do
- Recognize which tool to use for common tasks
- Understand that Claude Code is a toolbox, not just a chatbot
- Feel confident trying tools for their own tasks
- See how to chain tools for complex workflows
