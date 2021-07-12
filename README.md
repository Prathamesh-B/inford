# inford 📬

![GitHub](https://img.shields.io/github/license/Prathamesh-B/inford)
![PyPI](https://img.shields.io/pypi/v/inford)
[![Tests](https://github.com/Prathamesh-B/inford/actions/workflows/python-tests.yml/badge.svg)](https://github.com/Prathamesh-B/inford/actions/workflows/python-tests.yml)

inford is a python library for sending discord webhooks.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install inford
```

## Usage

```python
from inford import DiscordWebhook

web = DiscordWebhook(
    webhook_url="https://discord.com/api/webhooks/123***/abc***",
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
web.send() #or use send=True as a Argument
```

![image](img/example.png "Example")

### Presets

```python
from inford import Presets

web = Presets(
    webhook_url="https://discord.com/api/webhooks/123***/AbC***",
)

web.info("Python", "Update available")
web.error("Database", "No data found")
web.warn("System", "Ram overload")
web.success("Program", "Executed successfully")
```

![preset_img](img/presets_example.png "Preset")

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
