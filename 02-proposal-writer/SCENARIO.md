# Scenario 02: Proposal Writer

## The Story

Mountain Pine Coffee Roasters has been writing wholesale proposals for 2 years. Marcus has a folder of 20 past proposals - some won, some lost - but he writes each one from scratch every time.

Now Riverside Cafe is asking for a proposal, and Marcus wants to:
1. Figure out what makes his winning proposals work
2. Create a reusable template from his best work
3. Automate writing new proposals based on that template

This is the "learn from my past work" use case.

---

## What the Learner Does

**Phase 1: Analyze**
- Review 20 past proposals
- Identify patterns in structure, tone, what works
- Extract a template

**Phase 2: Generate**
- Read the new inquiry from Riverside Cafe
- Use the extracted template to write a proposal
- Personalize it for Riverside

**Phase 3: Polish**
- Convert to professional PDF using cc-markdown
- Use boardroom theme for business look

---

## Folder Structure

```
Mountain Pine Coffee Roasters/
    Proposals/
        PROPOSAL_PROMPT.md
        past_proposals/
            won/
                2023-03-alpine-bakery.pdf
                2023-05-cedar-falls-cafe.pdf
                2023-08-mountain-view-diner.pdf
                2023-11-summit-coffee-house.pdf
                2024-01-pine-ridge-bistro.pdf
                2024-02-riverside-restaurant.pdf
                2024-04-valley-cafe.pdf
                2024-06-hilltop-diner.pdf
                2024-08-lakeside-coffee.pdf
                2024-09-woodland-cafe.pdf
                2024-11-creekside-bakery.pdf
                2025-01-boulder-brunch.pdf
            lost/
                2023-04-bigchain-coffee.pdf
                2023-07-corporate-catering.pdf
                2023-10-hotel-grand.pdf
                2024-03-airport-cafe.pdf
                2024-05-convention-center.pdf
                2024-07-stadium-concessions.pdf
                2024-10-hospital-cafeteria.pdf
                2024-12-university-dining.pdf
        company_info/
            our_story.txt
            product_catalog.txt
            wholesale_pricing.txt
            delivery_zones.txt
        inquiries/
            riverside_cafe_email.txt
        templates/
            (empty - Claude extracts template here)
        completed/
            (empty - Claude creates proposals here)
```

---

## CC-Tools Showcased

| Tool | How It's Used | Why It Matters |
|------|---------------|----------------|
| **cc-markdown** | Convert proposal.md to proposal.pdf | THE STAR - turns plain text into professional PDF |

### cc-markdown Deep Dive

```bash
# Basic conversion
cc-markdown proposal.md -o proposal.pdf

# With professional theme (what we'll use)
cc-markdown proposal.md -o proposal.pdf --theme boardroom

# Available themes for different vibes:
#   boardroom - corporate, executive (USE THIS)
#   paper     - minimal, clean
#   terminal  - technical, developer
#   blueprint - technical documentation
#   thesis    - academic
#   spark     - creative, colorful
#   obsidian  - dark theme
```

---

## What This Teaches

1. **Learning from past work** - Your existing documents are training data
2. **Pattern extraction** - Claude can identify what makes your work "yours"
3. **Template creation** - Codify your best practices into a reusable format
4. **Automated generation** - Apply your style to new situations
5. **Professional output** - cc-markdown for polished final product

---

## Prompt Draft

```
Help me create a proposal system for Mountain Pine Coffee Roasters.

## Phase 1: Analyze My Past Proposals

Read all proposals in past_proposals/won/ and past_proposals/lost/

Analyze them and answer:
1. What structure do my winning proposals follow?
2. What tone/language patterns do I use?
3. What do winning proposals have that losing ones don't?
4. What sections are always included?

Create a template based on my winning proposals and save it as:
templates/proposal_template.md

## Phase 2: Write New Proposal

Read the inquiry from Riverside Cafe in inquiries/riverside_cafe_email.txt

Read our current info:
- company_info/our_story.txt
- company_info/product_catalog.txt
- company_info/wholesale_pricing.txt
- company_info/delivery_zones.txt

Using the template you extracted, write a proposal for Riverside Cafe.
Save as: completed/riverside_cafe_proposal.md

## Phase 3: Create PDF

Convert to professional PDF:
cc-markdown completed/riverside_cafe_proposal.md -o completed/Riverside_Cafe_Proposal.pdf --theme boardroom
```

---

## Generation Needed

### Past Proposals (20 total)

**Won proposals (12)** - These should:
- Have consistent structure
- Personal touches (mention specific things about the cafe)
- Clear pricing
- Strong calls to action
- Warm, relationship-focused tone

**Lost proposals (8)** - These should have subtle flaws:
- Too generic (no personalization)
- Buried pricing or unclear terms
- Weak calls to action
- Too formal/corporate tone
- Missing sections

### Proposal Content Pattern

Each proposal should be 1-2 pages covering:
- Greeting with something specific about their business
- Brief "about us"
- Recommended products for their needs
- Pricing for their volume
- Delivery terms
- Next steps / call to action

### Supporting Files

Same as before:
- riverside_cafe_email.txt (the new inquiry)
- our_story.txt
- product_catalog.txt
- wholesale_pricing.txt
- delivery_zones.txt

---

## Expected Output

1. **Extracted template** - templates/proposal_template.md
   - Shows Claude identified the winning pattern

2. **New proposal** - completed/riverside_cafe_proposal.md
   - Follows the extracted template
   - Personalized for Riverside Cafe

3. **Professional PDF** - completed/Riverside_Cafe_Proposal.pdf
   - Boardroom theme
   - Ready to email

---

## Success Criteria

After this scenario, learners can:
- Use their past work as training data for Claude
- Extract patterns and templates from existing documents
- Generate new documents that match their established style
- Understand the "learn from examples -> generate new" workflow
- Use cc-markdown for professional output
