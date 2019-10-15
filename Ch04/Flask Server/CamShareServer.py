import flask
import PIL.Image
import base64
import webbrowser
import sys
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

    html_code = '<html><head><meta http-equiv="refresh" content="1"><title>Displaying Uploaded Image</title></head><body><h1>Uploaded Image to the Flask Server</h1><img src="data:;base64,'+im_base64.decode('utf8')+'" alt="Uploaded Image at the Flask Server"/></body></html>'

    # The HTML page is not required to be opened from the Python code but open it yourself externally.
    html_url = os.getcwd()+"/templates/test.html"
    f = open(html_url,'w')
    f.write(html_code)
    f.close()

    if html_opened == False:
        webbrowser.open(html_url)
        html_opened = True

    return "SUCCESS"

ip_address = sys.argv[1]#"192.168.43.231"
port_number = int(sys.argv[2])#6666
app.run(host=ip_address, port=port_number, debug=True, threaded=True)

