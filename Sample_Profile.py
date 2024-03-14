import streamlit as st

def user_input_features():
        gender = st.selectbox("Select Gender",("Male", "Female"))
        age = st.selectbox("Select Age group",("0-24", "25-34", "35-44", "45-54", "55-64", "65-74", "75-84", "Above 85"))
        height = st.number_input("Height(cm)")
        weight = st.number_input("Weight(lb)")
        food_preference = st.text_input("Your food preference")
        food_allergies = st.text_input("Any allergies?")
        disease_history = st.text_input("Any disease history?")

        st.sidebar.text ("")
        st.sidebar.text ("")

        st.button("Submit", type="primary")

        #NPI1 = st.sidebar.checkbox ("I wash my hands as per CDC Guidelines")
        #NPI2 = st.sidebar.checkbox ("I practice social distancing as per CDC Guidelines")
        #NPI3 = st.sidebar.checkbox ("I use face coverings as per CDC Guidelines")
        data = {'gender': gender,
                'age': age,
                'height': height,
                'weight': weight,
                'food_preference': food_preference,
                'food_allergies': food_allergies,
                'disease_history': disease_history,
               }
        return data

user_input_features()
