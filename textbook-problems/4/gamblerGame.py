#first, initialize the state and policy arrays;
policyArray = [0 for x in range(101)]
stateArray = [0 for x in range(101)]
phead = 0.5
ptail = 1 - phead

#accuracy limit
limit = 0.001
gamma = 0.9
delta = 1000

def getReward(x):
	if (x <= 0):
		return -1
	elif (0 < x < 100):
		return 0
	else: 
		return 1


#now, we can do the algorithm
while (delta > limit):
	delta = 0

	# i represents our current state; 0 to 99
	for i in range(0, 100):
		v = stateArray[i]
		bestValue = 0
		bestAction = 0
		for j in range(0, min(i, 100-i) + 1):
			expected = phead * (getReward(i + j) + gamma * stateArray[i + j]) + ptail * (getReward(i - j) + gamma * stateArray[i - j])
			if (expected > bestValue):
				bestValue = expected
				bestAction = j
		stateArray[i] = bestValue
		policyArray[i] = bestAction
		delta = max(delta, abs(v - stateArray[i]))	

print(stateArray);
print("\n");
print(policyArray);
