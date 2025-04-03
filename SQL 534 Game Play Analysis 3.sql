-- https://www.bilibili.com/video/BV1KQ4y1k7km?spm_id_from=333.788.recommend_more_video.3&vd_source=eae2c885960bda71fb3bd248c305cdbf

SELECT player_id, event_date,
    SUM(game_played) OVER (PARTITION BY player_id ORDER BY event_date ASC) AS game_played_so_far
FROM Activity