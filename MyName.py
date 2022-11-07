str1 = "AMIR"
print_A = [[" " for c in range (5)] for r in range (7)]
print_M = [[" " for c in range (7)] for r in range (7)]
print_I = [[" " for c in range (5)] for r in range (7)]
print_R = [[" " for c in range (5)] for r in range (7)]

for row in range(7):
    for col in range(5):
        if ((col==0 or col==4) and row!=0) or ((row==0 or row==3) and (col>0 and col<4)):
             print_A[row][col]= "*"
             
for row in range(7):
    for col in range(7):
        if (col==0 or col==6) or ((row==col) and (col>0 and col<4)) or (row==1 and col==5) or (row==2 and col==4):
             print_M[row][col]="*"
             
for row in range(7):
    for col in range(5):
        if (col==2) or ((row==0 or row==6) and col!=2):
            print_I[row][col]="*"
            
for row in range(7):
    for col in range(5):
        if col==0 or (col==4 and (row!=0 and row!=3)) or ((row==0 or row==3) and (col>0 and col<4)):
            print_R[row][col]="*"
            
for r in range(7):
    for c in range(5):
        print(print_A[r][c], end=" ")
    print(end="  ")
    for c in range(7):
        print(print_M[r][c], end=" ")
    print(end="  ")
    for c in range(5):
        print(print_I[r][c], end=" ")
    print(end="  ")
    for c in range(5):
        print(print_R[r][c], end=" ")
    print()
            