from FileUtil.SourceBuilders import WellSourceBuilder, WellTableTemplateBuilder

__author__ = 'sulantha'
from DBUtil.PageTableAccesor import PageTableAccessor
from DBUtil.PageTableUpdater import PageTableUpdater

newIds = PageTableAccessor.getNewIds()

for entity in newIds:
    if entity == 'wells':
        for wellID in newIds[entity]:
            tableTemplateBuilder = WellTableTemplateBuilder(wellID)
            tableTemplateBuilder.buildTableTemplates()
            sourceBuilder = WellSourceBuilder(wellID)
            sourceBuilder.buildMainSource()
            PageTableUpdater.setUpdateSuccess(wellID)
    elif entity == 'county':
        pass
    elif entity == 'municipality':
        pass
    elif entity == 'operator':
        pass