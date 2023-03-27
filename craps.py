from dice import DoubleDice

outcome = {
    7: 'Natural', 11: 'Natural', 2: 'Craps', 3: 'Craps', 12: 'Craps' 
}

d = DoubleDice()

def __main__(dice_):
    game_status = 'Continue'
    player_point = 0
    _, _, sum_dice = dice_.roll_double_dice()
    print('Your rolled sum: ', sum_dice)

    for key, value in outcome.items():
        if key == sum_dice:
            game_status = value

    player_point = sum_dice
    print('Point is', player_point)

    while game_status == 'Continue':
        _, _, sum_ = dice_.roll_double_dice()
        if sum_ == player_point:
            game_status = 'Natural'
            break
        elif sum_ == 7:
            game_status = 'Craps'
            break 
    
    if game_status == 'Natural':
        print('You win!')
    elif game_status == 'Craps':
        print('You lose!')
    
__main__(d)