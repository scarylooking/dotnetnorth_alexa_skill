from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_intent_name


class LlamaIntentHandler(AbstractRequestHandler):

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return is_intent_name("LlamaIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        speech_text = "Al is an alpaca, not a llama."

        handler_input.response_builder.speak(speech_text).set_should_end_session(True)

        return handler_input.response_builder.response
