def handle_response(message) -> str:
    temp_message = message[8:19]
    if temp_message == 'twitter.com':
        message2 = message.replace("twitter", "fxtwitter")
        return message2


    