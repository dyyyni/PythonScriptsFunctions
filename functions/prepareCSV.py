def prepareCSV(fileName, path):
    
    savePath = path + '\\' + fileName +  '.csv'

    wrtFile = open(savePath, 'w')
    wrtFile.write('sep=,\n')

    return wrtFile