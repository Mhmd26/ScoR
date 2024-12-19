import asyncio
import aiohttp
from .utils.extdl import install_pip

try:
    import randomstuff
except ModuleNotFoundError:
    install_pip("aiohttp")
    import randomstuff

from ..Config import Config

async def create_client():
    async with aiohttp.ClientSession() as session:
        # يمكنك تمرير الجلسة إلى randomstuff إذا كان ذلك ضروريًا
        client = randomstuff.AsyncClient(api_key=Config.RANDOM_STUFF_API_KEY, version="4")
        # افعل شيئًا مع client هنا
        return client

async def main():
    client = await create_client()
    # قم بإجراء العمليات مع client هنا

if __name__ == "__main__":
    asyncio.run(main())
