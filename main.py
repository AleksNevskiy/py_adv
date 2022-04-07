import application.salary as sal
import application.people as pp
from datetime import date

if __name__ == '__main__':
    print(date.today())
    sal.calculate_salary()
    pp.get_employees()
