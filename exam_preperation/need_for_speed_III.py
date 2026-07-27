number_of_cars = int(input())

cars = {}

for _ in range(number_of_cars):
    car_info= input().split("|")
    car, mileage, fuel = car_info[0], int(car_info[1]), int(car_info[2])
    cars[car] = [mileage, fuel]


    






command = input()
while command != "Stop":
        command_as_list = command.split(" : ")
        if command_as_list[0] == "Drive":
              car, distance, fuel = command_as_list[1], int(command_as_list[2]), int(command_as_list[3])
              if cars[car][1] >= fuel:
                    cars[car][1] -= fuel
                    cars[car][0] += distance
                    print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
              else:
                    print("Not enough fuel to make that ride")
              if cars[car][0] >= 100_000:
                    del cars[car]
                    print(f"Time to sell the {car}!")

        elif command_as_list[0] == "Refuel":
              car, fuel = command_as_list[1], int(command_as_list[2])
              cars[car][1] += fuel
              if cars[car][1] > 75:
                    fuel = (fuel) - (cars[car][1] - 75)
                    cars[car][1] = 75

              print(f"{car} refueled with {fuel} liters")
        elif command_as_list[0] == "Revert":
              car, kilometers = command_as_list[1], int(command_as_list[2])
              cars[car][0] -= kilometers
              if cars[car][0] < 10000:
                    cars[car][0] = 10000
              else:
                    print(f"{car} mileage decreased by {kilometers} kilometers")

        command = input()


for key, value in cars.items():
      print(f"{key} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.")