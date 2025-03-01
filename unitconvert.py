import streamlit as st

# Apply custom CSS
st.markdown(
    """
    <style>
    .stApp {
        # background: linear-gradient(135deg, #bcbcbc, #cfe2f3);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.3);
    }
    h1 {
        text-align: center;
        font-size: 30px;
        color: black;
    }
    .center-buttons {
        display: flex;
        justify-content: center;
        gap: 20px;
    }
    .stButton > button {
         background-color: rgb(125, 134, 126) !important;
        color: white !important;
        border-radius: 5px;
        padding: 10px 15px;
        font-size: 16px;
        border: none;
    }
    .stButton > button:hover {
        transform: scale(1.05);
         background: linear-gradient(45deg, #f3f3f3, rgb(68, 59, 59)) !important;   
    }
    .result-box {
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        background-color: white;
        padding: 15px;
        border-radius: 10px;
        color: gray;
        margin-top: 20px;
        box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.2);
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 14px;
        color: gray;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and description
st.markdown("<h1>🔢 Unit Converter  </h1>", unsafe_allow_html=True)
st.write("This is a simple unit converter app that converts units from one category to another.")

# Sidebar menu
conversion_type = st.sidebar.selectbox("Select Category", ["Length", "Weight", "Temperature"])

# Input value
value = st.number_input("Enter Value", min_value=0.0, format="%.4f")

# Layout for the conversion
col1, col2 = st.columns(2)


if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["millimeter", "centimeter", "meter", "kilometer", "inch", "foot", "yard", "mile"])
    with col2:
        to_unit = st.selectbox("To", ["millimeter", "centimeter", "meter", "kilometer", "inch", "foot", "yard", "mile"])

elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["milligram", "gram", "kilogram", "pound", "ounce"])
    with col2:
        to_unit = st.selectbox("To", ["milligram", "gram", "kilogram", "pound", "ounce"])

elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["celsius", "fahrenheit", "kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["celsius", "fahrenheit", "kelvin"])

# Converter functions
def length_converter(value, from_unit, to_unit):
    length_units = {
        "millimeter": 1,
        "centimeter": 10,
        "meter": 1000,
        "kilometer": 1000000,
        "inch": 25.4,
        "foot": 304.8,
        "yard": 914.4,
        "mile": 1609344
    }
    return value / length_units[from_unit] * length_units[to_unit]

def weight_converter(value, from_unit, to_unit):
    weight_units = {
        "milligram": 1,
        "gram": 1000,
        "kilogram": 1000000,
        "pound": 453592,
        "ounce": 28350
    }
    return value / weight_units[from_unit] * weight_units[to_unit]

def temperature_converter(value, from_unit, to_unit):
    if from_unit == "celsius":
        if to_unit == "fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "kelvin":
            return value + 273.15
    elif from_unit == "fahrenheit":
        if to_unit == "celsius":
            return (value - 32) * 5/9
        elif to_unit == "kelvin":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "kelvin":
        if to_unit == "celsius":
            return value - 273.15
        elif to_unit == "fahrenheit":
            return (value - 273.15) * 9/5 + 32
    return value  
# Conversion Button

if st.button("Convert"):
    if from_unit == to_unit:
        result = value  # No conversion needed
    else:
        if conversion_type == "Length":
            result = length_converter(value, from_unit, to_unit)
        elif conversion_type == "Weight":
            result = weight_converter(value, from_unit, to_unit)
        elif conversion_type == "Temperature":
            result = temperature_converter(value, from_unit, to_unit)

    st.markdown(f"<div class='result-box'>{value} {from_unit} is equal to {result:.4f} {to_unit}</div>", unsafe_allow_html=True)

# Reset Button
if st.button("Reset"):
    st.cache_data.clear() 
    st.rerun()  
