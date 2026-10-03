from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app) # Vercel se call allow karega

@app.route('/')
def home():
    return {"status":"Bharat AGI Glove Ready","version":"v1","sensors":"Flex + IMU"}

@app.route('/haptic')
def haptic():
    finger = __import__('flask').request.args.get('finger','0')
    # GPIO code yaha ayega - abhi demo ke liye print
    print(f"HAPTIC: Vibrate finger {finger} - Piano teaching mode")
    return {"status":"vibrating","finger":finger,"mode":"piano-teach"}

app.run(host='0.0.0.0',port=5000)
