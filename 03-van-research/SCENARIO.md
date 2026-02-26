# Scenario 03: Van Research

## The Story

Mountain Pine Coffee Roasters needs a cargo van for their growing wholesale delivery operation. Instead of Marcus doing hours of research himself, he wants Claude to:

1. Interview him to understand exactly what he needs
2. Do the research based on his answers
3. Come back with a comparison including real local pricing

This is the "let Claude interview you first" approach.

---

## What the Learner Does

**Phase 1: Set Context**
- Briefly describe the business and van use case
- Tell Claude to interview them

**Phase 2: Get Interviewed**
- Claude asks questions one at a time
- Each question includes WHY Claude is asking
- User answers naturally
- Claude builds understanding

**Phase 3: Watch Claude Research**
- Claude uses cc-youtube-info for video reviews
- Claude uses cc-crawl4ai to find local dealers and pricing
- Claude searches for insurance and lease rates

**Phase 4: Review Output**
- Comparison spreadsheet with real numbers
- Recommendation based on interview answers

---

## Folder Structure

```
Mountain Pine Coffee Roasters/
    Van Research/
        VAN_RESEARCH_PROMPT.md
        output/
            (empty - Claude creates comparison here)
```

Minimal files - the interview replaces pre-written requirements.

---

## CC-Tools Showcased

| Tool | How It's Used |
|------|---------------|
| cc-youtube-info | Get transcripts from van review videos |
| cc-crawl4ai | Find local dealers, specs, pricing in Denver area |
| cc-markdown | Generate final comparison report |

---

## What This Teaches

1. **Interview mode** - Let Claude ask questions instead of dumping requirements
2. **Contextual questions** - Claude explains WHY it's asking each thing
3. **Live research** - Using cc-tools to get real, current data
4. **Local pricing** - Research specific to their area (Denver/Colorado)
5. **Decision-ready output** - Spreadsheet with all costs included

---

## Prompt Draft

```
I need help researching cargo vans for my business.

Here's the context:
- Business: Mountain Pine Coffee Roasters in Pine Ridge, Colorado (near Denver)
- We roast coffee and deliver wholesale to cafes and restaurants
- Currently doing 8 deliveries per week, growing to 15-20
- Need a van that can handle daily routes

Before you start researching, I want you to interview me. Ask me questions one at a time to understand exactly what I need.

For each question:
- Ask only ONE question
- Explain WHY you're asking (how it affects the van choice)
- Wait for my answer before asking the next question

When you have enough information, tell me you're ready to research.

Then:
1. Use cc-youtube-info to get reviews of the top van options
2. Use cc-crawl4ai to find dealers and pricing in the Denver/Colorado area
3. Research lease rates and insurance estimates for each option

Create a comparison spreadsheet with:
- Vehicle make/model/year
- Purchase price (local dealer)
- Monthly lease payment (if we lease instead)
- Estimated monthly insurance
- Fuel cost estimate (based on my routes)
- Total monthly cost of ownership

Save the comparison as Van_Comparison.xlsx and a summary report as Van_Recommendation.pdf using cc-markdown.
```

---

## Example Interview Questions Claude Might Ask

1. "What's your typical daily delivery route distance? (This affects whether fuel economy should be a priority and whether diesel makes sense for you.)"

2. "How much cargo space do you need per trip - are you delivering 50 lbs of coffee or 500 lbs? (This determines whether you need a full-size cargo van or if a smaller Transit Connect would work.)"

3. "Will you need to park in tight downtown spots, or mostly suburban areas with larger parking? (This affects whether the turning radius and overall size matter.)"

4. "Is climate control for the cargo area important - do your beans need to stay at a certain temperature? (Some vans offer insulated cargo areas or HVAC extensions.)"

5. "Are you planning to buy outright, lease, or finance? What's your budget range? (This changes which options I should focus on.)"

6. "How long do you plan to keep this van - 3 years, 5 years, 10 years? (This affects whether reliability and resale value should be weighted heavily.)"

7. "Will Marcus be the only driver, or will employees drive it too? (This affects insurance costs and whether you need commercial fleet insurance.)"

---

## Expected Output

1. **Interview transcript** - Shows Claude gathered requirements properly

2. **Van_Comparison.xlsx** - Spreadsheet with:
   | Vehicle | Local Price | Lease/mo | Insurance/mo | Fuel/mo | Total/mo |
   |---------|-------------|----------|--------------|---------|----------|
   | Ford Transit 250 | $42,500 | $650 | $180 | $320 | $1,150 |
   | Ram ProMaster 1500 | $38,900 | $580 | $165 | $340 | $1,085 |
   | ... | ... | ... | ... | ... | ... |

3. **Van_Recommendation.pdf** - Summary report with:
   - Top recommendation based on interview answers
   - Pros/cons of top 3 options
   - Local dealer info
   - Next steps

---

## Location Details

- **Business location:** Pine Ridge, Colorado (fictional, near Denver)
- **Delivery area:** Denver metro, Boulder, Fort Collins
- **Dealers to search:** Denver-area Ford, Ram, Mercedes, Chevrolet dealers
- **Insurance:** Colorado commercial vehicle rates

---

## Success Criteria

After this scenario, learners can:
- Use "interview mode" to have Claude gather requirements
- Understand why context matters for each question
- Use cc-youtube-info to extract video content
- Use cc-crawl4ai for local pricing research
- Get decision-ready output with real numbers
