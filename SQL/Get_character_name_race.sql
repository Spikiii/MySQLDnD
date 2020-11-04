SELECT 
SQLDnD.Character.characterName,
SQLDnD.Race.raceName 

FROM SQLDnD.Character
JOIN SQLDnD.Character_has_Race ON SQLDnD.Character.idCharacter = SQLDnD.Character_has_Race.Character_idCharacter
JOIN SQLDnD.Race ON SQLDnD.Character_has_Race.Race_idRace = SQLDnD.Race.idRace
;