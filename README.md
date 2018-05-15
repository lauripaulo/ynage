# Ynage is Not Another Github Explorer

And it's a personal playground to explore Python and Django.

You can <a href='https://ynage.herokuapp.com/' target='_blank'>try it in Heroku</a>!

<h2>What it does?</h2>

Not much actually. It just queries the github api using a wonderful python lib called 'pygithub'.

You need to inform a keyword and choose one of my favorite (hyped?) languages and click a button. The application will bring the top 5 repositories it finds order by stars.

Once the the query results are back they are persisted in a database and you can browse the results. If you don't want to see a particular result you can delete it (or all of them if you do not like any of them).

Every time you search again the results will be merged. New entries will be added and entries already present will be updated.

You can also change the saved repositories using django <a href='https://ynage.herokuapp.com/admin/' target='_blank'>admin interface</a> with the user 'admin' and password 'ynageHeroku2018' (the functionality is free. Thanks Django!!!)

Pretty straightforward. Give it a try.

<h2>Will it do anything else in the future?</h2>

Maybe, with more time it will show the repository owner. And will have some kind of way to compare repos.

If you have any suggestions I'll be glad to hear.

Peace!

<h3>Setting up in production</h3>

To protect sensible data in a production server some environment variables must be set:

- DJANGO_SECRET_KEY
- DJANGO_DEBUG