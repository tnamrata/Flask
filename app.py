import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

UPLOAD_FOLDER = 'C:/Users/tnamr/OneDrive/Desktop/DL/flash/app/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

app.config.update(DEBUG = True)
TEMPLATES_AUTO_RELOAD = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
	return render_template('upload.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# @app.route('/')
# def index():
#     return redirect('/0')

@app.route('/', methods=['POST', 'GET'])
def upload():

    target = os.path.join(APP_ROOT, 'uploads')
   

    if not os.path.isdir(target):
    	os.mkdir(target)
    global destination
    for file in request.files.getlist("file"):
    	
    	filename = file.filename
    	destination = "\\".join([target, filename])
    	
    	file.save(destination)
    print('my file bro')
    
    print(destination)
    print(type(destination))
    return render_template("template.html", file_nm = destination)
    # return redirect(url_for('uploaded_file', filename=destination)) 

@app.route('/', methods = ['POST', 'GET'])
def uploaded_file(filename):
    file = "\\".join([filename, ])
    print('my file')
    print(filename)
    return render_template('template.html', file_nm=filename)

'''
@app.route('/')
def send_file(filename):
    return send_from_directory("UPLOAD_FOLDER", filename)
'''

if __name__ == '__main__':
	app.run()





