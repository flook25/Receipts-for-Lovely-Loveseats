import streamlit as st

# --- Page Configuration ---
# Set the page title and icon for the browser tab
st.set_page_config(
    page_title="My Professional Portfolio",
    page_icon="✨", # You can use an emoji as an icon
    layout="centered" # Can be "centered" or "wide"
)

# --- Header Section ---
st.title("Welcome to My Portfolio! 👋")
st.write("---") # A horizontal line for visual separation

# You can add a profile picture. Replace with your own image URL or local path.
# If using a local path, make sure the image is in the same directory as your script
# or provide the full path.
# Example using a placeholder image:
st.image("https://placehold.co/150x150/000000/FFFFFF?text=Your+Photo", width=150)
st.header("John Doe") # Replace with your name
st.subheader("Data Scientist | Web Developer | AI Enthusiast") # Replace with your profession/tagline

st.write(
    """
    Hello! I'm John Doe, a passionate professional with expertise in data science, web development,
    and artificial intelligence. I love building innovative solutions and exploring new technologies.
    This portfolio showcases some of my work and skills.
    """
)

# Add a link to your LinkedIn or GitHub
st.markdown(
    """
    [LinkedIn Profile](https://www.linkedin.com/in/yourprofile) |
    [GitHub Repository](https://github.com/yourusername)
    """
)
st.write("---")

# --- About Me Section ---
st.header("About Me")
st.write(
    """
    I have a strong background in analytical problem-solving and a keen interest in leveraging
    technology to create impactful applications. My journey into tech began with a curiosity
    for how data can tell stories, leading me to specialize in machine learning and data visualization.
    I am always eager to learn and contribute to projects that make a difference.
    """
)
st.write("---")

# --- Projects Section ---
st.header("My Projects")
st.write("Here are some of the projects I've worked on:")

# Project 1
st.subheader("Project 1: Predictive Analytics Dashboard")
st.write("Built a Streamlit dashboard to visualize and predict customer churn using machine learning models.")
st.markdown("Technologies: `Python`, `Pandas`, `Scikit-learn`, `Streamlit`, `Plotly`")
# You can add a link to the project's GitHub repo or a live demo
st.markdown("[View Project on GitHub](https://github.com/yourusername/project1)")
st.write("---")

# Project 2
st.subheader("Project 2: E-commerce Recommendation System")
st.write("Developed a collaborative filtering recommendation system for an online retail platform.")
st.markdown("Technologies: `Python`, `Surprise`, `Flask`, `PostgreSQL`")
st.markdown("[View Project on GitHub](https://github.com/yourusername/project2)")
st.write("---")

# Project 3 (You can add more projects)
st.subheader("Project 3: Personal Blog Website")
st.write("Created a responsive personal blog using modern web development frameworks.")
st.markdown("Technologies: `React`, `Node.js`, `MongoDB`, `Tailwind CSS`")
st.markdown("[View Project on GitHub](https://github.com/yourusername/project3)")
st.write("---")

# --- Skills Section ---
st.header("Skills")

# Using columns for a more organized display of skills
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Programming Languages")
    st.markdown("- Python")
    st.markdown("- JavaScript")
    st.markdown("- SQL")
    st.markdown("- R")

with col2:
    st.subheader("Libraries & Frameworks")
    st.markdown("- Pandas, NumPy")
    st.markdown("- Scikit-learn, TensorFlow, Keras")
    st.markdown("- Streamlit, Dash")
    st.markdown("- React, Node.js")

with col3:
    st.subheader("Tools & Platforms")
    st.markdown("- Git, GitHub")
    st.markdown("- Docker")
    st.markdown("- AWS, Google Cloud")
    st.markdown("- VS Code")

st.write("---")

# --- Contact Section ---
st.header("Contact Me")
st.write("Feel free to reach out if you have any questions or opportunities!")

# Simple contact form (Streamlit doesn't handle backend, so this is just for display)
# For a functional form, you'd integrate with a service like Formspree or build a backend.
contact_form = """
<form action="https://formspree.io/f/your_form_id" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your Name" required style="width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc;">
    <input type="email" name="email" placeholder="Your Email" required style="width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc;">
    <textarea name="message" placeholder="Your Message" required style="width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc; height: 150px;"></textarea>
    <button type="submit" style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;">Send</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)

# You can also just provide your email directly
st.write("Or email me directly at: your.email@example.com")
st.write("---")

# --- Footer ---
st.write("© 2025 John Doe. All rights reserved.")
