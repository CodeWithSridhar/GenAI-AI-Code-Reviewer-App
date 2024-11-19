import streamlit as st
import google.generativeai as ai

# Configure API Key
key = "AIzaSyDrt9sLDzhY7qm_noqxckAaQPFB3DYs-5U"
ai.configure(api_key=key)

# App Title and Description
st.set_page_config(page_title="Code Reviewer", layout="wide")
st.title("🔍 AI-Powered Code Reviewer")
st.write("""
    Enter your Python code snippet below, and our AI will debug it for you. 
    Get clean, correct, and professional code effortlessly!
""")

# Sidebar for Inputs
with st.sidebar:
    st.header("⚙️ Settings")
    st.write("Configure the AI Debugging Tool:")
    model_name = st.selectbox("Select Model", options=["gemini-1.5-flash"], index=0)
    prompt = st.text_area(
        "Custom Prompt",
        value="The following Python code has an error. Debug it and give me a correct code.",
        help="You can customize the instructions to the AI for debugging."
    )
    st.info("Default model is `gemini-1.5-flash`. Prompt can be modified.")

# Main Section
code_snippet = st.text_area(
    "📜 Enter Your Python Code Here:",
    placeholder="Paste your Python code...",
    height=200
)

# Submit Button
if st.button("✨ Debug Code"):
    if not code_snippet.strip():
        st.error("Please enter a code snippet to debug.")
    else:
        try:
            # Call the AI model for debugging
            model = ai.GenerativeModel(model_name=model_name)
            response = model.generate_content([code_snippet, prompt])

            # Display Results
            st.success("✅ Debugging Complete!")
            st.subheader("🔧 Fixed Code")
            st.code(response.text, language="python")

        except Exception as e:
            st.error(f"An error occurred: {e}")

# Footer
st.markdown("---")
st.caption("Powered by Google Generative AI")
