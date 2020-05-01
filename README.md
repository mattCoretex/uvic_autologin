# CourseSpaces Scraper

***A web crawler that downloads all course handouts on UVic CourseSpaces.***

**To do:

 - Download all files other than .pdf
 - Create a user-friendly login GUI.



<br>
<br>
Require Scrapy to run.
```
pip install scrapy
```
see https://scrapy.org/
<br>
<br>
How to use:

1. Download this program and extract it into a folder.
2. In the extracted folder, navigate to ```/coursespace/spiders/login.py```
3. Open the terminal in this directory
4. Run the program with ```scrapy runspider login.py```
5. Wait for the program to initialize. Then enter your```NetLinkID and password``` in the terminal
6. Wait til all files are downloaded.
7. Folders containing handouts should be generated in ```/coursespace/spiders/login.py```



## Disclaimer:

This scraper should only be used as a learning tool only. 
It's the responsibility of the user who deploys this scraper to know what you're doing is legal and doesn't harm the website.
