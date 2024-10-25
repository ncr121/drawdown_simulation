# drawdown_simulation

Compute the probability of breaching 5% and 7.5% drawdown for a normally distributed returned P&L series with 7% annualised volatility (for different Sharpe Ratios) using simulation

Simple yet highly useful exercise to help credit pod inside multi-strategy hedge funds (HFs) risk-manage the overall portfolio better. 
The results show that even for a successful trading strategy with a SR of 1.0, the probability of hitting the 5% barrier at some point in the 1st year of trading is alarmingly high at 56%. This finding is consistent with the risk management philosophy in the major multi-strategy HFs that cut capital by 50% for any pod that hits the 5% drawdown level and then takes away 100% capital (fires the pod)if the 7.5% drawdown level is hit. 

in fact credit distributions are fat-tailed and not Gaussian, so the true probability is even higher. These simulations all assume a 7% annualised volatility and a 0 interest rate environment (as was prevalent after GFC and for ease of calculating excess returns). In practice, multi-strategy HFs  can dissolve trading pods even before the 5% threshold is breached - so this table is a useful guideline for all PMs managing AUM in a multi-strat fund.   
