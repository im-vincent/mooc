import os


def rename_files():
    file_list = os.listdir("prank")
    os.chdir("prank")

    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))

rename_files()
