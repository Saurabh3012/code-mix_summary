from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
from summarization import text_rank
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app, resources={r"/YOURAPP/*": {"origins": "*"}})


@app.route('/', methods=['GET', 'POST'])
def hello_world():

        if request.method == 'POST':
            # print("req data", request.form)
            # rq = request.get_json()['text']
            text = request.form['para']
            summ = text_rank(text)
            #text = text.decode('utf-8')
            #print(text)

            return '''
                    <h3> Input your text here:</h3>
                    <form method="POST">
                              <textarea name="para" cols="150" rows="15">'''+text+'''</textarea><br>
                              <select name="summ_met">
                                  <option value="tx" selected>Text Rank</option>
                                  <option value="fb">Feature based</option>
                              </select>
                              <h6> Input Length: '''+str(len(text))+'''</h6>
                              <input type="submit" value="Submit">
                    </form>
                    <br><br>
                    <h3> Summary of the text: </h3>
                    <form >
                              <textarea name="parares" cols="150" rows="15">'''+summ+'''</textarea>
                              <h6> Summary Length: '''+str(len(summ))+'''</h6>
                              <br>
                    </form>'''

        else:
             	return '''
                        <h3> Input your text here:</h3>
                        <form method="POST">
                              <textarea name="para" cols="150" rows="15">Enter your code-mix article here</textarea><br>
                              <select name="summ_met">
                                  <option value="tx" selected>Text Rank</option>
                                  <option value="fb">Feature based</option>
                              </select>
                              <input type="submit" value="Submit"><br>
                          </form>''' 
