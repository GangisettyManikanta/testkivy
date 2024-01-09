import anvil.server

anvil.server.connect("server_O45LTWVVBIYCUGCNAADCA3XV-3JAGBBHZT5YXO5WX")
@anvil.server.callable
def name(email,password):
    user_info = []
    user_info.append(email)
    user_info.append(password)
    print(user_info)
    return user_info

anvil.server.wait_forever()