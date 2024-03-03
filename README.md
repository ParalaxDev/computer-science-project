# Will Baker Computer Science Coursework

## Testing

If you dont have an X32, you can either use the X32 Simulator by Patrick-Gilles Maillot which you can download [here](https://sites.google.com/site/patrickmaillot/x32#h.p_rE4IH0Luimc0), or simply observe the packets being sent using the Wireshark filter:

`ip.src == 127.0.0.1 and udp and ip.dst == 127.0.0.1 and not icmp`

## Pseudocode

```py
procedure createAccount(username, password)
    hash = hashPassword(password)
    allUsernames = getUsernames() # This function will read any saved usernames from a file
    for name in allUsernames
        if username == name:
            error("An account already exists with that username")
        endif
    endfor
    if username.length < 1 and username.length > 8
        error("A Username should be between 8 and 1 characters" )
    else if password.length > 8
        error("The password should be between 8 and 1 characters" )
    else if password contains [0-9]
        error("The password should contain a number" )
    else if password contains [A-Z]
        error("The password should contain a capital letter" )
    else if password contains [$&+,:;=?@#|<>.^*()%!-]
        error("The password should contain a symbol" )
    else if password.length < 0
        error("The password should contain a symbol" )
    else
        saveUsername(username, hash) # This function will save the provided user details to a file
    endif
endprocedure
```

```py
function checkPassword(username, password)
    hash = hashPassword(password)
    correctHash = getHashedPassword(username) # This function will get the hash password associated with a username from a file. If the username doesn't exist then it will return an empty string.

    if correctHash == ""
        error("There is no account with that name. Please try again")
        return False
    else
        if correctHash == hash:
            return True
        else:
            return False
```

```py
function createOSCMessage(message, args) # args is a 2D array, where the first item contains the type of the value, and the second is the value
    typeString = ""
    valueArray = b[] # this represents an array of bytes

    for arg in args
        type = arg[0]
        val = arg[1]

        typeString.append(type)
        if type == "f"
            valueArray.append(convertFloatToBigEndian(val)) # This function will take a float and return it in bytes
        else if type == "i"
            valueArray.append(convertIntToBigEndian(val)) # This function will take an integer and return it in bytes
        else if type == "s"
            valueArray.append(convertStringToBytes(val)) # This function will take a string and convert it to bytes using ascii encoding, and ensure the string is correctly zero padded
        else
            error("There was an error creating the OSC message")

    return (message, typeString, valueArray)
```

```py
function decodeMessage(data) # data is the raw hex data recieved straight from the socket
    message = parseMsgFromData(data) # This function will split the raw data by the correct delimiter (a comma), strip any empty characters from the first half and return the string

    datagram = parseDgramFromData(data) # This function will split the raw data by the correct delimiter (a comma), and return a byte string for all the data, minus the message

    typetag, index = getStringFromDgram(dgram, 0) # This function will return the first string it encounters in the datagram from the index 0. It will return this string and then the index of the next byte. This allows us to continue parsing from this point

    params = ()

    for type in typetag
        if type == "i":
            val, index = getIntFromDgram(dgram, index) # This function will return the first big endian integer. It will return this and then the index of the next byte. This allows us to continue parsing from this point
        else if type == "f":
            val, index = getFloatFromDgram(dgram, index) # This function will return the first big endian float. It will return this and then the index of the next byte. This allows us to continue parsing from this point
        else if type == "s":
            val, index = getStringFromDgram(dgram, index) # This function will return the first string it encounters in the datagram from the index 0. It will return this string and then the index of the last byte in the string. This allows us to continue parsing from this point
        else if type == "b":
            val, index = getBlobFromDgram(dgram, index) # Each blob in the OSC spec starts with an integer to gauge the length of it. This function will parse that integer, and then return the next x bytes of data as a byte string.
        else:
            error("There is an error in the recieved message, there is an unknown or unsupported type")
            val, index = b'x00', index
        endif
        params.append(val)
    endfor
    return (message, params)
```

```py
procedure sendData(message, typeString, valueArray) # this is the data formatted as though the function createOSCMessage was called
    if not message.startsWith('/'):
        error("The message is not valid as it doesn't start with a /")
    endif

    formattedMessage = bytes(message + "," + typeString, "ascii") + valueArray # The bytes function takes a string and a character set and returns it in bytes.

    try:
        sendBytes(formattedMessage, IP, PORT) # The send bytes function will interact with a socket, and send the bytes passed as a parameter. It also takes in the IP and PORT to send the bytes to.
    except:
        error("An error occured while sending the following message:", message)
    endcatch
```

```py
function decodeMeterBlob(data):
    index = 0
    meterVals = []

    for i in range(count):
        value, pos = getLittleEndianFloatFromDgram(data, index)
        meterVals.append(value)

    return meterVals
```

```py
procedure listenToSocketThread()
    while True:
        data = receiveDataFromNetwork() # This function will return data received from the socket. The function is blocking, so the code won't continue until data is recieved.

        message, value = decodeMessage(data)

        rootMessage = message.split('/')[0] # All osc messages are sperated into different sections with a slash. Different sections require different processing

        if rootMessage == "meters"
            decodeMeterBlob(data)
        else if rootMessage == "xremote"
        else
            index = findMessageInExpectedQueue(message) # This function will return an index of where the message is in the queue. If it is not found it will return -1

            if index >= 0
                removeMessageFromExpectedQueue(index) # This will remove the item from the queue

                addToResultQueue(message, value) # This function will add the values to a dictionary and then to a queue to send the data out of the thread and back to the original caller of the function.
```
