"""calculates_results_stats.py
                                                                            
PROGRAMMER: Mike Anderson
DATE CREATED: 2022-06-22
REVISED DATE: 2022-06-22
PURPOSE: Create a function calculates_results_stats that calculates the
         statistics of the results of the programrun using the classifier's model
         architecture to classify the images. This function will use the
         results in the results dictionary to calculate these statistics.
         This function will then put the results statistics in a dictionary
         (results_stats_dic) that's created and returned by this function.
         This will allow the user of the program to determine the 'best'
         model for classifying the images. The statistics that are calculated
         will be counts and percentages. Please see "Intro to Python - Project
         classifying Images - xx Calculating Results" for details on the
         how to calculate the counts and percentages for this function.
        This function inputs:
           -The results dictionary as results_dic within calculates_results_stats
            function and results for the function call within main.
        This function creates and returns the Results Statistics Dictionary -
         results_stats_dic. This dictionary contains the results statistics
         (either a percentage or a count) where the key is the statistic's
          name (starting with 'pct' for percentage or 'n' for count) and value
         is the statistic's value.  This dictionary should contain the
         following keys:
           n_images - number of images
           n_dogs_img - number of dog images
           n_notdogs_img - number of NON-dog images
           n_match - number of matches between pet & classifier labels
           n_correct_dogs - number of correctly classified dog images
           n_correct_notdogs - number of correctly classified NON-dog images
           n_correct_breed - number of correctly classified dog breeds
           pct_match - percentage of correct matches
           pct_correct_dogs - percentage of correctly classified dogs
           pct_correct_breed - percentage of correctly classified dog breeds
           pct_correct_notdogs - percentage of correctly classified NON-dogs
"""

##
# TODO 5: Define calculates_results_stats function below, please be certain to replace None
#       in the return statement with the results_stats_dic dictionary that you create 
#       with this function
# 
def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model 
    architecture to classifying pet images. Then puts the results statistics in a 
    dictionary (results_stats_dic) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images. Note that 
    the statistics calculated as the results are either percentages or counts.
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                    a percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value. See comments above
                     and the classroom Item XX Calculating Results for details
                     on how to calculate the counts and statistics.
    
    z: Number of Images
        length of results_dic
    a: Number of Correct Dog matches
        Both labels are of dogs: results_dic[key][3] = 1 and results_dic[key][4] = 1
    b: Number of Dog Images
        Pet Label is a dog: results_dic[key][3] = 1
    c: Number of Correct (NOT SPECIES) Non-Dog matches
        Both labels are NOT of dogs: results_dic[key][3] = 0 and results_dic[key][4] = 0
    t: Number of correct species matches of non-dogs
        results_dic[key][2] = 1, results_dic[key][3] = 0
    d: Number of Not Dog Images
        number images - number dog images --OR--
        Pet Label is NOT a dog: results_dic[key][3] = 0
    e: Number of Correct Breed matches
        Pet Label is a dog & Labels match: results_dic[key][3] = 1 and results_dic[key][2] = 1
    y: Number of label matches
        Labels match: results_dic[key][2] = 1


    """
    results_stats_dic = {}
    z = len(results_dic)
    a, b, c, d, e, t, y = 0, 0, 0, 0, 0, 0, 0
    for entry in results_dic.values():
        if entry[3]:
            # label is a dog
            b += 1
            if entry[4]:
                # both labels are of dogs
                a += 1
            if entry[2]:
                # correct breed match
                e += 1
                # label matches classifier
                y += 1
        else:
            # label is not a dog
            d += 1
            if not entry[4]:
                # classifier and label agree non-dog
                c += 1
            if entry[2]:
                # non-dog correct species
                t += 1
                # label matches classifier
                y += 1
        # if entry[3] and entry[4]:
        #     # correct dog
        #     a += 1
        # elif entry[2] and not entry[3]:
        #     # correct non-dog
        #     c += 1
        # if entry[3]:
        #     # label is a dog
        #     b += 1
        # else:
        #     # label is not a dog
        #     d += 1
        # if entry[2] and entry[3]:
        #     # correct breed match
        #     e += 1
        # if entry[2]:
        #     # labels match
        #     y += 1
    
    results_stats_dic.update({'n_images': z})
    results_stats_dic.update({'n_dogs_img': b})
    results_stats_dic.update({'n_notdogs_img': d})
    results_stats_dic.update({'pct_correct_notdogs': c/d*100})
    results_stats_dic.update({'pct_id_other_species': t/d*100})
    results_stats_dic.update({'n_correct_dogs': a})
    results_stats_dic.update({'pct_correct_dogs': a/b*100})
    results_stats_dic.update({'n_correct_breed': e})
    results_stats_dic.update({'pct_correct_breed': e/b*100})
    results_stats_dic.update({'n_label_match': y})
    results_stats_dic.update({'pct_label_match': y/z*100})

    return results_stats_dic


if __name__ == '__main__':

    import json

    res_data = {}
    with open('test_results.json', 'r') as file:
        # sample data I captured
        res_data = json.load(file)
    print(calculates_results_stats(res_data))
