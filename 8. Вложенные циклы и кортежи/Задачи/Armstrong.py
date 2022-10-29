n=3
for i in range(1,10):
    for j in range (1,10):
        for k in range (1,10):
            if i**n + j**n + k**n == i*100+j*10+k:
                print(i*100+j*10+k)