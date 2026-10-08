matrix = [[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]
print(matrix[1][2])
print(matrix[0][0])
print(matrix[2][1])

coords = {(0, 0), (1, 2), (3, 4), (1, 2)}
print(coords)
print(len(coords))

article_tags = [
{"Python", "AI"},
{"Python", "Web"},
{"AI", "ML"},
]
print(article_tags[0])
print("AI" in article_tags[1])
print(len(article_tags))

data = [
("Alice", {95, 87, 92}),
("Bob", {78, 85, 90}),
]
print(data[0][0])
print(data[1][1])
print(88 in data[0][1])