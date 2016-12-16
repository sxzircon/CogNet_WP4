
import pandas
import csv
from shapely.geometry import shape, Point
import geojson as json

#Entertainment
Arts_Enter = ["Arts & Entertainment", "Aquarium", "Planetarium", "Concert Hall", "Arcade",
              "Museum", "Zoo", "General Entertainment", "Movie Theater", "Science Museum",
              "Public Art", "Art Museum", "Theater", "Racetrack", "History Museum", "Pool Hall",
              "Stadium", "Art Gallery", "Bowling Alley", "Music Venue", "Historic Site", "Casino"]
#Education
College_Univer = ["College Theater", "Trade School", "Student Center", "Fraternity House", "College Academic Building",
                  "College Stadium", "Community College", "College & University", "General College & University",
                  "University", "Comedy Club", "Performing Arts Venue", "Law School", "Sorority House", "Medical School"]
#Night Life
Night_Spot = ["Bar", "Nightlife Spot", "Beer Garden", "Brewery", "Other Nightlife"]

#Recreation
Out_doors = ["Playground", "Castle", "Pool", "River", "Outdoors & Recreation", "Campground", "Ski Area",
             "Gym / Fitness Center", "Park", "Scenic Lookout", "Plaza", "Neighborhood", "Garden", "City",
             "Harbor / Marina", "Beach", "Sculpture Garden", "Athletic & Sport", "Athletic & Sports", "Bridge",
             "Other Great Outdoors", "Cemetery"]

#Social Services
Prof_Places = ["Shrine", "Building", "Government Building", "Professional & Other Places", "Mosque", "Convention Center",
               "Library", "School", "Parking", "Event Space", "Elementary School", "Military Base", "Church",
               "Music School", "Fair", "Nursery School", "High School", "Animal Shelter", "Funeral Home",
               "Synagogue", "Temple", "Spiritual Center", "Post Office", "Winery", "Distillery", "Medical Center",
               "Office", "Embassy / Consulate", "Factory"]
#Residence
Residence = ["Home (private)", "Residential Building (Apartment / Condo)", "Middle School", "Housing Development"]

#Shopping
Shops_Service = ["Bridal Shop", "Financial or Legal Service", "Bike Shop", "Bookstore", "Video Game Store",
                 "Motorcycle Shop", "Jewelry Store", "Music Store", "Gift Shop", "Garden Center", "Board Shop",
                 "Tattoo Parlor", "Cosmetics Shop", "Flea Market", "Car Wash", "Recycling Facility",
                 "Hardware Store", "Convenience Store", "Spa / Massage", "Miscellaneous Shop", "Antique Shop",
                 "Nail Salon", "Candy Store", "Clothing Store, Mall", "Photography Lab", "Electronics Store",
                 "Pet Store", "Thrift / Vintage Store", "Toy / Game Store", "Gaming Cafe",
                 "Furniture / Home Store", "Internet Cafe", "Sporting Goods Shop", "Newsstand",
                 "Drugstore / Pharmacy", "Laundry Service", "Smoke Shop", "Video Store",
                 "Pet Service", "Storage Facility", "Shop & Service", "Mobile Phone Shop",
                 "Design Studio", "Market", "Automotive Shop", "Hobby Shop", "Department Store",
                 "Paper / Office Supplies Store", "Record Shop", "Salon / Barbershop", "Flower Shop",
                 "Bank, Food & Drink Shop", "Camera Store", "Arts & Crafts Store", "Car Dealership",
                 "Gas Station / Garage", "Tanning Salon"]

#Travelling
Travel_Transport = ["Light Rail", "Ferry", "Bike Rental / Bike Share", "Rest Area", "Train Station",
                    "Moving Target", "Subway", "General Travel", "Hotel", "Airport", "Rental Car Location",
                    "Road", "Taxi", "Bus Station", "Travel Lounge", "Travel & Transport"]

#Eating
Food = ["Molecular Gastronomy Restaurant", "Argentinian Restaurant", "Italian Restaurant",
        "French Restaurant", "Korean Restaurant", "Filipino Restaurant", "Indian Restaurant",
        "Mexican Restaurant", "Japanese Restaurant",  "Sushi Restaurant", "Restaurant",
        "Southern / Soul Food Restaurant", "Hot Dog Joint", "Ice Cream Shop", "Cuban Restaurant",
        "Bakery", "Malaysian Restaurant", "Salad Place", "Brazilian Restaurant", "Eastern European Restaurant",
        "Coffee Shop", "Cupcake Shop", "Afghan Restaurant", "Mediterranean Restaurant", "Turkish Restaurant",
        "Seafood Restaurant", "Greek Restaurant", "Tapas Restaurant", "Caf_", "Cafe",
        "Caribbean Restaurant", "African Restaurant", "Arepa Restaurant", "Steakhouse",
        "Thai Restaurant", "Vietnamese Restaurant", "Australian Restaurant", "Peruvian Restaurant",
        "Asian Restaurant", "South American Restaurant", "American Restaurant", "Soup Place",
        "Spanish Restaurant", "Scandinavian Restaurant", "BBQ Joint", "Falafel Restaurant",
        "Chinese Restaurant", "Burger Joint", "Food", "Burrito Place", "Wings Joint", "Donut Shop",
        "Vegetarian / Vegan Restaurant", "Cajun / Creole Restaurant", "Gastropub", "Swiss Restaurant",
        "Moroccan Restaurant", "Food Truck", "Fried Chicken Joint", "Tea Room", "Middle Eastern Restaurant",
        "Ethiopian Restaurant", "Portuguese Restaurant", "Fast Food Restaurant", "Dumpling Restaurant",
        "Latin American Restaurant", "Pizza Place", "Breakfast Spot", "Dessert Shop",
        "Mac & Cheese Joint", "Sandwich Place", "Bagel Shop", "Taco Place", "Dim Sum Restaurant",
        "German Restaurant", "Fish & Chips Shop", "Gluten-free Restaurant", "Deli / Bodega", "Diner",
        "Snack Place", "Ramen /  Noodle House"]

def activity_category_classification (functionalclass):
    if any(functionalclass in s for s in Arts_Enter):
        acitivity_cateog = "Entertainment"
    elif any(functionalclass in s for s in College_Univer):
        acitivity_cateog = "Education"
    elif any(functionalclass in s for s in Night_Spot):
        acitivity_cateog = "NightLife"
    elif any(functionalclass in s for s in Out_doors):
        acitivity_cateog = "Recreation"
    elif any(functionalclass in s for s in Prof_Places):
        acitivity_cateog = "SocialServices"
    elif any(functionalclass in s for s in Residence):
        acitivity_cateog = "Residence"
    elif any(functionalclass in s for s in Shops_Service):
        acitivity_cateog = "Shopping"
    elif any(functionalclass in s for s in Travel_Transport):
        acitivity_cateog = "Traveling"
    elif any(functionalclass in s for s in Food):
        acitivity_cateog = "Eating"
    else:
        acitivity_cateog = "NA"
    return acitivity_cateog;
