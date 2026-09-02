# NOTES.md — Week 5: Model Registry Governance

**Student ID used with `generate_for_student.py`:**
<!-- paste the --student-id value you used -->
student_id: 112301034

## Which candidate reached Production, and why?

<!-- Which candidate ended up in Production, and why? -->
candidate_b reached production because its f1 score was 0.75, which is above the 0.70 limit. candidate_a had an f1 score of 0.556, so it could not be promoted.


## Gating stale feature data

<!-- What would you need to add to promote_model's gate if you also wanted
     to block promotion of a model trained on stale (e.g. >30-day-old)
     feature data? -->
i would add a check for the age of the training data in promote_model. if the data is more than 30 days old, the model should not be promoted to production.


## Scaling the gate to 40 candidates

<!-- Tying back to this week's AutoML/HPO framing: if a hyperparameter
     search had handed you 40 candidates instead of 2, what in your
     register_model/promote_model design would need to change (or
     genuinely wouldn't) to gate 40 instead of 2? -->
nothing major needs to change. register_model can create a separate version for each candidate and promote_model can apply the same rules to each candidate.