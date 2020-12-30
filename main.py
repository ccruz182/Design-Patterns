import datetime

from vacation_facade import VacationFacade

begin_date = datetime.datetime(2021, 2, 1)
end_date = datetime.datetime(2021, 2, 18)

vacation = VacationFacade()
vacation.book(begin_date, end_date)
