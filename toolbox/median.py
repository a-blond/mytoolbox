def median(samples):
    """Return the standard deviation of a sample"""
    samples.sort()
    num_elem = len(samples)
    if num_elem%2 == 1:
        median = samples[(num_elem)//2]
    else:
        median = (samples[num_elem//2] + samples[(num_elem-2)//2])/2
    return median

