import os
from glob import glob
import re
import errno
from importStringFormatter import cutimportString
from ClassModel import ClassModel


def get_subdirectories(testModule):
    filename = create_index_file(testModule)

    with open(filename, "w+") as f:
        # print directory_ts_contant
        directory_ts_contant = glob(testModule+'/*.ts')

        for fileName in directory_ts_contant:
            with open (fileName, 'r')as file:
                a = file.read()
                # className =  re.search('export class[\s]([\s]+)', a)

                className =  re.search('class\s(.*?)\s', a) or re.search('interface\s(.*?)\s', a)
                # print className\s

                if className:
                    fileName = cutimportString(fileName, testModule)
                    classObject = ClassModel(className.group(1),fileName)
                    importString =  classObject.genrateImport()
                    f.write(importString)
                    f.write('\n')

        directory_folder_contant = glob(testModule+'/*/')

        for fileName in directory_folder_contant:
            # fileName = cutimportString(fileName,testModule)

            classObject = ClassModel('', fileName)
            importDirectoryString = classObject.genrateImportForDirectory()
            f.write(importDirectoryString)
            f.write('\n')
            get_subdirectories(fileName)


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


get_subdirectories('/Users/alex/tooling-spa/frontend/src/main/tooling-spa/src/app/shared')
