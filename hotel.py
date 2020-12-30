import datetime


class Hotel:
    DATEFORMAT = "%Y-%m-%d"

    def book(self, begin_date: datetime.datetime, end_date: datetime.datetime):
        print("Booking hotel room for {} to {}".format(begin_date.strftime(
            self.DATEFORMAT), end_date.strftime(self.DATEFORMAT)))
