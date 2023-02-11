from flask import current_app as app, request, render_template
import os
from model.prediction import predict

@app.route("/", methods = ["GET", "POST"])
def home():
    caption_pred = ""
    if request.method == "POST":
        f = request.files["image"]
        path = os.path.join(app.config['UPLOAD_FOLDER'], "inputImage.jpg")
        f.save(path)
        caption_pred = predict()
    return render_template("index.html", caption = caption_pred)
