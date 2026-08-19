# NOTES.md — Week 3: ETL and Data Validation

**Student ID used with `generate_for_student.py`:**
<!-- paste the --student-id value you used -->
student-id : 112301034


## Quarantine count vs. the 7 known injected problems

<!-- How many rows ended up quarantined, and does that match the 7 known
     injected problems? (It won't match exactly — some rows may trip more
     than one expectation. Explain the discrepancy if there is one.) -->
6 rows ended up quarantined.

This does not exactly match the 7 known injected problems because some
rows can violate more than one expectation. The ETL pipeline quarantines
rows rather than individual violations, so multiple violations in the
same row count as one quarantined row.

The validation report records 8 total expectation violations across
6 quarantined rows. The provided expectation suite does not include
a country-code validation, so the invalid country-code problem
mentioned in the assignment is not detected by the current suite.