import streamlit as st

import datetime


st.set_page_config(page_title="Growth Mindset Challenge", layout="wide")


st.title("🚀 Growth Mindset Challenge")
st.subheader("Develop, Learn, and Grow with a Positive Mindset")

st.markdown(
    """
    **A growth mindset** is the belief that abilities and intelligence can be developed with hard work, perseverance, and learning from mistakes.
    Let's take on this challenge and improve ourselves daily! 🌱  
    """
)


st.sidebar.header("Your Growth Tracker")
name = st.sidebar.text_input("Enter Your Name", placeholder="John Doe")
goal = st.sidebar.text_area("What’s your current learning goal?", placeholder="I want to improve in Python and algorithms.")
progress = st.sidebar.slider("How much progress have you made?", 0, 100, 50)

if st.sidebar.button("Save Progress"):
    st.sidebar.success(f"✅ Progress saved! Keep going, {name}!")


quotes = [
    "“Success is not an accident, success is a choice.” – Stephen Curry",
    "“The only way to do great work is to love what you do.” – Steve Jobs",
    "“Don’t let what you cannot do interfere with what you can do.” – John Wooden",
]
import random
st.sidebar.markdown(f"📢 **Motivational Quote:** *{random.choice(quotes)}*")


st.header("💡 Growth Mindset Principles")
st.markdown(
    """
    - **Embrace Challenges**: View obstacles as opportunities to learn rather than as setbacks.
    - **Learn from Mistakes**: Making mistakes is a natural part of learning.
    - **Persist Through Difficulties**: Stay determined, even when things get tough.
    - **Celebrate Effort**: Reward yourself for progress, not just results.
    - **Keep an Open Mind**: Stay curious and be willing to adapt.
    """
)


st.header("📖 Reflect on Your Journey")
reflection = st.text_area("What did you learn today?", placeholder="Write about your experiences, successes, or challenges...")
if st.button("Save Reflection"):
    today = datetime.date.today()
    st.success(f"✅ Reflection saved for {today}!")

st.header("🙌 Community Support")
st.markdown(
    """
    Join our community of learners!  
    - **WhatsApp Group:** [Click here to join](#)  
    - **Submit Your Challenge:** [Google Form](https://forms.gle/tS7C3sr55tUZ36GY8)  
    """
)

# Footer
st.markdown("---")
st.markdown("📌 *Stay committed to learning and growth!  by Umema Sultan*")