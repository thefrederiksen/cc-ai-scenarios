"""
Generate 20 proposal PDFs for the Proposal Writer scenario.
12 "won" proposals with good characteristics
8 "lost" proposals with subtle flaws
"""

import subprocess
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent / "Mountain Pine Coffee Roasters" / "Proposals"
WON_DIR = BASE_DIR / "past_proposals" / "won"
LOST_DIR = BASE_DIR / "past_proposals" / "lost"
TEMP_DIR = BASE_DIR / ".temp"

# Create temp directory for markdown files
TEMP_DIR.mkdir(exist_ok=True)

# Won proposals - good structure, personalization, clear pricing, strong CTA
WON_PROPOSALS = [
    {
        "filename": "2023-03-alpine-bakery",
        "business": "Alpine Bakery",
        "contact": "Rachel",
        "location": "Arvada",
        "personal_hook": "I stopped by last week and loved your sourdough croissants - the perfect pairing for a good cup of coffee",
        "specific_need": "You mentioned wanting something that complements your pastries without overpowering them",
        "recommendation": "Summit Blend",
        "volume": "15 lbs/week",
        "price": "$9.50/lb",
    },
    {
        "filename": "2023-05-cedar-falls-cafe",
        "business": "Cedar Falls Cafe",
        "contact": "Tom and Lisa",
        "location": "Golden",
        "personal_hook": "Your location overlooking Clear Creek is amazing - what a spot for morning coffee",
        "specific_need": "With your outdoor seating crowd, you need something bold enough to pair with the mountain air",
        "recommendation": "Alpine Dark and Morning Trail",
        "volume": "25 lbs/week",
        "price": "$8.75/lb",
    },
    {
        "filename": "2023-08-mountain-view-diner",
        "business": "Mountain View Diner",
        "contact": "Frank",
        "location": "Lakewood",
        "personal_hook": "Your regulars clearly love the place - I saw three tables of folks who obviously come every morning",
        "specific_need": "Diner coffee needs to be consistent, affordable, and ready to refill - no fussy brewing",
        "recommendation": "Summit Blend in 5lb bags",
        "volume": "30 lbs/week",
        "price": "$8.00/lb",
    },
    {
        "filename": "2023-11-summit-coffee-house",
        "business": "Summit Coffee House",
        "contact": "Maya",
        "location": "Boulder",
        "personal_hook": "Love what you're doing with the local art on the walls - really builds that community feel",
        "specific_need": "Your crowd clearly knows their coffee - you need options for the adventurous drinkers",
        "recommendation": "Ethiopian Yirgacheffe and Guatemalan Antigua single origins",
        "volume": "20 lbs/week",
        "price": "$10.75/lb",
    },
    {
        "filename": "2024-01-pine-ridge-bistro",
        "business": "Pine Ridge Bistro",
        "contact": "Chef Daniel",
        "location": "Pine Ridge",
        "personal_hook": "We're practically neighbors! I drive past your place every day heading to the roastery",
        "specific_need": "Your farm-to-table concept deserves a roaster with the same local, small-batch philosophy",
        "recommendation": "Custom blend with your name on it",
        "volume": "15 lbs/week",
        "price": "$9.50/lb",
    },
    {
        "filename": "2024-02-riverside-restaurant",
        "business": "Riverside Restaurant",
        "contact": "James",
        "location": "LoDo Denver",
        "personal_hook": "Your dinner service is legendary but I hear the brunch is where coffee really shines",
        "specific_need": "High-end brunch crowd expects something special with their eggs benedict",
        "recommendation": "Ethiopian Yirgacheffe for pour-over, Summit Blend for espresso",
        "volume": "22 lbs/week",
        "price": "$9.50/lb average",
    },
    {
        "filename": "2024-04-valley-cafe",
        "business": "Valley Cafe",
        "contact": "Susan",
        "location": "Centennial",
        "personal_hook": "The way you've set up that reading nook is perfect - people settling in for the morning",
        "specific_need": "Your customers want to linger, which means lots of refills on that drip coffee",
        "recommendation": "Summit Blend - smooth enough for multiple cups",
        "volume": "28 lbs/week",
        "price": "$8.75/lb",
    },
    {
        "filename": "2024-06-hilltop-diner",
        "business": "Hilltop Diner",
        "contact": "Maria",
        "location": "Aurora",
        "personal_hook": "Your breakfast burritos have quite the reputation - had three people tell me to try them",
        "specific_need": "Fast-paced breakfast spot needs reliable, quick-brewing coffee that stands up to bold food",
        "recommendation": "Alpine Dark - bold enough for breakfast burritos",
        "volume": "35 lbs/week",
        "price": "$8.00/lb",
    },
    {
        "filename": "2024-08-lakeside-coffee",
        "business": "Lakeside Coffee",
        "contact": "Brian",
        "location": "Sloan's Lake Denver",
        "personal_hook": "That patio view of the lake is unbeatable - perfect spot to enjoy a morning cup",
        "specific_need": "Joggers and dog walkers need grab-and-go cold brew alongside sit-down espresso",
        "recommendation": "Morning Trail for cold brew, Summit for espresso",
        "volume": "40 lbs/week",
        "price": "$8.00/lb",
    },
    {
        "filename": "2024-09-woodland-cafe",
        "business": "Woodland Cafe",
        "contact": "Karen",
        "location": "Evergreen",
        "personal_hook": "The mountain town vibe is real - saw a guy bring his dog inside and nobody batted an eye",
        "specific_need": "Tourists and locals both want something that feels authentic mountain Colorado",
        "recommendation": "Colorado Custom Blend (we'll name it together)",
        "volume": "18 lbs/week",
        "price": "$9.50/lb",
    },
    {
        "filename": "2024-11-creekside-bakery",
        "business": "Creekside Bakery",
        "contact": "Emma",
        "location": "Littleton",
        "personal_hook": "Your chocolate croissants are dangerous - I may have had two while waiting to meet you",
        "specific_need": "Bakery coffee needs to complement, not compete with, the pastries",
        "recommendation": "Summit Blend - chocolate notes that pair with your baked goods",
        "volume": "12 lbs/week",
        "price": "$9.50/lb",
    },
    {
        "filename": "2025-01-boulder-brunch",
        "business": "Boulder Brunch Co",
        "contact": "Alex and Jordan",
        "location": "Boulder",
        "personal_hook": "The line out the door on Saturday says everything - you've built something special",
        "specific_need": "High volume weekend crowd plus health-conscious Boulder customers",
        "recommendation": "Organic options plus Swiss Water Decaf",
        "volume": "45 lbs/week",
        "price": "$8.00/lb",
    },
]

