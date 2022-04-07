import streamlit as st
import streamlit.components.v1 as  components



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


###         COMPARISON BY GENDER

# with container:
    
    
#     st.write("Below are different categories for data analysis  \n"
#             "Part 1 : Shelter sites types with count  \n"
#             "Part 2 : Shelter sites capacity count distribution \n"
#             "Part 3 : Shelter sites average capacity distribution  \n"
#             "Part 4 : Comparison by Education  \n"
#             "Part 5 : Additional info using Google trends")
#     st.markdown("___")

#     with st.expander("Option 1 : Comparison by Gender"):
    
#         st.markdown(" ")
#         st.markdown("Please select the filters below:")
#         city = df1['City'].unique().tolist()
#         shelter_type = df1['ShelterType'].unique().tolist()
#         year = df1['YEAR'].unique().tolist()

#         columns = st.columns((3,3,2))

#         with columns[0]:
#             city_selection = [st.multiselect("City",
#                                             city, default=city)]
#         with columns[1]:
#             shelter_type_selection = [st.multiselect('Shelter Type',
#                                                 shelter_type,
#                                                 default = shelter_type)]
#         with columns[2]:
#             year_selection = [st.multiselect('Year',
#                                             year, default = year)]                              
     

#         # gender_both = ['Males','Females']
#         # all_age = ['15 years and over','15 to 24 years','25 to 54 years','55 years and over']
#         # age_15_over = ['15 years and over']
#         # age_15_24 = ['15 to 24 years']
#         # age_25_54 = ['25 to 54 years']
#         # age_55_over = ['55 years and over']

#         ## Dataframe filter/mask

#         mask1 = (df1['City'].isin(city_selection)) & (df1['ShelterType'].isin(shelter_type_selection)) & (df1['YEAR'].isin(year_selection))
       


        # st.subheader("Shelter type distribution")                    

        # fig1 = px.line(df1[mask1], x = 'YEAR', y = 'Capacity', color='ShelterType', template='gridon')
        # # fig1.update_layout( width=1000, height = 500)
        # #fig1.update_layout({'plot_bgcolor':'rgba(0, 0, 0, 0)'})
        # st.plotly_chart(fig1)

        # data = [dict(
        #         type = 'Scatter',
        #         x = 'Date',
        #         y = 'Capacity',
        #         mode = 'markers',
        #         transforms = [dict(
        #                         type = 'aggregate',
        #                         groups = df1['ShelterTypes'],
        #                         aggregations = [dict(
        #                             target= 'y', func ='sum', enabled = True
        #                                         )]
        #                     )]
        #          )]

        # fig1_dict = dict(data=data)
        # pio.show(fig1.dict, validate=False)

###         COMPARISION BY AGE
# with container:

#     with st.expander("Option 2 : Comaprison by Age"):

        # st.markdown("___")
        # st.subheader("Comparison by age")
        # st.markdown("Age filter at top is NA for this section")
        
        # fig2=px.line(df[mask3], x='Date', y='Value', facet_col='Age group', template='gridon')
        # fig2.update_layout( width=1200, height=500)
        # st.plotly_chart(fig2)
    
        # columns = st.columns((2,2))

        # with columns[0]:
        #     fig3 = px.line(df[mask4], x='Date', y='Value', color_discrete_sequence=["black"], title="Age 15 and over", template='plotly')
        #     fig3.update_layout(title_x=0.5, title_y=0.85)
        #     fig3.update_layout({'plot_bgcolor':'rgba(0, 0, 0, 0)'})
        #     st.plotly_chart(fig3)

        #     fig5 = px.line(df[mask5], x='Date', y='Value', color_discrete_sequence=["purple"], title="Age 15-24", template='presentation')
        #     fig5.update_layout(title_x=0.5, title_y=0.85)
        #     fig5.update_layout({'plot_bgcolor':'rgba(0, 0, 0, 0)'})
        #     st.plotly_chart(fig5)
            
        
        # with columns[1]:
        #     fig4 = px.line(df[mask7], x='Date', y='Value', color_discrete_sequence=["indigo"], title="Age 55 and over", template='ggplot2')
        #     fig4.update_layout(title_x=0.5, title_y=0.85)
        #     fig4.update_layout({'plot_bgcolor':'rgba(0, 0, 0, 0)'})
        #     st.plotly_chart(fig4)

        #     fig6 = px.line(df[mask6], x='Date', y='Value', color_discrete_sequence=["green"], title="Age 25-54", template='gridon')
        #     fig6.update_layout(title_x=0.5, title_y=0.85)
        #     fig6.update_layout({'plot_bgcolor':'rgba(0, 0, 0, 0)'})
        #     st.plotly_chart(fig6)


###     GOOGLE TRENDS
with container:
    # st.markdown("___")
    

    st.subheader("Dashboard")
    htmlfile=open("5205.html", 'r', encoding ='utf-8')
    source_code = htmlfile.read()
    print(source_code)
    components.html(source_code, height = 868, width = 1350)

#  dataset
# with container:
#     st.subheader("Filtered Dataset")
#     st.dataframe(df[mask1])
    
##   CREDITS
with container:
    st.markdown(" ")
    st.subheader('*Credits*')
    st.markdown("This project was created by Abhijeet Singh for course ITEC-5205 (Data intensive application) at Carleton University taught by Prof. Omair Shafiq.")
