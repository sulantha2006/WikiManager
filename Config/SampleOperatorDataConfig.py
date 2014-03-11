__author__ = 'sulantha'


operatorDataDBTables = dict(wells='')

operatorDataDBTableIDs = dict(operator='OPERATOR_NAME')


operatorDataSelectedColumnsFromTables = dict(wells='')
operatorDataProperColumnNames = dict(wells=['Well ID', 'County', 'Municipality', 'First Permit Date', 'Spud Date', 'Unconventional', 'Horizontal', 'Producing', 'Violations'])

operatorDataSelectiveSortingEnabled = False
operatorDataSortableColumns = dict(wells=['Well ID', 'County', 'Municipality', 'Operator Name', 'First Permit Date', 'Spud Date', 'Unconventional', 'Horizontal', 'Producing', 'Violations'])

operatorDataProperFinalTableTopics = dict(wells='Wells from this operator.')

operatorDetailsTables = ['operator']
operatorDetailsTablesSelectionColumns = dict(operator='OPERATOR_OGO, OPERATOR_NAME, OPERATOR_ADDRESS, OPERATOR_CITY, OPERATOR_STATE, OPERATOR_ZIP, UNCONVENTIONAL')
operatorDetailsDataProperColumnNames = dict(OPERATOR_NAME='Operator Name',
                                        OPERATOR_OGO='Operator Number',
                                        OPERATOR_ADDRESS='Address',
                                        OPERATOR_CITY='City',
                                        OPERATOR_STATE='State',
                                        OPERATOR_ZIP='Zip Code',
                                        UNCONVENTIONAL='Unconventional')