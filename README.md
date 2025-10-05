# AI Summarizer Project

This project is a simple AI summarizer that utilizes the Hugging Face Transformers library to summarize text input. It includes a command-line application and a Streamlit web application for user interaction.

## Project Structure

```
ai-bot
├── app.py              # Core functionality for text summarization
├── streamlit_app.py    # Streamlit web application interface
├── requirements.txt     # Dependencies for the project
└── README.md           # Project documentation
```

## Installation

1. **Install Dependencies**:
   Ensure you have Python installed. Then, create a virtual environment and install the required packages. You can do this by running:
   ```
   pip install -r requirements.txt
   ```

## Running the Streamlit Application

1. **Create `streamlit_app.py`**:
   This file sets up the Streamlit interface for the application.

2. **Run the Streamlit Application**:
   You can run the Streamlit app by executing the following command in your terminal:
   ```
   streamlit run streamlit_app.py
   ```

3. **Access the Application**:
   After running the command, Streamlit will provide a local URL (usually `http://localhost:8501`) where you can access your web application.

## Usage

- Open the Streamlit application in your web browser.
- Paste a news article or blog text into the text area.
- Click the "Summarize" button to generate a summary of the text.
- The summary will be displayed below the input area.

## Dependencies

- `streamlit`: For creating the web application interface.
- `transformers`: For utilizing the AI model for text summarization.

## License

This project is licensed under the MIT License.