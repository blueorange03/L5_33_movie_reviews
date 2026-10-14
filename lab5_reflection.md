# Lab 5 Reflection

Static analysis examines source code without requiring the program to run through every possible scenario. It helps surface security concerns, possible bugs, and style problems early so they can be reviewed and fixed consistently.

Bandit identified a high-severity MD5 use, a medium-severity all-interface host, and low-severity findings for a hard-coded password and standard pseudo-random selection. Pylint identified missing documentation, naming and maintainability issues, a global statement, and opportunities to simplify the code. Flake8 found four formatting problems.

I changed the review ID hash to SHA-256 while keeping its length, defaulted the stream host to loopback, removed the unused hard-coded password, and selected the featured movie with `secrets.choice`. I also improved rating validation and unknown-title errors, removed mutable global featured state, renamed functions to snake_case, added docstrings, and fixed the reported style problems.

The code is easier to read and rejects invalid ratings explicitly. Its final Pylint score is 10.00/10, Bandit identifies no issues, and Flake8 emits no findings. I ran the demo before and after the fixes; it continues to show the ratings, rankings, featured movie, review ID, stream address, and genres. The featured movie may vary because selection is random. I did not run a separate unit test suite.
