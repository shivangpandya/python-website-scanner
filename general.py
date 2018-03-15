import os

#Functionn to write directory
def create_dir(directory):

    if not os.path.exists(directory):

        os.makedirs(directory)


#Funtion to write path and data
def write_path(path,data):
        f = open(path ,"w")
        f.write(data)
        f.close()


