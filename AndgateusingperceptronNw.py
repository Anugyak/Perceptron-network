
def relu(y): # activation function
    if y > 0:
        return 1
    if y == 0:
        return 0
    return -1
#Initialing Weights and Bias to 0
w = [0, 0]
bias = 0
#Input Vector
x1 = [1, -1, 1, -1]
x2 = [1, 1, -1, -1]
#Output Target Vector
t = [1, -1, -1, -1]
#Learning Rate
alpha = 1

print("x1\t x2\t b\t yin \ty\t t\t dw1 \tdw2 \tdb\t w1\t w2\t b")
for i in range(len(x1)):
    #Yin = b + ∑_(i=1)^n▒XiWi
    yin = bias + x1[i] * w[0] + x2[i] * w[1]
    y = relu(yin)
    if y is not t[i]:
        dw1 = alpha * t[i] * x1[i]
        dw2 = alpha * t[i] * x2[i]
        db = alpha * t[i]
    else:
        dw1, dw2, db = 0, 0, 0
    #wi(new) = wi(old) + alpha * t * xi
    w[0] = w[0] + dw1
    w[1] = w[1] + dw2
    #b(new) = b(0ld) + alpha * t
    bias = bias + db
    print(x1[i],"\t",x2[i],"\t 1 \t",yin,"\t",y,"\t",t[i],"\t",dw1,"\t",dw2, end="")
    print("\t", db, "\t", w[0], "\t", w[1], "\t", bias)




