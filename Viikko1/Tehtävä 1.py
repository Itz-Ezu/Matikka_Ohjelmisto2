import numpy as np

#tehtävä 1.1:
a1 = 2.493
b1 = 0.911
print(f"\nTehtävä 1.1: \n")
print(f"{a1} : {np.degrees(a1)}")
print(f"{b1} : {np.degrees(b1)}")

#tehtävä 1.2:
print(f"\nTehtävä 1.2: \n")
a2 = 137.7
b2 = 62.3


print(f"{a2} : {np.radians(a2)}")
print(f"{b2} : {np.radians(b2)}")

#tehtävä 1.3:
print(f"\nTehtävä 1.3: \n")
A = np.array([30, 45, 60, 90, 120, 135, 150, 180, 270, 360])

for i in A:
  print(f"{i} : {np.radians(i)}")
