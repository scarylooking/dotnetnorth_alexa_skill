import datetime
from utility import events_utility
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_intent_name


class EventInformationIntentHandler(AbstractRequestHandler):

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return is_intent_name("EventInformationIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        speech_text = self.get_speech_text()

        handler_input.response_builder.speak(speech_text).set_should_end_session(True)

        return handler_input.response_builder.response

    @staticmethod
    def get_speech_text():
        upcoming_events = events_utility.get_events()

        if not upcoming_events or upcoming_events is None:
            return "There are no events scheduled at the moment"

        next_event = upcoming_events[0]

        event_name = next_event.get('name', None)
        event_date = next_event.get('date', None)
        event_time = next_event.get('time', None)

        if event_name is None or event_date is None or event_time is None:
            return "There is an event scheduled, but I was unable to process it..."

        event_is_online = next_event.get('online', None)

        event_datetime = datetime.datetime.strptime(f'{event_date} {event_time}', '%Y-%m-%d %H:%M')
        event_day_name = event_datetime.strftime("%A")
        event_date_suffix = 'th' if 11 <= event_datetime.day <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(event_datetime.day % 10, 'th')

        return f'The next event is "{event_name}" on {event_day_name} the {event_datetime.day}{event_date_suffix} of {event_datetime.strftime("%B")}. The session will be streamed online via our Twitch channel'