import aiohttp
from http import HTTPStatus

from fastapi import HTTPException


URL = "https://jservice.io/api/random"

TIMEOUT = aiohttp.ClientTimeout(total=60)


async def async_get(num: int):
    params = {"count": num}
    async with aiohttp.ClientSession(timeout=TIMEOUT) as session:
        response = await session.get(url=URL, params=params)
        if response.status == HTTPStatus.OK:
            return await response.json()

        raise HTTPException(status_code=response.status, detail="Something went wrong!")
