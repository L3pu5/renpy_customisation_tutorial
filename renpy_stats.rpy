# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

label start:
    e "Time to select your stats!"
    call screen stat_page
    e "Great! Your stats are [stats[strength]] strength, [stats[dexterity]] dexterity, and [stats[smarts]] smarts!"
    return

#Statistics
default stat_points = 20
default stats = {"strength": 0, "dexterity": 0, "smarts": 0}


init python:
    #Increase
    def increase_stat(stat_name):
        global stat_points
        global stats
        if stat_points > 0:
            stat_points -= 1
            stats[stat_name] += 1
    
    #Decrease
    def decrease_stat(stat_name):
        global stat_points
        global stats
        if stats[stat_name] > 0:
            stat_points += 1
            stats[stat_name] -= 1
    

#Stats Page
screen stat_page():  
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 50
        ypadding 50
        background Solid((49,57,99))
        

        vbox:
            xalign 0.5
            yalign 0.5
            text "Remaining stat points: [stat_points]"

            vpgrid:
                cols 3
                spacing 10
                xalign 0.5
                yalign 0.5

                #Stats
                image "strength_label.png"
                image "dexterity_label.png"
                image "smarts_label.png"
                
                #Current stats
                text "[stats[strength]]" xalign 0.5 yalign 0.5 
                text "[stats[dexterity]]" xalign 0.5 yalign 0.5
                text "[stats[smarts]]" xalign 0.5 yalign 0.5

                #Up Buttons
                imagebutton auto "stat_up_button_%s.png" xalign 0.5 yalign 0.5 action Function(increase_stat, "strength")
                imagebutton auto "stat_up_button_%s.png" xalign 0.5 yalign 0.5 action Function(increase_stat, "dexterity")
                imagebutton auto "stat_up_button_%s.png" xalign 0.5 yalign 0.5 action Function(increase_stat, "smarts")

                #Down Buttons
                imagebutton auto "stat_down_button_%s.png" xalign 0.5 yalign 0.5 action Function(decrease_stat, "strength")
                imagebutton auto "stat_down_button_%s.png" xalign 0.5 yalign 0.5 action Function(decrease_stat, "dexterity")
                imagebutton auto "stat_down_button_%s.png" xalign 0.5 yalign 0.5 action Function(decrease_stat, "smarts")
    
            textbutton "Confirm" xalign 0.5 action If(stat_points == 0 ,Return(), )

