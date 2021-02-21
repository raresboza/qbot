# Qbot
A work in progress discord bot.
## Features
* Reddit post search: 
    &emsp;The current implementation has two commands that work with the reddit API (hottest post and random post). The first command is used to get the hottest thread on a specified subreddit by typing in discord `$hottest <name-of-subreddit>`. Similarly, randpost retrieves a thread from the most popular 500 posts on the specified subreddit. This can be used by calling `$randpost <name-of-subreddit>`.  
    &emsp; This can be exemplified by the following screenshot  
    ![discord](https://i.imgur.com/K6sbmtU.png)  
    In the event that the subreddit name isn't a valid one, the bot chooses the closest match.  

* Random images: (currently, command is bugged and might not display anything)  
    &emsp; WARNING! The images that are retrieved by this command are totally random, hence we are not responsible for disturbing content.  
    &emsp; Using the command `$image` a random imgur link is generated and verified to be valid, the contents of which are inserted in a embeded message.  
    
* Movies:
    &emsp; Currently in development, the commands intend to provide a way of searching movies, rating them and being able to see what other people thought of the screening.  
    &emsp;Commands:  
    - search: `$movies search <name-of-movie>` using themoviedb API the bot retrieves the closest movie to match the name provided, displaying the name, the description and the poster of the given movie  
    ![Movie](https://i.imgur.com/X4vsU5u.png)  
* Weather:  
    &emsp; Given a location name the command `$weather <location-name>` the command retrieves useful information about the weather in the specified region (the temperature in celcius, the sunrise and sunset hours). The current implementation specifies the hours by UTC+0, regardless of the actual time zone.  
    ![Weather](https://i.imgur.com/zYqqKGt.png)  

## Tehnologies
The following API were used in making this project:
* [Reddit](https://www.reddit.com/dev/api/)
* [OpenWeather](https://openweathermap.org/api)
* [TheMovieDB](https://developers.themoviedb.org/)
* [GeoPy](https://geopy.readthedocs.io/en/stable/)

## Contributors
* [Rares-Dorian Boza](https://github.com/raresboza)
* [Blanar George](https://github.com/giobiba)
* [Anghel Alin](https://github.com/Alinnus1)
