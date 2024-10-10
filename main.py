import turtle as t
import pandas as pd


screen=t.Screen()
screen.setup(677,922)
image="Colombia_map.gif"
screen.addshape(image)
t.shape(image)

lat_min, lat_max = -4.2, 12.5  
lng_min, lng_max = -81.7, -67.0 

screen_width = 677
screen_height = 922

factor_y = screen_height / (lat_max - lat_min)
factor_x = screen_width / (lng_max - lng_min)

data=pd.read_csv("cities_data.csv")
cities_list=data.city.tolist()

guessed_cities=[]
not_guessed_cities=[]
score=0
while len(guessed_cities)<84:
    user_answer=t.textinput(f"Guess the city.{score}/84", "Please enter a Colombian city: ").title()
    if user_answer in cities_list:
        if user_answer not in guessed_cities:
            score+=1
        guessed_cities.append(user_answer)
        city_name=t.Turtle()
        city_name.penup()
        city_name.hideturtle()
        city_guessed=data[data.city==user_answer]
        x_coor=(city_guessed.lng.item()-lng_min)*factor_x-screen_width/2-105
        y_coor=(city_guessed.lat.item()-lat_min)*factor_y-screen_height/2-15
        city_name.goto(x_coor,y_coor)
        city_name.write(user_answer)
        
        
    
    if user_answer=="Exit":
        for city in cities_list:
            if city not in guessed_cities:
                not_guessed_cities.append(city)
        missing_cities=pd.DataFrame(not_guessed_cities)
        missing_cities.to_csv("missing_Colombia_cities.csv")
        break
    



