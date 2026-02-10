Fastrans Accounting UI Prototype (Static)
================================================

What this is
------------
This is a STATIC (no-backend) UI prototype made with HTML/CSS/JavaScript.
It includes:
- Login page (localStorage demo auth)
- Linked pages for: Dashboard, Bank Recon, Invoices/AR, Suppliers/AP, SOA, GST Form 5,
  Payroll, IR8A, Corporate Tax, ACRA Reports, Auditor Pack, Audit Trail, Supplier Invoice Inbox,
  Customers, Settings.

Demo credentials
----------------
1) admin / admin123
2) accounts / accounts123

How to run locally
------------------
1) Extract the ZIP.
2) Open: login.html (double-click)
3) Login and navigate using the sidebar.

Important note about browsers
-----------------------------
Some browsers restrict local file access for certain features.
This UI is built to work as simple static pages. If anything is blocked, use a local server:

Option A (Python)
- Open a terminal inside the folder and run:
  python -m http.server 8000
- Then open:
  http://localhost:8000/login.html

Option B (VS Code)
- Install "Live Server" extension → Right-click login.html → "Open with Live Server"

Files/folders
-------------
/assets/css/styles.css     -> UI theme
/assets/js/app.js          -> login/session + common nav handling
/login.html                -> entry point
/*.html                    -> pages

Security
--------
This uses localStorage for demo only.
For production (Django), replace with server-side authentication + sessions.

Next integration idea (Django)
------------------------------
- Convert each *.html into Django templates
- Replace placeholder buttons with real endpoints (GST compute, IR8A export, bank import, email outbox, etc.)
- Replace localStorage auth with Django auth
- Add database-backed audit trail + period locks + document storage

Generated on: 2026-02-07T02:15:47.914345


Update v2:
- Sidebar renamed: Invoices & AR → Customers; Suppliers & AP → Suppliers
- Added Customer Ledger page and Supplier Ledger page
- Added Payslips page and payroll link to create payslips
- Added manual create forms for Customers and Suppliers master


Update v3:
- Stronger Fastrans blue theme applied (background, sidebar, cards, buttons, active nav)


Update v5:
- Added Reports section + report pages (TB, P&L, BS, GST summary/recon, AR/AP ageing, bank recon summary, payroll summary)
- Added Opening Balances (Data Migration) page


Update v6:
- Added accounting number formatting (thousands separators)
- Negative numbers display in red with brackets
- Currency selector (SGD/USD) in header to toggle display currency prefix
- Amount columns auto-formatted via JS (demo)


Update v7:
- Added customer invoicing workflow: Costing Sheet Upload (Sales Order) → Create Invoice → Credit Note
- Added supplier workflow: Supplier Document Upload → Create Bill → Debit Note
- Line items include Account Codes + Qty/Rate + GST + Subtotal/GST/Total calculator
- UI-only placeholders for parsing uploads and auto-posting to ledger


Update v8:
- Added Data Migration section + pages: migration dashboard, COA import, customer import, supplier import, transaction import
- Sidebar links added under Migration
- All import pages are UI prototypes with templates + previews


Update v9:
- Added Receive Payment (Customers): partial allocations + credit note offsets
- Added Pay Bills (Suppliers): partial allocations + debit note offsets


Update v10:
- Added Import History (batch logs) page
- Added Migration Validation Report (TB agrees, AR/AP ties, GST control ties)
- Added COA Mapping (Old→New) for different account codes with same descriptions
- Migration sidebar updated with new links


Update v11:
- Added Unapplied Receipts / Prepayments page
- Added Overpayment Refund workflow
- Added Payment Allocation History (audit trail) page
- Enhanced Transaction Import preview: shows old vs mapped new codes side-by-side and blocks import if any unmapped
- Enhanced COA Mapping: selectable mapping + saves mapping to localStorage for use in import preview


Update v12:
- Added Cashflow module: Cashflow Dashboard, Forecast Modelling, Actual Cashflow, AP Payment Plan
- Sidebar updated with Cashflow section
- Basic demo chart + tables (UI prototype)


Update v13:
- Added AR Collection Plan (terms + due dates) and linked into Cashflow
- Extended COA mapping: mapping by old-code + by description, many-to-one supported
- Added Unmapped Accounts report with auditor sign-off
- Added ACRA-style reports: Cashflow Statement + Statement of Changes in Equity
- Added Journal Viewer + 'View Journal' buttons on key transaction pages


Update v14:
- Added General Ledger view with drill-down to journal lines
- Journal Viewer now renders exact journal lines from demo posted ledger and supports CSV export + Print-to-PDF
- Added CSV export helpers for audit pack (Excel-friendly)
- Added GL shortcut buttons from transaction pages (demo) and Journal Viewer -> GL


Update v15:
- Added Auditor Report: Opening Balance Tie-Out (closing audited figures vs opening balances) with sign-off and audit pack checklist


Update v16:
- Added Opening Balance Journal page (exact DR/CR opening posting) with CSV export + Print-to-PDF
- Added Period Lock page (month-end close / audit sign-off) with lock-to date and lock log
- Period lock state stored in localStorage and disables transaction action buttons (demo)


Update v17:
- Moved Opening Balance Tie-Out navigation link from Reports section to Audit section


Update v18:
- Added Approval Queue (approve before posting) + Posting Controls (enable automation later)
- Posting policy stored in localStorage (approval_required, auto_post_enabled, auto_post_after_days)
- Added banners to Bank Reconciliation and Supplier Invoice Inbox and links to Approval Queue
- Demo: Auto-post actions are disabled when Approval Required is ON and Auto-post is OFF


Update v19:
- Extended approval workflow to Receive Payment and Pay Bills (auto-match postings submit to Approval Queue)
- Added GST & Closing Adjustments page requiring approval before posting
- Added Period Lock manager approval request workflow (creates Approval Queue item)
- Approval Queue seed includes Receive/Pay, GST Adjustment, and Period Lock requests


Update v20:
- Approval Queue now captures approver name + timestamp + comments for Approve/Reject/Post via modal
- All actions are written to Approval Audit Trail (localStorage) and shown in new report page with CSV/PDF export
- Added Approval Audit Trail link under Audit navigation


Update v21:
- Added CFO Analytics module (Power BI style): KPIs + chart placeholders + drill-down notes
- Added CFO Assistant chatbot UI to create custom KPI/chart widgets (saved in localStorage)
- Added CFO subpages: Cashflow, Profitability, Expense, AR Risk, AP Exposure, Ratios, Budget vs Actual


Update v23:
- Added CFO Financial Overview (Finboard-style) with KPI tiles + IS/BS + ratios (SGD functional)
- Added CFO Budget Overview (Budget vs Actual) without departments: budgets by service/customer/account codes
- Added Income Statement + Balance Sheet analytics placeholder pages
- CFO Assistant KPI/Chart builder available on CFO pages (localStorage)


Update v24:
- CFO Assistant upgraded to Data Copilot (demo) using assets/data/demo_data.json
- Works best via local web server (VSCode Live Server), not file://
