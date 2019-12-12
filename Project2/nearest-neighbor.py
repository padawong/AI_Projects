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
# For each of the current features and feature to add, find accuracy
#     by comparing testing accuracy of sample of data with those features
# for number of features being tested
#     for every sample (index 0 to num of samples)
def leave_one_out_cross_validation(dataset, current_features, feature_to_add):
    # print('current_features = ' + str(current_features) + '; feature_to_add = ' + str(feature_to_add))
    
    num_correct = 0

    sample_line = 0
    for sample in dataset:
        curr_best = -1
        curr_best_line = -1

        compare_line = 0
        for compare in dataset:
            if sample != compare:
                distance = 0.0
                for feature in current_features:
                    distance += (sample[feature] - compare[feature])**2
                distance += (sample[feature_to_add] - compare[feature_to_add])**2
                distance = math.sqrt(distance)
                    
                if curr_best < 0 or distance < curr_best:
                    curr_best = distance
                    curr_best_line = compare_line

            compare_line += 1
        if dataset[sample_line][0] == dataset[curr_best_line][0]:
            num_correct += 1
        sample_line += 1

    accuracy = num_correct / len(dataset)
    return accuracy

"""




    num_features = len(cat_1)
    distance = 0.0
    curr_best = -1
    best_cat = 0
    num_correct = 0
    
    # Iterate through all cat_1 samples in terms of the specified features
    # Compare to each other sample in order to determine predicted class
    i = 0
    while i < len(cat_1[0]):

        # Compare with all other samples in cat_1
        j = 0
        while j < len(cat_1[0]):
            if i != j:
                # print('i = ' + str(i) + '; j = ' + str(j))
                # Calculate (potentially multidimensional) Euclidean Distance
                # TODO: Figure out if should use a different distance metric
                inner_diff = 0.0
                distance = 0.0
                for feature in current_features:
                    #print('i = ' + str(i) + '; j = ' + str(j) + 'feature = ' + str(feature) + '; current_features = ' + str(current_features) + '; cat_1[feature - 1][i] = ' + str(cat_1[feature - 1][i]) + '; cat_1[feature - 1][j] = ' + str(cat_1[feature - 1][j]))
                    inner_diff = cat_1[feature - 1][i] - cat_1[feature - 1][j]
                    distance += inner_diff**2
                #print('feature_to_add = ' + str(feature_to_add) + '; cat_1[feature_to_add][' + str(i) + '] = ' + str(cat_1[feature_to_add][i]) + '; cat_1[f_t_a][' + str(j) + '] = ' + str(cat_1[feature_to_add][j]))
                inner_diff = cat_1[feature_to_add][i] - cat_1[feature_to_add][j]
                distance += inner_diff**2
                distance = math.sqrt(distance)
                #print('distance = ' + str(distance))

                if curr_best < 0 or distance < curr_best:
                    curr_best = distance
                    best_cat = 1
            j += 1

        # Compare with all samples in cat_2
        j = 0
        while j < len(cat_2[0]):
            inner_diff = 0
            distance = 0.0
            for feature in current_features:
                #print('i = ' + str(i) + '; j = ' + str(j) + 'feature = ' + str(feature) + '; current_features = ' + str(current_features) + '; cat_1[feature - 1][i] = ' + str(cat_1[feature - 1][i]) + '; cat_2[feature - 1][j] = ' + str(cat_2[feature - 1][j]))
                inner_diff = cat_1[feature - 1][i] - cat_2[feature - 1][j]
                distance += inner_diff**2
            #print('feature_to_add = ' + str(feature_to_add) + '; cat_1[feature_to_add][' + str(i) + '] = ' + str(cat_1[feature_to_add][i]) + '; cat_2[f_t_a][' + str(j) + '] = ' + str(cat_2[feature_to_add][j]))
            inner_diff = cat_1[feature_to_add][i] - cat_2[feature_to_add][j]
            distance += inner_diff**2
            distance = math.sqrt(distance)
            #print('distance = ' + str(distance))

            if curr_best < 0 or distance < curr_best:
                curr_best = distance
                best_cat = 2
            j += 1
        i += 1 

        # Matched correct category
        if best_cat == 1:
            num_correct += 1
            #print('cat_1[' + str(i) + '] is correct!')

    # Iterate through all cat_2 samples in terms of the specified features
    # Compare to each other sample in order to determine predicted class
    curr_best = -1
    i = 0
    while i < len(cat_2[0]):

        # Compare with all other samples in cat_2
        j = 0
        #print('\n\n')
        while j < len(cat_2[0]):
            if i != j:
                distance = 0.0
                inner_diff = 0.0
                for feature in current_features:
                    #print('i = ' + str(i) + '; j = ' + str(j) + 'feature = ' + str(feature) + '; current_features = ' + str(current_features) + '; cat_2[feature - 1][i] = ' + str(cat_2[feature - 1][i]) + '; cat_2[feature - 1][j] = ' + str(cat_2[feature - 1][j]))
                    inner_diff = cat_2[feature - 1][i] - cat_2[feature - 1][j]
                    distance += inner_diff**2
                #print('feature_to_add = ' + str(feature_to_add) + '; cat_2[feature_to_add][' + str(i) + '] = ' + str(cat_2[feature_to_add][i]) + '; cat_2[f_t_a][' + str(j) + '] = ' + str(cat_2[feature_to_add][j]))
                inner_diff = cat_2[feature_to_add][i] - cat_2[feature_to_add][j]
                distance += inner_diff**2
                distance = math.sqrt(distance)
                #print('distance = ' + str(distance))

                if curr_best < 0 or distance < curr_best:
                    curr_best = distance
                    best_cat = 2
            j += 1

        # Compare with all samples in cat_1
        j = 0
        while j < len(cat_1[0]):
            distance = 0.0
            inner_diff = 0.0
            for feature in current_features:
                #print('i = ' + str(i) + '; j = ' + str(j) + 'feature = ' + str(feature) + '; current_features = ' + str(current_features) + '; cat_2[feature - 1][i] = ' + str(cat_2[feature - 1][i]) + '; cat_1[feature - 1][j] = ' + str(cat_1[feature - 1][j]))
                inner_diff = cat_2[feature - 1][i] - cat_1[feature - 1][j]
                distance += inner_diff**2
            #print('feature_to_add = ' + str(feature_to_add) + '; cat_2[feature_to_add][' + str(i) + '] = ' + str(cat_2[feature_to_add][i]) + '; cat_1[f_t_a][' + str(j) + '] = ' + str(cat_1[feature_to_add][j]))
            inner_diff = cat_2[feature_to_add][i] - cat_1[feature_to_add][j]
            distance += inner_diff**2
            distance = math.sqrt(distance)
            #print('distance = ' + str(distance))

            if curr_best < 0 or distance < curr_best:
                curr_best = distance
                best_cat = 1
            j += 1
        i += 1 

        # Matched correct category
        if best_cat == 2:
            num_correct += 1
            #print('cat_2[' + str(i) + '] is correct!')

    print('\t\tnum correct = ' + str(num_correct))
    print('\t\tlen(cat_1[0]) = ' + str(len(cat_1[0])) + '\tlen(cat_2[0])) = ' + str(len(cat_2[0])))
    accuracy = num_correct / (len(cat_1[0]) + len(cat_2[0]))
    print('\t\taccuracy = ' + str(accuracy))
    return accuracy
"""

