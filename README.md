# Why are you doing this?
[It's this tweet](https://twitter.com/JacksonChen666/status/1273626516971290625?s=20)

# How are you doing this?
I am using a command which takes the amount of commits, increment it, and creates a commit for nothing.

Check [command.sh](command.sh)

It calls git gc every 10000 commits to reduce the size of the commits, which can take a while. The reason i'm doing this is because it tends to pack straight in if it's too slow withpout clean up.

## Records
See [records.md](records.md) for more past records in time

### Why aren't the commits signed?
Making gpg sign all the commits is very intensive and is even faster than not signing it. Let's just say it's about 5-10x times faster because the amount of processing is just less.
