from django.shortcuts import render
from rest_framework import  views, status
from rest_framework.response import Response
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
import nltk
import wikipedia
import re
from .models import StopWord

class SentenceAnalyzeView(views.APIView):

    def post(self, request, *args, **kwargs):
        sentence = request.data["sentence"]
        # ノイズ除去
        for sw in StopWord.objects.all():
            remove_text = '\s' + sw.word + '\s'
            sentence = re.sub(remove_text, ' ', sentence)
        sentence = word_tokenize(sentence)
        fd = nltk.FreqDist(sentence)
        fd = fd.most_common(10)
        result = {}
        for word_and_count in fd:
            word = word_and_count[0]
            count = word_and_count[1]
            wiki_url = ""
            search_response = wikipedia.search(word)
            if search_response:
                print(word)
                print(search_response[0])
                try:
                    wiki_page = wikipedia.page(search_response[0])
                    wiki_url = wiki_page.url
                except wikipedia.DisambiguationError as e:
                    print(e)
                except wikipedia.PageError as e:
                    print(e)
        
            result[word] = [wiki_url, count]
        res_list = {
            'result': result
        }
        
        return Response(res_list, status=status.HTTP_200_OK)
