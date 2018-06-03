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
			
			if 'Final Summary' in line:
				train_loss.append(float(line[:-1].split(' ')[-1]))
			elif 'Train Accuracy of the network' in line:
				train_accuracy.append(float(line[:-1].split(' ')[-2]))
			elif 'Test Accuracy of the network' in line:
				test_accuracy.append(float(line[:-1].split(' ')[-2]))

	plt.plot(train_accuracy, label= 'train_accuracy')
	plt.plot(test_accuracy, label = 'test_accuracy')
	plt.plot(train_loss, label = 'train_loss')
	plt.xlabel('epochs')
	plt.ylabel('accuracy')
	plt.title('LazyNet Augmented')
	plt.legend(loc = 'best')
	plt.savefig('LazyNet-augmented-plot.png')
	
if __name__ == '__main__':
	main()