import datetime


class Flight:
    DATEFORMAT = "%Y-%m-%d"

    def book_outward_journey(self, begin_date: datetime.datetime):
        print("Outbound flight booked for {}".format(
            begin_date.strftime(self.DATEFORMAT)))

    def book_return_journey(self, end_date: datetime.datetime):
        print("Return flight booked for {}".format(
            end_date.strftime(self.DATEFORMAT)))
