# Discord Bot For Fun

![](https://i.imgur.com/ZQLLmKd.png)  
取得 Bob the bot - [只有 "Send message" 權限(無法使用部分功能)](https://discord.com/api/oauth2/authorize?client_id=808253042172493834&permissions=2048&scope=bot) / [管理員權限](https://discord.com/api/oauth2/authorize?client_id=808253042172493834&permissions=8&scope=bot)

## 目錄

- [指令列表](#cmd)
  - [BrainFuck](#cmd-bf)
    - [!br](#cmd-bf-bf) : BrainFuck
    - [!ttbr](#cmd-bf-ttbf) : Text To BrainFuck
    - [!ttac](#cmd-bf-ttac) : Text To AsCii
    - [!actt](#cmd-bf-actt) : AsCii To Text
  - [QRCode](#cmd-qr)
    - [!qr](#cmd-qr-qr) : QRcode
  - [Image to Accii](#cmd-itac)
    - [!itac](#cmd-itac-itac) : Image To AsCii
  - [Spotify](#cmd-spotify)
    - [!search](#cmd-spotify-search) : search things on Spotify
- [Listeners](#listeners)
  - [Weeb](#listener-weeb) : 讓你說話像個肥宅 (燦笑
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

#### convert text to ascii code array <a id="cmd-bf-ttac"></a>

`!ttac {text}`

**Example**

![](https://i.imgur.com/6ZPo0iN.png)

#### convert ascii code array to text<a id="cmd-bf-actt"></a>

note that you can separate numbers by **any thing** (well... except numbers).

`!actt {numbers}`

**Example**

![](https://i.imgur.com/Mp6A0A8.png)

### QRCode <a id="cmd-qr"></a>

#### url(or text) to QRCode <a id="cmd-qr-qr"></a>

powered by [QRCode-api](https://github.com/BWsix/QRCode-api)

`!qr {url(or text)}`

**Example**

![](https://i.imgur.com/vnROdjL.png)

### Image to Ascii <a id="cmd-itac"></a>

#### image to ascii <a id="cmd-itac-itac"></a>

`!itac` + _Image_

**Example**

![](https://i.imgur.com/J64mnSg.png)
### Spotify<a id="cmd-spotify"></a>

powered by [Spotify-api](https://github.com/BWsix/spotify-api)

#### search things on spotify<a id="cmd-spotify-search"></a>

`!spotify {your query string}` 

**Example**

![](https://i.imgur.com/z40Yc5D.png)

## Listeners<a id="listeners"></a>

### Weeb <a id="listener-weeb"></a>

只要頻道名稱包含 **weeb** 便會自動啟用

**Example**

![](https://i.imgur.com/3FzXfuC.png)

## 貢獻 <a id="contribute"></a>

將你的 cog 加入`bot/cogs`，  
並將其 import 至`bot/bot.py`

可以參考[這個 commit](https://github.com/BWsix/discord-bot/commit/d480e48fa13de79ed4af03fb7590643ad1d0c08e)
