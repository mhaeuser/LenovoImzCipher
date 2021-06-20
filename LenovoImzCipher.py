## @file
#  Applies the Lenovo IMZ cipher to cleartext passwords.
#  
#  Copyright (C) 2021 Marvin Häuser. All rights reserved.
#  SPDX-License-Identifier: BSD-3-Clause
#
##

#
# REF: https://thinkpad-forum.de/threads/45475-recovery-zip-archives-passwort
#

PwChars = "k`gybs0vampjd"

Password = input("Original password: ")

print("Ciphered password: ", end = '')
for i in range(len(Password)):
  print(chr(ord(PwChars[ord(Password[i]) % 13]) - (i % 3) + 2), end = '')
print("")
