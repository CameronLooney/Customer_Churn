import streamlit as st
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
st.title("Churn Prediction App")

st.sidebar.title("Churn Probability of a Single Customer")


gender = st.sidebar.radio("Gender", ('Male',"Female"))
senior_citizen = st.sidebar.radio("Senior Citizen", ('Yes',"No"))
partner= st.sidebar.radio("Partner", ('Yes',"No"))
dependents = st.sidebar.radio("Dependents", ('Yes',"No"))
phoneService = st.sidebar.radio("Phone Service", ('Yes',"No"))
multipleLines =st.sidebar.radio("Multiple Lines", ('Yes',"No", "No phone service"))
InternetService=st.sidebar.radio("Customer’s internet service provider", ('DSL', 'Fiber optic', 'No'))
OnlineSecurity=st.sidebar.radio("Customer`s online security", ('No', 'Yes', 'No internet service'))
OnlineBackup =st.sidebar.radio("Customer's online backup", ('No', 'Yes', 'No internet service'))
TechSupport=st.sidebar.radio("Customer has tech support?", ('No', 'Yes', 'No internet service'))
device_protection=st.sidebar.radio("Customer's device protection?", ('No', 'Yes', 'No internet service'))
streamingTV = st.sidebar.radio("TV Streaming?", ('No', 'Yes', 'No internet service'))
streamingMovies = st.sidebar.radio("Movie Streaming?", ('No', 'Yes', 'No internet service'))
Contract=st.sidebar.radio("Contract term", ('Month-to-month', 'One year', 'Two year'))
paperless_billings =  st.sidebar.radio("Paperless Billings?", ('Yes',"No"))
PaymentMethod =  st.sidebar.radio("Payment Method?", ("Electronic check","Mailed check","Bank transfer (automatic)","Electronic check","Credit card (automatic)"))
tenure = st.sidebar.slider("Tenure : Months of customer stayed",1,72,33,step=1)
MonthlyCharges = st.sidebar.slider("Charge : Amount charged to customer",18.25,118.75,50.00,step = 0.05)
totalCharge = st.sidebar.slider("Charge : Amount charged to customer total",18.25,9000.01,50.00,step = 0.05)





my_dict = { "gender":gender,"SeniorCitizen":senior_citizen,	"Partner":partner,"Dependents":dependents,"tenure":tenure,"PhoneService":phoneService,"MultipleLines":multipleLines,
            "InternetService": InternetService,"OnlineSecurity":OnlineSecurity,"OnlineBackup":OnlineBackup,	"DeviceProtection":device_protection	,"TechSupport":TechSupport,	"StreamingTV":streamingTV,
            "StreamingMovies":streamingMovies,"Contract":Contract,"PaperlessBilling":paperless_billings,"PaymentMethod":PaymentMethod,"MonthlyCharges":MonthlyCharges,"TotalCharges":totalCharge}
df = pd.DataFrame.from_dict([my_dict])
def object_to_int(dataframe_series):
    if dataframe_series.dtype=='object':
        dataframe_series = LabelEncoder().fit_transform(dataframe_series)
    return dataframe_series
df = df.apply(lambda x: object_to_int(x))


with open('my_model.pkl', 'rb') as file:
    model = pickle.load(file)

run = st.sidebar.button("RUN")
if run:
    prediction = model.predict(df)[0]


    prediction_percent = model.predict_proba(df)



    if prediction == 1:
        percent = float(prediction_percent[0][1])
        percent = round((percent *100),2)
        prediction = "Churn Yes !"
        st.warning(prediction)
        st.write("We are {}% confident this customer will churn".format(percent))

    else:
        percent = float(prediction_percent[0][0])
        percent = round((percent * 100), 2)
        prediction = "Churn No"
        st.success(prediction)
        st.write("We are {}% confident this customer will not churn".format(percent))





