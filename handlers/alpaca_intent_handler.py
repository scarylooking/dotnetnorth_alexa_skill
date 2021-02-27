from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_intent_name


class AlpacaIntentHandler(AbstractRequestHandler):

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return is_intent_name("AlpacaIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        speech_text = "Friendly but stern, wise, and presumably competent at IT - in the dev-shop of animals, the alpaca would be the technical architect, seeing far into the distance from its mountain pedestal. " \
                      "Also, Oli met an alpaca called Sirius on a friends farm and he was so smitten that he had already changed the logo before anyone could stop him."

        handler_input.response_builder.speak(speech_text).set_should_end_session(True)

        return handler_input.response_builder.response
