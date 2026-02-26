# Scenario 06: Website Signup Guide

## The Story

Mountain Pine Coffee Roasters wants to set up an online ordering system using Square. But Sarah (who handles the website) is intimidated by the setup process:

- Multiple pages of settings
- Confusing options (what's "fulfillment"? "tax jurisdiction"?)
- Fear of clicking the wrong thing
- No one to ask questions to in real-time

Instead of spending hours figuring it out or paying someone $500 to set it up, she takes screenshots and has Claude guide her through it step by step.

---

## What the Learner Does

**Phase 1: Screenshot and Ask**
- Take a screenshot of the confusing page
- Ask Claude "What should I click? What does this mean?"

**Phase 2: Get Guided**
- Claude explains what each option means in plain English
- Claude recommends what to select based on the business
- Claude warns about settings that might cause problems

**Phase 3: Verify**
- Screenshot the next page
- Claude confirms or corrects
- Repeat until setup is complete

---

## Folder Structure

```
Mountain Pine Coffee Roasters/
    Website Setup/
        WEBSITE_GUIDE_PROMPT.md
        screenshots/
            screenshot_01.png      <- First confusing page
            screenshot_02.png      <- Next step
            ...
        output/
            setup_notes.md        <- Claude's explanations saved
```

---

## CC-Tools Showcased

| Tool | How It's Used |
|------|---------------|
| cc-image (implicit) | Claude sees and interprets screenshots |
| cc-browser (optional) | Could open browser for user to navigate |

This scenario primarily showcases Claude's **vision capability** - the ability to see and understand screenshots.

---

## What This Teaches

1. **Screenshot-based guidance** - Claude can see what you see
2. **Plain-English explanations** - Technical settings explained simply
3. **Context-aware advice** - Recommendations based on your specific business
4. **Safe exploration** - Get answers before clicking
5. **Learn while doing** - Understand the "why" not just the "what"

---

## Prompt Draft

```
I'm setting up Square Online for Mountain Pine Coffee Roasters.
This is a coffee roasting business that sells bags of coffee online
and needs to set up shipping for US orders.

I'm going to share screenshots of each page I encounter.
For each screenshot:

1. Explain what this page is for (in plain English, not tech jargon)
2. Tell me what I should select/enter based on my business
3. Warn me about any settings that could cause problems
4. Tell me what to click to continue

I'll take a new screenshot after each step so you can confirm
I'm on the right track.

Here's the first page: [screenshot]
```

---

## Example Interaction

**User shares screenshot of Square shipping settings:**

**Claude:**
```
This is Square's shipping settings page. Let me break it down:

**What it's asking:**
- "Fulfillment method" = How do you get products to customers?
- "Ship from" = Where you mail packages from

**What you should select:**
- Fulfillment: Choose "Shipping" (not pickup, since you're mailing coffee bags)
- Ship from address: Enter your roastery address in Pine Ridge
- Shipping carrier: Start with USPS - it's cheapest for packages under 1 lb

**Watch out for:**
- Don't enable "Local Delivery" unless you actually want to deliver
  yourself. That's different from USPS shipping.
- The "Calculated shipping" vs "Flat rate" choice: I'd recommend
  flat rate ($5.99 for 1-2 bags) - simpler for customers.

**Click Next:**
After filling in your address, click "Continue" in the bottom right.

Take a screenshot of the next page and I'll help with that one.
```

---

## Why This Scenario Matters

This is one of the most relatable use cases:

1. **Everyone has encountered confusing websites**
2. **No technical knowledge required** - just take screenshots
3. **Immediate practical value** - save time and money
4. **Builds confidence** - user learns while doing
5. **Shows Claude's vision** - many people don't know AI can see images

---

## Screenshots Needed

We'll create screenshots of a Square-like interface showing:

1. **Initial setup** - Business type selection
2. **Shipping settings** - Fulfillment options
3. **Tax settings** - Jurisdiction options
4. **Payment settings** - Processor connection
5. **Product setup** - Adding first product
6. **Checkout settings** - Customer options
7. **Domain/URL settings** - Website address

Each screenshot should look realistic but not actually be Square (to avoid trademark issues). We'll create a "Square-like" mockup.

---

## Alternative: Real Platform

Instead of creating fake screenshots, we could use a real platform:
- **Shopify** free trial
- **Stripe** dashboard (payment settings)
- **Google Workspace** admin console
- **Mailchimp** campaign setup

The learning is the same: Claude can guide you through any confusing interface.

---

## Expected Output

1. **Successful setup** - User completes Square Online configuration
2. **setup_notes.md** - Claude's explanations saved for reference
3. **Understanding** - User knows WHY they made each choice

---

## Success Criteria

After this scenario, learners can:
- Use screenshots to get guidance on any confusing website
- Understand that Claude can see and interpret images
- Get plain-English explanations of technical settings
- Navigate complex setup processes with confidence
- Know to ask Claude before clicking when unsure
