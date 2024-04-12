# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
'const.py'
'
This class helps to create constant variables similar to 'typing.Final'
construct (available in versions >= 3.8.*).

(evoai_app.helper.const.py)

Copyright (c) 2016-2022 EncoreSky Ltd. All rights reserved.
"""

import sys

class _const:
    """Create a constant variable by setting a class attribute for a given variable
       name at the first assingement statement and then raising an exception when
       tried to modify it. Using objects's (_const class object) internal dictionary
       used to store object’s (writable) attributes.

    Raises:
        self.ConstError: The variable has already a value assigned
    """
    class ConstError(TypeError):
        """Raise if a class attribute, used as an constant variable, has already
        a reference to an object"""

    def __setattr__(self, name, value):
        if name in self.__dict__.keys():
            raise self.ConstError("Can't rebind const({})".format(name))
        self.__dict__[name] = value

sys.modules[__name__]=_const()
