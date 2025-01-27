values = input().split(' ')

X , Y = map(float, values)

if X == 0.0 and Y == 0.0:
    print('Origem')
elif(X==0):
    print("Eixo Y")
elif(Y==0):
    print("Eixo X")
elif X > 0.0 and Y > 0.0:
    print('Q1')
elif X < 0.0 and Y > 0.0:
    print('Q2')
elif X < 0.0 and Y < 0.0:
    print('Q3')
else:
    print('Q4')