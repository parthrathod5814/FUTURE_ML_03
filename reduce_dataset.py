import pandas as pd
df = pd.read_csv("job_descriptions.csv")

small_df = df.sample(10000, random_state=42)

small_df.to_csv("jobs_small.csv", index=False)

print("✅ Smaller dataset created!")
