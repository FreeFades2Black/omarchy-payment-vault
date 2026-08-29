# 💳 Omarchy High-Throughput Payment Vault

High-performance encrypted transaction settlement and tokenization microservice migrated from Azure DevOps to GitHub Enterprise.

---

## 📋 Migration & Governance Audit

* **Source Platform:** Azure DevOps (`source-ado-repos/omarchy-payment-vault`)
* **Target Platform:** GitHub Enterprise (`FreeFades2Black/omarchy-payment-vault`)
* **Pipeline Translation:** Converted legacy `azure-pipelines.yml` to native GitHub Actions `.github/workflows/ci.yml`.
* **Compliance Verdict:** `PASSED_100_PERCENT_PARITY`
* **Secret Scan:** `CLEAN` (0 exposed credentials in git history).

---

## 🚀 API Endpoints

* `GET /health` — Service health & database connectivity.
* `POST /api/payments/charge` — Securely authorizes and settles payment transactions.

---

## 🛠️ Local Development

```bash
# Run service locally
python3 -m uvicorn app:app --host 0.0.0.0 --port 8820
```
