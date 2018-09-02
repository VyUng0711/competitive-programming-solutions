user_dict = dict()
logged_in = dict()
def register(username, password):
  if username in user_dict:
    print("fail: user already exists")
  else:
    print("success: new user added")
    user_dict[username] = password

def login(username, password):
  if username not in user_dict:
    print("fail: no such user")
  else:
    if user_dict[username] != password:
      print("fail: incorrect password")
    else:
      if logged_in.get(username):
        print("fail: already logged in")
      else:
        print("success: user logged in")
        logged_in[username] = True
        

def logout(username):
  if username not in user_dict:
    print("fail: no such user")
  else:
    if logged_in.get(username):
      print("success: user logged out")
      logged_in[username] = False
    else:
      print("fail: already logged out")
      
  
n = int(input())
for i in range(n):
  op = input().split()
  if op[0] == "register":
    register(op[1], op[2])
  elif op[0] == "login":
    login(op[1], op[2])
  elif op[0] == "logout":
    logout(op[1])
