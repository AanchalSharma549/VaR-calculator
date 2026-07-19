import pandas as pd
from scipy import stats
import numpy as np


# Load data
df = pd.read_csv('stockdata.csv')

# Calculate returns
df['Returns'] = df['Close'].pct_change()

# Remove NaN values (first row has no previous price)
df = df.dropna()

# Show results
print("Data loaded, returns calculated, NaN removed!")
print(f"\nTotal rows after cleanup: {len(df)}")
print(f"Mean daily return: {df['Returns'].mean():.6f}")
print(f"Daily volatility (std dev): {df['Returns'].std():.6f}")

print("\nFirst 5 rows:")
print(df[['Date', 'Close', 'Returns']].head(5))
confidence_level=0.95
var_historical=df['Returns'].quantile(1-confidence_level)
print( '='*20)
print('METHOD 1 : HISTORICAL VAR')
print('='*20)
print(f"VAR at {confidence_level*100:.0f}% confidence:{var_historical:.4f}")
print(f"Interpretation: On 95% of the days, loss won't exceed {abs(var_historical)*100:.2f}")
z_score= stats.norm.ppf(1-confidence_level)
mean_return=df['Returns'].mean()
std_dev=df['Returns'].std()
var_parametric=mean_return+(z_score * std_dev)
print("\n"+"="*50)
print(f"METHOD-2: PARAMETRIC")
print("="*50)
print(f"Mean return: {mean_return:.6f}")
print(f"Volatility: {std_dev:.4f}")
print(f"Z score at {confidence_level*100:.0f}% : {z_score:.4f}")
print(f"VaR at {confidence_level*100:.0f}% confidence: {var_parametric:.4f}")
print(f"Interpretation: If it follows normal distribution,")
print(f"                 then the loss won't exceed: {abs(var_parametric)*100:.2f} %")
np.random.seed(42)
num_simulations= 10000
simulated_returns= np.random.normal(mean_return, std_dev,num_simulations)
var_mc=np.percentile(simulated_returns, 5)
print("="*50)
print(f"METHOD 3: MONTE CARLO")
print("="*50)
print(f"no. of simulations: {num_simulations:,}")
print(f"VaR at {confidence_level*100:.0f}% confidence:{var_mc:.4f}")
print(f"Interpretation: In simulated returns,")
print(f"            the loss won't exceed: {abs(var_mc)*100:.2f} %")
# ===== STEP 4: COMPARISON - ALL 3 METHODS =====
print("\n" + "="*50)
print("SUMMARY: VaR COMPARISON")
print("="*50)

methods = ['Historical', 'Parametric', 'Monte Carlo']
var_values = [var_historical, var_parametric, var_mc]

# Create a comparison dataframe
comparison_df = pd.DataFrame({
    'Method': methods,
    'VaR (95%)': var_values,
    'Daily Loss %': [abs(v)*100 for v in var_values]
})

print(comparison_df.to_string(index=False))

print("\n" + "="*50)
print("KEY INSIGHTS:")
print("="*50)
print(f"Most conservative (highest loss): {methods[var_values.index(max(var_values))]}")
print(f"  VaR = {abs(max(var_values))*100:.2f}%")
print(f"\nMost optimistic (lowest loss): {methods[var_values.index(min(var_values))]}")
print(f"  VaR = {abs(min(var_values))*100:.2f}%")
print(f"\nAverage across all 3 methods: {abs(np.mean(var_values))*100:.2f}%")
# ===== STEP 5: FINAL SUMMARY - BUSINESS INTERPRETATION =====
print("\n" + "="*70)
print("WHAT THIS MEANS")
print("="*70)

avg_var = abs(np.mean(var_values)) * 100

print(f"\nBased on {len(df):,} days of historical data (20 years):")

print(f"\n--- IF YOU INVEST $100,000 ---")
print(f"On a bad day (worst 5%), you could lose: ${100000 * (avg_var/100):,.2f}")

print(f"\n--- IF YOU INVEST $1,000,000 ---")
print(f"On a bad day (worst 5%), you could lose: ${1000000 * (avg_var/100):,.2f}")

print(f"\n--- IF YOU INVEST $10,000,000 ---")
print(f"On a bad day (worst 5%), you could lose: ${10000000 * (avg_var/100):,.2f}")

print(f"\n" + "="*70)
print("IMPORTANT: WHAT '95% CONFIDENCE' REALLY MEANS")
print("="*70)
print(f"- Out of 100 trading days, on ~5 days, losses COULD EXCEED this amount")
print(f"- It's NOT a maximum loss, extreme events can be FAR worse")
print(f"- It's a boundary, not a guarantee")

print(f"\n" + "="*70)
print("WHY WE USE 3 METHODS")
print("="*70)
print(f"Historical:   Uses actual past data")
print(f"              Pros: Real events, no assumptions")
print(f"              Cons: Past != Future, can miss rare events")

print(f"\nParametric:   Assumes bell curve distribution")
print(f"              Pros: Fast calculation, simple formula")
print(f"              Cons: Returns often NOT bell curves (fat tails)")

print(f"\nMonte Carlo:  Generates random scenarios")
print(f"              Pros: Flexible, can model complex patterns")
print(f"              Cons: Computationally heavy, randomness varies")

print(f"\n" + "="*70)
print("RECOMMENDATION FOR RISK MANAGEMENT")
print("="*70)
print(f"Use AVERAGE VaR = {avg_var:.2f}% as your risk estimate")
print(f"This is the middle ground of all 3 methods")
print(f"1 Not too conservative")
print(f"2 Not too aggressive")
print(f"3 Balances all three approaches")
print("="*70)