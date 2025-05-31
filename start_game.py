from views.alien_invasion import AlienInvasion

def start_game():
    ai = AlienInvasion()
    ai.run_game()


if __name__ == '__main__':
    start_game()
