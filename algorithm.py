import math
import numpy as np

#return ||f-f_n*||^2
def diffSquared(n):
	nums = [i+1 for i in range(n)]
	return 1/18 - 4/np.pi**4 * sum([1/m**4 for m in nums])

#return f(x)
def computeF(x):
	return 1/2 * x**2

#return f'(x)
def computeDF(x):
	return x

#return f_n*(x)
def computeFStar(n, x):
	nums = [i+1 for i in range(n)]
	return 1/6 + 2/np.pi**2 * sum([ (-1)**m/m**2 * math.cos(m * np.pi * x) for m in nums])

#return (f_n*)'(x)
def computeDFStar(n, x):
	nums = [i+1 for i in range(n)]
	return -2/np.pi * sum([(-1)**m/m * math.sin(m * np.pi * x) for m in nums])

#return s_n(x)
def s(n, x):
	return 1/(n+1) * sum([computeDFStar(p, x) for p in range(n+1)])

#helpful defs
nums = [i+1 for i in range(100)]
interval = np.linspace(-1.0, 1.0, 200)

