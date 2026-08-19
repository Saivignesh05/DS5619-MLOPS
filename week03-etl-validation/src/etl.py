"""
Extract -> Validate -> Transform -> Load pipeline for the fraud transaction
data. Run with:

    python src/etl.py --config config.yaml

(a default config.yaml pointing at data/raw_transactions.csv is provided)
"""
import argparse
import csv
import json
import os
import sys

import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import expectations as exp

KNOWN_CATEGORIES = {
    "grocery", "electronics", "fuel", "travel", "restaurant",
    "online_retail", "utilities", "pharmacy", "entertainment", "atm_withdrawal",
}


def build_expectation_suite():
    """The data contract for this dataset. Each entry says which expectation
    function to run, and with what arguments. This is provided — read it to
    know exactly what your expectation functions in expectations.py need to
    handle correctly.
    """
    return [
        (exp.expect_column_not_null, {"column": "amount"}),
        (exp.expect_column_not_null, {"column": "card_id"}),
        (exp.expect_column_positive, {"column": "amount"}),
        (exp.expect_column_in_set, {"column": "merchant_category", "allowed_values": KNOWN_CATEGORIES}),
        (exp.expect_column_unique, {"column": "transaction_id"}),
    ]


def extract(input_path):
    with open(input_path, newline="") as f:
        return list(csv.DictReader(f))


def run_etl(config):
    """Implement the four ETL steps described in ASSIGNMENT.md:
    extract, validate (run every expectation in build_expectation_suite()
    and collect ALL violations, not just the first), transform (split into
    clean vs quarantined rows — a row with ANY violation is quarantined),
    load (write clean_output_path, quarantine_output_path, and
    report_output_path as described in the assignment).

    Return the validation_report dict as well as writing it to disk.
    """
    """Run the ETL pipeline: extract, validate, transform, and load."""

    # 1. Extract
    rows = extract(config["input_path"])

    # 2. Validate
    expectations = build_expectation_suite()

    all_violations = []

    for expectation_func, kwargs in expectations:
        violations = expectation_func(rows, **kwargs)
        all_violations.extend(violations)

    # 3. Group violations by row
    violated_row_indices = {
        violation.row_index
        for violation in all_violations
    }

    # 4. Transform
    clean_rows = []
    quarantined_rows = []

    for index, row in enumerate(rows):
        if index in violated_row_indices:
            quarantined_rows.append(row)
        else:
            clean_rows.append(row)

    # 5. Build validation report
    report = {
        "total_rows": len(rows),
        "clean_rows": len(clean_rows),
        "quarantined_rows": len(quarantined_rows),
        "expectations": []
    }

    for expectation_func, kwargs in expectations:
        expectation_name = expectation_func.__name__

        violations = [
            violation
            for violation in all_violations
            if violation.expectation == expectation_name
        ]

        report["expectations"].append({
            "expectation": expectation_name,
            "column": kwargs["column"],
            "n_violations": len(violations),
            "row_indices": [v.row_index for v in violations]
        })

    # 6. Load clean transactions
    fieldnames = list(rows[0].keys())

    with open(config["clean_output_path"], "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(clean_rows)

    # 7. Load quarantined transactions
    with open(config["quarantine_output_path"], "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(quarantined_rows)

    # 8. Load validation report
    with open(config["report_output_path"], "w") as f:
        json.dump(report, f, indent=2)

    return report


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="config.yaml")
    args = parser.parse_args()

    with open(args.config) as f:
        config = yaml.safe_load(f)

    report = run_etl(config)
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
