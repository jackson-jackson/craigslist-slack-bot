# craigslist-slack-bot

Scrape Craigslist for listings and post to Slack. Search body for included or excluded terms (e.g., filter out terms like 'no pets', 'cozy' (you know it's bad if they say it's cozy!), 'furnished', etc., or look for included terms like 'air conditioning', graphics card, etc.

## Get your Slack Token

If you're just using simple webhooks you can use the legacy token system here: https://api.slack.com/custom-integrations/legacy-tokens

If you want the newest features then you'll need to use the new Slack Apps API here: https://api.slack.com/slack-apps

## Configure your settings

Settings are in settings.py file. Configure your parameters here and then run the code.

## Configure your private settings

You can (and should) create a file called private.py and store your Slack Token and any other senstive information in it. Reference it in your code by making sure your private file is imported to your settings file:

```python
import private
```

You can refer to it from now on as

```
private.SLACK_TOKEN or settings.SLACK_TOKEN
```

## Run the code

```shell
$ python main_loop.py
```

