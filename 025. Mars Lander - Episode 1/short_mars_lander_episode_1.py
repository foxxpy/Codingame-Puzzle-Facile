import sys
import math

surface_n = int(input())  # the number of points used to draw the surface of Mars.

for i in range(surface_n):
    land_x, land_y = [int(j) for j in input().split()]

# game loop
while True:

    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]
    if v_speed < -40 and power < 4:
        power += 1 

    print("0 "+str(power))
