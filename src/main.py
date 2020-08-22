

    StoryTime = True

    while StoryTime:
        print ("The new adventure for adventures sake where everything is obviously an adventure!")
        print ("Directions: Don't let your character find out it's in a video game")

        character_name = input("Whats your character's name?")

        print ("Alright, " + character_name + " it is. Starting the adventure....Now.")
        print (" A long, long, long time ago. There was an incredible hero that saved humanity. You ," + character_name + " , are not said hero." )

        ## Chapter One: The begining of the non-heroe heroe

        choice = input("So tell me " + character_name + " are you feeling more spicey or cool?")
        if choice == 'spicey':
            print("Sweet! hmmm, I mean spicey.. Now you have spicey powers that will become mostly irrelevant until its neeeded to further the plot. hrmm I mean Adventure!!")
            super_power = too_hot_to_handle = True
        elif choice == 'cool':
            print("Thats cool, you can probably diffuse a high stakes situation with no effort.")
            super_power = cool_vibe = True
        else:
            print("Thats not spicey or cool, check your spelling next time")
