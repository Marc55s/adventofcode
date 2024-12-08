from lib import *

input = read_input(2024, 5).strip()
input = input.split("\n")
input.remove('')
rules = [x for x in input if "|" in x]
updates = [x for x in input if "," in x]
ordering = {}
for r in rules:
    x, y = r.split("|")
    if x in ordering.keys():
        ordering[x].append(y)
    else:
        ordering[x] = [y]


def is_page_before_others(page, others, modifylist=[]):
    for afterpage in others:
        # either nothings comes after page or other is not comiing after page
        if page not in ordering.keys():
            return False
        if afterpage not in ordering[page]:
            return False
    return True


def is_page_after_others(page, others):
    for beforepage in others:
        if beforepage not in ordering.keys():
            return False
        if page not in ordering[beforepage]:
            return False
    return True


def check_update(pages) -> bool:
    # print(pages)
    for page in pages:
        index = pages.index(page)
        pages_before_current = pages[0:index]
        pages_after_current = pages[index+1:len(pages)]
        if not is_page_after_others(page, pages_before_current) or not is_page_before_others(page, pages_after_current):
            return False
    return True



def p2(pages):
    pages_copy = pages.copy()
    while not check_update(pages_copy):
        for page in pages_copy:
            index = pages_copy.index(page)
            b = pages_copy[0:index]
            a = pages_copy[index+1:len(pages_copy)]
            for beforepage in b:
                if beforepage not in ordering.keys():
                    # on of the beforepage is not followed by anything -->  move beforepage to the end
                    pages_copy.remove(beforepage)
                    pages_copy.append(beforepage)
                    break
                if page not in ordering[beforepage]:
                    # one of the beforepage is not followed by page --> move beforepage behind page
                    pages_copy.remove(beforepage)
                    pages_copy.insert(pages_copy.index(page), beforepage)
            for afterpage in a:
                if page not in ordering.keys():
                    # page should be last --> move page to end
                    pages_copy.remove(page)
                    pages_copy.append(page)
                    break
                if afterpage not in ordering[page]:
                    # a member of the rest is not after page --> move afterpage before page
                    pages_copy.remove(afterpage)
                    pages_copy.insert(pages_copy.index(page)-1, afterpage)
    return pages_copy


sum = 0
incorrect = []
for update in updates:
    update = update.split(",")
    if check_update(update):
        sum += int(update[len(update)//2])
    else:
        incorrect.append(update)

print("part 1 =", sum)

ans2 = 0
for inc in incorrect:
    corrected = p2(inc)
    ans2 += int(corrected[len(corrected)//2])

print("part 2 =", ans2)
