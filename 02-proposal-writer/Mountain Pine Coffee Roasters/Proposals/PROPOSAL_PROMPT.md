# Proposal Writer Task

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
```
cc-markdown completed/riverside_cafe_proposal.md -o completed/Riverside_Cafe_Proposal.pdf --theme boardroom
```
