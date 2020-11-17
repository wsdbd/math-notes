import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import math;

R = 2.0
x, y = 0.0, 0.0
a, b = R, R

fig_width, fig_height = 4.0, 4.0
fig = plt.figure(figsize=(fig_width, fig_height), frameon=False)
ax = fig.add_axes([-0.25, -0.25, 1.5, 1.5], aspect='equal')
ax.set_axis_off()
ax.set_xlim(-R*1.0, R*1.0)
ax.set_ylim(-R*1.0, R*1.0)

# Axes
# ax.axhline(0.0)
# ax.axvline(0.0)

ax.plot([0.0, math.sqrt(2)/2.0], [0.0, math.sqrt(2)/2.0], 'k')

ax.plot([math.sqrt(2)/2.0, 1.0], [math.sqrt(2)/2.0, 0.0], 'k')

ax.plot([0.0, 1.0], [0.0, 0.0], 'k')

ax.plot([math.sqrt(2)/2.0, math.sqrt(2)/2.0], [math.sqrt(2)/2.0, 0.0], 'k--')


# ax.text(0.0 - 0.1, 0.0 - 0.1, r'O', fontsize=10)

ax.text(0.495, 0.495, '$O$',
        horizontalalignment='right',
        verticalalignment='top',
        transform=ax.transAxes)


ax.text(1.05, 0.0, '$A$',
        horizontalalignment='left',
        verticalalignment='center')

ax.text(math.sqrt(2)/2.0 + 0.05, math.sqrt(2)/2.0 + 0.05, '$B$',
        horizontalalignment='left',
        verticalalignment='center')

ax.text(math.sqrt(2)/2.0, -0.05, '$C$',
        horizontalalignment='center',
        verticalalignment='top')

ax.text(0.5 - 0.05, 0.5 - 0.05, '$D$',
        horizontalalignment='right',
        verticalalignment='bottom')

ax.text(0.2 * math.cos(math.radians(22.5)), 0.2 * math.sin(math.radians(22.5)), '$x$',
        horizontalalignment='center',
        verticalalignment='center')


ax.text(1.1 * math.cos(math.radians(22.5)), 1.1 * math.sin(math.radians(22.5)), '$x$',
        horizontalalignment='center',
        verticalalignment='center')


ax.add_patch(Arc((x, y), a, b,
                 theta1=0.0, theta2=360.0, edgecolor='k'))
ax.add_patch(Arc((x, y), a, b,
                 theta1=0.0, theta2=45.0, edgecolor='k', lw=1.5))

ax.add_patch(Arc((x, y), a * math.sqrt(2)/2.0, b * math.sqrt(2)/2.0,
                theta1=0.0, theta2=45.0, edgecolor='k', lw=1.0, linestyle='dashed'))


ax.add_patch(Arc((x, y), 0.2, 0.2,
                 theta1=0.0, theta2=45.0, edgecolor='k'))

fig.savefig("draw-08-01.png")
