import cv2
import os
from scipy.interpolate import UnivariateSpline
import numpy as np

def rename_image(file_path, new_name):
    file_path = 'upload/'+file_path

    directory = os.path.dirname(file_path)

    new_path = os.path.join(directory, new_name)

    os.rename(file_path, new_path)

def rescale(image, image_path, token):
    name = os.path.basename(image_path)
    rename_image(name, token+name)
    width = int(270)
    height = int(390)
    boyut = (width, height)
    return cv2.resize(image, boyut, interpolation=cv2.INTER_AREA)

def convert_to_image_gray(image_path, token): # Bu çalışıyor
    gray_image=rescale(cv2.imread(image_path,0), image_path, token)
    name=image_path.split("/")[-1]
    cv2.imwrite(token+name,gray_image)

def applyPencilSketch(image_path, token, display=True): # Bu çalışıyor
    image = rescale(cv2.imread(image_path), image_path, token)

    if image is None:
        print("Error: Failed to read image file")
        return None

    if image.shape[-1] == 1:
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    elif image.shape[-1] == 4:
        image = cv2.cvtColor(image, cv2.COLOR_RGBA2BGR)

    gray_sketch, color_sketch = cv2.pencilSketch(image, sigma_s=20, sigma_r=0.5, shade_factor=0.02)


    if display:
        name = os.path.basename(image_path)
        cv2.imwrite(token+name, color_sketch)

    else:
        return color_sketch

def applyPencilSketch2(image_path, token, display=True):# Bu çalışıyor
    image = rescale(cv2.imread(image_path), image_path, token)

    if image is None:
        print("Error: Failed to read image file")
        return None

    if image.shape[-1] == 1:
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    elif image.shape[-1] == 4:
        image = cv2.cvtColor(image, cv2.COLOR_RGBA2BGR)

    gray_sketch, color_sketch = cv2.pencilSketch(image, sigma_s=20, sigma_r=0.5, shade_factor=0.02)

    if display:
        name = os.path.basename(image_path)
        cv2.imwrite(token+name, gray_sketch)
    else:
        return gray_sketch

def applyGotham(image_path, token, display=True):# Bu çalışıyor
    image = rescale(cv2.imread(image_path), image_path, token)
    midtone_contrast_increase = UnivariateSpline(x=[0, 25, 51, 76, 102, 128, 153, 178, 204, 229, 255],
                                                 y=[0, 13, 25, 51, 76, 128, 178, 204, 229, 242, 255])(range(256))

    lowermids_increase = UnivariateSpline(x=[0, 16, 32, 48, 64, 80, 96, 111, 128, 143, 159, 175, 191, 207, 223, 239, 255],
                                          y=[0, 18, 35, 64, 81, 99, 107, 112, 121, 143, 159, 175, 191, 207, 223, 239, 255])(range(256))


    uppermids_decrease = UnivariateSpline(x=[0, 16, 32, 48, 64, 80, 96, 111, 128, 143, 159, 175, 191, 207, 223, 239, 255],
                                          y=[0, 16, 32, 48, 64, 80, 96, 111, 128, 140, 148, 160, 171, 187, 216, 236, 255])(range(256))

    blue_channel, green_channel, red_channel = cv2.split(image)
    red_channel = cv2.LUT(red_channel, midtone_contrast_increase.astype(np.uint8))
    blue_channel = cv2.LUT(blue_channel, lowermids_increase.astype(np.uint8))
    blue_channel = cv2.LUT(blue_channel, uppermids_decrease.astype(np.uint8))
    output_image = cv2.merge((blue_channel, green_channel, red_channel))

    if display:
        name = os.path.basename(image_path)
        cv2.imwrite(token+name, output_image)
    else:
        return output_image

def applyWarm(image_path, token, display=True):# Bu çalışıyor
    image = rescale(cv2.imread(image_path), image_path, token)
    blue_channel, green_channel, red_channel = cv2.split(image)

    increase_table = np.array([i+50 if i+50 < 255 else 255 for i in np.arange(0, 256)]).astype("uint8")
    decrease_table = np.array([i-30 if i-30 > 0 else 0 for i in np.arange(0, 256)]).astype("uint8")

    red_channel = cv2.LUT(red_channel, increase_table)
    blue_channel = cv2.LUT(blue_channel, decrease_table)

    output_image = cv2.merge((blue_channel, green_channel, red_channel))

    if display:
        name = os.path.basename(image_path)
        cv2.imwrite(token+name, output_image)
    else:
        return output_image

