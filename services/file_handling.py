from re import search, S

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    reg = search(r".*[,.!:;?]", text[start:start+PAGE_SIZE], S).group(0)
    if reg[-2:] == '?.':
        reg = search(r"(.*[,.!:;?]).*\?\.$", reg).group(1)
    return reg, len(reg)


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(path, encoding="utf-8") as f:
        start, c = 0, 1
        text = f.read()

        while True:
            try:
                book[c] = _get_part_text(text, start, PAGE_SIZE)[0].lstrip()
                start += _get_part_text(text, start, PAGE_SIZE)[1]
                c += 1
            except:
                break


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(BOOK_PATH)