"""Configuration for agest.vn test automation."""

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# Base URL for agest.vn
BASE_URL = os.getenv("BASE_URL", "https://www.agest.vn")

# Paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Timeouts (ms)
DEFAULT_TIMEOUT = 30_000
NAVIGATION_TIMEOUT = 60_000

# Screenshots & traces
SCREENSHOT_ON_FAILURE = True
TRACE_ON_FAILURE = True
