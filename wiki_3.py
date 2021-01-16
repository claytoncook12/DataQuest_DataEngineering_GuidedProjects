import concurrent.futures
from bs4 import BeautifulSoup
import time
import json
from collections import Counter
import re

def word_count_ext(html):
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text().lower()
    c = Counter(re.findall(r'[a-z]{5,}', text))
    return c

def main():
    
    # Read in data file
    with open('wiki_content_extracted.txt', 'r', encoding='utf-8') as f:
        content = json.load(f)
    
    process_pool = [1,2,3,4,5,6]
    
    for num in process_pool:
        c = None
        start = time.time()
        pool = concurrent.futures.ProcessPoolExecutor(max_workers=num)
        word_count = pool.map(word_count_ext,content)
        word_count = list(word_count)
        end = time.time() - start
        print("Time of {} processes: {:0.2f} secs".format(num,end))
        
    # Write out word_count file
    with open('wiki_word_count.txt', 'w', encoding='utf-8') as f:
        json.dump(word_count, f)
        
if __name__=='__main__':
    main()
