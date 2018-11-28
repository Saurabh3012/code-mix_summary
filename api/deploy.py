from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
from summarization import text_rank

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():

        if request.method == 'POST':
            rq = request.get_json()
            text = rq['text']
            #text = text.decode('utf-8')
            #print(text)

            return text_rank(text)
        #         if 'file' not in request.files:
        #                 print('No file part')
        #                 return redirect(request.url)

        #         file = request.files['file']
        #         if file.filename == '':
        #                 print('No selected file')
        #                 return redirect(request.url)
        #         if file:
        #                 filename = secure_filename(file.filename)
        #                 file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #                 filepath = (app.config['UPLOAD_FOLDER'] + '/' +filename)

        #                 base = filepath
        #                 basename = os.path.splitext(base)[0]
        #                 if not os.path.exists(basename):
        #                     os.makedirs(basename)
        #                     video_frame(filepath, basename)
                        

        #                 rstf = main_func(basename)
        #                 return (str(rstf))

        else:
             	return "Make a post request" 
