import streamlit as st
import ollama

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Chatbot", "Stress Tips", "Anxiety Relief", "Yoga & Meditation", "Vitamins & Minerals"])

# Function to handle user input
def handle_input():
    user_input = st.session_state.chat_input  # Get input
    if user_input:
        response = ollama.chat(model="llama3.2", messages=[{"role": "user", "content": user_input}])
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.session_state.messages.append({"role": "assistant", "content": response['message']['content']})
    
    # Clear input field safely
    st.session_state.chat_input = ""

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Home Page - AI Chatbot
if page == "Chatbot":
    st.title("AI Chatbot for Stress & Anxiety")
    st.write("Ask anything about stress, anxiety, and mental wellness!")

    # Input field with ENTER-to-send functionality
    st.text_input("Type your message:", key="chat_input", on_change=handle_input)

    # Display chat history
    for message in st.session_state.messages:
        role = "**You:**" if message["role"] == "user" else "**AI:**"
        st.markdown(f"{role} {message['content']}")

# Stress Management Tips Page
elif page == "Stress Tips":
    st.title("Stress Management Tips")
    st.markdown("""
    - **Exercise regularly** 🏃‍♂️  
    - **Practice deep breathing** 🧘‍♀️  
    - **Take breaks and rest** 😴  
    - **Stay connected with loved ones** ❤️  
    - **Listen to calming music** 🎵  
    """)

# Anxiety Relief Page
elif page == "Anxiety Relief":
    st.title("Anxiety Relief Strategies")
    st.markdown("""
    - **Try mindfulness meditation**  
    - **Limit caffeine and sugar intake**  
    - **Use positive affirmations**  
    - **Engage in a relaxing hobby**  
    - **Seek professional help if needed**  
    """)

# Yoga & Meditation Page
elif page == "Yoga & Meditation":
    st.title("Yoga & Meditation")
    st.markdown("""
    - **Child’s Pose (Balasana)**  
    - **Cat-Cow Stretch**  
    - **Legs-Up-The-Wall Pose**  
    - **Corpse Pose (Shavasana)**  
    - **Seated Forward Bend**  
    """)

    st.write("Try **guided meditation** for relaxation:")
    st.video("https://www.youtube.com/watch?v=inpok4MKVLM")  # Example meditation video

# Vitamins & Minerals Page
elif page == "Vitamins & Minerals":
    st.title("Vitamins, Minerals, and Their Deficiency Diseases")
    st.markdown("""
    | **Nutrient**      | **Function**                               | **Deficiency Disease**         |
    |------------------|--------------------------------|--------------------------------|
    | **Vitamin A**   | Vision, immune function       | Night blindness, Xerophthalmia |
    | **Vitamin B1**  | Energy metabolism             | Beriberi                         |
    | **Vitamin B2**  | Growth, red blood cell production | Ariboflavinosis              |
    | **Vitamin B3**  | Digestion, skin health        | Pellagra                        |
    | **Vitamin B12** | Nervous system, red blood cells | Pernicious anemia           |
    | **Vitamin C**   | Antioxidant, immune function  | Scurvy                           |
    | **Vitamin D**   | Bone health, calcium absorption | Rickets, Osteomalacia       |
    | **Vitamin E**   | Antioxidant, skin health      | Nerve and muscle damage        |
    | **Vitamin K**   | Blood clotting                | Excessive bleeding             |
    | **Calcium**     | Bone strength, muscle function | Osteoporosis                   |
    | **Iron**        | Oxygen transport in blood     | Anemia                           |
    | **Iodine**      | Thyroid function              | Goiter                           |
    | **Zinc**        | Immune function, wound healing | Growth retardation, hair loss |
    """)

st.sidebar.markdown("Be Healthy ❤️")