# Name

頻出単語調査アプリ

# DEMO

[こちらにアクセス](https://com-word-app-ver-2.herokuapp.com/)

# Features

文章を入力すると，頻出単語が上から10個グラフで表示されます．  
また，棒グラフをクリックすると，その単語に関連するwikipediaのページへ飛びます.（関連するwikipediaがある場合のみ)  
自分が研究室で論文を読んでいて，頻出単語（大事な単語）をすぐチェックできるアプリがあったらいいなと思い，作りました．



# Requirement

- Docker
- Docker Compose

# Installation

https://docs.docker.jp/get-docker.html

# Usage

- `git clone https://github.com/mayukorin/com_word_app_ver_2.git`
- docker-compose.yml の front: 内にある `command: "npm run serve"` をコメントアウト
- `docker-compose up`
- `docker exec -it com_word_app2_front_1 bash` で frontのコンテナ内に入る
- コンテナ内で `npm install`
- `exit` でコンテナを出る
- 先ほどのコメントアウトを外して，`docker-compose up --build`



