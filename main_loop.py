from scraper import scrape_housing, scrape_whips
import settings
import time
import sys
import traceback

if __name__ == "__main__":
    while True:
        print("{}: Starting scrape cycle for housing".format(time.ctime()))
        try:
            scrape_housing()
        except KeyboardInterrupt:
            print("Exiting....")
            sys.exit(1)
        except Exception as exc:
            print("Error with the scraping:", sys.exc_info()[0])
            traceback.print_exc()
        else:
            print("{}: Successfully finished scraping housing".format(time.ctime()))
        
        print("{}: Starting scrape cycle for whips".format(time.ctime()))
        try:
            scrape_whips()
        except KeyboardInterrupt:
            print("Exiting....")
            sys.exit(1)
        except Exception as exc:
            print("Error with the scraping:", sys.exc_info()[0])
            traceback.print_exc()
        else:
            print("{}: Successfully finished scraping for whips".format(time.ctime()))
        time.sleep(settings.SLEEP_INTERVAL)
