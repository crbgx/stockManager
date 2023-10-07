#bin/usr/stockManager

#### Input data ####
producedDay = [5, 0, 3, 5]
consumedDay = [4, 1, 3, 1]
expectedDuration = 2    # Minimum value: 1



#### Error ####
def error_demand(index):
    print('Error: Demand cannot be satisfied')
    print(f'This happened at day: {index}')
    print(f'Necessary stock missing: {consumedDay[index]}')
    end_program()



def success(stock, thrownAway):
    print('Simulation finished successfully')
    print(f'Final stock: {stock}')
    print(f'Thrown away: {thrownAway}')



#### Program end ####
def end_program():
    print('Exiting program...')
    exit()



#### Data check ####
def check_data():
    if expectedDuration < 1:
        print('Error: Expected duration must be greater than 0')
        end_program()

    for index, (i, j) in enumerate(zip(producedDay, consumedDay)):
        if i < 0:
            print(f'Error: Produced input list at: {index} cannot be negative')
            end_program()
        if j < 0:
            print(f'Error: Consumed input list at:{index} cannot be negative')
            end_program()


def stockManager(consumedDay, producedDay, expectedDuration):
    # Variables init
    stock = [0] * (expectedDuration - 1)   # Product goes off in: [n, n-1, n-2 ... 2, 1, 0] days
    thrownAway = 0

    check_data()
    for index, i in enumerate(producedDay):
        # We first calculate the stock array by adding the producedDay to the previous stock
        stock = [producedDay[index]] + stock
        thrownAway = thrownAway + stock[-1]
        if index != 0:
            del stock[-1]


        # First day special case
        if index == 0:  
            stock[index] = producedDay[index] - consumedDay[index]
            if stock[index] >= 0:
                print(f'We have satisfied demand for day: {index} with stock with {expectedDuration} days left')

            else:
                error_demand(index)


        else:
            for j in range(0, len(stock)):
                k = -j-1
                if stock[k] >= consumedDay[index]:
                    stock[k] = stock[k] - consumedDay[index]
                    consumedDay[index] = 0
                    print(f'We have satisfied demand for day: {index} with stock with {-k} days left')
                    break

                else:
                    consumedDay[index] = consumedDay[index] - stock[k]
                    stock[k] = 0

                # Check if we run out of stock
                if j == len(stock)-1 and consumedDay[index] != 0:
                    error_demand(index)

    success(stock, thrownAway)



#### Main ####
stockManager(consumedDay, producedDay, expectedDuration)