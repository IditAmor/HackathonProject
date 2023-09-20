user_interest_list = []
field_of_volunteering = ["אוכלוסיות חלשות", "בעלי מוגבלות", "אנשים חולים", "קשישים", "בעלי חיים"]


def user_interest():
    print("רשום את התחום בו תרצה להתנדב מהרשימה הבאה: "
          "בעלי חיים, קשישים, אנשים חולים, בעלי מוגבלות ואוכלוסיות חלשות")
    print("אם סיימת תכתוב סוף")
    user_input = input()
    while user_input != "סוף":
        if user_input not in field_of_volunteering:
            print("תחום ההתנדבות חייב להיות "
                  "בעלי חיים, קשישים, אנשים חולים, בעלי מוגבלות ואוכלוסיות חלשות")
            user_input = input()
        else:
            user_interest_list.append(user_input)
            user_input = input()
    print(user_interest_list)


def user_city():
    print("באיזה עיר אתה רוצה להתנדב?")
    user_input = input()
    return user_input


# from ip2geotools.databases.noncommercial import DbIpCity
# import socket
# hostname = socket.gethostname()
# ip = socket.gethostbyname(hostname)
# res = DbIpCity.get(ip, api_key="free")
# print(f"Location: {res.city}, {res.region}, {res.country}")ר שאתה מצא בה או בעיר אחרת? (ענה כן או לא)")