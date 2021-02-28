# memesapp
Display memes to user post login

Here is some details about app - 
1) User will be landed on login page. If user enters valid details, user gets logged in successfully. Else user will stay to login page.
2) Post login, user is redirected to dispaly memes. These memes are requested from other site. 

----------------------------------------------------------------------------------------------------------------------------------------------------------------


Below are some steps provided to host app on Heroku - 

1)Create test account in Heroku 
2)Create app using option in website or create app using command line (for command line we need heroku toolbelt. Kind of utility allows your local host to communicate to heroku server)
3)run command- 
heroku login 

4)heroku create memesapp (cmd to create app) 

5)cmd to list all apps -
heroku apps

6)create below additional files for initial setup- 
-requirement.txt -> dependecies for python app
(install gunicorn module as well so heroku can handle http request)

-Procfile -> to let heroku know use gunicorn for web requests 

-runtime.txt -> to specify python version heroku should use 

6)upload project files to heroku using git - 

git init --> initialize repo 
git add . --> add files in current dir
git commit -m "commit"

heroku git:remote --app memesapp --> specify heroku app name 

git config --global user.email "emailid"
git config --global user.name  "name"

git push heroku master 

7) heroku open 

open app in browser


