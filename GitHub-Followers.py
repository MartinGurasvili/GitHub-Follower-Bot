from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import tkinter
from tkinter import *
from tkinter import ttk
import sys

# makes the driver run in background
options = Options()
options.add_argument('--headless')

root = Tk()
root.title("GitHub Follower Bot")


root.minsize(width=300, height=280)

title = Label(root, text='Follower Bot', fg="#7faaab", font="Helveca 40 bold",bg="#282828")
title.pack()


class PlaceholderEntry(ttk.Entry):
    def __init__(self, container, placeholder, *args, **kwargs):
        super().__init__(container, *args, style="Placeholder.TEntry", **kwargs)
        self.placeholder = placeholder

        self.insert("0", self.placeholder)
        self.bind("<FocusIn>", self._clear_placeholder)
        self.bind("<FocusOut>", self._add_placeholder)

    def _clear_placeholder(self, e):
        if self["style"] == "Placeholder.TEntry":
            self.delete("0", "end")
            self["style"] = "TEntry"

    def _add_placeholder(self, e):
        if not self.get():
            self.insert("0", self.placeholder)
            self["style"] = "Placeholder.TEntry"

def follow(following):
    global ui_username,ui_password,root,title
    title.config(fg="#7faaab",text="Follower Bot")  
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    except:
        title.config(fg="#990000",text="PATH Error")
        return
    # base url
    driver.get("http://github.com/login")

    username = driver.find_element(By.ID, "login_field")
    password = driver.find_element(By.ID, "password")

    # password and username need to go into these values
    username.send_keys(ui_username.get())
    time.sleep(1)
    password.send_keys(ui_password.get())
    time.sleep(1)

    login_form = driver.find_element(By.XPATH, "//input[@value='Sign in']")
    time.sleep(1)
    login_form.click()
    time.sleep(1)
    auth = driver.find_element(By.XPATH, '//*[@id="github-mobile-authenticate-prompt"]/h1')
    if((auth.text).isdigit()):
        title.config(fg="#7faaab",text="GH Mobile Code = "+auth.text)    
        root.update()
        try:
            while((auth.text).isdigit()):
                try:
                    root.update()
                    auth = driver.find_element(By.XPATH, '//*[@id="github-mobile-authenticate-prompt"]/h1')
                    print(auth.text) 
                    time.sleep(10)
                except:
                    break
        except:
            print("continue")
    
   
    
    # These are some of the most popular users on github
    prepend = [ "michaelliao", "ryanb", "clowwindy", "JacksonTian","ruanyf", "substack", "kennethreitz", "jlord", "daimajia", "mdo", "schacon", "mattt",
               "sindresorhus", "defunkt", "douglascrockford", "mbostock", "jeresig",
               "mojombo", "addyosmani", "paulirish", "vczh", "romannurik", "tenderlove", "chriscoyier", "johnpapa",
               "josevalim",
               "charliesome", "CoderMJLee", "ry", "antirez", "muan", "isaacs", "angusshire",
               "hadley", "hakimel", "yyx990803", "fat", "fabpot", "ibireme", "tekkub",
               "BYVoid", "laruence", "onevcat", "tpope", "mrdoob", "LeaVerou", "chrisbanes", "wycats", "lifesinger",
               "cloudwu", "mitsuhiko","yinwang0", "Trinea","jashkenas",
               "pjhyett", "dhh", "gaearon"]

    for user in prepend:
        for t in range(1, 100):
            # Switches follower page - for new users to follow        
            string = "https://github.com/{}?page={}&tab=followers".format(user,t)
           
            driver.get(string)
            time.sleep(1)
            
            if(following):
                follow_button = driver.find_elements(By.XPATH,"//input[@value='Follow']")
                title.config(fg="#7faaab",text="Following..")  
                root.update() 
            else:
                follow_button = driver.find_elements(By.XPATH,"//input[@value='Unfollow']")
                title.config(fg="#7faaab",text="Unfollowing..")  
                root.update() 
            print("on page",t)   
            # Once page is loaded this clicks all buttons for follow
            if (len(follow_button) !=0):
                try:
                    for i in follow_button:
                        time.sleep(0.1)
                        i.submit()
                except:
                    
                    pass
                time.sleep(1)
            else:
                print("error")
                errorr()
                
                
def errorr():
    title.config(fg="#990000",text="Login Error")       
    #error made on purpose to stop program - to update text         
    driver.close()
    title.config(fg="#990000",text="Login ")  
    


space = Label(root, text=' ', fg="#898989", font="Helveca 5 bold",bg="#282828")
space.pack()
user=""
style = ttk.Style(root)

style.configure("Placeholder.TEntry", foreground="white",background="#282828")
ui_username = PlaceholderEntry(root, "Enter Username Or Email",textvariable=user,font="Geneva 30 bold",justify=CENTER)
ui_username.pack()

space2 = Label(root, text=' ', fg="#898989", font="Helveca 1 bold",bg="#282828")
space2.pack()

passw=""
ui_password= PlaceholderEntry(root, "Enter Password",textvariable=passw,font="Geneva 30 bold",justify=CENTER)
ui_password.pack()

space3 = Label(root, text=' ', fg="#898989", font="Helveca 2 bold",bg="#282828")
space3.pack()

f = Button(root,text ="Follow", fg="#282828",command=lambda:follow(True), font="Geneva 30 bold",bg='#282828',activebackground='#282828',highlightbackground="#288888",disabledforeground="#288888",justify=CENTER)
f.configure(bg='#282828',width = 20)
f.pack()
uf = Button(root,text ="Unfollow", fg="#282828",command=lambda:follow(False), font="Geneva 30 bold",bg='#282828',activebackground='#282828',highlightbackground="#288888",disabledforeground="#288888",justify=CENTER)
uf.configure(bg='#282828',width = 20)
uf.pack()
root.attributes("-alpha", 0.90)
root.configure(background="#282828")

root.mainloop()