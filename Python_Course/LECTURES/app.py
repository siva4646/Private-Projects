from gmail import *
from random import *
import threading

def send_email():
    

gmail = GMail('throwaway05314@gmail.com', 'dodbwiqcgmpojzcg')
print('Created GMail account')
i = 0

random_words = ['Balls', 'Penis', 'Vagina', 'Cock', 'Hubble', 'Telescopes', 'Planet', 'Earth', 'Urethra']

for i in range(1000):
    random_num = randint(0, 8)
    word = random_words[random_num]
    msg = Message(word + str(i), to="michelepipicellii@gmail.com", text=
    '''
    BallsBalls                      
    BallsBalls                      
    BallsBalls                     
    BallsBalls                      
    BallsBalls                      
    BallsBalls                      
    BallsBallsBallsBallsBalls
    BallsBallsBallsBallsBalls 
    
    
    BallsBallsBallsBallsBallsBallsBalls
    BallsBallsBallsBallsBallsBallsBalls
    BallsBalls               BallsBalls
    BallsBalls               BallsBalls
    BallsBalls               BallsBalls
    BallsBalls               BallsBalls
    BallsBalls               BallsBalls
    BallsBallsBallsBallsBallsBallsBalls         
    BallsBallsBallsBallsBallsBallsBalls 
    
    
    BallsBalls
    BallsBalls
    BallsBalls
    BallsBalls
    BallsBalls
    BallsBalls
    BallsBallsBallsBallsBallsBalls
    BallsBallsBallsBallsBallsBalls
    ''')
    print('Created message', i)
    gmail.send(msg)
    print('Sent message')

# Spams the selected email with LOL

