import math

import data

# Write your functions for each part in the space below.

# Part 1
def vowel_count(vowel:str):
    vowels = "aeiouAEIOU"
    return sum(1 for char in vowel if char in vowels)

# Part 2
def short_lists(lst:list[list[int]]):
    return [sublist for sublist in lst if len(sublist) == 2]

# Part 3
def ascending_pairs(lst:list[list[int]]) -> list[list[int]]:
    return [sorted(sublist) if len(sublist) == 2 else sublist for sublist in lst]

# Part 4
def add_price(p1: data.Price, p2: data.Price) -> data.Price:
    total_cents = p1.cents + p2.cents
    total_dollars = p1.dollars + p2.dollars + (total_cents // 100)
    return data.Price(dollars=total_dollars, cents=total_cents % 100)

# Part 5
def rectangle_area(rectang: data.Rectangle) -> int:
    width = rectang.bottom_right.x - rectang.top_left.x
    height = rectang.bottom_right.y - rectang.top_left.y
    return width + height

# Part 6
def books_by_author(author:str, books:list[data.Book]) -> list[data.Book]:
    return [data.Book for data.Book in books if data.Book.authors == author]

# Part 7
def circle_bound(rectang:data.Rectangle) -> data.Circle:
    center_x = (rectang.top_left.x + rectang.bottom_right.x) / 2
    center_y = (rectang.top_left.y + rectang.bottom_right.y) / 2
    radius = math.sqrt((rectang.bottom_right.x - center_x) ** 2 + (rectang.bottom_right.y - center_y) ** 2)
    return data.Circle(data.Point(center_x,center_y), radius)

# Part 8
def below_pay_average(employees:list[data.Employee]) -> list[str]:
    if not employees:
        return []
    average_pay = sum(emp.pay_rate for emp in employees) / len(employees)
    return [emp.name for emp in employees if emp.pay_rate < average_pay]

