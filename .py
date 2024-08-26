// Definition of code parameters
DEFPARAM CumulateOrders = False // Cumulating positions deactivated
// The system will cancel all pending orders and close all positions at 0:00. No new ones will be allowed until after the "FLATBEFORE" time.
DEFPARAM FLATBEFORE = 083000
// Cancel all pending orders and close all positions at the "FLATAFTER" time
DEFPARAM FLATAFTER = 200000

// Prevents the system from placing new orders on specified days of the week
daysForbiddenEntry = OpenDayOfWeek = 1 OR OpenDayOfWeek = 3 OR OpenDayOfWeek = 4 OR OpenDayOfWeek = 5 OR OpenDayOfWeek = 6 OR OpenDayOfWeek = 0

// Conditions to enter long positions
ignored, ignored, ignored, ignored, ignored, ignored, indicator1 = CALL "MyIndicator(2)"
c1 = (close[1] CROSSES OVER indicator1[1])

IF c1 AND not daysForbiddenEntry THEN
BUY 7 CONTRACT AT MARKET
ENDIF

// Conditions to exit long positions
ignored, ignored, ignored, ignored, ignored, indicator2, ignored = CALL "MyIndicator(2)"
c2 = (close[1] CROSSES OVER indicator2[1])

IF c2 THEN
SELL AT MARKET
ENDIF

// Stops and targets
SET STOP %LOSS 10
