'''
selenium was developed by jason huggins in 2004, thoughworks but managed by google
it was given a name as javascript test runner but renamed to selenium to irradicate or remove its competetor called 
qtp which worked on mercury interractive developed by hp .


components of selenium 


1.selenium ide
record and playback tools
limited to browser and language


2.selenium rc remote control
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


locator:  method used to find HTML elements.
types:

id
Locates element by its unique id attribute.
driver.find_element(By.ID, "username") 

name
Finds element using the name attribute.
driver.find_element(By.NAME, "email")

class name
Identifies elements by their class attribute.
driver.find_element(By.CLASS_NAME, "btn")

tag name 
Selects elements based on their tag (like input, div, a).
driver.find_elements(By.TAG_NAME, "input")

link text
Finds anchor (<a>) tags using exact link text.
driver.find_element(By.LINK_TEXT, "Login")

partial link text
Locates link using partial matching text.
driver.find_element(By.PARTIAL_LINK_TEXT, "Log")

css selector
Selects elements using CSS-style selectors.
driver.find_element(By.CSS_SELECTOR, "div#login input[type='text']")

x path
Uses XML path language to navigate the DOM.
driver.find_element(By.XPATH, "//input[@id='username']")

find.element()- single element
find.elements()- list of elements- takes 2 arguement -- locator name`
                                                        value

x path has 2 types:
1.absolute path --- specific path of ele by traversing from parent tag to child tag ele
2.relative path----- starts from parent node/tag starts with "/" it uses only tag names
specify path of the directly using some attributes of that ele
it directly jumps to ele
starts with '//'
it uses mainly attribute also tagname
//tagname[@attribute.name='attribute_value']

y rel xpath is preffered?????
it is efficient and takes less instructions
developer when adds or remove anything from webpage the absolute xpath will be broken

rel xpath
using attribute "//tagname[@att_name='att_val']"
using text()    "//tagname[text()='text_of_ele']"
using contains()  "//tagname[contains(source,'val')]"
using starts-with() "//tagname[starts-with(source,'val')]"


//input[contains(@id,'ab')]
//button[contains(@type,'a')]
//a[contains(text(),'s')]
//button[contains(text(),"selenium")]
//*[not(@class)]
//button[@id or contains(@class,"abc")]
//a[starts-with(text(),"python")]
//input[contains(@id) and contains(@name)]
//*[contains(@id,"a") and starts-with(@name)]



tagname -all select=*
//*[contains(@id)] or //*[@id]

Browser commands
close()- it used to close single window wherever driver is focused .
quit()- it will kill all the windows.


'''