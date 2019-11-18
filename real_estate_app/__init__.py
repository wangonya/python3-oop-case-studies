class Property:
    def __init__(self, square_feet='', beds='', baths='', **kwargs):
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        print("PROPERTY DETAILS")
        print("=================")
        print(f"square feet ==> {self.square_feet}")
        print(f"bedrooms ==> {self.num_bedrooms}")
        print(f"bathrooms ==> {self.num_baths}")

    @staticmethod
    def prompt_init():
        return dict(square_feet=input("Enter square feet: "),
                    beds=input("Enter num of bedrooms: "),
                    baths=input("Enter num of bathrooms: "))


class Apartment(Property):
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony='', laundry='', **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry
