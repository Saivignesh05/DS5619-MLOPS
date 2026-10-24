# NOTES.md — Week 11: Model Compression Benchmark

**Student ID used with `generate_for_student.py`:**
<!-- paste the --student-id value you used -->
112301034


## pruned_dense_fp32 vs. pruned_sparse_coo

<!-- Compare pruned_dense_fp32 and pruned_sparse_coo in your report — same
     weights, same accuracy, very different size_bytes. Explain why in your
     own words (tie it to the lecture's pruning pitfall). -->
both have the same accuracy (98.33%) and the same weights, but pruned_dense_fp32 is 1024 bytes while pruned_sparse_coo is 616 bytes. this happens because dense storage still saves every zero as a 4-byte float, so pruning alone doesn't reduce the file size at all (the pruning pitfall from class). sparse coo format only stores the 77 non-zero weights with their indices (4 bytes value + 4 bytes index = 8 bytes each), which actually shrinks the size once more than half the weights are zero.


## The 0.95-sparsity experiment

<!-- Try editing PRUNE_SPARSITY in src/run_pipeline.py to 0.95 and re-run —
     what happens to accuracy, and why does that make sense given only 40
     of the 256 weights are actually informative? -->

