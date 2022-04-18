# Synthetic Blur Detector Network
Synthetic blur detector network (SBDN) includes two subnetworks: Classifier (discriminative) network and Identifier network. Following jupyter notebook files show the progress of developing Classifier network and Identifier network and final results based on tensorflow-keras library.  
**Click on:**<br/>
**- [resnet_blur_classification.ipynb](https://github.com/MasoudMoeini/Synthetic-Blur-Detector-Network/blob/main/Street_View_resnet_blur_classification.ipynb)** file to see resnet-50 classifier model which is responsible to classify input images into two binary classes based on whether they are blurry or they are real-sharp images. The classifier network implementation inspired from [here](https://machinelearningknowledge.ai/keras-implementation-of-resnet-50-architecture-from-scratch/)
<br/>
**Click on:**<br/>
**- [image_blur_detection_with_keras.ipynb](https://github.com/MasoudMoeini/Synthetic-Blur-Detector-Network/blob/main/image_blur_detection_with_keras.ipynb)** file to see Identifier model which is responsible to detect the blurry areas/regions of input blurry images.
<br/>
**Click on:**   <br/> 
**- [synthetic_image_blur_detector_show.ipynb](https://github.com/MasoudMoeini/Synthetic-Blur-Detector-Network/blob/main/synthetic_image_blur_detector_show.ipynb)**  file to see the final test and evaluation results of SBDN.
<br/>
![Screenshot 2022-04-12 at 08 15 07](https://user-images.githubusercontent.com/43514418/162893058-42548adc-9116-41ad-8f5d-ed5d5c717982.png)
<br/>
Figure 1: Synthetic Blur Detector Network (SBDN) architecture. a) Input images. b) Classifier network result: real sharp image. c) Identifier network result for blurry images and discolored burred regions with red color.
<br/>
![Screenshot 2022-03-27 at 22 19 02](https://user-images.githubusercontent.com/43514418/162891691-b04cf645-376b-442e-93ec-66a0ebd6d12f.png)
<br/>
Figure 2: Identifier network architecture
