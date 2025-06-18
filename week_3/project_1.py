# Girls Data
girls = ["Evelyn", "Jessica", "Somto", "Edith", "Liza", "Madonna", "Waje", "Tola", "Aisha", "Latifa"]
g_ages = [17,16,17,18,16,18,17,20,19,17]
g_heights = [5.5,6.0,5.4,5.9,5.6,5.5,5.6,6.1,6.0,5.5]
g_scores = [80,85,70,66,70,66,68,77,95,50]

# Boys Data
boys = ["Chinedu", "Liam", "Wale", "Gbenga", "Abiola", "Kola", "Kunle", "George", "Thomas", "Wesley"]
b_ages = [19,16,18,17,20,19,16,18,17,19]
b_heights = [5.7,5.9,5.8,6.1,5.9,5.5,6.1,5.4,5.8,5.7]
b_scores = [74,87,75,68,66,78,87,98,54,60]

print("Name\t\tAge\tHeight\tScore")
print("-" * 40)

# Print girls
for i in range(10):
    print(f"{girls[i]:<10}\t{g_ages[i]}\t{g_heights[i]}\t{g_scores[i]}")

# Print boys
for i in range(10):
    print(f"{boys[i]:<10}\t{b_ages[i]}\t{b_heights[i]}\t{b_scores[i]}")
