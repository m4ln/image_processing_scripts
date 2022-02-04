from PIL import Image
import os


def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)


new_size_x = 1539
new_size_y = 1376
input_dir = "/home/marlen/resizeImages/B"
output_dir = input_dir + "_resize_" + str(new_size_x) + "_" + str(new_size_y) + "/"
print(output_dir)
assure_path_exists(output_dir)

for filename in os.listdir(input_dir):
    im = Image.open(os.path.join(input_dir, filename))
    im_resized = im.resize((new_size_x, new_size_y))
    output_name = output_dir + filename[:-5] + "_x" + str(new_size_x) + "_y" + str(new_size_y) + ".tiff"
    im_resized.save(output_name)
