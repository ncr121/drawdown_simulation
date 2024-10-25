# drawdown_simulation

Simulate the probability of breaching 5% and 7.5% drawdown for a normally distributed P&L series with 7% annualised volatility (for different Sharpe Ratios)

Wrote simple yet highly useful tool to help credit pod inside multi-strategy hedge funds (HFs) risk-manage their overall portfolio prudently.

The results show that even for a successful trading strategy with a SR of 1.0, the probability of hitting the 5% barrier at some point in the 1st year of trading is alarmingly high at 56%. This finding is consistent with the risk management practice in most established multi-strategy HFs that cut capital by 50% for any pod that hits the 5% drawdown level and then take away the entire capital (i.e. the trading team is fired) if the 7.5% drawdown level is hit. 

In fact, credit distributions are fat-tailed and not Gaussian, so the true probability is even higher. These simulations all assume a 7% annualised volatility and a 0 interest rate environment (as was prevalent after GFC and for ease of calculating excess returns). In practice, multi-strategy HFs  can dissolve trading pods well before the 7.5% drawdown level and even before the 5% threshold is breached - so this table is a fundamental starting point risk template for all PMs managing capital (AUM) in a multi-strat fund.   
