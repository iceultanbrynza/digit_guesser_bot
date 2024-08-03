answers = {"start": {
                0: "{name}, привет! Я бот и я умею угадывать числа. Давай попробуем?",
                1: "{name}, greetings! I am a bot. I pick random number that you have to guess. Let's try?"
                },
            "help": {
                0: 'Я загадываю число от 1 до 100, '
                    'а твоя задача угадать его. '
                    '/cancel - остановить игру '
                    '/stat - посмотреть статистику '
                    '/language - язык' ,
                1: 'I pick a number from 1 to 100, '
                    'you have to guess it. '
                    '/cancel - to stop the game '
                    '/stat - to check your statistics '
                    '/language - change language'
                },
            "cancel": {
                0: {
                    'on': 'Вы отменили игру(',
                    'off': 'А мы и так с вами не играем'
                    },
                1: {
                    'on': 'You have cancelled the game(',
                    'off': 'We are not playing with you yet'
                    }
                },
            "stat": {
                ">0": {
                    0: '{name}, вы сыграли {games} раз. '
                        'Из них вы выиграли {wins} раз. '
                        'Ваш коэффициент побед: {win_rate}',
                    1: '{name}, you have played {games} times '
                        'including {wins} wins. '
                        'Your win rate: {win_rate}'
                    },
                "<0": {
                    0: 'У вас нет статистики',
                    1: 'You do not have any statistics'
                    }
                },
            "go_game": {
                0: {
                    'on': 'Вы находитесь в состоянии игры.',
                    'off': 'Вы начали игру. Я загадал число, у вас есть 5 попыток.'
                    },
                1: {
                    'on': 'You are already playing with me',
                    'off': 'Game is started. You have 5 tries'
                    }
                },
            "refuse_game": {
                0: {
                    'on': 'Вы имели ввиду /cancel?',
                    'off': 'Если захотите, обязательно напишите об этом'
                    },
                1: {
                    'on': 'Did you mean /cancel?',
                    'off': 'It is a pity( You can play later'
                    }
                },
            "digit_input": {
                0: {
                    'on': {
                        "guessed": 'Ура! Вы угадали число за {tries} попыток.',
                        "bigger": 'Загаданное число больше',
                        "smaller": 'Загаданное число меньше',
                        "loose": 'Кажется, вы проиграли.. Я загадал {secret_number}. Но вы можете попытать удачу еще раз!'
                        },
                    'off': 'Игра не начата'
                    },
                1: {
                    'on': {
                        "guessed": 'Hurrah! You guessed a number in {tries} tries.',
                        "bigger": 'My number is bigger',
                        "smaller": 'my number is smaller',
                        "loose": 'You lost.. My number was {secret_number}. Do you want to play again?'
                        },
                    'off': 'Game session has not started'
                    }
                },


        }