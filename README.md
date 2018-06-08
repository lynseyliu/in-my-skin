# In My Skin? #

The final project for Computer Vision for Spring 2018. 

Detecting skin cancer early is crucial to patient survival. Without dermoscopic imaging, dermatologists have an accuracy of 60%. With aided imaging techniques, this accuracy can increase to over 80%. Our approach involves training on a dataset of benign and cancerous skin lesion images to create a model that can detect malignancy of new lesions.

Therefore, we developed convolutional neural networks using PyTorch to assess malignancy of skin lesions. For our model, we relied on the ISIC image archive. Each image contains a skin lesion that can be characterized as benign or malignant. From this dataset, 19,373 lesions are labeled as benign and 2,286 are labeled as malignant. This produces a strong bias towards over-classification of images as being benign.

To balance this bias, we augmented the malignant data by performing transformations of the images. Our model did not take into account transformations as being equivalent skin lesions. We performed trials between multiple models on the original dataset and the augmented dataset. 

We found that overall accuracy was high prior to augmentation but after performing confusion matrices, this was due to overclassification to benign. With augmentation, overall accuracy decreased and would benefit from additional optimization and preprocessing. However, individual classifications were better spread with a slight overclassification of malignant. 

In our dataset, we rely on color differences in order to determine the positioning and features of a skin lesion. In particular, the biggest necessity is the color difference between an individual's skin and the lesion itself. If a lesion has a higher contrast to skin, then it is more likely to be malignant. With darker skinned individuals, dark, malignant regions will not be as visible or contrast as much with skin, so it will be less likely to deem it as malignant.
