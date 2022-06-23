"""
Configure argparse to collect command line params.

PROGRAMMER: Mike Anderson
DATE CREATED: 2022-06-22
REVISED DATE: 2022-06-23
PURPOSE: Create a function that retrieves 3 command line inputs
         from the user using the argparse module. If the user fails to
         provide some or all of the 3 inputs, then the default values are
         used for the missing inputs. Command Line Arguments:
    1. Image Folder as --dir with default value 'pet_images'
    2. CNN Model Architecture as --arch with default value 'vgg'
    3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
"""

# Imports python modules
import argparse


def get_input_args():
    """
    Configure argparse for relevant parameters.

    Command Line Arguments:
        1. Image Folder as --dir with default value 'pet_images'
        2. CNN Model Architecture as --arch with default value 'vgg'
        3. File with Dog Names as --dogfile default value 'dognames.txt'
    This function returns these arguments as an ArgumentParser object.
    Parameters:
        None
    Returns:
        parse_args() - command line arguments object
    """
    parser = argparse.ArgumentParser(description='Run doggie recognition.')
    parser.add_argument('--dir', type=str, default='pet_images/',
                        help='image directory', required=False)
    parser.add_argument('--arch', type=str, default='vgg',
                        choices=['vgg', 'resnet', 'alexnet'],
                        help='CNN model architecture',
                        required=False)
    parser.add_argument('--dogfile', type=str, default='dognames.txt',
                        help='dognames file', required=False)

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    """module testing"""
    args = get_input_args()
    print(f'dir: {args.dir} {type(args.dir)}')