file_in = open("data.txt", 'r')

# Data is stored into 2 lists: one for each category
# Each feature is stored as a dictionary where the key is the index of the feature and the value is a list of the feature values
cat_1_raw = defaultdict(list)
cat_2_raw = defaultdict(list)
dataset = []

# Parse all data to perform normalization
category = -1
feature_num = 0
for line in file_in:
    dataline = []
    for number in line.split():
        # Parse features into a 2D matrix that holds all data in the same positions as the original file
        dataline.append(float(number))

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
                print("ERROR: category = " + str(category))
            feature_num += 1

    category = -1
    feature_num = 0
    dataset.append(dataline)

"""
for featurelist in cat_1_raw:
    print('\ncat_1_raw[' + str(featurelist) + '].size() = ' + str(len(cat_1_raw[featurelist])))
    print('featurelist: ' + str(cat_1_raw[featurelist]))

print('Raw Dataset: ')
n = 0
for line in dataset:
    print(str(n) + ': ' + str(line))
    n += 1

# Normalize all data in the dataset by referring to the appropriate category
for line in dataset:
    n = 0
    for number in line:
        mean = 0
        std_dev = 0

        if n == 0:
            n += 1
            continue

        if line[0] == 1:
            #print('sum(cat_1_raw[' + str(n-1) + ']) = ' + str(sum(cat_1_raw[n-1])))
            #print('len(cat_1_raw[' + str(n-1) + ']) = ' + str(len(cat_1_raw[n-1])))
            #print('cat_1_raw[' + str(n-1) + '] = ' + str(cat_1_raw[n-1]))
            mean = sum(cat_1_raw[n-1]) / len(cat_1_raw[n-1])
            std_dev = pstdev(cat_1_raw[n-1])
        elif line[0] == 2:
            #print('sum(cat_2_raw[' + str(n-1) + ']) = ' + str(sum(cat_2_raw[n-1])))
            #print('len(cat_2_raw[' + str(n-1) + ']) = ' + str(len(cat_2_raw[n-1])))
            #print('cat_2_raw[' + str(n-1) + '] = ' + str(cat_2_raw[n-1]))
            mean = sum(cat_2_raw[n-1]) / len(cat_2_raw[n-1])
            std_dev = pstdev(cat_2_raw[n-1])

        #print('line[' + str(n) + '] = ' + str(line[n]))
        #print('number = ' + str(number))
        line[n] = (number - mean) / std_dev
        n += 1

print('Normalized Dataset: ')
n = 0
for line in dataset:
    print(str(line))
    n += 1

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

for featurelist in cat_1_norm:
    print('\ncat_1_norm[' + str(featurelist) + '].size() = ' + str(len(cat_1_norm[featurelist])))
    print('featurelist: ' + str(cat_1_norm[featurelist]))
"""

### FORWARD SEARCH FUNCTION
# Number of features in this dataset is equal to the num of keys in the dictionary
num_features = len(cat_1_raw)
level_accuracy = {} # A dictionary of len(num_features) whose keys are the lists of the highest accuracy at each level and values are the accuracy
current_features = []
i = 0
# Starting with a set of one feature, test each set of features for highest accuracy
# Outer loop is to traverse each level of the tree
while i < num_features:
    print('\nOn level ' + str(i + 1) + ' of the search tree:')
    # Feature to add at this level
    add_feature = -1
    # Best accuracy so far
    curr_best_acc = 0

    j = 0
    # Inner loop is to determine best feature to add on each level
    while j < num_features:
        if j + 1 not in current_features:
            print('\t- Considering adding feature ' + str(j + 1))
            accuracy = leave_one_out_cross_validation(dataset, current_features, j + 1)
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
