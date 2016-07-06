import usb.core
import usb.util

dev = usb.core.find()

for device in dev
    print device

