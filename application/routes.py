from flask import Flask, render_template, request, redirect, url_for, flash, session
from application import app, forms
from application import db_operations

@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    form = forms.LoginForm()
    if form.validate_on_submit():
        username = request.form.get("username")
        password = request.form.get("password")
        if db_operations.authenticate(username, password):
            pass
            # Decide what should be done after user logs in 
        else:
            flash("Invalid login credentials!! Please try again", category="danger")
    else:
        pass
        # Decide what happens when form validation fails
    return render_template("form.html", form=form, form_title="Login", action_path="/index")

@app.route("/create-patient", methods=["GET", "POST"])
def create_patient():
    form = forms.CreatePatientForm()
    if form.validate_on_submit():
        ssn = request.form.get("ssn")
        name = request.form.get("name")
        age = request.form.get("age")
        bed_type = request.form.get("bed_type")
        address = request.form.get("address")
        city = request.form.get("city")
        state = request.form.get("state")
        
        if db_operations.create_new_patient(ssn, name, age, bed_type, address, city, state):
            redirect("/create-patient")
            flash("New patient admitted!", category="success")
        else:
            flash("Operation failed!", category="danger")


    return render_template("form.html", form=form, form_title="Create Patient", action_path="/create-patient")


@app.route("/update-patient", methods=["GET", "POST"])
def update_patient():
    form_0 = forms.PatientIdForm()
    form = forms.UpdatePatientForm()

    if form_0.check.data and form_0.validate():
        patient_id = request.form.get("patient_id")
        session["previous patient id"] = patient_id
        if db_operations.validate_patient_id(patient_id):
            patient_details = db_operations.get_patient_details(patient_id)

            patient_name = patient_details[0]
            patient_age = patient_details[1]
            patient_admission_date = patient_details[2]
            patient_bed_type = patient_details[3]
            patient_address = patient_details[4]
            patinet_city = patient_details[5]
            patient_state = patient_details[6]
            
            form = forms.UpdatePatientForm()
            form.patient_id.default = patient_id
            form.patient_id.render_kw = {'readonly': 'True'}

            form.name.default = patient_name
            form.age.default = patient_age
            form.admission_date.default = patient_admission_date
            form.bed_type.default = patient_bed_type
            form.address.default = patient_address
            form.city.default = patinet_city
            form.state.default = patient_state
            form.process()

            return render_template("form.html", form_0=form_0, form=form, form_title="Update Patient", action_path="/update-patient")
        else:
            flash("Invalid Patient ID!", category="danger")

    if form and form.update.data:
        patient_id = request.form.get("patient_id")
        new_name = request.form.get("name")
        new_age = request.form.get("age")
        new_admission_date = request.form.get("admission_date")
        new_bed_type = request.form.get("bed_type")
        new_address = request.form.get("address")
        new_city = request.form.get("city")
        new_state = request.form.get("state")

        if db_operations.update_patient(patient_id, new_name, new_age, new_admission_date, new_bed_type,
                                new_address, new_city, new_state):
            flash("Patient Updated Successfully!", category="success")
        else:
            flash("Something went wrong while making changes to the database!", category="danger")

    return render_template("form.html", form_0=form_0, form=None, form_title="Update Patient", action_path="/update-patient")
