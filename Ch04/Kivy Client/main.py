import kivy.app
import requests
import kivy.clock
import kivy.uix.screenmanager
import threading

class Configure(kivy.uix.screenmanager.Screen):
    pass

class Capture(kivy.uix.screenmanager.Screen):
    pass

class PycamApp(kivy.app.App):
    num_images = 0

    def cam_size(self):
        camera = self.root.screens[1].ids['camera']
        cam_width_height = {'width': camera.resolution[0], 'height': camera.resolution[1]}

        ip_addr = self.root.screens[0].ids['ip_address'].text
        port_number = self.root.screens[0].ids['port_number'].text
        url = 'http://'+ip_addr+':'+port_number+'/camSize'

        try:
            self.root.screens[0].ids['cam_size'].text = "Trying to Establish a Connection..."
            requests.post(url, params=cam_width_height)
            self.root.screens[0].ids['cam_size'].text = "Done."
            self.root.current = "capture"
        except requests.exceptions.ConnectionError:
            self.root.screens[0].ids['cam_size'].text = "Connection Error! Make Sure Server is Active."

    def capture(self):
        kivy.clock.Clock.schedule_interval(self.upload_images, 1.0)

    def upload_images(self, *args):
        self.num_images = self.num_images  + 1
        print("Uploading image", self.num_images )

        camera = self.root.screens[1].ids['camera']

        print("Image Size ", camera.resolution[0], camera.resolution[1])
        print("Image corner ", camera.x, camera.y)

        pixels_data = camera.texture.get_region(x=camera.x, y=camera.y, width=camera.resolution[0],height=camera.resolution[1]).pixels

        ip_addr = self.root.screens[0].ids['ip_address'].text
        port_number = self.root.screens[0].ids['port_number'].text
        url = 'http://'+ip_addr+':'+port_number+'/'
        files = {'media': pixels_data}
       
        t = threading.Thread(target=self.send_files_server, args=(files, url))
        t.start()

    def build(self):
        pass

    def send_files_server(self, files, url):
        try:
#            self.root.screens[1].ids['capture'].text = "Trying to Establish a Connection..."
            requests.post(url, files=files)
#            self.root.screens[1].ids['capture'].text = "Capture Again!"
        except requests.exceptions.ConnectionError:
            self.root.screens[1].ids['capture'].text = "Connection Error! Make Sure Server is Active."

if __name__ == "__main__":
    app = PycamApp()
    app.run()
