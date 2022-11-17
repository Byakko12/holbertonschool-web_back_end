-- lists bands with Glam rock as their main style
-- Ranked by how long they have been playing
SELECT band_name, (IFNULL(split, 2020) - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%';