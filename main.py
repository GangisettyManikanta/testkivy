import anvil.server

anvil.server.connect("server_YF6XTXVQVNEBLCROSVZEJP7H-RFRSPJAPC6QZAPLG")

    
@anvil.server.callable
def name():
    email = "kivy@gmail.com"
    password = "kcy@123"
    users = {
        'email': email,
        'password': password
    }
    return users

anvil.server.wait_forever()