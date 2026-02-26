"""
Create Bookkeeping 2025.xlsx for Mountain Pine Coffee Roasters
"""
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side, PatternFill
from openpyxl.utils import get_column_letter
from datetime import datetime

# Create workbook
wb = openpyxl.Workbook()

# Define styles
header_font = Font(bold=True)
header_fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
header_font_white = Font(bold=True, color="FFFFFF")
currency_format = '"$"#,##0.00'
date_format = 'MM/DD/YYYY'
thin_border = Border(
    left=Side(style='thin'),
    right=Side(style='thin'),
    top=Side(style='thin'),
    bottom=Side(style='thin')
)

# ============ TRANSACTIONS SHEET ============
ws_trans = wb.active
ws_trans.title = "Transactions"

# Headers
trans_headers = ["Date", "Type", "Category", "Vendor/Customer", "Description",
                 "Reference", "Income", "Expense", "Balance", "Tax Deductible", "Notes", "Bank Matched"]
for col, header in enumerate(trans_headers, 1):
    cell = ws_trans.cell(row=1, column=col, value=header)
    cell.font = header_font_white
    cell.fill = header_fill
    cell.alignment = Alignment(horizontal='center')

# Bank statement transactions (extracted from PDFs)
bank_transactions = [
    # January 2025
    ("2025-01-01", "Opening", "Opening Balance", "", "Opening Balance from 2024", "", 0, 0, 15420.00, "N", "From bank statement", "Y"),
    ("2025-01-03", "Expense", "Cost of Goods Sold", "Pacific Coffee Importers", "Check #1042 - Green coffee beans", "CHK-1042", 0, 1705.00, 13715.00, "Y", "", "Y"),
    ("2025-01-05", "Income", "Retail Sales", "Online Customer", "Online Sale", "RET-2025-001", 47.74, 0, 13762.74, "N", "", "Y"),
    ("2025-01-06", "Expense", "Internet & Phone", "Xfinity Business", "Autopay - Internet/Phone", "AUTO", 0, 128.99, 13633.75, "Y", "", "Y"),
    ("2025-01-07", "Expense", "Vehicle & Fuel", "Shell Gas Station", "POS Purchase - Fuel", "POS", 0, 46.72, 13587.03, "Y", "", "Y"),
    ("2025-01-07", "Income", "Retail Sales", "Online Customer", "Online Sale", "RET-2025-002", 39.17, 0, 13626.20, "N", "", "Y"),
    ("2025-01-08", "Expense", "Packaging & Supplies", "PackagingPro Supply", "POS Purchase - Packaging", "POS", 0, 284.34, 13341.86, "Y", "", "Y"),
    ("2025-01-09", "Income", "Retail Sales", "Online Customer", "Online Sale", "RET-2025-003", 95.85, 0, 13437.71, "N", "", "Y"),
    ("2025-01-10", "Expense", "Utilities", "Boulder Electric Co.", "Autopay - Electric", "AUTO", 0, 198.45, 13239.26, "Y", "", "Y"),
    ("2025-01-12", "Expense", "Shipping & Delivery", "UPS Store", "POS Purchase - Shipping", "POS", 0, 90.12, 13149.14, "Y", "", "Y"),
    ("2025-01-12", "Income", "Retail Sales", "Online Customer", "Online Sale", "RET-2025-004", 53.64, 0, 13202.78, "N", "", "Y"),
    ("2025-01-14", "Expense", "Vehicle & Fuel", "Shell Gas Station", "POS Purchase - Fuel", "POS", 0, 51.35, 13151.43, "Y", "", "Y"),
    ("2025-01-14", "Income", "Retail Sales", "Online Customer", "Online Sale", "RET-2025-005", 39.68, 0, 13191.11, "N", "", "Y"),
    ("2025-01-15", "Expense", "Office Supplies", "Office Depot", "POS Purchase - Office supplies", "POS", 0, 109.42, 13081.69, "Y", "", "Y"),
    ("2025-01-17", "Expense", "Cost of Goods Sold", "Pacific Coffee Importers", "Check #1043 - Green coffee beans", "CHK-1043", 0, 1540.00, 11541.69, "Y", "", "Y"),
    ("2025-01-17", "Income", "Retail Sales", "Online Customer", "Online Sale", "RET-2025-006", 39.16, 0, 11580.85, "N", "", "Y"),
    ("2025-01-18", "Income", "Wholesale", "The Daily Grind Cafe", "Deposit - Wholesale order", "INV", 386.00, 0, 11966.85, "N", "", "Y"),
    ("2025-01-19", "Income", "Retail Sales", "Online Customer", "Online Sale", "RET-2025-007", 60.61, 0, 12027.46, "N", "", "Y"),
    ("2025-01-21", "Expense", "Vehicle & Fuel", "Shell Gas Station", "POS Purchase - Fuel", "POS", 0, 43.07, 11984.39, "Y", "", "Y"),
    ("2025-01-22", "Income", "Wholesale", "Sunrise Espresso Bar", "Deposit - Wholesale order", "INV", 304.00, 0, 12288.39, "N", "", "Y"),
    ("2025-01-22", "Income", "Retail Sales", "Online Customer", "Online Sale", "RET-2025-008", 73.35, 0, 12361.74, "N", "", "Y"),
    ("2025-01-24", "Expense", "Equipment & Maintenance", "Coffee Tech Services", "Check #1044 - Equipment service", "CHK-1044", 0, 386.28, 11975.46, "Y", "", "Y"),
    ("2025-01-25", "Income", "Retail Sales", "Online Customer", "Online Sale", "RET-2025-009", 43.45, 0, 12018.91, "N", "", "Y"),
    ("2025-01-26", "Expense", "Shipping & Delivery", "UPS Store", "POS Purchase - Shipping", "POS", 0, 75.10, 11943.81, "Y", "", "Y"),
    ("2025-01-28", "Expense", "Vehicle & Fuel", "Shell Gas Station", "POS Purchase - Fuel", "POS", 0, 51.84, 11891.97, "Y", "", "Y"),
    ("2025-01-28", "Income", "Retail Sales", "Online Customer", "Online Sale", "RET-2025-010", 68.12, 0, 11960.09, "N", "", "Y"),

    # February 2025 - NOTE: Bank shows opening $13,940.09 but Jan ended $11,960.09 - DISCREPANCY
    ("2025-02-02", "Income", "Retail Sales", "Online Customer", "Online Sale", "RET-2025-011", 53.64, 0, 13993.73, "N", "BANK DISCREPANCY - Feb opening doesnt match Jan closing", "Y"),
    ("2025-02-03", "Income", "Wholesale", "The Daily Grind Cafe", "Deposit - Wholesale order", "INV", 482.00, 0, 14475.73, "N", "", "Y"),
    ("2025-02-03", "Expense", "Cost of Goods Sold", "Pacific Coffee Importers", "Check #1045 - Green coffee beans", "CHK-1045", 0, 1765.00, 12710.73, "Y", "", "Y"),
    ("2025-02-05", "Expense", "Vehicle & Fuel", "Shell Gas Station", "POS Purchase - Fuel", "POS", 0, 49.58, 12661.15, "Y", "", "Y"),
    ("2025-02-05", "Income", "Wholesale", "Sunrise Espresso Bar", "Deposit - Wholesale order", "INV", 410.00, 0, 13071.15, "N", "", "Y"),
    ("2025-02-05", "Income", "Retail Sales", "Online Customer", "Online Sale", "RET-2025-012", 61.68, 0, 13132.83, "N", "", "Y"),
    ("2025-02-06", "Expense", "Internet & Phone", "Xfinity Business", "Autopay - Internet/Phone", "AUTO", 0, 128.99, 13003.84, "Y", "", "Y"),
    ("2025-02-08", "Expense", "Packaging & Supplies", "PackagingPro Supply", "POS Purchase - Packaging", "POS", 0, 531.14, 12472.70, "Y", "", "Y"),
    ("2025-02-08", "Income", "Retail Sales", "Online Customer", "Online Sale", "RET-2025-013", 36.46, 0, 12509.16, "N", "", "Y"),
    ("2025-02-10", "Expense", "Utilities", "Boulder Electric Co.", "Autopay - Electric", "AUTO", 0, 215.78, 12293.38, "Y", "", "Y"),
    ("2025-02-10", "Income", "Wholesale", "Mountain View Bistro", "ACH Deposit - Wholesale order", "ACH", 790.88, 0, 13084.26, "N", "", "Y"),
    ("2025-02-10", "Income", "Retail Sales", "Online Customer", "Online Sale", "RET-2025-014", 59.55, 0, 13143.81, "N", "", "Y"),
    ("2025-02-11", "Expense", "Shipping & Delivery", "UPS Store", "POS Purchase - Shipping", "POS", 0, 118.56, 13025.25, "Y", "", "Y"),
    ("2025-02-12", "Expense", "Vehicle & Fuel", "Shell Gas Station", "POS Purchase - Fuel", "POS", 0, 50.01, 12975.24, "Y", "", "Y"),
    ("2025-02-13", "Income", "Retail Sales", "Online Customer", "Online Sale", "RET-2025-015", 71.33, 0, 13046.57, "N", "", "Y"),
    ("2025-02-14", "Expense", "Office Supplies", "Office Depot", "POS Purchase - Office supplies", "POS", 0, 53.61, 12992.96, "Y", "", "Y"),
    ("2025-02-15", "Income", "Retail Sales", "Online Customer", "Online Sale", "RET-2025-016", 45.60, 0, 13038.56, "N", "", "Y"),
    ("2025-02-17", "Income", "Wholesale", "The Daily Grind Cafe", "Deposit - Wholesale order", "INV", 548.00, 0, 13586.56, "N", "", "Y"),
    ("2025-02-18", "Expense", "Cost of Goods Sold", "Pacific Coffee Importers", "Check #1046 - Green coffee beans", "CHK-1046", 0, 1695.00, 11891.56, "Y", "", "Y"),
    ("2025-02-18", "Income", "Retail Sales", "Online Customer", "Online Sale", "RET-2025-017", 58.46, 0, 11950.02, "N", "", "Y"),
    ("2025-02-19", "Expense", "Vehicle & Fuel", "Shell Gas Station", "POS Purchase - Fuel", "POS", 0, 47.46, 11902.56, "Y", "", "Y"),
    ("2025-02-19", "Income", "Wholesale", "Sunrise Espresso Bar", "Deposit - Wholesale order", "INV", 362.00, 0, 12264.56, "N", "", "Y"),
    ("2025-02-21", "Income", "Retail Sales", "Online Customer", "Online Sale", "RET-2025-018", 53.64, 0, 12318.20, "N", "", "Y"),
    ("2025-02-24", "Expense", "Shipping & Delivery", "UPS Store", "POS Purchase - Shipping", "POS", 0, 127.68, 12190.52, "Y", "", "Y"),
    ("2025-02-24", "Income", "Retail Sales", "Online Customer", "Online Sale", "RET-2025-019", 86.20, 0, 12276.72, "N", "", "Y"),
    ("2025-02-26", "Expense", "Vehicle & Fuel", "Shell Gas Station", "POS Purchase - Fuel", "POS", 0, 51.31, 12225.41, "Y", "", "Y"),
    ("2025-02-27", "Income", "Retail Sales", "Online Customer", "Online Sale", "RET-2025-020", 26.29, 0, 12251.70, "N", "", "Y"),

    # March 2025 - NOTE: Bank shows opening $14,220.68 but Feb ended $12,251.70 - DISCREPANCY
    ("2025-03-02", "Income", "Retail Sales", "Online Customer", "Online Sale", "RET-2025-021", 32.18, 0, 14252.86, "N", "BANK DISCREPANCY - Mar opening doesnt match Feb closing", "Y"),
    ("2025-03-03", "Expense", "Cost of Goods Sold", "Pacific Coffee Importers", "Check #1047 - Green coffee beans", "CHK-1047", 0, 1980.00, 12272.86, "Y", "", "Y"),
    ("2025-03-03", "Income", "Wholesale", "The Daily Grind Cafe", "Deposit - Wholesale order", "INV", 466.00, 0, 12738.86, "N", "", "Y"),
    ("2025-03-05", "Expense", "Vehicle & Fuel", "Shell Gas Station", "POS Purchase - Fuel", "POS", 0, 56.24, 12682.62, "Y", "", "Y"),
    ("2025-03-05", "Income", "Wholesale", "Sunrise Espresso Bar", "Deposit - Wholesale order", "INV", 484.00, 0, 13166.62, "N", "", "Y"),
    ("2025-03-05", "Income", "Retail Sales", "Online Customer", "Online Sale", "RET-2025-022", 55.24, 0, 13221.86, "N", "", "Y"),
    ("2025-03-06", "Expense", "Internet & Phone", "Xfinity Business", "Autopay - Internet/Phone", "AUTO", 0, 128.99, 13092.87, "Y", "", "Y"),
    ("2025-03-07", "Expense", "Packaging & Supplies", "PackagingPro Supply", "POS Purchase - Packaging", "POS", 0, 520.41, 12572.46, "Y", "", "Y"),
    ("2025-03-08", "Income", "Retail Sales", "Online Customer", "Online Sale", "RET-2025-023", 63.83, 0, 12636.29, "N", "", "Y"),
    ("2025-03-10", "Expense", "Utilities", "Boulder Electric Co.", "Autopay - Electric", "AUTO", 0, 187.23, 12449.06, "Y", "", "Y"),
    ("2025-03-11", "Income", "Retail Sales", "Online Customer", "Online Sale", "RET-2025-024", 53.64, 0, 12502.70, "N", "", "Y"),
    ("2025-03-12", "Expense", "Vehicle & Fuel", "Shell Gas Station", "POS Purchase - Fuel", "POS", 0, 51.30, 12451.40, "Y", "", "Y"),
    ("2025-03-12", "Income", "Wholesale", "Mountain View Bistro", "ACH Deposit - Wholesale order", "ACH", 938.00, 0, 13389.40, "N", "", "Y"),
    ("2025-03-13", "Expense", "Shipping & Delivery", "UPS Store", "POS Purchase - Shipping", "POS", 0, 118.03, 13271.37, "Y", "", "Y"),
    ("2025-03-14", "Income", "Retail Sales", "Online Customer", "Online Sale", "RET-2025-025", 64.90, 0, 13336.27, "N", "", "Y"),
    ("2025-03-15", "Expense", "Office Supplies", "Office Depot", "POS Purchase - Office supplies", "POS", 0, 86.88, 13249.39, "Y", "", "Y"),
    ("2025-03-17", "Expense", "Cost of Goods Sold", "Pacific Coffee Importers", "Check #1048 - Green coffee beans", "CHK-1048", 0, 2070.00, 11179.39, "Y", "", "Y"),
    ("2025-03-17", "Income", "Retail Sales", "Online Customer", "Online Sale", "RET-2025-026", 75.47, 0, 11254.86, "N", "", "Y"),
    ("2025-03-19", "Expense", "Vehicle & Fuel", "Shell Gas Station", "POS Purchase - Fuel", "POS", 0, 51.30, 11203.56, "Y", "", "Y"),
    ("2025-03-19", "Income", "Wholesale", "Sunrise Espresso Bar", "Deposit - Wholesale order", "INV", 427.00, 0, 11630.56, "N", "", "Y"),
    ("2025-03-20", "Income", "Retail Sales", "Online Customer", "Online Sale", "RET-2025-027", 47.74, 0, 11678.30, "N", "", "Y"),
    ("2025-03-21", "Expense", "Equipment & Maintenance", "Coffee Tech Services", "Check #1049 - Equipment service", "CHK-1049", 0, 654.53, 11023.77, "Y", "Need receipt - per notes.txt", "Y"),
    ("2025-03-23", "Income", "Retail Sales", "Online Customer", "Online Sale", "RET-2025-028", 73.35, 0, 11097.12, "N", "", "Y"),
    ("2025-03-24", "Expense", "Shipping & Delivery", "UPS Store", "POS Purchase - Shipping", "POS", 0, 94.38, 11002.74, "Y", "", "Y"),
    ("2025-03-26", "Expense", "Vehicle & Fuel", "Shell Gas Station", "POS Purchase - Fuel", "POS", 0, 55.94, 10946.80, "Y", "", "Y"),
    ("2025-03-26", "Income", "Retail Sales", "Online Customer", "Online Sale", "RET-2025-029", 37.53, 0, 10984.33, "N", "", "Y"),
    ("2025-03-28", "Expense", "Packaging & Supplies", "PackagingPro Supply", "POS Purchase - Packaging", "POS", 0, 191.00, 10793.33, "Y", "", "Y"),
    ("2025-03-28", "Income", "Retail Sales", "Online Customer", "Online Sale", "RET-2025-030", 53.64, 0, 10846.97, "N", "", "Y"),
]

