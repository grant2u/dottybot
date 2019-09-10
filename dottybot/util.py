import sys
import aiohttp
import numpy as np
import logging
import json_logging
from io import BytesIO
from asyncio import gather
from PIL import Image
from .settings import DEBUG, MAX_SIZE, MAX_EMOJIS


def get_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler(sys.stdout))

    if not DEBUG:
        json_logging.ENABLE_JSON_LOGGING = True
        json_logging.init_non_web()

    return logger


def find_emoji(emoji_id, emojis):
    for em in emojis:
        if em.name == emoji_id.strip(':'):
            return em


def find_emojis(emoji_ids, emojis):
    ids = emoji_ids[:MAX_EMOJIS]
    return [e for e in [find_emoji(ei, emojis) for ei in ids] if e]


def format_codeblock(text):
    return f"```{text}```"


def format_braille(emojis):
    return format_codeblock(' '.join(emojis))


def tobraille(img, size):
    scale = size/(img.width/2)
    width = 2*int((img.width*scale)/2)
    height = 4*int((img.height*scale)/4)
    bits = np.array([[1, 8], [2, 16], [4, 32], [64, 128]])
    img = img.resize((width, height)).convert(mode='1')
    imgarr = np.array(img)
    output = ''

    for i in range(0, height, 4):
        for j in range(0, width, 2):
            block = imgarr[i:i+4, j:j+2]*bits
            output += chr(0x2800+block.sum())
        output += "\n"
    return output


def convert_image(source, size):
    return tobraille(Image.open(source), size)


def convert_images(sources):
    if sources:
        size = int(MAX_SIZE / len(sources))
        return " ".join([convert_image(s, size) for s in sources])


async def fetch_emoji_old(url, loop):
    async with aiohttp.ClientSession(loop=loop) as session:
        async with session.get(url) as response:
            file_bytes = await response.read()
            return BytesIO(file_bytes)


async def fetch(session, url):
    async with session.get(url) as response:
        if response.status == 200:
            file_bytes = await response.read()
            return BytesIO(file_bytes)


async def fetch_all(urls, loop):
    async with aiohttp.ClientSession(loop=loop) as session:
        results = await gather(*[fetch(session, u) for u in urls],
                               return_exceptions=True)
        return results
