import matplotlib.pyplot as plt
import argparse

from sim_utils import *

parser = argparse.ArgumentParser(description='To run: python3 plot_any.py [path_to_cycle_folder] [chamber] --compare [path to the second cycle folder]')
parser.add_argument('path_to_cycle_folder', help='path to the cycle folder')
parser.add_argument('--compare', help='path to the second cycle folder')
parser.add_argument('chamber', help='la / ra / lv / rv / aorta')
args = parser.parse_args()
cycle_folder = args.path_to_cycle_folder
chamber = args.chamber
cycle_folder2 = args.compare

LV_pres,RV_pres,LA_pres,RA_pres = prepare_pres_data(cycle_folder)
LV_vol,RV_vol,LA_vol,RA_vol = prepare_vol_data(cycle_folder)

Ao_pres = prepare_Ao_data(cycle_folder)

if args.compare is not None:
    lv_pres,rv_pres,la_pres,ra_pres = prepare_pres_data(cycle_folder2)
    lv_vol,rv_vol,la_vol,ra_vol = prepare_vol_data(cycle_folder2)
    ao_pres = prepare_Ao_data(cycle_folder2)

else:
    print("No simulation was provided for comparison")

if chamber in ['la', 'La', 'LA', 'lA']:
    pres = LA_pres
    vol = LA_vol
    if args.compare is not None:
        p = la_pres
        v = la_vol

if chamber in ['ra', 'Ra', 'RA', 'rA']:
    pres = RA_pres
    vol = RA_vol
    if args.compare is not None:
        p = ra_pres
        v = ra_vol

if chamber in ['rv', 'Rv', 'RV', 'rV']:
    pres = RV_pres
    vol = RV_vol
    if args.compare is not None:
        p = rv_pres
        v = rv_vol

if chamber in ['lv', 'Lv', 'LV', 'lV']:
    pres = LV_pres
    vol = LV_vol
    if args.compare is not None:
        p = lv_pres
        v = lv_vol

if chamber in ['ao', 'Ao', 'AO', 'aO']:
    pres = Ao_pres
    vol = np.zeros(len(pres))
    if args.compare is not None:
        p = ao_pres
        v = np.zeros(len(ao_pres))

time = [T/1000 for T in range(0, len(LA_pres))]

if args.compare is not None:
    t = [T/1000 for T in range(0, len(la_pres))]


# Set up a custom color palette
colors = ['#FF5A5F', '#00A699']

# Create a figure and two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Plot data on the first subplot
if args.compare is not None:
    ax1.plot(vol[0:len(pres)], pres, color=colors[0], linewidth=2, label='sim A')
    ax1.plot(v[0:len(p)], p, color=colors[1], linewidth=2, label='sim B')
else:
    ax1.plot(vol[0:len(pres)], pres, color=colors[0], linewidth=2, label='sim')

ax1.set_xlabel('volume [ml]', fontsize=12)
ax1.set_ylabel('pressure [mmHg]', fontsize=12)
ax1.set_title('Pressure-Volume', fontsize=14, fontweight='bold')
ax1.legend(fontsize=10)

# Plot data on the second subplot
if args.compare is not None:
    ax2.plot(time[0:len(pres)], pres, color=colors[0], linewidth=2, label='sim A')
    ax2.plot(t[0:len(p)], p, color=colors[1], linewidth=2, label='sim B')
else:
    ax2.plot(time[0:len(pres)], pres, color=colors[0], linewidth=2, label='sim')

ax2.set_xlabel('time [s]', fontsize=12)
ax2.set_ylabel('pressure [mmHg]', fontsize=12)
ax2.set_title('Pressure-Time', fontsize=14, fontweight='bold')
ax2.legend(fontsize=10)

# Adjust the spacing between subplots
plt.subplots_adjust(wspace=0.4)

# Set a light gray background color for the figure
fig.patch.set_facecolor('#F7F7F7')

# Customize the tick labels and grid lines
for ax in [ax1, ax2]:
    ax.tick_params(axis='both', which='both', direction='in', length=4, width=1, labelsize=10)
    ax.grid(color='gray', linestyle='--', linewidth=0.5)

# Add a subtle gray border around each subplot
for ax in [ax1, ax2]:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color('gray')
    ax.spines['left'].set_color('gray')
    ax.spines['bottom'].set_linewidth(0.5)
    ax.spines['left'].set_linewidth(0.5)

# Show the figure
plt.show()
