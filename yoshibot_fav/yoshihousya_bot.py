# coding:utf-8
import tweepy
import random

# 各種キーをセット
CONSUMER_KEY = "LoqNpuBFwxPMS9SLuhgrm1ino"
CONSUMER_SECRET = "ijYm0cE3e8oAcauQtFJ4ey1Ew7Tk4zzxnO9KBQodKiopKdKO1u"
ACCESS_TOKEN = "1022470594766360576-2ukqSvK3pePTSyeAAmNSdnt5swHUmC"
ACCESS_SECRET = "qMlJmvWWZMKT5DiUkx5avNJplcn0Px8HMHJIXcOSMYWSs"

#APIインスタンスを作成
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

#検索キーワード
#ここに検索キーワードを設定
q=["ブログ","音楽","youtuber","オンラインサロン","yahoo","副業","ウェブデザイナー","google","アドセンス","ブログ更新","ブログ仲間募集中","読書",
"英語","エンジニア","ブロガー","フリーランス","python","留学","読了","プログラミング","ラジオ","旅行","wordpress","newspicks","note","facebook",
"instagram","filmmarks","progate","音楽","youtuber","yahoo","ウェブデザイナー","アドセンス","英語","エンジニア","python","プログラミング",
"ラジオ","旅行","facebook"]

qq = q[random.randrange(len(q))]
print(qq)
#params={"status": randomtweet}
#print(params)

count = 20


search_results = api.search(qq, count=count)

for result in search_results:
            username = result.user._json['screen_name']
            user_id = result.id #ツイートのstatusオブジェクトから、ツイートidを取得
            #print(user_id)
            user = result.user.name #ツイートのstatusオブジェクトから、userオブジェクトを取り出し、名前を取得する
            #print(user)
            tweet = result.text
            #print(tweet)
            time = result.created_at
            #print(time)
            try:
                api.create_favorite(user_id) #ファヴォる
                print(user)
                print("をライクしました")
                api.create_friendship(user_id)
                print("をフォローしました")
            except:pass
            print("もうすでにふぁぼかフォローしてますわ")
            #print("##################")

