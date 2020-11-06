SELECT 
SQLDnD.Character.characterName,
SQLDnD.Race.raceName 

FROM SQLDnD.Character
JOIN SQLDnD.Race ON SQLDnD.Character.Race_idRace = SQLDnD.Race.idRace
ORDER BY SQLDnD.Character.characterName DESC
;