import datetime

from car_rental import CarRental
from flight import Flight
from hotel import Hotel

class VacationFacade():
    def book(self, begin_date: datetime.datetime, end_date: datetime.datetime):
        flight = Flight()
        flight.book_outward_journey(begin_date)
        flight.book_return_journey(end_date)

        hotel = Hotel()
        hotel.book(begin_date, end_date)

        car_rental = CarRental()
        car_rental.book(begin_date, end_date)
