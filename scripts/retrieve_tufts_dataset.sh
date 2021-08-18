# Retrieves and downloads the IR/RGB images of the Tufts Face dataset

# If lftp is not installed, uncomment the following:
# sudo apt update
# sudo apt install lftp

# Retrieve and download data in current working directory
lftp -c 'mirror --parallel=100 http://tdface.ece.tufts.edu/downloads/TD_IR_RGB_CROPPED/ ;exit'
