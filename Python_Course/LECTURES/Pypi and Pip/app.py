from gmail import *
import sms4

gmail = GMail('throwaway05314@gmail.com', 'dodbwiqcgmpojzcg')
print('Created GMail account')
i = 0

for i in range(1):
    msg = Message('Balls' + str(i), to="PIPICM25@smc.sa.edu.au", text=
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

