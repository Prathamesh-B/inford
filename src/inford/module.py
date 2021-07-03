import requests
import json


class DiscordWebhook:
    def __init__(self, webhook_url, **kwargs):
        self.webhook_url = webhook_url
        self.username = kwargs.get("username")
        self.avatar_url = kwargs.get("avatar_url")
        self.content = kwargs.get("content")
        self.title = kwargs.get("title")
        self.color = kwargs.get("color")
        self.description = kwargs.get("description")
        self.author_name = kwargs.get("author_name")
        self.author_url = kwargs.get("author_url")
        self.image = kwargs.get("image")
        self.thumbnail = kwargs.get("thumbnail")
        self.footer_text = kwargs.get("footer_text")
        self.footer_icon = kwargs.get("footer_icon")
        # if kwargs.get("timestamp") == True:
        #     timestamp = datetime.now()  #Discord Format: 2021-06-28T12:46:00.000Z %d/%m/%Y %H:%M:%S"
        #     self.timestamp = timestamp.strftime("%Y-%m-%d")
        if kwargs.get("send") == True:
            self.send()

    def format(self):
        embed_data = False
        payload = {}
        embed = {"author": {}, "footer": {}, "image": {}, "thumbnail": {}, "fields": []}

        if self.username:
            payload["username"] = self.username

        if self.avatar_url:
            payload["avatar_url"] = self.avatar_url

        if self.content:
            payload["content"] = self.content

        if self.title:
            embed_data = True
            embed["title"] = self.title

        if self.color:
            embed_data = True
            if self.color.startswith("#"):
                color = self.color[1::]
                embed["color"] = int(color, 16)
            else:
                embed["color"] = int(self.color, 16)

        if self.description:
            embed["description"] = self.description

        if self.author_name:
            embed_data = True
            embed["author"]["name"] = self.author_name

        if self.author_url:
            embed_data = True
            embed["author"]["url"] = self.author_url

        if self.image:
            embed_data = True
            embed["image"]["url"] = self.image

        if self.thumbnail:
            embed_data = True
            embed["thumbnail"]["url"] = self.thumbnail

        if self.footer_text:
            embed_data = True
            embed["footer"]["text"] = self.footer_text

        if self.footer_icon:
            embed_data = True
            embed["footer"]["icon_url"] = self.footer_icon

        if embed_data:
            payload["embeds"] = []
            payload["embeds"].append(embed)

        # if self.timestamp:
        #     embed["timestamp"] = str(self.timestamp)

        print(payload)
        return payload

    def send(self):
        payload = self.format()

        if payload == {}:
            print("Error: Message cannot be empty.")
        else:
            try:
                request = requests.post(
                    self.webhook_url,
                    data=json.dumps(payload),
                    headers={"Content-Type": "application/json"},
                )

                request.raise_for_status()

            except requests.exceptions.RequestException as error:
                print("Error: %s" % error)
