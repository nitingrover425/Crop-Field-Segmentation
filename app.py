from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from keras.preprocessing.image import load_img


app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    return render_template('index.html')

@app.route('/', methods = ['POST'])
def predict():
    imagefile = request.files['imagefile']
    image_path = "./images/" + imagefile.filename
    imagefile.save(image_path)

    image = load_img(image_path, target_size = (500,500))
    VGG = load_model("modelVGG.h5")

    prediction = VGG.predict(image)
    pred = prediction.reshape(500,500,3)
    pred_ = cv.resize(pred,(700,450))
    plt.imshow(pred_)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port=3000, debug=True)