# Write transactions
for row_num, trans in enumerate(bank_transactions, 2):
    for col_num, value in enumerate(trans, 1):
        cell = ws_trans.cell(row=row_num, column=col_num, value=value)
        if col_num == 1 and value:  # Date
            try:
                cell.value = datetime.strptime(value, "%Y-%m-%d")
                cell.number_format = date_format
            except:
                pass
        elif col_num in [7, 8, 9]:  # Income, Expense, Balance
            cell.number_format = currency_format

# Set column widths
col_widths = [12, 10, 20, 25, 35, 12, 12, 12, 14, 14, 40, 12]
for i, width in enumerate(col_widths, 1):
    ws_trans.column_dimensions[get_column_letter(i)].width = width

# ============ MONTHLY SUMMARY SHEET ============
ws_monthly = wb.create_sheet("Monthly Summary")
monthly_headers = ["Month", "Opening Balance", "Total Income", "Total Expenses", "Net Change", "Closing Balance"]
for col, header in enumerate(monthly_headers, 1):
    cell = ws_monthly.cell(row=1, column=col, value=header)
    cell.font = header_font_white
    cell.fill = header_fill

monthly_data = [
    ("January 2025", 15420.00, 1250.77, 4710.68, -3459.91, 11960.09),
    ("February 2025", 13940.09, 3145.73, 4834.12, -1688.39, 12251.70),
    ("March 2025", 14220.68, 2872.52, 6246.23, -3373.71, 10846.97),
]

