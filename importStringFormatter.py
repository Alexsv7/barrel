import os


def cutimportString(importString,testModule):
    nestingCount = importString.count('/') - testModule.count('/')
    # print nestingCount
    # print importString.rsplit('/',nestingCount)
    # print os.path.split(testModule)[1]
    rel = os.path.relpath(importString, testModule)

    print importString
    print testModule
    print './'+rel

    return './'+rel