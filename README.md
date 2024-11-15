# Optimized Portfolio Allocation and Risk Analysis

## Overview

This script performs portfolio optimization and risk analysis for a multi-asset portfolio consisting of:
- **Bonds** (10-year Treasury Yield, `^TNX`)
- **Commodities** (Gold, `GLD`)
- **Cryptocurrency** (Bitcoin, `BTC-USD`)
- **Real Estate** (Real Estate ETF, `VNQ`)
- **Simulated Private Credit** (a low-volatility synthetic asset).

The goal is to construct a portfolio that meets a risk/return profile similar to the S&P 500 by optimizing for maximum Sharpe ratio while incorporating constraints on return, volatility, and diversification. Additional risk metrics such as **Value at Risk (VaR)**, **Conditional Value at Risk (CVaR)**, and **Maximum Drawdown** are calculated to provide a comprehensive view of portfolio risk.

---

## Features

1. **Asset Data Retrieval**:
   - Fetches historical price data for selected assets from Yahoo Finance.
   - Includes synthetic data for private credit as a low-volatility proxy.

2. **Portfolio Optimization**:
   - Uses the **Sharpe ratio** as the primary objective for optimization.
   - Constraints include:
     - Weights summing to 1 (fully allocated portfolio).
     - Target annualized return (≥8%).
     - Target annualized volatility (≤15%).
   - Includes a concentration penalty to avoid over-allocation to a single asset.

3. **Risk Metrics**:
   - **Annualized Return and Volatility**: Standard portfolio performance metrics.
   - **Sharpe Ratio**: Risk-adjusted performance.
   - **Value at Risk (VaR)**: Maximum expected loss at a 95% confidence level.
   - **Conditional Value at Risk (CVaR)**: Expected loss beyond the VaR threshold.
   - **Maximum Drawdown**: Largest historical loss from peak to trough.

4. **Visualization**:
   - Outputs a pie chart showing the optimized asset allocation.

---

## Requirements

### Libraries
The script requires the following Python libraries:
- `yfinance`: For fetching historical asset price data.
- `numpy`: For numerical computations.
- `pandas`: For data manipulation.
- `scipy`: For optimization.
- `matplotlib`: For data visualization.

Install the required libraries using pip:
```bash
pip install yfinance numpy pandas scipy matplotlib
```

---

## How to Run the Script

1. **Download and Prepare the Script**:
   Save the Python code into a file, e.g., `portfolio_optimization.py`.

2. **Run the Script**:
   Execute the script using Python:
   ```bash
   python portfolio_optimization.py
   ```

3. **View Results**:
   - The script will output:
     - Optimized portfolio weights.
     - Expected return, volatility, and Sharpe ratio.
     - Risk metrics (VaR, CVaR, Max Drawdown).
   - A pie chart visualizing the asset allocation will be displayed.

---

## Key Components of the Code

### Data Preparation
- Historical price data is fetched from Yahoo Finance.
- Daily percentage returns are calculated for each asset.
- Simulated private credit returns are generated as normally distributed data.

### Portfolio Optimization
- An objective function maximizes the Sharpe ratio while applying a concentration penalty.
- Constraints ensure portfolio diversification and alignment with the target risk/return profile.

### Risk Metrics
- **VaR and CVaR**: Quantify downside risks at a 95% confidence level.
- **Max Drawdown**: Measures historical worst-case loss.
- Additional metrics such as annualized return, volatility, and Sharpe ratio are included.

---

## Example Output

### Optimized Portfolio Weights:
```
          Asset    Weight
0          ^TNX    0.150
1           GLD    0.250
2       BTC-USD    0.300
3           VNQ    0.200
4  Private Credit    0.100
```

### Performance Metrics:
```
Expected Annual Return: 8.20 %
Expected Annual Volatility: 14.80 %
Sharpe Ratio: 0.42
Value at Risk (95%): -0.025
Conditional VaR (95%): -0.040
Maximum Drawdown: -0.25
```

### Visualization:
- A pie chart showing the allocation of each asset in the portfolio.

---

## Customization

1. **Modify Asset Universe**:
   - Replace or add tickers in the `assets` list to analyze a different set of assets.

2. **Adjust Constraints**:
   - Update `target_return` and `target_volatility` variables to reflect different objectives.

3. **Risk Metrics**:
   - Additional metrics can be implemented based on specific requirements (e.g., tracking error, information ratio).

---

## Potential Enhancements

- **Dynamic Constraints**: Adjust constraints dynamically based on historical performance.
- **Factor Analysis**: Incorporate factors like size, value, or momentum to guide optimization.
- **Multi-Objective Optimization**: Optimize for both Sharpe ratio and downside risk simultaneously.

---

## License

This script is provided for educational purposes and is free to use and modify. Attribution to the author is appreciated but not required.
```
