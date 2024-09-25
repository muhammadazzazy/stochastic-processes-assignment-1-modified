# Question 1
# An insurance company monitors claims in two regions, Region A and Region B. The number of claims in Region A follows a
# Poisson distribution with mean λ_A = 4, and the number of claims in Region B follows a Poisson distribution with
# mean λ_B = 6. Assume the number of claims in Region A and B are independent.
from scipy.stats import poisson
mean_a = 4
mean_b = 6

# (a) What is the probability that exactly 3 claims are filed in Region A and exactly 5 claims are filed in Region B
# next year
claims_a = 3
claims_b = 5

prob_a = poisson.pmf(claims_a,mean_a)
prob_b = poisson.pmf(claims_b,mean_b)

print("The probability that exactly {} claims are filed in Region A and exactly {} claims are filed in Region B "
      "next year is {}.".format(claims_a,claims_b,prob_a*prob_b))
# (b) What is the expected number of claims in both regions combined?
mean_claims = mean_a + mean_b
print("The expected number of claims in both regions combined is {}.".format(mean_claims))

# (c) Let X represent the total number of claims in both regions combined. Find the distribution of X and calculate the
# probability that there are exactly 9 claims in total.
total_claims = 9
prob = poisson.pmf(total_claims,mean_a + mean_b)
print("The probability that there are {} claims in total is {}.".format(total_claims,prob))
