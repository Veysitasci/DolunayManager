from FallenRobot import telethn
from FallenRobot.events import register

@register(pattern="^/owner$")
async def _(event):
    j = "ʜᴇʏ {message.from_user.mention},

ɪ ᴀᴍ 𝗙𝝙𝗟𝗟𝝣𝗡 ✘ 𝗥𝗢𝗕𝗢𝗧

ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ ɪs​‌ [𝝙𝗡𝗢𝗡𝗬𝗠𝗢𝗨𝗦](tg://user?id=1356469075)"
    await event.reply(j)
    
__mod_name__ = "Hi"