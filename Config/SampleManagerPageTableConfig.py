__author__ = 'sulantha'

entityList = ['wells', 'county', 'municipality', 'operator']
entityTableDictionary = dict(wells='well_complete',
                             county='county',
                             municipality='municipality',
                             operator='operator')
entityColumnDictionary = dict(wells='WELL_API_COUNTY_ID',
                              county='county_name',
                              municipality='municipality_name',
                              operator='operator_name')

managerPageTableName = 'wikiManagerPages'
managerPageTableColumns = dict(pageTitle='PAGE_NAME',
                               typeColumn='TYPE',
                               needsUpdate='NEEDS_UPDATE')