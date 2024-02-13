#!/usr/bin/env python
import json
import fileinput
# input comes from STDIN (standard input)

for file in fileinput.input():
    try:
        data = json.loads(file)
        if 'retweeted_status' in data:
            continue
        else:
            visited = []
            words = data['text'].split()
            for word in words:
                if word.lower() == 'hon' or word.lower() == 'han' or word.lower() == 'den' or word.lower() == 'det' or word.lower() == 'denna' or word.lower() == 'denne' or word.lower() == 'hen':
                    if word.lower() not in visited:
                        visited.append(word.lower())
                        print(word.lower(),1)
    except:
        #print('----------------------------------------------------------------------------')
        continue
