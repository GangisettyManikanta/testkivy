import anvil.server

anvil.server.connect("server_YF6XTXVQVNEBLCROSVZEJP7H-RFRSPJAPC6QZAPLG")

@anvil.server.callable
def name():
    return "Yarisingu"

anvil.server.wait_forever()