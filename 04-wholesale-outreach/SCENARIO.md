# Scenario 04: Wholesale Outreach

## The Story

Mountain Pine Coffee Roasters wants to grow from 8 wholesale customers to 25+. They have a list of potential cafes and restaurants in the Denver area.

Before reaching out, they need:
1. A clear message template - what are we offering and why choose us?
2. Research on each prospect
3. Personalized emails that combine the template with what we learned

---

## What the Learner Does

1. Define the outreach template (goal + 2 key value props)
2. Research prospects using cc-crawl4ai
3. Write personalized emails combining template + research
4. Queue emails for approval via cc-comm-queue
5. Track outreach in a spreadsheet

---

## Folder Structure

```
Mountain Pine Coffee Roasters/
    Wholesale Outreach/
        OUTREACH_PROMPT.md
        outreach_template.md        <- Core message + value props
        prospect_list.csv           <- 20-30 businesses
        research/                   <- Claude fills with notes
        drafts/                     <- Claude creates emails here
        our_story.txt
        pricing_wholesale.pdf
```

---

## The Outreach Template

```markdown
# Mountain Pine Wholesale Outreach Template

## Goal
Get local cafes and restaurants to switch to our coffee or add us as a supplier.

## Our Core Message
We're a local Colorado roaster offering fresh, small-batch coffee delivered weekly.

## Two Key Value Props

**1. Freshness**
We roast 3x per week and deliver within 48 hours of roasting.
Big distributors ship coffee that's already weeks old.
Your customers taste the difference.

**2. Local Partnership**
We're not a faceless supplier. Marcus personally visits every
wholesale customer monthly. We adjust roast profiles based on
your feedback. We're invested in your success.

## What We're Offering
- Free sample pack (3 lbs) to try our beans
- No minimum commitment to start
- Free delivery in Denver metro area
- Flexible ordering (adjust weekly based on your needs)

## Call to Action
Would you be open to trying a sample? I can drop some off this week.
```

---

## CC-Tools Showcased

| Tool | Purpose |
|------|---------|
| cc-crawl4ai | Research each prospect's website |
| cc-comm-queue | Queue emails for human approval |

---

## What This Teaches

1. **Template + Personalization** - Have a core message, customize per prospect
2. **Value props first** - Know your 2 key selling points before outreach
3. **Research before writing** - Personalization based on real info
4. **Safe email workflow** - Never send without human approval

---

## Prompt Draft

```
Help me with wholesale outreach for Mountain Pine Coffee Roasters.

First, read our outreach template in outreach_template.md. This has:
- Our goal
- Our two key value propositions
- What we're offering
- Our call to action

Then read prospect_list.csv.

For each prospect:

1. Use cc-crawl4ai to visit their website
2. Note: What kind of place? What vibe? Do they mention their coffee?
3. Save notes to research/[business_name].txt

For the top 10 most promising prospects:

4. Write a personalized email that:
   - Uses our core message and value props from the template
   - Adds 1-2 sentences specific to THEIR business
   - Keeps the same call to action

5. Save each draft to drafts/[business_name].txt

6. Queue each email using cc-comm-queue for my approval

Create a tracking spreadsheet: Prospect, Website, Researched, Email Drafted, Status
```

---

## Generation Needed

1. **outreach_template.md** - As shown above

2. **prospect_list.csv**
   ```
   business_name,contact_name,email,website,type,notes
   The Daily Grind,Mike Thompson,mike@dailygrind.com,dailygrind.com,cafe,Downtown
   Sunrise Bakery,,,sunrisebakery.com,bakery,No email found
   ...
   ```
   - 20-30 entries
   - Mix: cafes, restaurants, bakeries, offices

3. **our_story.txt** - Company background

4. **pricing_wholesale.pdf** - Pricing tiers

---

## Example Personalized Email

```
Subject: Fresh-roasted coffee for The Daily Grind?

Hi Mike,

I saw you recently added pour-over to your menu - great choice for
a downtown crowd that appreciates good coffee.

I'm Marcus from Mountain Pine Coffee Roasters. We're a local Colorado
roaster, and I think we could be a great fit for The Daily Grind.

Two things that set us apart:

1. Freshness - We roast 3x per week and deliver within 48 hours.
   Your customers will taste the difference vs. coffee that's been
   sitting in a warehouse.

2. Local partnership - I personally visit every wholesale customer
   monthly. We'll dial in the roast profile based on your feedback.

Would you be open to trying a sample? I can drop off a few pounds
this week - no commitment, just want you to taste the difference.

Marcus Rivera
Mountain Pine Coffee Roasters
```

---

## Success Criteria

After this scenario, learners can:
- Create a reusable outreach template with clear value props
- Use cc-crawl4ai to research prospects
- Combine template + personalization for each email
- Use cc-comm-queue for safe email approval
- Understand "template + customize" pattern for outreach at scale
