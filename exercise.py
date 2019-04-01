def luck_check(string):
    if len(string) % 2 != 0 or string == "" or type(string) != str:
        # didn't realize string length could be odd numbered fix later
        print('Must be an even number string of digits.')
    else:        
        first_half = string[:len(string) // 2]
        second_half = string[len(string) // 2:]
        first_half_total = 0
        second_half_total = 0
        for i in first_half:
            first_half_total += int(i)
        for i in second_half:
            second_half_total += int(i)
        
        if first_half_total == second_half_total:
            print('Congrats this is a lucky ticket!')
        else:
            print('This ticket is unlucky.')

user_str = input('Enter an even numbered string of digits: ')
luck_check(user_str)
