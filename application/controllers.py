from flask import current_app as app, request, render_template, url_for, redirect
import os
from model.prediction import predict
from gtts import gTTS


@app.route("/", methods = ["GET", "POST"])
def home():
    caption_pred = ""
    src = "https://images.unsplash.com/photo-1591485423007-765bde4139ef?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=80"
    if request.method == "POST":
        f = request.files["image"]
        path = os.path.join(app.config['UPLOAD_FOLDER'], "inputImage.png")
        f.save(path)
        caption_pred = predict()
        caption_pred = caption_pred.replace("startseq", "")
        caption_pred = caption_pred.replace("endseq", "")
        caption_pred = caption_pred.strip().capitalize()
        audio = gTTS(text = caption_pred, lang = "en", slow = False)
        audio.save(app.config['UPLOAD_FOLDER'] + "/" + "caption_audio.mp3")
        src = path
    return render_template("index.html", caption = caption_pred, src = src)

@app.route('/display/<filename>')
def display_image(filename):
	return redirect(url_for('app_data', filename='inputImage.jpg'), code=301)