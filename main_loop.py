from scraper import scrape_housing, scrape_whips
import settings
import time
import sys
import traceback

if __name__ == "__main__":
    while True:
        print(f"{time.ctime()}: Starting scrape cycle for housing...")
        try:
            scrape_housing()
        except KeyboardInterrupt:
            print("Exiting...")
            sys.exit(1)
        except Exception as exc:
            print("Error with the scraping:", sys.exc_info()[0])
            traceback.print_exc()
        else:
            print(f"{time.ctime()}: Successfully finished scraping housing.")

        print(f"{time.ctime()}: Starting scrape cycle for whips...")
        try:
            scrape_whips()
        except KeyboardInterrupt:
            print("Exiting....")
            sys.exit(1)
        except Exception as exc:
            print("Error with the scraping:", sys.exc_info()[0])
            traceback.print_exc()
        else:
            print(f"{time.ctime()}: Successfully finished scraping for whips.")
            print(f"{time.ctime()}: Going to sleep for {int(settings.SLEEP_INTERVAL / 60)} minutes.\n")
        time.sleep(settings.SLEEP_INTERVAL)
