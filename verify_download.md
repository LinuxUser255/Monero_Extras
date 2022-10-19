## Get the developer's .asc signature file

```
wget -O binaryfate.asc https://raw.githubusercontent.com/monero-project/monero/master/utils/gpg_keys/binaryfate.asc
```


## Verify signing key finger print matches:
```
gpg --keyid-format long --with-fingerprint binaryfate.asc
gpg: WARNING: no command supplied.  Trying to guess what you mean ...
pub   rsa4096/F0AF4D462A0BDF92 2019-12-12 [SCEA]
      Key fingerprint = 81AC 591F E9C4 B65C 5806  AFC3 F0AF 4D46 2A0B DF92
uid                           binaryFate <binaryfate@getmonero.org>
sub   rsa4096/2593838EABB1F655 2019-12-12 [SEA]

match:  F0AF4D462A0BDF92   F0AF 4D46 2A0B DF92
```

## Import his signing key
```
gpg --import binaryfate.asc
```

## If this is the first time you have imported the key, the output will look like this:
```
gpg: key F0AF4D462A0BDF92: 2 signatures not checked due to missing keys
gpg: key F0AF4D462A0BDF92: public key "binaryFate <binaryfate@getmonero.org>" imported
gpg: Total number processed: 1
gpg:               imported: 1
gpg: marginals needed: 3  completes needed: 1  trust model: pgp
```
## If you have imported the key previously, the output will look like this:
```
gpg: key F0AF4D462A0BDF92: "binaryFate <binaryfate@getmonero.org>" not changed
gpg: Total number processed: 1
gpg:              unchanged: 1

```

## Get the sha265 hashes of all the Monero wallets
```
wget -O hashes.txt https://www.getmonero.org/downloads/hashes.txt
```

## Now that you have the developer's signing key, you can verify the authenticity of the hashes file
# which he uses to sign the Monero binaries
```
gpg --verify hashes.txt
```
# In this example, I downloaded:
```
monero-gui-linux-x64-v0.18.1.2.tar.bz2
```

## There will be a SHA256 hash value of that wallety on that list

## Easy way: hash the file and output the results in a txt file for easy comparioson using grep
```
sha256sum -c hashes.txt 2>/dev/null | grep monero-gui-linux-x64-v0.18.1.2.tar.bz2
```

**Desired Output**
```
monero-gui-linux-x64-v0.18.1.2.tar.bz2: OK
```

![hash_confirm](https://user-images.githubusercontent.com/46334926/196581084-24cc9d31-4372-40d0-a063-dc4053adbd08.png)



