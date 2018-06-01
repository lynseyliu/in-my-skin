import torch
import torchvision
import torchvision.transforms as transforms

class IsicLoader(object):
	"""docstring for IsicLoader"""
	def __init__(self, args):
		super(IsicLoader, self).__init__()
		transform = transforms.Compose([
			# TODO: Add data augmentations here
			transforms.CenterCrop(700),
			transforms.Resize(32),
			transforms.ToTensor(),
			transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
		])

		transform_test = transforms.Compose([
		    transforms.ToTensor(),
		    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)), 
		])

		trainset = torchvision.datasets.ImageFolder(root='data/train', transform=transform)
		self.trainloader = torch.utils.data.DataLoader(trainset, batch_size=args.batchSize,
		                                          shuffle=True, num_workers=2)

		testset = torchvision.datasets.ImageFolder(root='data/test', transform=transform_test)
		self.testloader = torch.utils.data.DataLoader(testset, batch_size=args.batchSize,
		                                         shuffle=False, num_workers=2)

		self.classes = ('benign', 'malignant')
