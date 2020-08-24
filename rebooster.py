import time

from mastodon import Mastodon

try:
    import config
except ModuleNotFoundError:
    print("ERROR: You must rename `config_example.py` to `config.py` and edit it with your account credentials.")
    import sys; sys.exit()

# Constants
TIME_TO_SLEEP = 180 # 180 seconds = 3 minutes
CLIENT_CRED_FILE = '{}_clientcred.secret'.format(config.CLIENT_NAME.lower())


print("Initializing HashtagGamedev Bot")
print("===============================")
print(" > Connecting to {}".format(config.API_BASE_URL))

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
print(" > Beginning search-loop")
print("------------------------")

while True:
    for tag in config.TAGS:
        tag = tag.lower().strip("# ")
        print(" > Reading timeline for tag #{}".format(tag))

        statuses = mastodon.timeline_hashtag(tag, local=False)
        for status in statuses:
            if not status.favourited:
                # Boost and favorite the new status
                print('   * Reboosting new toot by {} using tag #{} viewable at: {}'.format(
                    status.account.username, tag, status.url))
                mastodon.status_reblog(status.id)
                mastodon.status_favourite(status.id)

    # Sleep for a bit and then try again
    print(" > Sleeping for {} seconds".format(TIME_TO_SLEEP))
    time.sleep(TIME_TO_SLEEP)
