from collections import defaultdict
import math
import time

# For each of the current features and feature to add, find accuracy
#     by comparing testing accuracy of sample of data with those features
# For personal algorithm, number of min misses so far will be passed in instead of a string specifying the algorithm
def leave_one_out_cross_validation(dataset, current_features, feature_to_consider, algorithm):
    num_correct = 0
    misses = 0

    # Call from personal algorithm
    if algorithm.isnumeric():
        min_misses = int(algorithm)

    temp_features = current_features.copy()
    if algorithm == 'backward':
        temp_features.remove(feature_to_consider)

    # Compare each sample in the dataset with every other sample based on the current feature(s)
    sample_line = 0
    for sample in dataset:
        curr_best = -1
        curr_best_line = -1

        compare_line = 0
        for compare in dataset:
            if sample != compare:
                distance = 0.0

                for feature in temp_features:
                    distance += (sample[feature] - compare[feature])**2

                if algorithm == 'forward' or algorithm.isnumeric():
                    distance += (sample[feature_to_consider] - compare[feature_to_consider])**2

                distance = math.sqrt(distance)
                    
                if curr_best < 0 or distance < curr_best:
                    curr_best = distance
                    curr_best_line = compare_line

            compare_line += 1
        if dataset[sample_line][0] == dataset[curr_best_line][0]:
            num_correct += 1
        else:
            misses += 1
        sample_line += 1

        # For personal algorithm, if number of misses exceeds the minimum passed in, stop checking how lousy it is and return
        if algorithm.isnumeric() and misses > min_misses:
            accuracy = 0
            return accuracy, misses

    accuracy = num_correct / len(dataset)
    return accuracy, misses

# Pass data from file into list of lists in original positions
# Generate lists of features to perform normalization
def parse_file(file_loc):
    file_in = open(file_loc, 'r')

    # Parse all data to perform normalization
    # For normalizing, all values of all features are stored into a dictionary
    features_raw = defaultdict(list)

    # All data is stored in original positions in a 2D list
    dataset = []
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
    return dataset, features_raw


# Normalize all data in the dataset by referring to the appropriate category
def normalize(dataset, features_raw):
    for line in dataset:
        n = 0
        for number in line:
            if n == 0:
                n += 1
                continue

            minimum = min(features_raw[n-1])
            maximum = max(features_raw[n-1])
            line[n] = (number - minimum) / (maximum - minimum)
            n += 1
    return dataset, len(features_raw)


# FORWARD SEARCH FUNCTION
def forward_search(dataset, num_features):
    level_accuracy = {} 
    current_features = []
    best_accuracy = 0
    best_set = []

    i = 0
    # Starting with a set of one feature, test each set of features for highest accuracy
    # Outer loop is to traverse each level of the tree
    while i < num_features:
        if num_features < 100:
            print('\nOn level ' + str(i + 1) + ' of the search tree:')
        # Feature to add at this level
        add_feature = -1
        # Best accuracy so far
        curr_best_acc = 0

        j = 0
        # Inner loop is to determine best feature to add on each level
        while j < num_features:
            if j + 1 not in current_features:
                if num_features < 100:
                    print('\t- Considering adding feature ' + str(j + 1))
                accuracy, null = leave_one_out_cross_validation(dataset, current_features, j + 1, 'forward')
                temp_features = current_features.copy()
                temp_features.append(j+1)
                if num_features < 100:
                    print('\t\t* Accuracy for ' + str(temp_features) + ' = {:.1%}'.format(accuracy))

                if accuracy > curr_best_acc:
                    curr_best_acc = accuracy
                    add_feature = j
            j += 1
        
        if add_feature > -1:
            current_features.append(add_feature + 1)
            print('\t+ On level ' + str(i + 1) + ', feature ' + str(add_feature + 1) + ' added to current set')
            print('\tCurrent set: ' + str(current_features) + ' -- {:.1%}'.format(curr_best_acc))

        if curr_best_acc < best_accuracy and i != num_features - 1:
            print('\n*** WARNING: accuracy has decreased. Continuing search in case of local maxima ***')
        
        if curr_best_acc > best_accuracy:
            best_accuracy = curr_best_acc
            best_set = current_features.copy()
            
        level_accuracy[tuple(current_features)] = curr_best_acc
        i += 1

    return best_accuracy, best_set


# BACKWARD SEARCH FUNCTION
def backward_search(dataset, num_features):
    level_accuracy = {} 
    current_features = list(range(1, num_features + 1))
    best_accuracy = 0
    best_set = []

    i = num_features
    # Starting with a set of all features, test each subset for highest accuracy
    # Outer loop is to traverse each level of the tree

    accuracy, null = leave_one_out_cross_validation(dataset, current_features, 0, 'initial')
    print('\nAccuracy for initial set ' + str(current_features) + ' = {:.1%}'.format(accuracy))

    while i > 1:
        if num_features < 100:
            print('\nOn level ' + str(i) + ' of the search tree:')
        # Feature to remove at this level
        remove_feature = -1

        curr_best_acc = -1

        # Inner loop is to determine best feature to remove on each level
        for feature in current_features:
            if num_features < 100:
                print('\t- Considering removing feature ' + str(feature))
            accuracy, null = leave_one_out_cross_validation(dataset, current_features, feature, 'backward')
            temp_features = current_features.copy()
            temp_features.remove(feature)
            if num_features < 100:
                print('\t\t* Accuracy for ' + str(temp_features) + ' = {:.1%}'.format(accuracy))

            if accuracy > curr_best_acc:
                curr_best_acc = accuracy
                remove_feature = feature
        
        if remove_feature > -1:
            current_features.remove(remove_feature)
            print('\t+ On level ' + str(i) + ', feature ' + str(remove_feature) + ' removed from current set')
            print('\tCurrent set: ' + str(current_features) + ' -- {:.1%}'.format(curr_best_acc))

        if curr_best_acc > best_accuracy:
            best_accuracy = curr_best_acc
            best_set = current_features.copy()
           
        level_accuracy[tuple(current_features)] = curr_best_acc
        i -= 1

    return best_accuracy, best_set


