import os
from os.path import exists


def system_file_explorer_browsing():
    all_steps = []
    folder_location = "C:/"
    command = str(input(folder_location + "> "))
    new_command = ""
    while command != "stop":
        if "cd " in command:
            new_command = command.replace("cd ", "")
            folder_location += new_command
            if not exists(folder_location):
                folder_location = folder_location.replace(new_command, "")
                print("The system cannot find the path specified.")
            else:
                folder_location += command.replace(str(command), "") + "/"
                all_steps.append(folder_location)
        elif "cd.." in command:
            if len(all_steps) <= 1:
                folder_location = "C:/"
            else:
                all_steps.pop(-1)
                folder_location = all_steps[-1]

        elif "mkdir" in command:
            new_command = command.replace("mkdir ", "")
            make_a_dir(folder_location, new_command)

        command = str(input(folder_location + "> "))

    return folder_location, new_command


def make_a_dir(folder_location, new_command):
    folder_location = folder_location
    new_folder = new_command
    path = os.path.join(folder_location, new_folder)
    print(path)
    os.mkdir(path)


system_file_explorer_browsing()











































'''Dont Mind That'''
# import codecs
# from tkinter import filedialog as fd
# from os import listdir


# def content_html():
#     location = str(input("Give an existing location (Computer): "))
#
#     file = codecs.open(location, "r", "utf-8")
#
#     all_lines = file.readlines()
#     for line in all_lines:
#         print(line)
#
#
# def create_file():
#     dir = fd.askdirectory()
#     folder_content = listdir(dir)
#     for file in folder_content:
#         print(file)


# def run_functions():
#     command = str(input("Give A Command: "))
#     while command != "stop":
#         if command == "p":
#             print(3.14)
#         command = str(input("Give A Command: "))
