import re
import sys
import os.path

class XML_Parser(object):
    """Pare xml benchmark file. You can use:
    benchmarkMap - dictionary is structure {benchmark_name:iterations}
    """
    def __init__(self, filename):
        self.path = filename
        self.__readFile()
        self.getBenchmark()

    def __readFile(self):
        try:
            os.path.exists(self.path)
        except Exception: 
            pass
        else:
            self.fileLineList = open(self.path).readlines()
            startTag = re.compile('<BenchmarksToRun>')
            endTag = re.compile('<\/BenchmarksToRun>')

            for item in self.fileLineList:
                if startTag.match(item):
                    self.firstBenchItem = self.fileLineList.index(item) + 1
                elif endTag.match(item):
                    self.lastBenchItem = self.fileLineList.index(item) - 1

    def __getValue(self, str, searchMap):
        
        nameTag = re.compile(searchMap[0])
        iterTag = re.compile(searchMap[1])

        for item in str.split():
            if nameTag.match(item):
                name = item.replace('name=\"','').replace('\"','')
            if iterTag.match(item):
                iteration = item.replace('iterations=\"','').strip('\"\/>')

        return {name:iteration}

    def getBenchmark(self):
        self.benchmarksMap = dict()
        for i in range(self.firstBenchItem, self.lastBenchItem + 1):
            self.benchmarksMap.update(self.__getValue(self.fileLineList[i], ("name", "iterations")))

    def addBenchmark(self, nameMap):
        self.benchmarksMap.update(nameMap)

    def writeFile(self):
        FO = open(self.path, "w")
        FO.writelines('<?xml version="1.0" encoding="utf-8" ?>\n')
        FO.writelines('<BenchmarksToRun>\n')
        for name in sorted(self.benchmarksMap.keys()):
            FO.writelines('\t\t<Benchmark name=\"%s\" iterations=\"%s\"/>\n' % (name, self.benchmarksMap[name]))
        FO.writelines('</BenchmarksToRun>')
        FO.close()