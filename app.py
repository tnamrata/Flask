import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask.ext.uploads import UploadSet, configure_uploads, IMAGES
from werkzeug.utils import secure_filename

# UPLOAD_FOLDER = '/path/to/the/uploads'
# ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'static/img'
#app.debug = True

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
    	filename = photos.save(request.files['photo'])
    	return filename
    return render_template('upload.html')
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)    

@app.route('/display')
def show_index():
	full_filename = os.path.join(app.config['UPLOAD_FOLDER'])
  	return render_template(upload.html, user_image=full_filename)

if __name__ == '__main__':
	app.run()

