from app.commands.name_command import NameCommand
from app.commands.menu_command import MenuCommand
from app.commands.support_command import SupportCommand
from app.commands.schedule_command import ScheduleCommand
from app.commands.human_command import HumanCommand
from app.commands.end_human_command import EndHumanCommand

class CommandDispatcher:

    def __init__(self):

        self.commands = [
            NameCommand(),
            MenuCommand(),
            SupportCommand(),
            ScheduleCommand(),
            HumanCommand(),
            EndHumanCommand(),
        ]

    def dispatch(self, user_id: str, message: str):

        for command in self.commands:

            if command.can_handle(user_id, message):
                return command.handle(user_id, message)

        return None