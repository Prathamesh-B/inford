import unittest
from src.inford import DiscordWebhook


class TestWebhook(unittest.TestCase):
    def testContent(self):
        hook = DiscordWebhook(webhook_url="url", content="TEST")
        exp_payload = {"content": "TEST"}
        self.assertEqual(hook.format(), exp_payload)

    def testWithEmbed(self):
        hook = DiscordWebhook(
            webhook_url="url",
            username="hey",
            title="hello",
        )
        exp_payload = {
            "username": "hey",
            "embeds": [
                {
                    "author": {},
                    "footer": {},
                    "image": {},
                    "thumbnail": {},
                    "fields": [],
                    "title": "hello",
                }
            ],
        }
        self.assertEqual(hook.format(), exp_payload)

    def testFull(self):
        hook = DiscordWebhook(
            webhook_url="URL",
            username="inford",
            avatar_url="https://avatars.githubusercontent.com/u/55992548?v=4",
            content="Lorem ipsum dolor sit",
            title="Hey!",
            color="#0099ff",
            description="Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            author_name="INFORD",
            author_url="https://github.com/Prathamesh-B/inford",
            footer_text="thank you",
            footer_icon="https://user-images.githubusercontent.com/5679180/79618120-0daffb80-80be-11ea-819e-d2b0fa904d07.gif",
            image="https://avatars.githubusercontent.com/u/55992548?v=4",
            thumbnail="https://avatars.githubusercontent.com/u/55992548?v=4",
        )

        exp_payload = {
            "username": "inford",
            "avatar_url": "https://avatars.githubusercontent.com/u/55992548?v=4",
            "content": "Lorem ipsum dolor sit",
            "embeds": [
                {
                    "author": {
                        "name": "INFORD",
                        "url": "https://github.com/Prathamesh-B/inford",
                    },
                    "footer": {
                        "text": "thank you",
                        "icon_url": "https://user-images.githubusercontent.com/5679180/79618120-0daffb80-80be-11ea-819e-d2b0fa904d07.gif",
                    },
                    "image": {
                        "url": "https://avatars.githubusercontent.com/u/55992548?v=4"
                    },
                    "thumbnail": {
                        "url": "https://avatars.githubusercontent.com/u/55992548?v=4"
                    },
                    "fields": [],
                    "title": "Hey!",
                    "color": 39423,
                    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                }
            ],
        }

        self.assertEqual(hook.format(), exp_payload)


if __name__ == "__main__":
    unittest.main()
