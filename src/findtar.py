#!/usr/bin/python 
import commands

# this script executes a find command based upon user input, then allows the
# user to select a number of files returned by said find command and archive them
# using tar.

# File name: findtar.py
# Authors: Scott Greenberg, Devon Shumaker
# Date created: 9/19/2016
# Date last modified: 9/26/2016
# Python Version: 2.7

# define functions
# gets a selection of items from array (including ranges)
# e.g. '1,2,5-10,15'


# selection: the comma separated (or single) collection of numbers inputted by the user
# this represents the choices of files the user wants to be archived via tar

# array: this represents the previously retrieved results from our find command (see lines 64-103)
def select_from_array(array, selection):

    # init
    # prints if selection isn't valid
    error_message = 'Selection must consist of numbers, \',\' and \'-\' only.'
    # string of space separated selections returned at end of function
    return_string = ''

    # splits selection string on commas
    comma_split = selection.split(",")

    # main parsing algorithm for selection
    for i in comma_split:
        # splits hyphenated ranges and selects from find_array by range
        if '-' in i:
            hyphen_split = i.split('-')
            # subtract by 1 to account for 0-indexing
            for j in range(int(hyphen_split[0]), int(hyphen_split[1])+1):
                try:
                    return_string += array[int(j)]
                    return_string += " "
                # we want to ignore range errors, since this will have no impact on the user's selection
                except IndexError:
                    pass

        # todo: add error handling for cases where no numbers are found

        # adds single integer selections from array
        elif i != ',' or i != ' ':
            try:
                # test to make sure char can be converted to an int
                int(i)
                # if index is out of range do nothing
                try:
                    return_string += array[int(i)]
                    return_string += " "

                except IndexError:
                    pass
            # if char can't be converted to int do nothing
            except ValueError:
                pass
        else:
            print error_message

    return return_string


if __name__ == '__main__':
    # loop for find command
    find_out_array = []
    while True:

        # input from user
        # prompt_options = raw_input('Enter option(s) in "-***" format:')
        # prompt_test = raw_input('Enter test(s) in "-***" format:')
        # prompt_expression = raw_input('Enter search expression:')
        # prompt_path = raw_input('Enter search path:')


        # main find command
        # find_comm = 'find %s %s %s %s' %(prompt_options,prompt_path,prompt_test,prompt_expression)

        # TEST QUERY/PRINT
        find_comm = 'find / -name "f.txt*"'
        print "***" + find_comm + "***"

        # stores output of find command as array
        find_out_array = commands.getstatusoutput(find_comm)[1].split('\n')
        # make this less redundant
        pruned_array = []

        # loops through results array and prints remaining files by index

        # if permission is not denied
        increment = 0
        # keeps track of labeling files that aren't permission denied
        label_inc = 1

        for i in find_out_array:
            if 'Permission denied' in i:
                # todo: find out why this del line doesn't work!
                del find_out_array[increment]
            else:
                print str(label_inc) + ' ' + i
                label_inc += 1
                pruned_array.append(i)
            increment += 1
        break

    #print pruned_array

    # loop for tar command
    while True:

        # todo: Error handling for all of these needs to be added
        # user input for selection of files to be archived
        selection = raw_input('Enter numbers of files to be archived:')
        # user input for compression archive to use
        comp_util = raw_input('Enter compression utility:\n[j] bzip2\n[J] xz\n[z] gzip\n')
        # user input for naming archive to be created
        archive_name = raw_input('Enter name of archive to be created\n')

        # tar command string
        tar_comm = "tar cf" + comp_util + " " + archive_name + " "

        # parse input for errors and add selection of files to tar command
        if selection.upper() == 'ALL':
            # cast to str because our select_from_array function expects a string, not an int
            tar_comm += select_from_array(find_out_array, str(len(find_out_array)))
        else:
            tar_comm += select_from_array(find_out_array, selection)

        # PRINT TEST
        print tar_comm
        # execute tar command
        commands.getstatusoutput(tar_comm)
        break
