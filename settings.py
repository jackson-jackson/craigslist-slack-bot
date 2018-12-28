import private

# The min and max rent you want to pay each month.
MIN_PRICE_RENT = 2000
MAX_PRICE_RENT = 3000

# The min and max price you want to pay for car.
MIN_PRICE_WHIPS = 30000
MAX_PRICE_WHIPS = 130000

# The specific Craigslist site you want to search on.
# For instance, https://sfbay.craigslist.org is SF and the Bay Area.
CRAIGSLIST_SITE = 'vancouver'

# Which Craigslist subdirectories to search.
# For instance, https://sfbay.craigslist.org/eby/ is the East Bay, and https://sfbay.craigslist.org/sfc/ is San Francisco.
# You only need the last three letters of the URLs.
AREA = ['van']

# The Craigslist section underneath housing that you want to search in.
# For instance, https://sfbay.craigslist.org/search/apa find apartments for rent.
# https://sfbay.craigslist.org/search/sub finds sublets.
# You only need the last 3 letters of the URLs.
CRAIGSLIST_HOUSING_SECTION = 'apa'
CRAIGSLIST_AUTO_SECTION = 'cta'

# Search body of post for these terms and do not include posts that contain them in our results.
HOUSING_EXCLUDED_TERMS = ['no pets', 'furnished', 'cozy']

# Seach title for included terms
WHIPS_INCLUDED_TERMS = ['Tesla']

# Time between scrapes.
SLEEP_INTERVAL = 20 * 60  # 20 minutes

# Which slack channel you want to post the results to.
SLACK_CHANNEL_HOUSING = '#housing'
SLACK_CHANNEL_WHIPS = '#whips'

# The token that allows us to connect to slack.
# Should be put in private.py, or set as an environment variable.
SLACK_TOKEN = private.SLACK_TOKEN
