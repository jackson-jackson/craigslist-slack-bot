import settings

def post_listing_to_slack(sc, listing):
    """
    Posts the listing to slack.
    :param sc: A slack client.
    :param listing: A record of the listing.
    """
    desc = "{0} | {1} | {2}".format(
        listing["price"], listing["name"], listing["url"])
    sc.api_call(
        "chat.postMessage", channel=settings.SLACK_CHANNEL_HOUSING, text=desc,
        username='pybot', icon_emoji=':robot_face:'
    )


def post_whip_to_slack(sc, listing):
    """
    Posts the listing to slack.
    :param sc: A slack client.
    :param listing: A record of the listing.
    """
    desc = "{0} | {1} | {2} | {3}".format(
        listing['price'], listing['name'], listing['url'], 'image_url={}'.format(listing['images'][0]))
    sc.api_call(
        "chat.postMessage", channel=settings.SLACK_CHANNEL_WHIPS, text=desc,
        username='pybot', icon_emoji=':robot_face:'
    )