# Lost proposals - have subtle flaws
LOST_PROPOSALS = [
    {
        "filename": "2023-04-bigchain-coffee",
        "business": "BigChain Coffee",
        "contact": "Regional Manager",  # Too corporate
        "location": "Multiple Locations",
        "flaw": "too_generic",  # No personalization
    },
    {
        "filename": "2023-07-corporate-catering",
        "business": "Corporate Catering Solutions",
        "contact": "Procurement Department",
        "location": "Denver Tech Center",
        "flaw": "buried_pricing",  # Pricing unclear
    },
    {
        "filename": "2023-10-hotel-grand",
        "business": "The Grand Hotel",
        "contact": "Food & Beverage Director",
        "location": "Downtown Denver",
        "flaw": "weak_cta",  # No clear next step
    },
    {
        "filename": "2024-03-airport-cafe",
        "business": "Airport Express Cafe",
        "contact": "Operations Manager",
        "location": "DIA",
        "flaw": "too_formal",  # Stiff corporate tone
    },
    {
        "filename": "2024-05-convention-center",
        "business": "Convention Center Catering",
        "contact": "Catering Director",
        "location": "Colorado Convention Center",
        "flaw": "missing_sections",  # No delivery details
    },
    {
        "filename": "2024-07-stadium-concessions",
        "business": "Mile High Concessions",
        "contact": "Concessions Manager",
        "location": "Empower Field",
        "flaw": "too_generic",  # No understanding of their needs
    },
    {
        "filename": "2024-10-hospital-cafeteria",
        "business": "St. Luke's Hospital Cafeteria",
        "contact": "Dietary Services",
        "location": "Aurora",
        "flaw": "buried_pricing",  # Confusing pricing structure
    },
    {
        "filename": "2024-12-university-dining",
        "business": "CU Denver Dining Services",
        "contact": "Purchasing Coordinator",
        "location": "CU Denver Campus",
        "flaw": "weak_cta",  # Vague follow-up
    },
]


