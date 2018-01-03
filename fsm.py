from transitions.extensions import GraphMachine
from all_text import detail
from parse import get_articles
from parse import get_web_page

import sys
from io import BytesIO
######parse########
#Taurus=[]
#page1 = get_web_page('http://astro.click108.com.tw/daily_1.php?iAstro=1')
#if page1:
#    current_articles = get_articles(page1)
#    for post in current_articles:
#        print(post)
#        Taurus.append(post)
########

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )
    def which_to_which(self, update):
        text = update.message.text
        return (text!='1' and text !='2')

    def is_going_to_horoscope(self, update):
        text = update.message.text
        return text == '1'

    def is_going_to_divination(self, update):
        text = update.message.text
        return text == '3'

    def is_going_to_2018(self, update):
        text = update.message.text
        return text == '2'
    def is_going_to_2018query(self, update):
        text = update.message.text
        return (text == '1' or text == '2' or text == '3' or text == '4' or text == '5' or text == '6' or text == '7' or text == '8' or text == '9' or text == '10' or text == '11' or text == '12')
    
    def is_going_to_horoquery(self, update):
        text = update.message.text
        return (text == '1' or text == '2' or text == '3' or text == '4' or text == '5' or text == '6' or text == '7' or text == '8' or text == '9' or text == '10' or text == '11' or text == '12')
    
    def on_enter_which(self, update):
        update.message.reply_text(
                "歡迎來到占卜星球\n"
                "查看今日星座運勢請按1\n"
                "查看2018年運勢請按2"
                )

    def on_enter_horoscope(self, update):
        update.message.reply_text(
                "#daily\n"
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
        update.message.reply_text('Searching...')

    def on_enter_horoquery(self, update):
        text = update.message.text
        if text == '1':
            page1 = get_web_page('http://astro.click108.com.tw/daily_1.php?iAstro=0')
        elif text == '2':
            page1 = get_web_page('http://astro.click108.com.tw/daily_1.php?iAstro=1')
        elif text == '3':
            page1 = get_web_page('http://astro.click108.com.tw/daily_1.php?iAstro=2')
        elif text == '4':
            page1 = get_web_page('http://astro.click108.com.tw/daily_1.php?iAstro=3')
        elif text == '5':
            page1 = get_web_page('http://astro.click108.com.tw/daily_1.php?iAstro=4')
        elif text == '6':
            page1 = get_web_page('http://astro.click108.com.tw/daily_1.php?iAstro=5')
        elif text == '7':
            page1 = get_web_page('http://astro.click108.com.tw/daily_1.php?iAstro=6')
        elif text == '8':
            page1 = get_web_page('http://astro.click108.com.tw/daily_1.php?iAstro=7')
        elif text == '9':
            page1 = get_web_page('http://astro.click108.com.tw/daily_1.php?iAstro=8')
        elif text == '10':
            page1 = get_web_page('http://astro.click108.com.tw/daily_1.php?iAstro=9')
        elif text == '11':   
            page1 = get_web_page('http://astro.click108.com.tw/daily_1.php?iAstro=10')
        elif text == '12':    
            page1 = get_web_page('http://astro.click108.com.tw/daily_1.php?iAstro=11')
        if page1:
            current_articles = get_articles(page1)
            for post in current_articles:
                print(post)
                update.message.reply_text(post)
        self.go_back(update)

    def on_enter_divination(self, update):
        update.message.reply_text("I'm entering state2")
        self.go_back(update)

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
        update.message.reply_text("lucky color")
        if text == '1':
            update.message.reply_photo(open("img/Aries.png","rb"))
            show_text = detail('Aries','1')
            update.message.reply_text(show_text)
            show_text = detail('Aries','2')
            update.message.reply_text(show_text)
            show_text = detail('Aries','3')
            update.message.reply_text(show_text)

        elif text == '2':
            update.message.reply_photo(open("img/2.png","rb"))
            show_text = detail('Taurus','1')
            update.message.reply_text(show_text) 
            show_text = detail('Taurus','2')
            update.message.reply_text(show_text)
            show_text = detail('Taurus','3')
            update.message.reply_text(show_text)
        elif text == '3':
            update.message.reply_photo(open("img/3.jpg","rb"))
            show_text = detail('Gemini','1')
            update.message.reply_text(show_text)
            show_text = detail('Gemini','2')
            update.message.reply_text(show_text)
            show_text = detail('Gemini','3')
            update.message.reply_text(show_text)
        elif text == '4':
            update.message.reply_photo(open("img/4.png","rb"))
            show_text = detail('Cancer','1')
            update.message.reply_text(show_text)
            show_text = detail('Cancer','2')
            update.message.reply_text(show_text)
            show_text = detail('Cancer','3')
            update.message.reply_text(show_text)
        elif text == '5':
            update.message.reply_photo(open("img/5.jpg","rb"))
            show_text = detail('Leo','1')
            update.message.reply_text(show_text)
            show_text = detail('Leo','2')
            update.message.reply_text(show_text)
        elif text == '6':
            update.message.reply_photo(open("img/6.png","rb"))
            show_text = detail('Virgo','1')
            update.message.reply_text(show_text)
            show_text = detail('Virgo','2')
            update.message.reply_text(show_text)
        elif text == '7':        
            update.message.reply_photo(open("img/7.png","rb"))
            show_text = detail('Libra','1')
            update.message.reply_text(show_text)
            show_text = detail('Libra','2')
            update.message.reply_text(show_text)
        elif text == '8':
            update.message.reply_photo(open("img/8.png","rb"))
            show_text = detail('Scorpio','1')
            update.message.reply_text(show_text)
            show_text = detail('Scorpio','2')
            update.message.reply_text(show_text)
        elif text == '9':
            update.message.reply_photo(open("img/9.png","rb"))
            show_text = detail('Sag','1')
            update.message.reply_text(show_text)
            show_text = detail('Sag','2')
            update.message.reply_text(show_text)
            show_text = detail('Sag','3')
            update.message.reply_text(show_text)
        elif text == '10':
            update.message.reply_photo(open("img/10.png","rb"))
            show_text = detail('Cap','1')
            update.message.reply_text(show_text)
            show_text = detail('Cap','2')
            update.message.reply_text(show_text)
            show_text = detail('Cap','3')
            update.message.reply_text(show_text)
        elif text == '11':
            update.message.reply_photo(open("img/11.png","rb"))
            show_text = detail('Aquarius','1')
            update.message.reply_text(show_text)
            show_text = detail('Aquarius','2')
            update.message.reply_text(show_text)
            show_text = detail('Aquarius','3')
            update.message.reply_text(show_text)
        elif text == '12':
            update.message.reply_photo(open("img/12.png","rb"))
            show_text = detail('Pisces','1')
            update.message.reply_text(show_text)
            show_text = detail('Pisces','2')
            update.message.reply_text(show_text)
            show_text = detail('Pisces','3')
            update.message.reply_text(show_text)
        self.go_back(update)
