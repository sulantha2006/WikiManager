__author__ = 'sulantha'

import Config.ManagerPageTableConfig as mPTConfig
from DBUtil.PageTableUpdater import PageTableUpdater

for entity in mPTConfig.entityList:
    PageTableUpdater.updateEntity(entity,
                                  mPTConfig.entityTableDictionary[entity],
                                  mPTConfig.entityColumnDictionary[entity])

