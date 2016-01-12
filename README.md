# Auto-Flight-Check-In
<hr>
Have you ever wanted to automatically check into your flight without having to pay the fees?

This utility can help you out with that!

####Dependencies
- [PhantomJS](http://phantomjs.org/download.html)
- Selenium 
- argparse

####Prep
```
$ pip install selenium
$ pip install argparse
```

####How to set up
The best way to set this up is using a cronjob. [Tutorial](https://www.digitalocean.com/community/tutorials/how-to-use-cron-to-automate-tasks-on-a-vps)

Easier way is to use a visual crontab [utility](http://www.corntab.com/pages/crontab-gui).

The cronjob must be set up to exactly 24 hours before your flight. 

Use the following command
```
/usr/bin/python /path/to/checkin.py <firstName> <lastName> <confirmationNumber> 
```

Once generated, paste it into your crontab by running ```crontab -e```

####Example
If your name is John Smith, your confirmation number is 5GXHD and your flight is at 8:00 PM on 1/3/2016 then your command should be set to run at 8:00 PM on 1/2/2015. This line shoud be pasted into your crontab
```
0 20 2 1 * /usr/bin/python /path/to/checkin.py John Smith 5GXHD
```
Please make sure to comment out or remove the line after you're checked in. 
