#main driver 
from futbin import futbin
from sofifa import sofifa
def main():
    player_name= str(input("Enter player name: "))
    sofifa_or_futbin = str(input("Enter 'sofifa' or 'futbin': "))
    if sofifa_or_futbin == 'sofifa':
        sofifa(player_name)
    if sofifa_or_futbin == 'futbin':
        futbin(player_name)
    
if __name__ == "__main__":
    main()