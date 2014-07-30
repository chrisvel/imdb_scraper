import urllib.request
from bs4 import BeautifulSoup
import re
import collections
from string import punctuation
 
class MovieScraper:
    """Scrapes movie data from imdb"""
    def __init__(self, titles=None):
        self.titles = titles
        if self.titles == None:
            print('No titles found, input via console:')
            self.run_input()
 
    def scrape(self):
        """Runs the main script"""
        for title in self.titles:
            try:
                movie = '+'.join(title.split())
 
                movie_search_url = 'http://www.imdb.com/find?q={movie}&s=all'.format(movie=movie)
                movie_soup = BeautifulSoup(urllib.request.urlopen(movie_search_url))
                print('- Got html from website')
 
                movie_link = movie_soup.find('a', href=re.compile('title/(.*?)/'))['href']
                movie_id = re.findall('title/(.*?)/', movie_link)[0]
                new_movie_link = 'http://www.imdb.com/title/{}/'.format(movie_id)
 
                print('- Scanning for data in movielink: {}'.format(new_movie_link))
 
                movie_url = "{}synopsis".format(new_movie_link)
                print('- Synopsis url is: {0}'.format(movie_url))
                synopsis_page = urllib.request.urlopen(movie_url)
                synopsis_soup = BeautifulSoup(synopsis_page.read())
                synopsis_text = synopsis_soup.find(id='swiki.2.1').text
                
                # strip words from punctuation marks
                movie_word_list =re.findall(r'\w+',synopsis_text)
  
                word_dict={}
                for word in set(movie_word_list):
                    word_dict[word] = movie_word_list.count(word)
                    
                # count unique words and put them in a dict    
                unique_words_dict = collections.Counter(movie_word_list)
                
                print('* Found: [' + str(len(unique_words_dict)) + '] unique words out of [' 
                    + str(len(movie_word_list)) + ']')
                for word, count in unique_words_dict.most_common(): 
                    if count > 15 & len(word) > 5:
                        print (count, word)
                    
            except KeyboardInterrupt:
                print('You cancelled the operation.')
                break
            else:
                pass
            print("-".center(100, '-'))
 
 
    def run_input(self):
        """Gets movie names from user input and parses them to self."""
        movies = [item.strip() for item in input("Enter movie names, separated by comma:").split(',')]
        self.titles = movies
        print("Starting to scrape".center(79, '='))
        self.scrape()
 
if __name__ == '__main__':
    movie_obj = MovieScraper()