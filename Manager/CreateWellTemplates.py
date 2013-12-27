__author__ = 'sulantha'
from FileUtil.WellTableTemplateBuilder import WellTableTemplateBuilder
from DBUtil.PageTableAccesor import PageTableAccessor

pageTableAccessor = PageTableAccessor()
newWellIDs = [x[0] for x in pageTableAccessor.getNewWells()]

for wellID in newWellIDs:
    tableTemplateBuilder = WellTableTemplateBuilder(wellID)
    tableTemplateBuilder.buildTableTemplates()