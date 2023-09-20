import InputFunctions
import Dict


def find_associations_by_city():
    for field in InputFunctions.user_interest_list:
        for association in Dict.associations[field].get():
            association_name = association[0]
            association_contact_details = association[1]
            association_cities = association[2]
            if InputFunctions.user_city() in association_cities:
                return association_name, association_contact_details
            else:
                return "No Results"
