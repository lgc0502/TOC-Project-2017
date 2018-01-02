from transitions.extensions import GraphMachine

import sys
from io import BytesIO

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )
    def which_to_which(self, update):
        text = update.message.text
        return (text!='1' and text !='2' and text != '3')

    def is_going_to_horoscope(self, update):
        text = update.message.text
        return text == '1'

    def is_going_to_divination(self, update):
        text = update.message.text
        return text == '2'

    def is_going_to_2018(self, update):
        text = update.message.text
        return text == '3'
    def is_going_to_2018query(self, update):
        text = update.message.text
        return (text == '1' or text == '2' or text == '3' or text == '4' or text == '5' or text == '6' or text == '7' or text == '8' or text == '9' or text == '10' or text == '11' or text == '12')
    
    def on_enter_which(self, update):
        update.message.reply_text(
                "歡迎來到占卜星球\n"
                "查看今日星座運勢請按1\n"
                "查看占卜請按2\n"
                "查看2018年運勢請按3"
                )

    def on_enter_horoscope(self, update):
        update.message.reply_text(
                "請輸入星座編號\n"
                "1. 牡羊座( 3/21 - 4/20 )\n"
                "2. 金牛座( 4/21 - 5/21 )\n"
                "3. 雙子座( 5/22 - 6/21 )\n"
                "4. 巨蟹座( 6/22 - 7/22 )\n"
                "5. 獅子座( 7/23 - 8/23 )\n"
                "6. 處女座( 8/24 - 9/23 )\n"
                "7. 天秤座( 9/24 - 10/23 )\n"
                "8. 天蝎座( 10/24 - 11/22 )\n"
                "9. 射手座( 11/23 - 12/21 )\n"
                "10.魔羯座( 12/22 - 1/20 )\n"
                "11.水瓶座( 1/21 - 2/19 )\n"
                "12.雙鱼座( 2/20 - 3/20 )")
        #self.go_back(update)

    def on_exit_horoscope(self, update):
        print('Leaving state1')

    def on_enter_divination(self, update):
        update.message.reply_text("I'm entering state2")
        #self.go_back(update)

    def on_exit_divination(self, update):
        print('Leaving state2')
    
    def on_enter_2018(self, update):
        update.message.reply_text(
                "請輸入星座編號\n"
                "1. 牡羊座( 3/21 - 4/20 )\n"
                "2. 金牛座( 4/21 - 5/21 )\n"
                "3. 雙子座( 5/22 - 6/21 )\n"
                "4. 巨蟹座( 6/22 - 7/22 )\n"
                "5. 獅子座( 7/23 - 8/23 )\n"
                "6. 處女座( 8/24 - 9/23 )\n"
                "7. 天秤座( 9/24 - 10/23 )\n"
                "8. 天蝎座( 10/24 - 11/22 )\n"
                "9. 射手座( 11/23 - 12/21 )\n"
                "10.魔羯座( 12/22 - 1/20 )\n"
                "11.水瓶座( 1/21 - 2/19 )\n"
                "12.雙鱼座( 2/20 - 3/20 )")
    def on_enter_2018query(self, update):
        text = update.message.text
        if text == '1':
            update.message.reply_text("  2018 年裡歲星來到了羊座疾厄宮，可以預料這一年裡運勢變化精采無比，當中不乏好運與壞運的逆轉，有機會柳暗花明，在最需要的時候得到好運。\n  獨立經營事業當頭家的，考驗中能讓生意蒸蒸日上，能開創新的契機；固定受薪族的變化較不明顯，但作為核心幕僚的人，今年表現不俗，能蒙受多位貴人提攜。得特別注意八月火星逆入魔羯宮帶來的情緒問題。感情變化上半年多冷靜下半年多險阻，考驗著彼此的信念，如果過於患得患失則很可能有一波三折的走向。") 
        elif text == '2':  
            update.message.reply_text("金牛們在新的一年裡很可能從本來就事論事、實事求是的理性腦，一下子轉身成了風花雪月的浪漫腦，任何事都可能觸動你的愁緒，遠在異鄉打拼的人會有遇見故知的機緣，單身者特別容易感到孤單，上半年波折較多的反倒能在下半年苦盡甘來，2018 整體來說感情上夠你折騰，但相對也能嘗到愈發甜美的果實。")
            update.message.reply_text("工作上表現平盤，雖然暗藏凶險，但大都能化險為夷，比起做事，職場中的牛座更要學著靈活彈性的做人")
        self.go_back(update)
