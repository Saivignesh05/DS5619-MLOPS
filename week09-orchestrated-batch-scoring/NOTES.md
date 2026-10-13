# NOTES.md — Week 9: Orchestrated Batch Scoring

**Student ID used with `generate_for_student.py`:**
<!-- paste the --student-id value you used -->
112301034

## notify retry count

<!-- How many attempts did notify take in your run? (Check
     dag_run_summary.json.) -->
notify took 3 attempts to succeed.

## Branch independence

<!-- Why does load still succeed even though notify — its "sibling" in the
     DAG — failed on its first two attempts? What does that tell you about
     how failures in one branch of a DAG should (or shouldn't) affect an
     unrelated branch? -->
load succeeds because it depends only on score, not notify. A failure in one branch should not stop an unrelated branch from running.

## Retry cost under FinOps

<!-- Tying back to this week's FinOps content: if notify were a metered API
     call you paid for per attempt, what would you change about the retry
     strategy, and why is "retry every failed task the same way" a risky
     default once cost enters the picture? -->
For a metered API, I would use fewer retries, exponential backoff, and a retry limit. Retrying every failure equally can increase costs, especially for permanent errors that will not succeed on retry.