from flask import Flask, request, send_file, jsonify
import os

app = Flask(__name__)

@app.route("/api/whitelist")
def api_whitelist():
    hwid = request.args.get("hwid")
    print(f"[+] Запрос whitelist для HWID: {hwid}")
    return jsonify({"success": False})

@app.route("/api/sellix")
def api_key():
    key = request.args.get("key")
    hwid = request.args.get("hwid")
    print(f"[+] Активация ключа '{key}' для HWID '{hwid}'")
    return "Key Activation Complete!"

@app.route("/jq")
def download_jq():
    return send_file("jq", mimetype="application/octet-stream")

@app.route("/hwid")
def download_hwid():
    return send_file("hwid", mimetype="application/octet-stream")

@app.route("/macsploit.zip")
def download_zip():
    return send_file("macsploit.zip", mimetype="application/zip")

@app.route("/macsploit.dylib")
def download_dylib():
    return send_file("macsploit.dylib", mimetype="application/octet-stream")

@app.route("/insert_dylib")
def download_insert():
    return send_file("insert_dylib", mimetype="application/octet-stream")

@app.route("/")
def root():
    return "✅ KallSploit Server работает"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
