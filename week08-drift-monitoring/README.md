Lab 8 --- Drift and Observability Monitoring
Track B (BMD-45 vehicle detection) · Week 8 · DS5619 Machine Learning
Systems Operations

Background
BMD-45's paper reports a real domain-shift finding: a detector trained
on a different dataset scores only ~33.6% mAP when evaluated on
BMD-45's real-world CCTV footage, versus ~83.8% mAP for a detector
trained in-domain on BMD-45 itself --- the same kind of train/deploy
mismatch that drift monitoring exists to catch.
data/fixtures/camera_A_daylight/ and
data/fixtures/camera_B_lowlight/ are a synthetic, illustrative
stand-in for that idea --- same mock_detector.py, two different visual
conditions, deliberately built so the confidence-score distribution
differs between them.
You'll treat camera_A_daylight as the reference distribution (what
you'd expect from training-time-like conditions) and camera_B_lowlight
as live traffic you're monitoring.

workflow
first, generate the personalized camera data using the student id. the generated data contains two camera conditions: camera_a_daylight as the reference data and camera_b_lowlight as the live data. the mock detector is run on both camera folders to collect confidence scores from the detections.
next, the confidence score distributions from both cameras are compared using psi (population stability index). the psi value measures how much the live camera distribution has changed from the reference distribution. based on the psi value, the drift is classified as none, moderate, or significant.
finally, the pipeline generates drift_report.json containing the confidence statistics, psi value, and drift level. the implementation is checked using the provided tests, notes.md is completed with the results and observations, and the required files are committed and tagged for submission.

Source: this lab operationalizes the ML Observability and Drift
Detection (PSI, univariate feature drift) content from the Week 8
lecture deck. Dataset: Sharma et al., "BMD-45: A Large-Scale CCTV
Vehicle Detection Dataset for Urban Traffic," CVPR 2026 Findings.