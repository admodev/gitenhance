import chime

from plyer import notification

class TerminalNotification:
    def __init__(self):
        self.theme = 'big-sur'

    def _play_sound(self, sound_type):
        chime.theme(self.theme)
        getattr(chime, sound_type)()

    def notify_success(self):
        self._play_sound('success')
        notification.notify(
                title = "Success!",
                message = "Everything is ok.",
                timeout = 3
        )

    def notify_info(self):
        return self._play_sound('info')

    def notify_error(self):
        return self._play_sound('error')