for row_num, data in enumerate(monthly_data, 2):
    for col_num, value in enumerate(data, 1):
        cell = ws_monthly.cell(row=row_num, column=col_num, value=value)
        if col_num > 1:
            cell.number_format = currency_format

# Total row
ws_monthly.cell(row=5, column=1, value="Q1 2025 TOTAL").font = header_font
ws_monthly.cell(row=5, column=3, value="=SUM(C2:C4)").number_format = currency_format
ws_monthly.cell(row=5, column=4, value="=SUM(D2:D4)").number_format = currency_format
ws_monthly.cell(row=5, column=5, value="=SUM(E2:E4)").number_format = currency_format

for i, width in enumerate([15, 15, 15, 15, 15, 15], 1):
    ws_monthly.column_dimensions[get_column_letter(i)].width = width

# ============ EXPENSE CATEGORIES SHEET ============
ws_categories = wb.create_sheet("Expense Categories")
cat_headers = ["Category", "Tax Deductible", "Description"]
for col, header in enumerate(cat_headers, 1):
    cell = ws_categories.cell(row=1, column=col, value=header)
    cell.font = header_font_white
    cell.fill = header_fill

categories = [
    ("Bank Fees", "Y", "Banking fees, wire transfer fees"),
    ("Cost of Goods Sold", "Y", "Raw materials - green coffee beans, tea"),
    ("Equipment & Maintenance", "Y", "Roasting equipment repairs and service"),
    ("Insurance", "Y", "Business insurance premiums"),
    ("Internet & Phone", "Y", "Business internet, phone service"),
    ("Marketing & Advertising", "Y", "Advertising, promotional materials"),
    ("Meals & Entertainment", "Partial", "Business meals (50% deductible)"),
    ("Office Supplies", "Y", "Office supplies, printer supplies"),
    ("Packaging & Supplies", "Y", "Bags, labels, packaging materials"),
    ("Professional Services", "Y", "Accounting, legal, consulting"),
    ("Rent", "Y", "Facility rent/lease payments"),
    ("Shipping & Delivery", "Y", "UPS, FedEx, USPS shipping"),
    ("Utilities", "Y", "Electric, gas, water"),
    ("Vehicle & Fuel", "Y", "Delivery vehicle fuel and maintenance"),
]

