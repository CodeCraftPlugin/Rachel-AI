"""A very simple parallel code example to execute parallel functions in python"""
import multiprocessing
import numpy as np
def multiprocessing_func(x):
	"""Individually prints the squares y_i of the elements x_i of a vector x"""
	for x_i in x:
		y=x_i**2 
		print('The square of ',x_i,' is ',y)
def chunks(input, n):
    """Yields successive n-sized chunks of input"""
    for i in range(0, len(input), n):
        yield input[i:i + n]
if __name__=='__main__':
	n_proc=4 #Numer of available processors
	x=np.arange(100) #Input
	chunked_x=list(chunks(x, int(x.shape[0]/n_proc)+1)) #Splits input among n_proc chunks
	processes=[] #Initialize the parallel processes list
	for i in np.arange(0,n_proc):
		"""Execute the target function on the n_proc target processors using the splitted input""" 
		p = multiprocessing.Process(target=multiprocessing_func,args=(chunked_x[i],))
		processes.append(p)
		p.start()
	for process in processes:
		process.join()