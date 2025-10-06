This one was stuck behind a paywall so I'll just write it out myself:

Basically a list of strings will be sent over a 'network', they will first be decoded in a function:

`encode(list<string>: strs) -> str`

and then decoded on the other end in a function:

`decode(str: encoded_str) -> list<str>`

to provide all the original strings.
