import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi*3, np.pi*3, 256, endpoint=True)
C,S = np.cos(X), np.sin(X)

fig, ax = plt.subplots(figsize=(6.8*3, 4.8))

plt.plot(X, C, color="green", linewidth=3, linestyle="--", label="cosine")
plt.plot(X, S, color="purple",  linewidth=3, linestyle="-.", label="sine")

plt.legend(loc='upper left', frameon=False)

plt.xlim(X.min()*1, X.max()*1)
plt.ylim(C.min()*1, C.max()*1)

plt.xticks( [-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
plt.yticks([-1, 0, +1])

plt.xticks([-np.pi*3, -np.pi*5/2, -np.pi*2, -np.pi*3/2, -np.pi, -np.pi/2, 0, np.pi/2, np.pi, np.pi*1.5, np.pi*2, np.pi*2.5, np.pi*3],
       [r'$-3\pi$', r'$-2.5\pi$', r'$-2\pi$', r'$-1.5\pi$', r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$', r'$+1.5\pi$', r'$+2\pi$',  r'$+2.5\pi$', r'$+3\pi$'])

plt.yticks([-1, -0.50, 0, 0.50, +1],
       [r'$-1$', r'$-0.50$', r'$0$', r'$0.50$', r'$+1$'])




plt.show()