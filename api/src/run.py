from app import app

if __name__ == "__main__":
    dev_msg = "Flask 监听IP: {}, 监听端口为: {}"
    print(dev_msg.format(app.config.get('COMMON_SERVER_IP'), app.config.get('COMMON_SERVER_PORT')))
    app.run(host=app.config.get("COMMON_SERVER_IP"), port=app.config.get("COMMON_SERVER_PORT"), debug=True)
