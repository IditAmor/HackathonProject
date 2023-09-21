import InputFunctions
import Dict

existing_cities_of_associations = []


def find_associations_by_city():
    city = InputFunctions.user_city()
    for field in InputFunctions.user_interest_list:
        print(field, ':')
        for association in Dict.associations[field]:
            association_name = association[0]
            association_contact_details = association[1]
            association_cities = association[2]
            if city in association_cities:
                existing_cities_of_associations.append(association_name)
                print(association_name, association_contact_details)
        if len(existing_cities_of_associations) == 0:
            print("לא נמצאה עמותה בעיר זו לפי תחום ההתנדבות זה.")
