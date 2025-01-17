This creates a calendar for your class schedule to import into google/apple/ms calendar

prepare the file 

1. download the python file
2. if you haven't installed python, do this, else skip to step 5:
3. open powershell: Win + R , type "powershell", then enter
4. in powershell type: "pip install python"

Now setup the file

5. open the python file in your code editor, like vscode
6. Where you see semester start and end date, adjust to the beginning and end of your semester
7. Where you see the list classes, change the classes to your class details and add sections as needed, following the existing format
8. Where you see file_path, adjust to where the filepath you want to save the .ics calendar file

run the file

9. in powershell, navigate to the directory where you saved the python file using "cd" (ex. cd C:/users/user123/Desktop/where/the/file/is)
10. in powershell type: "python makeClassSchedule-v2-pub.py" or whatever you renamed the file to
11. if it's says done, then the .ics is saved. 
12. go into your calendar app and import the calendar. 
13. all done.
