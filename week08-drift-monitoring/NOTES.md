# NOTES.md — Week 8: Drift and Observability Monitoring

**Student ID used with `generate_for_student.py`:**
<!-- paste the --student-id value you used -->
112301034

## Drift level vs. expectation

<!-- What drift level did the report show, and does that match what you'd
     expect given the two cameras were built with deliberately different
     visual statistics? -->
the pipeline showed significant drift. this is expected because the daylight and lowlight cameras have different image conditions.

## What confidence-score-only monitoring misses

<!-- What would you monitor IN ADDITION to confidence score if you had
     access to ground-truth labels a day later? (Tie this to the kinds of
     drift from the lecture — which one does confidence-score-only
     monitoring miss?) -->
confidence scores do not tell whether the predictions are actually correct. if labels are available, we can also monitor precision, recall and f1 score.