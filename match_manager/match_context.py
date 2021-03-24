import asyncio
from typing import List

from telethon.tl.types import Message

from db_methods.group_match import GroupMatchJobs
from rps import RPS_CORE
from telethon import TelegramClient
from telethon.tl.custom.button import Button


class MatchContext:
    def __init__(
        self,
        client: TelegramClient,
        group_id: int,
        match_id: str,
        round_duration=30,
        round_count=5
    ):
        self.__client = client
        self.__group_id = group_id
        self.__match_id = match_id
        self.__round_duration = round_duration
        self.__round_cards = {}
        self.__round_count = round_count
        self.__to_edit_messages: List[Message] = []
        self.__dont_edit: List[int] = []

    @property
    def match_id(self):
        return self.__match_id

    def card_selected(self, player_id: int, card: str):
        if player_id not in self.__round_cards:
            self.__round_cards[player_id] = card
            self.__dont_edit.append(player_id)
            return True
        return False

    async def report(self, text: str):
        return await self.__client.send_message(
            self.__group_id, text
        )

    async def __on_chois_maden(self):
        with GroupMatchJobs() as gmj:
            group = gmj.get_match_secure(
                self.__match_id, self.__group_id
            )
            if group:
                match = RPS_CORE.GetMatch(self.__match_id)
                if match:
                    await self.report("Started fighting.")
                    match.Fight(self.__round_cards)
                    await self.report(str(match.PlayerStatus))

    def build_keyboard(self, your_list: List[str]):
        buttons: List[List[Button]] = []
        added = 0
        for x in your_list:
            if added % 3 == 0:
                buttons.append(
                    [Button.inline(
                        x,
                        f'choisCard_{self.match_id}_{x}'
                    )]
                )
            else:
                buttons[-1].append(Button.inline(
                    x,
                    f'choisCard_{self.match_id}_{x}'
                ))
            added += 1
        return buttons

    async def __on_new_round(self):
        with GroupMatchJobs() as gmj:
            group = gmj.get_match_secure(
                self.__match_id, self.__group_id
            )
            if group:
                match = RPS_CORE.GetMatch(self.__match_id)
                if match:
                    for player_id in match.PlayerIds:
                        try:
                            available_cards = match.AvailableCards(player_id)
                            message = await self.__client.send_message(
                                player_id,
                                "Choose your card!",
                                buttons=self.build_keyboard(available_cards)
                            )
                            self.__to_edit_messages.append(message)
                        except Exception as e:
                            print(e)

    async def edit_messages(self):
        for message in self.__to_edit_messages:
            if message.chat_id in self.__dont_edit:
                continue
            await message.edit("Timed Out!", buttons=None)

        self.__to_edit_messages = []
        self.__dont_edit = []

    async def __start(self):
        for _ in range(self.__round_count):
            await self.__on_new_round()
            await self.report("Please select your cards!")
            await asyncio.sleep(self.__round_duration)
            await self.edit_messages()
            await self.__on_chois_maden()
            self.__round_cards = {}

    def start(self):
        # loop = asyncio.get_running_loop()
        asyncio.ensure_future(self.__start())
        # loop.run_until_complete(task)
