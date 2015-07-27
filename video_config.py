import Video
import fresh_tomatoes

# each movie image url saved in a variable of type String
sin_image = '''http://ia.media-imdb.com/images/M/MV5BMTI2NjUyMDUyMV5BMl5BanBnXkFtZ
TcwMzU0OTkyMQ@@._V1_SX640_SY720_.jpg'''
warm_image = "http://ecx.images-amazon.com/images/I/51Mxun8Z0XL.jpg"
carrie_image = '''http://wp.production.patheos.com/blogs/poptheology/files/2013/10/
carrie-poster-2013.jpg'''
obli_image = '''http://ia.media-imdb.com/images/M/MV5BMTQwMDY0MTA4MF5BMl5BanBnXk
FtZTcwNzI3MDgxOQ@@._V1_SX214_AL_.jpg'''
fight_image = "http://doublefeatureshow.com/images/covers/fight-club.jpg"
taken_image = '''http://ia.media-imdb.com/images/M/MV5BNjM5MDU3NTY0M15BMl5BanBnXkFtZT
gwOTk2ODU2MzE@._V1_SX640_SY720_.jpg'''

# each movie youtube trailer url saved in a variable of type String
sin_trailer = "https://www.youtube.com/watch?v=C3VjVMitTbA"
warm_trailer = "https://www.youtube.com/watch?v=c9RQe5WBbww"
carrie_trailer = "https://www.youtube.com/watch?v=LxwPUSWRaJo"
obli_trailer = "https://www.youtube.com/watch?v=6ob3ygJ-zfY"
fight_trailer = "https://www.youtube.com/watch?v=SUXWAEX2jlg"
taken_trailer = "https://www.youtube.com/watch?v=uPJVJBm9TPA"

# each movie description saved in a variable of type String
sin_desc = """A film that explores the dark and miserable town, Basin City,
and tells the story of three different people,
all caught up in violent corruption."""

warm_desc = """A terrible plague has left the planet's population divided
between zombies and humans. An unusual zombie
sees his walking-dead brethren attacking a living woman and rescues her."""

carrie_desc = """A reimagining of the classic horror tale about Carrie White, a
shy girl outcast by her peers and sheltered by her
deeply religious mother, who unleashes telekinetic terror on her small town."""

obli_desc = """A veteran assigned to extract Earth's remaining resources
begins to question what he knows about his mission and himself."""

fight_desc = """An insomniac office worker, looking for a way to change his
life, crosses paths with a devil-may-care soap maker,
forming an underground fight club that evolves into
something much, much more..."""

taken_desc = """Ex-covert operative Bryan Mills (Liam Neeson) and his ex-wife,
Lenore (Famke Janssen), are enjoying a reconciliation
when Lenore is brutally murdered. """

# creating an instance of type movie for each movie
# calling Movies init() and passing required arguments

sin_city = Video.Movie("Sin City", sin_image, sin_trailer, sin_desc)
warm_bodies = Video.Movie("Warm Bodies", warm_image, warm_trailer, warm_desc)
carrie = Video.Movie("Carrie", carrie_image, carrie_trailer, carrie_desc)
oblivion = Video.Movie("Oblivion", obli_image, obli_trailer, obli_desc)
fight_club = Video.Movie("Fight Club", fight_image, fight_trailer, fight_desc)
taken = Video.Movie("Taken 3", taken_image, taken_trailer, taken_desc)

# every movie object is stored in an array called movies
movies = [sin_city, warm_bodies, carrie, oblivion, fight_club, taken]

# .open_movies_page() is called which takes an array of movie objects
fresh_tomatoes.open_movies_page(movies)
