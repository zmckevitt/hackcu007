# hackcu007 README

##Inspiration:
The inspiration for this assignment came from the Spotify rapports on your yearly music habits. We all really liked this idea and we were wondering if there was some way to get more updates. We googled if Spotify had an API and it did. Our next steps were to see if we could use python with the API and luckily we found Spotipy. Now we had our project in mind and all we had to do is create the website to host our python script.

## What it does
This website takes your Spotify login and allows you to see a few metrics. These are your top ten songs, top ten artists, top ten most danceable songs, top ten most energetic songs, the top three genres that you've listened to, and the overall valence (or happiness) of the music you've listened to. All over a chosen time scale of either 4 weeks, 6 months, or all-time. We were especially interested in the all-time stats as this is not available on Spotify Wrapped. All of this is presented on a gorgeous GUI.

## How we built it:
There are many different portions of our project that had to be researched and created. The start of our idea was to interact with spotify using an API. We solved this problem using Spotipy a python library with extensive documentation that allowed us to gather tons of data on songs and users. Next we had to have some way to connect this script to the html output. For this we used a flask server using ajax. This allowed us to gather the data from the user then send an output to our html. Our final step was to output the data in an organized manner. For this we used a custom html site that sorted each of your top songs into our outputs.

## Challenges we ran into
We ran into a couple challenges along the way. Getting the flask server to communicate between the HTML UI and the Python code was a big challenge. We also ran into problems while interfacing with the API. The API stored cache locally, which meant that the information displayed on the website was not refreshing. Purging the cache was the solution, however it was difficult to implement a solution that worked across all operating systems.

## Accomplishments that we're proud of
We are incredibly proud of the work that we put together over the past 24 hours. From brainstorming ideas, to breaking down the problem statement, we were able to come up a working product at the end of it. The whole process was a big learning moment, and everyone of us learned something new and applicable. None of us had experience with the Spotify API, AJAX, or JSON objects in the past, yet were able to implement a functional product incorporating all of these in the past 24 hrs.

##What we learned:
What we learned in this project was how to fully roll out a working website. We created a server with flask and a front end with html and a python script using Spotipy. We learned how to attach a python script to a website and how to use the API. When we started this project we had almost no experience in any full stack development and after finishing we gained lots of knowledge of this process.

## What's next for Spotipy Guys:
What's next for the Spotipy guys is to host our website on a server and open our creation to the world. Currently our website is hosted locally and we would love to be able to have a real website. We also have plans to work on the GUI of our website unfortunately we only had about a day so creating a great looking UI with all the features we wanted was quite difficult. We want to have graphs added in the future so we can represent our stats in a more visual manner.
