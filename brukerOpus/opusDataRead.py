'''A simple script to read the OPUS format files and convert them into CSV files.
Created by: Daniel Luoma, Tampere University'''

import os
import sys
from brukeropusreader import read_file


def readFile(fileName):
    # Returns a list of the ScSm (=Single channel Sample) readings from the OPUS file
    opusFile = read_file(fileName)

    return opusFile['ScSm']

def prepareFile(fileName, path):
    savePath = path + '\\' + fileName +  '.csv'

    wrtFile = open(savePath, 'w')
    wrtFile.write('sep=,\n')

    return wrtFile

def prepareSpectrum():
    spJump = 1.92882 # the distance between consecutive datapoints in the spectrum [98.36984 ... 9997.07576]
    spMin = 98.36984
    spMax = 9997.07576

    spectrum = []

    while spMin < spMax:
        spectrum.append(spMin)
        spMin += spJump

    return spectrum

def writeFile(opusFile, wrtFile):
    spectrum = prepareSpectrum()

    for i in range(len(opusFile)):
        wrtFile.write(str(spectrum[i]) + ',' + str(opusFile[i]) + '\n')

    wrtFile.close()
    return


def makeDir():
    # Create a directory in order to ease the data handling after translation
    # Returns the path to the created directory

    parentDir = os.getcwd()
    directory = 'translatedData'
    mode = 0o666
    path = os.path.join(parentDir, directory)

    os.mkdir(path, mode)

    return path

def main():

    path = makeDir()

    for fileName in os.listdir(os.getcwd()):
        if fileName not in ['opusDataRead.py', 'translatedData']:
            opusFile = readFile(fileName)
            wrtFile = prepareFile(fileName, path)
            writeFile(opusFile, wrtFile)

    return

if __name__ == '__main__':
    main()