-- https://www.bilibili.com/video/BV1ZZ4y1c7YJ/?spm_id_from=333.337.search-card.all.click&vd_source=eae2c885960bda71fb3bd248c305cdbf

SELECT Name
FROM Customers
WHERE customers.Id NOT IN (SELECT UNIQUE CustomerID FROM Orders);

-- Method 2
SELECT Customers.name
FROM Customers
LEFT JOIN orders
ON customers.Id = orders.CustomerID
WHERE o.id IS NULL