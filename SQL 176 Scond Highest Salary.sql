-- https://www.bilibili.com/video/BV1Xa4y1n7Dh/?spm_id_from=333.337.search-card.all.click&vd_source=eae2c885960bda71fb3bd248c305cdbf

SELECT Salary
FROM Employee
ORDER BY Salary DESC
LIMIT 1 OFFSET 1;

SELECT a.Salary
FROM
(
SELECT Salary, dense_rank() OVER (Order BY Salary DESC) AS SalaryRank
FROM Employee
) a
WHERE SalaryRank = 2