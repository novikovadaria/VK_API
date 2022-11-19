import vk_api
token = 'hfiaondaodoadoa' # your token
session = vk_api.VkApi(token=token)
vk = session.get_api()
my_id = 473138077
vk_friends = {           # Словарь с айдишниками людей, которым юзер время от времени будет писать
    'Алина': 948562846,
    'Эмиль': 123456588
}


action = input('Выбирете дейсвтие:\n1 - пишем смс\n2 - пишем пост\n')
if action == '1':
    person = input('Кому пишем?))\n')
    if person in vk_friends.keys():
        msg = input('')
        vk.messages.send(user_id=vk_friends[person], message=msg, random_id=0)
    else:
        print('Такого человека нет у вас в друзьях')
elif action == '2':
    msg = input('')
    vk.wall.post(owner_id=my_id, friends_only=0,
                 message=msg, status=0, long=180)
else:
  print('Ошибка ввода. Повторите попытку.')
