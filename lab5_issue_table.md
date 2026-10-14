# Lab 5 Issue Table

Initial findings refer to the original `movie_reviews.py`; findings were reviewed for relevance before fixes.

| Issue | Type | Line(s) | Description | Fix Approach |
|-------|------|---------|-------------|--------------|
| MD5 hash used for review IDs (Bandit B324, High) | Security | 46 | Bandit flags MD5 as a weak hash. | Replaced with SHA-256 while preserving the 10-character ID format. |
| Bind to all interfaces (Bandit B104, Medium) | Security | 4 | `0.0.0.0` may expose a bound service through every network interface. | Set the default host to loopback (`127.0.0.1`). |
| Hard-coded password (Bandit B105, Low) | Security | 6 | A plaintext moderator password is in source and unused in the demo. | Removed the unused credential. |
| Pseudo-random generator (Bandit B311, Low) | Security review | 41 | `random` is unsuitable for cryptographic choices; this featured-movie choice is not security-sensitive. | Used `secrets.choice` to remove the finding while retaining random selection. |
| Rating validation and unknown movie (manual review) | Bug / validation | 16–23 | Non-integer values could be accepted as ratings, and unknown titles failed with an implicit dictionary error. | Reject non-integer/out-of-range ratings and raise a clear `KeyError` for unknown titles. |
| Maintainability findings (Pylint) | Maintainability | Multiple | Missing docstrings, camelCase names, mutable global state, and an unnecessary `else` reduced clarity. | Added docstrings, changed names to snake_case, removed the global state, simplified the conditional, and added a main guard. |
| Style findings (Flake8) | Style | 35, 48, 70, 72 | Missing operator spacing, blank lines, comment spacing, and comma spacing. | Corrected whitespace and formatting; final Flake8 report is empty. |

## Final verification

Pylint: **10.00/10**. Bandit: **no issues identified**. Flake8: **no findings**. Final and initial reports are saved as `*_report.txt` and `*_initial_report.txt` respectively.
