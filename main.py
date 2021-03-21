import file_worker as file
import csv_manipulator as manipulator


if __name__ == '__main__':
    data = file.read_csv('transactions.csv')
    data = manipulator.filter_data(data, 'CandidateOrCommittee == "COH"')
    data['ReportFiledDate'] = [(lambda x: manipulator.convert_from_datetime_to_unix(x))(x)
                               for x in data['ReportFiledDate']]
    print('To unix completed')
    data['PeriodBegining'] = [(lambda x: manipulator.convert_from_datetime_unix_iso(x))(x)
                              for x in data['PeriodBegining']]
    data['PeriodEnding'] = [(lambda x: manipulator.convert_from_datetime_unix_iso(x))(x)
                            for x in data['PeriodEnding']]
    print('To ISO completed')
    data = manipulator.concat_fields(data, 'CandidateFullName', 'CandidateFirstName', 'CandidateLastName')
    data = manipulator.add_new_columns(data, ['TransactionID', 'TransactionType', 'TransactionAmount'])
    file.save_csv(data)
