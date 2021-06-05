import os
from flask import Flask, render_template

import os
import mysql.connector
import EditProfileQueries
import CreateSlackUserQueries


from flask import Flask, request, render_template, redirect, url_for
from dotenv import load_dotenv



app = Flask(__name__)
load_dotenv()


host = os.getenv("HOST")
user = os.getenv("USER")
password = os.getenv("PASSWORD")
database = os.getenv("DATABASE")

mydb = mysql.connector.connect(
  host = host,
  user = user,
  password = password,
  database = database
)

app = Flask(__name__)

@app.route("/UserDetailsForActiveUser/<user_name>")
def UserDetailsForActiveUser(user_name):

    cursor = mydb.cursor()
    sql = CreateSlackUserQueries.UserDetailsForActiveUser
    
    UserName = user_name

    val = (UserName, )
    cursor.execute(sql, val)
    dataList = cursor.fetchall()

    print (dataList)
    data = dataList[0]
    print(data)

    name = data[0]
    print(name)

    my_email= data[1]
    print(my_email)

    retype_email=data[2]
    print(retype_email)

    education=data[3]
    print(education) 

    from_=data[4]
    print(from_)

    in_=data[5]
    print(in_) 

    My_Expected_compensation=data[6]
    print(My_Expected_compensation)

    Your_Linkedin_Profile=data[7]
    print(Your_Linkedin_Profile)

    github=data[8]
    print(github) 

    My_expertise_lies_in=data[9]
    print(My_expertise_lies_in) 

    My_Core_competencies=data[10]
    print(My_Core_competencies) 

    My_Work_Experience=data[11]
    print(My_Work_Experience) 

    My_Mobile_number=data[12]
    print(My_Mobile_number) 

    My_Current_Employer=data[13]
    print(My_Current_Employer) 

    Im_available_in=data[14]
    print(Im_available_in) 

    type_=data[15]
    print(type_) 

    stage=data[16]
    print(stage) 

    company=data[17]
    print(company) 

    CandidateStatus=data[18]
    print(CandidateStatus) 

    CandidateStatusActive=data[19]
    print(CandidateStatusActive)
        
    return render_template("activeCandidateEditProfile.html", 
                            name = name, 
                            my_email = my_email, 
                            Your_Linkedin_Profile = Your_Linkedin_Profile,
                            My_Mobile_number = My_Mobile_number,
                            My_expertise_lies_in = My_expertise_lies_in,
                            My_Core_competencies = My_Core_competencies,
                            My_Expected_compensation = My_Expected_compensation,
                            github = github,
                            My_Work_Experience = My_Work_Experience,
                            My_Current_Employer = My_Current_Employer )
    #return("values added to DB")


@app.route("/RecruiterDetailsForRecruiter/<email>")
def UserDetailsForUser(email):

    cursor = mydb.cursor()
    sql = CreateSlackUserQueries.RecruterDetails
    UserEmail = email
   

    val = (UserEmail, )
    cursor.execute(sql, val)
    RecruterDetailsList = cursor.fetchall()
    RecruterDetailsTuple = RecruterDetailsList[0]
    

    CompanyName=RecruterDetailsTuple[0]
    print(CompanyName) 

    ContactPerson=RecruterDetailsTuple[1]
    print(ContactPerson) 

    OfficialEmailID=RecruterDetailsTuple[2]
    print(OfficialEmailID) 

    Password=RecruterDetailsTuple[3]
    print(Password) 

    SlackID=RecruterDetailsTuple[4]
    print(SlackID) 

    ContactNumber=RecruterDetailsTuple[5]
    print(ContactNumber)

    return render_template("RecruterEditProfile.html", ContactPerson = ContactPerson, OfficialEmailID = OfficialEmailID, SlackID = SlackID, ContactNumber = ContactNumber)

@app.route("/RecruiterDetailsUpdate/<Contact_Person>,<Official_EmailID>,<Slack_ID>,<Contact_Number>",  methods=['GET', 'POST'])
def RecruiterDetailsUpdate(Contact_Person, Official_EmailID, Slack_ID, Contact_Number ):

     if request.method == 'POST':
    
        Contact_Person = request.form['Contact_Person']
        Official_EmailID = request.form['Official_EmailID']
        Slack_ID = request.form['Slack_ID']
        Contact_Number = request.form['Contact_Number']

        print (Contact_Person)
        print (Official_EmailID)
        print (Slack_ID)
        print (Contact_Number)

        mycursor = mydb.cursor()
        sql = EditProfileQueries.RECRUTER_EDIT_PROFILE_UPDATE
        val = (Contact_Person, Slack_ID, Contact_Number, Official_EmailID)
        mycursor.execute(sql, val)
        mydb.commit()

        return ('', 204)

@app.route("/CandidateDetailsUpdate/<name>,<my_email>,<Your_Linkedin_Profile>,<My_Mobile_number>,<My_expertise_lies_in>,<My_Core_competencies>,<My_Expected_compensation>,<github>,<My_Work_Experience>,<My_Current_Employer>",  methods=['GET', 'POST'])
def CandidateDetailsUpdate( name, my_email, Your_Linkedin_Profile, My_Mobile_number, My_expertise_lies_in, My_Core_competencies, My_Expected_compensation, github, My_Work_Experience, My_Current_Employer):

     if request.method == 'POST':
    
        name = request.form['name']
        my_email = request.form['my_email']
        Your_Linkedin_Profile = request.form['Your_Linkedin_Profile']
        My_Mobile_number = request.form['My_Mobile_number']
        My_expertise_lies_in = request.form['My_expertise_lies_in']
        My_Core_competencies = request.form['My_Core_competencies']
        My_Expected_compensation = request.form['My_Expected_compensation']
        github = request.form['github']
        My_Work_Experience = request.form['My_Work_Experience']
        My_Current_Employer = request.form['My_Current_Employer']

        print (name)
        print (my_email)
        print (Your_Linkedin_Profile)
        print (My_Mobile_number)
        print (My_expertise_lies_in)
        print (My_Core_competencies)
        print (My_Expected_compensation)
        print (github)
        print (My_Work_Experience)
        print (My_Current_Employer)

        mycursor = mydb.cursor()
        sql = EditProfileQueries.CANDIDATE_EDIT_PROFILE_UPDATE
        val = (name, Your_Linkedin_Profile, My_Mobile_number, My_expertise_lies_in, My_Core_competencies, My_Expected_compensation, github, My_Work_Experience, My_Current_Employer, my_email)
        mycursor.execute(sql, val)
        mydb.commit()

        
        return ('', 204)


if __name__ == "__main__":
    app.run(host='localhost', port=8001, debug=True)
    