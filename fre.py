import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

W1, W2 = np.mgrid[-np.pi:np.pi:100j, -np.pi:np.pi:100j]  # 100分割

H = (1 + 2*np.cos(W1) + 2*np.cos(W2) + 4*np.cos(W1)*np.cos(W2))/9
H = np.absolute(H)

# figure 1
fig = plt.figure(1)
ax = Axes3D(fig)
ax.plot_wireframe(W1, W2, H)

# Range
plt.xlim([-np.pi, np.pi])
plt.ylim([-np.pi, np.pi])

plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$\pi/2$', r'$\pi$'])
plt.yticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$\pi/2$', r'$\pi$'])

ax.set_xlabel(r'$\omega_1$', fontsize=24)
ax.set_ylabel(r'$\omega_2$', fontsize=24)
ax.set_zlabel(r'$|H(\omega_1, \omega_2)|$', fontsize=24)

plt.savefig('average1_wf.png', dpi=144)
# /figure 1

# figure 2
plt.figure(2)
# extent: 座標[left, right, bottom, top]
plt.imshow(H, cmap=cm.gray, interpolation='nearest', vmin=0, vmax=1,
           extent=[-np.pi, np.pi, -np.pi, np.pi])
cbar = plt.colorbar()

# plotの大きさを調整
plt.subplots_adjust(bottom=0.15)

plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$\pi/2$', r'$\pi$'])
plt.yticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$\pi/2$', r'$\pi$'])

plt.xlabel(r'$\omega_1$', fontsize=24)
plt.ylabel(r'$\omega_2$', fontsize=24)
cbar.set_label(r'$|H(\omega_1, \omega_2)|$', fontsize=24)

plt.savefig('average1_cm.png', dpi=144)
# /figure 2

n1=np.arange(0,3)
n2=np.arange(0,3)
N1,N2=np.meshgrid(n1,n2)
h=np.ones((3,3),np.float32)/5
h[0][0]=0;h[0][2]=0;h[2][0]=0;h[2][2]=0;
print(h)
fig = plt.figure(3)
ax = Axes3D(fig)
ax.plot_wireframe(N1,N2,h)



plt.show()