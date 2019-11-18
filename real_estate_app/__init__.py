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

    def display(self):
        super().display()
        print("APARTMENT DETAILS")
        print(f"laundry: {self.laundry}")
        print(f"has balcony: {self.balcony}")

    @staticmethod
    def prompt_init():
        parent_init = Property.prompt_init()
        laundry = ''
        while laundry.lower() not in Apartment.valid_laundries:
            laundry = input(
                "What laundry facilities does the property have? {', '.join(Apartment.valid_laundries)}")
        balcony = ''
        while balcony.lower() not in Apartment.valid_balconies:
            balcony = input(
                "Does the property have a balcony? "
                f"{', '.join(Apartment.valid_balconies)}")
        parent_init.update({
                "laundry": laundry,
                "balcony": balcony
            })
        return parent_init
