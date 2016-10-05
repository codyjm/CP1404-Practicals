"""
For testing taxi.py
"""
from Prac08.taxi import Taxi, UnreliableCar


def main():
    # test Taxi class
    test_taxi = Taxi("Prius 1", 100)
    print(test_taxi)

    # drive 40km, print details, current fare
    test_taxi.drive(40)
    print("{} : Price: ${}".format(test_taxi, test_taxi.get_fare()))

    # restart meter, drive 100
    test_taxi.start_fare()
    test_taxi.drive(100)
    print("{} : Price: ${}\n".format(test_taxi, test_taxi.get_fare()))

    # test UnreliableCar class
    test_unrel = UnreliableCar("UnrelCar", 100, 60)
    print("{} : Reliability: {}".format(test_unrel, test_unrel.reliability))
    test_unrel.drive(40)
    print("{} : Reliability: {}".format(test_unrel, test_unrel.reliability))

main()
