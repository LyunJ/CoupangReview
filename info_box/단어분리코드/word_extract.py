# from konlpy.tag import Kkma
from konlpy.tag import Okt

# kkma = Kkma()
okt = Okt()

# import sys
# import os
import re
# sys.path.append(os.path.dirname('PyKoSpacing/'))
# from pykospacing import spacing

def preprocessing(review,name):
    total_review = ''
    #인풋리뷰
    for idx in range(len(review)):
        r = review[idx]
        #하나의 리뷰에서 문장 단위로 자르기
        sentence = re.sub(name.split(' ')[0],'',r)
        sentence = re.sub(name.split(' ')[1],'',sentence)
        sentence = re.sub('\n','',sentence)
        sentence = re.sub('\u200b','',sentence)
        sentence = re.sub('\xa0','',sentence)
        sentence = re.sub('([a-zA-Z])','',sentence)
        sentence = re.sub('[ㄱ-ㅎㅏ-ㅣ]+','',sentence)
        sentence = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]','',sentence)
        if len(sentence) == 0:
            continue
        sentence = okt.pos(sentence, stem = True)
        word = []
        for i in sentence:
            if not i[1] == 'Noun':
                continue
            if len(i[0]) == 1:
                continue
            word.append(i[0])
        word = ' '.join(word)
        word += '. '
        total_review += word
    return total_review

from krwordrank.sentence import summarize_with_sentences

st = ''
test = ['여운이 크게남는영화 엠마스톤 너무 사랑스럽고 라이언고슬링 남자가봐도 정말 매력적인 배우인듯 영상미 음악 연기 구성 전부 좋았고 마지막 엔딩까지 신선하면서 애틋하구요 30중반에 감정이 많이 메말라있었는데 오랜만에 가슴이 촉촉해지네요',
 '영상미도 너무 아름답고 신나는 음악도 좋았다 마지막 세바스찬과 미아의 눈빛교환은 정말 마음 아팠음 영화관에 고딩들이 엄청 많던데 고딩들은 영화 내용 이해를 못하더라ㅡㅡ사랑을 깊게 해본 사람이라면 누구나 느껴볼수있는 먹먹함이 있다',
 '정말 영상미랑 음악은 최고였다 그리고 신선했다 음악이 너무 멋있어서 연기를 봐야 할지 노래를 들어야 할지 모를 정도로 그리고 보고 나서 생각 좀 많아진 영화 정말 이 연말에 보기 좋은 영화 인 것 같다',
 '무언의 마지막 피아노연주 완전 슬픔ㅠ보는이들에게 꿈을 상기시켜줄듯 또 보고 싶은 내생에 최고의 뮤지컬영화였음 단순할수 있는 내용에 뮤지컬을 가미시켜째즈음악과 춤으로 지루할틈없이 빠져서봄 ost너무좋았음',
 '처음엔 초딩들 보는 그냥 그런영화인줄 알았는데 정말로 눈과 귀가 즐거운 영화였습니다 어찌보면 뻔한 스토리일지 몰라도 그냥 보고 듣는게 즐거운 그러다가 정말 마지막엔 너무 아름답고 슬픈 음악이 되어버린',
 '정말 멋진 노래와 음악과 영상미까지 정말 너무 멋있는 영화 눈물을 흘리면서 봤습니다 영화가 끝난 순간 감탄과 동시에 여운이 길게 남아 또 눈물을 흘렸던내 인생 최고의 뮤지컬 영화',
 '평소 뮤지컬 영화 좋아하는 편인데도 평점에 비해 너무나 별로였던 영화 재즈음악이나 영상미 같은 건 좋았지만 줄거리도 글쎄 결말은 정말 별로 6 7점 정도 주는게 맞다고 생각하지만 개인적으로 후반부가 너무 별로여서',
 '오랜만에 좋은 영화봤다는 생각들었구요 음악도 영상도 스토리도 너무나좋았고 무엇보다 진한 여운이 남는 영화는 정말 오랜만이었어요 연인끼리 가서 보기 정말 좋은영화 너뮤너뮤너뮤 재밌게 잘 봤습니다',
 '음악 미술 연기 등 모든 것이 좋았지만 마지막 결말이 너무 현실에 뒤떨어진 꿈만 같다 꿈을 이야기하는 영화지만 과정과 결과에 있어 예술가들의 현실을 너무 반영하지 못한 것이 아닌가하는 생각이든다 그래서 보고 난 뒤 나는 꿈을 꿔야하는데 허탈했다',
 '마지막 회상씬의 감동이 잊혀지질않는다마지막 십분만으로 티켓값이 아깝지않은 영화 음악들도 너무 아름다웠다옛날 뮤지컬 같은 빈티지영상미도 최고']
for r in range(len(test)): 
    b_idx = '제테크 실무'
    texts = preprocessing(test,b_idx)
    
    st += texts
    texts = st.split('. ')
    try:
            stopwords = {b_idx.split(' ')[0], b_idx.split(' ')[1]}
            keywords, sents = summarize_with_sentences(
                                                    texts, 
                                                    stopwords = stopwords,
                                                    num_keywords=100, 
                                                    num_keysents=10
                                                    )
    except ValueError:
            print('key가 없습니다.')
            print()
            continue
print(texts)
for word, r in sorted(keywords.items(), key=lambda x:x[1], reverse=True)[:7]:
#print('%8s:\t%.4f' % (word, r))
        print('#%s' % word)
print()
