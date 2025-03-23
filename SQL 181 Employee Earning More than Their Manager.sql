-- https://www.bilibili.com/video/BV1ZZ4y1c7YJ/?spm_id_from=333.337.search-card.all.click&vd_source=eae2c885960bda71fb3bd248c305cdbf

SELECT a.Name
(
SELECT e1.Name e1.Salary, e2.Salary AS m_salary
FROM Employee as e1
LEFT JOIN Employee AS e2
ON e1.ManagerId = e2.Id
) AS a
WHERE a.Salary > a.m_salary;