import streamlit as st
import streamlit.components.v1 as  components
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
from sklearn import tree
from PIL import Image
import pickle

st.set_page_config(page_title='ITEC 5205 Course Project', layout='wide')
                                                   # menu_items={
                                                               # 'Get Help': '<email-id>',
                                                               # 'Report a bug': "<email-id>",
                                                              #  'About': "# This is a header. This is an *extremely* cool app!"})
import time
with st.spinner('Wait for it...'):
    time.sleep(2)
st.success('Page loading complete')
st.balloons()

st.title('Impact of Covid-19 on Homeless Shelter Sites')

container = st.container()

###     DASHBOARD
with container:
    # st.markdown("___")
    

    st.subheader("Dashboard")
    htmlfile=open("5205.html", 'r', encoding ='utf-8')
    source_code = htmlfile.read()
    print(source_code)
    components.html(source_code, height = 868, width = 1350)

###     MACHINE LEARNING
with container:
    with st.expander("ML algorithm"):
       
        df= pd.DataFrame(pd.read_csv("combined.csv"))   
        to_scale = df.drop(['Date', 'GDP',
                            'Inflation'], axis=1)
        model = pickle.load(open('model_5205', 'rb'))

        #Normalization
        sc= MinMaxScaler()
        first = sc.fit_transform(to_scale)
        scaled = pd.DataFrame(first, columns = to_scale.columns)
        

        X = scaled.drop(['Shelter occupancy'], axis=1)
        y = scaled["Shelter occupancy"]

        if st.button('Click the button to run the model'):
            st.subheader("Random Forest Regressor Model")
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # regressor = RandomForestRegressor()
            # yoyo = regressor.fit(X_train, y_train)
            y_pred = model.predict(X_test)

            mae = metrics.mean_absolute_error(y_test, y_pred)
            
            mse = metrics.mean_squared_error(y_test, y_pred)
            
            rmse = np.sqrt(metrics.mean_squared_error(y_test, y_pred))
            
            r2 = r2_score(y_test, y_pred)

            columns = st.columns((1,1,1,1))

            with columns[0]:
                st.markdown("Mean absolute error: " + str(mae))
            with columns[1]:
                st.markdown("Mean squared error: " + str(mse))
            with columns[2]:
                st.markdown("Root mean squared error: " + str(rmse))
            with columns[3]:
                st.markdown("Coefficient of determination (R2): " + str(r2))

           
            st.markdown(" ")
            st.caption("One decision tree from the random forest regressor model")
            fn=X.columns
            cn=['Shelter occupancy']
            fig = plt.figure(figsize = (12,5), dpi = 1200)

            tree.plot_tree(model.estimators_[1],
                        feature_names = fn, 
                        class_names=cn,
                        filled=True,
                        rounded= True,
                        fontsize=3)
                           
            st.pyplot(fig)
            
        else:
            st.write(' ') #space with no statement
        
 




###     GOOGLE MOBILITY

with container:
    with st.expander("Mobility"):
        st.subheader("Mobility based on Google's dataset")
        
        htmlfile1=open("google mobility.html", 'r', encoding ='utf-8')
        source_code1 = htmlfile1.read()
        print(source_code1)
        components.html(source_code1, height = 800, width = 1000)

###     GOOGLE TRENDS

with container:
    with st.expander("Trends"):
        st.subheader("Trends on web searches")
        
        htmlfile2=open("trends.html", 'r', encoding ='utf-8')
        source_code2 = htmlfile2.read()
        print(source_code2)
        components.html(source_code2, height = 350, width = 1000)

##   CREDITS
with container:
    st.markdown(" ")
    st.subheader('*Credits*')
    st.markdown("This project was created by Abhijeet Singh for course ITEC-5205 (Data intensive application) at Carleton University taught by Prof. Omair Shafiq.")
