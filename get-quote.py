import random


def read_from_a_file():
  print("\n")
  print("running code.")

  f = open("quotes.txt") # 变量 f 打开文件 quotes.txt
  quotes = f.readlines()
  f.close()
  # last_line = len(quotes) - 1
  last_line = 13 #
  rnd = random.randint(0,last_line)

  # print(last_line)
  print(quotes[rnd])

if __name__== "__main__":
  read_from_a_file()
