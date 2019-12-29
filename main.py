import vk
from random import randrange
from random import randint

mytoken = 'eb8adc138e1576dd0650cc527339130ed79d3eb78d7eae0c8060005522a63596219a376aaa7e4b1e4ee52'

session = vk.Session(access_token = mytoken)

api = vk.API(session)

while True:
      try:

          a = ['Нет, я юблю только девочек', 'Только отсосу', 'Иди нахуй', 'Давай втроем, с девочкой', 'Я лучше с твоей подругой хаха', 'Давай, только в твоих мечтах', 'Отлижи']
          
          random_index = randrange(0,len(a))

          b = ['Иди нахуй', 'Отлижи потом проси', 'Я лижу только девочкам']

          random_index = randrange(0,len(b))

          с = ['Жопа болит хуева у меня все', 'Как у шлюхи', 'ахуена казачка пришла', 'Пиздата', 'Очень хуево кавказка ушла от меня', 'Хорошо лижу пизду мамки']

          random_index = randrange(0,len(с))

          d = ['Ебать тебе мозги', 'Ебаца с девочками', 'Сосать', 'Лизать девочкам', 'Нихуя я тупая']

          random_index = randrange(0,len(d))

          e = ['ОлеК', 'Олегсандр', 'Диана самая крутая', 'Акакий Петрович', 'Лох', 'Я лесбичика']

          random_index = randrange(0,len(e))

          r = ['Как у твоей матери', 'Слижком глубоко, слижком много линеек затерались в моей жопе', 'Можешь проверить если хуй больше километра', 'пошел нахуй уебан', 'отсосу за три рубля дам в жопу за пять']

          random_index = randrange(0,len(r))

          t = ['нет только горячих казашек', 'нет я по посудомойкам', 'хачу мыть пол', 'я твоей матери лизала писку хаха твоя мать казашка', 'кстати я сороколетний лесби педофил а ты моя жертва хаха']

          random_index = randrange(0,len(t))

          dialogs = api.messages.getDialogs(unanswered = 1, v=5.92)

          usr_id = dialogs['items'][0]['message']['user_id']

          message = dialogs['items'][0]['message']['body']


          

          if message == ('Привет'):
              api.messages.send(user_id=usr_id, random_id = randint(0, 1000000), message = 'Приветики', v=5.92)
              
          elif message == ('Сколько см твое очко?'):
               api.messages.send(user_id=usr_id, random_id = randint(0, 1000000), message = r[random_index], v=5.92)

          elif message == ('Любишь горяцих кавказцев?'):
               api.messages.send(user_id=usr_id, random_id = randint(0, 1000000), message = t[random_index], v=5.92)

          elif message == ('Го ебаца'):
               api.messages.send(user_id=usr_id, random_id = randint(0, 1000000), message = a[random_index], v=5.92)

          elif message == ('Что ты умеешь?'):
               api.messages.send(user_id=usr_id, random_id = randint(0, 1000000), message = d[random_index], v=5.92)

          elif message == ('Отсоси'):
               api.messages.send(user_id=usr_id, random_id = randint(0, 1000000), message = b[random_index], v=5.92)

          elif message == ('Как дела?'):
               api.messages.send(user_id=usr_id, random_id = randint(0, 1000000), message = с[random_index], v=5.92)

          elif message == ('Как тебя зовут?'):
               api.messages.send(user_id=usr_id, random_id = randint(0, 1000000), message =  e[random_index], v=5.92) 

          elif message == ('Стоп'):
               api.messages.send(user_id=usr_id, random_id = randint(0, 1000000), message = 'Спасибо за использование! Буду рад видеть тебя снова!', v=5.92)

          

              

          
      except:
         pass
