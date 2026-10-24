# Week 11 — Model Compression Benchmark

Track B (BMD-45 vehicle detection) · DS5619 Machine Learning Systems Operations

## Overview & Problem Statement

In this lab, we benchmark two core model compression techniques:
1. **Magnitude-based unstructured pruning**
2. **Symmetric INT8 quantization**

We evaluate their effects on the three key axes of the Pareto frontier: **model size**, **accuracy**, and **latency**.

The classification head is represented by a linear model with 256 weights in `data/weights.json`. It is deliberately over-parameterized: only 40 weights are informative (large magnitude correlated with labels), while the remaining 216 weights are near-zero noise. The test set in `data/eval_data.json` contains 300 labeled examples.

---

## What We Implemented

In `src/compression.py`, we implemented the five core compression functions:

- **`model_size_bytes(weights, dtype_bytes)`**:
  Calculates the raw uncompressed dense storage size (`len(weights) * dtype_bytes`).
- **`prune_weights(weights, sparsity)`**:
  Performs unstructured magnitude pruning by finding the fraction of weights with the smallest absolute values and zeroing them out without mutating the original weight list.
- **`sparse_coo_size_bytes(weights, value_bytes=4, index_bytes=4)`**:
  Calculates storage size in Coordinate (COO) format, where only non-zero entries are saved (`non_zero_count * (value_bytes + index_bytes)`).
- **`quantize_int8(weights)`**:
  Performs symmetric linear INT8 quantization by computing `scale = max(|w|) / 127`, rounding each weight to the nearest integer, and clamping within `[-127, 127]`.
- **`benchmark_model(label, weights, eval_examples, dtype_bytes, n_latency_reps=50)`**:
  Evaluates a weight configuration by computing its storage size, test accuracy over `eval_examples`, and average pass latency in milliseconds across repetitions using `time.perf_counter()`.

---

## How to Set Up & Run

### 1. Virtual Environment & Dependencies
```bash
python -m venv .venv
# On Windows PowerShell:
.\.venv\Scripts\Activate.ps1
# On Linux/macOS:
source .venv/bin/activate

pip install -r requirements.txt
```

### 2. Generate Student Data
Generate your unique weights and evaluation dataset using your student ID:
```bash
python generate_for_student.py --student-id 112301034
```

### 3. Run Self-Check Tests
Run pytest to verify all unit and smoke tests pass:
```bash
pytest tests/ -q
```

### 4. Run the Benchmark Pipeline
Run the driver script to evaluate baseline FP32, dense pruned FP32, sparse COO pruned, and INT8 quantized models:
```bash
python src/run_pipeline.py
```
This generates `compression_report.json`.

---

## Key Findings

1. **The Pruning Pitfall (Dense vs Sparse COO)**:
   - Simply setting weights to zero in dense storage (`pruned_dense_fp32`) saves **0 bytes** because each zero float still takes 4 bytes.
   - Using COO sparse storage (`pruned_sparse_coo`) saves actual space (shrinking from 1024 bytes down to 616 bytes at 70% sparsity) by storing only non-zero weights and their coordinate indices.

2. **The 0.95 Sparsity Cliff**:
   - At 70% sparsity, pruning only removes noise weights, keeping accuracy high (~98.33%).
   - At 95% sparsity, 243 out of 256 weights are pruned. Since only 216 weights are noise, 27 of the 40 informative weights get wiped out, causing accuracy to collapse down to 79.00%.

3. **INT8 Quantization**:
   - Compresses weights by exactly **4x** (from 4 bytes/weight to 1 byte/weight) while preserving near-baseline accuracy (~99.33%).
