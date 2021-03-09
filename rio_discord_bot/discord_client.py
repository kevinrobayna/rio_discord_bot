import discord


class DiscordClient(discord.Client):
    def __init__(self, guild: int, channel: int, players: list):
        self.guild: int = guild
        self.channel: int = channel
        self.players: list = players

        super().__init__()

    async def on_ready(self):
        print(f"{self.user} is connected!")
        channel = self.get_channel(self.channel)
        lines = [
            "Hello! Ready to bring you RaiderIO information 🎉",
            "I'll only list the following characters: If I'm missing any, please add them here: TBD",
            "",
            "\n".join(self.players),
        ]
        await channel.send("\n".join(lines))

    async def on_member_join(self, member):
        print(member)

    async def on_message(self, message):
        print(message)
        if message.author == self.user:
            return
        if str(message.channel.id) != str(self.channel):
            return

        if message.content.lower().startswith("!rio rank"):
            channel = self.get_channel(self.channel)
            await channel.send("TBD, but Sylphyl Rocks!!! sozz Krugdir")
        return
