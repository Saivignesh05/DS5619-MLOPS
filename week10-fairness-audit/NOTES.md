# NOTES.md — Week 10: Fairness and Robustness Audit

**Student ID used with `generate_for_student.py`:**
<!-- paste the --student-id value you used -->
112301034

## Which classes got flagged?

<!-- Which classes got flagged, and does that match what you'd expect given
     how generate_for_student.py built the fixtures? -->
The clean audit flags the vehicle classes whose recall is below 90%.
Bicycles and Two-wheelers are expected to be underperforming because
the synthetic dataset makes their bounding boxes smaller, making them
harder for the detector to detect. Other flagged classes may be affected
by sampling noise because each class has relatively few ground-truth
boxes.

The actual flagged classes are recorded in `fairness_report.json`.


## If the grouping variable were a protected attribute

<!-- Tying back to the framing note: what would change about this audit's
     stakes and your obligations as an engineer if the grouping variable
     were a protected demographic attribute instead of a vehicle class? -->
If the grouping variable were a protected demographic attribute,
the audit would have greater ethical and legal significance. Poor
performance for a protected group could lead to unfair treatment or
discrimination. As an engineer, I would investigate the causes of
disparities, validate the dataset's representativeness, evaluate
performance across groups, document limitations, and work to mitigate
unfair outcomes. I would also consider applicable laws, privacy,
accountability, and the consequences of deployment.

## Which attack could corrupt this audit?

<!-- Name one lifecycle stage and attack from the lecture (data poisoning,
     model theft, or adversarial examples) that could silently corrupt THIS
     audit's result, and one control from the lecture that would reduce the
     risk. -->
Adversarial examples could corrupt the audit by changing input images
so that the detector misses objects, causing measured recall to fall.
An attacker could also target particular classes, concealing the true
performance of the system. Input validation, controlled access to
audit data, integrity checks, and robustness testing would help reduce
these risks.

## Would SHAP or LIME explain a missed detection?

<!-- Pick one missed ground-truth box in a flagged class. An auditor asks
     you to explain WHY the detector missed it, not just that it did. Would
     SHAP or LIME actually help you answer that for a bounding-box detector
     — and if not, what's different about this detector's inputs/outputs
     that breaks the assumption both tools make? -->
SHAP and LIME are primarily designed to explain model predictions
through feature contributions or local approximations. This detector
uses a hand-written colour rule rather than a trained model. Its
decision depends on pixel thresholds: red must exceed 120, and red
must exceed green and blue by more than 40.

Consequently, a missed detection can be investigated by examining
the pixel colours, bounding-box size, connected regions, and threshold
conditions. Standard SHAP or LIME explanations would not directly
explain the detector's complete object-detection behaviour because
its output consists of variable-length bounding boxes, category IDs,
and confidence scores rather than a single fixed classification
output. Direct inspection of the rule and image is more appropriate
for this implementation.

## What did your attack show?

<!-- Using fairness_report.json["adversarial"]: at what eps does each flagged
     class fall further? Which class is most fragile, and is it the same
     class the clean audit flagged? Compare the drop ranking
     (most_fragile) with lowest_recall_under_attack — do they agree, and
     which is the better measure of who is hurt? What does that say about who bears the
     cost of an attack (or of an unmonitored failure)? Then: what would
     adversarial training or input validation look like for this detector,
     and why does a rule this simple break so much more easily than a CNN
     (or does it)? -->

The adversarial audit reduces red values and increases green and blue
values by a maximum of eps per channel. This pushes reddish pixels
toward or beyond the detector's colour thresholds, causing detections
to disappear.

The exact eps at which each flagged class loses recall, the most
fragile class, the recall-drop ranking, and the lowest-recall ranking
must be taken from `fairness_report.json`. A class with the largest
recall drop is not necessarily the class with the lowest absolute
recall under attack. The former measures damage relative to clean
performance, while the latter measures final performance.

Adversarial training would involve exposing a learned detector to
perturbed training examples and training it to remain accurate.
For this rule-based detector, conventional adversarial training is
not directly applicable because there are no learned parameters.
Input validation could check image dimensions, format, channel values,
and suspicious colour distributions, while robustness tests could
evaluate detection under controlled perturbations. However, validation
alone cannot guarantee robustness against all attacks.