from app import app

@app.route('/')
def home():
    return 'WELCOME TO THE CTArm BACKEND :]'