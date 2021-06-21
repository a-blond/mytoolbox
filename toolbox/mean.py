def mean(samples):
    """Return the mean of a sample"""
    sum_ = 0
    for i in samples:
        sum_ += i
    return sum_/len(samples)
