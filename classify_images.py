"""
Classify images from given dir and populate results_dic.

PROGRAMMER: Mike Anderson
DATE CREATED: 2022-06-22
REVISED DATE: 2022-06-23
PURPOSE: Create a function classify_images that uses the classifier function
    to create the classifier labels and then compares the classifier
    labels to the pet image labels. This function inputs:
    -The Image Folder as image_dir within classify_images and function
    and as in_arg.dir for function call within main.
    -The results dictionary as results_dic within classify_images
    function and results for the functin call within main.
    -The CNN model architecture as model within classify_images function
    and in_arg.arch for the function call within main.
    This function uses the extend function to add items to the list
    that's the 'value' of the results dictionary. You will be adding the
    classifier label as the item at idx 1 of the list and the comparison
    of the pet and classifier labels as the item at index 2 of the list.
"""

# Imports classifier function for using CNN to classify images
from classifier import classifier


def classify_images(images_dir, results_dic, model):
    """
    Create classifier labels with classifier function.

    compares pet labels to
    the classifier labels, and adds the classifier label and the comparison of
    the labels to the results dictionary using the extend function. Be sure to
    format the classifier labels so that they will match your pet image labels.
    The format will include putting the classifier labels in all lower case
    letters and strip the leading and trailing whitespace characters from them.
    For example, the Classifier function returns
    'Maltese dog, Maltese terrier, Maltese'
    so the classifier label = 'maltese dog, maltese terrier, maltese'.
    Recall that dog names from the classifier function can be a string of dog
    names separated by commas when a particular breed of dog has multiple dog
    names associated with that breed. For example, you will find pet images of
    a 'dalmatian'(pet label) and it will match to the classifier label
    'dalmatian, coach dog, carriage dog' if the classifier function correctly
    classified the pet images of dalmatians.
    NOTE: This function uses the classifier() function defined in
    classifier.py within this function. The proper use of this function is
    in test_classifier.py Please refer to this program prior to using the
    classifier() function to classify images within this function
    Parameters:
    images_dir - The (full) path to the folder of images that are to be
                classified by the classifier function (string)
    results_dic - Results Dictionary with 'key' as image filename and 'value'
                as a List. Where the list will contain the following items:
                index 0 = pet image label (string)
                --- where index 1 & index 2 are added by this function ---
                NEW - index 1 = classifier label (string)
                NEW - index 2 = 1/0 (int)  where 1 = match between pet image
                and classifer labels and 0 = no match between labels
    model - Indicates which CNN model architecture will be used by the
            classifier function to classify the pet images,
            values must be either: resnet alexnet vgg (string)
    Returns:
        None - results_dic is mutable data type so no return needed.
    """
    for key, value in results_dic.items():
        path = images_dir + key
        # added strip() for potential whitespace
        img_class = classifier(path, model).lower().strip()
        value.insert(1, img_class)
        if img_class.find(value[0]) > -1:
            value.insert(2, 1)
        else:
            value.insert(2, 0)


if __name__ == '__main__':
    results_dic = {'Basenji_00963.jpg': ['basenji'],
                   'Basenji_00974.jpg': ['basenji'],
                   'Basset_hound_01034.jpg': ['basset hound']
                   }

    classify_images('pet_images/', results_dic, 'vgg')
    print(results_dic)
