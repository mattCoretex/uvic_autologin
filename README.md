# uvic_coursespaces_archiver

***A web crawler that downloads all course handouts on CourseSpaces.***

***PROBLEM: 
  + Might not be able to download all types of files yet (.pdf is OK so far).



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
5. Wait for the program to initialize until you're asked to enter your```NetLinkID and password``` in the terminal
6. Wait til all files are downloaded. **Probably will take a while!!
7. Folders containing handouts should be generated in ```/coursespace/spiders/login.py```



## Disclaimer:

This scraper should only be used as a learning tool only. 
It's the responsibility of the user who deploys this scraper to know what you're doing is legal and doesn't harm the website.
