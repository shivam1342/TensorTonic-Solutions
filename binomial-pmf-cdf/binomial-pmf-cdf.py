import numpy as np
from scipy.special import comb

def binomial_pmf_cdf(n, p, k):
    """
    Compute Binomial PMF and CDF.
    """
    # Write code here
    PMF = 0
    CDF = 0

    for i in range(k+1):
        n_choose_i = comb(n,i)
        PMF = n_choose_i * (p**i)*((1-p)**(n-i))
        CDF += PMF
    
    return (float(PMF), float(CDF))