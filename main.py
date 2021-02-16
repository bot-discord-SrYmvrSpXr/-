import discord
import keep_alive
import os

keep_alive.keep_alive()
client = discord.Client()

token =os.environ['TOKEN']


@client.event
async def on_ready():
    print("logged in as ")  #화면에 봇의 아이디, 닉네임 출력
    print(client.user.name)
    print(client.user.id)
    print("==============")
    # 디스코드에는 현재 본인이 어떤 게임을 플레이하는지 보여주는 기능이 있습니다.
    # 이 기능을 이용하여 봇의 상태를 간단하게 출력 가능합니다.
    game = discord.Game("인증 | 이라고 인증 채널에 적어라 휴먼")
    await client.change_presence(status=discord.Status.idle, activity=game)

# 봇이 새로운 메시지를 수신했을때 동작되는 코드
@client.event
async def on_message(message):
    # 받은 메시지의 author 가 bot 인 경우 return
    if message.author.bot:
        return None

    # 답장할 채널은 메세지 받은 채널로 설정
    channel = message.channel

    if message.content.startswith('인즌'):  # message 의 contest 가 '!커맨드' 로 시작할때
        await channel.send('ㅋㅋㅋㅋ `인즌`이 아니라 `인증`임'
                           )  # line 27의 channel 로 'abc' send



#client 실행

client.run(token)
