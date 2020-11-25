import sys
import math

def dist(x1, x2, y1, y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

n = int(input())

for k in range(n):
    parallelogram = False
    rhombus = False
    rectangle = False
    carre = False
    a, x_a, y_a, b, x_b, y_b, c, x_c, y_c, d, x_d, y_d = input().split()
    x_a = int(x_a)
    y_a = int(y_a)
    x_b = int(x_b)
    y_b = int(y_b)
    x_c = int(x_c)
    y_c = int(y_c)
    x_d = int(x_d)
    y_d = int(y_d)
        
    #Calcul des distances
    dist_a_b = dist(x_a, x_b, y_a, y_b)
    dist_b_c = dist(x_b, x_c, y_b, y_c)
    dist_c_d = dist(x_c, x_d, y_c, y_d)
    dist_d_a = dist(x_d, x_a, y_d, y_a)
    dist_a_c = dist(x_c, x_a, y_c, y_a)
    dist_b_d = dist(x_d, x_b, y_d, y_b)

    #Test parallelogram  : on teste si les côtés opposés sont égaux deux à deux  
    if dist_a_b == dist_c_d and dist_b_c == dist_d_a:
        parallelogram = True

    #Test rhombus : on teste que les 4 côtés soient égaux
    if dist_a_b == dist_b_c == dist_c_d == dist_d_a:
        rhombus = True
        
    #Test rectangle : on teste si les diagonales sont égales
    if dist_a_c == dist_b_d:
        rectangle = True
        print("rectangle : "+str(rectangle), file=sys.stderr)
    
    print(a+b+c+d+" is a ", end="")
    
    #Test carré ; on teste si c'est à la fois un rectangle et un rhombus
    if rectangle and rhombus:
        carre = True
        print("square.")
    
    elif rectangle and not rhombus:
        print("rectangle.")
        
    elif not rectangle and rhombus:
        print("rhombus.")
        
    elif parallelogram:
        print("parallelogram.")
        
    else:
        print("quadrilateral.")
