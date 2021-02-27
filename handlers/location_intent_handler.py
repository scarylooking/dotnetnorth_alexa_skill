from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_intent_name
from ask_sdk_model.ui import SimpleCard


class LocationIntentHandler(AbstractRequestHandler):

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return is_intent_name("LocationIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        speech_text = "Our next event is being live-streamed on our Twitch channel, Dot Net North Live"

        handler_input.response_builder.speak(speech_text).set_should_end_session(True)

        return handler_input.response_builder.response