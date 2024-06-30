# Hand Gesture Drawing and AI Interaction

This project uses computer vision to detect hand gestures and draw on a canvas. It also integrates with an AI model to generate responses based on the drawing.

## Features

- Hand gesture detection using the `cvzone` library.
- Drawing on a canvas based on hand gestures.
- Interaction with an AI model to generate responses based on the drawing.
- Web interface using `streamlit`.

## Installation

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/lvimuth/Hand-Gesture-Drawing-and-AI-Interaction.git
   cd Hand-Gesture-Drawing-and-AI-Interaction
   ```

2. **Create and Activate a Virtual Environment:**
   ```sh
   python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
   ```

3. **Install the Required Packages:**
   ```sh
    pip install -r requirements.txt
   ```
## Usage

1. **Run the Streamlit Application:**

```sh
    streamlit run main.py
```

2. **Use the Web Interface:**
   
 - Check the "Run" checkbox to start the video capture and hand tracking.
 - Use hand gestures to draw on the canvas:
 - Point with your index finger to draw.
 - how all five fingers to clear the canvas.
 - The AI model will generate responses based on the drawing and display them in the "Answer" section.

## Project Structure

  - main.py: The main script to run the Streamlit web application.
  - draw.py: Contains the drawing logic based on hand gestures.
  - sendToAI.py: Handles the interaction with the AI model.
  - requirements.txt: Lists the required Python packages for the project.
