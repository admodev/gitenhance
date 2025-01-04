import chime

class Notification:
    def __init__(self):
        self.theme = 'big-sur'

    def _play_sound(self, sound_type):
        chime.theme(self.theme)
        getattr(chime, sound_type)()

    def notify_success(self):
        return self._play_sound('success')

    def notify_info(self):
        return self._play_sound('info')

    def notify_error(self):
        return self._play_sound('error')

