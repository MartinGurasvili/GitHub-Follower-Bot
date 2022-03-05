

<h1 align="center">GitHub Follower Bot</h1>

<div align="center">
  <a href="https://github.com/MartinGurasvili/Python-GitHub-Follower-Bot">
    <img width="200" height="200" alt="cas" src="https://user-images.githubusercontent.com/76784461/156901083-8fb10d9d-4509-4f55-a071-6d0d3faed233.png">
  </a>
 <p> </p>

<p align="center">
    <br>
    This is an ui based tool to increase your GitHub following
    <br />
    <br>
    <a href="https://github.com/MartinGurasvili/Python-GitHub-Follower-Bot/releases/download/v1.0.0/GitHub-Followers.py"><h3>Try it now</h3></a>
    <br/>
</div>
<div align="center">
    <img style="width:60%"  alt="Screenshot 2022-02-26 at 7 11 24 pm" src="https://user-images.githubusercontent.com/76784461/156902360-38036981-2cf7-4e67-93d1-0717f2239f80.png">
  </div>



<h1 align="center" >Features </h1>
<br></br>

   - [ ] Error Detection
   - [ ] Simple UI
   
   - [ ] Quickly increase your github following by following people from the most followed on github, thus more likely to follow.
   
   - [ ] Easy Setup
   - [ ] Human Simulation - to eliminate githubs spam detection
   - [ ] Both Follower and Unfollower tools built into one
   - [ ] Runs in background
   
   
<br></br>
<h1 align="center" >Setup </h1>
<br></br>
<h2>Mac Install</h2>
First we need to install homebrew - paste this command into the terminal

 `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
   
After that paste these two lines

 `brew tap homebrew/cask`  
`brew cask install chromedriver`  

Now you need to import the python libaries

 `pip install selenium`
`pip install tkinter`

Now you can run the script

<h2>Windows Install</h2>
First Download ChromeDrivers from https://chromedriver.storage.googleapis.com/index.html

once that is done open the file and modify the 11th line

`path = "/opt/homebrew/bin/chromedriver"`

To the location of your driver

Now you need to import the python libaries

 `pip install selenium`
`pip install tkinter`

Now you can run the script

<br></br>
<h1 align="center" >Error Fixes </h1>
<br></br>
<h3>Login Error Fix</h3>
This means that the password or email you have entered is incorrect - please double check your details
<div align="center">
    <img style="width:40%" src="https://user-images.githubusercontent.com/76784461/156901634-380952bb-3479-45ce-b9c7-06a81734a768.png">
  </div>
 <br></br>

  <h3>PATH Error Fix</h3>
This means that the installation of the Chrome drivers was done incorrectly or that the drivers are stored in a different location to the default 
<div align="center">
    <img style="width:40%" src="https://user-images.githubusercontent.com/76784461/156901670-13c2d1a7-2010-4eb2-8b04-7fb5823f8ee7.png">
  </div>
 
 To fix this error
 Modify the 11th line of the python file

`path = "/opt/homebrew/bin/chromedriver"`

To the location of your driver

<br></br>
