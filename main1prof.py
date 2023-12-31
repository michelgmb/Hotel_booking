import pandas

df = pandas.read_csv("hotels.csv", dtype={"id": str})


class Hotel:
    watermark = "The real Estate Company"  # class varaibles

    @classmethod  # use for glogbal script   # @classmethod Class method Class decorator
    def get_hotel_count(cls, data):
        return len(data)

    def __init__(self, hotel_id):           # instance methods
        self.hotel_id = hotel_id           # instance variable
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Book a hotel by changing its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """Check if the hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False

    def __eq__(self, other):   # magic method
        if self.hotel_id == other.hotel_id:
            return True
        else:
            return False




class ReservationTicket:

    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are you booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel.name}
        """
        return content


    def generate(self):
        content = f"""
        Thank you for your SPA reservation!
        Here are you SPA booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel.name}
        """
        return content
    @property
    def the_customer_name(self):
      name = self.customer_name.strip()
      name = name.title()

    @staticmethod     # usually for convertion
    def convert(amount):
        return amount * 1.2


print(df)
hotel1 = Hotel(hotel_id="188")
hotel2 = Hotel(hotel_id="134")

print(hotel1.name)   # instance variable
print(hotel2.name)

print(hotel1.watermark)
print(hotel2.watermark)

print(Hotel.watermark)
print(Hotel.get_hotel_count(data=df)) # class variable
print(hotel1.get_hotel_count(data=df))

ticket = ReservationTicket(customer_name="jonh smith ", hotel_object=hotel1)
print(ticket.the_customer_name)
converted = ReservationTicket.convert(10)
print(converted)