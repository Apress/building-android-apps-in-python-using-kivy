import kivy.app
import jnius
import os

PythonActivity = jnius.autoclass("org.kivy.android.PythonActivity")
mActivity = PythonActivity.mActivity

class AudioApp(kivy.app.App):
    prepare_audio = False

    def start_audio(self):
        if AudioApp.prepare_audio == False:
            MediaPlayer = jnius.autoclass("android.media.MediaPlayer")
            self.mediaPlayer = MediaPlayer()
            try:
                fileName = os.getcwd()+"/bg_music_piano.wav"
                self.mediaPlayer.setDataSource(fileName)
                self.mediaPlayer.prepare()

                kivy.clock.Clock.schedule_interval(self.update_position, 0.1)

                self.mediaPlayer.start()
                AudioApp.prepare_audio = True
                mActivity.toastError("Playing")
            except:
                self.current_pos.text = "Error Playing the Audio File"
                print("Error Playing the Audio File")
                mActivity.toastError("Error Playing the Audio File")
        else:
                self.mediaPlayer.start()
                mActivity.toastError("Playing")

    def pause_audio(self):
        if AudioApp.prepare_audio == True:
            self.mediaPlayer.pause()
            mActivity.toastError("Paused")

    def stop_audio(self):
        if AudioApp.prepare_audio == True:
            self.mediaPlayer.stop()
            mActivity.toastError("Stopped")
            AudioApp.prepare_audio = False

    def update_position(self, *args):
        audioDuration = self.mediaPlayer.getDuration()
        currentPosition = self.mediaPlayer.getCurrentPosition()
        pos_percent = float(currentPosition)/float(audioDuration)

        self.root.ids['audio_pos'].size_hint_x = pos_percent

        self.root.ids['audio_pos_info'].text = "Duration: "+str(audioDuration) + "\nPosition: " + str(currentPosition)+"\nPercent (%): "+str(round(pos_percent*100, 2))

app = AudioApp()
app.run()

