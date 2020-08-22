import csv

# with open('../helpers/names.csv', 'w', newline='') as csvfile:
#     fieldnames = ['number', 'review','type']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
#     writer.writeheader()
#     writer.writerow({'number': '0', 'review': 'Beans', 'type': 'good'})
#     writer.writerow({'number': '1', 'review': 'Spam', 'type': 'good'})
#     writer.writerow({'number': '2', 'review': 'Spam', 'type': 'bad'})


def make_csv_from_list(data_set, csv_name):

    with open(csv_name, 'w', newline='') as csvfile:
        headers = ['Num', 'Review', 'Review_type']
        csv_writer = csv.DictWriter(csvfile, fieldnames=headers)

        csv_writer.writeheader()
        for data in data_set:
            csv_writer.writerow({'Num':data['Num'],'Review':data['Review'], 'Review_type':data['Review_type']})


def make_list_from_data_frame(data_frame):

    data_list = []
    number_list = data_frame['number']
    review_list = data_frame['review']
    review_type_list = data_frame['review_type']

    for row in range(0, len(number_list)):
        row_data = {'Num':number_list[row],'Review':review_list[row], 'Review_type':review_type_list[row]}
        data_list.append(row_data)

    return  data_list

