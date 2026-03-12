# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Python learning and algorithm practice repository. Structured class exercises progress from basics to intermediate topics, plus LeetCode solutions.

## Running Scripts

```bash
# Activate virtual environment (Windows Git Bash)
source .venv/Scripts/activate

# Run any exercise
python workspaces/101/clase_1.py

# Run LeetCode solutions
python workspaces/leetcode/mergeSortedArray.py
```

No build system, test framework, or linter is configured. Scripts are run directly with Python 3.13.

## Dependencies

- pygame (only for clase_8)
- Install: `pip install pygame`

## Structure

- `workspaces/101/` — Class exercises (clase_1 through clase_8), each a standalone Python script
- `workspaces/leetcode/` — LeetCode solutions with multiple approaches and complexity analysis in comments

## Conventions

- Exercise files are named `clase_N.py` with variants like `clase_N_2.py`
- LeetCode solutions include Big-O complexity comments for each approach
- All code is in Spanish learning context (variable names, comments may be in Spanish)
