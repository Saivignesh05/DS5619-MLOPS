Week 7 — CI/CD Integration Testing

This week, we implemented a CI pipeline using GitHub Actions to automatically check the Week 7 application.

What we implemented

We created .github/workflows/ci.yml with three jobs:

Lint

Sets up Python 3.11.
Installs dependencies from week07-cicd/requirements.txt.
Runs:
flake8 src/

Unit Test

Sets up Python 3.11.
Installs the same dependencies.
Runs:
pytest tests/ -q
These tests check the Flask application without Docker.

Integration Test

Runs only after both lint and unit-test succeed:
needs: ["lint", "unit-test"]
This avoids wasting CI time building a Docker container when the code already failed linting or unit tests.
How the integration test works

We completed:

scripts/integration_test.sh

It performs an actual end-to-end test of the Docker container:

Docker build->
Start container->
Wait for /health->
Send image to /detect ->
Check response contains "detections"->
Stop and remove container.

So we aren't just testing the Python code directly. We are testing the real Dockerized application, just like it would run as a deployed service.

Important fix we made

Initially GitHub Actions couldn't find requirements.txt because the Week 7 files are inside:

week07-cicd/

We therefore added:

defaults:
  run:
    working-directory: week07-cicd

to the jobs. This makes commands such as:

pip install -r requirements.txt

run from the correct directory.

Final result

Our final GitHub Actions run successfully completed:

lint
unit-test
integration-test

And the integration test successfully verified the actual Docker container, including /health and /detect.