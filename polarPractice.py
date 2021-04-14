
import numpy as np
import matplotlib.pyplot as plt
import polarcodes as pc


# initialise polar code
myPC = pc.PolarCode(256, 100)
myPC.construction_type = 'bb'

# mothercode construction
design_SNR  = 5.0
pc.Construct(myPC, design_SNR)
print(myPC, "\n\n")

# set message
my_message = np.random.randint(2, size=myPC.K)
myPC.set_message(my_message)
print("The message is:", my_message)

# encode message
pc.Encode(myPC)
print("The coded message is:", myPC.get_codeword())

# transmit the codeword
pc.AWGN(myPC, design_SNR)
print("The log-likelihoods are:", myPC.likelihoods)

# decode the received codeword
pc.Decode(myPC)
print("The decoded message is:", myPC.message_received)




