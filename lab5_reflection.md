# Lab 5 Reflection

Static analysis checks source code without needing to exercise every path at runtime. It helps find security risks, likely bugs, and style problems early, and gives maintainers a repeatable way to check improvements.

## What the tools detected

- **Bandit** found a high-severity MD5 use, a medium-severity all-interface bind address, and low-severity findings for a hard-coded password and use of the standard pseudo-random generator.
- **Pylint** found missing documentation, naming and maintainability issues, use of a `global` statement, an unnecessary `else`, and a loop that could use `enumerate`.
- **Flake8** found whitespace and line formatting violations.

## What I changed

I replaced MD5 with SHA-256 while keeping review IDs at ten hexadecimal characters, changed the stream host default to loopback, removed the unused hard-coded password, and used `secrets.choice` for the featured movie. I also added rating type/range validation, made unknown movie errors clearer, removed the featured-movie global, documented and renamed functions, simplified the average calculation, used `enumerate`, and corrected style issues.

## How quality improved

The resulting code has no findings in the final Bandit or Flake8 reports and scores 10.00/10 in Pylint. The demo still adds movies, accepts valid ratings, rejects the six-star example, prints averages and rankings, selects a featured title, and generates a review ID. The host now defaults to local-only access, and input failures are handled more clearly.

## Verification performed

I ran `movie_reviews.py` before and after the edits, and reran all three analysis tools after the edits. Their output is saved in the final report files. The featured title is intentionally random, so it may differ across runs. No separate unit test suite was present or run.
