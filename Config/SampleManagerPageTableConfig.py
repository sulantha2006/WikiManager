__author__ = 'sulantha'

entityList = ['wells', 'county', 'municipality', 'operator']
entityTableDictionary = dict(wells='well_complete',
                             county='county',
                             municipality='municipality',
                             operator='operator')
entityColumnDictionary = dict(wells='WELL_API_COUNTY_ID',
                              county='county_name',
                              municipality='CONCAT(municipality_name_long, \', \', county_name, \', \', state_code)',
                              operator='operator_name')

managerPageTableName = 'wikiManagerPages'
managerPageTableColumns = dict(pageTitle='PAGE_NAME',
                               typeColumn='TYPE',
                               needsUpdate='NEEDS_UPDATE')