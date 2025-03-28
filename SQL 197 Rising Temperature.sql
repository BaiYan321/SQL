-- https://www.bilibili.com/video/BV11U4y1L7SE?spm_id_from=333.788.recommend_more_video.2&vd_source=eae2c885960bda71fb3bd248c305cdbf

SELECT
  a.id
FROM
  (
    SELECT
      Id,
      DATE,
      temperature,
      lag(temperature, 1) OVER (ORDER BYrecoredDate) AS previous_temp
    FROM
      weather
  ) AS a
WHERE
  a.previous_temp < a.temperature;