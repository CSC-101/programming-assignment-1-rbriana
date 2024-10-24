import data
import hw1
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel_count1(self):
        word = "Hi "
        result = hw1.vowel_count(word)
        expected = 1
        self.assertEqual(expected, result)

    def test_vowel_count2(self):
        word = "ew"
        result = hw1.vowel_count(word)
        expected = 1
        self.assertEqual(expected, result)

    # Part 2
    def test_short_lists1(self):
        result = hw1.short_lists([[2,3], [1], [4,5]])
        self.assertEqual(result, [[2,3], [4,5]])

    # Part 3
    def test_ascending_pairs(self):
        result = hw1.ascending_pairs([[2,1], [4,5], [1,2,3]])
        self.assertEqual(result, [[1,2], [4,5], [1,2,3]])
    # Part 4
    def test_add_prices(self):
        p1 = data.Price(2,75)
        p2 = data.Price(1,50)
        result = hw1.add_price(p1, p2)
        self.assertEqual(result, data.Price(4,25))


    # Part 5
    def test_rectangle_area(self):
        rectang = data.Rectangle(data.Point(0,0), data.Point(4,4))
        result = hw1.rectangle_area(rectang)
        self.assertEqual(result, 8)

    # Part 6
    def test_books_by_author(self):
        books = [data.Book("Author1", "Title1"), data.Book("Author2", "Title2")]
        result = hw1.books_by_author("Author1", books)
        self.assertEqual(result, [data.Book("Author1", 'Title1')])

    def test_books_by_author(self):
        books = [data.Book("Author1", "Title1"), data.Book("Author2", "Title2")]
        result = hw1.books_by_author([])
        self.assertEqual(result,[])
    # Part 7
    def test_circle_bound(self):
        rectang = hw1.data.Rectangle(data.Point(0, 0), data.Point(3,4))
        result = hw1.circle_bound(rectang)
        self.assertAlmostEqual(result.radius, 2.5)

# Part 8
    def test_below_pay_average(self):
        employees = [data.Employee("Ally", 5000), data.Employee("Billy", 60000)]
        result = hw1.below_pay_average(employees)
        self.assertEqual(result, ["Ally"])




if __name__ == '__main__':
    unittest.main()