for row_num, cat in enumerate(categories, 2):
    for col_num, value in enumerate(cat, 1):
        ws_categories.cell(row=row_num, column=col_num, value=value)

for i, width in enumerate([25, 15, 45], 1):
    ws_categories.column_dimensions[get_column_letter(i)].width = width

# ============ PROFIT & LOSS SHEET ============
ws_pl = wb.create_sheet("Profit & Loss")
ws_pl.cell(row=1, column=1, value="PROFIT & LOSS STATEMENT").font = Font(bold=True, size=14)
ws_pl.cell(row=2, column=1, value="Mountain Pine Coffee Roasters LLC")
ws_pl.cell(row=3, column=1, value="Q1 2025 (January - March)")

pl_headers = ["", "January", "February", "March", "Q1 Total"]
for col, header in enumerate(pl_headers, 1):
    cell = ws_pl.cell(row=5, column=col, value=header)
    cell.font = header_font

pl_data = [
    ("INCOME", "", "", "", ""),
    ("Retail Sales", 560.77, 652.85, 637.52, "=SUM(B7:D7)"),
    ("Wholesale", 690.00, 2592.88, 2315.00, "=SUM(B8:D8)"),
    ("Total Income", "=SUM(B7:B8)", "=SUM(C7:C8)", "=SUM(D7:D8)", "=SUM(B9:D9)"),
    ("", "", "", "", ""),
    ("EXPENSES", "", "", "", ""),
    ("Cost of Goods Sold", 3245.00, 3460.00, 4050.00, "=SUM(B12:D12)"),
    ("Equipment & Maintenance", 386.28, 0, 654.53, "=SUM(B13:D13)"),
    ("Internet & Phone", 128.99, 128.99, 128.99, "=SUM(B14:D14)"),
    ("Office Supplies", 109.42, 53.61, 86.88, "=SUM(B15:D15)"),
    ("Packaging & Supplies", 284.34, 531.14, 711.41, "=SUM(B16:D16)"),
    ("Shipping & Delivery", 165.22, 246.24, 212.41, "=SUM(B17:D17)"),
    ("Utilities", 198.45, 215.78, 187.23, "=SUM(B18:D18)"),
    ("Vehicle & Fuel", 192.98, 248.36, 214.78, "=SUM(B19:D19)"),
    ("Total Expenses", "=SUM(B12:B19)", "=SUM(C12:C19)", "=SUM(D12:D19)", "=SUM(B20:D20)"),
    ("", "", "", "", ""),
    ("NET PROFIT/(LOSS)", "=B9-B20", "=C9-C20", "=D9-D20", "=SUM(B22:D22)"),
]

