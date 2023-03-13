import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models
diabetes_model = pickle.load(open(diabetes_model.sav','rb'))
heart_disease_model = pickle.load(open(heart_model.sav','rb'))
parkinsons_model = pickle.load(open(parkinsons_model.sav','rb'))
kidney_model=pickle.load(open(kidney_model.sav','rb'))


# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Kidney Disease Prediction',
                           'Parkinsons Prediction'
                            ],
                           default_index=0)

# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):

    # page title
    st.title('Diabetes Prediction using ML')
    st.write("Please fill out the following fields to predict your risk of diabetes:")
    st.write("---")

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.slider('Number of Pregnancies (0-17)', min_value=0, max_value=17, step=1)

    with col2:
        Glucose = st.slider('Glucose Level (0-199)', min_value=0, max_value=199, step=1)

    with col3:
        BloodPressure = st.slider('Blood Pressure value(0,122)', min_value=0, max_value=122, step=1)

    with col1:
        SkinThickness = st.slider('Skin Thickness value(0-99)', min_value=0, max_value=99, step=1)

    with col2:
        Insulin = st.slider('Insulin Level(0-846)', min_value=0, max_value=846, step=1)

    with col3:
        BMI = st.slider('BMI value(0.0-67.1)',min_value=0.0, max_value=67.1, step=0.1)

    with col1:
        DiabetesPedigreeFunction = st.slider('Diabetes Pedigree Function value(0.078-2.42)', min_value=0.078,
                                                   max_value=2.42, step=0.01)

    with col2:
        Age = st.slider('Age of the Person(21-81 )', min_value=21, max_value=81, step=1)

    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict(
            [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if (diab_prediction[0] == 1):
            diab_diagnosis = "You are at high risk of diabetes. Please consult your doctor."
        else:
            diab_diagnosis = "You are at low risk of diabetes."

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):

    # page title
    st.title('Heart Disease Prediction using ML')
    st.write("Please fill out the following fields to predict your risk of heart disease:")
    st.write("---")

    # Add input fields
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        age = st.slider("Age", min_value=20, max_value=80, step=1)
    with col2:
        sex = st.selectbox("Sex", options=["Male", "Female"])
    with col3:
        cp = st.selectbox("Chest Pain Type",
                                  options=["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"])
    with col4:
        trestbps = st.slider("Resting Blood Pressure(90,200)", min_value=90, max_value=200, step=1)

    with col1:
        chol = st.slider("Cholesterol(100-500)", min_value=100, max_value=500, step=1)
    with col2:
        fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", options=["True", "False"])
    with col3:
        restecg = st.selectbox("Resting ECG",
                                   options=["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"])
    with col4:
        thalach = st.slider("Maximum Heart Rate Achieved(50-250)", min_value=50, max_value=250, step=1)

    with col1:
        exang = st.selectbox("Exercise Induced Angina", options=["Yes", "No"])
    with col2:
        oldpeak = st.slider("ST Depression Induced by Exercise Relative to Rest(0.0-6.2)", min_value=0.0,max_value= 6.2,step= 0.1)
    with col3:
        slope = st.selectbox("ST-Segment Slope", options=["Upsloping", "Flat", "Downsloping"])
    with col4:
        ca = st.selectbox("Number of Major Vessels", options=["0", "1", "2", "3"])

    with col1:
        thal = st.selectbox("Thalassemia Type", options=["Normal", "Fixed Defect", "Reversible Defect"])

    # Map string inputs to numerical values
    sex = 1 if sex == "Male" else 0
    cp = 0 if cp == "Typical Angina" else 1 if cp == "Atypical Angina" else 2 if cp == "Non-Anginal Pain" else 3
    fbs = 1 if fbs == "True" else 0
    restecg = 0 if restecg == "Normal" else 1 if restecg == "ST-T Wave Abnormality" else 2
    exang = 1 if exang == "Yes" else 0
    slope = 1 if slope == "Flat" else 2 if slope == "Downsloping" else 0
    thal = 1 if thal =='Fixed Defect' else 2 if thal=='Reversible Defect' else 0

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict(
            [[int(age), int(sex), int(cp), int(trestbps), int(chol),int(fbs),
             int(restecg),int(thalach), int(exang), int(oldpeak), int(slope), int(ca), int(thal)]])


        if (heart_prediction[0] == 1):
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if (selected== "Parkinsons Prediction"):

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.slider('MDVP: Fo(Hz)', 40.0, 200.0, 100.0)

    with col2:
        fhi = st.slider('MDVP: Fhi(Hz)', 40.0, 400.0, 200.0)

    with col3:
        flo = st.slider('MDVP: Flo(Hz)', 40.0, 200.0, 120.0)

    with col4:
        Jitter_percent = st.slider('MDVP: Jitter(%)',0.001, 1.0, 0.005)

    with col5:
        Jitter_Abs = st.slider('MDVP: Jitter(Abs)',0.0, 0.1, 0.0)

    with col1:
        RAP = st.slider('MDVP: RAP', 0.0, 0.1, 0.0)

    with col2:
        PPQ = st.slider('MDVP: PPQ',0.0, 0.1, 0.0)

    with col3:
        DDP = st.slider('Jitter: DDP',0.0, 0.3, 0.0)

    with col4:
        Shimmer = st.slider('MDVP: Shimmer',0.0, 0.1, 0.0)

    with col5:
        Shimmer_dB = st.slider('MDVP: Shimmer(dB)', 0.0, 20.0, 0.0)

    with col1:
        APQ3 = st.slider('Shimmer: APQ3', 0.0, 0.05, 0.0)

    with col2:
        APQ5 = st.slider('Shimmer: APQ5',0.0, 0.05, 0.0)

    with col3:
        APQ = st.slider('MDVP: APQ',0.0, 0.1, 0.0)

    with col4:
        DDA = st.slider('Shimmer: DDA',0.0, 0.1, 0.0)

    with col5:
        NHR = st.slider('NHR',0.0, 0.5, 0.0)

    with col1:
        HNR = st.slider('HNR',10.0, 35.0, 20.0)

    with col2:
        RPDE = st.slider('RPDE',0.0, 1.0, 0.5)

    with col3:
        DFA = st.slider('DFA',0.0, 1.0, 0.5)

    with col4:
        spread1 = st.slider('spread1',-10.0, 10.0, 0.0)

    with col5:
        spread2 = st.slider('spread2', 0.0, 0.2, 0.0)

    with col1:
        D2 = st.slider('D2', 0.0, 3.0, 1.0)

    with col2:
        PPE = st.slider('PPE',0.0, 0.5, 0.0)

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP,
                                                           Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE,
                                                           DFA, spread1, spread2, D2, PPE]])

        if (parkinsons_prediction[0] == 1):
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)

# Kidney Disease Prediction Page
if (selected== "Kidney Disease Prediction"):

    # page title
    st.title("Kidney Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        age = st.slider('Age', 0, 100, 25)
    with col2:
        bp = st.slider('Blood Pressure',min_value=50,max_value=120,step=1)
    with col3:
        al = st.selectbox('Albumin', [0.0, '1.0', '2.0', '3.0', '4.0'])
    with col4:
        su = st.selectbox('Sugar', [0.0, '1.0', '2.0', '3.0', '4.0', '5.0'])
    with col5:
        rbc = st.selectbox('Red Blood Cells', ['Normal', 'Abnormal'])
    with col1:
        pc = st.selectbox('Pus Cells', ['Normal', 'Abnormal'])
    with col2:
        pcc = st.selectbox('Pus Cell Clumps', ['Not Present', 'Present'])
    with col3:
        ba = st.selectbox('Bacteria', ['Not Present', 'Present'])
    with col4:
        bgr = st.slider('Blood Glucose Random', 0, 500, 100)
    with col5:
        bu = st.slider('Blood Urea', 0, 200, 50)
    with col1:
        sc = st.slider('Serum Creatinine', 0, 20, 5)
    with col2:
        pot = st.slider('Potassium', 0.0, 10.0, 4.0)
    with col3:
        wc = st.slider('White Blood Cell Count', 0, 100000, 5000)
    with col4:
        htn = st.selectbox('Hypertension', ['Yes', 'No'])
    with col5:
        dm = st.selectbox('Diabetes Mellitus', ['Yes', 'No'])
    with col1:
        cad = st.selectbox('Coronary Artery Disease', ['Yes', 'No'])
    with col2:
        pe = st.selectbox('Pedal Edema', ['Yes', 'No'])
    with col3:
        ane = st.selectbox('Anemia', ['Yes', 'No'])

    # Convert categorical data to binary
    rbc = 1 if rbc == 'Abnormal' else 0
    pc = 1 if pc == 'Abnormal' else 0
    pcc = 1 if pcc == 'Present' else 0
    ba = 1 if ba == 'Present' else 0
    htn = 1 if htn == 'Yes' else 0
    dm = 1 if dm == 'Yes' else 0
    cad = 1 if cad == 'Yes' else 0
    pe = 1 if pe == 'Yes' else 0
    ane = 1 if ane == 'Yes' else 0

        # code for Prediction
    kidney_disease_diagnosis = ''

    # creating a button for Prediction

    if st.button('Kidney Disease Prediction Result'):
        kidney_disease_diagnosis = kidney_model.predict(
            [[age, bp, al, su, rbc,pc,pcc,ba,bgr,bu,sc,pot,wc,htn,dm,cad,pe,ane]])

        if kidney_model[0] == 1:
            kidney_disease_diagnosis = 'The Person is having Chronic Kidney Disease'
        else:
            kidney_disease_diagnosis='The Person is not having Chronic Kidney Disease '

    st.success(kidney_disease_diagnosis)
