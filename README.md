# ⚡ Webhook Pulse: Resilient Ingestion & Health Engine

**Category**: Automation & Backend  
**Author**: Hashim ([@hashim_py](https://x.com/hashim_py) · [hashim.me.uk](https://hashim.me.uk))  
**Status**: Live / Production Ready  

---

## 🎯 What it does
Webhook Pulse is a clean, dependency-free Python engine designed to ingest, verify, and forward webhooks from payment gateways (Stripe), version control (GitHub), and automation platforms (n8n, Zapier) without losing events or failing silently.

### Core Capabilities:
1. **Cryptographic Verification**: HMAC SHA-256 signature verification preventing spoofed or replay attacks.
2. **Exponential Backoff Dispatch**: Forwarding alerts with self-healing retry logic when destination endpoints are temporarily unavailable.
3. **Structured Audit Trail**: Keeps an in-memory event log for real-time observability.
4. **Standard Library Only**: 100% native Python with zero external pip bloat.

---

## 🛠️ Architecture & Tech Stack
- **Language**: Python 3.10+
- **Security**: `hmac`, `hashlib` (SHA-256 constant-time comparison)
- **Zero Third-Party Telemetry**: 100% local, self-hosted

---

## 🚀 Getting Started

### 1. Run the Demo
```bash
python main.py
```

### 2. Run Test Suite
```bash
python test_pulse.py
```

---

## 🔗 Live Links & Portfolio
- Developer Portfolio & Live Web Tools: [https://hashim.me.uk](https://hashim.me.uk)
- Author on X: [@hashim_py](https://x.com/hashim_py)
