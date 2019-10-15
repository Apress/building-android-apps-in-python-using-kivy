import flask
import base64
import PIL.Image
import webbrowser
import os

app = flask.Flask(import_name="FlaskUpload")

cam_width = 0
cam_height = 0

html_opened = False

@app.route('/camSize', methods = ['GET', 'POST'])
def cam_size():
    global cam_width
    global cam_height

    cam_width = int(float(flask.request.args["width"]))
    cam_height = int(float(flask.request.args["height"]))

    print('Width',cam_width,'& Height',cam_height,'Received Successfully.')

    return "OK"

@app.route('/', methods = ['POST'])
def upload_file():
    global cam_width
    global cam_height
    global html_opened

    file_to_upload = flask.request.files['media'].read()

    image = PIL.Image.frombytes(mode="RGBA", size=(cam_width, cam_height), data=file_to_upload)
    image = image.rotate(-90)
    image.save('out.png')

    print('File Uploaded Successfully.')

    f = open('out.png', 'rb')
#    im_base64 = base64.b64encode(image.tobytes())
    im_base64 = base64.b64encode(f.read())

    html_code = '<html><head><meta http-equiv="refresh" content="0.5"><title>Displaying Uploaded Image</title></head><body><h1>Uploaded Image to the Flask Server</h1><img src="data:;base64,'+im_base64.decode('utf8')+'" alt="Uploaded Image at the Flask Server"/></body></html>'

    html_url = os.getcwd()+"/templates/test.html"
    f = open(html_url,'w')
    f.write(html_code)
    f.close()

    if html_opened == False:
        webbrowser.open(html_url)
        html_opened = True

    return "SUCCESS"

app.run(host="192.168.16.103", port=6666, debug=True)
