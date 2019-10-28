import matplotlib.pyplot as plt
a =[]
colors = ['#fdae61' , '#a6d96a']

for i in range(11):
    b = []
    for j in range(i):
        b.append(0)
    for j in range(i, 10):
        b.append(1)
    a.append(b)
print(a)
for i in range(11):
    #for j in range(10):
    y = [50-2.5*i for _ in range(10)]
    x = list(range(10))
    c = [colors[j] for j in a[i]]
    plt.scatter(x, y, c=c, s=800, alpha=0.95)
plt.show()
