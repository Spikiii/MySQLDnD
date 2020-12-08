SELECT
SQLDnD.Player.playerName,
SQLDnD.Item.itemName,
SQLDnD.Item.itemDescription
FROM SQLDnD.Player
JOIN SQLDnD.Character ON SQLDnD.Player.idPlayer = SQLDnD.Character.Player_idPlayer
JOIN SQLDnD.Character_has_Item ON SQLDnD.Character.idCharacter = SQLDnD.Character_has_Item.Character_idCharacter
JOIN SQLDnD.Item ON SQLDnD.Character_has_Item.Item_idItem = SQLDnD.Item.idItem
WHERE Player.playerName = "Eytan"
;