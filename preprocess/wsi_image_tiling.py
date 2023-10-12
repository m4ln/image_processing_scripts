# ''' Whole Slide Image Tiling.
#     This script is used to tile whole slide images (WSI) into smaller images.
#     The script takes as input a WSI file (tiff or svs) and tiles it into smaller images of specified size (e.g. 512x512) and image format (e.g. png, jpg).
#     The script can be used to tile a single WSI file or multiple WSI files in a directory.
# '''
# import argparse
# import os
#
# os.add_dll_directory(
#     "C:/Users/mr38/Downloads/openslide-win64-20230414/openslide-win64-20230414/bin")
# import openslide
# import numpy as np
# import cv2
#
#
# def is_patch_background(patch, intensity_threshold=255, ratio_threshold=0.9):
#     # Convert the patch to grayscale
#     gray_patch = cv2.cvtColor(patch, cv2.COLOR_BGR2GRAY)
#
#     # Calculate the percentage of white pixels
#     white_pixels_ratio = np.count_nonzero(
#         gray_patch >= intensity_threshold) / gray_patch.size
#
#     # If the percentage of white pixels is greater than the threshold, consider it a background patch
#     return white_pixels_ratio > ratio_threshold
#
#
# def extract_patches_from_wsi(wsi_file, patch_size, image_format, output_folder):
#     # # Get list of WSI files in input directory
#     # wsi_files = [f for f in os.listdir(input_dir) if os.path.isfile(
#     #     os.path.join(input_dir, f)) and f.lower().endswith(
#     #     '.svs') or f.lower().endswith('.tiff')]
#
#     # Open the WSI file
#     slide = openslide.open_slide(wsi_file)
#
#     # Get the dimensions of the WSI
#     wsi_width, wsi_height = slide.dimensions
#
#     # Define the patch size (width and height)
#     patch_width, patch_height = patch_size
#
#     # Create the output folder if it doesn't exist
#     os.makedirs(output_folder, exist_ok=True)
#
#     # Calculate the number of patches in both dimensions
#     num_patches_x = wsi_width // patch_width
#     num_patches_y = wsi_height // patch_height
#
#     # print nnumer of patches to be extracted from the WSI
#     print(f"Extracting {num_patches_x * num_patches_y} patches of size "
#           f"{patch_width}x{patch_height} from WSI file: {wsi_file}")
#
#     # Loop through each patch and extract the image
#     for i in range(num_patches_x):
#         for j in range(num_patches_y):
#             # Calculate the starting coordinates of the patch
#             start_x = i * patch_width
#             start_y = j * patch_height
#
#             # Extract the patch from the WSI
#             patch = slide.read_region((start_x, start_y), 0,
#                                       (patch_width, patch_height))
#
#             # Convert the patch to a NumPy array
#             patch_array = np.array(patch)
#
#             # Convert the RGBA image to BGR (remove alpha channel)
#             patch_bgr = cv2.cvtColor(patch_array[:, :, :3],
#                                      cv2.COLOR_RGBA2BGR)
#             # Check if the patch is a background image
#             if not is_patch_background(patch_bgr):
#                 # Save the patch as an image
#                 patch_filename = f"patch_{i}_{j}.{image_format}"
#                 patch_filepath = os.path.join(output_folder, patch_filename)
#                 cv2.imwrite(patch_filepath, patch_bgr)
#
#     # Close the WSI slide
#     slide.close()
#
#
# def jpg_from_wsi(wsi_file, patch_size, image_format, output_file):
#
#     # Open the WSI file
#     slide = openslide.open_slide(wsi_file)
#
#     top_size = slide.level_dimensions[len(slide.level_dimensions) - 1]
#     img_area = slide.read_region((0, 0), len(slide.level_dimensions) - 1,
#                                  top_size)
#     img_area = np.asarray(img_area, dtype=np.uint8)
#
#     # resize to patch_size
#     img_area = cv2.resize(img_area, patch_size)
#
#     # convert the slide to an image (image_format) of size patch_size and save it
#     output_filename = f"resized_wsi.{image_format}"
#     output_filepath = os.path.join(output_file)
#     cv2.imwrite(output_filepath, img_area)
#
#     # Close the WSI slide
#     slide.close()
#
#
# def main():
#     # Argument parser for specifying input and output directories
#     parser = argparse.ArgumentParser(description='WSI Tiling')
#     parser.add_argument('-i', '--input', help='Input directory of WSI files',
#                         required=False,
#                         default='../test_data/wsi_image_tiling/HE.svs')
#     parser.add_argument('-o', '--output', help='Output directory for tiles',
#                         required=False,
#                         default='../test_data/wsi_image_tiling/patches')
#     parser.add_argument('-s', '--size',
#                         help='Tile size in pixels (default: 512x512)',
#                         default='512x512')
#     parser.add_argument('-f', '--format', help='Image format (default: png)',
#                         default='png')
#     args = vars(parser.parse_args())
#
#     # Input directory of WSI files
#     wsi_file = args['input']
#     # Output directory for tiles
#     output_dir = args['output']
#     # Tile size in pixels
#     patch_size = tuple(map(int, args['size'].split('x')))
#     # Image format
#     image_format = args['format']
#
#     # extract_patches_from_wsi(wsi_file, patch_size, image_format, output_dir)
#     jpg_from_wsi(wsi_file, patch_size, image_format, output_dir)
#
#
# if __name__ == "__main__":
#     main()
#     ## test
#     # wsi_file = '../test_data/wsi_image_tiling/HE.svs'
#     # patch_size = (512, 512)
#     # output_folder = '../test_data/wsi_image_tiling/patches'
#     # image_format = 'png'
#     #
#     # extract_patches_from_wsi(wsi_file, patch_size, image_format, output_folder)


import argparse
import os
os.add_dll_directory(
    "C:/Users/mr38/Downloads/openslide-win64-20230414/openslide-win64-20230414/bin")
import openslide
import numpy as np
import cv2


def wsi_extract_top_view(input_path, out_path):
    img_raw = openslide.OpenSlide(input_path)
    top_size = img_raw.level_dimensions[len(img_raw.level_dimensions) - 1]
    img_area = img_raw.read_region((0, 0), len(img_raw.level_dimensions) - 1,
                                   top_size)
    img_area = np.asarray(img_area, dtype=np.uint8)
    # resize to patch_size
    img_area = cv2.resize(img_area, (512, 512))
    cv2.imwrite(out_path, img_area)


if __name__ == "__main__":
    # parser = argparse.ArgumentParser()
    # parser.add_argument('input_file', type=argparse.FileType('r'),
    #                     help='input file')
    # parser.add_argument('out_file', help='out file')
    # args = parser.parse_args()

    wsi_file = '../test_data/wsi_image_tiling/HE.svs'
    output_file = '../test_data/wsi_image_tiling/HE.png'

    wsi_extract_top_view(wsi_file, output_file)
