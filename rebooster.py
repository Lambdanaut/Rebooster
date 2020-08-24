import time
from urllib.parse import urlparse

from mastodon import Mastodon

try:
    import config
except ModuleNotFoundError:
    print("ERROR: You must rename `config_example.py` to `config.py` and edit it with your account credentials.")
    import sys; sys.exit()

# Constants
TIME_TO_SLEEP = 1800  # 1800 seconds = 30 minutes
CLIENT_CRED_FILE = '{}_clientcred.secret'.format(config.CLIENT_NAME.lower())
TIMELINE_DEPTH_LIMIT = 5  # How many of the latest statuses to pull per tag. 

def run():
    print("")
    print("Initializing {} Bot".format(config.CLIENT_NAME))
    print("=================" + "="*len(config.CLIENT_NAME))
    print(" > Connecting to {}".format(config.API_BASE_URL))
    setup_client_cred_file()

    # Create client
    mastodon = Mastodon(
        client_id = CLIENT_CRED_FILE,
        api_base_url = config.API_BASE_URL,
    )

    print(" > Logging in as {} with password <TRUNCATED>".format(config.USERNAME))

    # Then login. This can be done every time, or use persisted with to_file.
    mastodon.log_in(
        config.USERNAME,
        config.PASSWORD,
        # to_file = 'hashtaggamedev_usercred.secret'
    )

    print(" > Successfully logged in")
    print(" > Fetching account data")

    account = mastodon.me()

    print(" > Fetched account data for {}".format(account.acct))

    print(" > Beginning search-loop")
    print("------------------------")

    while True:
        for tag in config.TAGS:
            tag = tag.lower().strip("# ")
            print(" > Reading timeline for new toots tagged #{}".format(tag))

            try:
                statuses = mastodon.timeline_hashtag(tag, local=False, limit=TIMELINE_DEPTH_LIMIT)
            except ConnectionResetError:
                print(" ! Network error while attempting to fetch statuses. Trying again...")
                time.sleep(30)
                continue

            for status in statuses:
                domain = urlparse(status.url).netloc
                if not status.favourited and \
                        status.account.acct != account.acct and \
                        domain not in config.IGNORE_SERVERS:
                    # Boost and favorite the new status
                    print('   * Boosting new toot by {} using tag #{} viewable at: {}'.format(
                        status.account.username, tag, status.url))
                    mastodon.status_reblog(status.id)
                    mastodon.status_favourite(status.id)

        # Sleep for a bit and then try again
        print(" > Sleeping for {} minutes".format(TIME_TO_SLEEP // 60))
        print("--------------------------")
        time.sleep(TIME_TO_SLEEP)

def setup_client_cred_file():
    try:
        with open(CLIENT_CRED_FILE) as f:
            print(' > Found pre-existing secrets file')

    except IOError:
        # If the CLIENT_CRED_FILE doesn't exist, connect to Mastodon, get secrets, and create the cred file.
        print(' > No secrets file found. Auto-generating a new one')
        try:
            Mastodon.create_app(
             config.CLIENT_NAME,
             api_base_url = config.API_BASE_URL,
             to_file = CLIENT_CRED_FILE)
        except:
            print(' > Error connecting to Mastodon. Client secrets could not be generated')
            raise

if __name__ == '__main__':
    run()