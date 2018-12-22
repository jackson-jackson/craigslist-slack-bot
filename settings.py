import private

# The min and max rent you want to pay each month.
MIN_PRICE = 2000
MAX_PRICE = 3000

# The specific Craigslist site you want to search on.
# For instance, https://sfbay.craigslist.org is SF and the Bay Area.
CRAIGSLIST_SITE = 'vancouver'

# Which Craigslist subdirectories to search.
# For instance, https://sfbay.craigslist.org/eby/ is the East Bay, and https://sfbay.craigslist.org/sfc/ is San Francisco.
# You only need the last three letters of the URLs.
AREA = ['nvn']

# The Craigslist section underneath housing that you want to search in.
# For instance, https://sfbay.craigslist.org/search/apa find apartments for rent.
# https://sfbay.craigslist.org/search/sub finds sublets.
# You only need the last 3 letters of the URLs.
CRAIGSLIST_HOUSING_SECTION = 'apa'

# Search body of post for these terms and do not include posts that contain them in our results.
EXCLUDED_TERMS = ['no pets', 'furnished', 'cozy',
                  'shared laundry', 'Seven Peaks in Squamish']

# Time between scrapes.
SLEEP_INTERVAL = 20 * 60  # 20 minutes

# Which slack channel you want to post the results to.
SLACK_CHANNEL = '#housing'

# The token that allows us to connect to slack.
# Should be put in private.py, or set as an environment variable.
SLACK_TOKEN = private.SLACK_TOKEN
