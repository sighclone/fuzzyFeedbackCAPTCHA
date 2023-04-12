import subprocess
import os
import cv2
import numpy as np
import math
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import os
import shutil
import sys

# Read solution from file
file = open("..\\fend\\src\\main\\resources\\com\\sadhu\\storage_section\\solution.txt", "r")
solution = list(str(file.read()))
print("The solution is: ", solution)

# Get user's answer from Java frontend (fend)
a = sys.argv
user_answer = list(str(a[1]))
print("The user's answer was: ", user_answer)

for i in a:
    print("\t->", i)

# Using the sol and ans, calculate the accuracy of answer
accuracy = 0
sol_len = 0
i = 0
while i in range(0, len(solution)) and i<len(user_answer):
    sol_len += 1
    accuracy += 1 if solution[i] == user_answer[i] else 0
    i+=1
accuracy = (accuracy / sol_len) * 100       # get percent value
print("Type of accuracy_score is: ", type(accuracy))
print("accuracy_score is: ", accuracy)
# Get the time taken to solve from JS frontend
time_taken = float(a[2])
print("time_taken is: ", time_taken)
print("Type of time_taken is: ", type(time_taken))


# We now have the two input variables:
#       i)  accuracy
#       ii) time_taken


# Define ranges of the variables
#
# i/p variables:
x_accuracy = np.arange(0, 101, 1)       # [0, 100] value range
x_time_taken = np.arange(0, 11, 1)      # [0, 10] value range
#
# o/p variables:
x_disposition = np.arange(10, 31, 1)      # [10, 30] value range
# x_noise = np.arange(1000, 2001, 1)        # [1000, 2000] value range

# Define the membership functions for the variables
# mf[0] -> low; mf[1] -> med; mf[2] -> high
# Input variables:
accuracy_mf = [fuzz.trimf(x_accuracy, [0, 0, 50]), fuzz.trimf(x_accuracy, [0, 50, 100]), fuzz.trimf(x_accuracy, [50, 50, 100])]
#
time_taken_mf = [fuzz.trimf(x_time_taken, [0, 0, 5]), fuzz.trimf(x_time_taken, [0, 5, 10]), fuzz.trimf(x_time_taken, [5, 5, 10])]
# Output variable:
disposition_mf = [fuzz.trimf(x_disposition, [0, 0, 5]), fuzz.trimf(x_disposition, [0, 5, 10]), fuzz.trimf(x_disposition, [5, 5, 10])]


accuracy_level = [fuzz.interp_membership(x_accuracy, accuracy_mf[0], accuracy), fuzz.interp_membership(x_accuracy, accuracy_mf[1], accuracy), fuzz.interp_membership(x_accuracy, accuracy_mf[2], accuracy)]
time_taken_level = [fuzz.interp_membership(x_time_taken, time_taken_mf[0], time_taken), fuzz.interp_membership(x_time_taken, time_taken_mf[1], time_taken), fuzz.interp_membership(x_time_taken, time_taken_mf[2], time_taken)]

import statistics as stcs
disposition_activations = [
    stcs.fmean([accuracy_level[0], time_taken_level[2]]),
    stcs.fmean([accuracy_level[1], time_taken_level[1]]),
    stcs.fmean([accuracy_level[2], time_taken_level[0]])
]

disp_aggregated = np.fmax(disposition_activations[0], np.fmax(disposition_activations[1], disposition_activations[2]))
disposition = fuzz.defuzz(np.max(disposition_activations), disp_aggregated, 'mom')


overlap_range = [15-disposition*12, 15+disposition*12] # scale the outputs

gen = subprocess.Popen(["python", "..\\captcha_alt_generator.py", "1", str(int(overlap_range[0])), str(int(overlap_range[1])), str(0), str(255), str(10), str(21), str(0), str(300)])

gen.wait()
