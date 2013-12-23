__author__ = 'sulantha'
from FileUtil.WellTableTemplateBuilder import WellTableTemplateBuilder
from DBUtil.PageTableAccesor import PageTableAccessor

pageTableAccesor = PageTableAccessor()
newWellIDs = [x[0] for x in pageTableAccesor.getNewWells()]

for wellID in newWellIDs:
    tableTemplateBuilder = WellTableTemplateBuilder(wellID)
    tableTemplateBuilder.buildTableTemplates()