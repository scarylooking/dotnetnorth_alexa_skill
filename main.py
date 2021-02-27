from handlers import event_information_handler

event_intent = event_information_handler.EventInformationIntentHandler()

print(event_intent.handle([]))
