# uvic_course_archiver

***A web crawler that downloads all course handouts (pdf,doc,etc.) on CourseSpaces.**


***PROBLEM: Files are downloaded into the wrong local folder!

Put each handouts into a folder of its course name.

Require Scrapy to be installed.
```
pip install scrapy
```

How to use:

1. Download this program and extract it into a folder.
2. In the extracted folder, navigate to ```/coursespace/spiders/login.py```
3. Open the terminal in this directory
4. Run the program with ```scrapy runspider login.py```
5. Wait for the program to initialize until you're asked to enter your```NetLinkID and password``` in the terminal
6. Wait til all files are downloaded. **Probably will take a while!!
