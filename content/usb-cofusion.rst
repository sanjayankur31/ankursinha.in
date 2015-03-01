USB cofusion
############
:date: 2009-05-17 10:17
:author: ankur
:category: FOSS
:tags: Fedora 10, linux, USB
:tags: Fedora 10, linux, USB
:tags: Fedora 10, linux, USB
:tags: Fedora 10, linux, USB
:slug: usb-cofusion

My USB ports have been working slow. Really slow.. The speeds even
decrease to KB/s while copying to flash disks.. I was looking for a
solution.. I checked the specs `here`_ and this is the output from lshw
(the USB part).

From what I understand in the output.. My USB ports are listed as having
1.10 capabilities. The specs however show them as USB 2 ports. Why is
this happening? BUG ?? Need to dig up more to get to the bottom of this.

| \*-usb:0
|  description: USB Controller
|  product: 82801G (ICH7 Family) USB UHCI Controller #1
|  vendor: Intel Corporation
|  physical id: 1d
|  bus info: pci@0000:00:1d.0
|  version: 02
|  width: 32 bits
|  clock: 33MHz
|  capabilities: uhci bus\_master
|  configuration: driver=uhci\_hcd latency=0
|  resources: irq:23 ioport:1800(size=32)

| \*-usbhost
|  product: UHCI Host Controller
|  vendor: Linux 2.6.27.21-170.2.56.fc10.x86\_64 uhci\_hcd
|  physical id: 1
|  bus info: usb@2
|  logical name: /dev/usb2
|  version: 2.06
|  **capabilities: usb-1.10**
|  configuration: driver=hub slots=2 speed=12.0MB/s

| \*-usb:1
|  description: USB Controller
|  product: 82801G (ICH7 Family) USB UHCI Controller #2
|  vendor: Intel Corporation
|  physical id: 1d.1
|  bus info: pci@0000:00:1d.1
|  version: 02
|  width: 32 bits
|  clock: 33MHz
|  capabilities: uhci bus\_master
|  configuration: driver=uhci\_hcd latency=0
|  resources: irq:19 ioport:1820(size=32)

| \*-usbhost
|  product: UHCI Host Controller
|  vendor: Linux 2.6.27.21-170.2.56.fc10.x86\_64 uhci\_hcd
|  physical id: 1
|  bus info: usb@3
|  logical name: /dev/usb3
|  version: 2.06
|  **capabilities: usb-1.10**
|  configuration: driver=hub slots=2 speed=12.0MB/s

| \*-usb:2
|  description: USB Controller
|  product: 82801G (ICH7 Family) USB UHCI Controller #3
|  vendor: Intel Corporation
|  physical id: 1d.2
|  bus info: pci@0000:00:1d.2
|  version: 02
|  width: 32 bits
|  clock: 33MHz
|  capabilities: uhci bus\_master
|  configuration: driver=uhci\_hcd latency=0
|  resources: irq:18 ioport:1840(size=32)

| \*-usbhost
|  product: UHCI Host Controller
|  vendor: Linux 2.6.27.21-170.2.56.fc10.x86\_64 uhci\_hcd
|  physical id: 1
|  bus info: usb@4
|  logical name: /dev/usb4
|  version: 2.06
|  **capabilities: usb-1.10**
|  configuration: driver=hub slots=2 speed=12.0MB/s

| \*-usb
|  description: Bluetooth wireless interface
|  product: HP Integrated Module
|  vendor: Broadcom Corp
|  physical id: 2
|  bus info: usb@4:2
|  version: 1.00
|  capabilities: bluetooth usb-2.00
|  configuration: driver=btusb speed=12.0MB/s

| \*-usb:3
|  description: USB Controller
|  product: 82801G (ICH7 Family) USB UHCI Controller #4
|  vendor: Intel Corporation
|  physical id: 1d.3
|  bus info: pci@0000:00:1d.3
|  version: 02
|  width: 32 bits
|  clock: 33MHz
|  capabilities: uhci bus\_master
|  configuration: driver=uhci\_hcd latency=0
|  resources: irq:16 ioport:1860(size=32)

| \*-usbhost
|  product: UHCI Host Controller
|  vendor: Linux 2.6.27.21-170.2.56.fc10.x86\_64 uhci\_hcd
|  physical id: 1
|  bus info: usb@5
|  logical name: /dev/usb5
|  version: 2.06
|  **capabilities: usb-1.10**
|  configuration: driver=hub slots=2 speed=12.0MB/s

| \*-usb:4
|  description: USB Controller
|  product: 82801G (ICH7 Family) USB2 EHCI Controller
|  vendor: Intel Corporation
|  physical id: 1d.7
|  bus info: pci@0000:00:1d.7
|  version: 02
|  width: 32 bits
|  clock: 33MHz
|  capabilities: pm debug ehci bus\_master cap\_list
|  configuration: driver=ehci\_hcd latency=0
|  resources: irq:23 memory:de304000-de3043ff

| \*-usbhost
|  product: EHCI Host Controller
|  vendor: Linux 2.6.27.21-170.2.56.fc10.x86\_64 ehci\_hcd
|  physical id: 1
|  bus info: usb@1
|  logical name: /dev/usb1
|  version: 2.06
|  capabilities: usb-2.00
|  configuration: driver=hub slots=8 speed=480.0MB/s

| \*-usb UNCLAIMED
|  description: Video
|  vendor: Ricoh Co., Ltd
|  physical id: 4
|  bus info: usb@1:4
|  version: 1.00
|  capabilities: usb-2.00
|  configuration: maxpower=100mA speed=480.0MB/s

::

.. _here: http://www.rjesh.com/2007/04/hp-pavilion-dv6226tx-detailed.html
