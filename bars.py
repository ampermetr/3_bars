import json


def load_data(filepath):
    with open(filepath, 'r') as file:    
        data = json.load(file)
    return data


def get_biggest_bar(data):
    maximum_seats = float('-Inf')
    maximum_seats_name = []
    for item in data:
        if item["Cells"]["SeatsCount"] > maximum_seats:
            maximum_seats = item["Cells"]["SeatsCount"]
            maximum_seats_name = []
            maximum_seats_name.append (item["Cells"]["Name"])
        elif item["Cells"]["SeatsCount"] == maximum_seats:
            maximum_seats_name.append (item["Cells"]["Name"])
    return maximum_seats_name


def get_smallest_bar(data):
    minimal_seats = float('Inf')
    minimal_seats_name = []
    for item in data:
        if item["Cells"]["SeatsCount"] < minimal_seats:
            minimal_seats = item["Cells"]["SeatsCount"]
            minimal_seats_name = []
            minimal_seats_name.append (item["Cells"]["Name"])
        elif item["Cells"]["SeatsCount"] == minimal_seats:
            minimal_seats_name.append (item["Cells"]["Name"])
    return minimal_seats_name


def get_closest_bar(data, longitude, latitude):
    minimal_dist = float('Inf')
    minimal_dist_name = []
    for item in data:
        distance = ((item['Cells']['geoData']['coordinates'][0] - longitude)** 2 + (item['Cells']['geoData']['coordinates'][0] - latitude)** 2) ** 0.5
        if distance < minimal_dist:
            minimal_dist = distance        
            minimal_dist_name = []
            minimal_dist_name.append (item["Cells"]["Name"])
        elif distance == minimal_dist:        
            minimal_dist_name.append (item["Cells"]["Name"])
    return minimal_dist_name


if __name__ == '__main__':
    try:
        longitude = float(input('Введите широту' + '\n'))
    except ValueError:
        longitude = None
    if longitude is None:
        print ('Данные не верны')
        exit()
    try:
        latitude = float(input('Введите долготу' + '\n'))
    except ValueError:
        latitude = None
    if latitude is None:
        print ('Данные не верны')
        exit()
    filepath = input('Введите путь к файлу' + '\n')
    data = load_data(filepath)
    print (get_biggest_bar(data))
    print (get_smallest_bar(data))
    print (get_closest_bar(data, longitude, latitude))
    
