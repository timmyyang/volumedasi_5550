# -*- coding: UTF-8 -*-
#from gtts import gTTS
import random
import C7_2_Def_Talk_list

talk_1 = {
    0 :u'你好',
    1 :u'你在做什麼',
    2 :u'好無聊喔',
    3 :u'要吃飯了沒',
    4 :u'要不要來玩猜拳?',
    5 :u'喔嗨喲',
    6 :u'天氣真好',
    7 :u'天氣真糟糕' 
}

talk_2 = {
    0 :u'你好',
    1 :u'你在做什麼',
    2 :u'好無聊喔',
    3 :u'要吃飯了沒',
    4 :u'要不要來玩猜拳?',
    5 :u'喔嗨喲',
    6 :u'天氣真好',
    7 :u'天氣真糟糕' 
}

answer_1 = {
    0 :u'你好啊',
    1 :u'我在發呆',
    2 :u'對啊 不知道有沒有有趣的事情',
    3 :u'還早呢',
    4 :u'好哇 剪刀石頭布',
    5 :u'撒哪黑優',
    6 :u'可以出去玩',
    7 :u'一直在下雨 真煩' 
}

answer_2 = {
    0 :u'你好啊',
    1 :u'我在發呆',
    2 :u'對啊 不知道有沒有有趣的事情',
    3 :u'還早呢',
    4 :u'好哇 剪刀石頭布',
    5 :u'剪刀石頭布',
    6 :u'可以出去玩',
    7 :u'一直在下雨 真煩' 
}

def want_to_talk_length_check():
    #看which_one_i_want_to_talk if長度決定
    length==1
    return length
def want_to_talk_sub_length_check(value):
    #傳來的value得知指定的if範圍 在取得子集合長度
    if value[0:3] == '001':
        if value[3:5] == '01':
            sub_length==len(talk_1)
        elif value[3:5]== '02':
            sub_length==len(talk_2)
        return sub_length

def which_one_i_want_to_talk(value):
    #問候
    if value[0:3] == '001':
        r = random.randint(1,len(talk_1))
        #tts = gTTS(text='Good morning', lang='en')
        tts = gTTS(text=talk_1[r], lang='zh-tw')
        tts.save("/tmp/file/answer.mp3")
        need_brocast = 1 ;stat_rand_time = 1 ;end_rand_time = 10;
        
        
    return need_brocast ,stat_rand_time ,end_rand_time
        
        
def which_one_i_need_answer(value):
    #問候
    if value[0:3]=='001':
        #tts = gTTS(text='Good morning', lang='en')
        #tts = gTTS(text=u'你好啊', lang='zh-tw')
        r = int(value[3:5])-1
        tts = gTTS(text=answer_1[r], lang='zh-tw')
        tts.save("/tmp/file/answer.mp3")
        #問候 基礎值
        need_brocast = 0 ;stat_rand_time = 1 ;end_rand_time = 1;
        if r == '4':
            need_brocast = 0 ;value='00105'
        
        
    return need_brocast ,stat_rand_time ,end_rand_time
    

        

        
 
