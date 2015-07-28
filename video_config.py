import Video
import fresh_tomatoes


#creating an instance of type movie for each movie
#calling Movies init() and passing required arguments

sin_city = Video.Movie("Sin City",
                       "images/sin_city.jpg",
                       "https://www.youtube.com/watch?v=C3VjVMitTbA",
                       "A film that explores the dark and miserable town, Basin City.")

warm_bodies = Video.Movie("Warm Bodies",
                          "images/warm_bodies.jpg",
                          "https://www.youtube.com/watch?v=c9RQe5WBbww",
                          "A terrible plague has left the planet's population divided.")

carrie = Video.Movie("Carrie",
                     "images/carrie.jpg",
                     "https://www.youtube.com/watch?v=LxwPUSWRaJo",
                     "Classic horror tale about Carrie White, a shy girl outcast by her peers.")

oblivion = Video.Movie("Oblivion",
                       "images/oblivion.jpg",
                       "https://www.youtube.com/watch?v=6ob3ygJ-zfY",
                       "A veteran assigned to extract Earth's resources question his mission.")

fight_club = Video.Movie("Fight Club",
                         "images/fight_club.jpg",
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg",
                         "An insomniac office worker, looking for a way to change his life.")

taken = Video.Movie("Taken 3",
                    "images/taken.jpg",
                    "https://www.youtube.com/watch?v=uPJVJBm9TPA",
                    "Ex-covert operative ex-wife is brutally murdered.")

#every movie object is stored in an array called movies
movies=[sin_city,warm_bodies,carrie,oblivion,fight_club,taken]

#.open_movies_page() is called which takes an array of movie objects
fresh_tomatoes.open_movies_page(movies)
