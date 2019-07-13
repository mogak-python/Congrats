from slacker import Slacker
import config

token = config.BOT_USER_OAUTH_ACCESS_TOKEN['token']
slack = Slacker(token)

if __name__ == "__main__":
    slack.chat.post_message('#bots_test', "hello")