import random as rd

class ThompsonBernoulli:
    def __init__(self, succeses, failures):
        self.succeses = succeses
        self.failures = failures

    def initialize(self, n_arms):
        self.succeses = [0 for col in range(n_arms)]
        self.failures = [0 for col in range(n_arms)]

    def select_arm(self, alphas, betas):
        thetas = [rd.betavariate(self.succeses[i] + alphas[i],
            self.failures[i] + betas[i]) for i in range(len(alphas))]
        return thetas.index(max(thetas))

    def update(self, chosen_arm, reward):
        if reward == 1:
            self.succeses[chosen_arm] += 1
        else:
            self.failures[chosen_arm] += 1
