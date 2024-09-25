# Question 3
# Let the joint density function of X and Y be given by:
# f(x, y) = 6x(1-y), 0<=x<=1, 0<=y<=1
from scipy import integrate
# (a) Find the marginal densities fX(x) and fY(y).

# (b) Calculate the conditional expectation E(X|Y=0.5).
def f(x, y):
    return 6 * x * (1 - y)

y_val = 0.5
f_y, absolute_error = (integrate.quad(f, 0, 1, args=(y_val,)))
print(f_y)

def cond_pdf(x):
    return 3 * x / f_y

def g(x):
    return cond_pdf(x) * x

conditional_expectation, abs_err = integrate.quad(g,0,1)
print("The conditional expectation E(X|Y=0.5) is {}.".format(conditional_expectation))

# (c) Determine E(X^2).
def f(x):
    return 3 * x

def g(x):
    return x**2 * f(x)

mean_of_squares, err = integrate.quad(g,0,1)
print("E(X^2)="+str(mean_of_squares))
