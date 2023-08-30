from flask import Flask, render_template
import os
app = Flask(__name__, template_folder='template')

@app.route('/')
def system_info():
    # Lấy thông tin hệ thống
    hostname = os.uname()[1]
    os_name = os.name
    cpu_count = os.cpu_count()
    mem_info = os.popen('free -h').readlines()[1].split()
    total_mem = mem_info[1]
    used_mem = mem_info[2]
    available_mem = mem_info[6]

    # Hiển thị thông tin hệ thống trên trang web
    return render_template('system.html', hostname=hostname, os_name=os_name, cpu_count=cpu_count,
                            total_mem=total_mem, used_mem=used_mem, available_mem=available_mem)

if __name__ == '__main__':
	app.run(host='0.0.0.0')
