#編集時には　@@　で始まるところを直してください。
#動かない場合は以下に連絡を。

# Discord AMAMI#0001
# Twitter amami_ew


#アプリのトークン
TOKEN = '結構バレるとまずいTOKENなのでDMでお願いします。' #Bot_token

#パッケージのインポートとインスタンスの作成
import discord
client = discord.Client()

INVITE_CHANNEL = '@@入室したときのチャンネルID' # 入室したときのチャンネルID

# 起動時に動作する処理(これは管理側の画面(コンソールとか))
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')
    print('---起動完了---')


#「おはよう」っていうと返事してくれる機能。言葉の変更も可能。
@client.event
async def on_message(message):
    # 「おはよう」で始まるか調べる
    if message.content.startswith("おはよう"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            m = "「おはよう、" + message.author.name + "プロデューサー。」"
            # メッセージが送られてきたチャンネルへメッセージを送る。
            await message.channel.send(m)

#新規メンバー参加時に実行されるイベントハンドラ
@client.event
async def on_member_join(member):
    alert_channel = client.get_channel('@@入室したときのチャンネルID')
    msg = member.name + "さん、ようこそ。私は高嶺のあ、アイドルをやっているわ。 #自己紹介 で自己紹介するといいわ。これからもよろしくね。"
    await alert_channel.send(msg)

#新規ボイスチャンネル参加時に実行されるイベントハンドラ
@client.event
async def on_voice_state_update(member, before, after):
    if member.guild.id == '@@ボイスチャンネルのID' and (before.channel != after.channel):
        alert_channel = client.get_channel('@@ボイチャ入ったことを知らせるチャンネル')
        if before.channel is None: 
            #(スピーカーのマーク)hogeが参加しました。 って出力する。
            msg = ":speaker:" + member.name + "が参加しました。"
            await alert_channel.send(msg)
        elif after.channel is None: 
            msg = member.name + "が退出しました。"
            await alert_channel.send(msg)


# Bot起動 大事！
client.run(TOKEN)