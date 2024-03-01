import os
import subprocess

# Base path where the LUT files are stored
base_path = 'luts'
# Path to the standard test image you want to apply the LUTs to
test_image_path = 'test_image.jpg'
# Base path for saving the generated thumbnails
thumbnails_base_path = 'thumbnails'

def generate_thumbnails(base_path, test_image_path, thumbnails_base_path):
    categories = os.listdir(base_path)
    for category in categories:
        category_path = os.path.join(base_path, category)
        thumbnail_category_path = os.path.join(thumbnails_base_path, category)
        os.makedirs(thumbnail_category_path, exist_ok=True)  # Create the category directory for thumbnails

        if os.path.isdir(category_path):  # Ensure it's a directory
            luts = os.listdir(category_path)
            for lut in luts:
                lut_path = os.path.join(category_path, lut)
                lut_name = os.path.splitext(lut)[0]  # Removing the file extension
                thumbnail_path = os.path.join(thumbnail_category_path, f"{lut_name}.jpg")
                
                # FFmpeg command to apply LUT and save the thumbnail
                ffmpeg_cmd = [
                    'ffmpeg',
                    '-y',  # Overwrite output files without asking
                    '-i', test_image_path,  # Input file (the test image)
                    '-vf', f"lut3d={lut_path}",  # Apply the 3D LUT filter
                    thumbnail_path  # Output file
                ]
                
                # Execute the FFmpeg command
                subprocess.run(ffmpeg_cmd)

if __name__ == "__main__":
    generate_thumbnails(base_path, test_image_path, thumbnails_base_path)
