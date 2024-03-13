# Unit 1 Activity – dessert rater bot
# Tony Du
# Mar 4, 2024

def main():
    # Asks the user for their favourite dessert,
    initial_response = input("What's your favourite dessert?")
    # Asks how they rate the dessert on a scale of 1-5 
    dessert_taste = d_and_s (input("On a scale of 1-5, how would you rate the dessert?"))
    # and sweetness on a scale of 1-5
    sweetness = l_ (input("How would you rate the sweetness? "))
   # Finally, multiply the inputs to get a final value and evaluates the overall mark of the dessert
    overall_score = dessert_taste * sweetness

    # Note: This is one way to round a number to two decimal places
    print(f"{initial_response} is {overall(overall_score)}")

def d_and_s(ds):
    # TODO
    return float (ds)

def l_(l):
    # TODO
    return float (l)

def overall(o):
    if o == 0:
        return "probably not your fav :("
    if 0 < o <= 10:
        return "okay"
    if 10 < o <= 20:
        return "good"
    if 20 < 0 < 25:
        return "great"
    if o == 25:
        return "best dessert of the year!"
    
main()