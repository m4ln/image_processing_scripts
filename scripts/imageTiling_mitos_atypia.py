
from PIL import Image
import os

dim = 256
W = [dim]
H = W
X = [0, 30]
Y = X
set_name = "A03"
magnification = "x40"
input_dir = "/home/mr38/sds_hd/sd18a006/Marlen/datasets/MITOS-ATYPIA-14/extract/train/" + set_name + "/frames/" + magnification
input_dir = "/home/marlen/resizeImages/A"
output_dir = input_dir + "_tiles_" + str(dim) + "/"
print(output_dir)
assure_path_exists(output_dir)

for filename in os.listdir(input_dir):
    im = Image.open(os.path.join(input_dir, filename))
    for w in W:
        for h in H:
            for x in X:
                for y in Y:
                    region = im.crop((x, y, x+w, y+h))
                    output_name = output_dir + filename[:-5] + "_x" + str(x) + "_y" + str(y) + "_w" + str(w) + "_h" + str(h) + ".tiff"
                    region.save(output_name)
