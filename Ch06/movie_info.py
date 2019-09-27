favorite_movie='Human Traffic'
release_year=2000

def print_movie(name_movie,year_movie):
    print(f'The movie {name_movie} is from {year_movie}')

print_movie(favorite_movie,release_year)
print()

def movie_info(name_movie,year_movie):
    response=str(f'The movie {name_movie} is from {year_movie}')
    return response

mov_output=movie_info(favorite_movie,release_year)
print(mov_output)
print()





def print_movie_info(name,year):
    resp=str(f'The movie {name} is from {year}')
    return resp

movie1={'year':2000,'name':'Human Traffic'}
movie2={'year':2001,'name':'Groove'}
movie3={'year':1997,'name':'Better Living Through Circuitry'}

movie_list=[movie1,movie2,movie3]

for movie in movie_list:
    print(print_movie_info(movie['name'],movie['year']))