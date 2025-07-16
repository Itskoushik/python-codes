'''
selenium was developed by jason huggins in 2004, thoughworks but managed by google
it was given a name as javascript test runner but renamed to selenium to irradicate or remoce its competetor called 
qtp which worked on mercury interractive developed by hp .


components of selenium 


1.selenium ide
record and playback tools
limited to browser and language


2.selenium rc
supports multiple browser and lang and os
without server we cant interact with script to browser

3.selenium web drivers
supports multiple lang,browser and os
works serverless

4.selenium grid
it is basically used to test the application on different platforms like chrome ,windows or edge,linux or firefox on mac

selenium webdriver architecture 
                                                          http
python                    w3c protocol             chrome -->   chrome  
java                                               edge         edge                              
php                                                firefox <--- firefox
                                                          http

client library            web driver                 driver    browser


from selenium import webdriver
'''