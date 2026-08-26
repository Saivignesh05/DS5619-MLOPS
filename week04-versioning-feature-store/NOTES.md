# NOTES.md — Week 4: Versioning, Feature Store & Lineage

**Student ID used with `generate_for_student.py`:**
student_id : 112301034


## v1 vs. v2 manifest comparison

The feature group version and source raw version are different: v1 uses raw version v1, while v2 uses raw version v2. The row count is also different (384 for v1 and 119 for v2). The feature schema remains the same.


## Why treat amount_minor_units differently from amount?

amount_minor_units is stored in cents, so it must be divided by 100 before calculating the aggregates. This keeps the v1 and v2 amounts comparable.
