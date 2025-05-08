# simple-llm-chatbot-ollama
A simple chatbot built with a local LLM using Ollama. Easily run conversational AI on your machine without cloud dependencies.

Summary of Steps:
1.	Install Ollama on your respective OS.: Ollama is used to run large language models (LLMs) locally on your computer
2.	Install Llama 3.2 using ollama pull llama3.2.
3.	Install Python and the ollama ,Streamlit  Python client.
4.	Build a chatbot in Python by interacting with the Llama 3.2 model.
5.	Optionally, extend the chatbot for web-based deployment using Flask or other platforms.

1 . Install Ollama on your respective OS.
            Check out the platform https://ollama.com/download  to download ollama
    Once installed , Make sure its up and running
            For windows , run the set up file. And run the application .
           
2. Install Llama 3.2 Model
Once you have Ollama installed, you need to download the Llama 3.2 model for your chatbot. Run the following command:
        ollama pull llama3.2
Run the command using terminal.

This command will download the Llama 3.2 model to your system, making it ready for local use.
3. Install Python and Required Libraries 
Make sure you have Python installed on your system (preferably version 3.8 or higher). You will also need to install the ollama Python client and Streamlit for building the web-based chatbot.
•	Then, install the necessary Python libraries:
        pip install ollama streamlit
This installs the ollama Python client for interacting with the Llama model, and Streamlit for building the web interface.
4. Create python env and activate in command prompt:
	python -m venv chatbot
	chatbot\Scripts\activate 
5. Build a Chatbot in Python with Llama 3.2
Create a Python script to interact with the Llama 3.2 model. Here’s a simple chatbot script using the ollama client and Streamlit to create a web-based chatbot.
1.	Create a Python file, e.g., chatbot.py.
2.	Use the chatbot.py code to interact with the Llama 3.2 model and display the conversation on the Streamlit interface:
3.      Run the chatbot app:

        streamlit run chatbot.py
        Load http://localhost:8501/
