import settings
import requests
import json
import scraper

web_hook_url_whips = 'https://hooks.slack.com/services/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'


def post_listing_to_slack(sc, listing):
    """
    Posts the listing to slack.
    :param sc: A slack client.
    :param listing: A record of the listing.
    """
    desc = f"{listing['price']} | {listing['name']} | {listing['url']}"
    sc.api_call(
        "chat.postMessage", channel=settings.SLACK_CHANNEL_HOUSING, text=desc,
        username='pybot', icon_emoji=':robot_face:'
    )


def post_whip_to_slack(sc, whip):
    """
    Posts the whip to slack.
    :param sc: A slack client.
    :param whip: A record of the whip.
    """

    slack_msg = {
        'attachments': [
            {
                'fallback': 'This should be a picture of a car.',
                'color': '#36a64f',
                'title': f"{whip['price']} | {whip['name']} |",
                'title_link': f"{whip['url']}",
                'image_url': whip['images'][0],
                'thumb_url': whip['images'][0],
                "text": "Do you like this post?",
                'actions': [
                    {
                        "name": "like",
                        "text": "Yes",
                        "type": "button",
                        "value": "yes"
                    },
                    {
                        "name": "like",
                        "text": "No",
                        "type": "button",
                        "value": "no"
                    },
                    {
                        "name": "game",
                        "text": "Delete",
                        "style": "danger",
                        "type": "button",
                        "value": "delete",
                        "confirm": {
                            "title": "Are you sure?",
                            "text": "Is it that bad?",
                            "ok_text": "Yes",
                            "dismiss_text": "No"
                        }
                    }
                ]
            }
        ]
    }
    # print(json.dumps(slack_msg))
    requests.post(web_hook_url_whips, data=json.dumps(slack_msg))
