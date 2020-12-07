# helper-scripts
all purpose scripts mostly written in python but also other programming languages (e.g shell)

### **./imageProcessing**  
all purpose scripts for image (pre- & post-) processing methods

**./imageProcessing/eval**  
evaluation methods
* *histo.py* - histogram calculation and plotting
* *similarityComparison.py* - compuation of Structured Similarity Metric (SSIM)

**./imageProcessing/preprocess**  
preprocessing methods
* *cropper.py* - create and save image crops based on W, H, X, Y
* *imageTiling.py* - create and save image tiles
* *removeWhiteImages.py* - remove background (white) images from directory
* *seperateWhiteImages.py* - put images into two seperate folders containing white and non-white images

*arrangeTrainTestValDataset.py* - from a given directory randomly divide into train, test and val dataset

*tiffToJpgConverter.sh* - convert tiff into jpg images 
