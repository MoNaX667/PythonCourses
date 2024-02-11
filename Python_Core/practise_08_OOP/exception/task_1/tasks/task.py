class Pagination:
    def __init__(self, data, items_on_page):
        self.data = []
        char_counter = 0
        page = ""
        for char in data:
            if char_counter < items_on_page:
                page += char
                char_counter += 1
            else:
                char_counter = 1
                self.data.append(page)
                page = char
                continue

        self.data.append(page)
        self.items_on_page = items_on_page

    @property
    def page_count(self):
        return len(self.data)

    @property
    def item_count(self):
        return sum(len(elem) for elem in self.data)

    def count_items_on_page(self, page_number):
        try:
            if page_number >= len(self.data):
                raise IndexError("Invalid index. Page is missing.")
            else:
                return len(self.data[page_number])
        except IndexError as e:
            print(str(e))

    def find_page(self, search_term):
        result_page_set = []
        for i, elem in enumerate(self.data):
            if str(elem).__contains__(search_term):
                result_page_set.append(i)

        if len(result_page_set) <= 0:
            raise ValueError(f"'{search_term}' is missing on the pages")

        return result_page_set

    def display_page(self, page_number):
        try:
            return self.data[page_number]
        except IndexError:
            raise IndexError("Invalid index. Page is missing.")
