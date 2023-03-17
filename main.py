import discord
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

import config
from cogs.database import Base


class MyClient(discord.Client):
    def __init__(self):
        super().__init__()

        db_url = f'mysql+aiomysql://{config.MYSQL_USER}:{config.MYSQL_PASSWORD}@{config.MYSQL_HOST}:{config.MYSQL_DATABASE}'
        self.engine = create_async_engine(db_url, echo=True)
        self.session = async_sessionmaker(self.engine, expire_on_commit=False)

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

    async def close(self) -> None:
        await self.engine.dispose()
        await super().close()


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('my token goes here')