def generate_won_proposal(p):
    """Generate a good proposal with all the right elements."""
    return f"""# Coffee Partnership Proposal

## For {p['business']}

---

Dear {p['contact']},

{p['personal_hook']}. It was great chatting about your coffee needs, and I'm excited about the possibility of working together.

## About Mountain Pine Coffee Roasters

I'm Marcus Rivera, founder of Mountain Pine Coffee Roasters. We're a small-batch roastery right here in Pine Ridge, about 30 minutes from {p['location']}. I started this company because I was tired of seeing cafes served by roasters who treated them like account numbers. You deserve better than that.

What makes us different:
- **Freshness**: We roast Monday, Wednesday, and Friday - and deliver within 48 hours
- **Personal service**: I visit every wholesale partner monthly to make sure things are dialed in
- **Flexibility**: We adjust roast profiles based on your feedback, not ours

## My Recommendation for {p['business']}

{p['specific_need']}.

Based on our conversation, I'd recommend starting with **{p['recommendation']}**. Here's why this will work for your customers:

- It matches your menu style and customer expectations
- It's forgiving across different brew methods and barista skill levels
- Your customers will notice the upgrade

## Pricing

For your estimated volume of **{p['volume']}**, you'd be at our competitive pricing:

| Product | Price |
|---------|-------|
| {p['recommendation']} | {p['price']} |

Free delivery included for {p['location']}. No minimums. Net 15 terms.

That's straightforward pricing with no hidden fees.

## Getting Started

Here's what I'd like to do:

1. **This week**: I'll drop off a free 3 lb sample pack - no commitment
2. **Next week**: You and your team try it out
3. **When you're ready**: We set up weekly delivery on your schedule

No contracts. No minimums. If it's not working, we part as friends.

## Let's Talk

I'd love to stop by this week with samples. Does Thursday or Friday morning work for you?

Looking forward to it,

**Marcus Rivera**
Founder, Mountain Pine Coffee Roasters
(303) 555-7832
marcus@mountainpinecoffee.com
"""


