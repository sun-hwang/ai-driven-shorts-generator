# VVS Generator 🎥✨

## Overview 🌐
**VVS Generator** is a cutting-edge web application enabling users to generate short videos from textual inputs. Powered by the formidable GPT-4 for story generation and a sophisticated diffusion model for image creation, it brings textual stories to life in a visually stunning format.

![image](https://github.com/sun-hwang/vvs_generator/assets/146854712/05245396-47cb-4455-8072-1bac440de167)

<iframe width="560" height="315" src="https://www.youtube.com/embed/NdxJA0li79U?si=hRqePeW3oj8mywDj" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    

## How it Works 🛠️
### Story Generation 📜
Upon receiving user input, a concise three-sentence story is crafted using GPT-4 and saved as a text file.
- **Code File**: [`main.py`](https://github.com/sun-hwang/vvs_generator/blob/64ffc491965ca11ea8db6f780734892107f886ee/main.py)
- **HTML Template**: [`index.html`](https://github.com/sun-hwang/vvs_generator/blob/0c398f64c3b685491ef3247a225610a3b183f892/templates/index.html)

## Setup and Configuration ⚙️

### Installation 📥
Before diving in, ensure **Python** is installed on your system. Subsequently, the necessary Python packages, such as Flask, torch, and diffusers need to be set up.
[Diffusers: https://huggingface.co/runwayml/stable-diffusion-v1-5]

#### Installing Dependencies 🔗
Use the following commands in your terminal or command prompt to install the requisite packages:
```bash
pip install Flask torch diffusers
pip install openai moviepy Pillow
```

#### API Keys 🔐
Your OpenAI API key needs to be placed in the config.py file as shown:

```
API_KEYS = {
    'openai': 'PUT_YOUR_API_KEY_HERE'
}
```
Code File: [config.py](https://github.com/sun-hwang/vvs_generator/blob/09010b78d4f139b831017681bf8d366428a9cfcf/config.py)

#### Running the Application 🚀
Execute the following command to get the app up and running:

```
python main.py
```

This kickstarts the Flask application. You can then access the web interface by heading to http://localhost:5000 on your web browser.

Usage 🖱️
Once on the web interface, input your text into the provided area and hit "Generate Video". The application will then weave a story, spawn images, morph them into a video, and showcase it on the webpage.

Note: Ensure to substitute 'PUT_YOUR_API_KEY_HERE' with your actual OpenAI API key to ensure the application operates seamlessly.
