"""
Created on 05/01/2021

@author: Gregorius Ivan Sebastian
@office: Sprint Asia Technology
@email: greg.sebastian@sprintasia.co.id / ivansebastian60@gmail.com
"""
from line_bot_app.responses.arcade_lobby_responses.flex_message_responses.flex_message_responses import \
    arcade_lobby_flex_responses_obj

from line_bot_app.db_models.models import UserArcadeModel, RichMenuModel


class UserUnfollowEventHandlers:
    def user_unfollow_event_handler_function(self, event, line_bot_api):
        idUser = event.source.user_id
        UserArcadeModel.reset_fields_by_user_id(idUser)
        line_bot_api.link_rich_menu_to_user(idUser, RichMenuModel.get_rich_menu_by_pk_id(1))


user_unfollow_event_handlers_obj = UserUnfollowEventHandlers()
