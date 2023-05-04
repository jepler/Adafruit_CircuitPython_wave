# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2023 Jeff Epler for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense

import adafruit_wave

with adafruit_wave.open("sample.wav") as w:
    print(w.getsampwidth())
    print(w.getnchannels())
    print(w.getcomptype())
    print(list(memoryview(w.readframes(100)).cast('h')))
