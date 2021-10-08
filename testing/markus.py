def getPizzas(person):
    result_pizzas = []
    while True:
        try:
            input_pizza = input()
        except EOFError:
            break
        if input_pizza == "":
            break
        result_pizzas.append(input_pizza)

    print(person + " favorite pizzas are:")

    for pizza in result_pizzas:
        print(pizza)
  
getPizzas("My")
getPizzas("My friends")