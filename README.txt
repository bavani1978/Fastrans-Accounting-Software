Fastrans Backend (Django) — v1

This is a backend starter for your Fastrans Accounting UI.

Included now
- Login / session auth APIs
- Master data APIs: Chart of Accounts, Customers, Suppliers
- Journal drill-down APIs: journal detail + GL listing
- Approval Queue (approver + timestamp + comments) + Period Lock approval request workflow
- Import batches + COA mapping + Unmapped Accounts report + tie-out validation stub
- Document upload/list endpoints
- CFO endpoints (demo) that read ui/assets/data/demo_data.json if you copy the UI into backend/ui/

Not included yet (next phase)
- Full posting engine (invoice/bill/payment → journals)
- Auto bank statement matching + approval + posting
- GST Form 5 engine + timing differences
- Payroll + payslips + IR8A
- Corporate tax computation engine
- ACRA financial statements builder

Quick start
1) python -m venv venv
2) pip install -r requirements.txt
3) python manage.py migrate
4) python manage.py createsuperuser
5) (optional) copy your UI into ./ui/ then run:
   python manage.py load_demo_ui_data
6) python manage.py runserver 127.0.0.1:8000

API examples (after login)
- GET  /api/ledger/coa/
- GET  /api/ledger/customers/
- GET  /api/ledger/suppliers/
- GET  /api/approvals/queue/
- GET  /api/approvals/audit-report/
- GET  /api/imports/mapping/
- GET  /api/imports/unmapped-report/?old_codes=1000,2000,9999
- GET  /api/cfo/kpis/     (requires UI demo_data.json copied into backend/ui/)

How to connect UI → backend later
- Replace the UI demo_data.json usage with fetch calls to these /api/* endpoints.
- When posting engine is ready, Data Copilot will read real journals and AR/AP tables.
