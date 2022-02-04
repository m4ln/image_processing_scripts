# image processing
all purpose scripts mostly written in python but also other programming languages (e.g shell)

### **./src**  
*removeWhiteImages.py* - remove background (white) images from directory

**./src/convert**  
*tiffToJpgConverter.sh* - convert tiff into jpg images 

**./src/eval**  
evaluation methods
* *histo.py* - histogram calculation and plotting
* *similarityComparison.py* - compuation of Structured Similarity Metric (SSIM)

**./src/preprocess**  
preprocessing methods
* *cropper.py* - create and save image crops based on W, H, X, Y
* *imageTiling.py* - create and save image tiles
* *seperateWhiteImages.py* - put images into two seperate folders containing white and non-white images
* *arrangeTrainTestValDataset.py* - from a given directory randomly divide into train, test and val dataset
