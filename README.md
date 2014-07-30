imdb scraper 
=================================================================

.: Get movie statistics data for further development :.

This software retrieves the synopsis of the movie and creates a dictionary with all words used plus their frequency 
from the `Internet Movie Database `<http://www.imdb.com/>`_.


Installation and requirements
-----------------------------

- Python 3.3
- BeautifulSoup 4

- Tested on a virtualenv 


Usage
-----

The software has been setup to print all words that are over 5 characters long and appear over 15 times in the synopsis.

    python imdb_scraper.py
    
    No titles found, input via console:
    Enter movie names, separated by comma: matrix
    ===============================Starting to scrape==============================
    - Got html from website
    - Scanning for data in movielink: http://www.imdb.com/title/tt0133093/
    - Synopsis url is: http://www.imdb.com/title/tt0133093/synopsis
    * Found: [1644] unique words out of [6586]
    104 Morpheus
    62 Trinity
    44 Matrix
    33 Cypher
    31 Agents
    17 Oracle
    12 himself
    11 building
    10 through
    9 humans
    8 inside
    8 appears
    8 replies
    7 trying
    7 before
    ----------------------------------------------------------------------------------------------------
    
License
-------
::
    Copyright (c) 2014 hyp3rkyd
   
    Permission is hereby granted, free of charge, to any person
    obtaining a copy of this software and associated documentation
    files (the "Software"), to deal in the Software without
    restriction, including without limitation the rights to use,
    copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the
    Software is furnished to do so, subject to the following
    conditions:
   
    The above copyright notice and this permission notice shall be
    included in all copies or substantial portions of the Software.
   
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
    OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
    NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
    HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
    WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
    OTHER DEALINGS IN THE SOFTWARE.
