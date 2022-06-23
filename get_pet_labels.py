"""
Use filenames to generate image labels and start results_dic.

PROGRAMMER: Mike Anderson
DATE CREATED: 2022-06-22
REVISED DATE: 2022-06-23
PURPOSE: Create the function get_pet_labels that creates the pet labels from
         the image's filename. This function inputs:
          - The Image Folder as image_dir within get_pet_labels function and
            as in_arg.dir for the function call within the main function.
         This function creates and returns the results dictionary results_dic
         within get_pet_labels function and as results within main.
         The results_dic dictionary has a 'key' that's the image filename and
         a 'value' that's a list. This list will contain the following item
         at index 0 : pet image label (string).
"""

# Imports python modules
from os import listdir


def get_pet_labels(image_dir):
    """
    Create a dictionary of pet labels.

    Based upon the filenames
    of the image files. These pet image labels are used to check the accuracy
    of the labels that are returned by the classifier function, since the
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    results_dic = {}
    f_list = listdir(image_dir)
    for f_name in f_list:
        if f_name.startswith('.'):
            # skip hidden files
            continue
        f_split = f_name.split('_')
        f_split.pop()
        label = ' '.join(f_split).lower()
        if f_name not in results_dic:
            label_list = [label]
            results_dic.update({f_name: label_list})
        else:
            print(f'Warning: key {f_name} already exists in results_dic.')
    return results_dic


if __name__ == '__main__':
    print(get_pet_labels('pet_images/'))
