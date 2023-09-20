user_interest_list = []
field_of_volunteering = ["אוכלוסיות חלשות", "בעלי מוגבלות", "אנשים חולים", "קשישים", "בעלי חיים"]


def user_interest():
    user_input = input("רשום את התחום בו תרצה להתנדב מהרשימה הבאה: "
                       "בעלי חיים, קשישים, אנשים חולים, בעלי מוגבלות ואוכלוסיות חלשות. \n אם סיימת הכנס 'סוף' : ")
    while user_input != "סוף":
        if user_input not in field_of_volunteering:
            print("תחום ההתנדבות חייב להיות "
                  "בעלי חיים, קשישים, אנשים חולים, בעלי מוגבלות ואוכלוסיות חלשות")
            user_input = input("הכנס תחום התנדבות חדש: ")
        else:
            user_interest_list.append(user_input)
            user_input = input(" הכנס תחום התנדבות נוסף או 'סוף' :")


def user_city():
    user_input = input("באיזה עיר אתה רוצה להתנדב? ")
    return user_input

# from ip2geotools.databases.noncommercial import DbIpCity
# import socket
# hostname = socket.gethostname()
# ip = socket.gethostbyname(hostname)
# res = DbIpCity.get(ip, api_key="free")
# print(f"Location: {res.city}, {res.region}, {res.country}")ר שאתה מצא בה או בעיר אחרת? (ענה כן או לא)")
