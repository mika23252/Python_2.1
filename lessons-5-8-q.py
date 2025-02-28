import matplotlib.pyplot as plt
import numpy as np


##############################################
# 1

fig1 = plt.figure()
x = np.linspace(1, 20, 5)
y1 = [1, 7, 3, 5, 11]
y2 = [4, 3, 1, 8, 12]

marksize = 13
plt.plot(x, y1, '.-r', label='line 1', markersize=marksize)
plt.plot(x, y2, '.-.g', label='line 1', markersize=marksize)
plt.legend()

##############################################
# 2

fig = plt.figure()
x = np.linspace(1, 5, 5)

plt.subplot(2, 1, 1)
plt.plot(x, [1, 7, 6, 3, 5])

plt.subplot(2, 2, 3)
plt.plot(x, [9, 4, 2, 4, 9])

plt.subplot(2, 2, 4)
plt.plot(x, [-7, -4, 2, -4, -7])

##############################################
# 3

fig, ax = plt.subplots()
x = np.linspace(-5, 5, 11)
ax.plot(x, x**2)
ax.annotate('min', xy=(0, 0), xytext=(0, 10), arrowprops=dict(facecolor='green'))

##############################################
# 4

from mpl_toolkits.axes_grid1.inset_locator import inset_axes

vals = np.random.randint(11, size=(7, 7))
fig, ax = plt.subplots()
gr = ax.pcolor(vals)
axins = inset_axes(ax,
                   width="5%",
                   height="50%",
                   loc='lower left',
                   bbox_to_anchor=(1.02, 0., 1, 1),
                   bbox_transform=ax.transAxes,
                   borderpad=0
                   )
plt.colorbar(gr, cax=axins)

##############################################
# 5

fig = plt.figure()
x = np.linspace(0.0, 5, 501)
y = np.cos(x*np.pi)
plt.plot(x, y, c="r")
plt.fill_between(x, y)

##############################################
# 6

fig = plt.figure()
x = np.linspace(0.0, 5, 501)
y = np.cos(x*np.pi)
y_masked = np.ma.masked_where(y < -0.5, y)
plt.ylim(-1, 1)
plt.plot(x, y_masked, linewidth=3)

##############################################
# 7

x = np.arange(0, 7)
y = x
pos_set = ['pre', 'post', 'mid']
fig, axs = plt.subplots(1, 3, figsize=(15, 4))
for i, ax in enumerate(axs):
    ax.step(x, y, "g-o", where=pos_set[i])
    ax.grid()

##############################################
# 8

x = np.arange(0, 11, 1)
y1 = np.array([(-0.2)*i**2+2*i for i in x])
y2 = np.array([(-0.4)*i**2+4*i for i in x])
y3 = np.array([2*i for i in x])
labels = ["y1", "y2", "y3"]
fig, ax = plt.subplots()
ax.stackplot(x, y1, y2, y3, labels=labels)
ax.legend(loc='upper left')

##############################################
# 9

vals = [24, 17, 53, 21, 35]
labels = ["Ford", "Toyota", "BMV", "AUDI", "Jaguar"]
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, explode=(0, 0, 0.15, 0, 0))
ax.axis("equal")

##############################################
# 10

vals = [24, 17, 53, 21, 35]
labels = ["Ford", "Toyota", "BMV", "AUDI", "Jaguar"]
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, wedgeprops=dict(width=0.5))

plt.show()
