from contextlib import redirect_stderr
import io
import pandas as pd
import error_writter as logger


def read_csv(file):
    io_obj = io.StringIO()
    with redirect_stderr(io_obj):
        try:
            data = pd.read_csv(file, error_bad_lines=False, warn_bad_lines=True)
            print('file red')
        except OSError:
            print("File error")
    if io_obj.getvalue():
        logger.log_error("Problem with line: {}".format(io_obj.getvalue()))
    return data


def save_csv(data):
    try:
        data.to_csv('output.csv')
        print('File saved as output.csv')
    except OSError:
        print("File error")
