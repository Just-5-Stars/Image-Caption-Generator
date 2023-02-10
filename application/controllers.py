from flask import current_app as app, request, render_template
import os

@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "POST":
        f = request.files["image"]
        path = os.path.join(app.config['UPLOAD_FOLDER'], "inputImage.jpg")
        f.save(path)
    return render_template("index.html")
    