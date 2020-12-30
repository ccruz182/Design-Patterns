import datetime


class CarRental:
    DATEFORMAT = "%Y-%m-%d"

    def book(self, begin_date: datetime.datetime, end_date: datetime.datetime):
        print("Booking car for {} to {}".format(begin_date.strftime(
            self.DATEFORMAT), end_date.strftime(self.DATEFORMAT)))
