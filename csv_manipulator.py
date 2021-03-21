import error_writter as logger
import time
from datetime import datetime


def filter_data(data, csv_filter):
    data.query(csv_filter, inplace=True)
    print('Data filtered')
    return data


def convert_from_datetime_to_unix(date):
    try:
        datetime_obj = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
        return time.mktime(datetime_obj.timetuple())
    except (ValueError, TypeError):
        logger.log_error('Date error with date {}'.format(date))
        return date


def convert_from_date_to_iso(date):
    try:
        date_obj = datetime.strptime(date, '%m/%d/%Y')
        return date_obj.isoformat()
    except (ValueError, TypeError):
        logger.log_error('Date error with date {}'.format(date))
        return date


def add_new_columns(data, *args):
    for arg in args:
        data[arg] = ''
    print('Columns added')
    return data


def concat_fields(data, new_field, first, second):
    try:
        data[new_field] = data[first] + data[second]
    except (ValueError, TypeError):
        pass
    print('Fields concated ')
    return data
