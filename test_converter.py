import converter

output = converter.convert('''

accept: */*
accept-encoding: gzip, deflate, br
accept-language: en-GB,en;q=0.9
authorization: Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA
content-length: 171
content-type: application/json
cookie: cookies
origin: https://twitter.com
referer: https://twitter.com/i/flow/signup
sec-fetch-dest: empty
sec-fetch-mode: cors
sec-fetch-site: same-origin
sec-gpc: 1
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36
x-csrf-token: 123
x-guest-token: 123
x-twitter-active-user: yes
x-twitter-client-language: en-GB

''')

print(output)