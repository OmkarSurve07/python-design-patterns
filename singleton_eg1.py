from tkinter import NO


class Singleton:
    # pass
    __instance = None
    

database = Singleton()
database1 = Singleton()

print(database == database1)