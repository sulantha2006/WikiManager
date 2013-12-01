__author__ = 'sulantha'

import Config.ManagerPageTableConfig as mPTConfig
from DBUtil.PageTableUpdater import PageTableUpdater

pageTableUpdater = PageTableUpdater()
for entity in mPTConfig.entityList:
    pageTableUpdater.updateEntity(entity,
                                  mPTConfig.entityTableDictionary[entity],
                                  mPTConfig.entityColumnDictionary[entity])

