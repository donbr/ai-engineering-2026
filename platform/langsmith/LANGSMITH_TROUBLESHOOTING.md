# LangSmith API Key & Connection Troubleshooting Guide

> A systematic guide to diagnosing and resolving LangSmith connection issues

## Understanding the Problem Space

Before diving into fixes, understand **why** LangSmith connection issues are tricky:

```
┌─────────────────────────────────────────────────────────────────┐
│                    THE CONNECTION CHAIN                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  .env file → IDE/Shell → Python os.environ → LangSmith Cache   │
│      │           │              │                    │         │
│      │     (may cache)    (may cache)          (definitely     │
│      │                                          caches!)       │
│      └──────────────────────────────────────────────────────── │
│                                                                 │
│  Each layer can hold STALE values even after you update .env   │
└─────────────────────────────────────────────────────────────────┘
```

**Key Insight**: The 403 Forbidden error almost always means authentication failed—but the *reason* varies.

---

## Quick Diagnostic Checklist

Run this cell **FIRST** when you encounter issues:

```python
import os

print("=== LangSmith Environment Diagnostic ===\n")

# Check all relevant variables
vars_to_check = [
    "LANGSMITH_API_KEY",      # New naming (preferred)
    "LANGCHAIN_API_KEY",      # Legacy naming (still works)
    "LANGSMITH_TRACING",      # New naming
    "LANGCHAIN_TRACING_V2",   # Legacy naming
    "LANGSMITH_ENDPOINT",     # For EU users
    "LANGSMITH_PROJECT",
]

for var in vars_to_check:
    val = os.getenv(var)
    if val:
        # Mask API keys for security
        if "API_KEY" in var:
            display = f"{val[:8]}...{val[-4:]}" if len(val) > 12 else "***"
        else:
            display = val
        print(f"✓ {var}: {display}")
    else:
        print(f"✗ {var}: NOT SET")

# Verify API key format
api_key = os.getenv("LANGSMITH_API_KEY") or os.getenv("LANGCHAIN_API_KEY")
if api_key:
    if api_key.startswith("lsv2_pt_"):
        print("\n✓ API key format: Personal Access Token (valid)")
    elif api_key.startswith("lsv2_sk_"):
        print("\n✓ API key format: Service Key (valid)")
    elif api_key.startswith("ls_"):
        print("\n⚠ API key format: Legacy format (may still work)")
    else:
        print("\n✗ API key format: INVALID - should start with lsv2_pt_ or lsv2_sk_")
```

---

## Error Pattern Recognition

### Pattern 1: 403 Forbidden

```
Failed to POST https://api.smith.langchain.com/runs/multipart
HTTPError('403 Client Error: Forbidden...')
```

**Possible Causes (in order of likelihood):**

| Cause | Probability | Quick Test |
|-------|-------------|------------|
| API key not set | 40% | Run diagnostic above |
| API key invalid/expired | 25% | Generate new key at smith.langchain.com |
| Cached stale API key | 20% | Clear cache (see below) |
| Wrong endpoint (EU user) | 10% | Check if you signed up at eu.smith.langchain.com |
| Workspace permission issue | 5% | Check X-Tenant-Id for org-scoped keys |

### Pattern 2: Connection Timeout / Network Error

```
ConnectionError: HTTPSConnectionPool(host='api.smith.langchain.com'...)
```

**Possible Causes:**
- Corporate firewall/proxy blocking
- VPN interference
- Temporary LangSmith service issue

### Pattern 3: Traces Going to Wrong Project

**Cause:** Environment variable caching (very common in Jupyter)

---

## The Caching Problem (CRITICAL)

### Why This Happens

LangSmith **intentionally caches** environment variables for performance. This cache persists even when you:
- Update your `.env` file
- Re-run `load_dotenv()`
- Restart the Jupyter kernel (soft restart)

### The Nuclear Option: Clear Everything

```python
# Step 1: Clear LangSmith's internal cache
try:
    from langsmith import utils
    utils.get_env_var.cache_clear()
    print("✓ LangSmith cache cleared")
except Exception as e:
    print(f"Note: Could not clear LangSmith cache: {e}")

# Step 2: Reload .env with override
from dotenv import load_dotenv
load_dotenv(override=True)
print("✓ Environment reloaded from .env")

# Step 3: Verify the new values
import os
print(f"✓ API Key now: {os.getenv('LANGSMITH_API_KEY', 'NOT SET')[:12]}...")
```

### IDE-Specific Cache Behavior

| IDE | Kernel Restart | Full IDE Restart | Notes |
|-----|---------------|------------------|-------|
| **VS Code** | Partial clear | Full clear | Known issue: env vars cached at kernel level |
| **Cursor** | Partial clear | Full clear | Same behavior as VS Code |
| **JupyterLab** | Full clear | Full clear | Most predictable |
| **Google Colab** | Full clear | N/A | Reconnect = new environment |

**Cursor + Jupyter Specific Issue**: After updating `.env`, you may need to:
1. Save notebook
2. Close the notebook tab
3. Restart Cursor entirely
4. Reopen notebook

---

## Solution Flowchart

```
START: Getting 403 Forbidden?
           │
           ▼
    ┌──────────────────┐
    │ Run diagnostic   │
    │ cell above       │
    └────────┬─────────┘
             │
             ▼
    ┌──────────────────┐     YES    ┌─────────────────────┐
    │ Is API key set?  │──────────▶│ Is format valid?    │
    └────────┬─────────┘            │ (lsv2_pt_ or lsv2_sk_)
             │ NO                   └──────────┬──────────┘
             ▼                                 │
    ┌──────────────────┐            ┌──────────┴──────────┐
    │ Set API key:     │            │ YES          NO     │
    │ os.environ[...]=│            │  │            │     │
    │ getpass(...)     │            │  ▼            ▼     │
    └──────────────────┘            │ Clear     Generate  │
                                    │ cache     new key   │
                                    └─────────────────────┘
                                              │
                                              ▼
                                    ┌─────────────────────┐
                                    │ Still failing?      │
                                    │ Check if EU user    │
                                    │ → Set LANGSMITH_    │
                                    │   ENDPOINT          │
                                    └─────────────────────┘
```

