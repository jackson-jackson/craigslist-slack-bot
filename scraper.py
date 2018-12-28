from craigslist import CraigslistHousing, CraigslistForSale
from slackclient import SlackClient
from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dateutil.parser import parse
import time
import settings
from util import post_listing_to_slack, post_whip_to_slack
import private

# Create database
engine = create_engine('sqlite:///listings.db', echo=False)

Base = declarative_base()


class Listing(Base):
    """
    A table to store data on craigslist listings.
    """

    __tablename__ = 'listings'

    id = Column(Integer, primary_key=True)
    cl_id = Column(Integer, unique=True)
    link = Column(String, unique=True)
    created = Column(DateTime)
    name = Column(String)
    price = Column(String)
    location = Column(String)
    sqft = Column(String)
    body = Column(String)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


class Whips(Base):
    """
    A table to store data on craigslist whips listings.
    """

    __tablename__ = 'whips'

    id = Column(Integer, primary_key=True)
    cl_id = Column(Integer, unique=True)
    link = Column(String, unique=True)
    created = Column(DateTime)
    name = Column(String)
    price = Column(String)
    location = Column(String)
    body = Column(String)
    image = Column(String)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def scrape_housing():
    # Scrape Craigslist for listings.
    cl_h = CraigslistHousing(site=settings.CRAIGSLIST_SITE, area='nvn', category=settings.CRAIGSLIST_HOUSING_SECTION,
                             filters={'min_price': settings.MIN_PRICE_RENT, 'max_price': settings.MAX_PRICE_RENT})

    results = []
    for result in cl_h.get_results(sort_by='newest', geotagged=True, limit=20, include_details=True):
        results.append(result)

    # Filter scraped results for excluded terms.
    good_listings = []
    x = 0
    for result in results:
        for term in private.EXCLUDED_TERMS:
            if term in result['body'].lower():
                x = x+1
                break
        else:
            listing = session.query(Listing).filter_by(
                cl_id=result["id"]).first()
            # Don't store the listing if it already exists.
            if listing is None:
                good_listings.append(result)
                listing = Listing(
                    cl_id=result['id'],
                    link=result['url'],
                    created=parse(result['datetime']),
                    name=result['name'],
                    price=result['price'],
                    location=result['where'],
                    sqft=result['area'],
                    body=result['body']
                )

            # Save the listing so we don't grab it again.
            session.add(listing)
            session.commit()
    print('{}{} listings contained excluded terms.'.format(time.ctime(), x))

    # Create slack client.
    sc = SlackClient(settings.SLACK_TOKEN)

    # Post each result to Slack.
    for listing in good_listings:
        post_listing_to_slack(sc, listing)


def scrape_whips():
    # Scrape Craigslist for listings.
    cl_fs = CraigslistForSale(site=settings.CRAIGSLIST_SITE, area='van', category=settings.CRAIGSLIST_AUTO_SECTION,
                              filters={'min_price': settings.MIN_PRICE_WHIPS, 'max_price': settings.MAX_PRICE_WHIPS, 'query': 'Macan', 'search_titles': True})

    results = []
    for result in cl_fs.get_results(sort_by='newest', limit=5, include_details=True):
        results.append(result)

    # Filter scraped results for included terms.
    listings = []
    for result in results:
        listing = session.query(Whips).filter_by(cl_id=result['id']).first()
        # Don't store the whip listing if it already exists.
        if listing is None:
            listings.append(result)
            listing = Whips(
                cl_id=result['id'],
                link=result['url'],
                created=parse(result['datetime']),
                name=result['name'],
                price=result['price'],  # '{:,}'.format('price')
                location=result['where'],
                body=result['body'],
                image=result['images'][0]
            )

        # Save whip so we don't grab it again.
        session.add(listing)
        session.commit()

    # Create slack client.
    sc = SlackClient(settings.SLACK_TOKEN)

    # Post each result to Slack.
    for listing in listings:
        post_whip_to_slack(sc, listing)
