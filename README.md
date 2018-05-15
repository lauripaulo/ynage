# Ynage is Not Another Github Explorer

And it's a personal playground to explore Python and Django.

You can [try it in Heroku](https://ynage.herokuapp.com/)!

## What it does?

Not much actually. It just queries the github api using a wonderful 
python lib called 'pygithub'.

You need to inform a keyword and choose one of my favorite (hyped?) 
languages and click a button. The application will bring the top 5 
repositories it finds order by stars.

Once the the query results are back they are persisted in a database 
and you can browse the results. If you don't want to see a particular 
result you can delete it (or all of them if you do not like any of them).

Every time you search again the results will be merged. New entries 
will be added and entries already present will be updated.

You can also change the saved repositories using django 
[admin interface](https://ynage.herokuapp.com/admin/) with the 
user `admin` and password `ynageHeroku2018` (the functionality is 
free. Thanks Django!!!)

Pretty straightforward. Give it a try.

## Will it do anything else in the future?

Maybe, with more time it will show the repository owner. 
And it will probably have some kind of way to compare repositories.

If you have any suggestions I'll be glad to hear. You can find me 
in Twitter [@lauripaulo](https://twitter.com/lauripaulo).

Peace!

## Setting up in production

To protect sensible data in a production server some environment 
variables must be set:

- DJANGO_SECRET_KEY
- DJANGO_DEBUG

You can find more information on how to setup it in a production 
environment [here](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment).