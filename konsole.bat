@echo off
if %1 == python3 (
    python 3py.py
)
if %1 == python2 (
    python 2py.py
    )
if %1 == node (
    python node.py
)
if %1 == bash (
    python bash.py
    )
@echo on
