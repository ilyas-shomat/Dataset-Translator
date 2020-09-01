import csv

def make_list_from_data_frame(data_frame):

    data_list = []
    number_list = data_frame['number']
    review_list = data_frame['review']
    review_type_list = data_frame['review_type']

    for row in range(0, len(number_list)):
        row_data = {'number':number_list[row],'review':review_list[row], 'review_type':review_type_list[row]}
        data_list.append(row_data)

    return data_list


def make_csv_from_list(data_set, csv_name):

    with open(csv_name, 'w', newline='') as csvfile:
        headers = ['Num', 'Review', 'Review_type']
        csv_writer = csv.DictWriter(csvfile, fieldnames=headers)

        csv_writer.writeheader()
        for data in data_set:
            csv_writer.writerow({'Num':data['number'],'Review':data['review'], 'Review_type':data['review_type']})


def get_review_list_from_data_list(list):

    review_list = []

    for row in list:
        review = row["review"]
        review_list.append(review)

    return review_list


def create_new_data_list_from_translated_list(translated_list, not_translated_list):

    data_list = []

    for index in range(0, len(translated_list)):
        current_row = not_translated_list[index]
        current_row["review"] = translated_list[index]
        data_list.append(current_row)

    return data_list