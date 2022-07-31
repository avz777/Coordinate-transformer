#convert from decimal degrees coordinates to rectangular coordinates
import math
import sys
L=float(input("Latitude:"))
B=float(input("Longitude:"))
N = int((6 + L) / 6)
B = B / 57.29577951
I = (L - (3 + 6 * (N - 1))) / 57.29577951
x = 6367558.4968 * B - math.sin(2 * B) * (16002.89 + 66.9607 * math.sin(B) * math.sin(B) + 0.3515 * math.sin(B) * math.sin(B) * math.sin(B) * math.sin(B) - I * I * (1594561.25 + 5336.535 * math.sin(B) * math.sin(B) + 26.79 * math.sin(B) * math.sin(B) * math.sin(B) * math.sin(B) + 0.149 * math.sin(B) * math.sin(B) * math.sin(B) * math.sin(B) * math.sin(B) * math.sin(B) + I * I * (672483.4 - 811219.9 * math.sin(B) * math.sin(B) + 5420.0 * math.sin(B) * math.sin(B) * math.sin(B) * math.sin(B) - 10.6 * math.sin(B) * math.sin(B) * math.sin(B) * math.sin(B) * math.sin(B) * math.sin(B) + I * I * (278194 - 830174 * math.sin(B) * math.sin(B) + 572434 * math.sin(B) * math.sin(B) * math.sin(B) * math.sin(B) - 16010 * math.sin(B) * math.sin(B) * math.sin(B) * math.sin(B) * math.sin(B) * math.sin(B) + I * I * (109500 - 574700 * math.sin(B) * math.sin(B) + 863700 * math.sin(B) * math.sin(B) * math.sin(B) * math.sin(B) - 398600 * math.sin(B) * math.sin(B) * math.sin(B) * math.sin(B) * math.sin(B) * math.sin(B))))))
y = (5 + 10 * N) * 100000.0 + I * math.cos(B) * (6378245 + 21346.1415 * math.sin(B) * math.sin(B) + 107.159 * math.sin(B) * math.sin(B) * math.sin(B) * math.sin(B) + 0.5977 * math.sin(B) * math.sin(B) * math.sin(B) * math.sin(B) * math.sin(B) * math.sin(B) + I * I * (1070204.16 - 2136826.66 * math.sin(B) * math.sin(B) + 17.98 * math.sin(B) * math.sin(B) * math.sin(B) * math.sin(B) - 11.99 * math.sin(B) * math.sin(B) * math.sin(B) * math.sin(B) * math.sin(B) * math.sin(B) + I * I * (270806 - 1523417 * math.sin(B) * math.sin(B) + 1327645 * math.sin(B) * math.sin(B) * math.sin(B) * math.sin(B) - 21701 * math.sin(B) * math.sin(B) * math.sin(B) * math.sin(B) * math.sin(B) * math.sin(B) + I * I * (79690 - 866190 * math.sin(B) * math.sin(B) + 1730360 * math.sin(B) * math.sin(B) * math.sin(B) * math.sin(B) - 945460 * math.sin(B) * math.sin(B) * math.sin(B) * math.sin(B) * math.sin(B) * math.sin(B)))))
print("X=")
print(x)
print("Y=")
print(y)
