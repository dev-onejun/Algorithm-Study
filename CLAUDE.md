# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

A personal collection of competitive-programming / algorithm-study solutions, organized by year. The current focus (`2026/`) is **coding-interview preparation for job recruiting**. Earlier directories are archives of past study cohorts:

- `2019/` — group study (SketchAlgorithm), mostly C++
- `2020/` — self-study, mostly C++ (book: *알고리즘 문제 해결 전략*)
- `tutorials/` — Python solutions for *이것이 취업을 위한 코딩테스트다 with 파이썬*
- `2026/` — **active interview prep; new work goes here**
- Loose `.py` files at the repo root are recent CODEFORCES / problem solutions awaiting filing.

There is no build system, no test runner, and no package manifest. Each file is a standalone solution intended to be pasted into an online judge (Codeforces, BOJ, LeetCode, programmers, etc.).

## How to Assist on Interview Problems

When the user presents a problem in this repo, follow this workflow (this is the user's stated preference, captured from the `/init` invocation):

1. **Build test cases first.** Before writing any solution, derive a set of test cases from the problem statement: the sample I/O, edge cases (empty input, min/max bounds, all-equal, single element), and at least one stress case.
2. **Present solutions in stages.** Start with the brute-force / most obvious approach, then progressively optimize. For each stage, state the time and space complexity and explain what insight enables the next improvement.
3. **Run each stage against the test cases before claiming it works.** Use the language matching the surrounding directory (Python for `2026/`, `tutorials/`, and loose root `.py` files; C++ for `2019/` and `2020/`). Execute with `python3 file.py < input.txt` or `g++ -std=c++17 file.cpp && ./a.out < input.txt`. Do not claim a stage passes without showing the actual run.
4. **When the user submits their own solution, evaluate it.** Run it against the same test cases you prepared, then give feedback on correctness, time/space complexity, readability, edge cases they missed, and how it compares to the optimal approach. Don't just say "looks good" — point out concrete issues or confirm specific properties (e.g., "passes all 7 cases; O(n log n) — matches optimum").
5. The `.gitignore` already excludes `input*` files, so scratch input fixtures can be created at the repo root as `input.txt`, `input1.txt`, etc., without polluting git.

## Conventions

- **File naming:** problems are named after the problem title itself (e.g., `Ice Skating.py`, `BOARDCOVER.cpp`, `왕실의 나이트.py`) — Korean titles are written in Hangul, English titles in their original form. Spaces in filenames are intentional and accepted.
- **Commit messages** follow an all-caps verb prefix convention:
  - `SOLVE: <problem name>` — first working solution
  - `REVIEW: <problem name>` — revisited / improved solution (often references a sibling repo PR like `AlgoHoney#4`)
  - `UPDATE: <thing>` — meta changes (gitignore, READMEs, moves)
  - Keep this style for any new commits.
- **I/O style:** Python solutions use `input()` / `print()` directly (judge-style), not `argparse` or files. C++ solutions read from `cin` / write to `cout`. Don't refactor problems into functions-with-fixtures unless the user asks.
- Solutions are intentionally minimal — no logging, no CLI wrappers, no abstractions. Match that style.

## External Context

- `2020/README.md` and `tutorials/README.md` defer to GitHub issue **#1** on `dev-onejun/Algorithm-Study` for tips and study notes. Check there before duplicating notes in-repo.
- `REVIEW:` commits often pair with PRs in a sibling repo `AlgoHoney/WONJUN-PARK` — those are review threads, not this repo's PRs.
