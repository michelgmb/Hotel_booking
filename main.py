import pandas as pd

df = pd.read_csv('hotels.csv', dtype={'id': 'str'})


class Hotel:
    def __init__(self, hotel_id, name):
        self.hotel_id = hotel_id
        name = df.loc[df['id'] == self.hotel_id, ['name']].squeeze()
        self.name = name

    def available(self):
        available = df.loc[df['id'] == self.hotel_id, ['available']].squeeze()
        if available == "yes":

            return True
        else:
            return f"Sorry! The {self.name}  Hotel is not available"

    def book(self):
    #     #df = pd.read_csv('hotels.csv', dtype={'id': 'str'})
    #     #print(df.loc[df['id'] == hotel_id, ['name']].squeeze())
        df.loc[df['id'] == self.hotel_id, 'available']='no'
        df.to_csv('hotels.csv',index=False)
    #     return self.name
        return self.name


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel_object = hotel_object

    def generate(self):
        return f"""
    Hello {self.customer_name}
    your hotel booking is  {self.hotel_object}
    Thank you for booking with us
        
        """


# print list of hotel

# for i in df.iterrows():
# print(df.loc['available', 'id'==134])
print(df)
hotel_id = input("Enter id of the hotel: ")
hotel = Hotel(hotel_id=hotel_id, name="")
if hotel.available() == True:
    hotel.book()
    customer_name = input("Enter your name: ")
    reservation = ReservationTicket(customer_name, hotel.book())
    print(reservation.generate())
else:
    print(hotel.available())


# df.loc[df['shield'] > 6, ['max_speed']]


# if available == 'yes':
#     print( df.loc[df['id'] == hotel_id, ['name']].squeeze())
#     df.loc[df['id'] == hotel_id,['available']]='no'
#     df = df.to_csv('hotels.csv',index=True)
#print(df)