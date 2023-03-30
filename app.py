#importing required libraries
import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#Creating Flast App
app=Flask(__name__)
model=pickle.load(open('predictive_model.pkl','rb'))
scalar=pickle.load(open('scalar_obj.pkl','rb'))
encoder=pickle.load(open('encoder.pkl','rb'))

@app.route('/')
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    gender=request.form['gender']
    if gender=='Male':
        gender==1
    else:
        gender==0
    
    SeniorCitizen=request.form['SeniorCitizen']
    if SeniorCitizen=='Yes':
        SeniorCitizen==0
    else:
        SeniorCitizen==1

    Partner=request.form['Partner']
    if Partner=='Married':
        Partner==1
    else:
        Partner==0

    Dependents=request.form['Dependents']
    if Dependents=='Yes':
        Dependents==1
    else:
        Dependents==0

    
    tenure=int(request.form['tenure'])

    PhoneService=request.form['PhoneService']
    if PhoneService=='Yes':
        PhoneService==1
    else:
        PhoneService==0

    MultipleLines=request.form['MultipleLines']
    if MultipleLines=='Yes':
        MultipleLines==2
    elif MultipleLines=='No':
        MultipleLines==0
    else:
        MultipleLines==1

    InternetService=request.form['InternetService']
    if InternetService=='DSL':
        InternetService==0
    elif InternetService=='Fiber Optic':
        InternetService==1
    else:
        InternetService==2

    OnlineSecurity=request.form['OnlineSecurity']
    if OnlineSecurity=='Yes':
        OnlineSecurity==2
    elif OnlineSecurity=='No':
        OnlineSecurity==0
    else:
        OnlineSecurity==1
    
    OnlineBackup=request.form['OnlineBackup']
    if OnlineBackup=='Yes':
        OnlineBackup==2
    elif OnlineBackup=='No':
        OnlineBackup==0
    else:
        OnlineBackup==1

    DeviceProtection=request.form['DeviceProtection']
    if DeviceProtection=='Yes':
        DeviceProtection==2
    elif DeviceProtection=='No':
        DeviceProtection==0
    else:
        DeviceProtection==1

    TechSupport=request.form['TechSupport']
    if TechSupport=='Yes':
        TechSupport==2
    elif TechSupport=='No':
        TechSupport==0
    else:
        TechSupport==1

    StreamingTV=request.form['StreamingTV']
    if StreamingTV=='Yes':
        StreamingTV==2
    elif StreamingTV=='No':
        StreamingTV==0
    else:
        StreamingTV==1

    StreamingMovies=request.form['StreamingMovies']
    if StreamingMovies=='Yes':
        StreamingMovies==2
    elif StreamingMovies=='No':
        StreamingMovies==0
    else:
        StreamingMovies==1

    Contract=request.form['Contract']
    if Contract=='Month to Month':
        Contract==0
    elif Contract=='One Year':
        Contract==1
    else:
        Contract==2


    PaperlessBilling=request.form['PaperlessBilling']
    if PaperlessBilling=='Yes':
        PaperlessBilling==1
    else:
        PaperlessBilling==0

    PaymentMethod=request.form['PaymentMethod']
    if PaymentMethod=='bank-transfer':
        PaymentMethod==0
    elif PaymentMethod=='credit-card':
        PaymentMethod==1
    elif PaymentMethod=='electronic-payment':
        PaymentMethod==2
    else:
        PaymentMethod==3



    MonthlyCharges=float(request.form['MonthlyCharges'])
    TotalCharges=float(request.form['TotalCharges'])
    numAdminTickets=int(request.form['numAdminTickets'])
    numTechTickets=int(request.form['numTechTickets'])

    input=pd.DataFrame([[gender,SeniorCitizen,Partner,Dependents,tenure,PhoneService,MultipleLines,InternetService,OnlineSecurity,OnlineBackup,DeviceProtection,TechSupport,StreamingTV,StreamingMovies,Contract,PaperlessBilling,PaymentMethod,MonthlyCharges,TotalCharges,numAdminTickets,numTechTickets]])
    for i in input.select_dtypes(include='object').columns:
        input[i]=encoder.fit_transform(input[i])
    
    final_input=scalar.transform(input)
    
    prediction=model.predict(final_input)[0]
    if prediction==0:
        return render_template('index.html',prediction_text="Customer Will Not Churn")
    else:
        return render_template('index.html',prediction_text="This Customer Will Churn. Time to announce some exciting offers.")
    

if __name__=="__main__":
    app.run(debug=True)