# Following the method discussed during lecture:
#   Keep track of the lowest number of incorrect matches during leave_one_out
#   If a feature has a higher number of incorrect matches, immediately stop and remove it
def secret_sauce(dataset, num_features):
    level_accuracy = {} 
    current_features = []
    best_accuracy = 0
    best_set = []

    i = 0
    # Starting with a set of one feature, test each set of features for highest accuracy
    # Outer loop is to traverse each level of the tree
    while i < num_features:
        print('\nOn level ' + str(i + 1) + ' of the search tree:')
        # Feature to add at this level
        add_feature = -1
        # Best accuracy so far
        curr_best_acc = 0

        lowest_incorr = len(dataset)
        j = 0
        # Inner loop is to determine best feature to add on each level
        while j < num_features:
            if j + 1 not in current_features:
                print('\t- Considering adding feature ' + str(j + 1))
                accuracy, misses = leave_one_out_cross_validation(dataset, current_features, j + 1, str(lowest_incorr))

                # Sampling was terminated early
                if misses > lowest_incorr:
                    print('\t\t* Feature ' + str(j + 1) + ' has at least ' + str(misses) + ' misses, exceeding feature ' + str(least_miss_ft) + '\'s ' + str(lowest_incorr) + ' misses.')
                    print('\t\t\tAccuracy calculation terminated before completion.')
                elif misses < lowest_incorr:
                    lowest_incorr = misses
                    least_miss_ft = j + 1
                    print('\t\t* Feature ' + str(least_miss_ft) + ' has the lowest number of misses among features tested so far at this level.')

                    # Accuracy only calculated for lowest miss feature
                    temp_features = current_features.copy()
                    temp_features.append(j+1)
                    print('\t\t* New lowest number of misses: ' + str(lowest_incorr))
                    print('\t\t* Accuracy for ' + str(temp_features) + ' = {:.1%}'.format(accuracy))

                    # Update accuracy only if a new lowest miss num was found
                    if accuracy > curr_best_acc:
                        curr_best_acc = accuracy
                        add_feature = j
            j += 1
        
        if add_feature > -1:
            current_features.append(add_feature + 1)
            print('\t+ On level ' + str(i + 1) + ', feature ' + str(add_feature + 1) + ' added to current set')
            print('\tCurrent set: ' + str(current_features) + ' -- {:.1%}'.format(curr_best_acc))

        if curr_best_acc < best_accuracy and i != num_features - 1:
            print('\n*** WARNING: accuracy has decreased. Continuing search in case of local maxima ***')
        
        if curr_best_acc > best_accuracy:
            best_accuracy = curr_best_acc
            best_set = current_features.copy()
            
        level_accuracy[tuple(current_features)] = curr_best_acc
        i += 1

    return best_accuracy, best_set


print('Welcome to Erin Wong\'s Feature Selection Algorithm!\n')
print('Please choose a file to test: ')
print('1) Small data set')
print('2) Large data set')
print('3) Enter file path')
sel = input()
while sel != '1' and sel != '2' and sel != '3':
    print('Please make a valid selection:')
    sel = input()

file_loc = ''
if sel == '1':
    file_loc = 'CS170_SMALLtestdata__35.txt'
elif sel == '2':
    file_loc = 'CS170_LARGEtestdata__37.txt'
else:
    print('Please type in the name of the file to test: ')
    file_loc = input()

print('\nType the number of the algorithm you wish to run:')
print('1) Forward Selection')
print('2) Backward Elimination')
print('3) Erin\'s Special Algorithm')
sel = input()
while sel != '1' and sel != '2' and sel != '3':
    print('Please make a valid selection:')
    sel = input()

dataset, features_raw = parse_file(file_loc)
print('\nThe dataset has ' + str(len(features_raw)) + ' features (not including the class attribute), with ' + str(len(dataset)) + ' instances.')
print('Please wait while data is normalized...')
dataset, num_features = normalize(dataset, features_raw)
print('\tDone!')
print('\n*** PLEASE NOTE: Large number of features detected. Most print statements will be suppressed')

best_accuracy = 0.0
best_set = []

start_time = time.time()

# Forward Selection
if sel == '1':
    print('\nBeginning forward selection:')
    best_accuracy, best_set = forward_search(dataset, num_features)
    algorithm = 'Forward Selection'

# Backward Elimination
elif sel == '2':
    print('\nBeginning backward elimination:')
    best_accuracy, best_set = backward_search(dataset, num_features)
    algorithm = 'Backward Elimination'

else:
    print('\nBeginning Erin\'s Special Algorithm:')
    best_accuracy, best_set = secret_sauce(dataset, num_features)
    algorithm = 'Erin\'s Special Algorithm'

print('\nFinished ' + algorithm + '! For ' + file_loc + ' the best feature subset is ' + str(best_set) + ' with accuracy {:.1%}'.format(best_accuracy))
print('\nTime to run algorithm: %s seconds' % (time.time() - start_time)) 
