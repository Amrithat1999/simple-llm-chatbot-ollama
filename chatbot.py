import streamlit as st
import ollama
# Function to generate a response from the LLM using ollama
def generate_llm_response(prompt, model = "llama3.2"):
    """
    Generate a response from a large language model using ollama.
    Args:
        prompt (str): The input prompt for the model.
        model (str): The model to use (default is llama2).
        temperature (float): Sampling temperature for the model. Higher values make output more random.
    Returns:
        str: Generated text from the model.
    """
    messages = [
            {
                'role': 'user',
                'content': prompt,
            }
        ]
   
    response = ollama.chat(model=model, messages=messages)
    return response['message']['content']
# Streamlit application layout
st.title("LLM Text Generator")
st.write("Interact with a Large Language Model (LLM) and generate responses.")

# Text input for the user prompt
user_prompt = st.text_area("Enter your prompt:")

# Button to generate the response
if st.button("Generate Response"):
    if user_prompt.strip() != "":
        with st.spinner("Generating response..."):
            try:
                # Generate the response from the LLM
                response = generate_llm_response(user_prompt)
                st.success("Response generated!")
                st.text_area("LLM Response:", value=response, height=200)
            except Exception as e:
                st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter a prompt.")
