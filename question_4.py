# Question 4
# A company has three typists, each with a different average error rate. If the task is assigned to Typist A, the number
# of errors follows a Poisson distribution with mean 1.8. For Typist B, the number of errors follows a Poisson
# distribution with mean 2.5, and for Typist C, the number of errors follows a Poisson distribution with mean 3.1.
# Assume that each typist is equally likely to be chosen for the task.
from scipy.stats import poisson
# (a) Find the expected number of errors if a task is randomly assigned to one of the typists.
N = 3
mean_a = 1.8
mean_b = 2.5
mean_c = 3.1

expected_errors = (mean_a + mean_b + mean_c)/N
print("The expected number of errors if a task is randomly assigned to one of the typists is {}.".format(
    expected_errors))

# (b) Suppose 3 errors were found in a document. What is the probability that Typist A was responsible for typing it?
errors = 3

prob_a = poisson.pmf(errors,mean_a)
print("P(A=3)=" + str(prob_a))

prob_b = poisson.pmf(errors,mean_b)
print("P(B=3)=" + str(prob_b))

prob_c = poisson.pmf(errors,mean_c)
print("P(C=3)=" + str(prob_c))

print("The probability that Typist A was responsible for typing the document is {}.".format(
    (1 / N) * prob_a / ((1 / N) * (prob_a + prob_b + prob_c))))

# (c) If the same task is assigned to two typists (one at a time) with equal probability, find the expected number of
# errors across both tasks
expectation = 2 * expected_errors
print("If the same task is assigned to two typists (one at a time) with equal probability, the expected number of"
      "errors across both tasks is {}.".format(expectation))
