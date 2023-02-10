from flask import current_app as app, request, render_template
import os
from model.prediction import predict_caption

@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "POST":
        f = request.files["image"]
        path = os.path.join(app.config['UPLOAD_FOLDER'], "inputImage.jpg")
        f.save(path)
        print(predict_caption())
    return render_template("index.html")
