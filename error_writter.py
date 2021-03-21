def log_error(error):
    try:
        file_object = open('errors.log', 'a')
        file_object.write('{} \n'.format(error))
    except OSError:
        print("File error")
