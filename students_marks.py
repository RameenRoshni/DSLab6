import pandas as pd
import matplotlib.pyplot as plt
# 1: Creating the dataset
data = {
    "Name": [" ali", "SARA ", "bilal", " Ayesha",
             "HAMZA", "zain ", "Noor", " usman "],
    "Marks": ["72", "85", "absent", "64",
              "90", "78", "81", "69"]
}
df = pd.DataFrame(data)
# 2: Cleaning student names
df["Name"] = df["Name"].str.strip().str.title()
# 3: Converting marks to numeric values
df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")
# 4: Filling absent marks with the mean
mean_marks = df["Marks"].mean()
df["Marks"] = df["Marks"].fillna(mean_marks)
# 5: Printing the cleaned DataFrame
print("Cleaned Student DataFrame:")
print(df)
print("\nMean used for absent mark:", mean_marks)
# 6: Creating a bar plot
plt.figure(figsize=(9, 5))
plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.ylim(0, 100)
plt.xticks(rotation=30)
plt.tight_layout()
# 7: Save and display the plot
plt.savefig("marks_bar.png")
plt.show()