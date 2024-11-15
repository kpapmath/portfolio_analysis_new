import numpy as np

def portfolio_performance(weights, mean_returns, cov_matrix):
    """
    Calculate portfolio return and volatility for a given set of weights.
    """
    returns = np.sum(mean_returns * weights)  # Weighted average return
    volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))  # Portfolio volatility
    return returns, volatility


def objective_function(weights, mean_returns, cov_matrix, risk_free_rate):
    """
    Objective function to maximize the Sharpe ratio while penalizing concentration.
    """
    # Calculate portfolio returns and volatility
    returns, volatility = portfolio_performance(weights, mean_returns, cov_matrix)

    # Calculate Sharpe ratio
    sharpe_ratio = (returns - risk_free_rate) / volatility

    # Add a concentration penalty to avoid over-concentration in a few assets
    concentration_penalty = np.sum(weights**2)  # Penalizes high concentration
    penalty_factor = 10  # Adjustable factor for the penalty strength

    # Return the negative of the Sharpe ratio (we're minimizing)
    return -sharpe_ratio + penalty_factor * concentration_penalty


def calculate_value_at_risk(returns, weights, confidence_level=0.95):
    """
    Calculate Value at Risk (VaR) at a given confidence level.
    """
    portfolio_returns = returns.dot(weights)
    var = -np.percentile(portfolio_returns, (1 - confidence_level) * 100)
    return var


def calculate_cvar(returns, weights, confidence_level=0.95):
    """
    Calculate Conditional Value at Risk (CVaR).
    """
    portfolio_returns = returns.dot(weights)
    var = calculate_value_at_risk(returns, weights, confidence_level)
    cvar = -portfolio_returns[portfolio_returns <= -var].mean()
    return cvar


def calculate_max_drawdown(portfolio_returns):
    """
    Calculate the maximum drawdown of the portfolio.
    """
    cumulative_returns = (1 + portfolio_returns).cumprod()
    peak = cumulative_returns.cummax()
    drawdown = (cumulative_returns - peak) / peak
    max_drawdown = drawdown.min()
    return max_drawdown


# Measures the sensitivity of the portfolio's returns to the market (e.g., S&P 500)
def calculate_beta(weights, returns, benchmark_returns):
    portfolio_returns = returns.dot(weights)
    covariance = np.cov(portfolio_returns, benchmark_returns)[0][1]  # Covariance between portfolio and benchmark
    benchmark_variance = np.var(benchmark_returns)  # Variance of the benchmark
    beta = covariance / benchmark_variance  # Beta = Covariance / Variance
    return beta