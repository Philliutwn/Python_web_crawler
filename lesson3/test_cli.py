import argparse

def main():
    parser = argparse.ArgumentParser(description='python test_cli.py Helen --greetings "Good morning"')
    parser.add_argument('name', help= 'Enter your name')
    parser.add_argument('greetings', help = 'Good morning!')
    parser.add_argument('--city', help='Enter your city name')
    args = parser.parse_args()

    talk(args.name, args.greetings, args.city)

def talk(name, greetings, city):
    print(f'Hi {name},')
    print(f'{greetings}!')
    print(f'lives in {city}')

if __name__ == '__main__':
    main()
    
# Example:
# python test_cli.py Helen "Good afternoon" --city Taipei



