WEIGHTS = {"critical": 4, "high": 3, "medium": 2, "low": 1, "pass": 0}

def score_checks(checks):
    return sum(WEIGHTS.get(str(c.get("status", "pass")).lower(), 0) for c in checks)

def summarize(checks):
    result = {k: 0 for k in WEIGHTS}
    for check in checks:
        status = str(check.get("status", "pass")).lower()
        result[status if status in result else "pass"] += 1
    return result
