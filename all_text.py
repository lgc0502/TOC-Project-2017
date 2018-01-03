from transitions.extensions import GraphMachine

import sys
from io import BytesIO


def detail(who,num):

    if (who == 'Taurus' and num == '1'):
        return "金牛們在新的一年裡很可能從本來就事論事、實事求是的理性腦，一下子轉身成了風花雪月的浪漫腦，任何事都可能觸動你的愁緒，遠在異鄉打拼的人會有遇見故知的機緣，單身者特別容易感到孤單"
    elif (who == 'Taurus' and num == '2'):
        return "上半年波折較多的反倒能在下半年苦盡甘來，2018 整體來說感情上夠你折騰，但相對也能嘗到愈發甜美的果實。"
    elif (who == 'Taurus' and num == '3'):
        return "工作上表現平盤，雖然暗藏凶險，但大都能化險為夷，比起做事，職場中的牛座更要學著靈活彈性的做人"
    elif (who == 'Aries' and num == '1'):
        return "2018 年裡歲星來到了羊座疾厄宮，可以預料這一年裡運勢變化精采無比，當中不乏好運與壞運的逆轉，有機會柳暗花明，在最需要的時候得到好運。"
    elif (who == 'Aries' and num == '2'):
        return "獨立經營事業當頭家的，考驗中能讓生意蒸蒸日上，能開創新的契機；固定受薪族的變化較不明顯，但作為核心幕僚的人，今年表現不俗，能蒙受多位貴人提攜。"
    elif (who == 'Aries' and num == '3'):
        return "得特別注意八月火星逆入魔羯宮帶來的情緒問題。感情變化上半年多冷靜下半年多險阻，考驗著彼此的信念，如果過於患得患失則很可能有一波三折的走向。"
    elif (who == 'Gemini' and num == '1'):
        return "走入一個收穫滿滿的年度，在木星進駐僕役宮來看，雙子今年個性中會多了不少穩定的味道，雖然腦子裡種種小點子、小創意依舊驚人"
    elif (who == 'Gemini' and num == '2'):
        return "不過這一年裡的你將有更理性實際的思維，過去常在感情上起起伏伏、捉摸不定的雙子，這一年裡反而會靜下心來認真經營自己的關係。"
    elif (who == 'Gemini' and num == '3'):
        return "小人仍是雙子今年裡存在的麻煩之一，且今年的小人看來就算不是有心要針對你，也會在無意間扯你後腿，最好能和身邊的天兵天將們保持點距離。"
    elif (who == 'Cancer' and num == '1'):
        return "蟹座在新的一年將能從奔波忙碌慢慢能回歸到一個收成的時刻，過去汲汲營營於工作、錢財的人，這一年裡將開始坐享過去辛勤耕耘的果實，時間也沒有往日的緊迫。"
    elif (who == 'Cancer' and num == '2'):
        return "而隨著經驗一點一滴的累積，今年開始正是好好將過去籌備已久的部分作一發揮的時刻，工作上亮點頻頻，只要有心最終都能得償所願。"
    elif (who == 'Cancer' and num == '3'):
        return "然而感情上有些小挫折，得持續的去學去領悟。整體運勢好壞折抵，雖然大致心情愉快，但要維持住企圖心和戰鬥力並不容易。"
    elif (who == 'Leo' and num == '1'):
        return "這一年裡獅子依然有著征服不完的任務、怎麼忙也忙不完的錢途，不論在人際、工作或是生活上各個層面，承接了去年旺盛的運勢軌跡，同樣呈現多頭馬車往前奔的傾象，每個獅子王今年裡都得試著從中調適自己，以防身體不聽話成了你成功的絆腳石。"
    elif (who == 'Leo' and num == '2'):
        return "土星進入六宮奴僕，看來工作上要出現可以放鬆的空檔並不容易，與同儕伙伴分工合作，你需要有更大的包容心與抗壓力。感情上魅力旺但緣分並不強，得看準任何感情契機，為未來埋下幸福種子。"
    elif (who == 'Virgo' and num == '1'):
        return "古人十年磨一劍，處女座過去默默為自己做準備的工夫將慢慢能從 2018 看到曙光。對所有處女座而言，今年行運有著勢如破竹的強旺運勢，順遂的運勢會在太陽行至本命宮時發揮到最大值。"
    elif (who == 'Virgo' and num == '2'):
        return "請留意 8-9 月吉星高照的日子，可以把心力集中在自己喜歡做的事情上 ，只要你有足夠的鬥志，就不用擔心事與願違，由於具備著優異的職場桃花運，若善用此點發揮于業務行銷層面，既交到了朋友也增加了客戶，把魅力轉換成錢財，才是明智之舉。"
    elif (who == 'Libra' and num == '1'):
        return " 木星這顆大吉星雖離開了命宮，卻走入財帛宮帶著天秤的正財運起飛，整體來說仍維持穩健順遂，只是當中開始出現許多混亂及意料外的變化存在其中，會感覺有些忙碌，若能突破層層工作瓶頸，今年理當在收入上邁進新境界"
    elif (who == 'Libra' and num == '2'):
        return "而除了自身熟悉的領域外，別排斥參與外國出差進修的機會，當變化突然出現在工作之中，正是提醒你更上層樓的契機已到，天秤天生慵懶需要被逼前進方能亮出潛力；而感情中有轉折有取捨，好消息多在下半年。"
    elif (who == 'Scorpio' and num == '1'):
        return "歲星木星在蠍座本命宮中發光，也揭開了天蠍滿滿強運的序幕。2018 可說是蠍座的平安好年，過往不論工作上、心靈上甚至感情上的風雨飄搖，到了今年總算塵埃落定，能依著穩健而實在的步伐向前踏進。"
    elif (who == 'Scorpio' and num == '2'):
        return "單身者能如願遇見心中的對象，但彼此能否長久維持，還得看兩人默契與包容。三月，七月，十一月的三次水星逆行，必會為你帶來工作面的刺激，過於高調張揚可能會在此時踢到鐵板，最好學著修正自己修正外在觀感的角度。"
    elif (who == 'Sag' and num == '1'):
        return "2018 射手的表現似乎有些腹背受敵，因鬆懈就容易陷入四面楚歌的境界，這一年裡事業上與你競爭衝突的人很多，因此工作上將有不少考驗，不只咬牙撐過還要贏過對手，你就多一層自我的修煉"
    elif (who == 'Sag' and num == '2'):
        return "這一年裡射手得收起大刺刺的模式，試著沈潛低調 ，小人運旺，四處結交盟友很可能交到小人，還不如獨善其身，積極充實自己的專業能力。"
    elif (who == 'Sag' and num == '3'):
        return "面對蜂擁而來的桃花運，別昏了頭而要清晰判斷，別為不正確的對象白花時間，到頭來會發現還不如把心思用在職場。"
    elif (who == 'Cap' and num == '1'):
        return "今年裡魔羯的福德宮就像點了光明燈，好運常在關鍵時從天而降，讓你建築出了更踏實的信心。你可以坐享眼前的種種好事，但也可以選擇把握機會挑戰更好的境界，要的是膽大心細的野心。"
    elif (who == 'Cap' and num == '2'):
        return "這一年裡雖然好運不請自來，但隨之而來的麻煩也不少， 最好的方式是處變不驚然後八面玲瓏的應對，耐心之外還要靠交際力與人緣來化解。"
    elif (who == 'Cap' and num == '3'):
        return "逢水金輪替雙逆的十一月前後，是財務問題最大的時間點，投資與支出都不要情緒化做決定，否則會難以收拾。"
    elif (who == 'Aquarius' and num == '1'):
        return "水瓶的交際宮位很忙碌，老友新友的頻繁邀約讓你時刻不得閒，但偏偏田宅宮的星象角度移轉又時時提醒著你，人際關係就是財路，你非得要花時間去交際應酬"
    elif (who == 'Aquarius' and num == '2'):
        return "在面對別人練習自我多面相的同時，也可從中好好觀測自己到底適合展現哪種對外的性格，也許能發掘出自己新的一面。"
    elif (who == 'Aquarius' and num == '3'):
        return "而感情世界較多起伏，過去一直被忽略或被掩蓋的事實很可能慢慢浮現，對於未來該下個決定了；事業有向外拓展的機會，不過屬於好運的部分稍蹤即逝，可別再猶豫了。"
    elif (who == 'Pisces' and num == '1'):
        return "天馬行空的爆發力與才華，往往是魚座運勢中的籌碼，這一年裡木星掌握遷移宮，可以讓你的思考變得更活躍、更有彈性，也有很好的出差與旅遊運"
    elif (who == 'Pisces' and num == '2'):
        return "但在因才華綻放而受注目的同時，也為此付出代價，身邊隨時都有小人環伺，你得試著與邪惡和平共處，最好的方式不是宣戰而是無視他們存在地做好自己。"
    elif (who == 'Pisces' and num == '3'):
        return "今年的同事感情充滿著挑戰，所以面對辦公室風暴是少不了的課題，如何站在對的一邊，錢財才能跟你共處，請謹記觀察風向球選對邊的道理。"

        




































