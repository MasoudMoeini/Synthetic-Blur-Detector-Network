# Synthetic Blur Detector Network
Synthetic blur detector network (SBDN) includes two subnetworks: Classifier (discriminative) network and Identifier network (Fig. 1). The jupyter notebook files below show the development of Classifier network and Identifier network, as well as the final results for SBDN, using the tensorflow-keras library in python.
<br/>
**Click on:**<br/>
**- [resnet_blur_classification.ipynb](https://github.com/MasoudMoeini/Synthetic-Blur-Detector-Network/blob/main/Street_View_resnet_blur_classification.ipynb)** file to see resnet-50 classifier model which is responsible to classify input images into two binary classes based on whether they are blurry or they are real-sharp images. The classifier network implementation inspired from [here](https://machinelearningknowledge.ai/keras-implementation-of-resnet-50-architecture-from-scratch/).
<br/>
**Click on:**<br/>
**- [image_blur_detection_with_keras.ipynb](https://github.com/MasoudMoeini/Synthetic-Blur-Detector-Network/blob/main/image_blur_detection_with_keras.ipynb)** file to see Identifier model which is responsible to detect the blurry areas/regions of input blurry images. Fig. 2 shows the Identifier network architecture. 
<br/>
**Click on:**   <br/> 
**- [synthetic_image_blur_detector_show.ipynb](https://github.com/MasoudMoeini/Synthetic-Blur-Detector-Network/blob/main/synthetic_image_blur_detector_show.ipynb)**  file to see the final test and evaluation results of SBDN. The initial results for Street-View images dataset are [here](https://github.com/MasoudMoeini/Synthetic-Blur-Detector-Network/blob/main/Steet_View_images_synthetic_image_blur_detector_show.ipynb). 
<br/>
![Screenshot 2022-04-12 at 08 15 07](https://user-images.githubusercontent.com/43514418/162893058-42548adc-9116-41ad-8f5d-ed5d5c717982.png)
<br/>
Figure 1: Synthetic Blur Detector Network (SBDN) architecture. a) Input images  b) Classifier network result: Sharp image (no blur)  c) Identifier network result for blurry images and discolored burred regions with red color.
<br/>
![Screenshot 2022-03-27 at 22 19 02](https://user-images.githubusercontent.com/43514418/162891691-b04cf645-376b-442e-93ec-66a0ebd6d12f.png)
<br/>
Figure 2: Identifier network architecture
<br/> 
<br/> 
**Datasets:** <br/> 
- [Blur Detection Dataset (Shi et al., 2014)](http://www.cse.cuhk.edu.hk/~leojia/projects/dblurdetect/dataset.html)
- [Blur detection with feature Engineering (Blur Dataset- Kaggle)](https://www.kaggle.com/code/harininarasimhan/blur-detection-with-feature-engineering/data)
- Street-View images dataset
