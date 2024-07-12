import time
import datetime

currTimeS = time.time()
currDate = datetime.datetime.now()
print('Seconds since January 1, 1970:',
      f'{currTimeS:,}', "or", '{:.2e}'.format(currTimeS),
      'in scientific notation')
print(currDate.strftime('%b'), currDate.strftime('%d'),
      currDate.strftime('%Y'))
