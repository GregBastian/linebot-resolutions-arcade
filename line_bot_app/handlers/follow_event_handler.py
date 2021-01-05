"""
Created on 05/01/2021

@author: Gregorius Ivan Sebastian
@office: Sprint Asia Technology
@email: greg.sebastian@sprintasia.co.id / ivansebastian60@gmail.com
"""
from line_bot_app.responses.flex_message_responses.flex_message_responses import \
    flex_responses_obj


class UserFollowEventHandlers:
    def user_follow_event_handler_function(self, event, line_bot_api):
        flex_responses_obj.received_follow_event(event, line_bot_api)


user_follow_event_handlers_obj = UserFollowEventHandlers()
