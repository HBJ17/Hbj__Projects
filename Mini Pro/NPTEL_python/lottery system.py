import random
import matplotlib.pyplot as plt

amount=0

x=[]
y=[]

for i in range(365):
    x.append(i+1)

    bet = random.randint(1,10)
    lucky_draw=random.randint(1,10)

    if bet==lucky_draw:
        amount = amount + 800

    else:
        amount = amount - 100

    y.append(amount)

print("Amount in your gaming account is",amount)

plt.plot(x,y)
plt.show()
