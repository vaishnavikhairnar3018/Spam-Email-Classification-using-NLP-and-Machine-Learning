import streamlit as st
import pickle

# Load the trained model and vectorizer
model = pickle.load(open('spam.pkl', 'rb'))
cv = pickle.load(open('vectorizer.pkl', 'rb'))

# Define the main function
def main():
    # Page configuration
    st.set_page_config(page_title="Email Spam Classification", layout="centered")
    
    # Custom dark mode CSS
    st.markdown(
        """
        <style>
        body {
            background-color: #121212;
            color: #ffffff;
        }
        .stApp {
            background-color: #121212;
            color: #ffffff;
        }
        .stTextArea textarea {
            background-color: #1e1e1e;
            color: #ffffff;
            border: 1px solid #4caf50;
            font-size: 16px;
        }
        .stButton button {
            background-color: #4caf50;
            color: white;
            font-size: 16px;
            border-radius: 5px;
        }
        .stButton button:hover {
            background-color: #66bb6a;
        }
        .stAlert {
            background-color: #1e1e1e;
            color: #ffffff;
            border-left: 4px solid #4caf50;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    # Title and description
    st.title("📧 Email Spam Classification Application")
    st.write("This is a **Machine Learning** application to classify emails as spam or ham.")
    
    # Subheader
    st.subheader("Classification")
    user_input = st.text_area("Enter an email to classify:", height=150, placeholder="Type your email content here...")
    
    # Button for classification
    if st.button("Classify"):
        if user_input:
            # Preprocess and predict
            data = [user_input]
            vec = cv.transform(data).toarray()
            result = model.predict(vec)

            # Display result
            if result[0] == 0:
                st.success("✅ This is Not A Spam Email", icon="✔️")
            else:
                st.error("🚨 This is A Spam Email", icon="⚠️")
        else:
            st.warning("⚠️ Please enter an email to classify!")

# Run the main function
if __name__ == "__main__":
    main()
