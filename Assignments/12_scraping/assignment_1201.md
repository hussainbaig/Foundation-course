Scraping Numbers from HTML using BeautifulSoup<br/>

The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.

We provide two files for this assignment:

http://py4e-data.dr-chuck.net/comments_42.html (Sum = 2553)<br/>
http://py4e-data.dr-chuck.net/comments_64152.html (Sum = 2600)<br/>

You do not need to save these files to your folder since your program will read the data directly from the URL.

Hint: <br/>
Look at the source code(HTML) of each file. <br/>
Notice the tag within which you have the numbers. Try to extract those specific tags and their contents using BeautifulSoup.<br/>
Be careful of what the return type of each method is (string or a list or something else?).
