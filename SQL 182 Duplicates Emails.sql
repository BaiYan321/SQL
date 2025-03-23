-- https://www.bilibili.com/video/BV1ZZ4y1c7YJ/?spm_id_from=333.337.search-card.all.click&vd_source=eae2c885960bda71fb3bd248c305cdbf

-- Method 1
SELECT a.email
FROM
(
    SELECT email, count(email) AS occurance
    FROM Person
    GROUP BY email
) AS a
WHERE a.occurance > 1;

-- Method 2
SELECT email
FROM Person
GROUP BY email
Having count(1)>1