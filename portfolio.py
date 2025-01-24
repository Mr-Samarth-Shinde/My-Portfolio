import streamlit as st
from PIL import Image
import plotly.express as px
import base64

# Page Configuration
st.set_page_config(page_title="Samarth's Portfolio", layout="wide")

# Personal Information
profile = "sam01.jpg"  # Replace with your profile image
Name = "Samarth Shinde"
description = "Data Science Enthusiast"
email = "samshinde6369@gmail.com"
phone = "7522953494"
linkedin = "https://www.linkedin.com/in/samarthshinde01"
resume_file = "Samarth-Resume.docx"  # Replace with your resume file

# Work Experience
Work_Experience = [
    {
        "Position": "Data Analyst Intern",
        "Company": "British Airways",
        "Duration": "4 Hours Virtual Internship",
        "Description": "Analyzed data, built predictive models, and visualized insights to aid business decisions."
    }
]

# Skills
Skills = [
    "Data Science", "Machine Learning", "Data Analytics",
    "Data Visualization", "Pandas", "Excel", "Power BI"
]

# Projects
Projects = [
    {
        "Name": "Movie Recommendation System",
        "Description": "Developed a movie recommendation system using Python and Scikit-learn.",
        "Demo": "https://example.com/movie-recommendation-demo"
    },
    {
        "Name": "Stock Prediction System",
        "Description": "Built a stock prediction system with LSTM neural networks and TensorFlow.",
        "Demo": "https://example.com/stock-prediction-demo"
    }
]

# Function to Add Resume Download Button
def add_resume_button(resume_path):
    with open(resume_path, "rb") as file:
        resume_data = file.read()
    b64 = base64.b64encode(resume_data).decode()
    href = f'<a href="data:application/pdf;base64,{b64}" download="Samarth_Shinde_Resume.pdf">📄 Download My Resume</a>'
    st.markdown(href, unsafe_allow_html=True)

# Sidebar
st.sidebar.image(profile, width=150, caption="Samarth Shinde")
st.sidebar.title("Contact Me")
st.sidebar.write(f"📧 Email: {email}")
st.sidebar.write(f"📞 Phone: {phone}")
st.sidebar.write(f"🔗 [LinkedIn]({linkedin})")
st.sidebar.markdown("---")
st.sidebar.write("Looking for a detailed overview?")
add_resume_button(resume_file)

# Header Section
st.title("Welcome to My Portfolio!")
st.write(
    f"Hello! I'm **{Name}**, a passionate Data Science enthusiast specializing in analyzing and visualizing data, "
    "developing predictive models, and creating impactful projects."
)

# Work Experience Section
st.header("📂 Work Experience")
for job in Work_Experience:
    with st.container():
        st.subheader(f"**{job['Position']}**")
        st.write(f"**{job['Company']}** | *{job['Duration']}*")
        st.write(job["Description"])
        st.markdown("---")

# Skills Section
st.header("🛠️ Skills")
skill_data = {
    "Skill": Skills,
    "Proficiency (%)": [90, 85, 88, 80, 92, 75, 80]
}
fig = px.bar(skill_data, x="Skill", y="Proficiency (%)", title="Skill Proficiency", color="Proficiency (%)", text="Proficiency (%)")
fig.update_layout(xaxis_title="Skills", yaxis_title="Proficiency (%)", template="plotly_white")
st.plotly_chart(fig, use_container_width=True)

# Projects Section
st.header("📚 Projects")
for project in Projects:
    with st.container():
        st.subheader(f"**{project['Name']}**")
        st.write(project["Description"])
        if project["Demo"]:
            st.markdown(f"[🔗 View Demo]({project['Demo']})", unsafe_allow_html=True)
        st.markdown("---")

# Interactive Section: Feedback Form
st.header("💬 Share Your Feedback")
with st.form(key="feedback_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    feedback = st.text_area("Your Feedback")
    submit_button = st.form_submit_button(label="Submit")
    if submit_button:
        st.success(f"Thank you, {name}! Your feedback has been received.")

# Footer Section
st.markdown("---")
st.write(
    f"**Portfolio Created by {Name}** | [LinkedIn]({linkedin}) | [Email Me](mailto:{email})"
)
