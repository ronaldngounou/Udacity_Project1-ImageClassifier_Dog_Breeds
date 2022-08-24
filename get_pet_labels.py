#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Ronald NGOUNOU
# DATE CREATED: 07/08/2022                                  
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
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
    # 1) Retrieve the filenames from folder pet_images/
    # images_dir should be generic in other to work on any path
    images_dir = "/home/workspace/pet_images/"
    filenames = listdir(images_dir)
    
    # 2) Create empty dictionary named results_dic
    results_dic = dict()
    
    # 3) Create Pet Image Labels 
    for filename in filenames:
        pet_name = ""
        low_pet_image = filename.lower()
        word_list_pet_image = low_pet_image.split("_")
        for word in word_list_pet_image:
            if word.isalpha():
                pet_name += word + " "
        pet_name = pet_name.strip()
    #At this stage, names could exist twice in the string called pet_names
    # 4) Creation of a list pet_names containing unique values
    #Adding new-key value pairs to the dictionary ONLY when the key, filename doesn't already exist. 
        if filename not in results_dic:
            results_dic[filename] = [pet_name] #pet name is a list
        else:
            print("** Warning: Key=", filename, 
                "already exists in results_dic with value =", 
                results_dic[filename])
            
    # 5) Iterating through a dictionary printing all keys & associated values
    print("\n Printing all key-value pairs in dictionary results_dic:")
    for key in results_dic:
        print("Filename=", key, "   Pet Label=", results_dic[key][0])
    
    
    return(results_dic)
