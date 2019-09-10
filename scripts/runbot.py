#!/usr/bin/env python

import os
from discord.ext.commands import Bot
from dottybot.util import (find_emojis,
                           fetch_all,
                           convert_images,
                           format_codeblock,
                           get_logger)

# Required to run
TOKEN = os.environ['BOT_TOKEN']
log = get_logger()
bot = Bot(command_prefix='!', description='Converts emotes to braille unicode')


@bot.event
async def on_ready():
    log.info(f"Logged in as {bot.user.name} ({bot.user.id})")


@bot.command()
async def dotty(ctx, *emojinames):
    try:
        emoji_objs = find_emojis(emojinames, bot.emojis)
        images = await fetch_all([e.url for e in emoji_objs], loop=bot.loop)
        result = convert_images(images)

        if result:
            await ctx.send(format_codeblock(result))
            # log.info(f"Converted and sent {emoji.name}")

    except KeyboardInterrupt:
        log.warn('Stopping bot..')
        bot.close()


log.info('Connecting to Discord..')
bot.run(TOKEN)
