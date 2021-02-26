from typing import List, Optional
import cdsapi
from dotenv import load_dotenv
import logging


logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


load_dotenv()


def get_year(id):
    year = id.split('_')[4][:4]

    return year


def get_month(id):
    month = id.split('_')[4][4:6]

    return month


def get_day(id):
    day = id.split('_')[4][6:8]

    return day


def get_hour(id):
    hour = id.split('_')[4][9:11]
    hour_formatted = f"{hour}:00"

    return hour_formatted


def wind_speed(id: str, bbox: List, sink_path: Optional[str]) -> str:
    """
    Get wind speed and direction from Sentinel 1 ID
    """
    left, bottom, right, top = bbox
    year = get_year(id)
    month = get_month(id)
    day = get_day(id)
    hour = get_hour(id)

    if not sink_path:
        sink_path = f'{id}.nc'

    log.info(f"{id}")
    log.info(f"{year}, {month}, {day}, {hour}, {left}, {bottom}, {right}, {top}")

    client = cdsapi.Client()

    result = client.retrieve(
        'reanalysis-era5-single-levels',
        {
            'product_type': 'reanalysis',
            'format': 'netcdf',
            'variable': [
                '10m_u_component_of_wind', '10m_v_component_of_wind',
            ],
            'year': [
                year
            ],
            'month': [
                month
            ],
            'day': [
                day
            ],
            'time': [
                hour
            ],
            'area': [
                top, left, bottom, right
            ],
        },
    f'{sink_path}')

    log.info(sink_path)

    return sink_path
