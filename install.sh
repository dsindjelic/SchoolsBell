echo "install package requirements"
echo "sudo apt-get install gcc"
sudo apt-get install gcc
echo "sudo apt-get install libusb++-dev"
sudo apt-get install libusb++-dev

echo "make"
cd commandline/makemake
make
echo "copying bin files"
sudo cp hidusb-relay-cmd /usr/bin
echo "done"
echo "Usage"
echo ""
echo "\thidusb-relay-cmd on <num>  - turn relay <num> ON"
echo "\thidusb-relay-cmd off <num> - turn relay <num> OFF"
echo "\thidusb-relay-cmd state     - print states of the relays"
echo "\thidusb-relay-cmd enum      - print state of all found relay devices"
echo ""
echo "Parameter ID=XXXXX selects one device if several are connected"
echo "Example: hidusb-relay-cmd ID=ABCDE ON 2"