---

## Environment Variable Reference

### Current (Preferred) Names

```bash
LANGSMITH_API_KEY=lsv2_pt_xxxxx     # Your API key
LANGSMITH_TRACING=true              # Enable tracing
LANGSMITH_PROJECT="My Project"      # Project name
LANGSMITH_ENDPOINT=https://api.smith.langchain.com  # US (default)
# LANGSMITH_ENDPOINT=https://eu.api.smith.langchain.com  # EU
```

### Legacy Names (Still Supported)

```bash
LANGCHAIN_API_KEY=lsv2_pt_xxxxx     # Maps to LANGSMITH_API_KEY
LANGCHAIN_TRACING_V2=true           # Maps to LANGSMITH_TRACING
LANGCHAIN_PROJECT="My Project"      # Maps to LANGSMITH_PROJECT
LANGCHAIN_ENDPOINT=...              # Maps to LANGSMITH_ENDPOINT
```

### EU vs US Endpoints

| Region | Account Created At | API Endpoint |
|--------|-------------------|--------------|
| **US** (default) | smith.langchain.com | `https://api.smith.langchain.com` |
| **EU** | eu.smith.langchain.com | `https://eu.api.smith.langchain.com` |

**Important**: Being in Europe does NOT require the EU endpoint. Only use EU if you specifically created your account at `eu.smith.langchain.com`.

---

## Recommended Setup Pattern for Notebooks

```python
# Cell 1: Environment Setup (run once at start)
import os
import getpass
from uuid import uuid4

# Clear any cached values first
try:
    from langsmith import utils
    utils.get_env_var.cache_clear()
except:
    pass

# Interactive input for API keys
print("Enter your API keys (press Enter to skip optional ones)\n")

openai_key = getpass.getpass("OpenAI API Key: ")
if openai_key:
    os.environ["OPENAI_API_KEY"] = openai_key

langsmith_key = getpass.getpass("LangSmith API Key (optional): ")
if langsmith_key:
    os.environ["LANGSMITH_API_KEY"] = langsmith_key
    os.environ["LANGSMITH_TRACING"] = "true"
    os.environ["LANGSMITH_PROJECT"] = f"AIE9-Session5-{uuid4().hex[:8]}"
else:
    os.environ["LANGSMITH_TRACING"] = "false"
    print("⚠ LangSmith tracing disabled (no API key)")

# Verification
print("\n=== Configuration Summary ===")
print(f"OpenAI: {'✓ Set' if os.getenv('OPENAI_API_KEY') else '✗ Missing'}")
print(f"LangSmith: {'✓ Enabled' if os.getenv('LANGSMITH_TRACING') == 'true' else '✗ Disabled'}")
if os.getenv('LANGSMITH_PROJECT'):
    print(f"Project: {os.getenv('LANGSMITH_PROJECT')}")
```

---

## The "Works Sometimes" Problem

If LangSmith works inconsistently, consider these factors:

### Timing Issues

```python
# BAD: Race condition possible
os.environ["LANGSMITH_API_KEY"] = key
client = Client()  # May use cached value

# GOOD: Explicit initialization
os.environ["LANGSMITH_API_KEY"] = key
from langsmith import utils
utils.get_env_var.cache_clear()
client = Client()  # Uses fresh value
```

### IDE State Pollution

```python
# Add this at the TOP of your notebook
import importlib
import langsmith

# Force module reload
importlib.reload(langsmith)
```

### Defensive Pattern

```python
from langsmith import Client
import os

def get_langsmith_client():
    """Get a fresh LangSmith client, clearing any cache."""
    try:
        from langsmith import utils
        utils.get_env_var.cache_clear()
    except:
        pass

    api_key = os.getenv("LANGSMITH_API_KEY")
    if not api_key:
        return None

    return Client(api_key=api_key)

# Use this instead of global Client()
client = get_langsmith_client()
```

---

## Quick Fixes Summary

| Problem | Quick Fix |
|---------|-----------|
| 403 Forbidden | Generate new API key, clear cache |
| Traces not appearing | Check `LANGSMITH_TRACING=true` |
| Wrong project | Clear cache, verify `LANGSMITH_PROJECT` |
| EU user issues | Set `LANGSMITH_ENDPOINT` to EU URL |
| Flaky in Cursor | Full IDE restart after .env changes |
| Works in terminal, not notebook | Environment isolation issue—use getpass |

---

## Disable Tracing (Workaround)

If you can't resolve the issue and need to continue with the assignment:

```python
os.environ["LANGSMITH_TRACING"] = "false"
os.environ["LANGCHAIN_TRACING_V2"] = "false"
```

This allows your code to run without LangSmith tracing. You can revisit the connection issue later.

---

## Resources

- [LangSmith: Troubleshoot Variable Caching](https://docs.langchain.com/langsmith/troubleshooting-variable-caching)
- [LangSmith: Create Account & API Key](https://docs.langchain.com/langsmith/create-account-api-key)
- [LangSmith: Regions FAQ](https://docs.langchain.com/langsmith/regions-faq)
- [LangSmith: Trace Without Environment Variables](https://docs.langchain.com/langsmith/trace-without-env-vars)
