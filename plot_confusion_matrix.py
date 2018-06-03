import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pdb
import argparse
import numpy as np


def argParser():
	parser = argparse.ArgumentParser(description='PyTorch Plot Progress')
	parser.add_argument('--file_name', default='')
	return parser.parse_args()


def main():
	args = argParser()
	train_accuracy=[]
	test_accuracy=[]
	train_loss=[]
	bcount = 0
	btotal = 0
	mcount = 0
	mtotal = 0
	with open(args.file_name) as f:
		for line in f:
			if 'Test Accuracy of benign' in line:
				bcount+=1
				#print(line[:-1].split(' ')[-2])
				btotal +=(float(line[:-1].split(' ')[-2]))
			elif 'Test Accuracy of malignant' in line:
				mcount+=1
				#print(line[:-1].split(' ')[-2])
				mtotal +=(float(line[:-1].split(' ')[-2]))

	# True was benign and predicted was benign
	avg00 = round(btotal/bcount / 100, 3)
	
	# True was benign and predicted was malignant
	avg01 = round(1 - avg00, 3)
	
	# True was malignant and predicted was malignant
	avg11 = round(mtotal/mcount / 100, 3)
	
	# True was malignant and predicted was benign
	avg10 = round(1 - avg11, 3)
	
	conf_arr = [[avg00,avg01], 
            [avg10,avg11]]
	
	norm_conf = []
	for i in conf_arr:
		a = 0
		tmp_arr = []
		a = sum(i, 0)
		for j in i:
			tmp_arr.append(float(j)/float(a))
		norm_conf.append(tmp_arr)

	fig = plt.figure()
	plt.clf()
	ax = fig.add_subplot(111)
	ax.set_aspect(1)
	res = ax.imshow(np.array(norm_conf), cmap=plt.cm.BuPu, 
					interpolation='nearest')

	for x in range(2):
		for y in range(2):
			ax.annotate(str(conf_arr[x][y]), xy=(y, x), 
						horizontalalignment='center',
						verticalalignment='center')

	cb = fig.colorbar(res)
	alphabet = ['benign','malignant']
	plt.xticks(range(2), alphabet[:2])
	plt.yticks(range(2), alphabet[:2])
	plt.xlabel('Predicted')
	plt.ylabel('True')
	plt.title('LazyNet nonaugmented confusion matrix')
	plt.savefig('lazynet_nonaugmented_confusion_matrix.png', format='png')

if __name__ == '__main__':
	main()