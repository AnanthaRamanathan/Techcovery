CREATE_USER = "INSERT INTO user_details(name, type_, stage, company, my_email, retype_email, education, from_, in_, CandidateStatus, CompanyNotInterest, My_Expected_compensation, Your_Linkedin_Profile, github,My_expertise_lies_in, My_Core_competencies, My_Work_Experience,My_Mobile_number, My_Current_Employer, Im_available_in) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

AUTHENTICATE_USER = "SELECT * FROM user_credential WHERE my_email = %s AND password =%s"

#USER_CREDENTIAL = "INSERT INTO user_credential(my_email, password) VALUES (%s, %s)"
USER_CREDENTIAL = "INSERT INTO credential(email, password, role, verification, emailHash) VALUES (%s, %s, 'candidate', %s, %s)"
#RECRUITER_CREDENTIAL = "INSERT INTO credential(recruiter_email, recruiter_password, role) VALUES (%s, %s, 'recruiter')"



GET_ALL_TYPE = ("select Type from company_details union select Type from company_details order by Type")

#GET_ALL_STAGE = "select Stage from company_details where Type = %s;"
GET_ALL_STAGE = "select Stage from company_details;"


GET_ALL_COMPANY = "select Company from company_details;"

RECRUTER_SIGNUP_DETAILS = "INSERT INTO company_signupDetails(CompanyName, ContactPerson, OfficialEmailID, SlackID, ContactNumber) VALUES (%s, %s, %s, %s, %s)"
RECRUITER_CREDENTIAL = "INSERT INTO credential(email, password, role, verification, emailHash) VALUES (%s, %s, 'recruiter', %s, %s)"


LOGIN = "SELECT role FROM credential WHERE email = %s AND password =%s"

VERIFY_MAIL = "UPDATE credential SET verification = 'Yes' WHERE emailHash = %s"



CANDIDATE_RECRUITER = "select role from credential where emailHash = %s"

ACCEPTANCE = "INSERT INTO acceptance(candidate, recruiter) VALUES (%s, %s)"

ACCEPTANCE_RECRUITER = "select recruiter from acceptance where candidate = %s"

CANDIDATE_NAME ="SELECT name from user_details where my_email = %s"