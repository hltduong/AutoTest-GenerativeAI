"""HTTP client for agest.vn API endpoints (if any)."""

import httpx
from typing import Any


class AgestClient:
    """Reusable API client for agest.vn."""

    def __init__(self, base_url: str | None = None, timeout: float = 30.0) -> None:
        self.base_url = (base_url or "https://www.agest.vn").rstrip("/")
        self.timeout = timeout

    def _client(self) -> httpx.Client:
        return httpx.Client(
            base_url=self.base_url,
            timeout=self.timeout,
            follow_redirects=True,
            headers={"User-Agent": "AGEST-AutoTest/1.0"},
        )

    def get(self, path: str = "") -> httpx.Response:
        """GET request to base URL or path."""
        with self._client() as client:
            return client.get(path or "/")

    def health_check(self) -> tuple[int, str]:
        """Check if site is reachable. Returns (status_code, reason)."""
        try:
            resp = self.get("/")
            return resp.status_code, resp.reason_phrase or "OK"
        except httpx.RequestError as e:
            return 0, str(e)
