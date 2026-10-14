# Lab 5 Issue Table

Initial findings came from the unmodified `movie_reviews.py`. Line numbers below refer to that initial version; tool findings were reviewed for relevance before making changes.

| Issue | Type | Line(s) | Description | Fix Approach |
|-------|------|---------|-------------|--------------|
| MD5 used for review identifiers (Bandit B324, High) | Security | 46 | MD5 is a weak hash and Bandit flags it as unsuitable for security-sensitive use. Review identifiers do not require a cryptographic hash, but retaining MD5 creates a weak-hash pattern and avoidable collision risk. | Replaced it with SHA-256 while preserving the 10-character identifier format. |
| Listen host exposes all interfaces (Bandit B104, Medium) | Security | 4 | `0.0.0.0` allows a bound service to listen on every network interface, potentially exposing it beyond the local machine. | Changed the default host to `127.0.0.1` (loopback). |
| Hard-coded moderator password (Bandit B105, Low) | Security | 6 | A plaintext password is embedded in source code and is unused by the demo. | Removed the unused credential rather than keeping a secret in source. |
| Weak validation and unchecked movie lookup (manual review) | Bug / input validation | 16–23 | Non-integer ratings could reach the rating list, and an unknown movie caused an implicit `KeyError` with little context. | Reject non-integer and out-of-range ratings; raise a clear `KeyError` for unknown movie titles. |
| Module globals and `global` assignment (Pylint W0603) | Maintainability | 8, 40–42 | Featured movie state required a mutable module global, making the picker harder to reason about. | Removed the global state and made the picker return the selection directly; handle an empty catalogue with `None`. |
| Style and readability findings (Pylint / Flake8) | Style | 1–72 | Missing docstrings, camelCase identifiers, unnecessary `else`, manual index iteration, and spacing issues reduced readability and lint quality. | Added docstrings, renamed functions/parameters to snake_case, simplified the conditional, used `enumerate`, and corrected whitespace. |
| Pseudo-random selection warning (Bandit B311, Low) | Security review | 41 | Bandit warns that `random` is not suitable for security-sensitive randomness. This selection is for a non-security featured-movie demo, so the finding was low risk in context. | Switched selection to `secrets.choice`, which removes the warning and remains a random choice. |

## Verification

After changes, Pylint reports **10.00/10**, Bandit reports **no issues**, and Flake8 reports no findings. The final reports are in `pylint_report.txt`, `bandit_report.txt`, and `flake8_report.txt`. Initial reports are retained as `*_initial_report.txt` for comparison.
