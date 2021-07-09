import os

def makeDir():
    # Create a directory
    # Returns the path to the created directory

    parentDir = os.getcwd()
    directory = 'newDir'
    mode = 0o666
    path = os.path.join(parentDir, directory)

    os.mkdir(path, mode)

    return path