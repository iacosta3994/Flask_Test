
    def decision(input_prompt, choice_a, choice_b, a_text, b_text):
        choice = input(input_prompt)
        if choice == choice_a:
            print(a_text)
        elif choice == choice_b:
            print(b_text)
        else:
            print("That didn't seem to be one of the choices, try again.")
            decision(input_prompt, choice_a, choice_b, a_text, b_text)


    StoryTime = True

    while StoryTime:
        print ("The new adventure for adventures sake where everything is obviously an adventure!")
        print ("Directions: Don't let your character find out it's in a video game")

        character_name = input("Whats your character's name?")

        print ("Alright, " + character_name + " it is. Starting the adventure....Now.")
        print (" A long, long, long time ago. There was an incredible hero that saved humanity. You ," + character_name + " , are not said hero." )

        ## Chapter One: The begining of the non-heroe heroe
        input_prompt = "So tell me " + character_name + " are you feeling more spicey or cool?"
        choice_a = 'spicey'
        a_text = "Sweet! hmmm, I mean spicey.. Now you have spicey powers that will become mostly irrelevant until its neeeded to further the plot. hrmm I mean Adventure!!"
        choice_b = 'cool'
        b_text = "Thats cool, you can probably diffuse a high stakes situation with no effort."

        decision(input_prompt,)
