"""
Created on 05/01/2021

@author: Gregorius Ivan Sebastian
@office: Sprint Asia Technology
@email: greg.sebastian@sprintasia.co.id / ivansebastian60@gmail.com
"""
from line_bot_app.responses.arcade_lobby_responses.flex_message_responses.flex_message_responses import \
    arcade_lobby_flex_responses_obj

from line_bot_app.db_models.models import UserArcadeModel, RichMenuModel, UserFlagGameModel, UserBatikGameModel


class UserFollowEventHandlers:
    def user_follow_event_handler_function(self, event, line_bot_api):
        user_id = event.source.user_id
        if UserArcadeModel.user_isExist_by_user_id(user_id):
            UserArcadeModel.reset_fields_by_user_id(user_id)
            UserArcadeModel.update_user_games_profile_after_refollow(user_id)
            line_bot_api.link_rich_menu_to_user(user_id, RichMenuModel.get_rich_menu_by_pk_id(1))
        else:
            UserArcadeModel.add_user(user_id)

        arcade_lobby_flex_responses_obj.received_follow_event(event, line_bot_api)


user_follow_event_handlers_obj = UserFollowEventHandlers()
