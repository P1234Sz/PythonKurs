def klasyfikator(napis):
    for slowo in napis.split():

        if len(slowo) <= 5:
            print("+ ", slowo)
        if len(slowo) > 5:
            print("- ", slowo)
    return

klasyfikator("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")