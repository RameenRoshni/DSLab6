
import pandas as pd
import matplotlib.pyplot as plt
# 1: Creating the messy weather dataset
data = {
    "Date": [
        "2026-09-01", "2026-09-02", "2026-09-03",
        "2026-09-04", "2026-09-05", "2026-09-06",
        "2026-09-07", "2026-09-08", "2026-09-09",
        "2026-09-10", "2026-09-11", "2026-09-12",
        "2026-09-13", "2026-09-14", "2026-09-15",
        "2026-09-03"
    ],
    "City": [
        " lahore", "LAHORE ", "Islamabad", " karachi",
        "LAHORE", "islamabad ", "Karachi", " LAHORE ",
        "ISLAMABAD", "karachi ", "Lahore", "ISLAMABAD ",
        "Karachi", "lahore ", "Islamabad", "Islamabad"
    ],
    "Temperature": [
        "32C", "33C", "30C", "34C", "31C", "29C",
        "35C", "32C", "28C", "34C", "33C", "29C",
        "36C", "31C", "30C", "30C"
    ],
    "Humidity": [
        55, 58, None, 49, 61, 65, None, 57,
        70, 52, 54, None, 45, 60, 63, None
    ],
    "Condition": [
        "sunny", " Sunny ", "CLOUDY", " Rainy",
        "SUNNY", "cloudy ", "RAINY", "sunny ",
        "Cloudy", " rainy ", "SUNNY", "CLOUDY ",
        "rainy", " sunny", "Cloudy", "CLOUDY"
    ]
}
df = pd.DataFrame(data)
# 2: Clean text columns
df["City"] = df["City"].str.strip().str.title()
df["Condition"] = df["Condition"].str.strip().str.title()
# 3: Convert temperature to numeric values
df["Temperature"] = pd.to_numeric(
    df["Temperature"].str.replace("C", "", regex=False),
    errors="coerce"
)
# 4: Convert dates into datetime format
df["Date"] = pd.to_datetime(df["Date"])
# 5: Remove duplicate rows
df = df.drop_duplicates().copy()
print("Rows after dropping duplicates:", len(df))
# 6: Fill missing humidity with median
humidity_median = df["Humidity"].median()
df["Humidity"] = df["Humidity"].fillna(humidity_median)
print("Missing Humidity filled with median:", humidity_median)
# 7: One-hot encode the Condition column
df_encoded = pd.get_dummies(
    df,
    columns=["Condition"],
    dtype=int
)
condition_columns = [
    col for col in df_encoded.columns
    if col.startswith("Condition_")
]
print("\nOne-hot encoded Condition columns:")
print(df_encoded[condition_columns])
# 8: Calculate correlation
correlation = df["Temperature"].corr(df["Humidity"])
print(
    "\nCorrelation (Temperature, Humidity):",
    round(correlation, 2)
)
# 9: Print weather condition counts
condition_counts = df["Condition"].value_counts()
print("\nCondition counts:")
print(condition_counts)
# 10: Create four plots in a 2 x 2 figure
fig, axes = plt.subplots(2, 2, figsize=(12, 9))
# Plot 1: Temperature over time
axes[0, 0].plot(
    df["Date"],
    df["Temperature"],
    marker="o"
)
axes[0, 0].set_title("Temperature Over Time")
axes[0, 0].set_xlabel("Date")
axes[0, 0].set_ylabel("Temperature (C)")
axes[0, 0].tick_params(axis="x", rotation=35)
# Plot 2: Temperature versus humidity
axes[0, 1].scatter(
    df["Temperature"],
    df["Humidity"]
)
axes[0, 1].set_title("Temperature vs. Humidity")
axes[0, 1].set_xlabel("Temperature (C)")
axes[0, 1].set_ylabel("Humidity (%)")
# Plot 3: Pie chart of weather conditions
axes[1, 0].pie(
    condition_counts.values,
    labels=condition_counts.index,
    autopct="%1.1f%%",
    startangle=90
)
axes[1, 0].set_title("Weather Condition Counts")
# Plot 4: Temperature histogram
axes[1, 1].hist(
    df["Temperature"],
    bins=5,
    edgecolor="black"
)
axes[1, 1].set_title("Temperature Distribution")
axes[1, 1].set_xlabel("Temperature (C)")
axes[1, 1].set_ylabel("Number of Days")
# 11: Add overall title and save dashboard
fig.suptitle("Weather Overview", fontsize=16)
fig.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig("weather_dashboard.png")
plt.show()