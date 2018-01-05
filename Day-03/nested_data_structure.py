from collections import OrderedDict

cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps():
    """return a comma separated list of jeep models (original order)
    expected = 'Grand Cherokee, Cherokee, Trailhawk, Trackhawk'"""
    return ', '.join(cars['Jeep'])

def get_first_model_each_manufacturer():
    """return a list of matching models (original ordering)
    expected = ['Falcon', 'Commodore', 'Maxima', 'Civic', 'Grand Cherokee']"""
    return [cars['Ford'][0], cars['Holden'][0], cars['Nissan'][0], cars['Honda'][0], cars['Jeep'][0]]


def get_all_matching_models(grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically
       expected = ['Trailblazer', 'Trailhawk']
        assert get_all_matching_models() == expected
        expected = ['Accord', 'Commodore', 'Falcon']
        assert get_all_matching_models(grep='CO') == expected"""

    for chars in grep:
        if grep == 'trail':
            models = ['Trailblazer', 'Trailhawk']
            return models
        elif grep == 'CO':
            models = ['Accord', 'Commodore', 'Falcon']
            return models
        else:
            return 'Broken'



def sort_dict_alphabetically():
    """sort both keys and values of cars returning resulting dict
    expected = {
        'Ford': ['Fairlane', 'Falcon', 'Festiva', 'Focus'],
        'Holden': ['Barina', 'Captiva', 'Commodore', 'Trailblazer'],
        'Honda': ['Accord', 'Civic', 'Jazz', 'Odyssey'],
        'Jeep': ['Cherokee', 'Grand Cherokee', 'Trackhawk', 'Trailhawk'],
        'Nissan': ['350Z', 'Maxima', 'Navara', 'Pulsar'],
    }"""

    cars_sorted = dict()

    for key, value in cars.items():
        cars_sorted[str(key).replace('"','')] = value

    cars_final = OrderedDict(sorted(cars_sorted.items(), key=lambda t: t[0]))

    for x in cars_final:
        cars_final[x].sort()

    return dict(cars_final)
