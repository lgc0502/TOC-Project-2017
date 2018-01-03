# Divination planet占卜星球chatbot
一個每天根據星座幫你快速分析今日運勢的好幫手
## 功能介紹
分成兩部分
- 每日星座運勢
  1. 整體運勢
  2. 愛情運勢
  3. 事業運
  4. 財運
- 2018年星座運勢分析
  1. 年度幸運色
  2. 唐立綺2018星座分析
## 程式執行環境
請裝好以下環境
```
sudo apt-get install python3-pip

sudo pip3 install flask 

sudo pip3 install transitions

sudo pip3 install python-telegram-bot

sudo apt-get update

sudo apt-get install graphviz pkg-config python-dev libgraphviz-dev


sudo pip3 install pygraphviz --install-option="--include-path=/usr/include/graphviz" --install-option="--library-path=/usr/lib/graphviz/" 
```
## 程式執行方式
```
python3 app.py
```

## Finite State Machine
![fsm](./show-fsm.png)

