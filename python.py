import pandas as pd

# 1. Sample raw medical data
raw_data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'], # Direct Identifier (Must be removed)
    'Age': [23, 29, 32, 38, 21],                        # Quasi-identifier
    'ZIP': [10001, 10003, 90210, 90211, 10002],         # Quasi-identifier
    'Diagnosis': ['Flu', 'Cold', 'Flu', 'Diabetes', 'Cold'] # Sensitive Data
}
df = pd.DataFrame(raw_data)

# 2. HIPAA Safe Harbor: Drop direct identifiers entirely
df_dropped = df.drop(columns=['Name'])

# 3. Apply Mathematical Aggregation to achieve k-anonymity (k=3)
# We generalize Age into 10-year buckets and ZIP codes into 3-digit prefixes
df_dropped['Age_Group'] = pd.cut(df_dropped['Age'], bins=[20, 30, 40], labels=['20-29', '30-39'])
df_dropped['ZIP_Prefix'] = df_dropped['ZIP'].astype(str).str[:3] + 'XX'

# 4. Drop original granular columns
hipaa_compliant_df = df_dropped.drop(columns=['Age', 'ZIP'])

print(hipaa_compliant_df)
