from algorithm import *
import matplotlib.pyplot as plt

#generate a plot given data points
def generatePlot1(xs, ys, title, file):
	plt.figure()
	plt.title(title)
	plt.plot(xs, ys)
	plt.savefig(file)


#generate data for given functions
def generatePlot2(func1, func2, l1, l2, file):
	plt.figure(figsize=(9,9))

	for n in [1,2,3,4,5,6,7,8,9]:
		plt.subplot(3,3,n)
		plt.title('n = ' + str(n))
		plt.plot(interval, [func1(x) for x in interval], 'b', label=l1)
		plt.plot(interval, [func2(n, x) for x in interval], 'r', label=l2)	
		plt.legend()

	plt.savefig(file)

#create the various graphs required for the task
generatePlot1(nums, [diffSquared(n) for n in nums], 'difference squared', 'diff')
generatePlot2(computeF, computeFStar, 'f', 'f*', 'normal')
generatePlot2(computeDF, computeDFStar, 'df', 'df*', 'derivative')

generatePlot1(nums, [computeDFStar(n, (2*n-1)/(2*n+1)) - computeDF((2*n-1)/(2*n+1)) for n in nums], 'derivative difference', 'ddiff')

generatePlot2(computeDF, s, 'df', 's', 'average')
