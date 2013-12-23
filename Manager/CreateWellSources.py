__author__ = 'sulantha'
from DBUtil.PageTableAccesor import PageTableAccessor
from FileUtil.WellSourceBuilder import WellSourceBuilder

pageTableAccesor = PageTableAccessor()
newWellIDs = [x[0] for x in pageTableAccesor.getNewWells()]

for wellID in newWellIDs:
    sourceBuilder = WellSourceBuilder(wellID)
    sourceBuilder.buildMainSource()
