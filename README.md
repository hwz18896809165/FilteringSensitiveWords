# FilteringSensitiveWords
This is an interface for filtering sensitive words. It currently runs at http://129.211.4.177:3000/. You can call this interface by URL + ‘keywords = your sentence’. After calling, it will return the sensitive words contained and help you filter them out.Techniques used:python,tornado,DFA

What's the biggest difference from direct comparison strings and regular substitution?
It uses DFA algorithm for modeling and searching，greatly improve the search efficiency.

Now the project is running in:http://129.211.4.177:3000，here is an example of calling this interface:

import urllib.request

import urllib.parse

import json

def get_api_data(key):
    
    # 指定api地址   
    url = "http://129.211.4.177:3000/search?%s"
    api_url = url % ("keywords=%s"%urllib.parse.quote(key))
    response = urllib.request.urlopen(api_url)
    print(json.loads(response.read().decode('utf-8')))

    
get_api_data(input("key:"))

test：

key:你说了敏感词

[['敏感词'], '你说了***']

Attached is a sensitive list of 5000 words.