from tortoise import Tortoise


async def init_db():
    await Tortoise.init(
        db_url='postgres://postgres:12qwer12@127.0.0.1:5432/shine_test',
        modules={'models': ['db_management.models']}
    )
