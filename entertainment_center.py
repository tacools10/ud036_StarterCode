import media
import fresh_tomatoes
import datetime as date

the_replacements = media.Movie("The Replacements", "Keanu Reeves leads a group of replacement players to victory coached by Gene Hackman",
  "https://static.rogerebert.com/uploads/movie/movie_poster/the-replacements-2000/large_cHI4RgNND66gAcV63V5SoS76tVQ.jpg",
  "https://www.youtube.com/watch?v=YkOI1iX0BOI", date.datetime(2000, 8, 11), "http://www.imdb.com/title/tt0191397/")

last_samurai = media.Movie("The Last Samurai", "Tom Cruise embeds himself in a Japenese samurai rebellion",
                    "http://www.impawards.com/2003/posters/last_samurai_ver3.jpg",
                    "https://www.youtube.com/watch?v=T50_qHEOahQ", date.datetime(2003, 12, 1),
                    "http://www.imdb.com/title/tt0325710/")

'''dark_knight = media.Movie("School of Rock", "Storyline",
                            "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                            "https://www.youtube.com/watch?v=3PsUJFEBC74")

return_of_the_king = media.Movie("Ratatouille", "Storyline",
                          "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

bladerunner_2046 = media.Movie("Midnight in Paris", "Storyline",
                          "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                          "https://www.youtube.com/watch?v=atLg2wQQxvU")'''

movies = [the_replacements, last_samurai]

fresh_tomatoes.open_movies_page(movies)
