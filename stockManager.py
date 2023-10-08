#bin/usr/stockManager

#### Input data ####
producedDay = [3, 0, 2, 5]
consumedDay = [4, 1, 3, 1]
expectedDuration = 2    # Minimum value: 2

warningCounter = 0

#### Warning ####
def warning_demand(index, consumedDay):
    global warningCounter
    warningCounter += 1
    print(f'Warning: {consumedDay[index]} stock missing at day: {index}')



def success(stock, thrownAway):
    global warningCounter
    print(f'Simulation finished successfully with {warningCounter} warnings')
    print(f'Final stock: {stock}')
    print(f'Final consumedDay array: {consumedDay}')
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
    stock = [0] * (expectedDuration)   # Product goes off in: [n, n-1, n-2 ... 2, 1, 0] days
    thrownAway = 0

    check_data()
    for index in range (0, len(producedDay)):
        # Calculate stock:
        stock = [producedDay[index]] + stock
        thrownAway = thrownAway + stock[-1]
        del stock[-1]

        # Remove demand from stock if possible
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
            if j == len(stock)-1 and consumedDay[index] > 0:
                if consumedDay[index] > 0:
                    consumedDay[index+1] += abs(consumedDay[index])
                    print(f'Out of stock. Day {index} updated demand: {consumedDay[index+1]}')
                warning_demand(index, consumedDay)

    success(stock, thrownAway)
    #end_program()



#### Main ####
stockManager(consumedDay, producedDay, expectedDuration)