import streamlit as st
import pandas as pd
import joblib
import os

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="VoltWise | EV Adoption Insight",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# CUSTOM CSS
# =========================================================
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Manrope:wght@400;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background-color: #0b1120;
    color: #f1f5f9;
}

.block-container {
    max-width: 1150px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

[data-testid="stHeader"] {
    background: transparent;
}

.hero {
    background: linear-gradient(135deg, #121d32 0%, #172b40 60%, #123c3b 100%);
    border: 1px solid rgba(148, 163, 184, 0.15);
    padding: 36px;
    border-radius: 24px;
    margin-bottom: 25px;
}

.hero-tag {
    display: inline-block;
    background: rgba(34, 197, 94, 0.12);
    color: #4ade80;
    padding: 7px 13px;
    border-radius: 30px;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1px;
}

.hero-title {
    font-family: 'Manrope', sans-serif;
    font-size: 42px;
    font-weight: 800;
    color: #ffffff;
    margin-top: 16px;
    margin-bottom: 10px;
}

.hero-description {
    color: #a8b6ca;
    font-size: 16px;
    max-width: 700px;
    line-height: 1.7;
}

.section-heading {
    font-family: 'Manrope', sans-serif;
    font-size: 23px;
    font-weight: 800;
    color: #f8fafc;
    margin-top: 18px;
    margin-bottom: 5px;
}

.section-subtitle {
    color: #94a3b8;
    font-size: 14px;
    margin-bottom: 20px;
}

div[data-testid="stForm"] {
    background: #111a2b;
    border: 1px solid #243249;
    padding: 24px;
    border-radius: 20px;
}

div[data-testid="stMetric"] {
    background: #121e30;
    padding: 18px;
    border: 1px solid #243249;
    border-radius: 16px;
}

div[data-testid="stMetricLabel"] {
    color: #94a3b8;
}

div[data-testid="stMetricValue"] {
    color: #f8fafc;
}

div[data-testid="stSelectbox"] label,
div[data-testid="stNumberInput"] label,
div[data-testid="stSlider"] label {
    color: #cbd5e1 !important;
}

.stButton > button {
    background: linear-gradient(90deg, #16a34a, #22c55e);
    color: #ffffff;
    border: none;
    border-radius: 12px;
    height: 52px;
    font-weight: 700;
    font-size: 16px;
    transition: 0.2s ease;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #15803d, #16a34a);
    transform: translateY(-1px);
}

.result-card {
    background: linear-gradient(145deg, #14243a, #112d32);
    border: 1px solid #2b4850;
    border-radius: 22px;
    padding: 28px;
    margin-top: 20px;
}

.result-label {
    color: #94a3b8;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
}

.result-title {
    font-family: 'Manrope', sans-serif;
    font-size: 30px;
    font-weight: 800;
    margin-top: 10px;
    margin-bottom: 12px;
}

.result-text {
    color: #bdcbdc;
    font-size: 15px;
    line-height: 1.7;
}

.insight-box {
    background: #111b2a;
    border: 1px solid #273449;
    border-radius: 16px;
    padding: 20px;
    margin-top: 15px;
}

.insight-title {
    color: #f8fafc;
    font-weight: 700;
    font-size: 16px;
}

.insight-text {
    color: #9eafc4;
    font-size: 14px;
    line-height: 1.7;
    margin-top: 8px;
}

.footer {
    text-align: center;
    color: #64748b;
    font-size: 12px;
    margin-top: 40px;
    padding-top: 20px;
    border-top: 1px solid #1e293b;
}

div[data-testid="stProgressBar"] > div > div > div {
    background-color: #22c55e;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# LOAD MODEL
# =========================================================
@st.cache_resource
def load_artifacts():
    preprocessor = joblib.load("preprocessor.pkl")
    model = joblib.load("model.pkl")

    # Optional: load target label encoder if it was saved
    label_encoder = None
    if os.path.exists("label_encoder.pkl"):
        label_encoder = joblib.load("label_encoder.pkl")

    return preprocessor, model, label_encoder


try:
    preprocessor, model, label_encoder = load_artifacts()

except Exception as e:
    st.error("Unable to load the prediction model.")
    st.exception(e)
    st.stop()


# =========================================================
# HERO SECTION
# =========================================================
st.markdown("""
<div class="hero">
    <div class="hero-tag">⚡ SMART MOBILITY INSIGHTS</div>
    <div class="hero-title">Is this customer ready for electric?</div>
    <div class="hero-description">
        Every customer has a different driving routine, budget and lifestyle.
        Let's understand their needs and estimate how likely they are to
        make the switch to an electric vehicle.
    </div>
</div>
""", unsafe_allow_html=True)


# =========================================================
# INPUT FORM
# =========================================================
st.markdown('<div class="section-heading">👤 Tell us about the customer</div>',
            unsafe_allow_html=True)

st.markdown(
    '<div class="section-subtitle">A few details help us understand their everyday driving experience.</div>',
    unsafe_allow_html=True
)

with st.form("ev_prediction_form"):

    # Personal details
    st.markdown("#### Personal & lifestyle")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input(
            "Customer age",
            min_value=18,
            max_value=100,
            value=30
        )

    with col2:
        gender = st.selectbox(
            "Gender",
            ["Male", "Female"]
        )

    with col3:
        income = st.number_input(
            "Annual household income (USD)",
            min_value=1000,
            value=50000,
            step=1000
        )

    col4, col5 = st.columns(2)

    with col4:
        city = st.selectbox(
            "Where do they live?",
            ["Urban", "Suburban", "Rural"]
        )

    with col5:
        cars = st.number_input(
            "Cars currently owned",
            min_value=0,
            max_value=10,
            value=1
        )

    st.markdown("---")

    # Driving profile
    st.markdown("#### 🚘 Their driving routine")

    col6, col7 = st.columns(2)

    with col6:
        commute = st.number_input(
            "Daily commute (kilometres)",
            min_value=0.0,
            value=20.0,
            step=1.0
        )

    with col7:
        current_car = st.selectbox(
            "Current vehicle",
            ["Petrol", "Diesel", "Hybrid", "Electric"]
        )

    st.markdown("---")

    # Charging
    st.markdown("#### 🔌 Charging accessibility")

    col8, col9, col10 = st.columns(3)

    with col8:
        home_station = st.number_input(
            "Charging stations near home",
            min_value=0,
            value=2
        )

    with col9:
        work_station = st.number_input(
            "Charging stations near workplace",
            min_value=0,
            value=2
        )

    with col10:
        home_charging = st.selectbox(
            "Can they charge at home?",
            ["Yes", "No"]
        )

    st.markdown("---")

    # Attitude & policy
    st.markdown("#### 🌱 Attitude & incentives")

    col11, col12 = st.columns(2)

    with col11:
        environment = st.slider(
            "Environmental concern",
            min_value=1,
            max_value=10,
            value=5,
            help="1 = Not very concerned, 10 = Extremely concerned"
        )

    with col12:
        subsidy = st.selectbox(
            "Government subsidy available?",
            ["Yes", "No"]
        )

    st.markdown("<br>", unsafe_allow_html=True)

    submitted = st.form_submit_button(
        "⚡ Analyze EV Adoption Likelihood",
        use_container_width=True
    )


# =========================================================
# PREDICTION
# =========================================================
if submitted:

    input_df = pd.DataFrame({
        "Gender": [gender],
        "City_Type": [city],
        "Current_Car_Type": [current_car],
        "Home_Charging_Possible": [home_charging],
        "Subsidy_Available": [subsidy],
        "Age": [age],
        "Annual_Income_USD": [income],
        "Daily_Commute_km": [commute],
        "Number_of_Cars_Owned": [cars],
        "Charging_Stations_Near_Home": [home_station],
        "Charging_Stations_Near_Work": [work_station],
        "Environmental_Concern_Level": [environment]
    })

    try:
        # Apply trained preprocessor
        transformed = preprocessor.transform(input_df)

        # Predict class
        prediction = model.predict(transformed)[0]

        # Predict probability if supported
        probability = None

        if hasattr(model, "predict_proba"):
            probabilities = model.predict_proba(transformed)[0]

            # Class 1 is treated as positive (EV purchase = Yes)
            classes = list(model.classes_)
            positive_index = classes.index(1) if 1 in classes else -1

            if positive_index != -1:
                probability = float(probabilities[positive_index])

        # Decode prediction
        if label_encoder is not None:
            predicted_label = label_encoder.inverse_transform([int(prediction)])[0]
            is_buyer = str(predicted_label).strip().lower() in [
                "yes", "1", "true", "will buy", "likely"
            ]
        else:
            # Assumes target encoding 0 = No and 1 = Yes
            is_buyer = int(prediction) == 1
            predicted_label = "Yes" if is_buyer else "No"

        st.markdown("---")
        st.markdown('<div class="section-heading">📊 Customer insight</div>',
                    unsafe_allow_html=True)

        if is_buyer:

            st.markdown("""
            <div class="result-card">
                <div class="result-label">Prediction</div>
                <div class="result-title" style="color:#4ade80;">
                    🟢 This customer may be ready to go electric
                </div>
                <div class="result-text">
                    Based on the information provided, this customer shows
                    characteristics associated with EV adoption in the model.
                    An electric vehicle could be worth exploring with them.
                </div>
            </div>
            """, unsafe_allow_html=True)

        else:

            st.markdown("""
            <div class="result-card">
                <div class="result-label">Prediction</div>
                <div class="result-title" style="color:#fbbf24;">
                    🟡 The customer may need more convincing
                </div>
                <div class="result-text">
                    Based on the information provided, the model does not currently
                    predict EV purchase. Their needs, budget, charging access or
                    preferences may make conventional vehicles more suitable for now.
                </div>
            </div>
            """, unsafe_allow_html=True)

        # Probability section
        if probability is not None:

            st.markdown("### EV adoption probability")

            st.metric(
                label="Estimated likelihood of buying an EV",
                value=f"{probability * 100:.1f}%"
            )

            st.progress(probability)

            if probability >= 0.70:
                st.caption("The model estimates a relatively high likelihood of EV adoption.")
            elif probability >= 0.40:
                st.caption("The model estimates a moderate likelihood of EV adoption.")
            else:
                st.caption("The model estimates a relatively low likelihood of EV adoption.")

        # Human-friendly summary
        st.markdown("""
        <div class="insight-box">
            <div class="insight-title">💬 What does this mean?</div>
            <div class="insight-text">
                This prediction is an estimate based on patterns learned from the
                training dataset. It is not a guarantee of what this person will
                purchase. Real decisions also depend on vehicle price, battery
                performance, family needs, brand preference and other factors.
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Customer profile summary
        st.markdown("### Customer profile summary")

        summary1, summary2, summary3, summary4 = st.columns(4)

        summary1.metric("Age", f"{age} years")
        summary2.metric("Daily travel", f"{commute:g} km")
        summary3.metric("Current vehicle", current_car)
        summary4.metric("Home charging", home_charging)

        with st.expander("View submitted customer data"):
            st.dataframe(input_df, use_container_width=True)

    except Exception as e:
        st.error("Something went wrong while making the prediction.")
        st.exception(e)


# =========================================================
# FOOTER
# =========================================================
st.markdown("""
<div class="footer">
    VOLTWISE · EV ADOPTION INTELLIGENCE<br>
    Built with Machine Learning · This tool provides estimates, not purchase guarantees.
</div>
""", unsafe_allow_html=True)