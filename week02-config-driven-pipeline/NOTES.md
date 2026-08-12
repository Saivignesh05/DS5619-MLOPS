# NOTES.md — Week 2: Config-Driven Data Pipelines

**Student ID used with `generate_for_student.py`:**
student - id : 112301034

## What was hardcoded, and what would switching it have required?

<!-- What specifically was hardcoded in the original script, and what would
     have had to happen to change the threshold or switch formats before
     your refactor? -->

## What was hardcoded, and what would switching it have required?

The original pipeline hardcoded the inputpath, high value threshold, and output path as literal values in the Python code. It also used a CSV-specific loader, so the input format was assumed to  be CSV all the time. changing those hardcoded values like path,threshold,output path required to modify the source code which needs repeated modifications. Switching from CSV to JSON would have required changing the data loading logic to use a JSON loader. After refactoring and using the pipeline.py , these choices are provided through the YAML configuration, so the threshold, input format, input path, and output path can be changed without modifying pipeline.py.
cd ..