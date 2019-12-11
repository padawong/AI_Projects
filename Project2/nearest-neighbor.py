# TODO: Adjust indexing to begin from 1 instead of 0 to match expected output

from collections import defaultdict
from statistics import pstdev

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
current_features = []
# Starting with a set of one feature, test each set of features for highest accuracy
i = 0
while i < num_features:
    print('On the ' + i + 'th level of the search tree:\n')
    # Feature to add at this level
    add_feature = -1
    # Best accuracy so far
    curr_best_acc = 0

    j = 0
    while j < num_features:
        if cat_1_norm[i][j] not in current_features:
            print('\t- Considering adding the ' + j + 'th feature\n')
            # TODO: Implement the stub for this
            accuracy = leave_one_out_cross_validation(data, current_features, j + 1)

            if accuracy > curr_best_acc:
                curr_best_acc = accuracy
                add_feature = j
        j += 1
    if add_feature > -1:
        current_set[i].append(add_feature)
        print('\t+ On level ' + i + ', feature ' + add_feature + 'added to current set')
    i += 1
###

# test_data is the left-out-one instance of data
def nearest_neighbor(test_data, ):

    for feature in features_list:
        
"""
    
# Output to verify construction of feature sets
for featurelist in cat_1_raw:
    print('\ncat_1_raw[' + str(featurelist) + '].size() = ' + str(len(cat_1_raw[featurelist])))
    print('featurelist: ' + str(cat_1_raw[featurelist]))
for featurelist in cat_2_raw:
    print('\ncat_2_raw[' + str(featurelist) + '].size() = ' + str(len(cat_2_raw[featurelist])))
    print('featurelist: ' + str(cat_2_raw[featurelist]))
"""
