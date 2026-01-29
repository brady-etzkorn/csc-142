class Review:
    def __init__(self, text, rating):
        self.text = text
        self.rating = rating
    
    def __repr__(self):
        return f"(rating = {self.rating}, text =' {self.text}')"

class Movie:
    '''Modeling a review system for different movies'''

    def __init__(self, movie_title):
        self.movie_title = movie_title
        self.review_list = []

    def addReview(self, review):
        self.review_list.append(review)
    
    def describe_movie(self):
        print(f"\n The title of the movie is {self.movie_title}")
        print(f"\n {self.review_list}")

    def get_highest(self):
        if not self.review_list:
            return None
        highest = self.review_list[0]
        
        for review in self.review_list:
            if review.rating > highest.rating:
                highest = review
                
        return highest
    
    def get_lowest(self):
        if not self.review_list:
            return None
        lowest = self.review_list[0]
        
        for review in self.review_list:
            if review.rating < lowest.rating:
                lowest = review
                
        return lowest
    
    def get_average(self):
        if not self.review_list:
            return 0
        total = sum(r.rating for r in self.review_list)
        return total / len(self.review_list)


    

movie = Movie("Revenge of the Sith")
movie.addReview(Review("This is the best movie I have ever seen", 5))
movie.addReview(Review("This movie was amazing, had some flaws though", 4))
movie.addReview(Review("I have never seen a worse movie in my life.", 1))
movie.addReview(Review("This movie is ok", 3))

print(movie)


movie.describe_movie()

print("\nHighest Review:", movie.get_highest())

print("\nLowest Review:", movie.get_lowest())

print("\nAverage:", movie.get_average())





