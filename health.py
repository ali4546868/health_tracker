import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Initialize session state for data persistence
if "health_data" not in st.session_state:
    st.session_state["health_data"] = pd.DataFrame(columns=["Date", "Weight (kg)", "Steps", "Calories Burned", "Exercise Duration (mins)"])

# Sidebar for data input
st.sidebar.header("Log Your Daily Health Data")

def log_data():
    date = st.sidebar.date_input("Date")
    weight = st.sidebar.number_input("Weight (kg)", min_value=0.0, step=0.1, format="%.1f")
    steps = st.sidebar.number_input("Steps", min_value=0, step=100)
    calories = st.sidebar.number_input("Calories Burned", min_value=0, step=50)
    exercise = st.sidebar.number_input("Exercise Duration (mins)", min_value=0, step=5)

    if st.sidebar.button("Add Data"):
        new_data = {"Date": [date], "Weight (kg)": [weight], "Steps": [steps], "Calories Burned": [calories], "Exercise Duration (mins)": [exercise]}
        new_df = pd.DataFrame(new_data)
        st.session_state["health_data"] = pd.concat([st.session_state["health_data"], new_df], ignore_index=True)
        st.success("Data added successfully!")

log_data()

# Main app area
st.title("Health Tracker Dashboard")

# Show logged data
if not st.session_state["health_data"].empty:
    st.subheader("Your Logged Data")
    st.dataframe(st.session_state["health_data"], use_container_width=True)

    # Plot data visualizations
    st.subheader("Data Visualizations")

    # Weight trend
    st.write("### Weight Trend")
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=st.session_state["health_data"], x="Date", y="Weight (kg)", marker="o")
    plt.xticks(rotation=45)
    plt.title("Weight Trend Over Time")
    st.pyplot(plt)

    # Steps and Calories Burned
    st.write("### Steps and Calories Burned")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=st.session_state["health_data"], x="Date", y="Steps", marker="o", label="Steps")
    sns.lineplot(data=st.session_state["health_data"], x="Date", y="Calories Burned", marker="o", label="Calories Burned")
    plt.xticks(rotation=45)
    plt.title("Steps and Calories Burned Over Time")
    ax.legend()
    st.pyplot(fig)

    # Exercise Duration
    st.write("### Exercise Duration")
    plt.figure(figsize=(10, 5))
    sns.barplot(data=st.session_state["health_data"], x="Date", y="Exercise Duration (mins)", color="blue")
    plt.xticks(rotation=45)
    plt.title("Exercise Duration Per Day")
    st.pyplot(plt)
else:
    st.info("No data logged yet. Use the sidebar to log your health data.")

# Reset button
if st.button("Reset Data"):
    st.session_state["health_data"] = pd.DataFrame(columns=["Date", "Weight (kg)", "Steps", "Calories Burned", "Exercise Duration (mins)"])
    st.success("All data has been reset!")
