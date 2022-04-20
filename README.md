# livetest
Allows user to test crypto trading strategies in a live environment. Handles one trade at a time, long or short, and can account for trading fees. 



# how-to

Step 1. At the top of the file, change the variable 'exchange' to fit your needs.


Step 2. Write your strategy


Step 3. Hooking everything up

   - to open a long order: Long.open('ticker')
      - returns your trade's opening price
 
   - to close a long order: Long.close('ticker')
      - returns your trade's closing price
    
   - to open a short order: Short.open('ticker')
      - returns your trade's opening price
    
   - to close a short order: Short.close('ticker')
      - returns your trade's closing price

   - to calculate a long trade's return: Ret.longRet('opening price', 'closing price')
      - returns the trade's percentage return
    
   - to calculate a short trade's return: Ret.shortRet('opening price', 'closing price')
      - returns the trade's percentage return
