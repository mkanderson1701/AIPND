"""
Print results to console.

PROGRAMMER: Mike Anderson
DATE CREATED: 2022-06-22
REVISED DATE: 2022-06-23
PURPOSE: Create a function print_results that prints the results statistics
    from the results statistics dictionary (results_stats_dic). It
    should also allow the user to be able to find cases of misclassified
    dogs and cases of misclassified breeds of dog using the Results
    dictionary (results_dic).
    This function inputs:
    -The results dictionary as results_dic within print_results
    function and results for the function call within main.
    -The results statistics dictionary as results_stats_dic within
    print_results function and results_stats for the function call within main.
    -The CNN model architecture as model wihtin print_results function
    and in_arg.arch for the function call within main.
    -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
    print_results function and set as either boolean value True or
    False in the function call within main (defaults to False)
    -Prints Incorrectly Classified Breeds as print_incorrect_breed within
    print_results function and set as either boolean value True or
    False in the function call within main (defaults to False)
    This function does not output anything other than printing a summary
    of the final results.
"""


def print_results(results_dic, results_stats_dic, model,
                  print_incorrect_dogs=False, print_incorrect_breed=False):
    """
    Print summary results on the classification.

    Prints incorrectly classified dogs and incorrectly classified dog breeds
    if user indicates they want those printouts (using non-default values.)

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
    results_stats_dic - Dictionary that contains the results statistics
        (a percentage or a count) where the key is the statistic's
        name (starting with 'pct' for percentage or 'n' for count)
        and the value is the statistic's value
    model - Indicates which CNN model architecture will be used by the
        classifier function to classify the pet images,
        values must be either: resnet alexnet vgg (string)
    print_incorrect_dogs - True prints incorrectly classified dog images and
        False doesn't print anything(default) (bool)
    print_incorrect_breed - True prints incorrectly classified dog breeds and
        False doesn't print anything(default) (bool)
    Returns:
           None - simply printing results.
    """
    print('\nSUMMARY RESULTS\n')
    print(f'---\nCNN architecture in use: {model}\n---\n')

    print('IMAGE COUNTS\n------------')
    print(f"Number of Images: {results_stats_dic['n_images']:2d}\n" +
          f"Number of dog images: {results_stats_dic['n_dogs_img']:2d}\n" +
          f"Number not-dog images: {results_stats_dic['n_notdogs_img']:2d}\n" +
          "\nPERCENTAGES\n-----------\n"
          "Percentage of dog pictures classified correctly as a dog: " +
          f"{results_stats_dic['pct_correct_dogs']:5.1f}%\n" +
          "Percentage of dog pictures with correctly identified breed: " +
          f"{results_stats_dic['pct_correct_breed']:5.1f}%\n" +
          "Percentage of non-dogs correct classified: " +
          f"{results_stats_dic['pct_correct_notdogs']:5.1f}%\n" +
          "Percentage of correct classifications, all pictures: " +
          f"{results_stats_dic['pct_label_match']:5.1f}%")

    if (print_incorrect_dogs and
        results_stats_dic['n_correct_dogs']
        + results_stats_dic['n_correct_notdogs']
            != results_stats_dic['n_images']):
        print('\nMISIDENTIFIED DOGS')
        print('------------------')
        print(f'{"LABEL":<30}CLASSIFIER')
        for result in results_dic.values():
            if sum(result[3:]) == 1:
                print(f'{result[0]:<30}{result[1]}')

    if (print_incorrect_breed and
        results_stats_dic['n_correct_dogs']
            != results_stats_dic['n_correct_breed']):
        print('\nMISCLASSIFIED BREEDS')
        print('------------------')
        print(f'{"LABEL":<30}CLASSIFIER')
        for result in results_dic.values():
            if sum(result[3:]) == 2 and result[2] == 0:
                print(f'{result[0]:<30}{result[1]}')
