# Discord Bot For Fun

![](https://i.imgur.com/ZQLLmKd.png)  
取得 Bob the bot - [只有 "Send message" 權限](https://discord.com/api/oauth2/authorize?client_id=808253042172493834&permissions=2048&scope=bot) / [管理員權限](https://discord.com/api/oauth2/authorize?client_id=808253042172493834&permissions=8&scope=bot)

## 目錄

- [指令列表](#cmd)
  - [BrainFuck](#cmd-bf)
    - [!br](#cmd-bf-bf)
    - [!ttbr](#cmd-bf-ttbf)
  - [QRCode](#cmd-qr)
    - [!qr](#cmd-qr-qr)
- [如何貢獻](#contribute)

## 指令列表 <a id="cmd"></a>

### BrainFuck <a id="cmd-bf"></a>

powered by [Brainfuck-api](https://github.com/BWsix/Brainfuck-api)

#### execute brainfuck code <a id="cmd-bf-bf"></a>

`!bf {brainFuck code}`

**Example**

![](https://i.imgur.com/p0WK3yP.png)

#### convert text to executable brainfuck code <a id="cmd-bf-ttbf"></a>

`!ttbf {text}`

**Example**

![](https://i.imgur.com/WSUDhxl.png)

### QRCode <a id="cmd-qr"></a>

#### url(or text) to QRCode <a id="cmd-qr-qr"></a>

powered by [QRCode-api](https://github.com/BWsix/QRCode-api)

`!qr {url(or text)}`

**Example**

![](https://i.imgur.com/vnROdjL.png)

## 貢獻 <a id="contribute"></a>

將你的 cog 加入`bot/cogs`，  
並將其 import 至`bot/bot.py`

可以參考[這個 commit](https://github.com/BWsix/discord-bot/commit/d480e48fa13de79ed4af03fb7590643ad1d0c08e)
