import numpy as np
import pandas as pd

print("=" * 55)
print("   RUDRAEDGE RE-T1 TELEMETRY PROCESSING TEST")
print("=" * 55)

# 1. Generate synthetic telemetry data
np.random.seed(42)

records = 20

data = {
    "Temperature": np.random.uniform(20, 80, records),
    "Pressure": np.random.uniform(950, 1050, records),
    "Voltage": np.random.uniform(10, 14, records),
    "Altitude": np.random.uniform(100, 1000, records),
    "Speed": np.random.uniform(20, 150, records)
}

df = pd.DataFrame(data)

print("\n1. RAW TELEMETRY DATA")
print(df.head())

# 2. Artificially create some missing values
df.loc[3, "Temperature"] = np.nan
df.loc[7, "Voltage"] = np.nan
df.loc[12, "Altitude"] = np.nan

print("\n2. MISSING VALUES")
print(df.isnull().sum())

# 3. Calculate basic statistics
print("\n3. TELEMETRY STATISTICS")
print(df.describe().round(2))

# 4. Detect abnormal values
print("\n4. VALIDATION CHECK")

if (df["Temperature"] > 70).any():
    print("WARNING: High temperature detected")

if (df["Voltage"] < 11).any():
    print("WARNING: Low voltage detected")

if (df["Speed"] > 140).any():
    print("WARNING: High speed detected")

# 5. Fill missing values using column median
for column in df.columns:
    df[column] = df[column].fillna(df[column].median())

# 6. Verify cleaned data
print("\n5. CLEANED TELEMETRY DATA")
print(df.head())

print("\n6. FINAL CHECK")
print("Missing values remaining:")
print(df.isnull().sum())

# 7. Save processed telemetry
df.to_csv("processed_telemetry.csv", index=False)

print("\nProcessed telemetry saved successfully.")
print("File: processed_telemetry.csv")

print("\n" + "=" * 55)
print("          TELEMETRY TEST COMPLETED")
print("=" * 55)