import sys
sys.path.append('./')
import devices.icb.disp.dispbios
import devices.icb.gc.gcbios
import devices.icb.netapt.netaptbios
import devices.icb.ram.rambios
import devices.icb.sb.sbbios
import devices.icb.sc.sc
import firmware.bootmod
#----------------------#
if __name__ =='__main__':
    devices.icb.disp.dispbios
    devices.icb.gc.gcbios
    devices.icb.netapt.netaptbios
    devices.icb.ram.rambios
    devices.icb.sb.sbbios
    devices.icb.sc.sc
    firmware.bootmod