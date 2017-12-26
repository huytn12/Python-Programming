import os


def rename_files():
    #(1) get file names from a folder
    list_files = os.listdir(r"/Users/aquarius121989/Downloads/prank")

    # Change directory to correct one
    saved_path = os.getcwd()
    print("The current working directory is: " + saved_path)


    os.chdir(r"/Users/aquarius121989/Downloads/prank")

    #(2)for each file, rename filename
    for filename in list_files:
        #print the old and new file name
        print("Old name: " +filename,)
        print("New name: " + filename[2:])
        os.rename(filename,filename[2:])
        #os.chdir(saved_path)


rename_files()