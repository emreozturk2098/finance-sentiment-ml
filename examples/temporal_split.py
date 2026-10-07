"""New educational excerpt, not the original CS540 implementation."""

def expanding_windows(n_rows, initial_train=90, test_size=15, embargo=1):
    """Row-index example. An embargo drops the immediately preceding row.

    With a one-observation-ahead target this illustrates excluding a training
    label that depends on the first test row. Check real timestamps and signal
    availability separately, particularly for irregular calendar panels.
    """
    if min(initial_train, test_size) < 1 or embargo < 0:
        raise ValueError("Positive window sizes and non-negative embargo required")
    test_start = initial_train + embargo
    while test_start + test_size <= n_rows:
        yield range(0, test_start - embargo), range(test_start, test_start + test_size)
        test_start += test_size
