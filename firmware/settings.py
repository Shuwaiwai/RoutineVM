#==================BOOT==================#
SecureBoot=True
#This option enables secure boot.
#(but has an impact on some operating systems.)
EFI=True
#This option enables EFI environment.
bootmode="singleboot"
#This option can change the boot mode(Boot 1st option only)
#To single-system boot when "singleboot";
#Multi-system boot when "multiBoot".
bootopn1st="./devices/sata/satadri01/00/BOOT/Bootrv64.py"
bootopn2nd=""
bootopn3rd=""
bootopn4th=""
#The above is the boot sequence at boot
#Available only in multi-system boot mode
#The boot file is a *.py file

#==================DEVICES==================#
hostVMswap=True