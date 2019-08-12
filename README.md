# BLACKNESS

## Researching or interested to find oout more about black history, your roots?
## Want to learn more about your culture and its vast heritage?
## Would you like to buy inspirational artworks by artist working in the community related to Black History?

This website is aimed at providing knowlege and useful resources and links to those people who would be 
interested in Black studies, Afro- American, Caribbean, Black British, and Black Europen culture. Also on this website you can upload current day people who you believe are making a valid contribution to improving the areas and society we live in. There is a voting system in place and awards/ recognition will
will be given to those with most likes/recommendations, as an act of support and acknowledgement for the good work being done.

### SEARCH the BLACKNESS database
search the main historical database by Surname, Nationality & Profession to find the known and forgotten histories of
African heritage around the world and its contribution to the society that we live in today. 

You can also access the the ´Local Heros´ database to view and vote for people working in the local communities,
supporting and nuturing them and creating positive values and visions for the future. You can also nominate your own local hero and
enter them into our database for awards.

### WEBSITE SPECIFICATIONS
This website is built using HTML5 & CSS for structure and styling. Some Javascript & Jquery comes into play when  loading the 
pages and to make the animations work. Flask and Mongo Db are used to implement and manipulate the 2 databases that are in function.
Jinja is also used to help display and create a better functionality in the backend.


### TESTING: 
These are some of the error I have found whilst creating the website and after giving access to it to family and friends.
>INPUT FORM -   when inputting a test element in ´add local hero´, oversized image did not adjust to the card element and completely disrupted the page.
>               Also found that when editing, rather than updating it is creating a new entry- fixed.
>               When resizing viewport - the title in the NavBar doesn´t stay within it- changed it back to original presets.
>               If  is 'Enter' was accidently pressed the form would send and an incomplete entry  would be place in the Database. I have now put ´required´
                onto each input, however, this does not stop visitors inputting a word rather than an image.

-Bootstrap & Materialize 
                don´t function well togther and I had to test mixing elements but Materialize`s form doesnt work well when Bootstrap
                is implemented, so I took out the Bootstrap links.
-Pep8 Online    I found I that could not get rid of the last four errors concerning indentation, I believe this has something
                to do with the length on my string for the name of the database and I did nt want to seperate it onto seperate line. In my files you can see evidence of the error.

###Future implementation
- User loggin or at lession Brower sessions so that only the person who uploaded a file can delete it.
- Voting system, where user can vote for 'local heroes' added to the DB
- Improve gallery page with better quality images, links form images to artist page where you could then buy the product, image or print.
- Spend more time on the design and structure to more it visually appealing.
- write some Javascript for specific functions, perhaps use of toggle to say if items are sold
- Put a limit on the textarea input field.
- put image placeholder into function on the form.
- improve the layout and design of the hero.html page
- When I tried to input the photographs into the gallery using Flask I found it impossible, also the files took too long to load so
I had have them stored locally.Later I would like to fix both issues.


##Frameworks & libraries

> Flask
> PyMongo
> Materialize

### Tech 
Jquery


### Deployment

This project has been hosted on 2 environments
- Github
- Heroku
To open the app on Heroku just follow this link https://blackness-a-project.herokuapp.com/
If you wish to open this project in your own environment you will have to
download the entire  project
install all of the requirements from requirements.txt
run the app.py using Python3.

#### CREDITS
Profile picture for placeholder was taken from here - (not implemented but will be)
<a href="https://www.freepik.com/free-photos-vectors/business">Business vector created by freepik - www.freepik.com</a>
