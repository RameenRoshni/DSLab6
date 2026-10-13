import pandas as pd
import matplotlib.pyplot as plt
# 1: Creating the inventory dataset
data = {
    "Product": [
        "Cola", "Chips", "Milk", "Biscuits", "Juice",
        "Yogurt", "Chocolate", "Water", "Cheese", "Crackers"
    ],
    "Category": [
        "beverages ", "SNACKS", " Dairy", "Snacks",
        "beverages", "DAIRY ", " snacks", "Beverages",
        "dairy", "SNACKS "
    ],
    "Price": [
        "Rs. 1,250", "Rs. 90", "Rs. 450", "Rs. 120",
        "Rs. 1,800", "Rs. 180", "Rs. 250", "Rs. 60",
        "Rs. 520", "Rs. 110"
    ],
    "Stock": [40, 120, 60, 90, 35, 50, 75, 150, 25, 80]
}
df = pd.DataFrame(data)
# 2: Cleaning category names
df["Category"] = df["Category"].str.strip().str.title()
# 3: Removing Rs. and commas, then converting prices
df["Price"] = (
    df["Price"]
    .str.replace("Rs. ", "", regex=False)
    .str.replace(",", "", regex=False)
    .astype(float)
)
# 4: Applying label encoding
df["Category_Code"] = df["Category"].astype("category").cat.codes
# 5: Printing the cleaned DataFrame
print("Cleaned Inventory DataFrame:")
print(df)
print("\nCategory Codes:")
print(
    df[["Category", "Category_Code"]]
    .drop_duplicates()
    .sort_values("Category_Code")
)
# 6: Calculate average price by category
average_price = df.groupby("Category")["Price"].mean()
average_price = average_price.sort_values(ascending=False)
# Calculate total stock by category
stock_by_category = df.groupby("Category")["Stock"].sum()
# 7: Create two plots side by side
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
# Bar plot
axes[0].bar(average_price.index, average_price.values)
axes[0].set_title("Average Price by Category")
axes[0].set_xlabel("Category")
axes[0].set_ylabel("Average Price (Rs.)")
axes[0].tick_params(axis="x", rotation=20)
# Pie chart
axes[1].pie(
    stock_by_category.values,
    labels=stock_by_category.index,
    autopct="%1.1f%%",
    startangle=90
)
axes[1].set_title("Share of Total Stock by Category")
# 8: Save and display both plots
plt.tight_layout()
plt.savefig("inventory_plots.png")
plt.show()