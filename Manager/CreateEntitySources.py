__author__ = 'sulantha'
from DBUtil.PageTableAccesor import PageTableAccessor
from DBUtil.PageTableUpdater import PageTableUpdater
from FileUtil.SourceBuilders import WellSourceBuilder
from FileUtil.SourceBuilders import WellTableTemplateBuilder
from FileUtil.SourceBuilders import MunicipalitySourceBuilder
from FileUtil.SourceBuilders import MunicipalityTableTemplateBuilder
from FileUtil.SourceBuilders import CountySourceBuilder
from FileUtil.SourceBuilders import CountyTableTemplateBuilder

newIds = PageTableAccessor.getNewIds()

for entity in newIds:
    if entity == 'wells':
        for wellID in newIds[entity]:
            tableTemplateBuilder = WellTableTemplateBuilder.WellTableTemplateBuilder(wellID)
            tableTemplateBuilder.buildTableTemplates()
            sourceBuilder = WellSourceBuilder.WellSourceBuilder(wellID)
            sourceBuilder.buildMainSource()
            PageTableUpdater.setUpdateSuccess(wellID)
    elif entity == 'county':
        for conID in newIds[entity]:
            tableTemplateBuilder = CountyTableTemplateBuilder.CountyTableTemplateBuilder(conID)
            tableTemplateBuilder.buildTableTemplates()
            sourceBuilder = CountySourceBuilder.CountySourceBuilder(conID)
            sourceBuilder.buildMainSource()
            PageTableUpdater.setUpdateSuccess(conID)
    elif entity == 'municipality':
        for munID in newIds[entity]:
            tableTemplateBuilder = MunicipalityTableTemplateBuilder.MunicipalityTableTemplateBuilder(munID)
            tableTemplateBuilder.buildTableTemplates()
            sourceBuilder = MunicipalitySourceBuilder.MunicipalitySourceBuilder(munID)
            sourceBuilder.buildMainSource()
            PageTableUpdater.setUpdateSuccess(munID)
    elif entity == 'operator':
        pass