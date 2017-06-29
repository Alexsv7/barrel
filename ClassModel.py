from importStringFormatter import cutimportString
class ClassModel:
    name = ''
    path = 'a';

    def __init__(self, name, path):
        self.name = name
        self.path = path

    def genrateImport(self):
        importString = 'export {'+ self.name + '} from \'' + self.path + '\';'
        return importString.replace(".ts","")

    def genrateImportForDirectory(self):
        importString = 'export * from \'' + self.path + '\';'
        # print importString
        return importString
