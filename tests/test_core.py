from secwatch import score_checks, summarize

def test_checks():
    checks = [{"status": "high"}, {"status": "pass"}]
    assert score_checks(checks) == 3
    assert summarize(checks)["pass"] == 1
