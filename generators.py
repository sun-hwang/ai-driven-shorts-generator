import openai
from moviepy.editor import ImageClip, CompositeVideoClip, concatenate_videoclips
from PIL import Image, ImageDraw, ImageFont
import os
import torch
from diffusers import StableDiffusionPipeline
import ast, re

class GPT4StoryGenerator:
    def __init__(self, api_key):
        """
        GPT4StoryGenerator.
        :param api_key: OpenAI API Key.
        """
        self.api_key = api_key
        openai.api_key = self.api_key

    def create_story(self, user_input, max_tokens=100, n=1, temperature=0.7):
        try:           
            print('Generating Story') 
            prompt = []
            user_input = 'Make a short story in three sentences. User input:{}, Do not output newline, Outputformat(one sentence for one element): story:[,,]'.format(user_input)
            prompt.append({'role': 'user', 'content': user_input})
            response = openai.ChatCompletion.create(model='gpt-4',messages=prompt)
            stories = response.choices[0].message.to_dict()['content']
            
            print(stories)
            
            sentences = '['+stories.split('[')[1].split(']')[0]+']'
            sentences = ast.literal_eval(sentences)
            
            return sentences
        
        except Exception as e:
            print(f"Error: {str(e)}")
            return [], []


class StoryBasedImageGenerator:
    def __init__(self):
        self.model_id = "runwayml/stable-diffusion-v1-5"
        self.device = "cuda" 
        
    # 가상의 이미지 생성 코드
    def generate_image(self, story_sentence, subtitle, output_path, duration=5):
         
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        pipe = StableDiffusionPipeline.from_pretrained(self.model_id, torch_dtype=torch.float16)
        pipe = pipe.to(self.device)
        input_prompt = 'digital art of {}, high quality, 4k, beautiful, fairy tale, children book, ebook'.format(story_sentence)
        image = pipe(input_prompt, height=360, width=640).images[0]  
                
        image.save(output_path)
        return output_path

class ShortsGenerator:
    @staticmethod
    def create_short_from_images(image_paths, output_path, fps=24):
        clips = [ImageClip(img_path, duration=5) for img_path in image_paths]
               
        # Adding crossfade effect
        faded_clips = []
        for i, clip in enumerate(clips):
            if i == 0:
                faded_clips.append(clip)
            else:
                faded_clips.append(clip.crossfadein(1))
                
        final_clip = concatenate_videoclips(faded_clips, method="compose")
        
        final_clip.write_videofile(output_path, fps=fps)
