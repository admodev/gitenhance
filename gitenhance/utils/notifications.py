import chime

from plyer import notification

class TerminalNotification:
    def __init__(self):
        self.theme = 'big-sur'
        self.app_name = 'Gitenhance'

    def _play_sound(self, sound_type):
        chime.theme(self.theme)
        getattr(chime, sound_type)()

    def notify_success(self):
        self._play_sound('success')
        notification.notify(
                title = "Success!",
                message = "Everything is ok.",
                app_name = self.app_name,
                timeout = 3
        )

    def notify_info(self):
        self._play_sound('info')
        notification.notify(
                title = "Info",
                message = "This is just an informative message...",
                app_name = self.app_name,
                timeout = 3
        )

    def notify_error(self):
        self._play_sound('error')
        notification.notify(
                title = "Error!",
                message = "Don't panic, but an error has occured.",
                app_name = self.app_name,
                timeout = 3
        )