def applyCold(image_path, token, display=True):
    image = rescale(cv2.imread(image_path), image_path, token)
    blue_channel, green_channel, red_channel = cv2.split(image)

    increase_table = np.array([i+15 if i+15<255 else 255 for i in np.arange(0,256)]).astype("uint8")
    decrease_table = np.array([i-15 if i-15>0 else 0 for i in np.arange(0,256)]).astype("uint8")

    red_channel = cv2.LUT(red_channel, decrease_table).astype(np.uint8)
    blue_channel = cv2.LUT(blue_channel, increase_table).astype(np.uint8)
    output_image = cv2.merge((blue_channel, green_channel, red_channel))

    if display:
        name = os.path.basename(image_path)
        cv2.imwrite(token+name, output_image)
    else:
        return output_image

def applyGrayscale(image_path, token, display=True):# Bu çalışıyor
    image = rescale(cv2.imread(image_path), image_path, token)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    output_image = cv2.merge((gray, gray, gray))
    if display:
        name = os.path.basename(image_path)
        cv2.imwrite(token+name, output_image)
    else:
        return output_image

def applySepia(image_path, token, display=True,):# Bu çalışıyor
    image = rescale(cv2.imread(image_path), image_path, token)
    image_float = np.float64(image)
    blue_channel, green_channel, red_channel = cv2.split(image_float)
    output_blue = (red_channel * .272) + (green_channel *.534) + (blue_channel * .131)
    output_green = (red_channel * .349) + (green_channel *.686) + (blue_channel * .168)
    output_red = (red_channel * .393) + (green_channel *.769) + (blue_channel * .189)
    output_image = cv2.merge((output_blue, output_green, output_red))

    sepia_matrix = np.array([[.272, .534, .131],
                             [.349, .686, .168],
                             [.393, .769, .189]], dtype=np.float64)
    output_image = np.clip(np.dot(output_image, sepia_matrix.T), 0, 255).astype(np.uint8)

    if display:
        name = os.path.basename(image_path)
        cv2.imwrite(token+name, output_image)
    else:
        return output_image

def applySharpening(image_path, token, display=True):# Bu çalışıyor
    image = rescale(cv2.imread(image_path), image_path, token)

    sharpening_kernel = np.array([[-1, -1, -1],
                                  [-1, 9.4, -1],
                                  [-1, -1, -1]]) / 2.0 

    sharpened_image = cv2.filter2D(image, -1, sharpening_kernel)

    if display:
        name = os.path.basename(image_path)
        cv2.imwrite(token+name, sharpened_image)
    else:
        return sharpened_image

def applySharpening2(image_path, token, display=True):# Bu çalışıyor
    image = rescale(cv2.imread(image_path), image_path, token)

    sharpening_kernel = np.array([[-1, -1, -1],
                                  [-1, 9.4, -1],
                                  [-1, -1, -1]]) / 9.0

    sharpened_image = cv2.filter2D(image, -1, sharpening_kernel)

    if display:
        name = os.path.basename(image_path)
        cv2.imwrite(token+name, sharpened_image)
    else:
        return sharpened_image

def applyStylization(image_path, token, display=True):# Bu çalışıyor@
    image = rescale(cv2.imread(image_path), image_path, token)
    output_image = cv2.stylization(image, sigma_s=15, sigma_r=0.55)
    if display:
        name = os.path.basename(image_path)
        cv2.imwrite(token+name, output_image)
    else:
        return output_image

def applyInvert(image_path, token, display=True):# Bu çalışıyor@
    image = rescale(cv2.imread(image_path), image_path, token)
    output_image = cv2.bitwise_not(image)
    if display:
        name = os.path.basename(image_path)
        cv2.imwrite(token+name, output_image)
    else:
        return output_image

def reverseReflection(image_path, token, display=True):# Bu çalışıyor
    dog = rescale(cv2.imread(image_path), image_path, token)
    if display:
        reverse_flip = np.fliplr(dog)
        name = os.path.basename(image_path)
        cv2.imwrite(token+name, reverse_flip)
    return reverse_flip

def horizontalStack(image_path, token):# Bu çalışıyor
    img=rescale(cv2.imread(image_path), image_path, token)
    hor=np.hstack((img,img))
    name = os.path.basename(image_path)
    cv2.imwrite(token+name, hor)

def verticalStack(image_path, token):# Bu çalışıyor
    img=rescale(cv2.imread(image_path), image_path, token)
    ver=np.vstack((img,img))
    name = os.path.basename(image_path)
    cv2.imwrite(token+name, ver)
