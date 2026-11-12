"""
Webhook Pulse - Lightweight Webhook Ingestion & Health Monitor
Author: Hashim (@hashim_py | https://hashim.me.uk)
"""
import hmac
import hashlib
import json
import time
from typing import Dict, Any, Tuple, Optional
from dataclasses import dataclass, field

@dataclass
class WebhookEvent:
    event_type: str
    payload: Dict[str, Any]
    received_at: float = field(default_factory=time.time)
    verified: bool = False
    delivery_attempts: int = 0

class WebhookPulse:
    def __init__(self, secret_key: str = "default_secret", max_retries: int = 3):
        self.secret_key = secret_key.encode("utf-8")
        self.max_retries = max_retries
        self.event_log = []

    def verify_signature(self, raw_body: bytes, signature_header: str) -> bool:
        if not signature_header:
            return False
        computed = hmac.new(self.secret_key, raw_body, hashlib.sha256).hexdigest()
        clean_sig = signature_header.replace("sha256=", "").strip()
        return hmac.compare_digest(computed, clean_sig)

    def ingest_event(self, event_type: str, raw_payload: bytes, signature: Optional[str] = None) -> Tuple[bool, str, Optional[WebhookEvent]]:
        is_verified = False
        if signature:
            is_verified = self.verify_signature(raw_payload, signature)
            if not is_verified:
                return False, "Invalid signature verification failed", None
        
        try:
            parsed_json = json.loads(raw_payload.decode("utf-8"))
        except Exception as e:
            return False, f"JSON decoding error: {str(e)}", None

        event = WebhookEvent(
            event_type=event_type,
            payload=parsed_json,
            verified=is_verified
        )
        self.event_log.append(event)
        return True, "Event ingested successfully", event

    def dispatch_alert(self, event: WebhookEvent) -> bool:
        for attempt in range(1, self.max_retries + 1):
            event.delivery_attempts = attempt
            if self._mock_send_http(event):
                return True
            time.sleep(0.05 * (2 ** (attempt - 1)))
        return False

    def _mock_send_http(self, event: WebhookEvent) -> bool:
        return True
