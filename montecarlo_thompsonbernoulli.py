import random
from bernoulliarm import *
from thompsonbernoulli import *
from bandittestframe import *

random.seed(1)
means = [0.1, 0.1, 0.1, 0.1, 0.9]
n_arms = len(means)
random.shuffle(means)
arms = [BernoulliArm(mu) for mu in means]
print("Best arm is " + str(means.index(max(means))))

f = open("thompson_bernoulli_results.tsv", "w+")

algo = ThompsonBernoulli([], [], [], [])
algo.initialize(n_arms)
results = test_algorithm(algo, arms, 5000, 250)
for i in range(len(results[0])):
    f.write("\t".join([str(results[j][i]) for j in range(len(results))])+ "\n")

f.close()
