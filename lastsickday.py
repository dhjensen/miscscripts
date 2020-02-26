from datetime import date
from datetime import timedelta

def add_days_to_date(year: int, month: int, day: int, days_to_add: int) -> date:
    try: 
        start_date = date(year = year, month = month, day = day)
        days_to_add_delta = timedelta(days = days_to_add)
        final_date = start_date + days_to_add_delta
    except ValueError as e:
        print('ValueError: ', str(e))
        final_date = None

    return final_date

def main():
    
    # My first sick day was 7-10-2019 and 120 day rule states that my employee can fire me with one month notice after 120 days
    # But I also had 2 sick days earlier in 2019 so I should set the start date to 5-10-2019 to compensate.
    last_sick_day = add_days_to_date(day = 5, month = 10, year = 2019, days_to_add = 120)
    try:
        print ('Last sick day based on 120 day rule: ', last_sick_day.strftime("%d/%m/%Y"))
    except AttributeError as e:
        print('Couldnt print date: ', str(e))
    
    # First day they can fire me also based on the 120 day rule
    first_fire_day = add_days_to_date(day = 5, month = 10, year = 2019, days_to_add = 121)
    try:
        print ('First day they can fire me based on 120 day rule: ', first_fire_day.strftime("%d/%m/%Y"))
    except AttributeError as e:
        print('Couldnt print date: ', str(e))
    
    # Doctor sick leave was created on 25-11-2019 and lasts 6 weeks
    six_weeks_in_days = 6*7
    last_doctor_sick_leave = add_days_to_date(day = 25, month = 11, year = 2019, days_to_add = six_weeks_in_days)
    try:
        print ('Last doctor sick leave day: ', last_doctor_sick_leave.strftime("%d/%m/%Y"))
    except AttributeError as e:
        print('Couldnt print date: ', str(e))
    
    # Time before we have to return info to foreign ministry. Letter 18-12-2019. 3 weeks deadline
    # before it will effect their casehandling time.
    tree_weeks_in_days = 3*7
    last_day_respond_to_foreign_ministy = add_days_to_date(day = 18, month = 12, year = 2019, days_to_add = tree_weeks_in_days)
    try:
        print ('Last day to respond to foreign ministry: ', last_day_respond_to_foreign_ministy.strftime("%d/%m/%Y"))
    except AttributeError as e:
        print('Couldnt print date: ', str(e))
        
    # Time before we have to return info to foreign ministry. Letter 21-02-2020. 3 weeks deadline
    # The bank have to take action on granting financial security.
    last_day_respond_to_foreign_ministy_for_economic_security = add_days_to_date(day = 21, month = 2, year = 2020, days_to_add = tree_weeks_in_days)
    try:
        print ('Last day to respond to foreign ministry for financial security: ', last_day_respond_to_foreign_ministy_for_economic_security.strftime("%d/%m/%Y"))
    except AttributeError as e:
        print('Couldnt print date: ', str(e))

if __name__ == "__main__":
    main()
