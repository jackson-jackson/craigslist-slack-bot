# craigslist-slack-bot

Scrape Craigslist for listings and post to Slack. Search body for included or excluded terms (e.g., filter out terms like 'no pets', 'cozy' (you know it's bad if they say it's cozy!), 'furnished', etc., or look for included terms like 'air conditioning', graphics card, etc.

## Getting your Slack Token

If you're just using simple webhooks you can use the legacy token system here: https://api.slack.com/custom-integrations/legacy-tokens

If you want the newest features then you'll need to use the new Slack Apps API here: https://api.slack.com/slack-apps

## Settings

Settings are in settings.py file. Configure your parameters here and then run the code.

## Running this code

```shell
$ python main_loop.py
```