for row_num, data in enumerate(pl_data, 6):
    for col_num, value in enumerate(data, 1):
        cell = ws_pl.cell(row=row_num, column=col_num, value=value)
        if col_num > 1 and value:
            cell.number_format = currency_format
        if row_num in [6, 11, 20, 22] or col_num == 1 and value in ["INCOME", "EXPENSES", "Total Income", "Total Expenses", "NET PROFIT/(LOSS)"]:
            cell.font = header_font

for i, width in enumerate([25, 12, 12, 12, 12], 1):
    ws_pl.column_dimensions[get_column_letter(i)].width = width

# ============ DASHBOARD SHEET ============
ws_dash = wb.create_sheet("Dashboard")
ws_dash.cell(row=1, column=1, value="BOOKKEEPING DASHBOARD").font = Font(bold=True, size=14)
ws_dash.cell(row=2, column=1, value="Mountain Pine Coffee Roasters LLC - Q1 2025")

ws_dash.cell(row=4, column=1, value="KEY METRICS").font = header_font
metrics = [
    ("Opening Balance (Jan 1)", 15420.00),
    ("Closing Balance (Mar 31)", 10846.97),
    ("Total Q1 Income", 7269.02),
    ("Total Q1 Expenses", 15791.03),
    ("Net Change", -8522.01),
]
for row_num, (label, value) in enumerate(metrics, 5):
    ws_dash.cell(row=row_num, column=1, value=label)
    cell = ws_dash.cell(row=row_num, column=2, value=value)
    cell.number_format = currency_format

ws_dash.cell(row=11, column=1, value="ISSUES TO RESOLVE").font = header_font
issues = [
    "1. CRITICAL: Bank statement opening balances do not chain properly between months",
    "2. Missing receipt for Coffee Tech Services repair (March) - per notes.txt",
    "3. Check for duplicate invoice - Mountain View Bistro - per notes.txt",
    "4. Potential duplicate files: PUR-019, PUR-022, PUR-033 have copies",
    "5. Follow up on unpaid invoices - per notes.txt",
    "6. IMG_2847.jpg in To File folder needs identification",
]
for row_num, issue in enumerate(issues, 12):
    ws_dash.cell(row=row_num, column=1, value=issue)

ws_dash.column_dimensions['A'].width = 70
ws_dash.column_dimensions['B'].width = 15

# Save workbook
output_path = r"D:\ReposFred\cc-ai-scenarios\01-bookkeeper\Mountain Pine Coffee Roasters\2025\Bookkeeping 2025.xlsx"
wb.save(output_path)
print(f"[OK] Created: {output_path}")
print(f"[OK] Sheets: {wb.sheetnames}")
print(f"[OK] Transactions: {len(bank_transactions)} rows from bank statements")
