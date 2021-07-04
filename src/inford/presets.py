from .module import DiscordWebhook


class Presets(DiscordWebhook):
    def __init__(self, webhook_url, **kwargs):
        super().__init__(webhook_url, **kwargs)

    def info(self, name, message):
        self.username = name
        self.description = message
        self.title = "Information"
        self.color = "0066ff"
        self.send()

    def error(self, name, message):
        self.username = name
        self.description = message
        self.title = "Error"
        self.color = "ff0000"
        self.send()

    def success(self, name, message):
        self.username = name
        self.description = message
        self.title = "Success"
        self.color = "00ff14"
        self.send()

    def warn(self, name, message):
        self.username = name
        self.description = message
        self.title = "Warning"
        self.color = "ffe900"
        self.send()
