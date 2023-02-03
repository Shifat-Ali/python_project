print('Profit visualization for Term Insuance with sum insured ranging from $1000 to $100,000\n')

sumInsured = float(input('What amount of Term Insurance you are selling?\n'))
term = float(input('What is the Term? (Max 15))\n'))
premium = float(input('What premium you will charge?\n'))
customers = float(input('How many customers do you have for this premium?\n'))
rate = float(input('What semi-annual risk free interest you are getting?\n'))
mc = int(input('Number of time you want to run simulation?\n'))

import random
import matplotlib.pyplot as plt

//randomly generating number of claims asked for each time simulation runs
def randomClaim(sim):
    claim = []
    for i in range(sim):
        claim.append(random.randint(0, customers))
    return claim

//calculating fraction of people who will ask for claim after every year in between total terms of insurance out of total claims
def claimProb():
    a = 1
    prob = []
    for _ in range(0, int(term)):
        b = random.uniform(0., a)
        prob.append(b)
        a = a - b
    return prob


// calculating profit after every year until term is completed
def profit(numClaim):
    net_profit = []
    probList = claimProb()
    
    // those who asked claims meand they are no more bound to pay insurance so calculating remaining number of customers
    rem_cust = []
    for i,j in enumerate(probList):
        if i == 0:
            rem_cust.append(customers - numClaim*probList[i])
        else :
            rem_cust.append(rem_cust[i-1] - numClaim*probList[i])
    
    // finding profit from amount of prev year and then calculating current year amount after settling claims ans recieving insurance from rem customers 
    curr_amount = []
    for i,s in enumerate(probList):
        if i == 0 :
            net = premium*customers
            curr_amount.append(net)
        else:
            net = curr_amount[i-1]*(1+rate/100) - sumInsured*numClaim*probList[i]
            curr_amount.append(net*(1+rate/100) + premium*rem_cust[i-1])

        net_profit.append(net)
    return net_profit

x = []
for i in range (0,int(term)):
    x.append(i)

for i in randomClaim(mc):
    y = profit(i)
    plt.plot(x,y)

plt.xlabel("term in years")
plt.ylabel("net profit")
plt.title("Profit visualization for Term Insuance with sum insured %d" %(sumInsured))
plt.show()

# newma691

    
