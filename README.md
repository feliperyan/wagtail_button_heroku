#Wagtail Heroku Button

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://github.com/feliperyan/wagtail_button_heroku)

Deploy this guy, then git clone locally:

```
$ heroku git:clone -a your-heroku-app-name
$ cd your-heroku-app-name
```

Make your changes and push it back up:

```
$ git add .
$ git commit -am "make it better"
$ git push heroku master
```

##Todo:

Get media storages to work with S3, right now the AWS S3 env vironments are there but don't do anything...