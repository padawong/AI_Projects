from collections import defaultdict
import math

# For each of the current features and feature to add, find accuracy
#     by comparing testing accuracy of sample of data with those features
def leave_one_out_cross_validation(dataset, current_features, feature_to_add):
    num_correct = 0
    sample_line = 0

    # Compare each sample in the dataset with every other sample based on the current feature(s)
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


file_in = open("data.txt", 'r')

# For normalizing, all values of all features are stored into a dictionary
features_raw = defaultdict(list)

# All data is stored in original positions in a 2D list
dataset = []

# Parse all data to perform normalization
category = -1
feature_num = 0
for line in file_in:
    dataline = []
    for number in line.split():
        # Parse features into a 2D matrix that holds all data in the same positions as the original file
        dataline.append(float(number))
        feature_values = []

        # First number in the line specifies the category; set category
        if category == -1:
            category = float(number)

        else:
            features_raw[feature_num].append(float(number))
            feature_num += 1
        # Current value is appended to the corresponding feature list

    category = -1
    feature_num = 0
    dataset.append(dataline)


# Normalize all data in the dataset by referring to the appropriate category
for line in dataset:
    n = 0
    for number in line:
        if n == 0:
            n += 1
            continue

        """
        if line[0] == 1:
            print('min(cat_1_raw[' + str(n-1) + ']) = ' + str(min(cat_1_raw[n-1])))
            print('max(cat_1_raw[' + str(n-1) + ']) = ' + str(max(cat_1_raw[n-1])))
            print('cat_1_raw[' + str(n-1) + '] = ' + str(cat_1_raw[n-1]))
            minimum = min(cat_1_raw[n-1])
            maximum = max(cat_1_raw[n-1])
        elif line[0] == 2:
            print('min(cat_2_raw[' + str(n-1) + ']) = ' + str(min(cat_2_raw[n-1])))
            print('max(cat_2_raw[' + str(n-1) + ']) = ' + str(max(cat_2_raw[n-1])))
            print('cat_2_raw[' + str(n-1) + '] = ' + str(cat_2_raw[n-1]))
            minimum = min(cat_2_raw[n-1])
            maximum = max(cat_2_raw[n-1])

        print('line[' + str(n) + '] = ' + str(line[n]))
        print('number = ' + str(number))
        """
        minimum = min(features_raw[n-1])
        maximum = max(features_raw[n-1])
        line[n] = (number - minimum) / (maximum - minimum)
        n += 1

### FORWARD SEARCH FUNCTION
# Number of features in this dataset is equal to the num of keys in the dictionary
num_features = len(features_raw)
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

