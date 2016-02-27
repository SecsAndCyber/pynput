# coding=utf-8
# pynput
# Copyright (C) 2015-2016 Moses Palmér
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import os
import sys

if os.environ.get('__PYNPUT_GENERATE_DOCUMENTATION') == 'yes':
    from ._base import Button, Controller, Listener
else:
    Button = None
    Controller = None
    Listener = None


if sys.platform == 'darwin':
    if Controller is None and Listener is None:
        from ._darwin import Button, Controller, Listener

elif sys.platform == 'win32':
    if Controller is None and Listener is None:
        from ._win32 import Button, Controller, Listener

else:
    if Controller is None and Listener is None:
        try:
            from ._xorg import Button, Controller, Listener
        except:
            pass


if not Button or not Controller or not Listener:
    raise ImportError('this platform is not supported')
