girls = ["Evelyn", "Jessica", "Somto", "Edith", "Liza", "Madonna", "Waje", "Tola", "Aisha", "Latifa"]

g_ages = [17, 16, 17, 18, 16, 18, 17, 20, 19, 17]
g_heights = [5.5, 6, 5.4, 5.9, 5.6, 5.5, 6.1, 6, 5.7, 5.5]
g_scores = [80, 85, 70, 60, 76, 66, 87, 95, 50, 49]

boys = ["Chinedu", "Liam", "Wale", "Gbenga", "Abiola", "Kola", "Kunle", "George", "Thomas", "Wesley"]
b_ages = [19, 16, 18, 17, 20, 19, 16, 18, 17, 19]
b_heights = [5.7, 5.9, 5.8, 6.1, 5.9, 5.5, 6.1, 5.4, 5.8, 5.7]
b_scores = [74, 87, 75, 68, 66, 78, 87, 98, 54, 60]

print("Name | Age | Height | Score")

for i in range(len(girls)):
  print(girls[i], "|", g_ages[i], "|", g_heights[i], "|", g_scores[i])

for i in range(len(boys)):
  print(boys[i], "|", b_ages[i], "|", b_heights[i], "|", b_scores[i])