# Задача 1. Представлен список из значений "Xiaomi Redmi Note 10S", "Смартфон Xiaomi Redmi Note 10 Pro",
# "Apple iPhone 13", "Apple iPhone 11", "Huawei nova Y70", "Смартфон Apple iPhone 13 Pro".
# Необходимо создать новый список, содержащий модели бренда Apple.

# Option1

list_of_phones = ["Xiaomi Redmi Note 10S", "Смартфон Xiaomi Redmi Note 10 Pro", "Apple iPhone 13", "Apple iPhone 11",
                  "Huawei nova Y70", "Смартфон Apple iPhone 13 Pro"]
apple_models = []
other_models = []
for i in range(len(list_of_phones)):
    if "apple" in list_of_phones[i].lower():
        apple_models.append(list_of_phones[i])
    else:
        other_models.append(list_of_phones[i])
print(f'Apple_models: {apple_models}')
print(f'Other_models: {other_models}')

# Option2

apple_models = [model for model in list_of_phones if "apple" in model.lower()]
print(f'Apple_list_generation: {apple_models}')


