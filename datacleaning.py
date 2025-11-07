import pandas as pd

# -----------------------------
# 1. Load the dataset
# -----------------------------
df = pd.read_csv("your_file.csv")

# See first few rows
print("Initial Data:")
print(df.head())

# -----------------------------
# 2. Check basic info
# -----------------------------
print("\nDataset Info:")
print(df.info())

# -----------------------------
# 3. Handle missing values
# -----------------------------

# Option A: Remove rows with missing values
df_dropna = df.dropna()

# Option B: Fill missing values
df_filled = df.fillna({
    'Column1': 0,            # numeric column
    'Column2': 'Unknown',    # categorical column
})

# -----------------------------
# 4. Remove duplicates
# -----------------------------
df = df.drop_duplicates()

# -----------------------------
# 5. Convert data types
# -----------------------------
df['Column1'] = df['Column1'].astype(float)      # example convert to float
df['DateColumn'] = pd.to_datetime(df['DateColumn'], errors='coerce')

# -----------------------------
# 6. Remove outliers (simple rule)
# -----------------------------
# Example: Remove values greater than 3 standard deviations
numeric_col = 'Column1'
df = df[(df[numeric_col] < df[numeric_col].mean() + 3*df[numeric_col].std()) &
        (df[numeric_col] > df[numeric_col].mean() - 3*df[numeric_col].std())]

# -----------------------------
# 7. Rename columns (clean names)
# -----------------------------
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# -----------------------------
# 8. Save cleaned file
# -----------------------------
df.to_csv("cleaned_data.csv", index=False)

print("\n✅ Cleaning complete! Saved as cleaned_data.csv")
