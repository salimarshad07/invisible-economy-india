import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Load data
df = pd.read_excel("svanidhi_2026_live.xlsx")

# Calculated columns
df['conversion_rate'] = (df['loans_disbursed_2026'] / df['eligible_applications_2026']) * 100
df['repayment_rate'] = (df['loans_repaid_2026'] / df['loans_disbursed_2026']) * 100
df['digital_adoption'] = (df['digitally_active_2026'] / df['beneficiaries_2026']) * 100

# Chart 1 - Top 10 states by beneficiaries
top10 = df.nlargest(10, 'beneficiaries_2026')

plt.figure(figsize=(12, 6))
plt.barh(top10['state_ut'], top10['beneficiaries_2026'], color='steelblue')
plt.xlabel('Number of Beneficiaries')
plt.title('Top 10 States by PM SVANidhi Beneficiaries (2026)')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('top10_beneficiaries.png', dpi=150, bbox_inches='tight')
plt.close()
print("Chart 1 saved.")

# Chart 2 - Bottom 10 repayment rates
bottom10 = df.nsmallest(10, 'repayment_rate')

plt.figure(figsize=(12, 6))
plt.barh(bottom10['state_ut'], bottom10['repayment_rate'], color='tomato')
plt.xlabel('Repayment Rate (%)')
plt.title('Bottom 10 States by Loan Repayment Rate (2026)')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('bottom10_repayment.png', dpi=150, bbox_inches='tight')
plt.close()
print("Chart 2 saved.")

print("Done. Check your Projects folder.")