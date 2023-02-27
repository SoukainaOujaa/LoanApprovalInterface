from flask import Flask , render_template, request
import pickle
import numpy as np
import pandas as pd
import joblib
import warnings 
import sys
if not sys.warnoptions:
    warnings.simplefilter("ignore")
warnings.filterwarnings("ignore",category=DeprecationWarning)


# model=pickle.load(open('first.h5','rb'))


model=joblib.load('loan_prediction')

app = Flask(__name__,template_folder='template')

@app.route('/')
def main():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def home():
    name = request.form['NAME']
    address = request.form['ADDRESS']
    email = request.form['EMAIL']
    mobile1 = request.form['MOBILE']
    

# form
    gender1 = request.form['GENDER']
    married1 = request.form['MARRIED']
    dependents1 = request.form['DEPENDENTS']
    education1 = request.form['EDUCATION']
    self_emp1 = request.form['SELF_EMP']
    app_income1 = request.form['APP_INCOME']
    coapp_income1 = request.form['COAPP_INCOME']
    loan_amount1 = request.form['LOAN_AMOUNT']
    la_term1 = request.form['LA_TERM']
    cr_history1 = request.form['CR_HISTORY']
    property1 = request.form['PROPERTY']

# valeurs saisies de string vers int / float
    mobile=int(mobile1)
    app_income=int(app_income1)
    coapp_income=float(coapp_income1)
    loan_amount=float(loan_amount1)
    la_term=float(la_term1)


    
    if(cr_history1=='Clear'):
        cr_history=1.0
    else:
        cr_history=0.0
    if(married1=='YES'):
        married=1
    else:
        married=0
    if(gender1=='MALE'):
        gender=1
    else:
        gender=0
 

    if(dependents1=='zero'):
        dependents='0'
    if(dependents1=='one'):
        dependents='1'
    if(dependents1=='two'):
        dependents='2'
    if(dependents1=='three_plus'):
        dependents='3+'

    if(education1=='Graduate'):
        education=1
    else:
        education=0
    if(self_emp1=='yes'):
        self_emp=1
    else:
        self_emp=0
    
    p_rural=0
    p_semi_urban=0
    p_urban=0
    if(property1=="rural"):
        p_a=0
    if(property1=="semi-urban"):
       p_a=2
    if(property1=="urban"):
        p_a=1
    
    arr=np.array([gender,married,dependents,education,self_emp,app_income,coapp_income,loan_amount,la_term,cr_history,p_a])
    # df=pd.DataFrame(arr)
    pred= model.predict(arr.reshape(1,-1))
    return render_template('prediction_page.html', data=pred,name=name)
    


if __name__ == "__main__":
    app.run(debug=True)