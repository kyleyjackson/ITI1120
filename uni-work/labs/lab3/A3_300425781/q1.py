#== Exercise One ==#
def pay(wage, hours):
    '''
    (number, number) => number

    Takes inputs for the employee's wage and the number of hours they worked this week
    then returns the hourly wage with overtime based on how long they worked
    '''
    # values
    regHours = 0
    if hours < 40:
        regHours = hours
    else:
        regHours = 40

    overtime = 0
    if hours < 61:
        overtime = hours - 40
    else:
        overtime = 20

    doubleOver = hours - 60
    paycheque = regHours * wage

    if overtime < 1:
        return paycheque

    else:
        paycheque += wage * 1.5 * overtime

        if doubleOver < 1:
            return paycheque
        
        else:
            paycheque += wage * 2 * doubleOver

            return paycheque
     

print(pay(10, 35))
print(pay(10, 45))
print(pay(10, 61))