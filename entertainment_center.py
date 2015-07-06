# -*- coding: utf-8 -*-
# Importing dependencies
import media
import fresh_tomatoes

# Movie instances
white_chicks = media.Movie(
    "White Chicks",
    "Two disgraced FBI agents go way undercover in an \
    effort to protect hotel heiresses the Wilson \
    Sisters from a kidnapping plot.",
    "https://upload.wikimedia.org/wikipedia/en/2/2b/White_chicks.jpg",
    "https://www.youtube.com/watch?v=QtlRjfWSk30",
    "Marlon Wayans",
    "June 23, 2004")

scary_movie = media.Movie(
    "Scary Movie",
    "A year after disposing the body of a man they \
    accidently killed, a group of dumb teenagers are \
    stalked by a bumbling serial killer.",
    "https://upload.wikimedia.org/wikipedia/en/2/29/Movie_poster_for_%22Scary_Movie%22.jpg",
    "https://www.youtube.com/watch?v=sSWewFbFTl4",
    "Anna Faris",
    "July 7, 2000")

ted = media.Movie(
    "Ted",
    "As the result of a childhood wish, John Bennett's \
    teddy bear, Ted, came to life and has been by \
    John's side ever since - a friendship that's \
    tested when Lori, John's girlfriend of four years, \
    wants more from their relationship.",
    "https://upload.wikimedia.org/wikipedia/en/6/62/Ted_poster.jpg",
    "https://www.youtube.com/watch?v=3Vl5q06UElM",
    "Mark Wahlberg",
    "June 29, 2012")

leon = media.Movie(
    "Léon: The Professional",
    "Mathilda, a 12-year-old girl, is reluctantly taken in by Léon, a \
    professional assassin, after her family is murdered. Léon and Mathilda \
    form an unusual relationship, as she becomes his protégée and learns the \
    assassin's trade.",
    "https://upload.wikimedia.org/wikipedia/en/0/03/Leon-poster.jpg",
    "https://www.youtube.com/watch?v=DcsirofJrlM",
    "Jean Reno",
    "November 18, 1994")

magic_mike = media.Movie(
    "Magic Mike XXL",
    "Three years after Mike bowed out of the stripper \
    life at the top of his game, he and the remaining \
    Kings of Tampa hit the road to Myrtle Beach to put \
    on one last blow-out performance.",
    "https://upload.wikimedia.org/wikipedia/en/d/df/Magic_mike_xxl.jpg",
    "https://www.youtube.com/watch?v=oLoyU3xYwbs",
    "Channing Tatum",
    "July 1, 2015")


silent_hill = media.Movie(
    "Silent Hill",
    "A woman goes in search for her daughter, within the \
    confines of a strange, desolate town called Silent\
    Hill. Based on the video game.",
    "https://upload.wikimedia.org/wikipedia/en/5/57/Silent_hill.jpg",
    "https://www.youtube.com/watch?v=f5mT5LhbRJw",
    "Radha Mitchell",
    "April 21, 2006")


# List of movie that will be sent to fresh_tomatoes.py
movies = [white_chicks, scary_movie, ted, leon, magic_mike, silent_hill]

# Send movies list to fresh_tomatoes.py and call the open_movies_page method
fresh_tomatoes.open_movies_page(movies)
