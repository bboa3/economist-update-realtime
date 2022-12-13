import schedule
import time
from src.currentCryptoTrades.main import currentCryptoTradesUseCase
from dotenv import load_dotenv

load_dotenv()

schedule.every(15).minutes.do(currentCryptoTradesUseCase)


# schedule.every(5).seconds.do(currentCryptoTradesUseCase)

while True:
    schedule.run_pending()
    time.sleep(1)
     