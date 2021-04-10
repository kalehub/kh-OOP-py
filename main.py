from MyClass import *



def main():

    # making an object
    obj = MyClass('teguh', 22)
    obj_2 = MyClass('satya', 21)

    # printing object attribute
    print(obj.name, obj.age, obj_2.name, obj_2.age)

    # modifying attribute
    obj_2.name = 'Dharma'
    print(obj.name, obj.age, obj_2.name, obj_2.age)

    # accessing methods
    print(obj.get_description())
    print(obj.speak('why so lonely'))
    print(obj.__str__())

    



if __name__ == '__main__':
    main()
