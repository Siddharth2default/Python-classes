def make_pizza(*topings):
    print(topings,end=" ")
    for toping in topings:
        print(toping,end=" ")
pramod = make_pizza("mushroom","salt","pepper")
santosh = make_pizza("onion","capsicum")
def make_base(*topings,base):
    print(topings,base,end=" ")
    for toping in topings:
        print(toping,end=" ")
pramod = make_base("mushroom","salt","pepper",base="thin")

