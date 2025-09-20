# CI/CD Pipeline Documentation

This document explains the *Continuous Integration* (CI) pipeline for MaskAI.

## Workflow Overview
The CI/CD workflow is defined in .github/workflows/ci.yml.
It runs automatically on every push to the main branch.

## Jobs
1. Build & Test
- Sets up Python environment (3.10).
- Installs project dependencies.
2. Linting 
- We use flake8 to enforce PEP8 style guidelines, maximum cyclomatic complexity of 10, and maximum line length of 127 characters.
3. Testing (Pytest)
- Runs unit tests (model masking functions).
- Runs integration tests (FastAPI endpoints).
- Verifies correct functionality before merge.

## 📝 Workflow File

    name: MaskAI CI/CD Workflow

    on:
    push:
        branches: [ "main" ]

    jobs:
    build_and_test:
        name: Code standard analysing
        runs-on: ubuntu-latest

        steps:
        - name: Checkout code
        uses: actions/checkout@v4

        - name: Set up Python 3.10
        uses: actions/setup-python@v3
        with:
            python-version: "3.10"

        - name: Install dependencies
        run: |
            python -m pip install --upgrade pip
            pip install flake8 pytest
            if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

        - name: Lint with flake8
        run: |
            # stop the build if there are Python syntax errors or undefined names
            flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
            # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
            flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
            
        - name: Test with pytest
        run: |
            pytest