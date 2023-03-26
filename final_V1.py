from __future__ import division, print_function
import json
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np
import cv2
import pandas as pd
import numpy as np
import biosppy
import matplotlib.pyplot as plt
# Keras
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model
from keras.preprocessing import image

model = load_model('/home/ashie/arth/ecgScratchEpoch2.hdf5')
model.make_predict_function()      
print('Model loaded. Start serving...')
output = []


def model_predict(uploaded_files, model):
    flag = 1
    
    for path in uploaded_files:

        APC, NORMAL, LBB, PVC, PAB, RBB, VEB = [], [], [], [], [], [], []
        output.append(str(path))
        result = {"APC": APC, "Normal": NORMAL, "LBB": LBB, "PAB": PAB, "PVC": PVC, "RBB": RBB, "VEB": VEB}

        
        indices = []
        
        kernel = np.ones((4,4),np.uint8)
        
        csv = pd.read_csv(path)
        csv_data = csv[' Sample Value']
        data = np.array(csv_data)
        signals = []
        count = 1
        peaks =  biosppy.signals.ecg.christov_segmenter(signal=data, sampling_rate = 200)[0]
        for i in (peaks[1:-1]):
           diff1 = abs(peaks[count - 1] - i)
           diff2 = abs(peaks[count + 1]- i)
           x = peaks[count - 1] + diff1//2
           y = peaks[count + 1] - diff2//2
           signal = data[x:y]
           signals.append(signal)
           count += 1
           indices.append((x,y))

            
        for count, i in enumerate(signals):
            fig = plt.figure(frameon=True)
            plt.plot(i) 
            plt.xticks([]), plt.yticks([])
            for spine in plt.gca().spines.values():
                spine.set_visible(False)



            # frame = plt.gca()
            # frame.set_aspect('equal')
            # frame.spines['bottom'].set_linewidth(2)
            # frame.spines['left'].set_linewidth(2)
            # frame.spines['right'].set_visible(False)
            # frame.spines['top'].set_visible(False)

            filename = 'fig' + '.png'
            fig.savefig(filename)
          

            print("IM HERE")
            im_gray = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
            # open a frame and visualize a image save the image in a directory
            
            
            im_gray = cv2.erode(im_gray,kernel,iterations = 1)
            im_gray = cv2.resize(im_gray, (128, 128), interpolation = cv2.INTER_LANCZOS4)
            cv2.imwrite(filename, im_gray)
            im_gray = cv2.imread(filename)
            pred = model.predict(im_gray.reshape((1, 128, 128, 3)))
            pred_class = pred.argmax(axis=-1)
            if pred_class == 0:
                APC.append(indices[count]) 
            elif pred_class == 1:
                NORMAL.append(indices[count]) 
            elif pred_class == 2:    
                LBB.append(indices[count])
            elif pred_class == 3:
                PAB.append(indices[count])
            elif pred_class == 4:
                PVC.append(indices[count])
            elif pred_class == 5:
                RBB.append(indices[count]) 
            elif pred_class == 6:
                VEB.append(indices[count])
        


        result = sorted(result.items(), key = lambda y: len(y[1]))[::-1]   
        output.append(result)
        data = {}
        data['filename'+ str(flag)] = str(path)
        data['result'+str(flag)] = str(result)

        json_filename = 'data.txt'
        with open(json_filename, 'a+') as outfile:
            json.dump(data, outfile) 
        flag+=1 
    



    with open(json_filename, 'r') as file:
        filedata = file.read()
    filedata = filedata.replace('}{', ',')
    with open(json_filename, 'w') as file:
        file.write(filedata) 
    # os.remove('fig.png')      
    return output
    
    
uploaded_files = glob.glob('/home/ashie/arth/ECG-Arrhythmia-classification/sampled.csv')
pred = model_predict(uploaded_files, model)
result = str(pred)
print(result)