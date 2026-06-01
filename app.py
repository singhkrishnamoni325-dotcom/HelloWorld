from flask import Flask, render_template, jsonify, request
import random
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 存储留言
messages = [
    {"id": 1, "author": "System", "text": "🚀 欢迎来到炫酷仪表盘！", "time": "2026-06-01 12:00:00"},
    {"id": 2, "author": "System", "text": "💡 试试点击卡片和发送消息吧~", "time": "2026-06-01 12:00:01"},
]

message_id = 3


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/stats")
def get_stats():
    """返回统计数据"""
    return jsonify({
        "visitors": random.randint(1000, 9999),
        "requests": random.randint(10000, 99999),
        "uptime": f"{random.randint(1, 99)}d {random.randint(0, 23)}h {random.randint(0, 59)}m",
        "cpu": random.randint(5, 85),
        "memory": random.randint(20, 90),
        "disk": random.randint(10, 70),
    })


@app.route("/api/time")
def get_time():
    """返回服务器时间"""
    now = datetime.now()
    return jsonify({
        "time": now.strftime("%Y-%m-%d %H:%M:%S"),
        "timestamp": now.timestamp(),
    })


@app.route("/api/messages", methods=["GET", "POST"])
def handle_messages():
    global message_id
    if request.method == "POST":
        data = request.get_json()
        msg = {
            "id": message_id,
            "author": data.get("author", "Anonymous"),
            "text": data.get("text", ""),
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        messages.append(msg)
        message_id += 1
        # 只保留最近20条
        if len(messages) > 20:
            messages.pop(0)
        return jsonify({"status": "ok", "message": msg})
    return jsonify(messages[-10:])


@app.route("/api/random")
def get_random():
    """返回随机颜色和数字 — 用于酷炫特效"""
    return jsonify({
        "color": f"hsl({random.randint(0, 360)}, 80%, 60%)",
        "number": random.randint(1, 100),
        "quote": random.choice([
            "The only way to do great work is to love what you do.",
            "Stay hungry, stay foolish.",
            "Think different.",
            "Code is poetry.",
            "Simplicity is the ultimate sophistication.",
            "Move fast and break things.",
            "Make it work, make it right, make it fast.",
        ]),
    })


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
    print("🚀 Flask server is running at http://127.0.0.1:5000/")
