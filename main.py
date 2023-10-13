from flask import Flask, render_template, request, url_for
from generators import GPT4StoryGenerator, StoryBasedImageGenerator, ShortsGenerator
from config import API_KEYS
import uuid
import os

OPENAI_API_KEY = API_KEYS['openai']

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    video_url = None
    subtitle = []
    if request.method == 'POST':
        user_input = request.form['user_input']
        vname = str(uuid.uuid4())
        # 스토리 생성
        story_gen = GPT4StoryGenerator(OPENAI_API_KEY)
        story = story_gen.create_story(user_input)
        story_save_path = 'static/story_{}.txt'.format(vname)
        f_story = open(story_save_path, 'w')
        subtitle = story
        for l in subtitle:
            f_story.write('{}\n'.format(l))
        f_story.close()
        
        # 이미지 생성
        image_gen = StoryBasedImageGenerator()
        image_paths = []
        
        for i, sentence in enumerate(story):
            output_path = f"static/image_{i}.png"  # 이미지 파일의 저장 경로 설정
            image_path = image_gen.generate_image(sentence, subtitle, output_path)
            image_paths.append(image_path)
        
        # 이미지를 동영상으로 변환
        shorts_gen = ShortsGenerator()
        unique_filename = vname + ".mp4"
        video_path = f"static/{unique_filename}"  
        shorts_gen.create_short_from_images(image_paths, output_path=video_path) 
        
        # 생성된 이미지 파일들 삭제
        for img_path in image_paths:
            os.remove(img_path)
        # 동영상 파일을 사용자에게 전송
        #return send_file(video_path, as_attachment=True)
        video_url = url_for('static', filename=unique_filename)  
    
    return render_template('index.html', video_url=video_url, subtitle=subtitle)

if __name__ == '__main__':
    app.run(debug=True)
