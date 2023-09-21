user_interest_list = []
field_of_volunteering = ["אוכלוסיות חלשות", "בעלי מוגבלויות", "אנשים חולים", "קשישים", "בעלי חיים"]


def user_interest():
    user_input = input("רשום את התחום בו תרצה להתנדב מהרשימה הבאה: "
                       "בעלי חיים, קשישים, אנשים חולים, בעלי מוגבלויות ואוכלוסיות חלשות. \n אם סיימת הכנס 'סוף' :\n ")
    if user_input == 'סוף':
        user_input = input("לא הכנסת תחום התנדבות, אתה חייב להכניס תחום!\nהכנס תחום התנדבות מהרשימה הבאה: "
                       "בעלי חיים, קשישים, אנשים חולים, בעלי מוגבלויות ואוכלוסיות חלשות: \n")
    while user_input != "סוף":
        if user_input not in field_of_volunteering:
            print("תחום ההתנדבות חייב להיות "
                  "בעלי חיים, קשישים, אנשים חולים, בעלי מוגבלויות ואוכלוסיות חלשות")
            user_input = input("הכנס תחום התנדבות חדש: \n")
        else:
            user_interest_list.append(user_input)
            user_input = input(" הכנס תחום התנדבות נוסף או 'סוף' :\n")


def user_city():
    user_input = input("באיזה עיר אתה רוצה להתנדב?\n")
    return user_input
