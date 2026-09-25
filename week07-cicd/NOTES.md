# NOTES.md — Week 7: CI/CD Integration Testing

**Student ID used with `generate_for_student.py`:**
<!-- paste the --student-id value you used -->
student-id :112301034

## Why gate integration-test on needs: [lint, unit-test]?

<!-- Why does integration-test need needs: [lint, unit-test] instead of
     just running in parallel with them — what's the actual cost being
     avoided? -->
The integration test builds and runs a Docker container, which takes more CI time and resources than linting or unit tests. Using needs: [lint, unit-test] prevents the Docker integration test from running when either lint or unit tests fail.