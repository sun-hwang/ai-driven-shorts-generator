# VVS Generator 🎥✨

## Overview 🌐
**VVS Generator** is a cutting-edge web application enabling users to generate short videos from textual inputs. Powered by the formidable GPT-4 for story generation and a sophisticated diffusion model for image creation, it brings textual stories to life in a visually stunning format.

## How it Works 🛠️
### Story Generation 📜
Upon receiving user input, a concise three-sentence story is crafted using GPT-4 and saved as a text file.
- **Code File**: `main.py`
- **HTML Template**: `index.html`

## Setup and Configuration ⚙️

### Installation 📥
Before diving in, ensure **Python** is installed on your system. Subsequently, the necessary Python packages, such as Flask, torch, and diffusers need to be set up.

#### Installing Dependencies 🔗
Use the following commands in your terminal or command prompt to install the requisite packages:
```bash
pip install Flask torch diffusers
pip install openai moviepy Pillow
```

#### API Keys 🔐
Your OpenAI API key needs to be placed in the config.py file as shown:

~
API_KEYS = {
    'openai': 'PUT_YOUR_API_KEY_HERE'
}
~
Code File: config.py

#### Running the Application 🚀
Execute the following command to get the app up and running:

```
python main.py
```

This kickstarts the Flask application. You can then access the web interface by heading to http://localhost:5000 on your web browser.

Usage 🖱️
Once on the web interface, input your text into the provided area and hit "Generate Video". The application will then weave a story, spawn images, morph them into a video, and showcase it on the webpage.

Note: Ensure to substitute 'PUT_YOUR_API_KEY_HERE' with your actual OpenAI API key to ensure the application operates seamlessly.
