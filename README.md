**VVS Generator**

Overview
VVS Generator is a web application that allows users to generate short videos based on textual input. The application utilizes GPT-4 for story generation and a diffusion model for image generation, which are then converted into a short video.

How it Works
Story Generation: Upon receiving user input, a story is generated using GPT-4. The story is created in three sentences and saved as a text file.

Code File: main.py
HTML Template: index.html

**Setup and Configuration**

Installation
Before running the VVS Generator, ensure that you have Python installed on your system. Then, you need to install the necessary Python packages, which include Flask, torch, and diffusers.

Installing Dependencies
To install the necessary packages, you can use the following commands in your terminal or command prompt:

pip install Flask torch diffusers
pip install openai moviepy Pillow

API Keys
You need to provide your OpenAI API key in the config.py file:
API_KEYS = {
    'openai': 'PUT_YOUR_API_KEY_HERE'
}
Code File: config.py

**Running the Application**

To run the application, execute the following command:
python main.py
This will start the Flask application, and you can access the web interface by navigating to http://localhost:5000 in your web browser.

Usage
Navigate to the web interface, enter your text in the provided text area, and click "Generate Video". The application will create a story, generate images, convert them into a video, and display it on the webpage.

Note: Ensure to replace 'PUT_YOUR_API_KEY_HERE' with your actual OpenAI API key for the application to function correctly.
