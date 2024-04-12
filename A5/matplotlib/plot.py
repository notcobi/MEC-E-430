import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read data from csv file
df = pd.read_excel(r"A4\matplotlib\data.xlsx", sheet_name="data")

# declare variables
P_e = df["P_e"]
V_e = df["V_e"]
P_b = df["P_b"]
m = df["m"]

# plot P_e vs P_b
plt.figure()
plt.plot(P_b, P_e, '-k', label='P_e vs P_b')
# plt.xlabel('$, Back pressure (kPa)')
# plt.ylabel('P_e, Exit pressure (kPa)')
plt.xlabel('$P_b$, Back pressure (kPa)')
plt.ylabel('$P_e$, Exit pressure (kPa)')
plt.savefig(r'A4\Questions\Figures\P_e_vs_P_b.png', dpi=300, bbox_inches='tight')

# plot V_e vs P_b
plt.figure()
plt.plot(P_b, V_e, '-k', label='V_e vs P_b')
plt.xlabel('$P_b$, Back pressure (kPa)')
plt.ylabel('$V_e$, Exit velocity (m/s)')
plt.savefig(r'A4\Questions\Figures\V_e_vs_P_b.png', dpi=300, bbox_inches='tight')

# plot m vs P_b
plt.figure()
plt.plot(P_b, m, '-k', label='m vs P_b')
plt.xlabel('$P_b$, Back pressure (kPa)')
plt.ylabel('$\dot{m}$, Mass flow rate (kg/s)')
plt.savefig(r'A4\Questions\Figures\m_vs_P_b.png', dpi=300, bbox_inches='tight')
