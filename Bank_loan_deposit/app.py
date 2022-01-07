from flask import Flask, render_template, request
import joblib

model=joblib.load('bank_loan_deposit.pkl') 

#instance of an app
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('prediction.html')

@app.route('/data', methods=['POST'] )
def data():
    age= request.form.get('age')
    job= request.form.get('job')
    marital= request.form.get('marital')
    education= request.form.get('education')
    default= request.form.get('default')
    balance= request.form.get('balance')
    housing= request.form.get('housing')
    loan= request.form.get('loan')
    contact= request.form.get('contact')
    day= request.form.get('day')
    month= request.form.get('month')
    duration= request.form.get('duration')
    campaign= request.form.get('campaign')
    pdays= request.form.get('pdays')
    previous= request.form.get('previous')
    poutcome= request.form.get('poutcome')




    result= model.predict([[age,job,marital,education,default,balance,housing,loan,contact,day,month,duration,campaign,pdays,previous,poutcome]])
    
    print(result)
    if result[0]==1:
        output='Deposit will be done'
    else:
        output='Deposit will not be done'

    
    return render_template('result.html', predict=output)

if __name__ == '__main__':
    app.run(debug=True)