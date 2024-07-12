def NULL_not_found(object: any) -> int:

    if type(object) is int and object == 0:
        print("Zero:", object, type(object))
    elif object == "":
        print("Empty: ", type(object))
    elif object != object:
        print("Cheese:", "nan", type(object))
    elif object is None:
        print("Nothing:", object, type(object))
    elif object is False:
        print("Fake:", object, type(object))
    else:
        print("Type not Found")
        return 1
    return 0
