"""
Adjust the results dictionary.

PROGRAMMER: Mike Anderson
DATE CREATED: 2022-06-22
REVISED DATE: 2022-06-23
PURPOSE: Create a function adjust_results4_isadog that adjusts the results
         dictionary to indicate whether or not the pet image label is of-a-dog,
         and to indicate whether or not the classifier image label is of-a-dog.
         All dog labels from both the pet images and the classifier function
         will be found in the dognames.txt file. We recommend reading all the
         dog names in dognames.txt into a dictionary where the 'key' is the
         dog name (from dognames.txt) and the 'value' is one. If a label is
         found to exist within this dictionary of dog names then the label
         is of-a-dog, otherwise the label isn't of a dog. Alternatively one
         could also read all the dog names into a list and then if the label
         is found to exist within this list - the label is of-a-dog, otherwise
         the label isn't of a dog.
        This function inputs:
           -The results dictionary as results_dic within adjust_results4_isadog
            function and results for the function call within main.
           -The text file with dog names as dogfile within
            adjust_results4_isadog
            function and in_arg.dogfile for the function call within main.
          This function uses the extend function to add items to the list
          that's the 'value' of the results dictionary. You will be adding the
          whether or not the pet image label is of-a-dog as the item at index
          3 of the list and whether or not the classifier label is of-a-dog as
          the item at index 4 of the list. Note we recommend setting the values
          at indices 3 & 4 to 1 when the label is of-a-dog and to 0 when the
          label isn't a dog.
"""


def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjust the results disctionary.

    Adjusts the results dictionary to determine if classifier correctly
    classified images 'as a dog' or 'not a dog' especially when not a match.
    Demonstrates if model architecture correctly classifies dog images even if
    it gets dog breed wrong (not a match).
    Parameters:
      results_dic - Dictionary with 'key' as image filename and 'value' as a
                    List. Where the list will contain the following items:
                  index 0 = pet image label (string)
                  index 1 = classifier label (string)
                  index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifer labels and 0 = no match between labels
                ------ where index 3 & index 4 are added by this function -----
                 NEW - index 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and
                            0 = pet Image 'is-NOT-a' dog.
                 NEW - index 4 = 1/0 (int)  where 1 = Classifier classifies
                 image
                            'as-a' dog and 0 = Classifier classifies image
                            'as-NOT-a' dog.
     dogfile - A text file that contains names of all dogs from the classifier
               function and dog names from the pet image files. This file has
               one dog name per line dog names are all in lowercase with
               spaces separating the distinct words of the dog name. Dog names
               from the classifier function can be a string of dog names
               separated
               by commas when a particular breed of dog has multiple dog names
               associated with that breed (ex. maltese dog, maltese terrier,
               maltese) (string - indicates text file's filename)
    Returns:
           None - results_dic is mutable data type so no return needed.
    """
    with open(dogfile, 'r') as file:
        dog_list = file.readlines()
    dog_list = list(map(lambda dog: dog.rstrip('\n'), dog_list))

    for value in results_dic.values():
        image_match = False
        class_match = False
        for dog in dog_list:
            if image_match is False and dog == value[0]:
                # image label seems to be in dog list
                value.insert(3, 1)
                image_match = True
            if class_match is False and dog == value[1]:
                # classification appears to be in dog list
                value.insert(4, 1)
                class_match = True
            if image_match is True and class_match is True:
                # both were matched, can move on
                break
        if not image_match:
            # image label was not in dog list
            value.insert(3, 0)
        if not class_match:
            # classification was not in dog list
            value.insert(4, 0)


if __name__ == '__main__':
    results_dic = {'Basenji_00963.jpg': ['basenji', 'basenji', 1],
                   'Basenji_00974.jpg': ['basenji', 'basenji', 1],
                   'Basset_hound_01034.jpg':
                   ['basset hound', 'basset, basset hound', 1],
                   'fox_squirrel_01.jpg':
                   ['fox squirrel',
                    'fox squirrel, eastern fox squirrel, sciurus niger', 1],
                   'gecko_80.jpg':
                   ['gecko',
                    'tailed frog, bell toad, ribbed toad, tailed toad,' +
                    ' ascaphus trui', 0]
                   }
    adjust_results4_isadog(results_dic, 'dognames.txt')
    print(f'results dic: {results_dic}')
