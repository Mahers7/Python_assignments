def count_digits(text):
   # counter = [0,0,0,0,0,0,0,0,0,0]
   counter = [0] * 10
   print(text)
   for ch in text:
       print(ch)
       counter[int(ch)] += 1
   return counter


def main():
    text = "12341"
    digits = count_digits(text)

    print(digits)

main()
