__author__ = 'sulantha'


wellDataDBTables = dict(inspection='compliance',
                        production='production',
                        waste='waste')

wellDataDBTableIDs = dict(compliance='WELL_API_COUNTY_ID',
                          production='WELL_API_COUNTY_ID',
                          waste='WELL_API_COUNTY_ID',
                          permit='WELL_API_COUNTY_ID',
                          unconventional='WELL_API_COUNTY_ID',
                          well_complete='WELL_API_COUNTY_ID')

wellDataSelectedColumnsFromTables = dict(compliance='INSP_ID, INSPECTION_DATE, INSP_CATEGORY, INSPECTION_RESULT_DESC, INSP_COMMENT, VIOLATION_ID',
                                         production='PERIOD_ID, GAS_QUANTITY_MCF, GAS_PRODUCTION_DAYS, CONDENSATE_QUANTITY_BBL, CONDENSATE_PRODUCTION_DAYS, OIL_QUANTITY_BBL, OIL_PRODUCTION_DAYS',
                                         waste='PERIOD_ID, WASTE_TYPE, WASTE_QUANTITY, UNITS, DISPOSAL_METHOD, WASTE_FACILITY_PERMIT_ID, WASTE_FACILITY_NAME, FACILITY_ADDRESS_1, FACILITY_ADDRESS_2, FACILITY_CITY, FACILITY_STATE, FACILITY_ZIP_CODE, FACILITY_PHONE, FACILITY_LATITUDE, FACILITY_LONGITUDE')

wellDataProperColumnNames = dict(inspection=['INSPECTION ID', 'DATE', 'CATEGORY', 'DESCRIPTION', 'COMMENT', 'VIOLATION ID'],
                                 production=['PERIOD', 'GAS QUANTITY', 'GAS PRODUCTION DAYS', 'CONDENSATE QUANTITY', 'CONDENSATE PRODUCTION DAYS', 'OIL QUANTITY', 'OIL PRODUCTION DAYS'],
                                 waste=['PERIOD', 'TYPE', 'QUANTITY', 'UNITS', 'DISPOSAL METHOD', 'WASTE FACILITY PERMIT ID', 'WASTE FACILITY NAME', 'FACILITY ADDRESS 1', 'FACILITY ADDRESS 2', 'FACILITY CITY', 'FACILITY STATE', 'FACILITY ZIP', 'FACILITY PHONE', 'FACILITY LATITUDE', 'FACILITY LONGITUDE'])

wellDataSelectiveSortingEnabled = False
wellDataSortableColumns = dict(inspection=['DATE'],
                               production=['PERIOD', 'GAS QUANTITY', 'GAS PRODUCTION DAYS', 'CONDENSATE QUANTITY', 'CONDENSATE PRODUCTION DAYS', 'OIL QUANTITY', 'OIL PRODUCTION DAYS'],
                               waste=['PERIOD', 'QUANTITY'])

wellDataProperFinalTableTopics = dict(inspection='Inspection Data',
                                      production='Production Data',
                                      waste='Waste Data')

wellDetailsTables = ['permit', 'unconventional', 'well_complete']
wellDetailsTablesSelectionColumns = dict(permit='OPERATOR_NAME, OPERATOR_OGO',
                                         unconventional='WELL_COUNTY, WELL_MUNICIPALITY, FARM_NAME, WELL_STATUS',
                                         well_complete='FIRST_PERMIT_ISSUED_DATE, LAST_PERMIT_ISSUED_DATE, SPUD_DATE, UNCONVENTIONAL, HORIZONTAL_WELL, VIOLATION_COUNT, LATITUDE_DECIMAL, LONGITUDE_DECIMAL')
wellDetailsDataProperColumnNames = dict(OPERATOR_NAME='Operator Name',
                                        OPERATOR_OGO='Operator Number',
                                        WELL_COUNTY='County',
                                        WELL_MUNICIPALITY='Municipality',
                                        FARM_NAME='Farm/Lease Name',
                                        WELL_STATUS='Producing',
                                        FIRST_PERMIT_ISSUED_DATE='First Permit Date',
                                        LAST_PERMIT_ISSUED_DATE='Last Permit Date',
                                        SPUD_DATE='Spud Date',
                                        UNCONVENTIONAL='Unconventional',
                                        HORIZONTAL_WELL='Horizontal',
                                        VIOLATION_COUNT='Violations',
                                        LATITUDE_DECIMAL='Latitude',
                                        LONGITUDE_DECIMAL='Longitude')