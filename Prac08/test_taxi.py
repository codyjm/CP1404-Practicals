"""
For testing taxi.py
"""
from Prac08.taxi import Taxi


def main():
    test_taxi = Taxi("Prius 1", 100)
    print(test_taxi)

    # drive 40km, print details, current fare
    test_taxi.drive(40)
    print("{} : Price: ${}".format(test_taxi, test_taxi.get_fare()))

    # restart meter, drive 100
    test_taxi.start_fare()
    test_taxi.drive(100)
    print("{} : Price: ${}".format(test_taxi, test_taxi.get_fare()))

main()
