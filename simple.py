from craigslist import CraigslistHousing
from slackclient import SlackClient

# Scrape Craigslist for listings.
cl_h = CraigslistHousing(site='vancouver', area='nvn', category='apa',
                         filters={'min_price': 2000, 'max_price': 3000})

results = []
for result in cl_h.get_results(sort_by='newest', geotagged=True, limit=20, include_details=True):
    results.append(result)

# Create variables for Slack bot.
SLACK_TOKEN = 'xoxp-506488927079-505635824741-506490320151-e915076bc57477c5a7d7b414ae1ad7fc'
SLACK_CHANNEL = '#housing'
sc = SlackClient(SLACK_TOKEN)

# Filter scraped results for excluded terms.
GOOD_LISTINGS = []
EXCLUDED_TERMS = ['no pets', 'furnished', 'cozy', 'shared laundry']
x = 0
for result in results:
    for term in EXCLUDED_TERMS:
        if term in result['body'].lower():
            x = x+1
            break
    else:
        GOOD_LISTINGS.append(result)
print('{} listings contained excluded terms.'.format(x))

# Create function to post filtered listings to Slack.
def post_listing_to_slack(sc, listing):
    """
    Posts the listing to slack.
    :param sc: A slack client.
    :param listing: A record of the listing.
    """
    desc = '{0} | {1} | {2}'.format(listing['price'], listing['name'], listing['url'])
    sc.api_call(
        'chat.postMessage', channel=SLACK_CHANNEL, text=desc,
        username='pybot', icon_emoji=':robot_face:'
    )

# Post each result to Slack.
for listing in GOOD_LISTINGS:
    post_listing_to_slack(sc, listing)
