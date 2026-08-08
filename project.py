import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# =====================================================
# FUNCTION TO CALCULATE ELASTICITY FROM CSV
# =====================================================

def calculate_elasticity_from_csv(file_name):

    data = pd.read_csv(file_name)

    # Check required columns
    if "Price" not in data.columns or "Demand" not in data.columns:
        raise ValueError(
            "CSV must contain 'Price' and 'Demand' columns"
        )

    price = data["Price"]
    demand = data["Demand"]

    # Remove invalid values
    data = data[
        (price > 0) &
        (demand > 0)
    ]

    price = data["Price"]
    demand = data["Demand"]


    # Log-log regression
    log_price = np.log(price).values.reshape(-1,1)
    log_demand = np.log(demand)


    model = LinearRegression()

    model.fit(
        log_price,
        log_demand
    )


    elasticity = model.coef_[0]

    r2_score = model.score(
        log_price,
        log_demand
    )


    return elasticity, r2_score


# =====================================================
# FUNCTION TO PREDICT DEMAND
# =====================================================

def predict_demand(current_price, current_demand, elasticity, new_price):

    price_change = (new_price - current_price) / current_price

    demand_change = elasticity * price_change

    predicted_demand = current_demand * (1 + demand_change)

    return predicted_demand


# =====================================================
# FUNCTION TO CALCULATE REVENUE
# =====================================================

def calculate_revenue(price, demand):

    return price * demand


# =====================================================
# FUNCTION TO CALCULATE PROFIT
# =====================================================

def calculate_profit(price, demand, cost):

    return (price - cost) * demand


# =====================================================
# MAIN PROGRAM
# =====================================================

print("=" * 50)
print("      DYNAMIC PRICING AND OPTIMIZATION ENGINE")
print("=" * 50)

print("\nOptimization Objective")
print("1. Revenue Maximization")
print("2. Profit Maximization")

choice = int(input("\nChoose Optimization Objective (1 or 2): "))

# current_price = float(input("\nCurrent Price: "))
# current_demand = float(input("Current Demand: "))
# elasticity = float(input("Elasticity : "))

current_price = float(input("\nCurrent Price: "))
current_demand = float(input("Current Demand: "))


print("\nElasticity Method")
print("1. Enter Elasticity manually")
print("2. Calculate Elasticity from CSV")


elasticity_choice = int(
    input("Choose option: ")
)


if elasticity_choice == 1:

    elasticity = float(
        input("Elasticity : ")
    )


else:

    csv_file = input(
        "Enter CSV file name: "
    )

    elasticity, r2 = calculate_elasticity_from_csv(
        csv_file
    )


    print("\nElasticity Calculated Automatically")
    print("-----------------------------------")
    print(f"Elasticity : {elasticity:.4f}")
    print(f"Model Accuracy (R²): {r2:.4f}")

price_range = float(input("Price Range (%) : "))
step_size = float(input("Step Size : "))

cost = float(input("Cost per Unit: "))


# =====================================================
# GENERATE PRICE LIST
# =====================================================

min_price = current_price * (1 - price_range / 100)

max_price = current_price * (1 + price_range / 100)

step = current_price * step_size / 100

prices = np.arange(min_price, max_price + 0.001, step)


# =====================================================
# SIMULATION
# =====================================================

results = []

for price in prices:

    demand = predict_demand(
        current_price,
        current_demand,
        elasticity,
        price
    )

    revenue = calculate_revenue(price, demand)

    profit = calculate_profit(
        price,
        demand,
        cost,
    )

    demand_change = (
        (demand - current_demand)
        / current_demand
    ) * 100

    price_change = (
        (price - current_price)
        / current_price
    ) * 100

    results.append([
        round(price, 2),
        round(price_change, 2),
        round(demand, 2),
        round(demand_change, 2),
        round(revenue, 2),
        round(profit, 2)
    ])


# =====================================================
# CREATE DATAFRAME
# =====================================================

df = pd.DataFrame(
    results,
    columns=[
        "Price",
        "Price Change %",
        "Predicted Demand",
        "Demand Change %",
        "Revenue",
        "Profit"
    ]
)


# =====================================================
# FIND OPTIMUM
# =====================================================

if choice == 1:
    optimum = df.loc[df["Revenue"].idxmax()]
    objective = "Revenue Maximization"

else:
    optimum = df.loc[df["Profit"].idxmax()]
    objective = "Profit Maximization"


# =====================================================
# DISPLAY RESULTS
# =====================================================

print("\n")
print("=" * 80)
print("PRICE OPTIMIZATION RESULTS")
print("=" * 80)

print(df.to_string(index=False))

print("\n")
print("=" * 80)
print("OPTIMAL SOLUTION")
print("=" * 80)

print(f"Objective          : {objective}")
print(f"Optimal Price      : {optimum['Price']:.2f}")
print(f"Predicted Demand   : {optimum['Predicted Demand']:.2f}")
print(f"Revenue            : {optimum['Revenue']:.2f}")
print(f"Profit             : {optimum['Profit']:.2f}")

# =====================================================
# PLOT GRAPH
# =====================================================

if choice == 1:
    y = df["Revenue"]
    ylabel = "Revenue"
    title = "Revenue vs Price"
else:
    y = df["Profit"]
    ylabel = "Profit"
    title = "Profit vs Price"


plt.figure(figsize=(10,6))

plt.plot(
    df["Price"],
    y,
    marker="o",
    linewidth=2
)

plt.scatter(
    optimum["Price"],
    optimum[ylabel],
    s=180,
    color="red",
    label="Optimal Price"
)

plt.annotate(
    f"Optimal\n{optimum['Price']}",
    (optimum["Price"], optimum[ylabel]),
    xytext=(10,15),
    textcoords="offset points"
)

plt.xlabel("Price")
plt.ylabel(ylabel)
plt.title(title)

plt.grid(True)

plt.legend()

plt.show()