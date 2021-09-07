from django.shortcuts import render
from rest_framework import views, status
from rest_framework.response import Response
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
import nltk
import wikipedia
import re
from .models import StopWord
from nltk.corpus import stopwords
from nltk.tag import pos_tag


class SentenceAnalyzeView(views.APIView):
    def post(self, request, *args, **kwargs):
        lem = WordNetLemmatizer()

        result = {}
        if request.data.get("sentence") is not None:

            word_tokens = word_tokenize(request.data["sentence"])

            # 正規化
            lemmatized_sentence = []
            for word, tag in pos_tag(word_tokens):
                if tag.startswith("NN"):
                    pos = "n"
                elif tag.startswith("VB"):
                    pos = "v"
                else:
                    pos = "a"
                lemmatized_sentence.append(lem.lemmatize(word, pos))

            # ノイズ除去
            filtered_sentence = []
            default_stop_words = set(stopwords.words("english"))
            db_stop_words = [sw.word for sw in StopWord.objects.all()]
            for w in lemmatized_sentence:
                if w not in default_stop_words and w not in db_stop_words:
                    filtered_sentence.append(w)

            common_10_words = (nltk.FreqDist(filtered_sentence)).most_common(10)

            for word_and_count in common_10_words:
                word = word_and_count[0]
                count = word_and_count[1]
                wiki_url = ""
                search_response = wikipedia.search(word)
                if search_response:
                    try:
                        wiki_page = wikipedia.page(search_response[0])
                        wiki_url = wiki_page.url
                    except wikipedia.DisambiguationError as e:
                        print(e)
                    except wikipedia.PageError as e:
                        print(e)

                result[word] = [wiki_url, count]
        res_list = {"result": result}

        return Response(res_list, status=status.HTTP_200_OK)
