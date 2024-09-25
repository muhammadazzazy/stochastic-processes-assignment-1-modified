# Question 2
# Suppose X and Y are random variables with the following joint probability mass function:
joint_probability_mass_function = [[0.2,0.1],[0.4,0.3]]

# (a) Find the marginal probability distributions of X and Y.
p_x = [0] * len(joint_probability_mass_function)
p_y = [0] * len(joint_probability_mass_function)
for i in range(len(joint_probability_mass_function)):
    for j in range(len(joint_probability_mass_function[0])):
        if i == 0:
            p_x[0] += joint_probability_mass_function[i][j]
        elif i == 1:
            p_x[1] += joint_probability_mass_function[i][j]
        if j == 0:
            p_y[0] += joint_probability_mass_function[i][j]
        elif j == 1:
            p_y[1] += joint_probability_mass_function[i][j]

print("P(X=1)="+str(round(p_x[0],1)))
print("P(X=2)="+str(round(p_x[1],1)))
print("P(Y=1)="+str(round(p_y[0],1)))
print("P(Y=2)="+str(round(p_y[1],1)))

# (b) Calculate the conditional probability P(Y=2|X=2).
cond_prob = joint_probability_mass_function[1][1] / p_x[1]
print("The conditional probability P(Y=2|X=2) is {}.".format((cond_prob)))

# (c) Find the conditional expectation E(Y|X=1).
conditional_expectation = 0
for i in range(len(joint_probability_mass_function)):
    conditional_expectation += (i+1) * joint_probability_mass_function[0][i] / p_x[0]

print("The conditional expectation E(Y|X=1) is {}.".format((conditional_expectation)))
