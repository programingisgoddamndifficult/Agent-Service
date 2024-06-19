from flask import Flask, render_template, session, request, jsonify
from flask_session import Session
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import machine_info

app = Flask(__name__)

# 配置 Flask-Session
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_USE_SIGNER"] = True
app.config["SESSION_KEY_PREFIX"] = "session:"
app.secret_key = "super secret key"
Session(app)

# 配置 Flask-Limiter
limiter = Limiter(key_func=get_remote_address, app=app)

# 初始化监控数据
monitor_data = {
    "request_count": 0,
    "http_sessions": 0
}

@app.before_request
def before_request():
    # 更新请求计数
    monitor_data["request_count"] += 1
    # 更新会话计数
    if "visited" not in session:
        session["visited"] = True
        monitor_data["http_sessions"] += 1

@app.route('/')
def monitor_info():
    result = machine_info.merge_all_info()
    result["web_monitor"] = monitor_data
    return render_template('monitor.html', **result)

@app.route('/device_info')
def get_device_info():
    device_info = machine_info.merge_all_info()
    return jsonify(device_info)

# 目标设备上运行
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)


if __name__ == '__main__':
    app.run(debug=True)
