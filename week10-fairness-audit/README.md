# Week 10: Fairness and Robustness Audit

## Overview

This assignment audits a vehicle detector for differences in recall
across vehicle classes and tests how image perturbations affect
detection.

## Implementation

-   `src/fairness_audit.py`: Computes IoU, matches detections to
    ground-truth boxes, calculates per-class recall, and flags classes
    below the recall threshold.
-   `src/adversarial.py`: Perturbs image colours, reruns the audit at
    different attack strengths, and ranks classes by recall drop.
-   `src/mock_detector.py`: Provided mock detector.
-   `src/run_pipeline.py`: Runs the audits and generates
    `fairness_report.json`.
-   `NOTES.md`: Records observations and answers the assignment
    questions.

## Setup

``` bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python generate_for_student.py --student-id <your-student-id>
```

## Run and test

``` bash
pytest tests/ -q
python src/run_pipeline.py
```

The pipeline creates `fairness_report.json`. Use its actual results to
complete `NOTES.md`.

## Submit

``` bash
git add -A
git commit -m "Week 10 fairness and robustness audit"
git tag week10-submit
git push origin main --tags
```

Do not edit the provided mock detector or pipeline unless the assignment
instructions say otherwise.
