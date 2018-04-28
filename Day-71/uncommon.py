my_cities = ['Rome', 'Paris', 'Madrid', 'Chicago', 'Seville', 'Berlin']
other_cities = ['Paris', 'Boston', 'Sydney', 'Madrid', 'Moscow', 'Lima']


def uncommon_cities(my_cities, other_cities):
    """Compare my_cities and other_cities and return the number of different
       cities between the two"""

    return print(len(set(my_cities)^set(other_cities)))


if __name__ == '__main__':
    uncommon_cities(my_cities, other_cities)