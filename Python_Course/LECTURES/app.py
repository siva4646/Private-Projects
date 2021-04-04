# skipped your comments for readability
import smtplib
import threading
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from random import randint

me = "throwaway05314@gmail.com"
my_password = r"dodbwiqcgmpojzcg"
you = "throwaway05314@gmail.com"

random_words = ['Balls', 'Penis', 'Vagina', 'Cock', 'Hubble', 'Telescopes', 'Planet', 'Earth', 'Urethra']

def send_email():
    random_num = randint(0, 8)
    word = random_words[random_num]
    msg = MIMEMultipart('alternative')
    msg['Subject'] = word
    msg['From'] = me
    msg['To'] = you

    html = '<html><body><p>Get Fucked!</p></body></html>'
    part2 = MIMEText(html, 'html')

    msg.attach(part2)

    s = smtplib.SMTP_SSL('smtp.gmail.com')

    s.login(me, my_password)

    s.sendmail(me, you, msg.as_string())
    print('Message sent!')
    s.quit()

threads = []

for i in range(5):
    t = threading.Thread(target=send_email)
    t.daemon = True
    threads.append(t)

for i in range(5):
    threads[i].start()

for i in range(5):
    threads[i].join()


# def send_email():
#     while True:
#         gmail = GMail('throwaway05314@gmail.com', 'dodbwiqcgmpojzcg')
#         i = 0
#
#         random_words = ['Balls', 'Penis', 'Vagina', 'Cock', 'Hubble', 'Telescopes', 'Planet', 'Earth', 'Urethra']
#
#         random_num = randint(0, 8)
#         word = random_words[random_num]
#         msg = Message(word + str(i), to="throwaway05314@gmail.com", text=
#         '''
#         BallsBalls
#         BallsBalls
#         BallsBalls
#         BallsBalls
#         BallsBalls
#         BallsBalls
#         BallsBallsBallsBallsBalls
#         BallsBallsBallsBallsBalls
#
#
#         BallsBallsBallsBallsBallsBallsBalls
#         BallsBallsBallsBallsBallsBallsBalls
#         BallsBalls               BallsBalls
#         BallsBalls               BallsBalls
#         BallsBalls               BallsBalls
#         BallsBalls               BallsBalls
#         BallsBalls               BallsBalls
#         BallsBallsBallsBallsBallsBallsBalls
#         BallsBallsBallsBallsBallsBallsBalls
#
#
#         BallsBalls
#         BallsBalls
#         BallsBalls
#         BallsBalls
#         BallsBalls
#         BallsBalls
#         BallsBallsBallsBallsBallsBalls
#         BallsBallsBallsBallsBallsBalls
#         ''')
#         gmail.send(msg)
#         print('Sent message')
#
# # Spams the selected email with LOL
#
# threads = []
#
# for i in range(100):
#     t = threading.Thread(target=send_email)
#     t.daemon = True
#     threads.append(t)
#
# for i in range(100):
#     threads[i].start()
#
# for i in range(100):
#     threads[i].join()
