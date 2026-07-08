from app.commands.greeting_command import GreetingCommand
from app.commands.name_command import NameCommand
from app.commands.menu_command import MenuCommand
from app.commands.support_command import SupportCommand
from app.commands.price_command import PriceCommand
from app.commands.schedule_command import ScheduleCommand

class CommandDispatcher:

    def __init__(self):

        self.commands = [
            NameCommand(),
            GreetingCommand(),
            MenuCommand(),
            SupportCommand(),
            PriceCommand(),
            ScheduleCommand(),
        ]

    def dispatch(self, user_id: str, message: str):

        for command in self.commands:

            if command.can_handle(user_id, message):
                return command.handle(user_id, message)

        return None