from flask import Flask, request, jsonify,send_from_directory
from flask_cors import CORS
import os
#from rembg import remove
from PIL import Image

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "uploads")
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/upload-image", methods=["POST"])
def upload_image():
    try:
        if "image" not in request.files:
            return jsonify({"error": "No image provided"}), 400
        
        image = request.files["image"]

        if image.filename == "":
            return jsonify({"error": "No selected image"}), 400

        global img_path
        img_path= os.path.join(app.config["UPLOAD_FOLDER"], image.filename)
        image.save(img_path)
        print(os.path.join(app.config["UPLOAD_FOLDER"], image.filename))
        input_img = Image.open(image)
        #output = remove(input_img)
        #print("output(type):", type(output))

        return jsonify({"message": "Image uploaded successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
   app.run(debug=True)