def generate_lost_proposal(p):
    """Generate a flawed proposal based on the flaw type."""

    if p['flaw'] == 'too_generic':
        return f"""# Wholesale Coffee Proposal

## {p['business']}

To Whom It May Concern,

Mountain Pine Coffee Roasters is a coffee roasting company based in Colorado. We offer a variety of coffee products for wholesale customers.

## Our Products

We offer the following blends:
- Summit Blend
- Alpine Dark
- Morning Trail
- Various single origins

## Pricing

Our pricing is competitive. Contact us for a quote based on your volume.

## Delivery

We deliver to the Denver metro area.

## Contact

Please contact us if you are interested in our products.

Mountain Pine Coffee Roasters
info@mountainpinecoffee.com
"""

    elif p['flaw'] == 'buried_pricing':
        return f"""# Partnership Proposal

## For {p['business']}

Dear {p['contact']},

Thank you for your interest in Mountain Pine Coffee Roasters. We are pleased to present this proposal for your consideration.

## About Us

Mountain Pine Coffee Roasters has been serving the Colorado community since 2018. We pride ourselves on quality and freshness.

## Products

We offer a full range of coffee products including blends and single origins. Our most popular option is the Summit Blend, which features chocolate and caramel notes.

## Service Details

We can accommodate various delivery schedules. Our standard terms include weekly invoicing.

## Volume Considerations

Pricing varies based on several factors including volume, product selection, frequency of delivery, payment terms, seasonal adjustments, and promotional considerations. Our base pricing starts at $12.50/lb for small orders but various discounts may apply depending on circumstances. For example, orders over 25 lbs may qualify for tier 2 pricing, while orders over 50 lbs may qualify for tier 3 pricing. Additional discounts may be available for prepayment or annual commitments.

Please contact us for a detailed pricing structure specific to your needs.

## Next Steps

We look forward to discussing this further.

Best regards,
Marcus Rivera
"""

    elif p['flaw'] == 'weak_cta':
        return f"""# Coffee Partnership Proposal

## {p['business']}

Dear {p['contact']},

I'm reaching out from Mountain Pine Coffee Roasters regarding a potential partnership.

## About Us

We're a local Colorado roastery focused on freshness and quality. We roast small batches and deliver within 48 hours.

## What We Offer

- Premium coffee blends
- Single origin options
- Flexible delivery
- Competitive pricing at $8-10/lb depending on volume

## Why Choose Us

Many customers tell us our coffee is fresher than what they were getting before. We focus on relationships, not just transactions.

## Summary

Thank you for considering Mountain Pine Coffee Roasters. Coffee is an important part of any food service operation and we believe we could be a good fit.

Please let us know if you have any questions.

Best,
Marcus Rivera
"""

    elif p['flaw'] == 'too_formal':
        return f"""# WHOLESALE PARTNERSHIP PROPOSAL

## PREPARED FOR: {p['business']}
## PREPARED BY: Mountain Pine Coffee Roasters
## DATE: [Proposal Date]

---

### EXECUTIVE SUMMARY

This document constitutes a formal proposal for wholesale coffee supply services from Mountain Pine Coffee Roasters to {p['business']}.

### COMPANY OVERVIEW

Mountain Pine Coffee Roasters, LLC ("MPCR") is a Colorado-based coffee roasting enterprise established in 2018. MPCR maintains facilities at 1847 Industrial Way, Pine Ridge, CO 80470.

### PRODUCT SPECIFICATIONS

MPCR offers the following product categories:

1. Signature Blends (SKUs: SUM-001, ALP-001, MTR-001)
2. Single Origin Offerings (SKUs: COL-001, ETH-001, SUM-002, GUA-001)
3. Decaffeinated Options (SKU: DEC-001)

### PRICING STRUCTURE

Per-unit pricing is determined by aggregate weekly volume as follows:
- Tier I (10-25 units): $9.50 per unit
- Tier II (26-50 units): $8.75 per unit
- Tier III (51+ units): $8.00 per unit

### TERMS AND CONDITIONS

Standard payment terms: Net 15 from invoice date.
Delivery: Per mutually agreed upon schedule.
Minimum order quantity: 10 units per delivery instance.

### CONCLUSION

MPCR welcomes the opportunity to establish a commercial relationship with {p['business']}.

Respectfully submitted,
Marcus Rivera
Principal, Mountain Pine Coffee Roasters
"""

    else:  # missing_sections
        return f"""# Coffee Proposal

## For {p['business']}

Hi {p['contact']},

Thanks for taking my call yesterday. I'm excited about the possibility of working with {p['business']}.

## Our Coffee

We roast some great coffee here at Mountain Pine. Our Summit Blend is our most popular - it has chocolate and caramel notes that customers love. We also have darker options and single origins for the adventurous.

## Why We're Different

I started this company because I was frustrated with how stale most commercial coffee is. We roast three times a week and get it to you fast. You'll taste the difference.

## Samples

I'd love to bring you some samples to try. Just let me know when works.

Talk soon,
Marcus
"""


def main():
    print("Generating proposals...")

    # Generate won proposals
    for p in WON_PROPOSALS:
        md_path = TEMP_DIR / f"{p['filename']}.md"
        pdf_path = WON_DIR / f"{p['filename']}.pdf"

        content = generate_won_proposal(p)
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(content)

        # Convert to PDF
        result = subprocess.run(
            ['C:/cc-tools/cc-markdown.exe', str(md_path), '-o', str(pdf_path), '--theme', 'boardroom'],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            print(f"[!] Error generating {pdf_path}: {result.stderr}")
        else:
            print(f"[+] Generated: {pdf_path.name}")

    # Generate lost proposals
    for p in LOST_PROPOSALS:
        md_path = TEMP_DIR / f"{p['filename']}.md"
        pdf_path = LOST_DIR / f"{p['filename']}.pdf"

        content = generate_lost_proposal(p)
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(content)

        # Convert to PDF
        result = subprocess.run(
            ['C:/cc-tools/cc-markdown.exe', str(md_path), '-o', str(pdf_path), '--theme', 'boardroom'],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            print(f"[!] Error generating {pdf_path}: {result.stderr}")
        else:
            print(f"[+] Generated: {pdf_path.name}")

    print(f"\nGenerated {len(WON_PROPOSALS)} won proposals and {len(LOST_PROPOSALS)} lost proposals")


if __name__ == '__main__':
    main()
