import os
import re
import errno
from glob import glob
from importStringFormatter import cutimportString
from ClassModel import ClassModel


def get_subdirectories(testModule):
    # if checkIfClassExistInDir(testModule):
        testModule = os.path.normpath(testModule)
        print testModule
        filename = create_index_file(os.path.normpath(testModule))
        with open(filename, "w+") as f:
            directory_ts_contant = glob(testModule + '/*.ts')

            for fileName in directory_ts_contant:
                with open(fileName, 'r')as file:
                    a = file.read()

                    className = re.search('class\s(.*?)\s', a) or re.search('interface\s(.*?)\s', a)

                    if className:
                        fileName = cutimportString(fileName, testModule)
                        classObject = ClassModel(className.group(1), fileName)
                        importString = classObject.genrateImport()
                        f.write(importString)
                        f.write('\n')


            directory_folder_contant = glob(testModule+'/*/')

            for file_path in directory_folder_contant:
                # if glob(file_path+'index.ts'):
                #     print glob(file_path+'index.ts')
                    formated_file_path = cutimportString(file_path,testModule)

                    #### check if directory contain index file and just then create parenetal index and make export

                    classObject = ClassModel('', formated_file_path)
                    importDirectoryString = classObject.genrateImportForDirectory()
                    f.write(importDirectoryString)
                    f.write('\n')
                    get_subdirectories(file_path)


def create_index_file(baseDir):
    filename = baseDir+ "/index.ts"
    # print filename
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    return filename

def checkIfClassExistInDir(dir_path):
    isExist = False

    directory_ts_contant = glob(dir_path + '/*.ts')
    for file_path in directory_ts_contant:
        with open(file_path, 'r')as file:
            a = file.read()
            className = re.search('class\s(.*?)\s', a) or re.search('interface\s(.*?)\s', a)
            if className:
                isExist = True
                return True

    directory_folder_contant = glob(dir_path + '/*/')
    for file_path in directory_folder_contant:
        if not isExist:
            checkIfClassExistInDir(file_path)

get_subdirectories('/Users/alex/tooling-spa/frontend/src/main/tooling-spa/src/app/shared')
