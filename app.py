import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


from services.weather_api import get_weather
from services.groq_service import ask_groq


from utils.analyzer import analyze_water_risk
from utils.water_score import (
    calculate_water_score,
    get_stress_level
)



# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="AI Water Crisis Manager",
    page_icon="💧",
    layout="wide"
)



# =====================================================
# TITLE
# =====================================================

st.title(
    "💧 AI Water Crisis Manager"
)


st.write(
    "AI-powered water shortage prediction and management system for Pakistan"
)



# =====================================================
# USER INPUT
# =====================================================

city = st.text_input(
    "Enter City Name",
    "Khanpur"
)



user_type = st.selectbox(
    "Choose User Category",
    [
        "🌱 Farmer",
        "🏠 Household",
        "🏛️ Government Officer"
    ]
)



# =====================================================
# ANALYSIS BUTTON
# =====================================================

if st.button("Analyze Water Crisis"):
    with st.spinner(
        "Analyzing water conditions..."
        ):


        # Weather Agent

        weather = get_weather(city)

        # Check Weather API response
        if "error" in weather:
            if "city not found" in weather["error"].lower():
                st.warning(
                    "⚠️ City not found. Please check spelling and try again."
                )
                st.info(
            "Examples: Lahore, Islamabad, Murree, Karachi, Multan"
            )
            else:
                st.error(
                    f"Weather API Error: {weather['error']}"
                )
            st.stop()




        # Risk Agent

        risk = analyze_water_risk(weather)



        # Water Intelligence Score

        water_score = calculate_water_score(
            weather,
            risk
        )



        stress = get_stress_level(
            water_score
        )



        # =====================================================
        # AI RECOMMENDATION AGENT
        # =====================================================


        prompt = f"""

You are an AI Water Management Expert for Pakistan.


User Category:
{user_type}


Location:
{city}


Weather Data:
{weather}


Risk Analysis:
{risk}


Water Crisis Score:
{water_score}%


Stress Level:
{stress}


Generate practical water management solutions.


Rules:

Farmer:
- irrigation methods
- crop suggestions
- soil moisture
- water saving


Household:
- daily conservation
- recycling
- storage


Government Officer:
- policies
- infrastructure
- planning


Use simple understandable language.

"""


        recommendation = ask_groq(prompt)



    # =====================================================
    # CURRENT WEATHER
    # =====================================================


    st.subheader(
        "🌦️ Current Weather Conditions"
    )


    col1, col2, col3 = st.columns(3)



    with col1:

        st.metric(
            "🌡 Temperature",
            f"{weather['temperature']} °C"
        )



    with col2:

        st.metric(
            "💧 Humidity",
            f"{weather['humidity']} %"
        )



    with col3:

        rainfall_text = (
            f"{weather['rainfall']} mm"
            if weather["rainfall"] > 0
            else "0 mm (Dry)"
            )
        st.metric(
            "🌧 Rainfall",
            rainfall_text
            )



    # =====================================================
    # WEATHER ANALYTICS DASHBOARD
    # =====================================================


    st.subheader(
        "📈 Weather Analytics Dashboard"
    )



    col1, col2, col3 = st.columns(3)



    # ---------------- Temperature Gauge ----------------


    with col1:


        temp_fig = go.Figure(

            go.Indicator(

                mode="gauge+number",

                value=weather["temperature"],


                title={
                    "text":"🌡 Temperature"
                },


                gauge={

                    "axis":{
                        "range":[0,50]
                    },


                    "steps":[

                        {
                            "range":[0,25],
                            "color":"lightgreen"
                        },

                        {
                            "range":[25,35],
                            "color":"yellow"
                        },

                        {
                            "range":[35,50],
                            "color":"red"
                        }

                    ]

                }

            )

        )


        st.plotly_chart(
            temp_fig,
            use_container_width=True
        )



    # ---------------- Humidity Gauge ----------------


    with col2:


        humidity_fig = go.Figure(

            go.Indicator(

                mode="gauge+number",

                value=weather["humidity"],


                title={
                    "text":"💧 Humidity"
                },


                gauge={

                    "axis":{
                        "range":[0,100]
                    },


                    "steps":[

                        {
                            "range":[0,30],
                            "color":"red"
                        },

                        {
                            "range":[30,60],
                            "color":"yellow"
                        },

                        {
                            "range":[60,100],
                            "color":"lightgreen"
                        }

                    ]

                }

            )

        )


        st.plotly_chart(
            humidity_fig,
            use_container_width=True
        )



    # ---------------- Rainfall ----------------


    with col3:


        rainfall_fig = go.Figure(

            go.Indicator(

                mode="gauge+number",

                value=weather["rainfall"],


                title={
                    "text":"🌧 Rainfall (mm)"
                }

            )

        )


        st.plotly_chart(
            rainfall_fig,
            use_container_width=True
        )
    # =====================================================
    # WEATHER COMPARISON GRAPH
    # =====================================================

    st.caption(
        "📊Real-time comparison of temperature, humidity and rainfall"
        )


    weather_df = pd.DataFrame({
        "Parameter": [
        "Temperature",
        "Humidity",
        "Rainfall"
        ],
        "Value": [
            weather["temperature"],
            weather["humidity"],
            weather["rainfall"]
        ]
    })


    # Horizontal Bar Chart

    weather_chart = px.bar(
        
        weather_df,
        
        x="Value",
        
        y="Parameter",
        
        orientation="h",
        
        text="Value",
        
        title="🌦 Current Weather Statistics",
        
        color="Parameter"
        )


    weather_chart.update_traces(
        textposition="outside"
        )
    
    weather_chart.update_layout(
        
        height=350,
        
        title_x=0.5,
        
        template="plotly_white",
        
        xaxis_title="Measurement",
        
        yaxis_title=""
        )
    
    st.plotly_chart(
        
        weather_chart,
        use_container_width=True
        )



    # =====================================================
    # WATER CRISIS INTELLIGENCE SCORE
    # =====================================================


    st.subheader(
        "💧 Water Crisis Intelligence Score"
    )



    st.progress(

        water_score / 100

    )



    st.metric(

        "Water Stress Score",

        f"{water_score}%"

    )



    # =====================================================
    # WATER STRESS GAUGE
    # =====================================================


    score_fig = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=water_score,


            title={
                "text":
                "Water Crisis Intelligence Score"
            },


            gauge={


                "axis":{

                    "range":[0,100]

                },


                "steps":[

                    {

                        "range":[0,40],

                        "color":"lightgreen"

                    },


                    {

                        "range":[40,70],

                        "color":"yellow"

                    },


                    {

                        "range":[70,100],

                        "color":"red"

                    }

                ]

            }

        )

    )



    st.plotly_chart(

        score_fig,

        use_container_width=True

    )



    st.info(

        stress

    )



    # =====================================================
    # CRISIS STATUS
    # =====================================================


    if water_score >= 75:


        st.error(

            "🚨 CRITICAL WATER CRISIS RISK"

        )


    elif water_score >= 50:


        st.warning(

            "⚠️ MODERATE WATER RISK"

        )


    else:


        st.success(

            "🟢 LOW WATER RISK"

        )




    # =====================================================
    # RISK FACTORS
    # =====================================================


    st.subheader(

        "📌 Risk Factors"

    )



    for item in risk["recommendations"]:


        st.warning(

            item

        )



    # =====================================================
    # AI WATER MANAGEMENT PLAN
    # =====================================================


    st.subheader(

        "🤖 AI Water Management Plan"

    )



    st.markdown(

        recommendation

    )