"""
UDACITY AIPND PROJECT.

PROGRAMMER/STUDENT: Mike Anderson
DATE CREATED: 2022-06-22
REVISED DATE: 2022-06-23
PURPOSE: Classifies pet images using a pretrained CNN model, compares these
         classifications to the true identity of the pets in the images, and
         summarizes how well the CNN performed on the image
         classification task.
         Note that the true identity of the pet (or object) in the image is
         indicated by the filename of the image. Therefore, your program must
         first extract the pet image label from the filename before
         classifying the images using the pretrained CNN model. With this
         program we will be comparing the performance of 3 different CNN model
         architectures to determine which provides the 'best' classification.

Use argparse Expected Call with <> indicating expected user input:
    python check_images.py --dir <directory with images> --arch <model>
            --dogfile <file that contains dognames>
  Example call:
    python check_images_solution.py --dir pet_images/ --arch vgg
        --dogfile dognames.txt
"""

# Imports python modules
from time import time, sleep, strftime

# Imports print functions that check the lab
from print_functions_for_lab_checks import *

# Imports functions created for this program
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results
from timeit import default_timer as timer


def main():
    """Run classification, recognition and create stats."""
    start_time = time()
    start_timeit = timer()

    # command line parser
    in_arg = get_input_args()
    check_command_line_arguments(in_arg)

    # Create labels based on file names
    results_dic = get_pet_labels(in_arg.dir)
    check_creating_pet_image_labels(results_dic)

    # Run classication
    classify_images(in_arg.dir, results_dic, in_arg.arch)
    check_classifying_images(results_dic)

    # Update dict with additional flags for is/is not dog
    adjust_results4_isadog(results_dic, in_arg.dogfile)
    check_classifying_labels_as_dogs(results_dic)

    # Create stats dictionary
    results_stats = calculates_results_stats(results_dic)
    check_calculating_results(results_dic, results_stats)

    # Output some stats and results to console
    print_results(results_dic, results_stats, in_arg.arch, True, True)

    end_timeit = timer()
    end_time = time()

    tot_time = end_time - start_time

    print(f'\n** Total Elapsed Runtime: {int((tot_time/3600)):02d}' +
          f':{int((tot_time%3600)/60):02d}:{int((tot_time%3600)%60):02d}')

    print(f'** Or, if you are not running on a potato: ' +
          f'{end_timeit - start_timeit:.3f}s\n')


# Call to main function to run the program
if __name__ == "__main__":
    main()
