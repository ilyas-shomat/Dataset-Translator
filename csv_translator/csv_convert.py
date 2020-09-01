

def make_list_from_data_frame(data_frame):

    data_list = []
    number_list = data_frame['number']
    review_list = data_frame['review']
    review_type_list = data_frame['review_type']

    for row in range(0, len(number_list)):
        row_data = {'Num':number_list[row],'Review':review_list[row], 'Review_type':review_type_list[row]}
        data_list.append(row_data)

    return  data_list