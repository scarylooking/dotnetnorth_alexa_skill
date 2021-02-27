import handlers
from utility import logging_utility
from ask_sdk_core.skill_builder import SkillBuilder

logging_utility.configure_logger()


def lambda_handler(event, context):
    return sb.lambda_handler()(event, context)


sb = SkillBuilder()

sb.add_request_handler(handlers.LaunchRequestHandler())
sb.add_request_handler(handlers.HelpIntentHandler())
sb.add_request_handler(handlers.CancelAndStopIntentHandler())
sb.add_request_handler(handlers.SessionEndedRequestHandler())
sb.add_exception_handler(handlers.AllExceptionHandler())

sb.add_request_handler(handlers.EventInformationIntentHandler())
sb.add_request_handler(handlers.AlpacaIntentHandler())
sb.add_request_handler(handlers.LlamaIntentHandler())
sb.add_request_handler(handlers.LocationIntentHandler())

handler = sb.lambda_handler()
