from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import tkinter
from tkinter import *
from tkinter import ttk
import sys

# make sure that this is the correct location for your chrome drivers

path = "/opt/homebrew/bin/chromedriver"

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
    global ui_username,ui_password
    title.config(fg="#7faaab",text="Follower Bot")  
    try:
        driver = webdriver.Chrome(path,chrome_options=options)
    except:
        title.config(fg="#990000",text="PATH Error")
        return
    # base url
    driver.get("http://github.com/login")

    username = driver.find_element_by_id("login_field")
    password = driver.find_element_by_id("password")

    # password and username need to go into these values
    username.send_keys(ui_username.get())
    time.sleep(1)
    password.send_keys(ui_password.get())
    time.sleep(1)

    login_form = driver.find_element_by_xpath("//input[@value='Sign in']")
    time.sleep(1)
    login_form.click()
    time.sleep(1)

    # These are some of the most popular users on github
    prepend = ["jashkenas", "ruanyf", "substack", "kennethreitz", "jlord", "daimajia", "mdo", "schacon", "mattt",
               "sindresorhus", "defunkt", "douglascrockford", "mbostock", "jeresig",
               "mojombo", "addyosmani", "paulirish", "vczh", "romannurik", "tenderlove", "chriscoyier", "johnpapa",
               "josevalim",
               "charliesome", "CoderMJLee", "ry", "antirez", "muan", "isaacs", "angusshire",
               "hadley", "hakimel", "yyx990803", "fat", "fabpot", "ibireme", "tekkub",
               "BYVoid", "laruence", "onevcat", "tpope", "mrdoob", "LeaVerou", "chrisbanes", "wycats", "lifesinger",
               "cloudwu", "mitsuhiko", "michaelliao", "ryanb", "clowwindy", "JacksonTian", "yinwang0", "Trinea",
               "pjhyett", "dhh", "gaearon"]

    for user in prepend:
        for t in range(1, 100):
            # Switches follower page - for new users to follow        
            string = "https://github.com/{}?page={}&tab=followers".format(user,t)
           
            driver.get(string)
            time.sleep(1)
            
            if(following):
                follow_button = driver.find_elements_by_xpath("//input[@value='Follow']")
            else:
                follow_button = driver.find_elements_by_xpath("//input[@value='Unfollow']")
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
ui_password= PlaceholderEntry(root, "Enter Passoword",textvariable=passw,font="Geneva 30 bold",justify=CENTER)
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