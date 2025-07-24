from datetime import datetime

def authenticate(username, password):
    # validate username and password
    # return True if valid and False otherwise
    return False

def create_new_patient(ssn, name, age, bed_type, address, city, state):
    # returns True if operation succeeds
    # and False otherwise
    return True

def validate_patient_id(patient_id):
    # If patient ID is present in database, return True
    # and False otherwise
    if patient_id == "1234":
        return True
    else:
        return False

def get_patient_details(patient_id):
    # return a list of patient details
    # like this:
    return ["name", 21, datetime.utcnow(), "sharing", "address", "city", "state"]
    # remove this ^ line 

def update_patient(patient_id, name, age, admission_date, bed_type, address, city, state):
    # update database row with given patient id to given values
    print(admission_date)
    # return True if everything goes well, and False otherwise
    return True