# NOTES.md — Week 6: Containerize and Serve a Detector

**Student ID used with `generate_for_student.py`:**
<!-- paste the --student-id value you used -->
student-id : 112301034

## Built image size

<!-- What image size did `docker images` report for week6-detector? -->
image size :- disk usage is 246 mb and content size is 60.3 mb

## Swapping in a real checkpoint

<!-- What's the single biggest thing you'd change about this Dockerfile if
     src/mock_detector.py were swapped for a real torch-based checkpoint?
     (Think about what that does to build time and image size.) -->

The biggest change would be adding the Pytorch and model dependencies to the docker image. This would increase the build time and significantly increase the image size compared with the current flask + pillow image.