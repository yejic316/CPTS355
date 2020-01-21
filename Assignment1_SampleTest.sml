fun busFinderTest () =
let    
  val buses = 
	[("Lentil",["Chinook", "Orchard", "Valley", "Emerald","Providence", "Stadium", "Main", "Arbor", "Sunnyside", "Fountain", "Crestview", "Wheatland", "Walmart", "Bishop", "Derby", "Dilke"]), 
	("Wheat",["Chinook", "Orchard", "Valley", "Maple","Aspen", "TerreView", "Clay", "Dismores", "Martin", "Bishop", "Walmart", "PorchLight", "Campus"]), 
	("Silver",["TransferStation", "PorchLight", "Stadium", "Bishop","Walmart", "Shopco", "RockeyWay"]),
	("Blue",["TransferStation", "State", "Larry", "TerreView","Grand", "TacoBell", "Chinook", "Library"]),
	("Gray",["TransferStation", "Wawawai", "Main", "Sunnyside","Crestview", "CityHall", "Stadium", "Colorado"])]
     
  val busFinderT1 = ((busFinder "Walmart" buses) = ["Lentil","Wheat","Silver"])
  val busFinderT2 = ((busFinder "Shopco" buses) = ["Silver"])
  val busFinderT3 = ((busFinder "Main" buses) = ["Lentil","Gray"])

 in 
     print ("busFinder:-------------------- \n"   ^ 
            "   test1: " ^ Bool.toString(busFinderT1) ^ "\n" ^ 
            "   test2: " ^ Bool.toString(busFinderT2) ^ "\n" ^  
            "   test4: " ^ Bool.toString(busFinderT3) ^ "\n")		
end
val _ = busFinderTest ()
