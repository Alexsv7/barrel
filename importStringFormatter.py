import os


def cutimportString(importString,testModule):
    nestingCount = importString.count('/') - testModule.count('/')

    rel = os.path.relpath(importString, testModule)

    # print importString
    # print testModule
    # print './'+rel

    return './'+rel