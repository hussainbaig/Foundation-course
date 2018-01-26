### Following Links in Python

The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.

We provide two files for this assignment.

Problem 1: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html <br/>
Find the link at position 3 (index 2). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.<br/>
Sequence of names: Fikret Montgomery Mhairade Butchi Anayah <br/>
Last name in sequence: Anayah<br/>

Problem 2: Start at: http://py4e-data.dr-chuck.net/known_by_Rajwinder.html <br/>
Find the link at position 18 (index 17). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.<br/>
Hint: The first character of the name of the last page that you will load is: K

**Strategy**<br/>
The web pages tweak the height between the links and hide the page after a few seconds to make it difficult for you to do the assignment without writing a Python program. But frankly with a little effort and patience you can overcome these attempts to make it a little harder to complete the assignment without writing a Python program. But that is not the point. The point is to write a clever Python program to solve the program.




Sample Execution:
<pre><code>
kapil@foundation:~/Foundation-course/Assignments/12_scraping$ python3 ex_1202_kv.py 
Enter URL: http://py4e-data.dr-chuck.net/known_by_Fikret.html
Enter count: 4
Enter position: 3
Retrieving: http://py4e-data.dr-chuck.net/known_by_Fikret.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Montgomery.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Mhairade.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Butchi.html
The final name is: Anayah
</code></pre>
