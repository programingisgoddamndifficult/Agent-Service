from flask import Flask, render_template
import machine_info
app = Flask(__name__)


@app.route('/')
def monitor_info():
    # 创建一个参数字典
    result = machine_info.merge_all_info()
    return render_template('monitor.html', **result)


if __name__ == '__main__':
    app.run(debug=True)