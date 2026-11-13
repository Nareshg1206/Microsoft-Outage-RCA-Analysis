import numpy as np
import matplotlib.pyplot as plt

# Simulation Parameters
total_servers = 100
baseline_load_per_server = 50.0  # 50% normal operating load
total_traffic = total_servers * baseline_load_per_server

# Simulate servers dropping offline from 0% to 60%
offline_percentages = np.linspace(0, 60, 61)
active_servers = total_servers * (1 - offline_percentages / 100)
load_per_active_server = total_traffic / active_servers

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(offline_percentages, load_per_active_server, color='#d9534f', linewidth=3, label='Load on Remaining Servers (%)')

# Threshold lines
plt.axhline(y=80, color='#f0ad4e', linestyle='--', linewidth=2, label='Warning Threshold (80% Capacity)')
plt.axhline(y=100, color='#000000', linestyle=':', linewidth=2, label='Critical Crash Point (100% Saturation)')

# Highlight critical failure zone
plt.fill_between(offline_percentages, load_per_active_server, 100, 
                 where=(load_per_active_server >= 100), color='#d9534f', alpha=0.2, label='Cascading Failure Zone')

# Annotations
plt.title('Cloud Infrastructure Cascading Failure Simulation', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Percentage of Servers Dropped by Failed Health Checks (%)', fontsize=11)
plt.ylabel('CPU / Traffic Load on Surviving Servers (%)', fontsize=11)
plt.ylim(40, 140)
plt.xlim(0, 60)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='upper left', frameon=True)

# Save and display
plt.tight_layout()
plt.savefig('cascading_overload_chart.png', dpi=300)
print("Chart saved successfully as cascading_overload_chart.png")

