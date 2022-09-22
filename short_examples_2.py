veri =   """jane made 250 calls and generated 1300 dollars last Month with an 7$ average deal size.  
ali called 12 times and Sold 4 courses generated 85 dollars last month with a 7$ average deal size.
  Hale called 500 people. Achieved success by getting 14$ average deal size, got 11500 dollars revenue.     
Micheal with 70 calls, made 2385 dollars and 22$ average deal size IN the previous month.  
   Sussan called 112 people and earned 650 dollars in REvenue and an AVERAGE DEAL SIZE of 6$ Last month.
ned called 120 people generated 780 dollars last month, his average deal size was 22$.  
Therry made 660 phone calls and generation 4250 dollars a past month 22$ average deal SIZE. 
Elish made 840 calls and generated 6300 dollars a prior mONTH and reached 38$ the average deal size. 
 Bobby made 240 phone calls, generated 820 dollars LAST MONTH and gaining 13$ average deal size.
Swift with 550 calls generated 1320 dollars in revenue pASt month, and the average deal size was 14$. 
  Juddy made 85 calls and earned 650 dollars for the company last month, her average deal size was 15$."""

# ilk önce satırları birbirinden ayırıp bir 
# listede toplayalım
dosya = open("tutorium.txt", "r")
veri = dosya.read()
satirlar = veri.splitlines()
print(satirlar)

# isimlere erişmek için her satırı kelimelerine 
# ayırabiliriz. Mesela ilk satırı kelimelerine 
# ayırmak için split() metodunu kullanalım
# kelimeleri de başka bir listede toplayalım
kelimeler = satirlar[0].split(" ")
print(kelimeler)
# kelimeler listesindeki ilk eleman isimdir.
print(kelimeler[0])


# kazanç miktarı "dollars" kelimesinden bir önceki
# kelimedir. "dollars" kelimesinin index değerini # bulduktan sonra bir önceki index değerine 
# erişerek kazanç miktarını elde edebiliriz
i = kelimeler.index("dollars")

print(kelimeler[0])
print(kelimeler[2])
print(kelimer[i-1])


# birim başına kazanılan miktar "$" işareti ile 
# birlikte yazılıyor "$" işaretinin yerini bulup 
# "$" işaretini ve varsa "." işaretini silip 
# sadece önündeki sayıya erişerebiliriz
for i in kelimeler:
  if "$" in i:
    print((i.strip(".")).strip("$"))
    
    
# şimdi bunu bütün satırlar için yapalım
for i in lines:
  kelimeler = i.split()
  k = kelimeler.index("dollars")
  print(f"{kelimeler[0]} {kelimeler[2]} {kelimeler[k-1]}", end=" ")
  for i in kelimeler:
    if "$" in i:
      print((i.strip(".")).strip("$")) 
