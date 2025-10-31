from flask import Flask
import redis

app = Flask(__name__)

r = redis.Redis(host='redis', port=6379)

@app.route('/')
def home():
    try:
        r.ping()
        return "Redis connected successfully! 🔥"
    except Exception as e:
        return f"Error connecting to Redis: {e}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
