# Dynamic-Pricing-and-Optimization-Engine
Dynamic Pricing and Optimization Engine 

A Python-based Dynamic Pricing and Optimization Engine that estimates price elasticity from historical sales data, predicts demand at different prices, and identifies the price that maximizes either revenue or profit.

The project combines econometric analysis, demand forecasting, and price optimization into a single command-line pricing tool.

Project Overview

Pricing decisions involve a trade-off between price, demand, revenue, and profit.
This project attempts to answer:
Given the current price and demand, what price should the business charge to maximize revenue or profit?

The system uses historical Price–Demand data to estimate price elasticity through a log-log linear regression model.
The estimated elasticity is then used to simulate demand across a user-defined price range.

The engine calculates:

Predicted demand
Revenue
Profit
Price and demand changes
Revenue-maximizing price
Profit-maximizing price

It also generates a visualization of the selected optimization objective against price.

How the Model Works
Historical Sales Data
        ↓
Data Validation & Cleaning
        ↓
Log-Log Regression
        ↓
Price Elasticity Estimation
        ↓
Current Price + Current Demand
        ↓
Demand Prediction at Different Prices
        ↓
Revenue & Profit Calculation
        ↓
Price Optimization
        ↓
Optimal Price Recommendation
        ↓
Revenue / Profit Curve

Key Features
1. Price Elasticity Estimation

The system can either:
Accept elasticity as a manual input, or
Automatically estimate elasticity from a CSV file.

For automatic estimation, the model uses:

[
\ln(Q) = \alpha + \beta\ln(P)
]

where:
(Q) = Demand
(P) = Price
(\beta) = Price Elasticity of Demand

Because this is a log-log regression, the estimated coefficient represents the percentage change in demand associated with a 1% change in price.
The model also reports the R² value.

2. Demand Prediction

Once elasticity has been estimated, the model predicts demand at alternative prices using:

Q_{current}
\left[
1+
E
\left(
\frac{P_{new}-P_{current}}{P_{current}}
\right)
\right]
]

where:

(Q_{current}) = Current demand
(P_{current}) = Current price
(P_{new}) = Alternative price
(E) = Estimated price elasticity

3. Revenue Optimization

Revenue is calculated as:

[
Revenue = Price \times Demand
]

The system evaluates multiple possible prices within the user-defined price range and selects the price generating the highest revenue.

4. Profit Optimization

Profit is calculated as:

[
Profit = (Price-Cost)\times Demand
]

The user provides the cost per unit, allowing the system to identify the price that maximizes total profit.

5. Price Scenario Analysis

The user specifies:

Current price
Current demand
Price range
Step size
Cost per unit
Optimization objective

The program then generates a table containing price, price change (in %),	predicted demand,	demand change (in %),	revenue, and	profit

6. Optimization Visualization

The program generates a graph showing either:
Revenue vs Price
or
Profit vs Price
The recommended price is highlighted on the graph.

Technologies Used:
Python
Pandas — data handling and preprocessing
NumPy — numerical calculations
Scikit-learn — linear regression and model evaluation
Matplotlib — visualization

Assumptions & Limitations

This project is an analytical pricing model, not a production pricing system.
The current model makes several simplifying assumptions:

Constant Elasticity:
The estimated elasticity is assumed to remain constant across the tested price range.

Price-Demand Relationship:
Demand prediction is based only on price elasticity and current demand.
Other factors such as-
Seasonality
Promotions
Competitor pricing
Consumer demographics
Inventory
Weather
Market conditions;
are not currently incorporated into the demand model.

Cost:
Cost per unit is entered manually and is assumed to remain constant across the tested prices.

Causal Interpretation:
The regression identifies an association between price and demand. It should not automatically be interpreted as a causal estimate because other factors affecting demand are not controlled for in the current model.

Future Improvements:
Potential extensions include:
Multiple product support
Region-wise pricing
Seasonality variables
Competitor pricing
Inventory constraints
Confidence intervals for elasticity
Statistical significance testing
Non-linear demand models
Scenario comparison
Historical vs optimized revenue comparison
