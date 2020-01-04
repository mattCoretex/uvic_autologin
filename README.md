# uvic_course_archiver

***A web crawler that downloads all course handouts on CourseSpaces.***

***PROBLEMs: 
  a) Might not be able to download all types of files yet (.pdf is OK so far).
  b) Might skip some course or handouts.

Put each handouts into a folder of its course name.
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


**Remember to Crawl Responsibly and Don't Harm the Website!!**
