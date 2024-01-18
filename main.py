import langchain_helper as lch
import streamlit as st

st.title("Pets Name Generator")

# List of pet options
pet_options = ["cat", "dog", "cow", "hen", "horse", "hamster"]
# User selects the pet type
user_animal_type = st.sidebar.selectbox("What is your pet?", pet_options)

# Initialize pet_color variable
pet_color = None

# Check if the selected pet type is in the pet_options list
if user_animal_type in pet_options:
    # User inputs the color of their pet with a dynamically created label
    pet_color = st.sidebar.text_area(f"What color is your {user_animal_type}?", max_chars=15)

# If pet_color is provided, generate and display the pet names
if pet_color:
    response = lch.generate_pet_names(user_animal_type, pet_color)
    st.text(response['pet_name'])
