import numpy as np
import pandas as pd


def max_drawdown(mu, sigma, days):
    """Compute the maximum drawdon of a normally distributed return series."""
    ret_series = np.random.normal(mu, sigma, days)
    cum_ret = np.cumprod(1 + ret_series)
    
    peak = cum_ret[0]
    drawdown = []
    
    for x in cum_ret:
        peak = max(peak, x)
        dd = (peak - x) / peak
        drawdown.append(dd)
    
    mdd = max(drawdown)
    
    return mdd


def simulation(ann_vol, sharpe, year, num_sims):
    """Simulate drawdown for multiple return series drawn from the same normal distribution."""
    mu = ann_vol * sharpe / 252
    sigma = ann_vol / (252 ** 0.5)
    days = year * 252

    mdds = [max_drawdown(mu, sigma, days) for i in range(num_sims)]

    return mdds



def results_fn(ann_vol, sharpe, years, num_sims, breaches):
    """Display results of simualtions."""
    mdds = [simulation(ann_vol, sharpe, year, num_sims) for year in years]
    breach_probs = [[len([mdd for mdd in year if mdd > x]) / num_sims for x in breaches] for year in mdds]
    
    results = pd.DataFrame(breach_probs, index = ['Years: ' + str(year) for year in years],
                           columns = [str(100 * x) + '% DD' for x in breaches])
    
    return results


ann_vol = 0.07
sharpes = [1, 1.5, 2]
years = [1, 2, 3]
num_sims = 1000

breaches = [0.05, 0.075, 0.1]
results = pd.concat([results_fn(ann_vol, sharpe, years, num_sims, breaches) for sharpe in sharpes],
                     keys = ['Sharpe: ' + str(sharpe) for sharpe in sharpes])
