class NetflixTitle(object):

    def __init__(self,
                 show_id,
                 type,
                 title,
                 director,
                 cast,
                 country,
                 date_added,
                 release_year,
                 rating,
                 duration,
                 listed_in,
                 description):

        self.show_id = show_id
        self.type = type
        self.title = title
        self.director = director
        self.cast = cast
        self.country = country
        self.date_added = date_added
        self.release_year = release_year
        self.rating = rating
        self.duration = duration
        self.listed_in = listed_in
        self.description = description
