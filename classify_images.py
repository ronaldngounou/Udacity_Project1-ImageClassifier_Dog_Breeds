#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:                                 
# REVISED DATE: 
# PURPOSE: Create a function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images and function 
#             and as in_arg.dir for function call within main. 
#            -The results dictionary as results_dic within classify_images 
#             function and results for the functin call within main.
#            -The CNN model architecture as model wihtin classify_images function
#             and in_arg.arch for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           classifier label as the item at index 1 of the list and the comparison 
#           of the pet and classifier labels as the item at index 2 of the list.
#
##
# Imports classifier function for using CNN to classify images 
from classifier import classifier 

# TODO 3: Define classify_images function below, specifically replace the None
#       below by the function definition of the classify_images function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 
def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with classifier function, compares pet labels to 
    the classifier labels, and adds the classifier label and the comparison of 
    the labels to the results dictionary using the extend function. Be sure to
    format the classifier labels so that they will match your pet image labels.
    The format will include putting the classifier labels in all lower case 
    letters and strip the leading and trailing whitespace characters from them.
    For example, the Classifier function returns = 'Maltese dog, Maltese terrier, Maltese' 
    so the classifier label = 'maltese dog, maltese terrier, maltese'.
    Recall that dog names from the classifier function can be a string of dog 
    names separated by commas when a particular breed of dog has multiple dog 
    names associated with that breed. For example, you will find pet images of
    a 'dalmatian'(pet label) and it will match to the classifier label 
    'dalmatian, coach dog, carriage dog' if the classifier function correctly 
    classified the pet images of dalmatians.
     PLEASE NOTE: This function uses the classifier() function defined in 
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
    
    # 1) Concatenate the images_dir with the filename to represent the full path to each pet image file
    fullpath =""
    for filename in results_dic:
        fullpath = images_dir + filename
        #print(fullpath) 
    # 2)Compare pet image labels to the classifier labels
    # pet images label are returned in as the value of the result_dic
    #The only processing to do in the classifier label is to put all the letters in lower case and to strip whitespace characters
        classifier_label = classifier(fullpath, model)
        classifier_label = (classifier_label.strip()).lower()

        if results_dic[filename][0] in classifier_label: #in returns True when a string exists within another string
            #The extend method doesn't return anything
            results_dic[filename].extend([classifier_label, 1]) #second index
        else: 
            results_dic[filename].extend([classifier_label, 0])
                         
    # Next step: Code Index 3&4
    # To begin with this task, I have coded this:
    
        #with open('/home/workspace/dognames.txt', 'r') as dognames_file:
        #    lines = dognames_file.readlines()
        #    list_dogs = [line.lower().strip("\n") for line in lines]
            #list_dogs = []
            #for line in lines:
            #    print("print line:",line)
            #    low_line = line.lower()
            #    print("lowline",low_line)
            #    word_dognames = low_line.strip("\n")
            #    print("word dog", word_dognames )
            #    list_dogs += [word_dognames]
            
                     
        #if results_dic[filename][0] in list_dogs:
        #    results_dic[filename].insert(2, 1) #the third index 1 if the image is a dog.
        #else:
        #    results_dic[filename].insert(2, 0)
        
        #if results_dic[filename][1] in list_dogs:
        #   results_dic[filename].insert(3, 1) #the fourth index 1 if the classifier label is a dog.
        #else:
        #   results_dic[filename].insert(3, 0)

    #print("final dictionary:", results_dic)
    # Iterates through the list to print the results for each filename
    #print("\nFilename=", filename, "\npet_image Label=", results_dic[filename][0],
    #      "\nClassifier Label=", results_dic[filename][1], "\nmatch=",
    #      results_dic[filename][2], "\nImage is dog=", results_dic[filename][3],
    #      "\nClassifier is dog=", results_dic[filename][4])                        
          
    #for filename in results_dic:
    #    if sum(results_dic[filename][2:] ) == 3:
    #          print("*Breed Match*")
    #    if sum(results_dic[filename][3:] ) == 2:
    #          print("*Is-a-Dog Match*")
    #    if sum(results_dic[filename][3:] ) == 0 and results_dic[filename][2] == 1:
    #          print("*NOT-a-Dog Match*")
    None # None because dictionaries are mutable data type