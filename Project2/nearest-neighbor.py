# TODO: Adjust indexing to begin from 1 instead of 0 to match expected output

from collections import defaultdict
from statistics import pstdev
import random
import math

random.seed()

""" Slightly different from example function provided
    In example function, data is provided in the original format
        Then, each data element is compared with every other data element to determine the nearest neighbor
    In this function, the data is passed in as two dictionaries whose key is the feature number and value is the list of feature values for all samples
    feature_to_add is the feature number that we are currently considering
"""
# For each 
# For each sample of data, 
def leave_one_out_cross_validation(data, current_features, feature_to_add):
    cat_1 = data[0]
    cat_2 = data[1]

    num_features = len(cat_1)
    num_samples = len(cat_1[0])

    distance = 0
    best_match = ""
    # Find distance using current_features and feature_to_add
    for feature_num in current_features:
        inner_diff = 0
        for samples in feature_num:
            print('cat_1[feature_num][samples] = ' + cat_1[feature_num][samples])
            inner_diff -= cat_1[feature_num][samples]
        distance += inner_diff**2

    i = 0
    for i < num_samples:
        best_match = ""
        curr_best = -1
        curr_best_index = -1
        j = 0
        for j < num_samples:
            if i != j:
                n = 0
                sum_squares = 0
                for n <= feature_to_add:
                    sum_squares += (cat_1[i][n] - cat_2[j][n])**2
                    print('cat_1[i][n] = ' + cat_1[i][n]) 
                    print('cat_2[i][n] = ' + cat_2[i][n]) 
                    n += 1
                distance = sqrt(sum_squares)
                print('distance = ' + distance)
                if distance < curr_best:
                    curr_best = distance
                    curr_best_index = j
            j += 1
        if 
        i += 1

    return 

file_in = open("CS170_SMALLtestdata__119.txt", 'r')

# Data is stored into 2 lists: one for each category
# Each feature is stored as a dictionary where the key is the index of the feature and the value is a list of the feature values
cat_1_raw = defaultdict(list)
cat_2_raw = defaultdict(list)
cat_1_norm = defaultdict(list)
cat_2_norm = defaultdict(list)

# Parse all data to perform normalization
category = -1
feature_num = 0
for line in file_in:
    for number in line.split():
        if number == ' ':
            continue
        # First number in the line specifies the category; set category
        if category == -1:
            category = float(number)

        # Current value is appended to the corresponding feature list
        else:
            if category == 1:
                cat_1_raw[feature_num].append(float(number))
            elif category == 2:
                cat_2_raw[feature_num].append(float(number))
            else:
                print("ERROR: category = " + category)
            feature_num += 1

    category = -1
    feature_num = 0

"""
for featurelist in cat_1_raw:
    print('\ncat_1_raw[' + str(featurelist) + '].size() = ' + str(len(cat_1_raw[featurelist])))
    print('featurelist: ' + str(cat_1_raw[featurelist]))
"""

# Calculate normalized value for each entry
for feature in cat_1_raw:
    mean = sum(cat_1_raw[feature]) / len(cat_1_raw[feature])
    std_dev = pstdev(cat_1_raw[feature])

    for element in cat_1_raw[feature]:
        cat_1_norm[feature].append((element - mean) / std_dev)

# Calculate normalized value for each entry
for feature in cat_2_raw:
    mean = sum(cat_2_raw[feature]) / len(cat_2_raw[feature])
    std_dev = pstdev(cat_2_raw[feature])

    for element in cat_2_raw[feature]:
        cat_2_norm[feature].append((element - mean) / std_dev)

"""
for featurelist in cat_1_norm:
    print('\ncat_1_norm[' + str(featurelist) + '].size() = ' + str(len(cat_1_norm[featurelist])))
    print('featurelist: ' + str(cat_1_norm[featurelist]))

"""

### FORWARD SEARCH FUNCTION
# Number of features in this dataset is equal to the num of keys in the dictionary
num_features = len(cat_1_norm)
level_accuracy = {} # A dictionary of len(num_features) whose keys are the lists of the highest accuracy at each level and values are the accuracy
current_features = []
i = 0
data = [cat_1_norm, cat_2_norm]
# Starting with a set of one feature, test each set of features for highest accuracy
# Outer loop is to traverse each level of the tree
while i < num_features:
    print('\nOn the ' + str(i + 1) + 'th level of the search tree:')
    # Feature to add at this level
    add_feature = -1
    # Best accuracy so far
    curr_best_acc = 0

    j = 0
    # Inner loop is to determine best feature to add on each level
    while j < num_features:
        if j + 1 not in current_features:
            print('\t- Considering adding feature ' + str(j + 1))
            # TODO: Implement the stub for this
            accuracy = leave_one_out_cross_validation(data, current_features, j)
            print('\t\t* Accuracy = ' + str(accuracy))

            if accuracy > curr_best_acc:
                curr_best_acc = accuracy
                print('\t\t* curr_best_acc = ' + str(curr_best_acc))
                add_feature = j
        j += 1
    if add_feature > -1:
        current_features.append(add_feature + 1)
        print('\t+ On level ' + str(i + 1) + ', feature ' + str(add_feature + 1) + ' added to current set')
        print('\tCurrent set: ' + str(current_features))
    
    level_accuracy[tuple(current_features)] = curr_best_acc
    i += 1

print('\n level_accuracy: ' + str(level_accuracy))
###

"""

# test_data is the left-out-one instance of data
def nearest_neighbor(test_data, ):

    for feature in features_list:
        
    
# Output to verify construction of feature sets
for featurelist in cat_1_raw:
    print('\ncat_1_raw[' + str(featurelist) + '].size() = ' + str(len(cat_1_raw[featurelist])))
    print('featurelist: ' + str(cat_1_raw[featurelist]))
for featurelist in cat_2_raw:
    print('\ncat_2_raw[' + str(featurelist) + '].size() = ' + str(len(cat_2_raw[featurelist])))
    print('featurelist: ' + str(cat_2_raw[featurelist]))
"""
