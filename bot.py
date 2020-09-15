import vk_api
import random
import wikipedia
import config
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

vk = vk_api.VkApi(token=config.mytoken)
vk._auth_token()
vk.get_api()
longpoll = VkBotLongPoll(vk, config.myid)

def send_msg(peer_id: int, message: str, attachment: str = ""):
    return vk.method("messages.send", {**locals(), "random_id": 0})

wikipedia.set_lang("RU")

while True:
    try:
       for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                   if event.object.peer_id != event.object.from_id: #конфа
                       roll= random.randint(1, 100)
                       if event.object.text == "/расписание": #Для Омы
                         (send_msg(event.obj.peer_id, "1 пара 8:00-9:30 \n2 пара 9:40-11:10\n 3 пара 11:40-13:10\n 4 пара 13:20-14:50\n 5 пара 15:10-16:40\n 6 пара 16:50-18:20\n 7 пара 18:30-20:00"))
                       if event.object.text == "/roll": #Случайное число от 1 до 100
                        (send_msg(event.obj.peer_id, "Ваше число - " + str(roll)) )
                       if event.object.text == "/help": 
                        (send_msg(event.obj.peer_id, "Вот что я умею: \n — Случайное число - /roll &#127922; \n \n —  Случайный мем про снюс - /cнюс &#128371;"))
                       foo = ['photo-195613372_457240416','photo-195613372_457240414','photo-195613372_457240408','photo-195613372_457240427','photo-195613372_457240422','photo-195613372_457240397','photo-195613372_457240393']
                       rndm = random.choice(foo)
                       def send_msgsnus(peer_id: int, message: str, attachment = rndm):
                            return vk.method("messages.send", {**locals(), "random_id": 0})
                       if event.object.text == "/снюс":
                        (send_msgsnus(event.obj.peer_id, "Ваш снюс" ))
                       if "/вики" in event.object.text.lower(): #Поиск по вики 
                        search_query = event.object.text.lower().replace('/вики ', '')
                        search_result = str(wikipedia.summary(search_query))
                        message = "Вот что я нашёл: \n{}".format(search_result)
                        vk.method("messages.send", {"peer_id": event.object.peer_id, "message": message, "random_id": 0})
    except Exception as e:
       print(repr(e))