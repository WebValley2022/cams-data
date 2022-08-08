import cdsapi

from settings import *

c = cdsapi.Client(
    url=API_URL,
    key=API_KEY
)

variables = [
    # 'carbon_monoxide', 
    'nitrogen_dioxide', 
    # 'ozone',
    'particulate_matter_10um', 
    # 'particulate_matter_2.5um', 
    # 'sulphur_dioxide',
]

year = 2022

c.retrieve(
    'cams-europe-air-quality-forecasts',
    {
        'variable': variables,
        'model': 'ensemble',
        'level': '0',
        'date': f'{year}-01-01/{year}-06-30',
        'type': 'forecast',
        'time': '00:00',
        'leadtime_hour': [
            '72', '73', '74',
            '75', '76', '77',
            '78', '79', '80',
            '81', '82', '83',
            '84', '85', '86',
            '87', '88', '89',
            '90', '91', '92',
            '93', '94', '95',
            '96',
        ],
        'area': [
            46.63, 10.42, 45.65,
            12.14,
        ],
        'format': 'netcdf',
    },
    '2022.nc'
)

