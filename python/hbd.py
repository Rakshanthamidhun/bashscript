def pattern():
    for i in range(len(name)):
       # 
        if name[i]==" ":
            print_empty= [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if col in range(6):
                        print_empty[row][col]=" "
            list2.append(print_empty)
	#A
        elif name[i]=="A":
             print_A= [[" " for i in range(6)] for j in range(7)]
             for row in range(7):
                for col in range(6):
                     if ((col==0 or col==5) and row!=0) or ((row==3 or row==0) and (col>0 and col<5)) :
                        print_A[row][col]="*"
             list2.append(print_A)
	#B
	elif name[i]=="B":
             print_B= [[" " for i in range(6)] for j in range(7)]
             for row in range(7):
                for col in range(6):
			if col==0 or (col==5 and (row!=0 and row!=3 and row!=6)) or ((row==0 or row==3 or row==6) and (col>0 and col<5)):
                           print_B[row][col]="*"
             list2.append(print_B)
	#C
        elif name[i]=="C":
             print_C= [[" " for i in range(6)] for j in range(7)]
             for row in range(7):
                for col in range(6):
                    if ((row==0 or row==6) and col>0) or ((row!=0 and row!=6) and col==0):
                        print_C[row][col]="*"
             list2.append(print_C)
	#D
	elif name[i]=="D":
             print_D= [[" " for i in range(6)] for j in range(7)]
             for row in range(7):
                for col in range(6):
                    if (col==0) or ((col==5) and (row!=0 and row!=6)) or ((row==0 or row==6) and (col>0 and col<5)):
                        print_D[row][col]="*"
             list2.append(print_D)       
	#E
	elif name[i]=="E":
             print_E= [[" " for i in range(6)] for j in range(7)]
             for row in range(7):
                for col in range(6):
                    if (col==0) or (row==0 or row==3 or row==6):
                        print_E[row][col]="*"
             list2.append(print_E)
	#F
	elif name[i]=="F":
             print_F= [[" " for i in range(6)] for j in range(7)]
             for row in range(7):
                for col in range(6):
                    if (col==0) or (row==0 or row==3):
                        print_F[row][col]="*"
             list2.append(print_F)
	#G
	elif name[i]=="G":
             print_G= [[" " for i in range(6)] for j in range(7)]
             for row in range(7):
                for col in range(6):
                    if (col==0 and (row!=6 and row!=0)) or (row==6 and (col!=0 and col!=5)) or (col==5 and (row<6 and row>2)) or (row==0 and col>0) or (row==3 and (col>2 and col<5)):
                        print_G[row][col]="*"
             list2.append(print_G)
	#H
	elif name[i]=="H":
             print_H= [[" " for i in range(6)] for j in range(7)]
             for row in range(7):
                for col in range(6):
                    if (col==0 or col==5) or (row==3):
                        print_H[row][col]="*"
             list2.append(print_H)
	#I
	elif name[i]=="I":
             print_I= [[" " for i in range(6)] for j in range(7)]
             for row in range(7):
                for col in range(6):
                    if (row==0 or row==6) or (col==2):
                        print_I[row][col]="*"
             list2.append(print_I)

	#J
	elif name[i]=="J":
             print_J= [[" " for i in range(6)] for j in range(7)]
             for row in range(7):
                for col in range(6):
                    if row==0 or (col==3 and row!=6) or (row==6 and col==2) or (row==5 and col==1) or (row==4 and col==0):
                        print_J[row][col]="*"
             list2.append(print_J)

	#K
	elif name[i]=="K":
             print_K= [[" " for i in range(6)] for j in range(7)]
             for row in range(7):
                for col in range(6):
                    if col==0 or row+col==3 or row-col==3:
                        print_K[row][col]="*"
             list2.append(print_K)	

	#L
	elif name[i]=="L":
             print_L= [[" " for i in range(6)] for j in range(7)]
             for row in range(7):
                for col in range(6):
                    if col==0 or row==6:
                        print_L[row][col]="*"
                list2.append(print_L)
	#M
	elif name[i]=="M":
             print_M= [[" " for i in range(6)] for j in range(7)]
             for row in range(7):
                for col in range(6):
                    if (col==0 or col==5) or ((row==col) and (col>0 and col<3)) or (row==1 and col==4) or (row==2 and col==3):
                        print_M[row][col]="*"
             list2.append(print_M)
	#N
	elif name[i]=="N":
             print_N= [[" " for i in range(6)] for j in range(7)]
             for row in range(7):
                for col in range(6):
                    if (col==0 or col==5) or (row==col and (col<6 and col>0)):
                        print_N[row][col]="*"
             list2.append(print_N)
	#O
	elif name[i]=="O":
             print_O= [[" " for i in range(6)] for j in range(7)]
             for row in range(7):
                for col in range(6):
                    if ((row==0 or row==6) and (col!=0 and col!=5)) or ((col==0 or col==5) and (row!=0 and row!=6)):
                        print_O[row][col]="*"
             list2.append(print_O)
	
	#P
	elif name[i]=="P":
             print_P= [[" " for i in range(6)] for j in range(7)]
             for row in range(7):
                for col in range(6):
                    #if col==0 or ((row==0 or row==3) and col!=5) or ((row==1 or row==2) and col==5):
                    if col==0 or ((row==0 or row==3) and (col<5 and col>0)) or ((row==1 or row==2) and col==5):
                        print_P[row][col]="*"
             list2.append(print_P)   

	#Q
	elif name[i]=="Q":
             print_Q= [[" " for i in range(6)] for j in range(7)]
             for row in range(7):
                for col in range(6):
                    if ((col==0 or col==5) and (row<5 and row>0)) or ((row==0 or row==5) and (col>0 and col<5)) or ((row==col) and (col>2 and col<=5)): 
                        print_Q[row][col]="*"
             list2.append(print_Q)
 
    	#R
	elif name[i]=="R":
             print_R= [[" " for i in range(6)] for j in range(7)]
             for row in range(7):
                for col in range(6):
                    if col==0 or (row==0 and col!=5) or ((col==row-1) and (col>2 and col<6)) or (row==3 and (col>0 and col<3)) or ((row+col==6) and (col>3 and col<=5)):
                        print_R[row][col]="*"
             list2.append(print_R)
	#S
	elif name[i]=="S":
             print_S= [[" " for i in range(6)] for j in range(7)]
             for row in range(7):
                for col in range(6):
                    if ((row==0 or row==3) and (col>0 and col<5)) or (col==5 and (row==0 or (row>3 and row<6))) or (row==6 and col!=5) or (col==0 and (row>0 and row<3)):
                        print_S[row][col]="*"
             list2.append(print_S)
	
	#T
	elif name[i]=="T":
             print_T= [[" " for i in range(6)] for j in range(7)]
             for row in range(7):
                for col in range(6):
                    if row==0 or col==2:
                        print_T[row][col]="*"
             list2.append(print_T)
	#U
	elif name[i]=="U":
             print_U= [[" " for i in range(6)] for j in range(7)]
             for row in range(7):
                for col in range(6):
                    if ((col==0 or col==5) and row!=6) or (row==6 and (col<5 and col>0)):
                        print_U[row][col]="*"
             list2.append(print_U)

	#V
	elif name[i]=="V":
             print_V= [[" " for i in range(6)] for j in range(7)]
             for row in range(7):
                for col in range(6):
                    if ((col==0 or col==5) and (row>=0 and row<5)) or (row==5 and (col==1 or col==4)) or (row==6 and (col==2 or col==3)):
                        print_V[row][col]="*"
             list2.append(print_V)
	#W
	elif name[i]=="W":
             print_W= [[" " for i in range(6)] for j in range(7)]
             for row in range(7):
                for col in range(6):
                    if (col==0 or col==5) or (row==3 and col==3) or ((row==4 and col==2) or (row==4 and col==4)) or (col==1 and row==5):
                        print_W[row][col]="*"
             list2.append(print_W)

	#X
	elif name[i]=="X":
             print_X= [[" " for i in range(6)] for j in range(7)]
             for row in range(7):
                for col in range(6):
                    if ((col==0 or col==5) and (row<=1 or row>=5)) or ((row==2 or row==4) and (col==1 or col==4)) or (row==3 and (col>1 and col<4)):
                        print_X[row][col]="*"
             list2.append(print_X)
	#Z
	elif name[i]=="Z":
             print_Z= [[" " for i in range(6)] for j in range(7)]
             for row in range(7):
                for col in range(6):
                    if (row==0 or row==6) or (row+col==6):
                        print_Z[row][col]="*"
             list2.append(print_Z)
	#heart
	elif name[i]==":":
             print_heart= [[" " for i in range(6)] for j in range(7)]
             for row in range(7):
                for col in range(6):
                    if ((col==0 or col==5) and (row>0 and row<5)) or (row==0 and ((col>0 and col<3) or col==4)) or (row==1 and col==3) or (row==5 and (col==1 or col==4)) or (row==6 and (col>1 and col<4)):
                        print_heart[row][col]="*"
             list2.append(print_heart)
	else:
	    print("don't enter numbers or small lettters or special character ")		
    return list2

import calendar
b="midhun"
a=input("Enter sweet name which i wished to call you > ")
if a=="cutiepie":
    print("correct guess i like you",b)
else:
    print("wrong guess",b)
d=input("Enter sweet name which i wished to call you > ")
print("My dear",d,"you have born on month calendar:\n",calendar.month(1993,5))

name=input("Please enter letters in caps and a valid letter can specify space and : for readabilty: ")
print("If you like to you : please use < before and > after of :")
list2=[]
list3=pattern()
for i in range(7):
    for j in range(len(list3)):
      for k in range(6):
        print(list3[j][i][k],end=" ")
      print(end=" ")
    print()

