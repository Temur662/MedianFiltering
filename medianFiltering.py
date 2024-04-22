import orderStatistic as orderStat
import os 
import glob
import cv2 as cv
import numpy as np
from PIL import Image as img

import numpy as np

import numpy as np

def extract_nxn_subarray(arr, i, j, n):
    # Get the dimensions of the original array
    rows, cols = arr.shape
    
    # Calculate the half size to determine range around the center
    half_n = n // 2
    
    # Calculate start and end indices for rows and columns
    start_row = max(0, i - half_n)
    end_row = min(rows, i + half_n + 1)
    start_col = max(0, j - half_n)
    end_col = min(cols, j + half_n + 1)
    
    # Extract the subarray
    sub_array = arr[start_row:end_row, start_col:end_col]
    
    # Pad the subarray if necessary to ensure it is n x n
    if sub_array.shape != (n, n):
        pad_before_row = max(0, half_n - i)
        pad_after_row = max(0, i + half_n + 1 - rows)
        pad_before_col = max(0, half_n - j)
        pad_after_col = max(0, j + half_n + 1 - cols)
        sub_array = np.pad(sub_array,
                           ((pad_before_row, pad_after_row),
                            (pad_before_col, pad_after_col)),
                           mode='constant', constant_values=0)
    return sub_array

def filterImage():
    path = "/Users/temursayfutdinov/Documents/CompSci/CSC382(Algorithms)/Project1/pics/*.*"
    windowSize = int(input("What size window would you like to filter by: "))
    for file in glob.glob(pathname=path):
        imgNum = 0
        theImage = img.open(file)
        imgArr = np.array(theImage)
        if (len(imgArr.shape)) >= 3:
            imgArr = imgArr.reshape(imgArr.shape[0], -1).T
        for pixelRow in range(len(imgArr)):
            for pixelCol in range(len(imgArr[pixelRow])):
                threeByThreeBox = extract_nxn_subarray(imgArr, pixelRow, pixelCol, windowSize)
                # Use flatten method to turn 2d array into 1d array for filtering
                threeByThreeBox = threeByThreeBox.flatten()
                imgArr[pixelRow,pixelCol] = orderStat.orderStatistics(threeByThreeBox, len(threeByThreeBox) // 2)
        filterdImage = img.fromarray(imgArr)
        filterdImage.show()
        
        
if __name__ == "__main__":
    filterImage()
    
