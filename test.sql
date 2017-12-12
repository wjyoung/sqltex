-- Problem 1.


-- Problem 2.


-- Problem 3. 

-- a.
SELECT *
FROM Stocks2016.d2010
WHERE cusip = '45920010';

-- b.
SELECT *
FROM Stocks2016.d2010
WHERE cusip = '45920010' AND retdate = '2010-01-07';

-- c.
SELECT bid - ask
FROM Stocks2016.d2010
WHERE cusip = '45920010' AND retdate = '2010-01-07';

-- d.
SELECT *
FROM Stocks2016.d2010
WHERE cusip = '45920010' AND vol < 5000000 AND bid > 140;


-- Problem 4.

-- a. 
SELECT shrout * prc
FROM Stocks2016.d2010
WHERE permno = 14593 AND retdate = '2010-02-01';

-- b. 
SELECT permno, shrout * prc
FROM Stocks2016.d2010
WHERE shrout IS NOT NULL AND prc IS NOT NULL
ORDER BY shrout * prc DESC
LIMIT 5;

-- c. 
SELECT permno, shrout * prc
FROM Stocks2016.d2010
WHERE retdate = '2010-02-03' AND shrout IS NOT NULL AND prc IS NOT NULL
ORDER BY shrout * prc DESC
LIMIT 5;

-- d.
SELECT permno, shrout * prc
FROM Stocks2016.d2010
WHERE retdate = '2010-02-03'
ORDER BY shrout * prc ASC
LIMIT 5;

-- e.
SELECT permno, shrout * prc
FROM Stocks2016.d2010
WHERE retdate = '2010-02-03' AND vol < 10000000 AND prc >= 0
ORDER BY shrout * prc ASC
LIMIT 5;


-- Problem 5.

-- a.
SELECT permno
FROM Stocks2016.d2010
WHERE vol < 25000
ORDER BY ABS(bid - ask) ASC
LIMIT 1;

-- b. 
SELECT permno
FROM Stocks2016.d2010
WHERE retdate = '2010-02-08'AND shrout > 500000
ORDER BY ABS(bid - ask) ASC
LIMIT 1;

-- c.
SELECT permno, bid - ask
FROM Stocks2016.d2010
WHERE vol < 1000
ORDER BY ABS(bid - ask) ASC
LIMIT 1;


-- Problem 6.

-- a.
SELECT tic
FROM Stocks2016.fnd
ORDER BY netinc DESC
LIMIT 1;

-- b. 
SELECT tic
FROM Stocks2016.fnd
WHERE fyear = '2011'
ORDER BY netinc DESC
LIMIT 1; 

-- c.
SELECT tic
FROM Stocks2016.fnd
ORDER BY netinc ASC
LIMIT 1; 

-- d. 
SELECT tic
FROM Stocks2016.fnd
WHERE fyear = '2011'
ORDER BY netinc ASC
LIMIT 1; 

-- e.
SELECT tic
FROM Stocks2016.fnd
WHERE emp > 1000 
ORDER BY netinc / emp DESC
LIMIT 1;

-- f.
SELECT tic, emp
FROM Stocks2016.fnd
WHERE emp != 0  AND netinc / emp  > 1
ORDER BY emp DESC
LIMIT 1;

