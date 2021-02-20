'''UUID:

uuid1() may compromise privacy since it creates a UUID containing the computer’s network address. uuid4() creates a random UUID.

Depending on support from the underlying platform, uuid1() may or may not return a “safe” UUID. A safe UUID is one which is generated using synchronization methods that ensure no two processes can obtain the same UUID. All instances of UUID have an is_safe attribute which relays any information about the UUID’s safety, using this enumeration.

Comparison of UUID objects are made by way of comparing their UUID.int attributes. Comparison with a non-UUID object raises a TypeError

str(uuid) returns a string in the form 12345678-1234-5678-1234-567812345678 where the 32 hexadecimal digits represent the UUID.

UUID instances have these read-only attributes'''

'''
Time Stamp

floating point number
when dealing with Python time, we are considering a period of time identified by a starting point. In computing, this starting point the epoch.
The number you get on your machine may be very different because the reference point considered to be the epoch may be very different.
To see the current time represented as a string. To do so, you can pass the number of seconds you get from time() into time.ctime().


The string representation of time, also known as a timestamp, returned by ctime() is formatted with the following structure:
1. Day of the week: Mon (Monday)
2. Month of the year: Feb (February)
3. Day of the month: 25
4. Hours, minutes, and seconds using the 24-hour clock notation: 19:11:59
5. Year: 2019
'''

'''
MD5 hash in Python

Advantages:
hashes used in digital signatures
message authentication codes, manipulation detection, fingerprints, checksums (message integrity check), hash tables, password storage etc..
They are also used in sending messages over network for security or storing messages in databases.
Functions  :
* encode() : Converts the string into bytes to be acceptable by hash function.
* digest() : Returns the encoded data in byte format.
* hex-digest() : Returns the encoded data in hexadecimal format.
'''