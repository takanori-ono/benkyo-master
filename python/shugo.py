# 異動で新しい係が作成されたが、新しい係はどれか探すのが大変だった。
# 集合演算の差で、無いものを見つけることができるのでは？
# A:既存の係の集合, B:新しい係を含んだ係の集合
# answer = B - A

#a = {"1234", "124", "012", "1234"}
#b = {"1234", "456", "124", "012"}
#print(b-a)

def read_file(nm):
  with open(nm, "r") as file:
    lines = file.readlines()
    # strip()がないと改行コードが入ってしまう
    return {l.strip() for l in lines}

#print(read_file("./data/old_kakaris.txt"))
old_kakaris = read_file("./data/old_kakaris.txt")
new_kakaris = read_file("./data/new_kakaris.txt")
sabun = new_kakaris - old_kakaris
{print(i) for i in sabun}