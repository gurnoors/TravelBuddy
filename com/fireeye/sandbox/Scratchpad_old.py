
from redis import Redis
from rq import Queue

q = Queue(connection=Redis())


import sys

path = 'Users/gurnoorsinghbhatia/PycharmProjects/FireEye'
sys.path.insert(0, path)

import Utils

url = 'http://nvie.com'



result = q.enqueue(Utils.count_words_at_url, url)

if __name__ == '__main__':
    print Utils.count_words_at_url(url)