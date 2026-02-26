# Bookkeeping Task

Complete the 2025 bookkeeping for Mountain Pine Coffee Roasters.

Use `../2024/Bookkeeping 2024.xlsx` as a template for the format and categories.

## Tools for Reading Files

- **PDF files**: Use the Read tool directly
- **Image files (PNG, JPG)**: Use `cc-image ocr <filepath>` via Bash to extract text

## Error Handling

If any file fails to process (too large, corrupted, unreadable):
1. Log the filename and error to `FAILED_FILES.md`
2. Continue processing the remaining files
3. Do NOT stop the entire task for one failed file

## Instructions

### Phase 1: Extract Data

Process all folders:
- Bank Statements (start here for reference)
- Customer Invoices
- Receipts & Expenses
- To File

For each file, extract:
- Date
- Amount
- Vendor/Customer name
- Category (based on 2024 template categories)
- Any notes or invoice numbers

Save extracted data to `BOOKKEEPING_DATA.md` as you work.

### Phase 2: Organize

After all files are processed:
- Review extracted data for completeness
- Note any duplicates or misfiled documents
- Reconcile against bank statements

### Phase 3: Create Spreadsheet

Create `Bookkeeping 2025.xlsx` with the same structure as the 2024 template. Enter all transactions from your extracted data.

### Phase 4: Verify

Compare spreadsheet totals against bank statements. Flag anything that doesn't match:
- Missing receipts
- Duplicate entries
- Amounts that don't add up
