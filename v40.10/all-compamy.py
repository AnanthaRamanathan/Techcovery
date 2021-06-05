from flask import Flask, render_template, jsonify, request
from flask_mysqldb import MySQL,MySQLdb 
import queries
 
app = Flask(__name__)
      

      
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'app'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)



@app.route('/')
def main():

    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("select Company from company_detail")
    Company = cur.fetchall()
    print (Company)
    
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("select Type from company_detail union select Type from company_detail order by Type")
    type_ = cur.fetchall()
    print (type_)

    

    
    return render_template('index.html', type_ = type_, CompanyNotInterest = Company)





 
@app.route("/stage",methods=["POST","GET"])
def carbrand():  
    cursor = mysql.connection.cursor()
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        companyType = request.form['companyType'] 
        print(companyType)  
        result = cur.execute("SELECT Stage FROM company_detail WHERE Type = %s", [companyType] )
        companyStage = cur.fetchall()  
        OutputArray = []
        for row in companyStage:
            outputObj = {
                'stage': row['Stage']}
            OutputArray.append(outputObj)
    return jsonify(OutputArray)

@app.route("/company",methods=["POST","GET"])
def company():  
    cursor = mysql.connection.cursor()
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        companyType = request.form['companyType']
        companyStage = request.form['companyStage'] 
        
        print(companyType)  
        print(companyStage)

        result = cur.execute("SELECT Company FROM company_detail WHERE Stage = %s and Type =%s", [companyStage, companyType ])
        print(result)

        cmodel = cur.fetchall()  
        OutputArray = []
        for row in cmodel:
                outputObj = {'company': row['Company']}
                OutputArray.append(outputObj)
    return jsonify(OutputArray)


if __name__ == "__main__":

    app.run(host="localhost", port=5003, debug=True)