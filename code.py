import vk
import time


def get_users_id(vkapi):
    getchat = vkapi.messages.getChat(chat_id = '/* enter ur chat id */', fields = 'id')
    users = getchat['users']
    di = {}
    for i in range(len(users)):
        num = users[i]['id']
        name = users[i]['first_name'] + ' ' + users[i]['last_name']
        di[num] = name
    return di


f = open('history.txt', 'w')

session = vk.Session(access_token = '/* enter ur token */')
vkapi = vk.API(session, v ='5.71')

get_users = get_users_id(vkapi)

gethistory_max = vkapi.messages.getHistory(user_id = /* ur page id */, peer_id = /* chat id + 2000000000 */, count = 1)
max_mess_id = gethistory_max['items'][0]['id']
loop_id = 0

for loop_id in range(max_mess_id, 0, -200):
    print(loop_id)
    history = vkapi.messages.getHistory(user_id = /* ur page id */, peer_id = /* chat id + 2000000000 */, count = 200,   start_message_id = loop_id)
    item = history['items']

    for i in range(200):
        try:
            x = item[i]
            userid = x['user_id']
            f.write(get_users[userid] + '\n' + x['body'] + '\n')
            time.sleep(0.005)
        except UnicodeEncodeError as err:
            continue

print('finish')
